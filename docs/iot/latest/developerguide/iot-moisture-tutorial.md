# Tutorial: Monitoring soil moisture with AWS IoT and

Raspberry Pi

This tutorial shows you how to use a [Raspberry
Pi](https://www.raspberrypi.org/ "https://www.raspberrypi.org/"), a moisture sensor, and AWS IoT to monitor the soil moisture level for a house
plant or garden. The Raspberry Pi runs code that reads the moisture level and temperature
from the sensor and then sends the data to AWS IoT. You create a rule in AWS IoT that sends an
email to an address subscribed to an Amazon SNS topic when the moisture level falls below a
threshold.

###### Note

This tutorial might not be up to date. Some references might have been superseded
since this topic was originally published.

###### Contents

- [Prerequisites](iot-moisture-tutorial.md#iot-moisture-prereqs "iot-moisture-tutorial.md#iot-moisture-prereqs")
- [Setting up AWS IoT](iot-moisture-setup.md "iot-moisture-setup.md")
  - [Step 1: Create the AWS IoT policy](iot-moisture-policy.md "iot-moisture-policy.md")
  - [Step 2: Create the AWS IoT thing,
    certificate, and private key](iot-moisture-create-thing.md "iot-moisture-create-thing.md")
  - [Step 3: Create an Amazon SNS topic and
    subscription](iot-moisture-create-sns-topic.md "iot-moisture-create-sns-topic.md")
  - [Step 4: Create an AWS IoT rule to send an
    email](iot-moisture-create-rule.md "iot-moisture-create-rule.md")

- [Setting up your Raspberry Pi and moisture
  sensor](iot-moisture-raspi-setup.md "iot-moisture-raspi-setup.md")

## Prerequisites

To complete this tutorial, you need:

- An AWS account.
- An IAM user with administrator permissions.
- A development computer running Windows, macOS, Linux, or Unix to access the
  [AWS IoT console](https://console.aws.amazon.com/iot/home "https://console.aws.amazon.com/iot/home").
- A [Raspberry Pi 3B or
  4B](https://www.raspberrypi.com/products/ "https://www.raspberrypi.com/products/") running the latest [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/ "https://www.raspberrypi.com/software/operating-systems/"). For installation instructions, see [Install an operating system](https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system "https://www.raspberrypi.com/documentation/computers/getting-started.html#installing-the-operating-system") on the Raspberry Pi website.
- A monitor, keyboard, mouse, and Wi-Fi network or Ethernet connection for your
  Raspberry Pi.
- A Raspberry Pi-compatible moisture sensor. The sensor used in this tutorial is
  an [Adafruit STEMMA I2C
  Capacitive Moisture Sensor](https://www.adafruit.com/product/4026 "https://www.adafruit.com/product/4026") with a [JST 4-pin to female socket cable
  header](https://www.adafruit.com/product/3950 "https://www.adafruit.com/product/3950").
