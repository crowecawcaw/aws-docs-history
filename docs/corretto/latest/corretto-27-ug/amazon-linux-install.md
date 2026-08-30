# Amazon Corretto 27 Installation Instructions for Amazon Linux 2023

This topic describes how to install and uninstall Amazon Corretto 27 on a host or container running the Amazon Linux 2023 operating systems.

## Download and Install RPMs Manually

1. Download RPMs from the [Downloads](downloads-list.md "downloads-list.md") page for your CPU architecture.
   To install the JDK, you will need to download the RPMs for both the JDK and the JRE.
2. Install using `yum localinstall`.

###### Example

```
sudo yum localinstall java-27-amazon-corretto*.rpm
```

## Verify Your Installation

In the terminal, run the following command to verify the installation.

###### Example

```
java -version
```

Expected output for 27.0.0:

```
openjdk 27 2026-08-20
 OpenJDK Runtime Environment Corretto-27.0.0.34.1 (build 27+34-FR)
 OpenJDK 64-Bit Server VM Corretto-27.0.0.34.1 (build 27+34-FR, mixed mode, sharing)
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
