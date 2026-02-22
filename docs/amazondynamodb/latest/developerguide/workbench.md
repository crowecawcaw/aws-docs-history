# Download NoSQL Workbench for DynamoDB

Follow these instructions to download NoSQL Workbench and DynamoDB local for Amazon DynamoDB.

###### To download NoSQL Workbench and DynamoDB local

- Download the appropriate version of NoSQL Workbench for your operating system.

| Operating system      | Download link                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| macOS (Intel)         | [Download for macOS (Intel)](https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench-x64.dmg "https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench-x64.dmg")             |
| macOS (Apple silicon) | [Download for macOS (Apple silicon)](https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench-arm64.dmg "https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench-arm64.dmg") |
| Windows               | [Download for Windows](https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench.exe "https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench.exe")                           |
| Linux                 | [Download for Linux](https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench.AppImage "https://dy9cqqaswpltd.cloudfront.net/NoSQL_Workbench.AppImage")                   |

###### Note

NoSQL Workbench includes DynamoDB local as part of the installation process.

Java Runtime Environment (JRE) version 17.x or newer is required for running DynamoDB local.

###### Note

NoSQL Workbench supports Ubuntu 12.04, Fedora 21, and Debian 8, or any newer versions of these Linux distributions.

There are two prerequisite pieces of software required for Ubuntu installs: `libfuse2` and `curl`.

As of Ubuntu 22.04, libfuse2 is no longer installed by default. To solve this, run `sudo add-apt-repository universe && sudo apt install libfuse2` to install for the newest Ubuntu version.

For cURL, run `sudo apt update && sudo apt upgrade && sudo apt install curl`.
