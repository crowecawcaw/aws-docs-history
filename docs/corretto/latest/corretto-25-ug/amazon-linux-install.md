# Amazon Corretto 25 Installation Instructions for Amazon Linux 2023

This topic describes how to install and uninstall Amazon Corretto 25 on a host or container running the Amazon Linux 2023 operating systems.

##

Option 1: Install using the yum Package Manager on Amazon Linux

Amazon Corretto 25 has a 'headless' variant available. This variant omits runtime dependencies that are
typically associated with GUI applications such as X11 and ALSA and is worth considering for
server-oriented workloads. The 'headful' variant adds support for X11 and ALSA. There is also a
'devel' package which contains the JDK development tools, as well as a 'jmods' package that
contains the Amazon Corretto 25 JMods used to create custom runtime images.

Option 1: Install the headless Amazon Corretto 25:

```
sudo yum install java-25-amazon-corretto-headless
```

Option 2: Install the headful Amazon Corretto 25:

```
sudo yum install java-25-amazon-corretto
```

Option 3: Install the JDK for Amazon Corretto 25:

```
sudo yum install java-25-amazon-corretto-devel
```

Option 4: Install the JMods for Amazon Corretto 25:

```
sudo yum install java-25-amazon-corretto-jmods
```

The installation location is `/usr/lib/jvm/java-25-amazon-corretto.<cpu_arch>`.

While it is recommended to use `/usr/lib/jvm/java-25-amazon-corretto.<cpu_arch>` location,
installation may also add alternative links making installation location accessible via
`/etc/alternatives/jre`, `/etc/alternatives/jre_25` and `/etc/alternatives/jre_25_openjdk` for JRE and
`/etc/alternatives/java_sdk`, `/etc/alternatives/java_sdk_25` and `/etc/alternatives/java_sdk_25_openjdk` for JDK.
The paths under `/etc/alternatives/` may point to another JDK depending on the packages installed and system configuration.

## Option 2: Download and Install RPMs Manually

1. Download RPMs from the [Downloads](downloads-list.md "downloads-list.md") page for your CPU architecture.
   To install the JDK, you will need to download the RPMs for both the JDK and the JRE.
2. Install using `yum localinstall`.

```
sudo yum localinstall java-25-amazon-corretto*.rpm
```

## Verify Your Installation

In the terminal, run the following command to verify the installation.

```
java -version
```

Expected output for 25.0.1:

```
openjdk version "25.0.1" 2025-10-21 LTS
OpenJDK Runtime Environment Corretto-25.0.1.8.1 (build 25.0.1+8-LTS)
OpenJDK 64-Bit Server VM Corretto-25.0.1.8.1 (build 25.0.1+8-LTS, mixed mode)
```

If you see a version string that doesn't mention `Corretto`,
run the following command to change the default `java` or `javac` providers.

```
sudo alternatives --config java
```

If using the JDK you should also run:

```
sudo alternatives --config javac
```

## Uninstall Amazon Corretto 25

You can uninstall Amazon Corretto 25 with the following commands.

Uninstall headless:

```
sudo yum remove java-25-amazon-corretto-headless
```

Uninstall headful:

```
sudo yum remove java-25-amazon-corretto
```

Uninstall devel:

```
sudo yum remove java-25-amazon-corretto-devel
```

Uninstall jmods:

```
sudo yum remove java-25-amazon-corretto-jmods
```
