

# Set up and configure Amazon EC2
<a name="dataflows.ec2-configuration"></a>

 Properly configuring your Amazon EC2 instance is required for synchronous delivery of VITA-49 Signal/IP data or VITA-49 Extension data/IP to be delivered via the AWS Ground Station Agent or a dataflow endpoint. Depending on your specific needs, you may perform the Front End (FE) processor or Software Defined Radio (SDR) directly on the same instance, or you may need to utilize additional EC2 instances. Selection and installation of your FE or SDR is beyond the scope of this user guide. For more information on the specific data formats, see [AWS Ground Station data plane interfaces](dataflows.md#dataflows.interfaces). 

For information about our service terms, please see [AWS Service Terms](https://aws.amazon.com/service-terms).

## Supplied Common Software
<a name="dataflows.ec2-configuration.common-software"></a>

AWS Ground Station provides common software to ease setup of your Amazon EC2 instance.

### AWS Ground Station Agent
<a name="dataflows.ec2-configuration.common-software.gs-agent"></a>

 The AWS Ground Station Agent receives Digital Intermediate Frequency (DigIF) downlink data and egresses decrypted data that enables the following: 
+ DigIF downlink capability from 40 MHz to 400 MHz of bandwidth.
+ High rate, low jitter DigIF data delivery to any public IP (AWS Elastic IP) on the AWS network.
+ Reliable data delivery using Forward Error Correction (FEC).
+ Secure data delivery using a customer managed AWS KMS key for encryption.

For more information, see [AWS Ground Station Agent User Guide](https://docs.aws.amazon.com/ground-station/latest/gs-agent-ug).

### Dataflow endpoint application
<a name="dataflows.ec2-configuration.common-software.dataflow-endpoint-application"></a>

A networking application that is used by AWS Ground Station to send and receive data between the AWS Ground Station antenna locations, and your Amazon EC2 instances. It can be used for the uplink and downlink of data.

### Software Defined Radio (SDR)
<a name="dataflows.ec2-configuration.common-software.software-defined-radio"></a>

A software defined radio (SDR) that can be used to modulate/demodulate the signal used to communicate with your satellite.

## AWS Ground Station Amazon Machine Images (AMIs)
<a name="dataflows.ec2-configuration.amis"></a>

To reduce the build and configuration times of these installs, AWS Ground Station also offers preconfigured AMIs. The AMIs with a dataflow endpoint networking application and a software defined radio (SDR) are made available to your account after your onboarding is complete. They can be found in the Amazon EC2 console by searching for *groundstation* in private [Amazon Machine Images (AMIs)](https://console.aws.amazon.com/ec2/home?#Images:visibility=private;search=groundstation;sort=imageName). The AMIs with AWS Ground Station Agent are public and can be found in the Amazon EC2 console by searching for *groundstation* in public [Amazon Machine Images (AMIs)](https://console.aws.amazon.com/ec2/home?#Images:visibility=public-images;search=groundstation;sort=imageName). 