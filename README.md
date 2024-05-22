# Let Him Cook Desktop Application

This application was built using Python and a library called Tkinter which allowed me to create custom widgets (ui elements) to the GUI. This version of the `Let Him Cook` project is used to show reports and create new users. Besides that, it's possible to export the reports in PDF and PNG formats.

## Status

- Developing 🚧

## Tech Stack

- [Python 3.12](https://www.python.org/downloads/release/python-3120/)
- [Tkinter (GUI)](https://docs.python.org/3/library/tkinter.html)
- [Matplotlib (Charts)](https://matplotlib.org/)
- [Pillow](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html)

## How to Run

- Install the Python and [pip](https://pip.pypa.io/en/stable/installation/) into your machine. After that, verify the version of this binaries.

```bash
python --version
pip --version
```

- Clone this repository using SSH or HTTPS protocols
- Navigate to the project directory. Open a terminal or command prompt and navigate to the root directory of the project where the `requirements.txt` file is located.

```bash
cd path/to/project
```

- Create a virtual environment (optional but recommended).

```bash
python -m venv venv
```

This command creates a virtual environment in a directory named `venv`.

Once you've created and activated the virtual environment, you can use pip install normally, and it will refer to the pip inside the venv directory automatically. Here are the steps to ensure you're using the pip inside your virtual environment correctly:

Activate the virtual environment:

On Windows:

```bash
.\venv\Scripts\activate
```

On macOS and Linux:

```bash
source venv/bin/activate
```

Once activated, your terminal prompt should change to indicate that you are now working within the virtual environment (usually it will show `(venv)` before the prompt).

- Install dependencies from `requirements.txt`

```bash
pip install -r requirements.txt
```

- Run the application: With the dependencies installed, you can now run the project!

```bash
python main.py
```
