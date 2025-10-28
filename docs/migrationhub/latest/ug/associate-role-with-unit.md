AWS Migration Hub will no longer be open to new customers starting November 7, 2025. To continue using the service, sign up prior to November 7, 2025. For capabilities similar to AWS Migration Hub, explore [AWS Transform](https://aws.amazon.com/transform "https://aws.amazon.com/transform").

# Associating an IAM role with an AWS Migration Hub

automation unit

###### Note

The AWS Migration Hub Automation feature is in preview release. It is available in
US East (N. Virginia). To use this feature, you must set your AWS Region to
US East (N. Virginia). You must also set the AWS Migration Hub home Region to US East (N. Virginia).
For instructions on how to set the AWS Migration Hub home Region, see [Managing your AWS Migration Hub home Region](home-region.md "home-region.md").

This is pre-release documentation. Both the AWS Migration Hub Automation feature and the
documentation are subject to change.

To run an automation unit, you must associate with it one of the IAM roles that are
described in [IAM roles and permissions for AWS Migration Hub automation
units](mha-iam-roles.md "mha-iam-roles.md"). This topic describes how to associate a role
with a unit.

###### To associate a role with one or more managed units

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane, expand **Automate**, and choose
   **Service permissions**.
3. In the list of automation units, select the units with which you want to associate
   a role.
4. Choose **Associate role**.
5. In the pop-up window, select a role from the drop-down list, and then choose
   **Associate role**.

###### To associate an IAM role with a custom unit

1. Sign in to the AWS Management Console and open
   the Migration Hub console at
   [https://console.aws.amazon.com/migrationhub/](https://console.aws.amazon.com/migrationhub/ "https://console.aws.amazon.com/migrationhub/").
2. In the left navigation pane, expand **Automate**, and choose
   **Automation units**.
3. In the list of units, choose the name of the custom unit. This action opens the
   details page for that unit.
4. In the **IAM role association** section, choose
   **Associate role**.
5. In the pop-up window, select a role from the drop-down list, and then choose
   **Associate role**.
