# Network

Ensure that you have your network constructs set up to deploy resources related to your SAP workload. If you haven’t already set up network components like Amazon Virtual Private Cloud (Amazon VPC), subnets, route tables and so on., you can use the [AWS Quick Start for Modular and Scalable VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/") to easily deploy scalable VPC architecture in minutes. Refer to the deployment guide for more details, then set up your EC2 instances for the SAP workload within this VPC.

You must also set up a secured network connection between the corporate datacenter and the VPC, along with appropriate route table configuration, if this is not already configured.
