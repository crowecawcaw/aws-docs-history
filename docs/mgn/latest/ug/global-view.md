NEW - You can now accelerate your migration and modernization with AWS Transform. Read [Getting Started](../../../transform/latest/userguide/getting-started.md "../../../transform/latest/userguide/getting-started.md") in the _AWS Transform User Guide_.

# Manage large-scale migrations with global view

The AWS Application Migration Service (AWS MGN) global view feature enables you to manage large-scale migrations
across multiple accounts. Global view provides visibility, and the ability to perform actions on
source servers, apps, and waves in different AWS accounts.

Global view utilizes AWS Organizations to structure a management account that has access to
source servers in multiple member accounts, and member accounts that only have access to their
own source servers.

To use this feature:

- You need to have an AWS account in which AWS Application Migration Service is initialized.
- The account must be a management account in AWS Organizations, or a delegated admin for
  AWS Application Migration Service which has the same feature permissions as a management account in AWS
  Organizations.
