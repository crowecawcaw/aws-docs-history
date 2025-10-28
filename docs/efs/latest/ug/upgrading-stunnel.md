# Upgrading `stunnel`

Encryption of data in transit with the EFS mount helper requires `OpenSSL`
version 1.0.2 or newer, and a version of `stunnel` that supports both Online
Certificate Status Protocol (OCSP) and certificate hostname checking. The EFS mount helper uses
the `stunnel` program for its TLS functionality. Note that some versions of
Linux don't include a version of `stunnel` that supports these TLS features by
default. When using one of those Linux distributions, mounting an EFS file system
using TLS fails.

After installing the EFS mount helper, you can upgrade your system's version of stunnel
with the following instructions.

###### To upgrade `stunnel` on Amazon Linux, Amazon Linux 2, and other supported Linux distributions (except for [SLES 12](#stunnel-on-sles12 "#stunnel-on-sles12"))

1. In a web browser, go to the `stunnel` downloads page [https://stunnel.org/downloads.html](https://www.stunnel.org/downloads.html "https://www.stunnel.org/downloads.html").
2. Locate the latest `stunnel` version that is available in `tar.gz` format. Note the name of the file as you will
   need it in the following steps.
3. Open a terminal on your Linux client, and run the following commands in the order presented.
   1. For RPM:

   ```
   sudo yum install -y gcc openssl-devel tcp_wrappers-devel
   ```

   For DEB:

   ```
   sudo apt-get install build-essential libwrap0-dev libssl-dev
   ```

   2. Replace `latest-stunnel-version` with the name of the file you noted previously in Step 2.

   ```
   sudo curl -o `latest-stunnel-version`.tar.gz https://www.stunnel.org/downloads/`latest-stunnel-version`.tar.gz
   ```

   3. ```
      sudo tar xvfz `latest-stunnel-version`.tar.gz
      ```

   ````
   4. ```
   cd `latest-stunnel-version`/
   ````

   5. ```
      sudo ./configure
      ```

   ````
   6. ```
   sudo make
   ````

   7. The current `stunnel` package is installed in `bin/stunnel`. So that the
      new version can be installed, remove that directory with the following command.

   ```
   sudo rm /bin/stunnel
   ```

   8. Install the latest version:

   ```
   sudo make install
   ```

   9. Create a symlink:

   ```
   sudo ln -s /usr/local/bin/stunnel /bin/stunnel
   ```

###### To upgrade stunnel on macOS

- Open a terminal on your EC2 Mac instance, and run the following command to upgrade
  to the latest version of stunnel.

```
brew upgrade stunnel
```

###### Upgrading stunnel for SLES 12

- Run the following commands and follow the zypper package manager instructions to upgrade stunnel on
  your compute instance running SLES12.

```
sudo zypper addrepo https://download.opensuse.org/repositories/security:Stunnel/SLE_12_SP5/security:Stunnel.repo
sudo zypper refresh
sudo zypper install -y stunnel
```

After you've installed a version of stunnel with the required features, you can mount your
file system using TLS with the Amazon EFS recommended settings.
