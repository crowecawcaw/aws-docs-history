

# Prerequisites for using CloudFormation StackSets
<a name="stacksets-prereqs"></a>

StackSets extend the functionality of stacks, so you can create, update, or delete stacks across multiple accounts and Regions with a single operation.

Because StackSets perform stack operations across multiple accounts, before you can create your first StackSet you need the necessary permissions defined in your AWS accounts.

You can manage StackSets using *self-managed* or *service-managed* permissions. 
+ For *self-managed* StackSets, you must create and manage IAM roles in each target account and AWS Region. For more information, see [Grant self-managed permissions](stacksets-prereqs-self-managed.md).
+ For *service-managed* StackSets, you don't need to manually create and manage IAM roles in each account; AWS handles the role creation and permissions for you. For more information, see [Activate trusted access](stacksets-orgs-activate-trusted-access.md).

**Topics**
+ [Prepare to perform StackSet operations in AWS Regions that are disabled by default](stacksets-opt-in-regions.md)
+ [Grant self-managed permissions](stacksets-prereqs-self-managed.md)
+ [Activate trusted access for StackSets with AWS Organizations](stacksets-orgs-activate-trusted-access.md)