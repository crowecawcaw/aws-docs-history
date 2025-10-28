# Amazon Corretto 11 Installation Instructions for Debian-Based,

RPM-Based and Alpine Linux Distributions

This topic describes how to install Amazon Corretto 11 on Debian-based, RPM-based and Alpine Linux
distributions.

If you need to install Amazon Corretto 11 on Amazon Linux, see
[Installing on Amazon Linux](amazon-linux-install.md "amazon-linux-install.md").

## Install Amazon Corretto 11 on Debian-Based

Linux

This section describes how to install and uninstall Amazon Corretto 11 on a host or container
running a Debian-based operating system.

### Using apt

To use the Corretto Apt repositories on Debian-based
systems, such as Ubuntu, import the Corretto public key and then add the repository to the
system list by using the following commands:

```
wget -O - https://apt.corretto.aws/corretto.key | sudo gpg --dearmor -o /usr/share/keyrings/corretto-keyring.gpg && \
echo "deb [signed-by=/usr/share/keyrings/corretto-keyring.gpg] https://apt.corretto.aws stable main" | sudo tee /etc/apt/sources.list.d/corretto.list
```

After the repo has been added, you can install Corretto 11 by running this
command:

```
sudo apt-get update; sudo apt-get install -y java-11-amazon-corretto-jdk
```

For old version Ubuntu such as 14.04, you might encounter error like

```
GPG error: https://apt.corretto.aws stable InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY A122542AB04F24E3
```

If so, add the public key via:

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A122542AB04F24E3
```

### Download and Install the Debian

Package Manually

1. Before you install the JDK, install the `java-common` package.

```
sudo apt-get update && sudo apt-get install java-common
```

2. Download the Linux `.deb` file from the [Downloads](downloads-list.md "downloads-list.md") page.
3. Install the `.deb` file by using `sudo dpkg --install`. For example install x86_64 deb using the following command:

```
sudo dpkg --install java-11-amazon-corretto-jdk_11.0.29.7-1_amd64.deb
```

### Verify Your Installation

In the terminal, run the following command to verify the installation.

```
java -version
```

Expected output for 11.0.29:

```
openjdk version "11.0.29" 2025-10-21 LTS
OpenJDK Runtime Environment Corretto-11.0.29.7.1 (build 11.0.29+7-LTS)
OpenJDK 64-Bit Server VM Corretto-11.0.29.7.1 (build 11.0.29+7-LTS, mixed mode)
```

If you see a version string that doesn't mention `Corretto`, run the
following command to change the default `java` or `javac`
providers.

```
sudo update-alternatives --config java
```

If you're using the JDK, you should also run the following.

```
sudo update-alternatives --config javac
```

### Uninstall Amazon Corretto 11

You can uninstall Amazon Corretto 11 by using the following command.

```
sudo dpkg --remove java-11-amazon-corretto-jdk
```

## Install Amazon Corretto 11 on RPM-Based

Linux

### Using yum

To use Corretto RPM repositories with the yum package manager (such as Amazon
Linux AMI), import the Corretto public key and then add the repository to the system
list. For most systems, you must run the following commands:

```
sudo rpm --import https://yum.corretto.aws/corretto.key
sudo curl -L -o /etc/yum.repos.d/corretto.repo https://yum.corretto.aws/corretto.repo
```

After the repository is added, you can install Corretto 11 by running this
command:

```
sudo yum install -y java-11-amazon-corretto-devel
```

### Using zypper

To use Corretto RPM repositories with the zyppr package manager (such as
openSUSE), import the Corretto public key and then add the repository to the system
list by running the following commands:

```
sudo zypper addrepo https://yum.corretto.aws/corretto.repo; sudo zypper refresh
```

After the repository is added, you can install Corretto 11 by running this command:

```
sudo zypper install java-11-amazon-corretto-devel
```

### Download and install RPM package manually

1. Download the Linux `.rpm` file from the [Downloads](downloads-list.md "downloads-list.md") page.
2. Install the downloaded `.rpm` file using `yum localinstall`. For example install x86_64 rpm using the following command:

```
sudo yum localinstall java-11-amazon-corretto-devel-11.0.29.7-1.x86_64.rpm
```

### Verify Your Installation

In the terminal, run the following command to verify the installation.

```
java -version
```

Expected output for 11.0.29:

```
openjdk version "11.0.29" 2025-10-21 LTS
OpenJDK Runtime Environment Corretto-11.0.29.7.1 (build 11.0.29+7-LTS)
OpenJDK 64-Bit Server VM Corretto-11.0.29.7.1 (build 11.0.29+7-LTS, mixed mode)
```

If you see a version string that doesn't mention `Corretto`,
run the following command to change the default `java` or `javac` providers.

```
sudo alternatives --config java
```

If you're using the JDK, you should also run the following.

```
sudo alternatives --config javac
```

### Uninstall Amazon Corretto 11

You can uninstall Amazon Corretto 11 by using the following command:

```
sudo yum remove java-11-amazon-corretto-devel
```

## Install Amazon Corretto 11 on Alpine

Linux

### Using Alpine Package Manager

To use Corretto Alpine repositories with the Alpine package manager import the Corretto public key
and then add the repository to the system list. For most systems, you must run the following
commands:

```
wget -O /etc/apk/keys/amazoncorretto.rsa.pub  https://apk.corretto.aws/amazoncorretto.rsa.pub
echo "https://apk.corretto.aws/" >> /etc/apk/repositories
apk update
```

After the repository is added, you can install Corretto 11 by running this
command:

```
apk add amazon-corretto-11
```

### Uninstall Amazon Corretto 11

You can uninstall Amazon Corretto 11 by using the following

Uninstall JDK:

```
apk del amazon-corretto-11
```
