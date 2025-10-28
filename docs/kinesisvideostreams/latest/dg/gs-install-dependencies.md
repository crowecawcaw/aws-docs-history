# Install dependencies

Before you can start using the Amazon Kinesis Video Streams producer SDK, you need to set up your development environment with the necessary dependencies. This page guides you through the process of installing the required software components and libraries on your system.

###### Note

For a list of supported operating systems, see [What operating systems does Amazon Kinesis Video Streams Edge Agent
support?](edge-faq.md#edge-faq-os "edge-faq.md#edge-faq-os").

###### Install dependencies on the device

1. To run the Amazon Kinesis Video Streams Edge Agent, install the following appropriate libraries on
   your device:

Ubuntu
Type:

```
wget -O- https://apt.corretto.aws/corretto.key | sudo apt-key add -
sudo add-apt-repository 'deb https://apt.corretto.aws stable main'
sudo apt-get update

sudo apt-get install -y gcc libssl-dev libcurl4-openssl-dev liblog4cplus-dev \
libgstreamer1.0-dev libgstreamer-plugins-base1.0-dev \
gstreamer1.0-plugins-base-apps gstreamer1.0-plugins-bad \
gstreamer1.0-plugins-good gstreamer1.0-tools \
unzip java-11-amazon-corretto-jdk maven
```

Amazon Linux 2
Type:

```
sudo yum update -y && sudo yum upgrade -y && sudo yum clean all -y
sudo yum install -y gcc-c++ openssl-devel libcurl-devel gstreamer1* wget \
java-11-amazon-corretto tar
```

Install `log4cplus-2.1.0` from the source.

```
wget https://github.com/log4cplus/log4cplus/releases/download/REL_2_1_0/log4cplus-2.1.0.tar.gz
tar -xzvf log4cplus-2.1.0.tar.gz
cd log4cplus-2.1.0 && \
mkdir build && \
cd build && \
cmake .. && \
sudo make && \
sudo make install
```

Install `apache-maven-3.9.2` from the
source.

```
wget https://dlcdn.apache.org/maven/maven-3/3.9.2/binaries/apache-maven-3.9.2-bin.tar.gz
RUN tar -xzvf apache-maven-3.9.2-bin.tar.gz -C /opt
```

###### Important

If you see a screen telling you that some services need to be
restarted, press Enter to select **Ok**.

For additional information, see [_Amazon Corretto 11 User Guide_](../../../corretto/latest/corretto-11-ug/generic-linux-install.md "../../../corretto/latest/corretto-11-ug/generic-linux-install.md"). 2. Install the AWS Command Line Interface. See the [Installing or
updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") procedures in the
_AWS Command Line Interface User Guide_.
