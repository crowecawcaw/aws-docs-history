

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Networking with your mobile device
<a name="network-mobile"></a>

From a networking perspective, the process of provisioning sensors or gateways goes like this.

**Topics**
+ [Setting up your Monitron network foundation with your mobile app](#network-mobile-foundation)
+ [Setting up your gateways](#network-gateways)
+ [Setting up your sensors](#network-sensors)

## Setting up your Monitron network foundation with your mobile app
<a name="network-mobile-foundation"></a>

1. Your mobile device uses Wi-Fi or a signal from outside the facility (such as a satellite or a tower) to connect to the internet.

1. Over the internet, you install the Amazon Monitron mobile app on your mobile device. (This only has to be done once per device.)

1. Over the internet, the Monitron app on your mobile device connects to the AWS infrastructure, authenticating with AWS IAM Identity Center.

1. Having been authenticated inside the AWS infrastructure, the app connects to the Amazon Monitron back end.

1. Using your authenticated app, you identify the framework of your local Amazon Monitron setup. This involves naming your local network and identifying how many gateways will be part of it.

## Setting up your gateways
<a name="network-gateways"></a>

1. In your mobile app, (running authenticated and securely over the internet), choose the option for adding a gateway.

1. You give your mobile app permission to access Bluetooth functionality on your mobile device.

1. The mobile app on your device, using Bluetooth, connects to your local gateway. 

1. You give the app the name of your local network (Wi-Fi only).

1. You give the app the password to your local network.

1. The app, securely over the internet, communicates with the Monitron back end about your gateway.

1. On the front end, through Bluetooth on your mobile device, the app gives the gateway the token it needs to communicate with the Monitron back end.

1. The gateway uses your local network (Ethernet or Wi-Fi) to connect to the internet through your local internet access point.

1. Securely, over the internet, your gateway registers itself with the Monitron back end.

1. A representation of your gateway now appears in your app as a part of your network.

## Setting up your sensors
<a name="network-sensors"></a>

1. In the mobile app, you indicate the name and class of your asset (once per asset).

1. In the mobile app, you give a name to a sensor.

1. In your facility, you physically attach an un-paired sensor to your asset.

1. From the mobile app, using your device’s NFC, you connect to the sensor.

1. The mobile app, using your device’s NFC, tells the sensor about your local Monitron gateway, already set up.

1. The mobile app, securely over the internet, tells the Monitron back end about the sensor.

1. The sensor, using Bluetooth, begins to send data about the asset to the gateway.

1. The gateway, securely over the internet, sends the sensor’s data to the Monitron back end.

1. In the mobile app (or the web app), securely over the internet, you can now view the analytical data about your asset.