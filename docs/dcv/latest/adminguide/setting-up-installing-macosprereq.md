

# Prerequisites for macOS Amazon DCV server on an Amazon EC2 instances
<a name="setting-up-installing-macosprereq"></a>

This topic describes how to prepare your Amazon EC2 Mac instance before you install the Amazon DCV server.

**Topics**
+ [Prerequisites for all supported instances](#setting-up-installing-all)

## Prerequisites for all supported instances
<a name="setting-up-installing-all"></a>

 Amazon EC2 Mac Apple silicon instances are supported on Amazon DCV version 2025.0 and later. See [ Amazon EC2 Mac documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) for a complete list of Apple silicon instances. You can install Amazon DCV Server with the interactive GUI or programmatically. For interactive GUI access, see the [ Amazon EC2 Mac documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-mac-instance.html#mac-instance-vnc). For unattended installations, System Integrity Protection (SIP) must be disabled. For more information on configuring SIP, see the [Amazon EC2 Mac documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mac-sip-settings.html). An example image creation automation can be found in the aws-samples Github within the [dcv-samples repository](https://github.com/aws-samples/dcv-samples/tree/main/cdk/dcv-mac-image-automation). 