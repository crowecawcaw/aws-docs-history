Effective November 7, 2025, AWS Snowball Edge will only be available to existing customers. If you would like to use AWS Snowball Edge,
sign up prior to that date. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Troubleshooting connection problems with Snowball Edge

The following information can help you troubleshoot certain issues that you might have
with connecting to your Snowball Edge:

- Routers and switches that work at a rate of 100 megabytes per second
  don't work with a Snowball Edge. We recommend that you use a switch that
  works at a rate of 1 GB per second (or faster).
- If you experience odd connection errors with the device, power off the
  Snowball Edge, unplug all the cables, and leave it for 10 minutes. After 10
  minutes have passed, restart the device, and try again.
- Ensure that no antivirus software or firewalls block the Snowball Edge
  device's network connection.
- Be aware that the NFS interface and Amazon S3 interface have different IP
  addresses.
  For more advanced connection troubleshooting, you can take the following steps:

- If you can't communicate with the Snowball Edge, ping the IP address of
  the device. If the ping returns `no connect`, confirm the IP address
  for the device and confirm your local network configuration.
- If the IP address is correct and the lights on the back of the device are
  flashing, use telnet to test the device on ports 22, 9091, and 8080. Testing
  port 22 determines whether the Snowball Edge is working correctly. Testing
  port 9091 determines whether the AWS CLI can be used to send commands to the
  device. Testing port 8080 helps ensure that the device can write to the Amazon S3
  buckets on it with S3 adapter only. If you can connect on port 22 but not on port 8080, first power
  off the Snowball Edge and then unplug all the cables. Leave the device for 10
  minutes, and then reconnect it and start again.
