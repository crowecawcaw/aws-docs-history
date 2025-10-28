# Linux client

The Linux client runs natively on the operating system. You can use it to connect to Amazon DCV
sessions that are hosted on Windows and Linux Amazon DCV servers.

You install the Linux client on a Linux client computer using a software package. The
software package installs all required packages and their dependencies, and performs the
required client configuration.

For instructions on how to connect to a Amazon DCV session using the Linux client, see [Connecting to a Amazon DCV session using the Linux
client](using-connecting-linux.md "using-connecting-linux.md").

###### To install the Linux client

1. The software packages are digitally signed with a secure GPG signature. To allow the
   package manager to verify the package signature, import the Amazon DCV GPG key. To do this,
   open a terminal window and import the Amazon DCV GPG key.
   - RHEL, CentOS, Rocky Linux, and SUSE Linux Enterprise 15

   ```
   `$` sudo rpm --import https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   - Ubuntu

   Download the GPG key.

   ```
   `$` wget https://d1uj6qtbmh3dt5.cloudfront.net/NICE-GPG-KEY
   ```

   Install the GPG key.

   ```
   `$` sudo apt-key add NICE-GPG-KEY
   ```

2. Download the appropriate client software package for your target operating system from the [Amazon DCV](http://download.amazondcv.com "http://download.amazondcv.com") website.

###### Tip

The [latest packages](http://download.amazondcv.com/latest.html "http://download.amazondcv.com/latest.html") page of the download website contains links that always point to the newest available version.
You can use these links to automatically retrieve the newest Amazon DCV packages. 3. Install the Linux client. Enter the filename of the downloaded file to complete the following command.

    * RHEL, CentOS, and Rocky Linux



    ```
    `$`  sudo yum install ``the downloaded .rpm file``
    ```
    * Ubuntu



    ```
    `$`  sudo dpkg --install ``the downloaded .deb file``
    ```
    * SUSE Linux Enterprise



    ```
    `$`  sudo zypper install ``the downloaded .rpm file``
    ```
