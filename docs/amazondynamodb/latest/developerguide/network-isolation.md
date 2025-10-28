# Infrastructure security in Amazon DynamoDB

As a managed service, Amazon DynamoDB is protected by the AWS global network security
procedures that are described in [Infrastructure protection](../../../wellarchitected/latest/security-pillar/infrastructure-protection.md "../../../wellarchitected/latest/security-pillar/infrastructure-protection.md") located in the AWS Well-Architected Framework.

You use AWS published API calls to access DynamoDB through the network. Clients can use TLS (Transport Layer Security) version 1.2 or 1.3. Clients must also support cipher suites with perfect forward
secrecy (PFS) such as Ephemeral Diffie-Hellman (DHE) or Elliptic Curve Diffie-Hellman
Ephemeral (ECDHE). Most modern systems such as Java 7 and later support these modes.
Additionally, requests must be signed using an access key ID and a secret access key that is
associated with an IAM principal. Or you can use the [AWS Security Token Service](../../../STS/latest/APIReference/Welcome.md "../../../STS/latest/APIReference/Welcome.md") (AWS STS) to generate temporary security credentials to sign
requests.

You can also use a virtual private cloud (VPC) endpoint for DynamoDB to enable Amazon EC2
instances in your VPC to use their private IP addresses to access DynamoDB with no exposure to
the public internet. For more information, see [Using Amazon VPC endpoints to access DynamoDB](#vpc-endpoints-dynamodb "#vpc-endpoints-dynamodb").

## Using Amazon VPC endpoints to access DynamoDB

For security reasons, many AWS customers run their applications within an Amazon Virtual Private Cloud
environment (Amazon VPC). With Amazon VPC, you can launch Amazon EC2 instances into a virtual private
cloud, which is logically isolated from other networks—including the public internet.
With an Amazon VPC, you have control over its IP address range, subnets, routing tables, network
gateways, and security settings.

###### Note

If you created your AWS account after December 4, 2013, then you already have a
default VPC in each AWS Region. A default VPC is ready for you to use—you can
immediately start using it without having to perform any additional configuration
steps.

For more information, see [Default VPC and
Default Subnets](../../../vpc/latest/userguide/default-vpc.md "../../../vpc/latest/userguide/default-vpc.md") in the _Amazon VPC User Guide_.

To access the public internet, your VPC must have an internet gateway—a virtual router
that connects your VPC to the internet. This allows applications running on Amazon EC2 in your
VPC to access internet resources, such as Amazon DynamoDB.

By default, communications to and from DynamoDB use the HTTPS protocol, which protects
network traffic by using SSL/TLS encryption. The following diagram shows an Amazon EC2 instance
in a VPC accessing DynamoDB, by having DynamoDB use an internet gateway rather than VPC
endpoints.

![Workflow diagram showing an Amazon EC2 instance accessing DynamoDB through a router, internet gateway, and the internet.](images/ddb-no-vpc-endpoint.png)

Many customers have legitimate privacy and security concerns about sending and receiving
data across the public internet. You can address these concerns by using a virtual private
network (VPN) to route all DynamoDB network traffic through your own corporate network
infrastructure. However, this approach can introduce bandwidth and availability
challenges.

VPC endpoints for DynamoDB can alleviate these challenges. A _VPC
endpoint_ for DynamoDB enables Amazon EC2 instances in your VPC to use their private
IP addresses to access DynamoDB with no exposure to the public internet. Your EC2 instances do
not require public IP addresses, and you don't need an internet gateway, a NAT device, or a
virtual private gateway in your VPC. You use endpoint policies to control access to DynamoDB.
Traffic between your VPC and the AWS service does not leave the Amazon network.

###### Note

Even when you use public IP addresses, all VPC communication between instances and
services hosted in AWS is kept private within the AWS network. Packets that
originate from the AWS network with a destination on the AWS network stay on the
AWS global network, except traffic to or from AWS China Regions.

When you create a VPC endpoint for DynamoDB, any requests to a DynamoDB endpoint within the
Region (for example, _dynamodb.us-west-2.amazonaws.com_) are routed to a
private DynamoDB endpoint within the Amazon network. You don't need to modify your applications
running on EC2 instances in your VPC. The endpoint name remains the same, but the route to
DynamoDB stays entirely within the Amazon network, and does not access the public internet.

The following diagram shows how an EC2 instance in a VPC can use a VPC endpoint to access
DynamoDB.

![Workflow diagram showing an EC2 instance accessing DynamoDB through a router and VPC endpoint only.](images/ddb-yes-vpc-endpoint.png)

For more information, see [Tutorial: Using a VPC endpoint for
DynamoDB](#vpc-endpoints-dynamodb-tutorial "#vpc-endpoints-dynamodb-tutorial").

### Sharing Amazon VPC endpoints and

DynamoDB

In order to enable access to the DynamoDB service through a VPC subnet's gateway
endpoint, you must have owner account permissions for that VPC subnet.

Once the VPC subnet’s gateway endpoint has been granted access to DynamoDB, any AWS
account with access to that subnet can use DynamoDB. This means all account users within
the VPC subnet can use any DynamoDB tables which they have access to. This includes DynamoDB
tables associated with a different account than the VPC subnet. The VPC subnet owner can
still restrict any particular user within the subnet from using the DynamoDB service
through the gateway endpoint, at their discretion.

### Tutorial: Using a VPC endpoint for

DynamoDB

This section walks you through setting up and using a VPC endpoint for DynamoDB.

###### Topics

- [Step 1: Launch
  an Amazon EC2 instance](#vpc-endpoints-dynamodb-tutorial.launch-ec2-instance "#vpc-endpoints-dynamodb-tutorial.launch-ec2-instance")
- [Step 2:
  Configure your Amazon EC2 instance](#vpc-endpoints-dynamodb-tutorial.configure-ec2-instance "#vpc-endpoints-dynamodb-tutorial.configure-ec2-instance")
- [Step 3: Create a
  VPC endpoint for DynamoDB](#vpc-endpoints-dynamodb-tutorial.create-endpoint "#vpc-endpoints-dynamodb-tutorial.create-endpoint")
- [Step 4: (Optional) Clean
  up](#vpc-endpoints-dynamodb-tutorial.clean-up "#vpc-endpoints-dynamodb-tutorial.clean-up")

#### Step 1: Launch

an Amazon EC2 instance

In this step, you launch an Amazon EC2 instance in your default Amazon VPC. You can then
create and use a VPC endpoint for DynamoDB.

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. Choose **Launch Instance** and do the following:

Step 1: Choose an Amazon Machine Image
(AMI)

    * At the top of the list of AMIs, go to **Amazon Linux
     AMI** and choose **Select**.

Step 2: Choose an Instance Type

    * At the top of the list of instance types, choose
     **t2.micro**.
    * Choose **Next: Configure Instance
     Details**.

Step 3: Configure Instance Details

    * Go to **Network** and choose your default
     VPC.


    Choose **Next: Add Storage**.

Step 4: Add Storage

    * Skip this step by choosing **Next: Tag
     Instance**.

Step 5: Tag Instance

    * Skip this step by choosing **Next: Configure Security
     Group**.

Step 6: Configure Security Group

    * Choose **Select an existing security
     group**.
    * In the list of security groups, choose
     **default**. This is the default security group
     for your VPC.
    * Choose **Next: Review and Launch**.

Step 7: Review Instance Launch

    * Choose **Launch**.

3. In the **Select an existing key pair or create a new key
   pair** window, do one of the following:
   - If you do not have an Amazon EC2 key pair, choose **Create a
     new key pair** and follow the instructions. You will be
     asked to download a private key file (_.pem_
     file); you will need this file later when you log in to your Amazon EC2
     instance.
   - If you already have an existing Amazon EC2 key pair, go to
     **Select a key pair** and choose your key pair
     from the list. You must already have the private key file (
     _.pem_ file) available in order to log in to
     your Amazon EC2 instance.

4. When you have configured your key pair, choose **Launch
   Instances**.
5. Return to the Amazon EC2 console home page and choose the instance that you
   launched. In the lower pane, on the **Description** tab,
   find the **Public DNS** for your instance. For example:
   `ec2-00-00-00-00.us-east-1.compute.amazonaws.com`.

Make a note of this public DNS name, because you will need it in the next
step in this tutorial ([Step 2:
Configure your Amazon EC2 instance](#vpc-endpoints-dynamodb-tutorial.configure-ec2-instance "#vpc-endpoints-dynamodb-tutorial.configure-ec2-instance")).

###### Note

It will take a few minutes for your Amazon EC2 instance to become available. Before
you go on to the next step, ensure that the **Instance State**
is `running` and that all of its **Status Checks**
have passed.

#### Step 2:

Configure your Amazon EC2 instance

When your Amazon EC2 instance is available, you will be able to log into it and prepare
it for first use.

###### Note

The following steps assume that you are connecting to your Amazon EC2 instance from
a computer running Linux. For other ways to connect, see [Connect to Your Linux
Instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the Amazon EC2 User Guide.

1.  You will need to authorize inbound SSH traffic to your Amazon EC2 instance. To
    do this, you will create a new EC2 security group, and then assign the
    security group to your EC2 instance.
    1.  In the navigation pane, choose **Security
        Groups**.
    2.  Choose **Create Security Group**. In the
        **Create Security Group** window, do the
        following:

            * **Security group name**—type a name
             for your security group. For example:
             `my-ssh-access`
            * **Description**—type a short
             description for the security group.
            * **VPC**—choose your default
             VPC.
            * In the **Security group rules** section,
             choose **Add Rule** and do the
             following:




            	+ **Type**—choose SSH.
            	+ **Source**—choose My
            	 IP.

        When the settings are as you want them, choose
        **Create**.

    3.  In the navigation pane, choose
        **Instances**.
    4.  Choose the Amazon EC2 instance that you launched in [Step 1: Launch
        an Amazon EC2 instance](#vpc-endpoints-dynamodb-tutorial.launch-ec2-instance "#vpc-endpoints-dynamodb-tutorial.launch-ec2-instance").
    5.  Choose **Actions** -->
        **Networking** --> **Change Security
        Groups**.
    6.  In the **Change Security Groups**, select the
        security group that you created earlier in this procedure (for
        example: `my-ssh-access`). The existing
        `default` security group should also be selected.
        When the settings are as you want them, choose **Assign
        Security Groups**.

2.  Use the `ssh` command to log in to your Amazon EC2 instance, as in
    the following example.

```
ssh -i `my-keypair.pem` ec2-user@`public-dns-name`
```

You will need to specify your private key file (_.pem_
file) and the public DNS name of your instance. (See [Step 1: Launch
an Amazon EC2 instance](#vpc-endpoints-dynamodb-tutorial.launch-ec2-instance "#vpc-endpoints-dynamodb-tutorial.launch-ec2-instance")).

The login ID is `ec2-user`. No password is required. 3. Configure your AWS credentials as shown in the following example. Enter your AWS
access key ID, secret key, and default Region name when prompted.

```
`aws configure`
```

```
AWS Access Key ID [None]: `AKIAIOSFODNN7EXAMPLE`
AWS Secret Access Key [None]: `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY`
Default region name [None]: `us-east-1`
Default output format [None]:
```

You are now ready to create a VPC endpoint for DynamoDB.

#### Step 3: Create a

VPC endpoint for DynamoDB

In this step, you will create a VPC endpoint for DynamoDB and test it to make sure
that it works.

1. Before you begin, verify that you can communicate with DynamoDB using its
   public endpoint.

```
`aws dynamodb list-tables`
```

The output will show a list of DynamoDB tables that you currently own. (If
you don't have any tables, the list will be empty.). 2. Verify that DynamoDB is an available service for creating VPC endpoints in
the current AWS Region. (The command is shown in bold text, followed by
example output.)

```
`aws ec2 describe-vpc-endpoint-services`
```

```
{
    "ServiceNames": [
        "com.amazonaws.us-east-1.s3",
        "com.amazonaws.us-east-1.dynamodb"
    ]
}
```

In the example output, DynamoDB is one of the services available, so you can
proceed with creating a VPC endpoint for it. 3. Determine your VPC identifier.

```
`aws ec2 describe-vpcs`
```

```
{
    "Vpcs": [
        {
            "VpcId": "vpc-0bbc736e",
            "InstanceTenancy": "default",
            "State": "available",
            "DhcpOptionsId": "dopt-8454b7e1",
            "CidrBlock": "172.31.0.0/16",
            "IsDefault": true
        }
    ]
}
```

In the example output, the VPC ID is `vpc-0bbc736e`. 4. Create the VPC endpoint. For the `--vpc-id` parameter, specify
the VPC ID from the previous step. Use the `--route-table-ids`
parameter to associate the endpoint with your route tables.

```
`aws ec2 create-vpc-endpoint --vpc-id vpc-0bbc736e --service-name com.amazonaws.us-east-1.dynamodb --route-table-ids rtb-11aa22bb`
```

```
{
    "VpcEndpoint": {
        "PolicyDocument": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"*\",\"Resource\":\"*\"}]}",
        "VpcId": "vpc-0bbc736e",
        "State": "available",
        "ServiceName": "com.amazonaws.us-east-1.dynamodb",
        "RouteTableIds": [
            "rtb-11aa22bb"
        ],
        "VpcEndpointId": "vpce-9b15e2f2",
        "CreationTimestamp": "2017-07-26T22:00:14Z"
    }
}
```

5. Verify that you can access DynamoDB through the VPC endpoint.

```
`aws dynamodb list-tables`
```

If you want, you can try some other AWS CLI commands for DynamoDB. For more
information, see the [AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md").

#### Step 4: (Optional) Clean

up

If you want to delete the resources you have created in this tutorial, follow
these procedures:

###### To remove your VPC endpoint for DynamoDB

1. Log in to your Amazon EC2 instance.
2. Determine the VPC endpoint ID.

```
`aws ec2 describe-vpc-endpoints`
```

```
{
    "VpcEndpoint": {
        "PolicyDocument": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"*\",\"Resource\":\"*\"}]}",
        "VpcId": "vpc-0bbc736e",
        "State": "available",
        "ServiceName": "com.amazonaws.us-east-1.dynamodb",
        "RouteTableIds": [],
        "VpcEndpointId": "vpce-9b15e2f2",
        "CreationTimestamp": "2017-07-26T22:00:14Z"
    }
}
```

In the example output, the VPC endpoint ID is
`vpce-9b15e2f2`. 3. Delete the VPC endpoint.

```
`aws ec2 delete-vpc-endpoints --vpc-endpoint-ids vpce-9b15e2f2`
```

```
{
    "Unsuccessful": []
}
```

The empty array `[]` indicates success (there were no
unsuccessful requests).

###### To terminate your Amazon EC2 instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Choose your Amazon EC2 instance.
4. Choose **Actions**, **Instance State**,
   **Terminate**.
5. In the confirmation window, choose **Yes,
   Terminate**.
