

# Get Started with Cross-Account AWS License Manager using Shared AWS Managed Microsoft AD
<a name="license-cross-account"></a>

AWS License Manager supports cross-account functionality using a shared AWS Managed Microsoft AD, enabling organizations to centrally manage user subscriptions from a directory owner account while deploying instances across multiple accounts.

## Terminology
<a name="cross-account-terminology"></a>
+ **Directory owner account** - license admin account where the managed AD exists and that is also responsible for managing subscriptions.
+ **Directory consumer account** - AWS accounts where you wat to launch user subscriptions instances using shared AD.

## Prerequisites
<a name="cross-account-prerequisites"></a>

Before you begin, ensure you have:
+ An AWS Managed Microsoft AD in the directory owner account - set up in directory owner account/license admin account from which you want to control subscriptions.
+ Network connectivity between your directory owner account and all of your directory consumer accounts.
+ Required IAM permissions - see [User-based subscription IAM roles](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscription-role.html).
+ Subscriptions to the required License Manager products in AWS Marketplace in the directory owner account:
  + [Visual Studio Professional 2022](https://aws.amazon.com/Marketplace/pp/prodview-zo3zltrbpgr5i)
  + [Visual Studio Enterprise 2022](https://aws.amazon.com/Marketplace/pp/prodview-dzstlnjdl3izg)
  + [Office LTSC Professional Plus](https://aws.amazon.com/Marketplace/pp/prodview-bh46d5p2hapns)
  + [Office LTSC Standard](https://aws.amazon.com/Marketplace/pp/prodview-4riznyn4eqlbw)

## Limitations
<a name="cross-account-limitations"></a>
+ User subscriptions management is restricted to the directory owner account.
+ Cross-region sharing is not supported.
+ Consolidated billing through directory owner account - all subscription costs are billed to the directory owner account, though subscriptions can exist in multiple accounts.
+ Network connectivity is required between accounts.

## Network Architecture
<a name="cross-account-architecture"></a>

![Architecture diagram showing AWS Managed Microsoft AD sharing between owner and consumer accounts.](http://docs.aws.amazon.com/license-manager/latest/userguide/images/cross-account.png)


## How to set up cross-account License Manager functionality
<a name="cross-account-process-overview"></a>

To set up cross-account License Manager functionality:

1. Set up the directory owner account/license admin account.

1. Configure directory consumer accounts.

1. Establish network connectivity.

1. Deploy instances and manage user associations.

### Step 1: Set up the Directory Owner/license admin account
<a name="cross-account-owner-setup"></a>

#### Create and share AWS Managed Microsoft AD
<a name="create-share-ad"></a>

1. Create an AWS Managed Microsoft AD in your VPC if it doesn't exist.

1. Share the directory with directory consumer accounts, as described in [Sharing your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_sharing.html).

1. Ensure that the directory is properly configured with the required users and groups.

#### Subscribe to products
<a name="subscribe-products"></a>

1. Navigate to AWS Marketplace.

1. Locate and subscribe to your needed products, Visual Studio or Office and RDS SAL.

1. Share the Visual Studio or Office subscription with the directory consumer accounts using License Manager **Create Grants**. Alternatively, you can subscribe to AWS Marketplace products in these accounts as this does not impact billing. See [Granted licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html).

1. Verify that the subscription status is active.

#### Register with License Manager
<a name="register-license-manager-owner"></a>

1. Open the License Manager console.

1. Navigate to **User-based subscriptions settings**.

1. Select **Register Identity Provider**.

1. Choose your AWS Managed Microsoft AD.

1. Complete the registration process.

### Step 2: Configure directory consumer accounts - accounts with shared AD
<a name="cross-account-child-config"></a>

#### Accept shared directory
<a name="accept-shared-directory"></a>

1. Open the AWS Directory Service console.

1. Navigate to **Shared directories**.

1. Locate and accept the shared directory invitation.

1. Note the new directory ID assigned in your account.

#### Accept MP subscription
<a name="accept-mp-subscription"></a>

In License Manager **Grants** accept the grant for AWS Marketplace products. Alternatively subscribe to AWS Marketplace products. Learn more in [CreateGrant API](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateGrant.html)).

#### Register with License Manager
<a name="register-license-manager-child"></a>

1. Open the License Manager console.

1. Navigate to **User-based subscriptions** and choose product.

1. Register using the shared directory ID and product.

1. Verify the registration status.

### Step 3: Establish networking connectivity between VPCs
<a name="cross-account-network-connectivity"></a>

To domain-join your Amazon Amazon EC2 instances to your directory, you need to establish networking connectivity between the VPCs. There are several options for establishing networking connectivity between two VPCs. This section shows you how to use Amazon VPC peering.

#### Set up VPC peering
<a name="vpc-peering-setup"></a>

1. [Create one VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/create-vpc-peering-connection.html#create-vpc-peering-connection-remote) between the directory owner VPC-0 and directory consumer VPC-1, then create another connection between the directory owner VPC-0 and directory consumer VPC-2.

1. Enable [traffic routing between the peered VPCs](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html#route-tables-vpc-peering) by adding a route to your VPC route table that points to the VPC peering connection to route traffic to the other VPC in the peering connection.

1. Configure each of the directory consumer VPC route tables by adding the peering connection with the directory owner VPC-0. If you want, you can also create and attach an Internet Gateway to your directory consumer VPCs. This enables the instances in the directory consumer VPCs to communicate with the Amazon EC2 Systems Manager agent that performs the domain join.

#### Configure security groups
<a name="security-groups-config"></a>

Configure your directory consumer VPCs' [security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html) to enable outbound traffic by adding the [AWS Managed Microsoft AD protocols and ports](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_getting_started_prereqs.html) to the outbound rules table. Also, configure your directory domain controllers VPCs' security group to enable inbound traffic by adding the AWS Managed Microsoft AD protocols and ports to the inbound rules table, to allow traffic from directory consumer accounts.

##### Security group requirements
<a name="security-group-requirements"></a>

**Consumer Account VPCs:**
+ Enable outbound traffic to directory owner VPC
+ Allow communication on required AD ports

**Directory Owner VPC:**
+ Configure inbound traffic from consumer VPCs
+ Add necessary AWS Managed Microsoft AD protocols and ports including:
  + TCP 53 (DNS)
  + UDP 53 (DNS)
  + TCP 88 (Kerberos)
  + UDP 88 (Kerberos)
  + TCP 135 (RPC)
  + TCP 389 (LDAP)
  + UDP 389 (LDAP)
  + TCP 445 (SMB)
  + TCP 464 (Kerberos Password)
  + UDP 464 (Kerberos Password)
  + TCP 636 (LDAPS)
  + TCP 9389 (Active Directory Web Services)
  + TCP 3268-3269 (Global Catalog)
  + TCP 1024-65535 (Dynamic RPC)

Port 9389 is required for Active Directory Web Services (ADWS), which is used by the Active Directory PowerShell module and other management tools to communicate with domain controllers.

### Step 4: Deploy instances and manage user associations
<a name="cross-account-deploy-manage"></a>

#### Subscribe users (directory owner account only)
<a name="subscribe-users"></a>

1. Open the License Manager console.

1. Navigate to **User-based subscriptions**.

1. Select **Subscribe Users**

1. Enter AWS Managed Microsoft AD user identifiers

1. Choose the product and confirm subscription.

#### Launch instances
<a name="launch-instances"></a>

Perform this step in any account.

1. Navigate to Amazon EC2 console.

1. Choose **Launch Instance**.

1. Select appropriate License Manager AMI.

1. Configure networking settings.

1. Review and launch.

#### Associate users with instances
<a name="associate-users-instances"></a>

Perform this step in any account where the instance exists.

1. Open License Manager console.

1. Navigate to **User Associations**.

1. Select target instance.

1. Choose **Associate Users**.

1. Enter AWS Managed Microsoft AD usernames.

1. Confirm association.

## Troubleshooting
<a name="cross-account-troubleshooting"></a>

Common issues and solutions:

### Domain join failures
<a name="domain-join-failures"></a>

1. Verify network connectivity between accounts.

1. Check security group configurations.

1. Confirm DNS resolution is working.

1. Validate route table entries.

### User subscription issues
<a name="user-subscription-issues"></a>

1. Confirm user exists in AWS Managed Microsoft AD.

1. Verify subscription status in directory owner account.

1. Check network connectivity.

1. Review error logs.

### Network connectivity issues
<a name="network-connectivity-issues"></a>

1. Test VPC peering connection status.

1. Verify route table configurations.

1. Check security group rules.

1. Confirm DNS resolution.

### DNS resolution problems
<a name="dns-resolution-problems"></a>

1. Verify DHCP option sets.

1. Check DNS server configurations.

1. Test name resolution from consumer instances.

## Additional resources
<a name="cross-account-additional-resources"></a>
+ [AWS License Manager User Guide](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscriptions.html)
+ [AWS Directory Service Documentation](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html)
+ [Sharing your directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_directory_sharing.html)
+ [How to domain join Amazon EC2 instances to AWS Managed Microsoft AD directory across multiple accounts and VPCs](https://aws.amazon.com/blogs/security/how-to-domain-join-amazon-ec2-instances-aws-managed-microsoft-ad-directory-multiple-accounts-vpcs/)
+ [Granted licenses](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html)