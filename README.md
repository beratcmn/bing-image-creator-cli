# Bing Image Creator Tool

**Description**: Bing Image Creator Tool is a tool that allows you to run Bing Image Creator (I'll call it BIC) from your terminal.
Due to Windows' limitations I wasn't able to create a Virtual Display such as Xvfb or Xvnc provided by [PyVirtualDesktop](https://github.com/ponty/PyVirtualDisplay). That's why in this project I use [pyvda](https://github.com/mrob95/pyvda) to create a virtual desktops in Windows 10/11.

_Why not use the --headless mode?_: I've tried to use the headless mode but Bing refused to run any scripts while the browser is headless. This error is consistent in both Chrome and Edge. Firefox requires further testing.

Other things to include:

- **Technology stack**: Two main python libraries has been used. **Selenium** for webscrapping and **pyvda** for managing desktops and windows.
- **Status**: At this I was trying to use BIC with AutoGPT so I had to create a basic template for my needs. This is a very early version to give a designated version number.

---

## Screenshot

![banner](https://raw.githubusercontent.com/beratcmn/bing-image-creator-cli/main/media/banner-0.png)

---

## Usage

To use this tool, you need to have Python 3.6 or higher installed on your computer. You can download it from [here](https://www.python.org/downloads/).

After installing Python, you need to install the required libraries. You can do this by running the following command in your terminal:

```bash
pip install -r requirements.txt
```

After installing the required libraries, you can run the tool by using the **run.bat** file. You can also run the tool by running the following command in your terminal:

```bash
python src/main.py
```

## Installation

To install the program run the following script

```bash
install.bat
```

Alternatively you can run following commands from the root of your project's directory:

```bash
git clone https://github.com/beratcmn/bing-image-creator-cli.git
cd bing-image-creator-cli
pip install requirements.txt
```

---
