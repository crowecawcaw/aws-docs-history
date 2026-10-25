

# Set up multi-account network migration
<a name="transform-vmware-network-multi-account-setup"></a>

For multi-account deployments, you must configure cross-account IAM roles and trusted access for AWS Organizations before you start the network migration.

When you select multi-account migration, AWS Transform provides a link to the network migration setup page. Open the link in the MGN console while signed in to your organization management account. Only the management account has the permissions that the setup requires. The link includes your connector role name and your target account, which AWS Transform uses to create the additional IAM roles and their trust policies.

The setup page does the following:
+ Enables trusted access for AWS Transform MGN, AWS Resource Access Manager (RAM), Reachability Analyzer, and CloudFormation StackSets.
+ If your target account is a delegated administrator (DA) account, registers it as a delegated administrator for AWS Transform MGN and Reachability Analyzer.
+ Creates the following IAM roles in each member account of your organization:
  + `AWSApplicationMigrationSharingRole_<target-account-id>` – Used by MGN to manage network deployments and run Reachability Analyzer checks in the member accounts.
  + `AWSTransformNetworkMigrationAgentSharingRole_<target-account-id>` – Used by AWS Transform for VPC discovery and other actions that support the migration process.

You can also set up the roles manually. This helps when your organization requires infrastructure as code for IAM changes, or when you want to create the roles in specific accounts instead of across your entire organization. The setup page provides AWS CLI commands to enable trusted access and register the delegated administrator. Run these commands from the organization management account. The page also provides a CloudFormation template that creates the IAM roles.