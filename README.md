# Bing Image Creator Tool

**Description**: Bing Image Creator Tool is tool that allows you to run Bing Image Creator (I'll call it BIC) from your terminal.
Due to windows limitations I wasn't able to create a Virtual Display such as Xvfb or Xvnc. That's why this proeject utilizes the [pyvda](https://github.com/mrob95/pyvda) to create a virtual desktops in Windows 10/11.

_Why not use the --headless mode?_: I've tried to use the headless mode but Bing refused to run any scripts while the browser headless . This error is consistent in both Chrome and Edge. Firefox requires further testing.

Other things to include:

- **Technology stack**: Two main python libraries has been used. **Selenium** for webscrapping and **pyvda** for managing desktops and windows.
- **Status**: At this I was trying to use BIC with AutoGPT so I had to create a basic template for my needs. This is a very early version to give a designated version number.

---

## Installation

To install all of the template files, run the following script from the root of your project's directory:

```
git clone https://github.com/beratcmn/bing-image-creator-cli.git
cd bing-image-creator-cli
pip install requirements.txt
python src/main.py
```

---
