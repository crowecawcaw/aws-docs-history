# Network

Ensure that you have your network constructs set up to deploy resources related to SAP NetWeaver. If you haven’t already set up network components, such as Amazon VPC, subnets, and route tables, you can use the [AWS Quick Start for Modular and Scalable VPC Architecture](https://aws.amazon.com/quickstart/architecture/vpc/ "https://aws.amazon.com/quickstart/architecture/vpc/") to easily deploy scalable VPC architecture in minutes. See the deployment guide for more details, then set up your EC2 instances for the NetWeaver application server within this VPC.

You also will need to set up a secured network connection between the corporate data center and the VPC, along with the appropriate route table configuration, if this has not already been configured.
