# Code-With-Mosh-Playlist-Downloader

> Bash/Python Script: A script to download full course from [codewithmosh.com](https://codewithmosh.com), given one has the valid login credentials <br />

### Topics Available:

| 1                | 2                            | 3                                                            |
| ---------------- | ---------------------------- | ------------------------------------------------------------ |
| ReactJS          | NodeJS                       | AngularJS: Beginner to Pro                                   |
| Redux in Angular | Angular4 Crash               | JS: Basics                                                   |
| JS: OOPS         | Complete Python              | Python Developers                                            |
| SQL              | C# Basics                    | C# Intermediate                                              |
| C# Advanced      | C# Xamarin Native Apps       | The Complete ASP.NET MVC 5 Course                            |
| C# Unit test     | Clean Coding and Refactoring | Build a Real-world App with ASP.NET Core 1.0+ and Angular 2+ |

### :pushpin: Aim

- Help those who want to avoid themselves from 'clicks-and-saves'
- To share a mixed-cum-messed-up learning experience (Python, JS, Shell Script etc)
- Would try include a flow graph of events and Progress

### :v: Missions Accomplised:

- Include as many Tutorials as possible
- Implemented using Scraping Module in Python and Bash Scripts

### :eyeglasses: Download Options

- [x] Download Playlist for a specific topic
- [x] Download all Playlists at once (only mentioned Topics)

## :cloud: Installation

#### Prerequisites
- ##### Install Python (Python2, if not installed on the system by default, like Ubuntu 18.04)
```shell
   sudo apt update
   sudo apt install python3
   sudo apt install python3-pip
   pip3 --version
```

#### Usage Steps

1. Clone the Repository and open the project directory
2. Install the packages required for the project
```bash
   $ pip3 install -r ./requirements.txt
```
3. Open ./core/config_detail.py  and add the following details
   - USERNAME (email)
   - PASSWORD
   - SCHOOL_ID (A numerical value found in your URL as you login)
     ```
     Sample URL: "https://sso.teachable.com/secure/121212/users/sign_in?clean_login=true&reset_purchase_session=1"
     Here the 121212 represents your SCHOOL_ID
      ```
   - TOPIC_URL : the url of the desired topic [Topic_list.url](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/core/Topic_list.url)
   - TOPIC_NAME : the name of the desired playlist
4. Given the right details, start the script (./core/download.py)
```bash
   $ python3 download.py
```

##### NOTE: The ReactJS playlist consumes upto 17 GB of your total data

##### Other modules can consume upto 35 GB (rough estimate) of your data

##### Recommended to use over Wifi only

## :books: About

> [AboutTheFiles.md](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/AboutTheFiles.md) contains the details about the files used in this module.

## :star2: Issues and Contributions
- Want to contribute and be a part of this small project. Check the simplest contributing guidelines [here](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/CONTRIBUTING.md)
- Contributions don't have to be very special. From 'simple typos' to 'serious bugs' all kinds of contributions are welcome! :smile:

Thanks! :heart:

## :scroll: License

[MIT](https://github.com/garganshul108/Code-With-Mosh-Playlist-Downloader/blob/master/LICENSE) © [Anshul Garg](https://github.com/garganshul108)
