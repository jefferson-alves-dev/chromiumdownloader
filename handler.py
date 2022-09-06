import inspect
import os
import platform
import sys
from zipfile import ZipFile

import requests


class ChromiumFileHandler:
    """
    Class responsible for downloading Chromium/Chromedriver and manipulating files and directories.
    """

    def __init__(self):
        """Automatically builds all necessary attributes for this object.


        Attributes
        ----------
            self.root_dir : str
                Get the root directory of the location where the class is being instantiated.

            self.this_operational_system : str
                Get the name of the operating system.

            self.zip_chromedriver_dir : str
                Path where the Chromedriver zip will be downloaded.

            self.zip_chromedriver_dir : str
                Path where the Chromium zip will be downloaded.

            self.unzip_chromedriver_dir : str
                Path where the Chromedriver zip will be unzipped.

            self.unzip_chromium_dir : str
                Path where the Chromium zip will be unzipped.
        """
        self.root_dir = os.getcwd()
        self.this_operational_system = platform.system()

        self.zip_chromedriver_dir: str = ''
        self.zip_chromium_dir: str = ''

        self.unzip_chromedriver_dir: str = ''
        self.unzip_chromium_dir: str = ''

    def check_if_dir_exists(self, _dir:str=None) -> bool:
        """Checks if the directory specified in the "dir" parameter exists.

        Args:
            dir (str, optional): Path of the directory you want to check if it exists.

        Returns:
            boll: True if directory exists. False if directory does not exist.
        """

        if '/' in _dir: # Replaces the standard '/' separator with the operating system's native separator.
            _dir = _dir.replace('/', os.sep)
        is_there_dir = os.path.exists(_dir)
        return is_there_dir

    def make_dir(self, _dir:str='') -> None:
        """Create directory

        Args:
            dir (str, optional): Defaults to ''.
        """
        try:
            os.makedirs(_dir)
        except Exception as _e:
            print(f"There was an error to create '{_dir}'. Error: {_e}")
            sys.exit()

    def download_chromedriver(self, dir_download:str='') -> None:
        """Method responsible for downloading Chromedriver

        Args:
            dir_download (str, optional): Location where the download file will be saved.
            If no location is specified, the file will be saved to the default location,
            which is the directory where this class was instantiated and
            concatenated with the operating system name.
        """
        chromedriver_version = self.get_last_version_chromedriver()

        if dir_download == '':
            dir_this_download = f"{self.root_dir}{os.sep}chromium{os.sep}{self.this_operational_system.lower()}"

        if dir_download != '':
            dir_this_download = f"{self.root_dir}{os.sep}{dir_download}"

        if self.check_if_dir_exists(_dir=dir_this_download) is False:
            self.make_dir(_dir=dir_this_download)

        if self.this_operational_system == 'Windows':
            url_chromedriver_download = f'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2F{chromedriver_version}%2Fchromedriver_win32.zip'

            querystring = {"generation":"0","alt":"media"}

            print('''Starting Chromedriver for Windows download. Please wait...\n
The wait time will depend on your connection speed.''')

            with requests.request("GET", url_chromedriver_download, params=querystring) as _r:
                _r.raise_for_status()
                with open(f"{dir_this_download}{os.sep}chromedriver.zip", 'wb') as _f:
                    for chunk in _r.iter_content(chunk_size=8192):
                        _f.write(chunk)
            print("Chromedriver for Windows successfully downloaded!")

        if self.this_operational_system == 'Linux':
            url_chromedriver_download = f'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F{chromedriver_version}%2Fchromedriver_linux64.zip'

            querystring = {"generation":"0","alt":"media"}

            print('''Starting Chromedriver for Linux download. Please wait...\n
The wait time will depend on your connection speed.''')
            with requests.request("GET", url_chromedriver_download, params=querystring) as _r:
                _r.raise_for_status()
                with open(f"{dir_this_download}{os.sep}chromedriver.zip", 'wb') as _f:
                    for chunk in _r.iter_content(chunk_size=8192):
                        _f.write(chunk)
            print("Chromedriver for Linux successfully downloaded!")

        self.zip_chromedriver_dir = f"{dir_this_download}{os.sep}chromedriver.zip"
        self.unzip_chromedriver_dir = dir_this_download

    def download_chromium(self, dir_download:str='') -> None:
        """Method responsible for downloading Chromium browser

        Args:
            dir_download (str, optional): Location where the download file will be saved.
            If no location is specified, the file will be saved to the default location,
            which is the directory where this class was instantiated and
            concatenated with the operating system name.
        """
        chromium_version = self.get_last_version_chromedriver()

        if dir_download == '':
            dir_this_download = f"{self.root_dir}{os.sep}chromium{os.sep}{self.this_operational_system.lower()}"

        if dir_download != '':
            dir_this_download = f"{self.root_dir}{os.sep}{dir_download}"

        if self.check_if_dir_exists(_dir=dir_this_download) is False:
            self.make_dir(_dir=dir_this_download)

        if self.this_operational_system == 'Windows':
            url_chromium_download = f'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2F{chromium_version}%2Fchrome-win.zip'

            querystring = {"generation":"0","alt":"media"}

            print('''Starting Chromium Browser for Windows download. Please wait...\n
The wait time will depend on your connection speed.''')
            with requests.request("GET", url_chromium_download, params=querystring) as _r:
                _r.raise_for_status()
                with open(f"{dir_this_download}{os.sep}chromium.zip", 'wb') as _f:
                    for chunk in _r.iter_content(chunk_size=8192):
                        _f.write(chunk)
            print("Chromium Browser for Windows successfully downloaded!")


        if self.this_operational_system == 'Linux':
            url_chromium_download = f'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2F{chromium_version}%2Fchrome-linux.zip'

            querystring = {"generation":"0","alt":"media"}

            print('''Starting Chromium Browser for Linux download. Please wait...\n
The wait time will depend on your connection speed.''')
            with requests.request("GET", url_chromium_download, params=querystring) as _r:
                _r.raise_for_status()
                with open(f"{dir_this_download}{os.sep}chromium.zip", 'wb') as _f:
                    for chunk in _r.iter_content(chunk_size=8192):
                        _f.write(chunk)
            print("Chromium Browser for Linux successfully downloaded!")

        self.zip_chromium_dir = f"{dir_this_download}{os.sep}chromium.zip"
        self.unzip_chromium_dir = dir_this_download

    def get_last_version_chromedriver(self) -> str:
        """Method that checks the Google repository for the latest version of Chromedriver\
            that is available.

        Returns:
            str: Latest version of Chromedriver available.
        """
        if self.this_operational_system == 'Windows':
            url_file_text = f'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Win%2FLAST_CHANGE?alt=media'

        if self.this_operational_system == 'Linux':
            url_file_text = f'https://www.googleapis.com/download/storage/v1/b/chromium-browser-snapshots/o/Linux_x64%2FLAST_CHANGE?alt=media'

        try:
            response = requests.get(url_file_text)
        except Exception as _e:
            print('There was an error downloading the ".txt" file', 'Error: ', _e)
            sys.exit()

        if response.status_code != 200:
            print(f'Request status code: {response.status_code}')
            sys.exit()

        if response.status_code == 200:
            with open(f'{self.root_dir}{os.sep}ChromedriverLastVersion.txt', 'wb') as file:
                file.write(response.content)

            with open('ChromedriverLastVersion.txt', 'r') as file:
                chromedriver_version = file.readlines()[0]

            os.remove('ChromedriverLastVersion.txt')

        print(f'Last version found: {chromedriver_version}')
        return chromedriver_version

    def unzip_file(self, dir_file:str='', to_dir:str='') -> None:
        """Method responsible for unzipping low files.

        Args:
            dir_file (str, optional): Directory where the file to be unzipped is located.
            to_dir (str, optional): Directory where the unzipped data will be.
        """
        try:
            with ZipFile(dir_file, 'r') as _f:
                _f.extractall(to_dir)
        except Exception as _e:
            print(f'There was an error executing the function "{inspect.currentframe().f_code.co_name}". Error: {_e}')
            sys.exit()

    def delete_file(self, dir_file:str='') -> None:
        """Method responsible for deleting '.zip' file that was downloaded.

        Args:
            dir_file (str, optional): Directory where the file to be deleted is located.
        """
        try:
            os.remove(dir_file)
        except Exception as _e:
            print(f'There was an error executing the function\
                "{inspect.currentframe().f_code.co_name}". Error: {_e}')
            sys.exit()

    def run(self,
            chromedriver_download_dir:str='',
            chromium_download_dir:str='',
        ) -> None:

        """Starts all download processes

        Parameters
        ----------
            chromedriver_download_dir : str
                Directory where the Chromedriver download file will be saved.

            chromium_download_dir : str
                Directory where the Chromium browser download file will be saved.
        """

        self.download_chromedriver(chromedriver_download_dir)
        self.unzip_file(
            dir_file=self.zip_chromedriver_dir,
            to_dir=self.unzip_chromedriver_dir
        )
        self.delete_file(self.zip_chromedriver_dir)

        self.download_chromium(chromium_download_dir)
        self.unzip_file(
            dir_file=self.zip_chromium_dir,
            to_dir=self.unzip_chromium_dir
        )
        self.delete_file(self.zip_chromium_dir)
