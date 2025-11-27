
<body>
  <div class="container" role="main">
    <header>
      <h1>Shape Classification Using Logistic Regression</h1>
      <p class="lead">A simple image classification project that trains a Logistic Regression model to identify <strong>Circle</strong>, <strong>Square</strong>, and <strong>Triangle</strong> from BMP images.</p>
      <div class="meta" aria-hidden="true">
        <span class="tag">Python</span>
        <span class="tag">NumPy</span>
        <span class="tag">Pillow (PIL)</span>
        <span class="tag">scikit-learn</span>
      </div>
    </header>
<section>
      <h2>📌 Features</h2>
      <ul>
        <li>Loads a dataset of BMP images</li>
        <li>Converts images to grayscale and flattens them</li>
        <li>Trains a Logistic Regression classifier</li>
        <li>User can input a custom image path for prediction</li>
        <li>Beginner-friendly; easy to extend with other models</li>
      </ul>
    </section>

 <section>
      <h2>📁 Dataset Structure</h2>
      <p class="note">Place the dataset in a <code class="inline">dataset/</code> folder and name images sequentially:</p>
      <pre><code>dataset/
1.bmp
2.bmp
3.bmp
...
50.bmp
</code></pre>
      <p>Labels are assigned in the code using an array <code class="inline">y</code> where:</p>
      <table>
        <tr><th style="text-align:left">Label</th><th style="text-align:left">Meaning</th></tr>
        <tr><td>0</td><td>Circle</td></tr>
        <tr><td>1</td><td>Square (shown as 'sqrt' in code)</td></tr>
        <tr><td>2</td><td>Triangle</td></tr>
      </table>
      <p class="note">Ensure the order of images matches the label array in the script.</p>
    </section>

 <section>
      <h2>🧠 How the Model Works</h2>
   <ol>
        <li>Each image is loaded with Pillow and converted to a NumPy array.</li>
        <li>The code extracts a single grayscale channel and flattens the image into a 1D vector.</li>
        <li>The dataset is split (default 80% train / 20% test).</li>
        <li>A <code class="inline">LogisticRegression</code> model is trained on flattened images.</li>
        <li>User supplies a path to a test image; the model predicts and prints the shape label.</li>
      </ol>
    </section>

 <section>
      <h2>💻 Installation</h2>
      <p>Clone the repository and install dependencies:</p>
      <pre><code>pip install numpy pillow scikit-learn matplotlib</code></pre>
    </section>

 <section>
      <h2>▶️ How to Run</h2>
    <p>Run the main script from the project folder:</p>
<pre><code>python main.py</code></pre>
<p>Then enter the path of an image to classify, for example:</p>
<pre><code>enter the path of your image: dataset/test_triangle.bmp</code></pre>
<h2>📌 Example Output</h2>
<pre><code>enter the path of your image: dataset/test_triangle.bmp
it is tringle
</code></pre>
    </section>

 <section>
      <h2>🛠 Technologies Used</h2>
      <ul>
        <li>Python 3</li>
        <li>NumPy — numerical processing</li>
        <li>Pillow (PIL) — image loading and handling</li>
        <li>scikit-learn — Logistic Regression</li>
        <li>Matplotlib — optional visualization</li>
      </ul>
    </section>

<section>
      <h2>🚀 Future Improvements</h2>
      <ul>
        <li>Support more shapes</li>
        <li>Try different ML models: SVM, RandomForest, KNN, Neural Networks</li>
        <li>Improve preprocessing: resizing, normalization, denoising</li>
        <li>Add automatic dataset labeling or augmentations</li>
        <li>Build a small GUI (Tkinter/PyQt) or a simple web demo</li>
      </ul>
    </section>

 <section>
      <h2>📜 License</h2>
      <p class="note">This project is open-source and free to use. Add a license file (e.g., <span class="kbd">MIT</span>) in your repository if you want to explicitly set terms.</p>
    </section>

 <footer>
      <p class="note">If you want, I can also:</p>
      <ul>
        <li>Provide this file as an actual <strong>README.html</strong> ready to paste into your repo.</li>
        <li>Add screenshots or sample images to include in the repo.</li>
        <li>Convert the same content to a minimal <strong>README.md</strong> or a GitHub Pages friendly layout.</li>
      </ul>
      <p style="margin-top:8px">Good luck — and tell me if you want a localized Persian version or slight wording changes for a portfolio!</p>
    </footer>
  </div>
</body>
