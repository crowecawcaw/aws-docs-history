# Setting up VPC endpoints with

Amazon SES

Many Amazon SES customers have corporate policies in place that limit the ability of their
internal systems to connect to the public internet. These policies prevent the use of the
public Amazon SES endpoints.

If you have similar policies, you can work within these restrictions by using Amazon Virtual Private Cloud.
With Amazon VPC, you can deploy AWS resources into a virtual network that exists in an isolated
area of the AWS Cloud. For more information about Amazon VPC, see the [Amazon VPC User Guide](../../../vpc/latest/userguide.md "../../../vpc/latest/userguide.md").

You can connect directly from [Amazon VPC](https://aws.amazon.com/vpc/ "https://aws.amazon.com/vpc/") to
SES through a [VPC Endpoint](../../../vpc/latest/privatelink/concepts.md#concepts-vpc-endpoints "../../../vpc/latest/privatelink/concepts.md#concepts-vpc-endpoints") in a secure and scalable manner. When you use an interface VPC
endpoint, it provides a better security posture as you don't need to open outbound traffic
firewalls as well as providing other benefits of using [Amazon VPC endpoints](https://aws.amazon.com/blogs/architecture/reduce-cost-and-increase-security-with-amazon-vpc-endpoints/ "https://aws.amazon.com/blogs/architecture/reduce-cost-and-increase-security-with-amazon-vpc-endpoints/").

When using a VPC Endpoint, traffic to SES does not transmit over the internet and
never leaves the Amazon network in order to securely connect your VPC to SES without
availability risks or bandwidth constraints on your network traffic. You can centralize
SES across your multi-account infrastructure and provide it as a service to your
accounts without the need to utilize an internet gateway.

###### Limitations

- SES does not support SMTP VPC endpoints in the following Availability Zones:
  `use1-az2`, `use1-az3`, `use1-az5`,
  `usw1-az2`, `usw2-az4`, `apne2-az4`,
  `cac1-az3`, and `cac1-az4`.
- The SMTP endpoint used within the VPC is restricted to the AWS Region
  currently being used for your account.
  You can also use VPC endpoints with Mail Manager ingress endpoints for secure, private email
  ingestion within your private network infrastructure. See [Receiving email through Amazon VPC
  endpoints](eb-ingress.md#eb-ingress-vpc-endpoint "eb-ingress.md#eb-ingress-vpc-endpoint") in the Mail Manager chapter.

## Walkthrough example of

setting up SES in Amazon VPC

### Prerequisites

Before you complete the procedure in this section, you have to complete the
following steps:

- Have an existing virtual private cloud (VPC) or create a new VPC. For
  procedures, see [Get
  started with Amazon VPC](../../../vpc/latest/userguide/vpc-getting-started.md "../../../vpc/latest/userguide/vpc-getting-started.md").
- Launch an Amazon EC2 instance in your VPC for testing connectivity to the VPC
  endpoint created in a later step. For more information, see [Default
  VPCs](../../../vpc/latest/userguide/default-vpc.md#launching-into "../../../vpc/latest/userguide/default-vpc.md#launching-into").

###### Note

While VPC endpoints for SES can be used with any resource, for
ease of test method, this example will have you use an EC2 instance as
the resource. Because Amazon EC2 restricts email traffic over port 25 by
default, for SMTP endpoints you'll have to use a different port other than TCP 25, such as
TCP 465, 587, 2465, or 2587—for more information, see [Restriction on email sent using port 25](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#port-25-throttle "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#port-25-throttle"). For API endpoints use port 443.

### Setting up SES in

Amazon VPC

The process of setting up a VPC endpoint to use with SES consists of a few
separate steps. First, you have to
create a security group that allows the instance to communicate with the chosen port(s),
then create a VPC endpoint for Amazon SES, and finally, test the connection to the VPC
endpoint to ensure that it's configured properly.

#### Step 1:

Create the security group

In this step,
you create a security group that lets Amazon EC2 instances communicate with VPC
interface endpoint you'll be creating.

###### To create the security group

1. In the navigation pane of the Amazon EC2 console, under **Network
   & Security**, choose **Security
   Groups**.
2. Choose **Create security group**.
3. Under **Basic details**, do the following:
   - For **Security group name**, enter a unique
     name that identifies the security group.
   - For **Description**, enter some text that
     describes the purpose of the security group.
   - For **VPC**, choose the VPC that you want to
     use Amazon SES in.

4. Under **Inbound rules**, choose **Add
   rule**.
5. For the new **Inbound rule**, do the
   following:
   - For **Type**, choose **Custom
     TCP**.
   - For **Port range**, enter the port number
     that you want to use to send email. For SMTP endpoints, you can use any of the
     following port numbers: `465`,
     `587`, `2465`, or
     `2587`. For API endpoints, use port 443.
   - For **Source type**, choose
     **Custom**.
   - For **Source**, enter the private IP CIDR
     range or other Security Group IDs that contain the resources
     that will use the VPC endpoint to communicate with the
     SES service.
   - (Repeat steps 4 - 5 for each CIDR range or Security Group you
     wish to allow access from.)

6. When you finish, choose **Create security
   group**.

#### Step 2:

Create the VPC endpoint

In Amazon VPC, a _VPC endpoint_ lets you connect your VPC to
supported AWS services. In this example, you configure Amazon VPC so that your
Amazon EC2 security group can connect to Amazon SES.

###### To create the VPC endpoint

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Under **PrivateLink and Lattice**, choose
   **Endpoints**.
3. Choose **Create Endpoint** to open the
   **Create Endpoint** page.
4. (Optional) In the **Endpoint settings** panel, create
   a tag in the **Name tag** field.
5. For **Service category**, select **AWS
   services**.
6. In the **Services** panel, for SMTP endpoints, filter on
   _smtp_ in the search bar, then select its radio
   button. For API endpoints, filter on _email_ in the search bar. You can also use a FIPS endpoint by searching for _email-fips_.
7. In the **VPC** panel, click inside the search bar and
   select a VPC from the list box (see [Prerequisites](#send-email-set-up-vpc-endpoints-prereqs "#send-email-set-up-vpc-endpoints-prereqs")).
8. In the **Subnets** panel, select
   _Availability Zones_ and _Subnet
   IDs_.

###### Note

Amazon SES doesn't support SMTP VPC endpoints in the following
_Availability Zones_: `use1-az2`,
`use1-az3`, `use1-az5`,
`usw1-az2`, `usw2-az4`,
`apne2-az4`, `cac1-az3`, and
`cac1-az4`. 9. In the **Security groups** panel, select the security
group you created earlier. 10. (Optional) In the **Tags** panel, you can create one
or more tags. 11. Choose **Create endpoint**. Wait approximately 5
minutes while Amazon VPC creates the endpoint. When the endpoint is ready to
use, the value in the **Status** column changes to
_Available_.

#### (Optional)

Step 3: Test the connection to the VPC endpoint

When you complete the process of configuring the VPC endpoint, you can test
the connection to ensure that the VPC endpoint is configured properly. You can
test the connection by using command-line tools that are included with most
operating systems.

###### To test the connection to the VPC endpoint

1. Launch an Amazon EC2 instance in the same VPC where you just created
   the email-smtp VPC endpoint.

For information about connecting to Linux instances, see [Connect to your Linux
instance](../../../AWSEC2/latest/UserGuide/AccessingInstances.md "../../../AWSEC2/latest/UserGuide/AccessingInstances.md") in the _Amazon EC2 User Guide_.

For information about connecting to Windows instances, see the [Get started tutorial](../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows "../../../AWSEC2/latest/WindowsGuide/EC2_GetStarted.md#ec2-connect-to-instance-windows") in the
_Amazon EC2 User Guide_. 2. Send a test email. For the SMTP endpoint, use the SES SMTP interface. For the API endpoint, use the SES CLI or API.

###### Note

You have to verify an email address or domain before you can send
email through Amazon SES. For more information about verifying
identities, see [Creating and verifying identities in Amazon SES](creating-identities.md "creating-identities.md").
