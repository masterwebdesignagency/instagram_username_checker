<h1>Instagram Username Checker (Desktop Application)</h1>

<h2>About the Project</h2>
<p>
    This project is a desktop application designed to check the validity of Instagram usernames.
    Built with Python and Selenium, the application features a user-friendly Graphical User Interface (GUI)
    created using <code>tkinter</code>.
</p>

<h2>Features</h2>
<ul>
    <li><strong>Username Validation:</strong> Verifies if Instagram usernames are valid or not.</li>
    <li><strong>Desktop Application:</strong> Offers a simple and intuitive user interface.</li>
    <li><strong>Start/Stop Functionality:</strong> Allows users to start and stop the checking process as needed.</li>
    <li><strong>Real-Time Results:</strong> Displays results in a text box within the GUI.</li>
    <li><strong>Threading Support:</strong> Ensures the application remains responsive during the checking process.</li>
    <li><strong>File Input/Output:</strong> Reads usernames from a <code>list.txt</code> file and saves the results to a <code>results.txt</code> file.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li>Python</li>
    <li>Selenium (For interacting with Instagram pages)</li>
    <li>tkinter (To create the desktop user interface)</li>
    <li>webdriver-manager (To handle ChromeDriver installation and management)</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Install the required Python libraries:
        <pre><code>pip install selenium webdriver-manager</code></pre>
    </li>
    <li>Clone the repository to your local machine:
        <pre><code>git clone https://github.com/username/instagram-username-checker.git
cd instagram-username-checker</code></pre>
    </li>
    <li>Create a <code>list.txt</code> file containing the usernames to check. Example:
        <pre><code>username1
username2
username3</code></pre>
    </li>
    <li>Run the application:
        <pre><code>python index.py</code></pre>
    </li>
</ol>

<h2>Usage</h2>
<p>
    Launch the application and click the <strong>Start</strong> button to begin the username check.
    Results will be displayed in the text box in real time. To stop the process, click the <strong>Stop</strong> button.
    All results will be saved in the <code>results.txt</code> file.
</p>

<h2>License</h2>
<p>
    This project is licensed under the <a href="LICENSE">MIT License</a>. Feel free to use, modify, and distribute it under the terms of the license.
</p>
