# Choose a lightweight protocol for messaging

IoT devices can use a number of application layer protocols to
communicate with each other as well as the cloud.  The most
common protocol for IoT devices is
[MQTT](https://mqtt.org/mqtt-specification/ "https://mqtt.org/mqtt-specification/").

MQTT is designed to be a lightweight and power efficient
protocol for IoT applications that require low power consumption
and low bandwidth usage. It uses a publish-subscribe model,
which allows devices to exchange small messages with each other
using a minimal amount of network bandwidth.

HTTP, on the other hand, is a more heavyweight protocol that is
used for web-based applications. While HTTP is not specifically
designed for IoT applications, it is widely used for sending and
receiving data over the internet. HTTP uses a request-response
model, which requires devices to send larger amounts of data
back and forth over the network. This can result in higher power
consumption and shorter battery life for IoT devices.
