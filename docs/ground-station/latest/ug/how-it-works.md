# Use AWS Ground Station Agent

The AWS Ground Station Agent enables you to receive (downlink) synchronous Wideband Digital
Intermediate Frequency (DigIF) dataflows during AWS Ground Station contacts.

## How it works

You can select two options for data delivery:

1. **Data delivery to an EC2 instance** - Data delivery to an EC2 instance that you own. You manage the AWS Ground Station Agent.
   This option may suit you best if you need near real-time data processing. See the [Work with dataflows](dataflows.md "dataflows.md") section for information about EC2 data delivery.
2. **Data delivery to an S3 bucket** - Data delivery to your AWS S3 bucket is fully managed by AWS Ground Station. See the [Get started](getting-started.md "getting-started.md") guide for information about S3 data delivery.

Both modes of data delivery require you to create a set of AWS resources.
The use of CloudFormation to create your AWS resources is highly recommended to ensure reliability, accuracy, and supportability.
Each contact can only deliver data to EC2 or S3 but not to both simultaneously.

The following diagram shows a DigIF dataflow from an AWS Ground Station Antenna Region to your EC2 instance
with your Software-Defined Radio (SDR) or similar listener.

![DigIF dataflow from an AWS Ground Station antennna region.](/images/ground-station/latest/ug/images/digif-data-delivery-overview.png)

## Additional information

For more detailed information, please see the full [AWS Ground Station Agent User Guide](../gs-agent-ug.md "../gs-agent-ug.md").
