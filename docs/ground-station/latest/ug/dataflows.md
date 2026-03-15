# Set up and configure Amazon EC2

Properly configuring your Amazon EC2 instance is required for synchronous delivery of VITA-49 Signal/IP
data or VITA-49 Extension data/IP to be delivered via the AWS Ground Station Agent or a dataflow endpoint.
Depending on your specific needs, you may perform the Front End (FE) processor or Software
Defined Radio (SDR) directly on the same instance, or you may need to utilize additional EC2
instances. Selection and installation of your FE or SDR is beyond the scope of this user guide.
For more information on the specific data formats, see
[AWS Ground Station data plane interfaces](dataflows.md#dataflows.interfaces "dataflows.md#dataflows.interfaces").

For information about our service terms, please see [AWS Service Terms](https://aws.amazon.com/service-terms "https://aws.amazon.com/service-terms").

## Supplied Common Software

AWS Ground Station provides common software to ease setup of your Amazon EC2 instance.

### AWS Ground Station Agent

The AWS Ground Station Agent receives Digital Intermediate Frequency (DigIF) downlink data and egresses
decrypted data that enables the following:

- DigIF downlink capability from 40 MHz to 400 MHz of bandwidth.
- High rate, low jitter DigIF data delivery to any public IP (AWS Elastic IP) on the AWS network.
- Reliable data delivery using Forward Error Correction (FEC).
- Secure data delivery using a customer managed AWS KMS key for encryption.

For more information, see [AWS Ground Station Agent User Guide](../gs-agent-ug.md "../gs-agent-ug.md").

### Dataflow endpoint application

A networking application that is used by AWS Ground Station to send and receive data
between the AWS Ground Station antenna locations, and your Amazon EC2 instances. It can be used for the
uplink and downlink of data.

### Software Defined Radio (SDR)

A software defined radio (SDR) that can be used to modulate/demodulate the signal
used to communicate with your satellite.

## AWS Ground Station Amazon Machine Images (AMIs)

To reduce the build and configuration times of these installs, AWS Ground Station also offers
preconfigured AMIs. The AMIs with a dataflow endpoint networking application and a software
defined radio (SDR) are made available to your account after your onboarding is complete.
They can be found in the Amazon EC2 console by searching for
_groundstation_ in private
[Amazon Machine Images (AMIs)](https://console.aws.amazon.com/ec2/home?#Images:visibility=private;search=groundstation;sort=imageName "https://console.aws.amazon.com/ec2/home?#Images:visibility=private;search=groundstation;sort=imageName").
The AMIs with AWS Ground Station Agent are public and can be found in the Amazon EC2 console by searching for
_groundstation_ in public
[Amazon Machine Images (AMIs)](https://console.aws.amazon.com/ec2/home?#Images:visibility=public-images;search=groundstation;sort=imageName "https://console.aws.amazon.com/ec2/home?#Images:visibility=public-images;search=groundstation;sort=imageName").
