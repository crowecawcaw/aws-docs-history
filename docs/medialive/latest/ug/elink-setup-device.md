# Deploying the Link hardware

You must deploy the Link device into the AWS cloud.

###### Note

You don't need to be logged into any AWS service to set up the Link
device.

**Deploying the hardware**

1. To set up the device and the camera that provides the source content, and to connect
   the device to the internet, see the instructions included in the packaging.

When you connect the device to the internet, it will verify connectivity by contacting
the following domains. If you are watching network traffic, you might see outbound traffic
to these domains:

    * amazon.com
    * aws.amazon.com

2. After you have connected the device to the internet, the device automatically connects
   to MediaLive in the AWS account and the AWS Region that it is configured for.

A user with AWS permissions can view the device on the console, and transfer the
device to a different Region.
**Performing network diagnostics**

If you have problems connecting the device to the internet, you can use the diagnostics
utility to troubleshoot these problems.

1. Use the instructions in your Link packaging to connect to the device's on-board
   user interface.
2. Locate the navigation pane on the left-hand side.
3. Select **Network Diagnostics**, then select **Run diagnostics
   test** at the top of the page.

The network diagnostic test starts and takes a few seconds to run. 4. The **Test Information** page appears. This page displays network
information and displays the test results: pass or fail (with a reason, and possibly with
troubleshooting steps).
The diagnostics feature tests the following:

- IP address valid – The configured IP address was
  successfully applied to the device.
- Gateway responsive – There is a connection
  between the device and the gateway.
- DNS resolution – The hostnames resolve to each
  of the configured DNS servers.
- AWS connectivity – There is a connection
  between the device and AWS over HTTPS.
- Time server connectivity – The device can sync
  the internal time clock using NTP on port 123.
- Stream connectivity – The device can send video
  packets to AWS using port 2088.
