# Overview

## What is the AWS Ground Station Agent?

With the AWS Ground Station Agent, available as an RPM, you can receive (downlink) synchronous Wideband Digital Intermediate Frequency (DigIF) dataflows during AWS Ground Station contacts.
You can select two options for data delivery:

1. **Data delivery to an EC2 instance** - Data delivery to an EC2 instance that you own. You manage the AWS Ground Station Agent.
   This option may suit you best if you need near real-time data processing. See the [Data Delivery to Amazon Elastic Compute Cloud](../ug/ec2-data-delivery.md "../ug/ec2-data-delivery.md") guide for information about EC2 data delivery.
2. **Data delivery to an S3 bucket** - Data delivery to an AWS S3 bucket that you own via a Ground Station managed service. See the [Getting started with AWS Ground Station](../ug/getting-started.md "../ug/getting-started.md") guide for information about S3 data delivery.

Both modes of data delivery require you to create a set of AWS resources.
The use of CloudFormation to create your AWS resources is highly recommended to ensure reliability, accuracy, and supportability.
Each contact can only deliver data to EC2 or S3 but not to both simultaneously.

###### Note

Since S3 data delivery is a Ground Station managed service, this guide focuses on data delivery to your EC2 instance(s).

The following diagram shows a DigIF dataflow from an AWS Ground Station Antenna Region to your EC2 instance
with your Software-Defined Radio (SDR) or similar listener.

![DigIF dataflow from an AWS Ground Station Antenna Region to your EC2 instance with your Software-Defined Radio (SDR) or similar listener.](images/digif-data-delivery-overview.png)

## Features of the AWS Ground Station Agent

The AWS Ground Station Agent receives Digital Intermediate Frequency (DigIF) downlink data and egresses decrypted data that enables the following:

- DigIF downlink capability from 40 MHz to 400 MHz of bandwidth.
- High rate, low jitter DigIF data delivery to any public IP (AWS Elastic IP) on the AWS network.
- Reliable data delivery using Forward Error Correction (FEC).
- Secure data delivery using a customer managed AWS KMS key for encryption.
