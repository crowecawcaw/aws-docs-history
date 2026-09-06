

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Subnet or VPC with no internet access
<a name="mf-runtime-setup-no-access"></a>

Make these additional changes if the subnet or VPC does not have outbound Internet access.

The license manager requires access to the following AWS services:
+ com.amazonaws.{{region}}.s3
+ com.amazonaws.{{region}}.ec2
+ com.amazonaws.{{region}}.license-manager
+ com.amazonaws.{{region}}.sts

The earlier steps defined the com.amazonaws.{{region}}.s3 service as a gateway endpoint. This endpoint needs a route table entry for any subnets without Internet access.

The additional three services will be defined as interface endpoints.

**Topics**
+ [Add the Route table entry for the Amazon S3 endpoint](#mf-runtime-setup-no-access-route-table)
+ [Define the required security group](#mf-runtime-setup-no-access-security-group)
+ [Create the service endpoints](#mf-runtime-setup-no-access-endpoints)

## Add the Route table entry for the Amazon S3 endpoint
<a name="mf-runtime-setup-no-access-route-table"></a>

1. Navigate to **VPC** in the AWS Management Console and choose **Subnets**.

1. Choose the subnet where the Amazon EC2 instances will be created and choose the Route Table tab.

1. Note a few trailing digits of the Route table id. For example, the 6b39 in the image below.  
![Route table details.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_1.png)

1. Choose **Endpoints** from the navigation pane.

1. Choose the endpoint created earlier and then **Manage Route tables**, either from the Route Tables tab for the endpoint, or from the Actions drop down.

1. Choose the Route table using the digits identified earlier and press Modify route tables.  
![Route table selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_2.png)

## Define the required security group
<a name="mf-runtime-setup-no-access-security-group"></a>

The Amazon EC2, AWS STS, and License Manager services communicate over HTTPS via port 443. This communication is bi-directional and requires inbound and outbound rules to allow the instance to communicate with the services.

1. Navigate to Amazon VPC in the AWS Management Console.

1. Locate **Security Groups** in the navigation bar and choose **Create security group**.

1. Enter a Security group name and description, for example “Inbound-Outbound HTTPS”.

1. Press the X in the VPC selection area to **remove the default VPC**, and choose the VPC that contains the S3 endpoint.

1. Add an Inbound Rule that **allows TCP traffic on Port 443** from anywhere.
**Note**  
The inbound (and outbound rules) can be restricted further by limiting the Source. For more information, see [Control traffic to your AWS resources using security groups](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html) in the *Amazon VPC User Guide*.  

![Basic details with inbound rule entered.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_3.png)


1. Press **Create security group**.

## Create the service endpoints
<a name="mf-runtime-setup-no-access-endpoints"></a>

Repeat this process three times – once for each service.

1. Navigate to Amazon VPC in the AWS Management Console and choose **Endpoints**.

1. Press **Create endpoint**.

1. Enter a name, for example “Micro-Focus-License-EC2”, “Micro-Focus-License-STS”, or “Micro-Focus-License-Manager”.

1. Choose the **AWS Services** Service Category.  
![Endpoint settings with AWS services selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_4.png)

1. Under Services search for the matching Interface service which is one of:
   + “com.amazonaws.{{region}}.ec2”
   + “com.amazonaws.{{region}}.sts”
   + “com.amazonaws.{{region}}.license-manager”

   For example:
   + “com.amazonaws.us-west-1.ec2”
   + “com.amazonaws.us-west-1.sts”
   + “com.amazonaws.us-west-1.license-manager”

1. Choose the matching Interface service.

   **com.amazonaws.{{region}}.ec2**:  
![Services with Amazon EC2 interface service selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_5.png)

   **com.amazonaws.{{region}}.sts:**  
![Services with AWS STS interface service selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_6.png)

   **com.amazonaws.{{region}}.license-manager:**  
![Services with License Manager interface service selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_7.png)

1. For VPC choose the VPC for the instance.  
![VPC with the VPC for the instance selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_8.png)

1. Choose the **Availability Zone** and the **Subnets** for the VPC.  
![Subnets with availability zone and subnet for the VPC selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_9.png)

1. Choose the Security Group created earlier.  
![Security groups with security group selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_10.png)

1. Under Policy choose **Full Access**.  
![Policy with Full Access selected.](http://docs.aws.amazon.com/m2/latest/userguide/images/mf-no-internet_11.png)

1. Choose **Create Endpoint**.

1. Repeat this process for the remaining interfaces.