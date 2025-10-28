# Prerequisites for connecting Amazon Neptune databases using IAM authentication

The following are instructions for installing Apache Maven and Java 8 on an Amazon EC2 instance.
These are required for the Amazon Neptune Signature Version 4 authentication samples.

###### To Install Apache Maven and Java 8 on your EC2 instance

1. Connect to your Amazon EC2 instance with an SSH client.
2. Install Apache Maven on your EC2 instance. If using Amazon Linux 2023 (preferred), use:

```
sudo dnf update -y
sudo dnf install maven -y
```

If using Amazon Linux 2, download the latest binary from [https://maven.apache.org/download.cgi:](https://maven.apache.org/download.cgi: "https://maven.apache.org/download.cgi:")

```
sudo yum remove maven -y
wget https://dlcdn.apache.org/maven/maven-3/ <version>/binaries/apache-maven-<version>-bin.tar.gz
sudo tar -xzf apache-maven-<version>-bin.tar.gz -C /opt/
sudo ln -sf /opt/apache-maven-<version> /opt/maven
echo 'export MAVEN_HOME=/opt/maven' >> ~/.bashrc
echo 'export PATH=$MAVEN_HOME/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

3. The Gremlin libraries require Java 8. Enter the following to install Java 8 on your
   EC2 instance.

```
sudo yum install java-1.8.0-devel
```

4. Enter the following to set Java 8 as the default runtime on your EC2 instance.

```
sudo /usr/sbin/alternatives --config java
```

When prompted, enter the number for Java 8. 5. Enter the following to set Java 8 as the default compiler on your EC2 instance.

```
sudo /usr/sbin/alternatives --config javac
```

When prompted, enter the number for Java 8.
