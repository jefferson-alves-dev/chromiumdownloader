### Actively soliciting contributors!

Have ideas for how Chromium Downloader can be improved? Feel free to open an issue or a pull request!

# Chromium Downloader

_Chromium Downloader_ is a genuine and lightweight Python library to automatically download the latest version of Chromium browser and Chromedriver.

## Features

- Support for customizing the directories where files will be saved
- Support to automatically download Chromium browser and Chromedriver according to the Operating System this script is running

### Installation

Installation via Pip will be available soon.

To use:

Clone this repository

```bash
git clone https://github.com/jefferson-alves-dev/chromiumdownloader.git
```

Install the necessary dependencies.

```bash
pip install -r requirements.txt
```

### Using Chromium Downloader in a Python script

To download the Chromium browser and Chromedriver, you will need to import the ChromiumFileHandler class from the chromiumdownloader module.

```python
from chromiumdownloader.handler import ChromiumFileHandler

app = ChromiumFileHandler()
app.run()
```
