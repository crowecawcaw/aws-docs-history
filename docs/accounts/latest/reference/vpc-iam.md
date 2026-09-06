

# Amazon Virtual Private Cloud endpoint policies for Account Management
<a name="vpc-iam"></a>

The following information is relevant for all AWS accounts.

You can create a Amazon VPC endpoint policy for Account Management in which you specify the following:
+ The principal that can perform actions.
+ The actions that the principals can perform.
+ The resources on which the actions can be performed.

The following example shows an Amazon VPC endpoint policy that allows one IAM user named Alice in account 123456789012 to both retrieve and change the alternate contact information for any AWS account, but denies all IAM users permission to delete any alternate contact information on any account.

If you want to grant access to accounts that are part of an AWS Organization to a principal that is in one of the organization's member accounts, then the `Resource` element must use the following format:

```
arn:aws:account::{{{ManagementAccountId}}}:account/{{o-{OrganizationId}}}/{{{AccountId}}}
```

For more information about creating endpoint policies, see [Controlling Access to Services with VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints-access.html) in the *AWS PrivateLink Guide*.