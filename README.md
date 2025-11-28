<body>
  <div class="container" role="main">
    <header>
      <h1>Shape Classifier – Image Recognition GUI</h1>
      <p class="lead">
        A Python project that uses <strong>Logistic Regression</strong> to classify 
        <strong>Circle</strong>, <strong>Square</strong>, and <strong>Triangle</strong> shapes.
        The project now includes a fully interactive <strong>Tkinter GUI</strong> where users can upload an image and instantly see the result.
      </p>
      <div class="meta">
        <span class="tag">Python</span>
        <span class="tag">Tkinter</span>
        <span class="tag">scikit-learn</span>
        <span class="tag">Pillow</span>
        <span class="tag">NumPy</span>
      </div>
    </header>

  <section>
      <h2>✨ New in This Version</h2>
      <ul>
        <li>Added a complete <strong>Graphical User Interface (GUI)</strong> using Tkinter</li>
        <li>User can select an image using a file dialog</li>
        <li>Model prediction appears instantly inside the GUI</li>
        <li>Improved structure and readability of the code</li>
        <li>Automatic resizing & preprocessing of input images</li>
      </ul>
    </section>

   <section>
      <h2>📌 Features</h2>
      <ul>
        <li>Loads and preprocesses a dataset of BMP images</li>
        <li>Trains a Logistic Regression classifier</li>
        <li>Graphical interface for selecting images</li>
        <li>Instant shape prediction (Circle / Square / Triangle)</li>
        <li>Beginner-friendly machine learning example</li>
      </ul>
    </section>

  <section>
      <h2>📁 Dataset Structure</h2>
      <p>Place training images inside a directory called <code>dataset/</code>:</p>
      <pre><code>dataset/
1.bmp
2.bmp
3.bmp
...
50.bmp
</code></pre>

 <p>Labels used in the project:</p>
      <table>
        <tr><th>Value</th><th>Shape</th></tr>
        <tr><td>0</td><td>Circle</td></tr>
        <tr><td>1</td><td>Square</td></tr>
        <tr><td>2</td><td>Triangle</td></tr>
      </table>
    </section>
  <section>
      <h2>🧠 How the Model Works</h2>
      <ol>
        <li>Loads images and converts them to grayscale</li>
        <li>Flattens each image into a 1D vector</li>
        <li>Splits data using <code>train_test_split</code></li>
        <li>Trains a <strong>Logistic Regression</strong> classifier</li>
        <li>Resizes user-selected image to 64×64</li>
        <li>Predicts the shape inside the GUI</li>
      </ol>
    </section>
  <section>
      <h2>💻 Installation</h2>
      <pre><code>pip install numpy pillow scikit-learn matplotlib</code></pre>
    </section>
  <section>
      <h2>🚀 How to Run</h2>
      <p>Run the main script:</p>
      <pre><code>python main.py</code></pre>

  <p>The GUI will open:</p>
     <ul>
        <li>Click "<strong>Choose file</strong>"</li>
        <li>Select an image</li>
        <li>The predicted shape will appear instantly</li>
      </ul>
    </section>
  <section>
      <h2>🛠 Technologies Used</h2>
      <ul>
        <li>Python 3</li>
        <li>Tkinter – GUI interface</li>
        <li>Pillow – image preprocessing</li>
        <li>scikit-learn – Logistic Regression model</li>
        <li>NumPy – array manipulation</li>
      </ul>
    </section>

  <section>
      <h2>🚀 Future Improvements</h2>
      <ul>
        <li>Switch to Convolutional Neural Networks (CNN)</li>
        <li>Add more shape classes</li>
        <li>Improve GUI design</li>
        <li>Add training visualization</li>
        <li>Use a JSON file for automatic labeling</li>
      </ul>
    </section>

   <section>
      <h2>📜 License</h2>
      <p>This project is open-source. Add a license file (MIT recommended) for public use.</p>
    </section>

  <footer>
      <p>If you want, I can also:</p>
      <ul>
        <li>Create a Markdown version: <strong>README.md</strong></li>
        <li>Add screenshots of your GUI</li>
        <li>Write a Persian (Farsi) version for your GitHub portfolio</li>
      </ul>
    </footer>
  </div>
</body>
