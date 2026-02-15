# Amazon Corretto 11 Installation Instructions for Amazon Linux 2 and Amazon Linux 2023

This topic describes how to install and uninstall Amazon Corretto 11 on a host or container running the Amazon Linux 2 or Amazon Linux 2023 operating systems.

##

Option 1: Install using the yum Package Manager on Amazon Linux

1. Enable the yum repository in Amazon Linux 2. This is not required on Amazon Linux 2022 and later.

###### Example

```
sudo amazon-linux-extras enable corretto8
```

2. You can install Amazon Corretto 11 as either the runtime environment (JRE) or the full development environment (JDK).
   The development environment includes the runtime environment.

Install Amazon Corretto 11 as JRE.

###### Example

```
sudo yum install java-11-amazon-corretto
```

Install Amazon Corretto 11 as JDK.

###### Example

```
sudo yum install java-11-amazon-corretto-devel
```

Amazon Corretto 11 has a 'headless' variant available. This variant omits runtime dependencies that are
typically associated with GUI applications such as X11 and ALSA and is worth considering for
server-oriented workloads. The 'headful' variant adds support for X11 and ALSA. There is also a
'devel' package which contains the JDK development tools, as well as a 'jmods' package that
contains the Amazon Corretto 11 JMods used to create custom runtime images.

Option 1: Install the headless Amazon Corretto 11:

###### Example

```
sudo yum install java-11-amazon-corretto-headless
```

Option 2: Install the headful Amazon Corretto 11:

###### Example

```
sudo yum install java-11-amazon-corretto
```

Option 3: Install the JDK for Amazon Corretto 11 (Amazon Linux 2023 only):

###### Example

```
sudo yum install java-11-amazon-corretto-devel
```

Option 4: Install the JMods for Amazon Corretto 11 (Amazon Linux 2023 only):

###### Example

```
sudo yum install java-11-amazon-corretto-jmods
```

The installation location is `/usr/lib/jvm/java-11-amazon-corretto.<cpu_arch>`.

While it is recommended to use `/usr/lib/jvm/java-11-amazon-corretto.<cpu_arch>` location,
installation may also add alternative links making installation location accessible via
`/etc/alternatives/jre`, `/etc/alternatives/jre_11` and `/etc/alternatives/jre_11_openjdk` for JRE and
`/etc/alternatives/java_sdk`, `/etc/alternatives/java_sdk_11` and `/etc/alternatives/java_sdk_11_openjdk` for JDK.
The paths under `/etc/alternatives/` may point to another JDK depending on the packages installed and system configuration.

## Option 2: Download and Install RPMs Manually

1. Download RPMs from the [Downloads](downloads-list.md "downloads-list.md") page for your CPU architecture.
   To install the JDK, you will need to download the RPMs for both the JDK and the JRE.
2. Install using `yum localinstall`.

###### Example

```
sudo yum localinstall java-11-amazon-corretto*.rpm
```

## Verify Your Installation

In the terminal, run the following command to verify the installation.

###### Example

```
java -version
```

Expected output for 11.0.30:

```
openjdk version "11.0.30" 2026-01-20 LTS
OpenJDK Runtime Environment Corretto-11.0.30.7.1 (build 11.0.30+7-LTS)
OpenJDK 64-Bit Server VM Corretto-11.0.30.7.1 (build 11.0.30+7-LTS, mixed mode)
```

If you see a version string that doesn't mention `Corretto`,
run the following command to change the default `java` or `javac` providers.

###### Example

```
sudo alternatives --config java
```

If using the JDK you should also run:

```
sudo alternatives --config javac
```

## Uninstall Amazon Corretto 11

You can uninstall Amazon Corretto 11 with the following commands.

Uninstall JRE:

###### Example

```
sudo yum remove java-11-amazon-corretto
```

Uninstall JDK:

###### Example

```
sudo yum remove java-11-amazon-corretto-devel
```

Uninstall headless:

###### Example

```
sudo yum remove java-11-amazon-corretto-headless
```

Uninstall headful:

###### Example

```
sudo yum remove java-11-amazon-corretto
```

Uninstall devel (Amazon Linux 2023 only):

###### Example

```
sudo yum remove java-11-amazon-corretto-devel
```

Uninstall jmods (Amazon Linux 2023 only):

###### Example

```
sudo yum remove java-11-amazon-corretto-jmods
```
