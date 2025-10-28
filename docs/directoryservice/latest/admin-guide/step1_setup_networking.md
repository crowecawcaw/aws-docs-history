# Step 1: Set up your networking

environment

You will need to establish an Amazon VPC peering connection to share your AWS Managed Microsoft AD
directory (directory account owner) with another AWS account (directory consumer
account). See the following procedures for steps to set up your networking environment
for a shared AWS Managed Microsoft AD.

## Prerequisites

Before you begin the steps in this tutorial, you must first do the
following:

- Create two new AWS accounts for testing purposes in the same Region.
  When you create an AWS account, it automatically creates a dedicated
  virtual private cloud (VPC) in each account. Take note of the VPC ID in each
  account. You will need this later.
- [Create an
  AWS Managed Microsoft AD](ms_ad_getting_started.md#ms_ad_getting_started_create_directory "ms_ad_getting_started.md#ms_ad_getting_started_create_directory").
- When creating a VPC peering connection, both the directory account owner
  and directory consumer account will need the necessary permissions to create
  and accept the peering connection. For more information, see [Example: Create a VPC peering connection](../../../vpc/latest/peering/security-iam.md#vpc-peering-iam-create "../../../vpc/latest/peering/security-iam.md#vpc-peering-iam-create") and [Example: Accept a VPC peering connection](../../../vpc/latest/peering/security-iam.md#vpc-peering-iam-accept "../../../vpc/latest/peering/security-iam.md#vpc-peering-iam-accept").

###### Note

While there are many ways to connect Directory owner and Directory
consumer account VPCs, this tutorial will use the VPC peering method.
For additional VPC connectivity options, see [Network connectivity](ms_ad_directory_sharing.md#network_connectivity "ms_ad_directory_sharing.md#network_connectivity").

## Configure a VPC peering

connection between the directory owner and the directory consumer
account

The VPC peering connection you will create is between the directory consumer and
directory owner VPCs. Follow these steps to configure a VPC peering connection for
connectivity with the directory consumer account. With this connection you can route
traffic between both VPCs using private IP addresses.

###### To create a VPC peering connection between the directory owner and directory

consumer account

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). Makes sure to sign in as a
   user with administrator credentials in the directory owner account with the
   necessary permissions to create a VPC peering connection. See [Prerequisites](#step1_setup_networking_prereqs "#step1_setup_networking_prereqs") for more
   information.
2. In the navigation pane, choose **Peering
   Connections**. Then choose **Create Peering
   Connection**.
3. Configure the following information:
   - **Peering connection name tag**:
     Provide a name that clearly identifies this connection with the VPC
     in the directory consumer account.
   - **VPC (Requester)**: Select the VPC
     ID for the directory owner account.
   - Under **Select another VPC to peer
     with**, ensure that **My
     account** and **This region** are
     selected.
   - **VPC (Accepter)**: Select the VPC ID
     for the directory consumer account.

4. Choose **Create Peering Connection**. In the
   confirmation dialog box, choose **OK**.

###### To accept the peering request on behalf of the directory consumer

account

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). Makes sure to sign in as a
   user with the necessary permissions to accept the peering request. See [Prerequisites](#step1_setup_networking_prereqs "#step1_setup_networking_prereqs") for more
   information.
2. In the navigation pane, choose **Peering
   Connections**.
3. Select the pending VPC peering connection. (Its status is Pending
   Acceptance.) Choose **Actions**, **Accept
   Request**.
4. In the confirmation dialog, choose **Yes,
   Accept**. In the next confirmation dialog box, choose **Modify my route tables now** to go directly to the
   route tables page.

Now that your VPC peering connection is active, you must add an entry to your VPC
route table in the directory owner account. Doing so enables traffic to be directed
to the VPC in the directory consumer account.

###### To add an entry to the VPC route table in the directory owner account

1. While in the **Route Tables** section of the Amazon VPC
   console, select the route table for the directory owner VPC.
2. Choose the **Routes** tab, choose **Edit
   routes**, and then choose **Add
   route**.
3. In the **Destination** column, enter the CIDR block for
   the directory consumer VPC.
4. In the **Target** column, enter the VPC peering
   connection ID (such as `pcx-123456789abcde000`) for the
   peering connection that you created earlier in the directory owner
   account.
5. Choose **Save changes**.

###### To add an entry to the VPC route table in the directory consumer

account

1. While in the **Route Tables** section of the Amazon VPC
   console, select the route table for the directory consumer VPC.
2. Choose the **Routes** tab, choose **Edit
   routes**, and then choose **Add
   route**.
3. In the **Destination** column, enter the CIDR block for
   the directory owner VPC.
4. In the **Target** column, type in the VPC peering
   connection ID (such as `pcx-123456789abcde001`) for the
   peering connection that you created earlier in the directory consumer
   account.
5. Choose **Save changes**.

Add Active Directory protocols and ports to the outbound rules for security groups in directory consumer VPCs.
For more information, see [Security
groups for your VPC](../../../vpc/latest/userguide/VPC_SecurityGroups.md "../../../vpc/latest/userguide/VPC_SecurityGroups.md") and [AWS Managed Microsoft AD
prerequisites](ms_ad_getting_started_prereqs.md "ms_ad_getting_started_prereqs.md").

**Next Step**

[Step 2: Share your directory](step2_share_directory.md "step2_share_directory.md")
