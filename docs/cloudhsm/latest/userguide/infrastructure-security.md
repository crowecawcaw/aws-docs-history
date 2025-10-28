# Infrastructure security in AWS CloudHSM

As a managed service, AWS CloudHSM is protected by the AWS global network security
procedures that are described in the [Amazon Web Services: Overview of Security Processes](https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf "https://d0.awsstatic.com/whitepapers/Security/AWS_Security_Whitepaper.pdf") whitepaper.

You use AWS published API calls to access AWS CloudHSM through the network. Additionally, requests must be signed by using
an access key ID and a secret access key that is associated with an IAM principal. Or you
can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate
temporary security credentials to sign requests.

## Network isolation

A virtual private cloud (VPC) is a virtual network in your own logically isolated area
in the AWS cloud. You can create a cluster in a private subnet in your VPC. You can create private subnets when you create a VPC. For more
information, see [Create a virtual private cloud (VPC) for AWS CloudHSM](create-vpc.md "create-vpc.md").

When you create an HSM, AWS CloudHSM put an elastic network interface (ENI) in your
subnet so that you can interact with your HSMs. For more information, see [AWS CloudHSM cluster architecture](cluster-architecture.md "cluster-architecture.md").

AWS CloudHSM creates a security group that allows inbound and outbound communication between
HSMs in your cluster. You can use this security group to enable your EC2 instances to
communicate with the HSMs in your cluster. For more information, see [Configure the Client Amazon EC2 instance security
groups for AWS CloudHSM](configure-sg-client-instance.md "configure-sg-client-instance.md").

## Authorization of users

With AWS CloudHSM, operations performed on the HSM require the credentials of an authenticated
HSM user. For more information, see [HSM user types for CloudHSM CLI](understanding-users.md "understanding-users.md").
