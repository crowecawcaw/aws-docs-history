# Amazon RDS for Db2 licensing options

Amazon RDS for Db2 has two licensing options: bring your own license (BYOL) and Db2 license
through AWS Marketplace.

###### Topics

- [Bring your own license (BYOL) for
  Db2](#db2-licensing-options-byol "#db2-licensing-options-byol")
- [Db2 license through AWS Marketplace](#db2-licensing-options-marketplace "#db2-licensing-options-marketplace")
- [Switching between Db2 licenses](#db2-edition-license-switching "#db2-edition-license-switching")

## Bring your own license (BYOL) for

Db2

In the BYOL model, you use your existing Db2 database licenses to deploy databases on
Amazon RDS. Verify that you have the appropriate Db2 database license for the DB instance
class and Db2 database edition that you want to run. You must also follow
IBM policies for licensing IBM database software in
the cloud computing environment.

###### Note

Multi-AZ DB instances are cold standbys because the Db2 database is installed but
not running. Standbys aren't readable, running, or serving requests. For more
information, see [IBM Db2 licensing information](https://www.ibm.com/support/customer/csol/terms/licenses#license-search " https://www.ibm.com/support/customer/csol/terms/licenses#license-search") on the IBM website.

In this model, you continue to use your active IBM support account, and
you contact IBM directly for Db2 database service requests. If you have
an Support account with case support, you can contact Support for Amazon RDS issues. Amazon Web Services
and IBM have a multi-vendor support process for cases that require
assistance from both organizations.

Amazon RDS supports the BYOL model for Db2 Standard Edition and Db2
Advanced Edition.

###### Topics

- [IBM IDs for bring your own
  license (BYOL) for Db2](#db2-prereqs-ibm-info "#db2-prereqs-ibm-info")
- [Adding IBM
  IDs to a parameter group for RDS for Db2 DB instances](#db2-licensing-options-byol-adding-ids "#db2-licensing-options-byol-adding-ids")
- [Integrating with AWS License Manager](#db2-lms-integration "#db2-lms-integration")

### IBM IDs for bring your own

license (BYOL) for Db2

In the BYOL model, you need your IBM Customer ID and your IBM Site ID to create, modify, or
restore RDS for Db2 DB instances. You must create a custom parameter group with your
IBM Customer ID and your IBM Site ID _before_ you create an
RDS for Db2 DB instance. For more information, see [Adding IBM
IDs to a parameter group for RDS for Db2 DB instances](#db2-licensing-options-byol-adding-ids "#db2-licensing-options-byol-adding-ids"). You can run multiple
RDS for Db2 DB instances with different IBM Customer IDs and IBM Site IDs in the same
AWS account or AWS Region.

###### Important

If we can't verify your license by your IBM Customer ID and your IBM Site ID, we might
terminate any DB instances running with these unverified licenses.

If you're a new IBM Db2 customer, you must first purchase a Db2 software license
from [IBM](https://www.ibm.com/products/db2/pricing "https://www.ibm.com/products/db2/pricing"). After you purchase a Db2 software license, you will
receive a Proof of Entitlement from IBM, which lists your IBM Customer ID
and your IBM Site ID.

If you're an existing IBM Db2 customer, you can find your IBM Customer ID and your
IBM Site ID on your Proof of Entitlement certificate from IBM.

You can also find your IBM Customer ID and your IBM Site ID in your [IBM
Passport Advantage Online](https://www.ibm.com/software/passportadvantage/pao_customer.html "https://www.ibm.com/software/passportadvantage/pao_customer.html") account. After your log in, you can view both
IDs on either the main page or the Software downloads page.

### Adding IBM

IDs to a parameter group for RDS for Db2 DB instances

Because you can't modify default parameter groups, you must create a custom
parameter group and then modify it to include the values for your IBM Customer ID and your
IBM Site ID. For information about parameter groups, see [DB parameter groups for
Amazon RDS DB instances](USER_WorkingWithDBInstanceParamGroups.md "USER_WorkingWithDBInstanceParamGroups.md").

###### Important

You must create a custom parameter group with your IBM Customer ID and your IBM Site ID
_before_ you create an RDS for Db2 DB
instance.

Use the parameter settings in the following table.

| Parameter             | Value                         |
| --------------------- | ----------------------------- |
| `rds.ibm_customer_id` | `<your IBM Customer ID>`      |
| `rds.ibm_site_id`     | `<your IBM Site ID>`          |
| `ApplyMethod`         | `immediate`, `pending-reboot` |

These parameters are dynamic, which means that any changes to them take effect
immediately and that you don't need to reboot the DB instance. If you don't want the
changes to take effect immediately, you can set `ApplyMethod` to
`pending-reboot` and schedule these changes to be made during a
maintenance window.

You can create and modify a custom parameter group by using the AWS Management Console, the
AWS CLI, or the Amazon RDS API.

###### To add your IBM Customer ID and your IBM Site ID to a parameter group

1. Create a new DB parameter group. For more information about
   creating a DB parameter group, see [Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").
2. Modify the parameter group that you created. For more information
   about modifying a parameter group, see [Modifying parameters in a DB parameter group
   in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### To add your IBM Customer ID and your IBM Site ID to a parameter group

1. Create a custom parameter group by running the [create-db-parameter-group](../../../cli/latest/reference/rds/create-db-parameter-group.md "../../../cli/latest/reference/rds/create-db-parameter-group.md") command.

Include the following required options:

    * `--db-parameter-group-name` – A name for
     the parameter group that you are creating.
    * `--db-parameter-group-family` – The Db2
     engine edition and major version. Valid values:
     `db2-se-11.5`, `db2-ae-11.5`.
    * `--description` – A description for this
     parameter group.

For more information about creating a DB parameter group, see
[Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 2. Modify the parameters in the custom parameter group that you
created by running the [modify-db-parameter-group](../../../cli/latest/reference/rds/modify-db-parameter-group.md "../../../cli/latest/reference/rds/modify-db-parameter-group.md")
command.

Include the following required options:

    * `--db-parameter-group-name` – The name
     of the parameter group that you created.
    * `--parameters` – An array of parameter
     names, values, and the application methods for the parameter
     update.

For more information about modifying a parameter group, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

###### To add your IBM Customer ID and your IBM Site ID to a parameter group

1. Create a custom DB parameter group by using the Amazon RDS API [CreateDBParameterGroup](../APIReference/API_CreateDBParameterGroup.md "../APIReference/API_CreateDBParameterGroup.md")
   operation.

Include the following required parameters:

    * `DBParameterGroupName`
    * `DBParameterGroupFamily`
    * `Description`

For more information about creating a DB parameter group, see
[Creating a DB parameter group in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md"). 2. Modify the parameters in the custom parameter group that you
created by using the RDS API [ModifyDBParameterGroup](../APIReference/API_ModifyDBParameterGroup.md "../APIReference/API_ModifyDBParameterGroup.md")
operation.

Include the following required parameters:

    * `DBParameterGroupName`
    * `Parameters`

For more information about modifying a parameter group, see [Modifying parameters in a DB parameter group
in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

Now you are ready to create a DB instance and attach the custom parameter group to
the DB instance. For more information, see [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md") and [Associating a DB parameter group with a
DB instance in Amazon RDS](USER_WorkingWithParamGroups.md "USER_WorkingWithParamGroups.md").

### Integrating with AWS License Manager

To aid in monitoring RDS for Db2 license usage in the BYOL model, [AWS License Manager](https://aws.amazon.com/license-manager/ "https://aws.amazon.com/license-manager/") integrates with
RDS for Db2. License Manager supports tracking of RDS for Db2 engine editions based on virtual CPUs
(vCPUs). You can also use License Manager with AWS Organizations to manage all of your organizational
accounts centrally.

To track license usage of your RDS for Db2 DB instances, you must create self-managed
licenses. You can create self-managed licenses by using the AWS Management Console, the AWS License Manager
CLI, and the AWS License Manager API. Or, you can automate the creation of self-managed
licenses with AWS CloudFormation and Terraform templates.

RDS for Db2 resources that match the product information filter are automatically
associated with the self-managed license. Discovery of RDS for Db2 DB instances can
take up to 24 hours.

The following table shows available values for the Engine Edition product
information filter for RDS for Db2.

| Value    | Description          |
| -------- | -------------------- |
| `db2-se` | Db2 Standard Edition |
| `db2-ae` | Db2 Advanced Edition |

###### Topics

- [Terminology](#db2-lms-integration-terms "#db2-lms-integration-terms")
- [Creating a self-managed license
  in AWS License Manager](#db2-lms-integration-tracking "#db2-lms-integration-tracking")
- [Automating the creation of
  self-managed licenses in AWS License Manager with templates](#db2-lms-integration-templates "#db2-lms-integration-templates")
- [Settings for creating self-managed
  licenses](#db2-settings-lms "#db2-settings-lms")

#### Terminology

This page uses the following terminology when discussing the Amazon RDS integration
with AWS License Manager.

Self-managed license

Self-managed license is a term used in AWS License Manager. The Amazon RDS
console refers to the license as an AWS License Manager configuration. A
self-managed license contains licensing rules based on the terms of
your enterprise agreements. The rules that you create determine how
AWS processes commands that consume licenses. While creating a
self-managed license, work closely with your organization's
compliance team to review your enterprise agreements. For more
information, see [Self-managed licenses in License Manager](../../../license-manager/latest/userguide/license-configurations.md "../../../license-manager/latest/userguide/license-configurations.md").

#### Creating a self-managed license

in AWS License Manager

You can create a self-managed license by using the AWS Management Console, the AWS License Manager
CLI, and the AWS License Manager API.

###### Note

If you create an RDS for Db2 DB instance by using the AWS Management Console, you will
create a self-managed license by entering a name for the license. Then Amazon RDS
associates the DB instance with this license. (In the Amazon RDS console, this
license is referred to as an AWS License Manager configuration.) If you want to create
an RDS for Db2 DB instance by using the AWS License Manager CLI or AWS License Manager API, you
must first create a self-managed license with the following steps. The same
situation applies to restoring an RDS for Db2 DB instance to a point in time or
from a snapshot.

###### To create a self-managed license to track the license usage of

your RDS for Db2 DB instances

1. Go to [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/ "https://console.aws.amazon.com/license-manager/").
2. Create a self-managed license.

For instructions, see [Create a self-managed license](../../../license-manager/latest/userguide/create-license-configuration.md "../../../license-manager/latest/userguide/create-license-configuration.md") in the
_AWS License Manager User Guide_.

Add a rule for an **RDS Product Information
Filter** in the **Product
Information** panel.

For more information, see [ProductInformation](../../../license-manager/latest/APIReference/API_ProductInformation.md "../../../license-manager/latest/APIReference/API_ProductInformation.md") in the _AWS License Manager API
Reference_.

###### Note

This procedure uses an AWS License Manager CLI command.

To create a self-managed license by using the AWS CLI, run the AWS License Manager
[create-license-configuration](../../../cli/latest/reference/license-manager/create-license-configuration.md "../../../cli/latest/reference/license-manager/create-license-configuration.md") command. Use the
`--cli-input-json` or `--cli-input-yaml`
options to pass the options to the command.

For more information, see [Settings for creating self-managed
licenses](#db2-settings-lms "#db2-settings-lms").

The following command creates a self-managed license for Db2 Standard
Edition.

```
aws license-manager create-license-configuration --cli-input-json file://rds-db2-se.json
```

The following JSON is the content of the
`rds-db2-se.json` file used in the previous
command.

```
{
    "Name": "rds-db2-se",
    "Description": "RDS Db2 Standard Edition",
    "LicenseCountingType": "vCPU",
    "LicenseCountHardLimit": false,
    "ProductInformationList": [
        {
            "ResourceType": "RDS",
            "ProductInformationFilterList": [
                {
                    "ProductInformationFilterName": "Engine Edition",
                    "ProductInformationFilterValue": ["db2-se"],
                    "ProductInformationFilterComparator": "EQUALS"
                }
            ]
        }
    ]
}
```

For more information about product information, see [Automated discovery of resource inventory](../../../license-manager/latest/userguide/automated-discovery.md "../../../license-manager/latest/userguide/automated-discovery.md") in the
_AWS License Manager User Guide_.

For more information about the `--cli-input` parameter, see
[Generating AWS CLI
skeleton and input parameters from a JSON or YAML input file](../../../cli/latest/userguide/cli-usage-skeleton.md "../../../cli/latest/userguide/cli-usage-skeleton.md")
in the _AWS CLI User Guide_.

###### Note

This procedure uses an AWS License Manager API command.

To create a self-managed license, use the [`CreateLicenseConfiguration`](../../../license-manager/latest/APIReference/API_CreateLicenseConfiguration.md "../../../license-manager/latest/APIReference/API_CreateLicenseConfiguration.md") AWS License Manager API
operation with the following required parameters:

- `Name`
- `LicenseCountingType`
- `ProductInformationList`
- `ResourceType`
- `ProductInformationFilterList`
- `ProductInformationFilterName`
- `ProductInformationFilterValue`
- `ProductInformationFilterComparator`
  For more information about the parameters, see [Settings for creating self-managed
  licenses](#db2-settings-lms "#db2-settings-lms").

#### Automating the creation of

self-managed licenses in AWS License Manager with templates

You can automate the creation of self-managed licenses by using AWS CloudFormation and
Terraform templates.

The following example AWS CloudFormation template creates self-managed licenses for Db2
Standard Edition on RDS for Db2. For a template for Db2 Advanced Edition, update
the values for `Name`, `Description`, and
`ProductInformationFilter`.

```
AWSTemplateFormatVersion: "2010-09-09"
Description: CloudFormation template to create a License Configuration for Db2 Standard Edition on RDS for Db2.

Resources:
  Db2LicenseConfiguration:
    Type: "AWS::LicenseManager::LicenseConfiguration"
    Properties:
      Name: "rds-db2-se"
      Description: "Db2 Standard Edition on RDS for Db2"
      LicenseCountingType: "vCPU"
      LicenseCountHardLimit: false
      ProductInformationList:
        - ResourceType: "RDS"
          ProductInformationFilterList:
            - ProductInformationFilterName: "Engine Edition"
              ProductInformationFilterValue:
                - "db2-se"
              ProductInformationFilterComparator: "EQUALS"
```

For more information about using AWS CloudFormation with Amazon RDS, see [Creating Amazon RDS
resources with AWS CloudFormation](creating-resources-with-cloudformation.md "creating-resources-with-cloudformation.md").

The following example Terraform template creates self-managed
licenses for Db2 Standard Edition on RDS for Db2. Replace
`us-east-1` with your AWS Region. For a template
for Db2 Advanced Edition, update the values for `name`,
`description`, and
`product_information_filter`.

```
provider "aws" {
  region = "`us-east-1`"
}

resource "aws_licensemanager_license_configuration" "rds_db2_license_config" {
  name                     = "rds-db2-se"
  description              = "Db2 Standard Edition on RDS for Db2
  license_counting_type    = "vCPU"
  license_count_hard_limit = false

  product_information_list {
    resource_type = "RDS"

    product_information_filter {
      name       = "Engine Edition"
      comparator = "EQUALS"
      value      = ["db2-se"]
    }
  }
}
```

For more information about using Terraform and Amazon RDS, see
[Using
Terraform as an IaC tool for the AWS Cloud](../../../prescriptive-guidance/latest/choose-iac-tool/terraform.md "../../../prescriptive-guidance/latest/choose-iac-tool/terraform.md") and
[Best practices for using the Terraform AWS Provider](../../../prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.md "../../../prescriptive-guidance/latest/terraform-aws-provider-best-practices/introduction.md") in _AWS Prescriptive Guidance_.

#### Settings for creating self-managed

licenses

In the following table, you can find details about the settings for creating
self-managed licenses by using the AWS License Manager CLI, the AWS License Manager API, an AWS CloudFormation
template, and a Terraform template. The parameter name in the
following table appears in the format of the name used in the AWS License Manager API and
the AWS CloudFormation template.

| Parameter name                     | Data type        | Required | Description                                                                                                                  |
| ---------------------------------- | ---------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Name                               | string           | Yes      | The name of the license configuration.                                                                                       |
| Description                        | string           | No       | The description of the license configuration.                                                                                |
| LicenseCountingType                | string           | Yes      | The dimension used to track the license inventory. Valid<br>value: `vCPU`.                                                   |
| LicenseCountHardLimit              | boolean          | No       | Indicates whether hard or soft license enforcement is used.<br>Exceeding a hard limit blocks the launch of new<br>instances. |
| ProductInformationList             | array of objects | Yes      | A list of product information for a license<br>configuration.                                                                |
| ResourceType                       | string           | Yes      | The resource type. Valid value: `RDS`.                                                                                       |
| ProductInformationFilterList       | array of objects | Yes      | A list of product information filters for a license<br>configuration.                                                        |
| ProductInformationFilterName       | string           | Yes      | The name of the type of filter being declared. Valid<br>value: `Engine Edition`.                                             |
| ProductInformationFilterValue      | array of strings | Yes      | The value to filter on. You must only specify one value.<br>Valid values: `db2-se` or<br>`db2-ae`.                           |
| ProductInformationFilterComparator | string           | Yes      | The logical operator for<br>`ProductInformationFilterName`. Valid value:<br>`EQUALS`.                                        |

## Db2 license through AWS Marketplace

In the Db2 license through AWS Marketplace model, you pay an hourly rate to subscribe to Db2
licenses. This model helps you get started quickly with RDS for Db2 without needing to
purchase licenses.

To use Db2 license through AWS Marketplace, you need an active AWS Marketplace subscription for the
particular IBM Db2 edition that you want to use. If you don't already have one, [subscribe to AWS Marketplace](#db2-marketplace-subscribing-registering "#db2-marketplace-subscribing-registering") for that
IBM Db2 edition.

Amazon RDS supports Db2 license through AWS Marketplace for IBM Db2 Standard Edition
and IBM Db2 Advanced Edition.

###### Topics

- [Terminology](#db2-marketplace-terminology "#db2-marketplace-terminology")
- [Payments and billing](#db2-marketplace-billing "#db2-marketplace-billing")
- [Subscribing to Db2
  Marketplace listings and registering with IBM](#db2-marketplace-subscribing-registering "#db2-marketplace-subscribing-registering")
- [Obtaining a private offer](#db2-marketplace-private-offer "#db2-marketplace-private-offer")

### Terminology

This page uses the following terminology when discussing the Amazon RDS integration
with AWS Marketplace.

SaaS subscription

In AWS Marketplace, software-as-a-service (SaaS) products such as the
pay-as-you-go license model adopt a usage-based subscription model. IBM,
the software seller for Db2, tracks your usage and you pay only for what
you use.

Public offer

Public offers allow you to purchase AWS Marketplace products directly from the
AWS Management Console.

Private offer

Private offers are a purchasing program that allow sellers and buyers
to negotiate custom prices and end user licensing agreement (EULA) terms
for purchases in AWS Marketplace.

Db2 Marketplace fees

Fees charged for the Db2 software license usage by IBM.
These service fees are metered through AWS Marketplace and appear on your AWS
bill under the AWS Marketplace section.

Amazon RDS fees

Fees that AWS charges for the RDS for Db2 services, which excludes
licenses when using AWS Marketplace for Db2 licenses. Fees are metered through the
Amazon RDS service being used and appear on your AWS bill.

### Payments and billing

RDS for Db2 integrates with AWS Marketplace to offer hourly, pay-as-you-go licenses for Db2.
The Db2 Marketplace fees cover the license costs of the Db2 software, and the Amazon RDS
fees cover the costs of your RDS for Db2 DB instance usage. For information about
pricing, see [Amazon RDS for Db2
pricing](https://aws.amazon.com/rds/db2/pricing/ "https://aws.amazon.com/rds/db2/pricing/").

To stop these fees, you must delete any RDS for Db2 DB instances. In addition, you
can remove your subscriptions to AWS Marketplace for Db2 licenses. If you remove your
subscriptions without deleting your DB instances, Amazon RDS will continue to bill you
for the use of the DB instances. For more information, see [Deleting a DB instance](USER_DeleteInstance.md "USER_DeleteInstance.md").

You can view bills and manage payments for your RDS for Db2 DB instances that use Db2
license through AWS Marketplace in the [AWS Billing console](https://console.aws.amazon.com/https://console.aws.amazon.com/billing "https://console.aws.amazon.com/https://console.aws.amazon.com/billing"). Your
bills includes two charges: one for your usage of Db2 license through AWS Marketplace and one
for your usage of Amazon RDS. For more information about billing, see [Viewing your
bill](../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md "../../../awsaccountbilling/latest/aboutv2/getting-viewing-bill.md") in the _AWS Billing and Cost Management User Guide_.

### Subscribing to Db2

Marketplace listings and registering with IBM

To use Db2 license through AWS Marketplace, you must use the AWS Management Console to complete the
following two tasks. You can't complete these tasks through the AWS CLI or the RDS
API.

###### Note

If you want to create your DB instances by using the AWS CLI or the RDS API, you
must complete these two tasks first.

###### Topics

- [Task 1: Subscribe to Db2 in
  AWS Marketplace](#db2-marketplace-subscribing "#db2-marketplace-subscribing")
- [Task 2: Register your subscription
  with IBM](#db2-marketplace-registering "#db2-marketplace-registering")

#### Task 1: Subscribe to Db2 in

AWS Marketplace

To use Db2 license with AWS Marketplace, you need to have an active AWS Marketplace subscription
for Db2. Because subscriptions are associated with a specific IBM Db2 edition, you
need to subscribe to Db2 in AWS Marketplace for each edition of Db2 that you want to use:
[IBM Db2
Advanced Edition](https://aws.amazon.com/marketplace/pp/prodview-w6m4yctzzy5fk "https://aws.amazon.com/marketplace/pp/prodview-w6m4yctzzy5fk"), [IBM Db2 Standard Edition](https://aws.amazon.com/marketplace/pp/prodview-gbsgwalbkphv6 "https://aws.amazon.com/marketplace/pp/prodview-gbsgwalbkphv6").
For information about AWS Marketplace subscriptions, see [Saas usage-based subscriptions](../../../marketplace/latest/buyerguide/buyer-saas-products.md#saas-pricing-models "../../../marketplace/latest/buyerguide/buyer-saas-products.md#saas-pricing-models") in the _AWS Marketplace Buyer
Guide_.

We recommend that you subscribe to Db2 in AWS Marketplace _before_ you start to [create a DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

#### Task 2: Register your subscription

with IBM

After you subscribe to Db2 in AWS Marketplace, complete the registration of your IBM
order from the AWS Marketplace page for the type of Db2 subscription that you chose. On
the AWS Marketplace page, choose **View purchase options**, and then
choose **Set up your account**. You can register either with
your existing IBM account or by creating a free
IBM account.

### Obtaining a private offer

You can request an AWS Marketplace private offer for Db2 from IBM. For more
information, see [Private offers](../../../marketplace/latest/buyerguide/buyer-private-offers.md "../../../marketplace/latest/buyerguide/buyer-private-offers.md") in the _AWS Marketplace Buyer
Guide_.

###### Note

If you are an AWS Organizations user and received a private offer that was issued to
your payer and member accounts, follow the procedure below to subscribe to Db2
directly on each account in your organization.

###### To obtain a Db2 private offer

1. After a private offer has been issued, sign in to the AWS Marketplace
   Console.
2. Open the email with a Db2 private offer link.
3. Follow the link to directly access the private offer.

###### Note

Following this link before logging in to the correct account will
result in a **Page note found** (404)
error. 4. Review the terms and conditions. 5. Choose **Accept terms**.

###### Note

If an AWS Marketplace private offer is not accepted, the Db2 service fees from
AWS Marketplace will continue to be billed at the public hourly rate. 6. To verify the offer details, select **Show
details** in the product listing.

After you've completed the procedure, you can create your DB instance by following the steps in [Creating an Amazon RDS DB instance](USER_CreateDBInstance.md "USER_CreateDBInstance.md"). In the AWS Management Console, under
**License**, make sure that you choose **Through
AWS Marketplace**.

## Switching between Db2 licenses

You can switch between Db2 licenses in RDS for Db2. For example, you can start with bring
your own license (BYOL), and then switch to Db2 license through AWS Marketplace.

###### Important

If you want to switch to Db2 license through AWS Marketplace, make sure that you have an
active AWS Marketplace subscription for the IBM Db2 edition that you want to use. If you don't,
first [subscribe to Db2 in
AWS Marketplace](#db2-marketplace-subscribing-registering "#db2-marketplace-subscribing-registering") for that Db2 edition, and then complete the restore procedure.

###### To switch between Db2 licenses

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Automated
   backups**.

The automated backups are displayed on the **Current
Region** tab. 3. Choose the DB instance that you want to restore. 4. For **Actions**, choose **Restore to point in
time**.

The **Restore to point in time** window
appears. 5. Choose **Latest restorable time** to restore to the
latest possible time, or choose **Custom** to choose a
time.

If you chose **Custom**, enter the date and time you
want to restore the instance to.

###### Note

Times are shown in your local time zone, which is indicated by an
offset from Coordinated Universal Time (UTC). For example, UTC-5 is
Eastern Standard Time/Central Daylight Time. 6. For **DB engine**, choose the Db2 license you want to
use. 7. For **DB instance identifier**, enter the name of the
target restored DB instance. The name must be unique. 8. Choose other options as needed, such as DB instance class, storage, and
whether you want to use storage autoscaling.

For information about each setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md"). 9. Choose **Restore to point in time**.
For more information, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

To switch between Db2 licenses, run the [restore-db-instance-to-point-in-time](../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md "../../../cli/latest/reference/rds/restore-db-instance-to-point-in-time.md") command. The following example
restores the latest point-in-time version, sets the DB engine to IBM Db2 Advanced
Edition, and sets the license model to Db2 license through AWS Marketplace.

You can specify other settings. For information about
each setting, see [Settings for DB instances](USER_CreateDBInstance.md "USER_CreateDBInstance.md").

For Linux, macOS, or Unix:

```
aws rds restore-db-instance-to-point-in-time \
    --source-db-instance-identifier `my_source_db_instance` \
    --target-db-instance-identifier `my_target_db_instance` \
    --use-latest-restorable-time \
    --engine `db2-ae` \
    --license-model `marketplace-license`
```

For Windows:

```
aws rds restore-db-instance-to-point-in-time ^
    --source-db-instance-identifier `my_source_db_instance` ^
    --target-db-instance-identifier `my_target_db_instance` ^
    --use-latest-restorable-time ^
    --engine `db2-ae` ^
    --license-model `marketplace-license`
```

For more information, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").

To switch between Db2 licenses, call the Amazon RDS API
[`RestoreDBInstanceToPointInTime`](../APIReference/API_RestoreDBInstanceToPointInTime.md "../APIReference/API_RestoreDBInstanceToPointInTime.md") operation with the
following parameters:

- `SourceDBInstanceIdentifier`
- `TargetDBInstanceIdentifier`
- `RestoreTime`
- `Engine`
- `LicenseModel`
  For more information, see [Restoring a DB instance to a specified time for Amazon RDS](USER_PIT.md "USER_PIT.md").
