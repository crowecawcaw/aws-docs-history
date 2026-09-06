

# Remote Desktop for Electronic Design Automation
<a name="remote-desktop-eda"></a>

Publication date: **April 5, 2021 ([Diagram history](#remote-eda-history))**

With this architecture, you can launch the Xilinx Vivado Design Suite by using [Amazon DCV](https://docs.aws.amazon.com/dcv/latest/adminguide/) remote desktop on AWS. The solution uses the FPGA Developer Amazon Machine Image (AMI) from [AWS Marketplace](https://docs.aws.amazon.com/marketplace/latest/buyerguide/), which includes Vivado pre-installed.

For more information about this workshop, see [aws-remote-desktop-for-eda](https://github.com/aws-samples/aws-remote-desktop-for-eda) on GitHub.

## Remote desktop for Electronic Design Automation diagram
<a name="remote-eda-diagram"></a>

![Reference architecture diagram showing how to launch Xilinx Vivado by using Amazon DCV remote desktop on AWS with CloudFormation and Amazon S3.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/remote-desktop-eda/images/remote-desktop-eda.png)


The following steps describe the setup and connection flow for this architecture:

1. Subscribe to the FPGA Developer AMI in AWS Marketplace. The Xilinx Vivado Design Suite is included with this AMI.

1. Specify required parameters (Amazon VPC, subnet, Availability Zone) and launch the [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) stack.

1. (Optional) Create an Elastic IP address for a persistent IP.

1. Choose a remote desktop instance type that works for your tools.

1. Connect to Amazon DCV by using the Amazon DCV client or a web browser on port 8443.

1. In the FPGA Developer AMI, launch the Xilinx Vivado Design Suite by typing `vivado` in a terminal window.

1. The remote desktop displays on your local system.

1. (Optional) Configure [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket access to load design data.

1. (Optional) Specify additional existing security groups.

## Further reading
<a name="remote-eda-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="remote-eda-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#remote-eda-history) | Reference architecture diagram first published. | April 5, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.