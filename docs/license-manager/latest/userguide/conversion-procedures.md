# Convert a license type in License Manager

You can convert Windows licenses, Microsoft SQL Server licenses, and Ubuntu Linux
subscriptions using the License Manager console or AWS CLI. You might need to complete additional
steps to convert the license or subscription in the operating system of the
instance.

You can convert license types using the License Manager console or the AWS CLI. When you create a
license type conversion, License Manager validates the billing products on your instance. If these
preliminary validations are successful, License Manager creates a license type conversion. You can
check the status of a license type conversion by using the
`list-license-conversion-tasks` and `get-license-conversion-task` AWS CLI commands.

License Manager might update the resources associated with your self-managed licenses as part of
a license type conversion. Specifically, for any self-managed license with automated
discovery rules of type `License Included`, License Manager disassociates the resource
in the license type conversion from the license if the `license included`
automated discovery rule explicitly excludes the resource.

For example, if your self-managed license contains two automated discovery rules, and
each rule excludes license-included Windows Server, then a license type conversion from
BYOL to license included Windows Server results in disassociation of the instance from
the self-managed license. However, if only one of the two automated discovery rules
contains a `License Included` rule, then the instance is not
disassociated.

You should not start or stop your instance while a license type conversion is in
progress. When the license type conversion succeeds, its status changes from
`IN_PROGRESS` to `SUCCEEDED`. If License Manager encounters issues
during the workflow, it updates the status of the license type conversion to
`FAILED`, and updates the status message with an error message.

###### Note

The billing product information on the AMI used to launch an instance does not
change when you convert the license type. To retrieve accurate billing information,
use the Amazon EC2 [`DescribeInstances`](../../../AWSEC2/latest/APIReference/API_DescribeInstances.md "../../../AWSEC2/latest/APIReference/API_DescribeInstances.md") API. Additionally, if you have
existing workflows that search for billing information from AMIs, update those
workflows to use `DescribeInstances`.

###### Contents

- [Convert a license type for Windows
  and SQL Server in License Manager](conversion-procedures-windows.md "conversion-procedures-windows.md")
  - [License type conversion limits](conversion-procedures-windows.md#conversion-limits "conversion-procedures-windows.md#conversion-limits")
  - [Convert a license type using the License Manager
    console](conversion-procedures-windows.md#conversion-console "conversion-procedures-windows.md#conversion-console")
  - [Convert a license type using the AWS CLI](conversion-procedures-windows.md#conversion-cli "conversion-procedures-windows.md#conversion-cli")

- [Convert a license type for Linux in
  License Manager](conversion-procedures-linux.md "conversion-procedures-linux.md")
  - [Convert a license type
    using the License Manager console](conversion-procedures-linux.md#convert-license-type-console-linux "conversion-procedures-linux.md#convert-license-type-console-linux")
  - [Convert a license type using
    the AWS CLI](conversion-procedures-linux.md#convert-license-type-cli-linux "conversion-procedures-linux.md#convert-license-type-cli-linux")
    - [Supported conversions for Red Hat](conversion-procedures-linux.md#rhel-li-conversions "conversion-procedures-linux.md#rhel-li-conversions")
      - [Convert from RHEL for SAP with HA and Update Services (Sold by AWS in AWS Marketplace) to RHEL for SAP with HA and Update Services (Sold by Red Hat in AWS Marketplace)](conversion-procedures-linux.md#rhel-sap-aws-to-redhat "conversion-procedures-linux.md#rhel-sap-aws-to-redhat")
      - [Convert from RHEL for SAP with HA and Update Services (Sold by AWS in AWS Marketplace) to Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace)](conversion-procedures-linux.md#rhel-sap-aws-to-saas "conversion-procedures-linux.md#rhel-sap-aws-to-saas")
      - [Convert from Red Hat License-Included (LI) to RHEL (Sold by Red Hat in AWS Marketplace)](conversion-procedures-linux.md#rhel-li-to-marketplace "conversion-procedures-linux.md#rhel-li-to-marketplace")
      - [Convert from Red Hat Enterprise Linux (RHEL) for AWS to Red Hat License-Included (LI)](conversion-procedures-linux.md#rhel-aws-to-li "conversion-procedures-linux.md#rhel-aws-to-li")

    - [Convert from Red Hat Subscriptions (Sold by Red Hat in AWS Marketplace) to Red Hat License-Included (LI)](conversion-procedures-linux.md#rhel-saas-to-li "conversion-procedures-linux.md#rhel-saas-to-li")
    - [Other requirements](conversion-procedures-linux.md#rhel-other-requirements "conversion-procedures-linux.md#rhel-other-requirements")
    - [Convert to Ubuntu Pro](conversion-procedures-linux.md#ubuntu-li-conversions "conversion-procedures-linux.md#ubuntu-li-conversions")

  - [Remove a Ubuntu Pro
    subscription](conversion-procedures-linux.md#remove-subscription-ubuntu-pro "conversion-procedures-linux.md#remove-subscription-ubuntu-pro")
