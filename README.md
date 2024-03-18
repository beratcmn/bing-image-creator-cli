![banner](https://raw.githubusercontent.com/beratcmn/bing-image-creator-cli/main/media/banner-0.png)

# Bing Image Creator Tool

**Description**: Bing Image Creator Tool is a tool that allows you to run Bing Image Creator (I'll call it BIC) from your terminal.
Due to Windows' limitations I wasn't able to create a Virtual Display such as Xvfb or Xvnc provided by [PyVirtualDesktop](https://github.com/ponty/PyVirtualDisplay). That's why in this project I use [pyvda](https://github.com/mrob95/pyvda) to create virtual desktops in Windows 10/11.

_Why not use the --headless mode?_: I've tried to use the headless mode but Bing refused to run any scripts while the browser is headless. This error is consistent in both **Chrome** and **Edge**. **Firefox** requires further testing.

Other things to include:

- **Technology stack**: Two main python libraries has been used. **Selenium** for webscrapping and **pyvda** for managing desktops and windows.
- **Status**: I was trying to use BIC with AutoGPT so I had to create a basic template for my needs. This is a very early version to give a designated version number.

---

## Changelog [19.03.2024]

- `pyvda` updated to `0.4.1` to work up to `Windows 11 OS Build 22631.3296`
- `MS Edge Driver` updated to `122.0.2365.92`
- Added a selector for initial input box.
- Bing Image Creator XPaths updated to work with 'Microsoft Designer' so it should work fine now.
- Fixed the timeout issue for 'Non-Boosted' images.
- Fixed the Cookie Popup issue.
- Fix issue causuing downloading the second image instead of first too.

## Known Issues

- So far only works with `Microsoft Edge` because of Auto Login feature.
- Less than 4 images are causing the tool to crash.
- Content Policy Error, I'll fix this issue in the next update.

## Example

https://user-images.githubusercontent.com/47108366/232227030-aa0e13ce-84b3-4a76-b011-1f15ac41c314.mp4

## Screenshot

![banner](https://raw.githubusercontent.com/beratcmn/bing-image-creator-cli/main/media/screenshot-0.png)

## Image grid example

![banner](https://raw.githubusercontent.com/beratcmn/bing-image-creator-cli/main/media/darth-vader-dancing-with-stormtroopers-comic-style.png)

---

## Installation

To install the program run the following script

```bash
install.bat
```

Alternatively you can run following commands from the root of your project's directory:

```bash
git clone https://github.com/beratcmn/bing-image-creator-cli.git
cd bing-image-creator-cli
python -m venv .venv
.venv\Scripts\activate.ps1
pip install -r requirements.txt
```

## Usage

After installing the required libraries, you can run the tool by using the **run.bat** file.

```bash
run.bat
```

You can also run the tool by running the following command in your terminal:

```bash
python src/main.py
```

## I highly recommend you to use **Microsoft Edge** because it will automatically login to your Microsoft account thus removing the need to login besides it's the only browser that I've tested and it works perfectly.

## Todo

- [ ] Add Magic Prompt feature to the tool like in Ideogram.
- [ ] Add a CLI for the tool.
- [ ] Add a simple REST API for the tool.
