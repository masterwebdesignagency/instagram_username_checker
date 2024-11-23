import threading
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import Tk, Button, Label, Text, Scrollbar, END

class InstagramCheckerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Instagram Username Checker")
        self.is_running = False  # Çalışma durumunu kontrol eder
        self.thread = None  # Thread kontrolü için
        self.init_gui()  # GUI'yi oluştur

    def init_gui(self):
        self.label = Label(self.root, text="Instagram Kullanıcı Adı Kontrol")
        self.label.pack(pady=10)

        self.start_button = Button(self.root, text="Başlat", command=self.start_check)
        self.start_button.pack(pady=5)

        self.stop_button = Button(self.root, text="Durdur", command=self.stop_check)
        self.stop_button.pack(pady=5)

        self.result_label = Label(self.root, text="Sonuçlar:")
        self.result_label.pack(pady=10)

        self.result_box = Text(self.root, height=15, width=50)
        self.result_box.pack(pady=5)

        scrollbar = Scrollbar(self.root, command=self.result_box.yview)
        scrollbar.pack(side="right", fill="y")
        self.result_box.config(yscrollcommand=scrollbar.set)

    def start_check(self):
        if not self.is_running:
            self.is_running = True
            self.thread = threading.Thread(target=self.check_usernames)
            self.thread.start()

    def stop_check(self):
        self.is_running = False
        if self.thread:
            self.thread.join()  # Thread'i sonlandır

    def check_username(self, username):
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        try:
            url = f"https://www.instagram.com/{username}/"
            driver.get(url)
            time.sleep(2)

            if "Üzgünüz, bu sayfaya ulaşılamıyor" in driver.page_source or "Tıkladığın bağlantı bozuk olabilir" in driver.page_source:
                return False
            return True
        except Exception as e:
            print(f"Request failed for {username}: {e}")
            return None
        finally:
            driver.quit()

    def check_usernames(self):
        try:
            with open('list.txt', 'r') as file:
                usernames = [line.strip() for line in file.readlines()]

            for username in usernames:
                if not self.is_running:
                    break  # Durdur butonuna basıldığında döngüden çık

                is_valid = self.check_username(username)
                if is_valid is True:
                    result = f"{username} geçerli\n"
                elif is_valid is False:
                    result = f"{username} geçersiz\n"
                else:
                    result = f"{username} kontrol edilemedi\n"

                # Sonuçları GUI'ye yazdır
                self.result_box.insert(END, result)
                self.result_box.see(END)
                time.sleep(2)  # Her istekte bekleme süresi
        except Exception as e:
            self.result_box.insert(END, f"Hata: {e}\n")
        finally:
            self.is_running = False

if __name__ == "__main__":
    root = Tk()
    app = InstagramCheckerApp(root)
    root.mainloop()
