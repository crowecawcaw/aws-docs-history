# Walkthrough: Configure AWS Control Tower Without a

VPC

This topic walks through how to configure your AWS Control Tower accounts without a VPC.

If your workload does not require a VPC, you can do the following:

- You can delete the AWS Control Tower virtual private cloud (VPC). This VPC was created when
  you set up your landing zone.
- You can change your Account Factory settings so that new AWS Control Tower accounts are created
  without an associated VPC.

###### Important

If you provision Account Factory accounts with VPC internet access settings enabled,
that Account Factory setting overrides the control [Disallow internet access for an Amazon VPC instance managed by a customer](data-residency-controls.md#disallow-vpc-internet-access "data-residency-controls.md#disallow-vpc-internet-access"). To avoid enabling internet access for newly provisioned accounts, you must change
the setting in Account Factory.

## Delete the AWS Control Tower VPC

Outside of AWS Control Tower, every AWS customer has a default VPC, which you can view on the
Amazon Virtual Private Cloud (Amazon VPC) console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/"). You’ll recognize the default VPC,
because its name always includes the word _(default)_
at the end of the name.

When you set up a AWS Control Tower landing zone, AWS Control Tower deletes your AWS default VPC and
creates a new AWS Control Tower default VPC. The new VPC is associated with your AWS Control Tower
management account. This topic refers to that new VPC as the _Control Tower VPC_.

When you view your AWS Control Tower VPC in the Amazon VPC console, you will _not_ see the word _(default)_ at the end
of the name. If you have more than one VPC, you must use the assigned CIDR range to
identify the correct AWS Control Tower VPC.

You can delete the AWS Control Tower VPC, but if you later need a VPC in AWS Control Tower, you must
create it yourself.

###### To delete the AWS Control Tower VPC

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. Search for `VPC` or select **VPC** from
   the Service Catalog options. You then see the **VPC Dashboard**.
3. From the menu on the left, choose **Your VPCs**. You then see
   a list of all your VPCs.
4. Identify the AWS Control Tower VPC by its CIDR range.
5. To delete the VPC, choose **Actions** and then choose
   **Delete VPC**.

An AWS _(default)_ VPC already exists in every Region
for the AWS Control Tower management account. To follow security best practices, if you choose to
delete the AWS Control Tower VPC, it's best also to delete the AWS default VPC associated with
the management account from all AWS Regions. Therefore, to secure the management account,
remove the default VPC from each Region, as well as removing the VPC created by Control
Tower in your AWS Control Tower home region.

## Optionally clean up the VPC resource in the account

Optionally, to clean up the AWS Control Tower VPC resource, `aws-controltower-VPC`,
from an existing account, you can remove the stack instance from the AWS CloudFormation StackSet
`AWSControlTowerBP-VPC-ACCOUNT-FACTORY-V1`, after you make sure that
there are no existing resources or resource dependencies in the VPC.

## Create an Account in AWS Control Tower Without a VPC

If your end-user workloads do not require VPCs, you can use this method to set up end-user
accounts that don't have VPCs created for them automatically.

From the AWS Control Tower dashboard, you can view and edit your network configurations
settings. After you change the settings so that AWS Control Tower accounts are created without an
associated VPC, all new accounts are created without a VPC until you change the settings
again.

###### To configure Account Factory for creating accounts without VPCs

1. Open a web browser, and navigate to the AWS Control Tower console at [https://console.aws.amazon.com/controltower](https://console.aws.amazon.com/controltower "https://console.aws.amazon.com/controltower").
2. Choose **Account Factory** from the menu on the left.
3. You then see the Account Factory page with the **Network
   Configuration** section.
4. Note the current settings if you intend to restore them later.
5. Choose the **Edit** button in the **Network
   Configuration** section.
6. In the **Edit account factory network configuration** page,
   go to the **VPC Configuration options for new accounts**
   section.

You can follow **Option 1** or **Option 2**,
or both, to ensure that AWS Control Tower does not create a VPC when provisioning an
account.

    1. ###### Option 1 – Removing subnets



    	* Turn off the **Internet-accessible subnet**
    	 toggle switch.
    	* Set the **Maximum number of private subnets**
    	 value to 0.
    2. ###### Option 2 – Removing AWS Regions



    	* Clear every checkbox in the **Regions for VPC
    	 creation** column.

7. Choose **Save**.

### Possible Errors

Be aware of these possible errors that could occur when you delete your AWS Control Tower
VPC or reconfigure Account Factory to create accounts without VPCs.

- Your existing management account may have dependencies or resources in the
  AWS Control Tower VPC, which can cause a _deletion failure_ error.
- If you leave the default CIDR in place when setting up to launch new
  accounts without a VPC, your request fails with an error that _the
  CIDR is not valid_.
