

# Convert a license type for Linux in License Manager
<a name="conversion-procedures-linux"></a>

You can use either the License Manager Console or the AWS CLI to convert the license type of eligible Ubuntu LTS, RHEL, and RHEL for SAP instances.

**Topics**
+ [Convert a license type using the License Manager console](#convert-license-type-console-linux)
+ [Convert a license type using the AWS CLI](#convert-license-type-cli-linux)
+ [Remove a Ubuntu Pro subscription](#remove-subscription-ubuntu-pro)

## Convert a license type using the License Manager console
<a name="convert-license-type-console-linux"></a>

You can use the License Manager console to convert a license type.

**Note**  
Only instances that are in a stopped state and have been associated by AWS Systems Manager Inventory are displayed.

**To start a license type conversion in the console**

1. Open the License Manager console at [ https://console.aws.amazon.com/license-manager/ ](https://console.aws.amazon.com/license-manager/).

1. From the left navigation pane, choose **License type conversion**, then choose **Create license type conversion**.

1. For **Source operating system**, choose the platform of the instance you want to convert:
   + **RHEL**
   + **RHEL for SAP**
   + **Ubuntu LTS**
   + **Windows BYOL**
   + **Windows license included**

1. (Optional) Filter the available instances by specifying a value for **Instance ID** or **Usage operation value**.

1. Select the instances whose licenses you want to convert, and then choose **Next**.

1. Enter the **Usage operation value** for the license type, select the license that you are converting to, and choose **Next**.

1. Verify that you are satisfied with your license type conversion configuration and choose **Start conversion**.

You can view the status of your license type conversion from the license type conversion panel. The Conversion status column displays the status of the conversion as **In progress**, **Completed**, or **Failed**.

## Convert a license type using the AWS CLI
<a name="convert-license-type-cli-linux"></a>

To start a license type conversion in the AWS CLI, you should confirm the license type of your instance is eligible, and then perform a license type conversion to change to the required subscription. For more information on eligible subscription types, see [Eligible subscription types for Linux in License Manager](conversion-types-linux.md).

**Determine the license type of your instance**  
Verify that you have installed and set up the AWS CLI. For more information, see Installing, updating, and uninstalling the AWS CLI and Configuring the AWS CLI.

**Important**  
You might need to update the AWS CLI to run certain commands and receive all required output in the following steps. Verify that you have permissions to run the `create-license-conversion-task-for-resource` AWS CLI command. For more information, see [Create IAM policies for License Manager](identity-access-management.md#iam-policy-examples).

To determine the license type currently associated with your instance, run the following AWS CLI command. Replace the instance ID with the ID of the instance for which you want to determine the license type:

```
aws ec2 describe-instances --instance-ids {{<instance-id>}} --query "Reservations[*].Instances[*].{InstanceId: InstanceId, PlatformDetails: PlatformDetails, UsageOperation: UsageOperation, UsageOperationUpdateTime: UsageOperationUpdateTime}"
```

The following is an example response to the `describe-instances` command. The **UsageOperation** value is the billing information code associated with the license. A usage operation value of `RunInstances` indicates that the instance is using AWS provided licensing. The `UsageOperationUpdateTime` is the time when the billing code was updated. For more information, see [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) in the *Amazon EC2 API Reference*.

```
"InstanceId": "i-0123456789abcdef",
"Platform details": "Linux/UNIX",
"UsageOperation": "RunInstances",
"UsageOperationUpdateTime: "2021-08-16T21:16:16.000Z"
```

### Supported conversions for Red Hat
<a name="rhel-li-conversions"></a>

The following conversions are supported for Red Hat Enterprise Linux (RHEL) products. Each conversion requires specific source and destination license contexts and may have additional requirements.

#### Convert from RHEL for SAP with HA and Update Services (Sold by AWS in AWS Marketplace) to RHEL for SAP with HA and Update Services (Sold by Red Hat in AWS Marketplace)
<a name="rhel-sap-aws-to-redhat"></a>

Example CLI command:

```
aws license-manager create-license-conversion-task-for-resource \
  --resource-arn {{<instance_arn>}} \
  --source-license-context "UsageOperation=RunInstances:0010,ProductCodes=[{ProductCodeType=marketplace,ProductCodeId={{<source_product_code_id>}}}]" \
  --destination-license-context "UsageOperation=RunInstances:00g0,ProductCodes=[{ProductCodeType=marketplace,ProductCodeId={{<destination_product_code_id>}}}]"
```

Notes:
+ RHEL for SAP with HA and Update Services (Sold by AWS in AWS Marketplace) has many different product code IDs (a.k.a. Marketplace code) depending your AWS Marketplace product subscription. Please check EC2 describe-instances response for the correct product code ID on your instances.
+ RHEL for SAP with HA and Update Services (Sold by Red Hat in AWS Marketplace) has two different product code IDs: du6111oq9lwrc996awt04qyql (NA & Global) and 952qwcsxkm430zxhpy32i7w8g (EMEA). Which you should use depends on your region. Please check your RHEL for SAP with HA and Update Services subscription in Marketplace to find out which one it is.

Once converted, you cannot convert the instance back to RHEL for SAP with HA and Update Services (Sold by AWS in AWS Marketplace), unless you are allowlisted for this private feature, which requires a Support request. For more information, see [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#creating-a-support-case).

#### Convert from RHEL for SAP with HA and Update Services (Sold by AWS in AWS Marketplace) to Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace)
<a name="rhel-sap-aws-to-saas"></a>

Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace) refers to the SaaS subscriptions that customers can purchase from AWS Marketplace. There are also two listings at this moment.

Example CLI command:

```
aws license-manager create-license-conversion-task-for-resource \
  --resource-arn {{<instance_arn>}} \
  --source-license-context "UsageOperation=RunInstances:0010,ProductCodes=[{ProductCodeType=marketplace,ProductCodeId={{<source_product_code_id>}}}]" \
  --destination-license-context "UsageOperation=RunInstances:00g0"
```

Notes:
+ RHEL for SAP with HA and Update Services (Sold by AWS in AWS Marketplace) has many different product code IDs (a.k.a. Marketplace code) depending your AWS Marketplace product subscription. Please check EC2 describe-instances response for the correct product code ID on your instances.
+ Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace) do not have a product code to add to the instances.
  + Explanations: SaaS product product codes are not attached to EC2 instances, so customers are expected to not include a destination product code when invoking the create-license-conversion-task-for-resource CLI command.

Once converted, you cannot convert the instance back to RHEL for SAP with HA and Update Services (Sold by AWS in AWS Marketplace), unless you are allowlisted for this private feature, which requires a Support request. For more information, see [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#creating-a-support-case).

#### Convert from Red Hat License-Included (LI) to RHEL (Sold by Red Hat in AWS Marketplace)
<a name="rhel-li-to-marketplace"></a>

Example CLI command:

```
aws license-manager create-license-conversion-task-for-resource \
  --resource-arn {{<instance_arn>}} \
  --source-license-context "UsageOperation=RunInstances:0010" \
  --destination-license-context "UsageOperation=RunInstances:00g0,ProductCodes=[{ProductCodeType=marketplace,ProductCodeId={{<destination_product_code_id>}}}]"
```

Notes:
+ RHEL (Sold by Red Hat in AWS Marketplace) has two different product code IDs: 6cd5fxzrad0cu2j23p692xytz (NA & Global) and 6t1yup6mik9ng3ge36n33xqhw (EMEA). Which you should use depends on your region. Please check your RHEL for SAP with HA and Update Services subscription in Marketplace to find out which one it is.

#### Convert from Red Hat Enterprise Linux (RHEL) for AWS to Red Hat License-Included (LI)
<a name="rhel-aws-to-li"></a>

Example CLI command:

```
aws license-manager create-license-conversion-task-for-resource \
  --resource-arn {{<instance_arn>}} \
  --source-license-context "UsageOperation=RunInstances,ProductCodes=[{ProductCodeType=marketplace,ProductCodeId={{<source_product_code_id>}}}]" \
  --destination-license-context "UsageOperation=RunInstances:0010"
```

Or this one:

```
aws license-manager create-license-conversion-task-for-resource \
  --resource-arn {{<instance_arn>}} \
  --source-license-context "UsageOperation=RunInstances:00g0,ProductCodes=[{ProductCodeType=marketplace,ProductCodeId={{<source_product_code_id>}}}]" \
  --destination-license-context "UsageOperation=RunInstances:0010"
```

Notes:
+ Red Hat Enterprise Linux (RHEL) for AWS has two different product code IDs: 6cd5fxzrad0cu2j23p692xytz (NA & Global) and 6t1yup6mik9ng3ge36n33xqhw (EMEA). Which you should use depends on your region. Please check EC2 describe-instances response for the correct product code ID on your instances.
+ Red Hat Enterprise Linux (RHEL) for AWS instances may have usage operation RunInstances or RunInstances:00g0. This depends on whether the instances were originally launched from a Red Hat Enterprise Linux (RHEL) for AWS product AMI or they were later converted into this subscription. Please check EC2 describe-instances response for the correct usage operation on your instances.

Example CLI command:

```
aws license-manager create-license-conversion-task-for-resource \
  --resource-arn {{<instance_arn>}} \
  --source-license-context "UsageOperation=RunInstances:0010" \
  --destination-license-context "UsageOperation=RunInstances:00g0"
```

Notes:
+ Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace) do not have a product code to add to the instances.
  + Explanations: SaaS product product codes are not attached to EC2 instances, so customers are expected to not include a destination product code when invoking the create-license-conversion-task-for-resource CLI command.
+ Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace) must be subscribed to by the caller of the CLI command. Subscriptions in other accounts in the same organization are not supported yet.

### Convert from Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace) to Red Hat License-Included (LI)
<a name="rhel-saas-to-li"></a>

Example CLI command:

```
aws license-manager create-license-conversion-task-for-resource \
  --resource-arn {{<instance_arn>}} \
  --source-license-context "UsageOperation=RunInstances:00g0" \
  --destination-license-context "UsageOperation=RunInstances:0010"
```

Notes:
+ Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace) do not have a product code that is added to the instances.

### Other requirements
<a name="rhel-other-requirements"></a>

Instances must be in stopped state before creating their license conversion tasks. Customers should not try to start or terminate the instances before the license conversion tasks complete or fail. This is the same requirement for all license type conversions.

If the destination is one of these Marketplace products:
+ RHEL for SAP with HA and Update Services (Sold by Red Hat in AWS Marketplace)
+ RHEL (Sold by Red Hat in AWS Marketplace)
+ Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace)

Then the customer must have an active subscription in Marketplace before invoking the CLI command. Otherwise, the conversion request might be rejected or might fail. Unlike in Console, when creating license conversion tasks from CLI, License Manager does not try to automatically subscribe customers to destination products.

### Convert to Ubuntu Pro
<a name="ubuntu-li-conversions"></a>

Before you convert your instance from Ubuntu LTS to Ubuntu Pro, your instance must have outbound internet access configured to retrieve a license token from the Canonical servers and install the Ubuntu Pro Client. For more information, see [Conversion prerequisites for License Manager license types](conversion-prerequisites.md).

You can convert from Ubuntu LTS to Ubuntu Pro using one of the following options:
+ **Ubuntu Pro provided by AWS** – The conversion changes the usage operation value of your instance to `RunInstances:0g00`, and you are billed by AWS for the subscription.
+ **Ubuntu Pro sold by Canonical in AWS Marketplace** – The conversion attaches a Canonical Ubuntu Pro AWS Marketplace product code to your instance while the usage operation value remains `RunInstances`, and you are billed by Canonical through your AWS Marketplace subscription. You must have an active Canonical Ubuntu Pro subscription in AWS Marketplace before you initiate this conversion.

**Convert to Ubuntu Pro provided by AWS**  
To convert Ubuntu LTS to Ubuntu Pro provided by AWS, follow these steps:

1. Run the following command from the AWS CLI while specifying your instance’s ARN:

   ```
   aws license-manager create-license-conversion-task-for-resource \
       --resource-arn {{<instance_arn>}} \
       --source-license-context UsageOperation=RunInstances \
       --destination-license-context UsageOperation=RunInstances:0g00
   ```

1. Run the following command from within the instance to retrieve details about your Ubuntu Pro subscription status:

   ```
   pro status
   ```

1. Confirm your output indicates that the instance has a valid Ubuntu Pro subscription:  
![Example output of the Ubuntu pro command with an active Ubuntu Pro subscription.](https://docs.aws.amazon.com/license-manager/latest/userguide/images/ubuntu-pro-conversion-output-valid.png)

**Convert to Ubuntu Pro sold by Canonical in AWS Marketplace**  
To convert Ubuntu LTS to Ubuntu Pro sold by Canonical in AWS Marketplace, follow these steps:

1. Confirm that you have an active Canonical Ubuntu Pro subscription in AWS Marketplace. If you don't have one, subscribe to a Canonical Ubuntu Pro listing in AWS Marketplace, or use the License Manager console to subscribe to the Canonical Ubuntu Pro general listing during conversion.

1. Run the following command from the AWS CLI, specifying your instance's ARN and the Canonical Ubuntu Pro AWS Marketplace product code as the destination product code:

   ```
   aws license-manager create-license-conversion-task-for-resource \
       --resource-arn {{<instance_arn>}} \
       --source-license-context "UsageOperation=RunInstances" \
       --destination-license-context "UsageOperation=RunInstances,ProductCodes=[{ProductCodeType=marketplace,ProductCodeId={{<product_code_id>}}}]"
   ```

1. Run the following command from within the instance to retrieve details about your Ubuntu Pro subscription status:

   ```
   pro status
   ```

**Note**  
Canonical offers multiple Ubuntu Pro product codes in AWS Marketplace, including specific listings (for example, Ubuntu Pro FIPS, LTS, EKS, Minimal, and CIS-hardened variants) and a general listing for customers who don't have an existing Canonical subscription.
To find the product code for your subscription, check your Canonical Ubuntu Pro subscription in AWS Marketplace.
If you don't already have a Canonical Ubuntu Pro subscription in AWS Marketplace, you can convert using a general listing. The general listings are general-purpose Ubuntu Pro subscriptions for customers who don't have a flavor-specific subscription. Choose the general listing that matches your instance's architecture: **Ubuntu Pro License Manager Upgrade** for x86\_64 instances, or **Ubuntu Pro License Manager Upgrade (Arm)** for Arm instances. You can subscribe to a general listing directly in AWS Marketplace, or subscribe during conversion using the License Manager console. The console offers the general listing that matches the architecture of the instances that you select.
Although Canonical offers different Ubuntu Pro flavors in AWS Marketplace, the conversion only attaches the AWS Marketplace product code to your instance for billing and entitlement. The result is standard Ubuntu Pro – the conversion does not install the flavor-specific packages (for example, FIPS, CIS hardening, or Real-time Kernel) on your behalf. After the conversion, you must install and configure those components yourself using the Ubuntu Pro Client (`pro`).

The following table lists the Canonical Ubuntu Pro products in AWS Marketplace that are supported for license type conversion, along with their AWS Marketplace product codes.


**Supported Canonical Ubuntu Pro AWS Marketplace products**  

|  Product name  |  AWS Marketplace product code  | 
| --- | --- | 
| Ubuntu Pro License Manager Upgrade (general listing for x86\_64 instances)<br />Choose this general-purpose option for x86\_64 instances if you don't have a flavor-specific Canonical Ubuntu Pro subscription. | 561bki7b434ls3uekcvfuzzph | 
| Ubuntu Pro License Manager Upgrade (Arm) (general listing for Arm instances)<br />Choose this general-purpose option for Arm instances if you don't have a flavor-specific Canonical Ubuntu Pro subscription. | 3cuwhptbszkqo4x83mut8ri41 | 
| Ubuntu Pro Minimal 22.04 LTS with CIS hardening | a7khwx7o72656zcnle5vu9k6w | 
| Ubuntu Pro FIPS 18.04 LTS | dw21ctly265u7zwld1ihi9jhk | 
| Ubuntu Pro FIPS 20.04 LTS | 7btbv7tkj4yxnrzltyygo1ipn | 
| Ubuntu Pro FIPS 22.04 LTS (FIPS with updates) | bk87i7rt8yk97zlstmtpq1kp3 | 
| Ubuntu Pro 20.04 LTS for EKS 1.29 | 6xnezn2o8gszp87p8w2hu7q81 | 
| Ubuntu Pro 22.04 LTS for EKS 1.33 | icun6atc7ykmlmt7jbg1rysg | 
| Ubuntu Pro 22.04 LTS for EKS 1.34 | c0szntev8wobbsex0eilrkoo4 | 
| Ubuntu Pro 24.04 LTS for EKS 1.32 | 6va1tmiigbi6vd2hyif22frg6 | 
| Ubuntu Pro 24.04 LTS for EKS 1.34 | 87oo7pzlcf8ghjbcjcsbmzoxs | 
| Ubuntu Pro 24.04 LTS for EKS 1.35 | ba39sytryy1xvvfovjg6meff0 | 
| Ubuntu Pro 24.04 LTS for EKS 1.35 (Arm) | 2jfo7rc4qa2kawa3fy30grjei | 
| Ubuntu Pro 22.04 LTS with Real-time Kernel | 9fzl7xjb32n5rbh54phy3z5ec | 
| Minimal Ubuntu Pro 20.04 LTS - Focal | 8crwd7k2hnmx862xvqinp3qwf | 
| Minimal Ubuntu Pro 22.04 LTS - Jammy | ea0rmyl52vxv6a1y9b1hu5i5s | 
| Minimal Ubuntu Pro 24.04 LTS - Noble | 7ysznfxm7eq81z7oktkyzea7c | 

## Remove a Ubuntu Pro subscription
<a name="remove-subscription-ubuntu-pro"></a>

License type conversion can only be used to convert from Ubuntu LTS to Ubuntu Pro. If you need to convert from Ubuntu Pro to Ubuntu LTS, you will need to raise a request to Support. For more information, see [Creating a support case](https://docs.aws.amazon.com/awssupport/latest/user/case-management.html#creating-a-support-case).