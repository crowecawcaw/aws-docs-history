# Amazon Corretto 25 Installation Instructions for Debian-Based,

RPM-Based and Alpine Linux Distributions

This topic describes how to install Amazon Corretto 25 on Debian-based, RPM-based and Alpine Linux
distributions.

If you need to install Amazon Corretto 25 on Amazon Linux, see
[Installing on Amazon Linux](amazon-linux-install.md "amazon-linux-install.md").

## Install Amazon Corretto 25 on Debian-Based

Linux

This section describes how to install and uninstall Amazon Corretto 25 on a host or container
running a Debian-based operating system.

### Using apt

To use the Corretto Apt repositories on Debian-based
systems, such as Ubuntu, import the Corretto public key and then add the repository to the
system list by using the following commands:

###### Example

```
wget -O - https://apt.corretto.aws/corretto.key | sudo gpg --dearmor -o /usr/share/keyrings/corretto-keyring.gpg && \
echo "deb [signed-by=/usr/share/keyrings/corretto-keyring.gpg] https://apt.corretto.aws stable main" | sudo tee /etc/apt/sources.list.d/corretto.list
```

After the repo has been added, you can install Corretto 25 by running this
command:

###### Example

```
sudo apt-get update; sudo apt-get install -y java-25-amazon-corretto-jdk
```

For old version Ubuntu such as 14.04, you might encounter error like

###### Example

```
GPG error: https://apt.corretto.aws stable InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY A122542AB04F24E3
```

If so, add the public key via:

###### Example

```
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A122542AB04F24E3
```

### Download and Install the Debian

Package Manually

1. Before you install the JDK, install the `java-common` package.

###### Example

```
sudo apt-get update && sudo apt-get install java-common
```

2. Download the Linux `.deb` file from the [Downloads](downloads-list.md "downloads-list.md") page.
3. Install the `.deb` file by using `sudo dpkg --install`. For example install x86_64 deb using the following command:

###### Example

```
sudo dpkg --install java-25-amazon-corretto-jdk_25.0.2.10-1_amd64.deb
```

### Verify Your Installation

In the terminal, run the following command to verify the installation.

###### Example

```
java -version
```

Expected output for 25.0.2:

```
openjdk version "25.0.2" 2026-01-20 LTS
OpenJDK Runtime Environment Corretto-25.0.2.10.1 (build 25.0.2+10-LTS)
OpenJDK 64-Bit Server VM Corretto-25.0.2.10.1 (build 25.0.2+10-LTS, mixed mode)
```

If you see a version string that doesn't mention `Corretto`, run the
following command to change the default `java` or `javac`
providers.

###### Example

```
sudo update-alternatives --config java
```

If you're using the JDK, you should also run the following.

```
sudo update-alternatives --config javac
```

### Uninstall Amazon Corretto 25

You can uninstall Amazon Corretto 25 by using the following command.

###### Example

```
sudo dpkg --remove java-25-amazon-corretto-jdk
```

## Install Amazon Corretto 25 on RPM-Based

Linux

### Using yum

To use Corretto RPM repositories with the yum package manager (such as Amazon
Linux AMI), import the Corretto public key and then add the repository to the system
list. For most systems, you must run the following commands:

###### Example

```
sudo rpm --import https://yum.corretto.aws/corretto.key
sudo curl -L -o /etc/yum.repos.d/corretto.repo https://yum.corretto.aws/corretto.repo
```

After the repository is added, you can install Corretto 25 by running this
command:

###### Example

```
sudo yum install -y java-25-amazon-corretto-devel
```

### Using zypper

To use Corretto RPM repositories with the zyppr package manager (such as
openSUSE), import the Corretto public key and then add the repository to the system
list by running the following commands:

###### Example

```
sudo zypper addrepo https://yum.corretto.aws/corretto.repo; sudo zypper refresh
```

After the repository is added, you can install Corretto 25 by running this command:

###### Example

```
sudo zypper install java-25-amazon-corretto-devel
```

### Download and install RPM package manually

1. Download the Linux `.rpm` file from the [Downloads](downloads-list.md "downloads-list.md") page.
2. Install the downloaded `.rpm` file using `yum localinstall`. For example install x86_64 rpm using the following command:

###### Example

```
sudo yum localinstall java-25-amazon-corretto-devel-25.0.2.10-1.x86_64.rpm
```

### Verify Your Installation

In the terminal, run the following command to verify the installation.

###### Example

```
java -version
```

Expected output for 25.0.2:

```
openjdk version "25.0.2" 2026-01-20 LTS
OpenJDK Runtime Environment Corretto-25.0.2.10.1 (build 25.0.2+10-LTS)
OpenJDK 64-Bit Server VM Corretto-25.0.2.10.1 (build 25.0.2+10-LTS, mixed mode)
```

If you see a version string that doesn't mention `Corretto`,
run the following command to change the default `java` or `javac` providers.

###### Example

```
sudo alternatives --config java
```

If you're using the JDK, you should also run the following.

```
sudo alternatives --config javac
```

### Uninstall Amazon Corretto 25

You can uninstall Amazon Corretto 25 by using the following command:

###### Example

```
sudo yum remove java-25-amazon-corretto-devel
```

## Install Amazon Corretto 25 on Alpine

Linux

### Using Alpine Package Manager

To use Corretto Alpine repositories with the Alpine package manager import the Corretto public key
and then add the repository to the system list. For most systems, you must run the following
commands:

###### Example

```
wget -O /etc/apk/keys/amazoncorretto.rsa.pub  https://apk.corretto.aws/amazoncorretto.rsa.pub
echo "https://apk.corretto.aws/" >> /etc/apk/repositories
apk update
```

After the repository is added, you can install Corretto 25 by running this
command:

###### Example

```
apk add amazon-corretto-25
```

You can install Corretto 25 JRE by running

###### Example

```
apk add amazon-corretto-25-jre
```

### Uninstall Amazon Corretto 25

You can uninstall Amazon Corretto 25 by using the following

Uninstall JDK:

###### Example

```
apk del amazon-corretto-25
```
