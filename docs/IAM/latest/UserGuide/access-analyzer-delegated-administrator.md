# Delegated administrator for

IAM Access Analyzer

If you're configuring AWS Identity and Access Management Access Analyzer in your AWS Organizations management account, you can add a
member account in the organization as the delegated administrator to manage IAM Access Analyzer
for your organization. The delegated administrator has permissions to create and manage
analyzers within the organization. Only the management account can add a delegated
administrator.

The delegated administrator for IAM Access Analyzer is a member account within the organization
that has permissions to create and manage analyzers that analyze access across the
organization. Only the management account can add, remove, or change a delegated
administrator.

If you add a delegated administrator, you can later change to a different account for the
delegated administrator. When you do, the former delegated administrator account loses
permission to all analyzers that were created using that account to analyze access across
the organization. These analyzers move to a disabled state and no longer generate new or
update existing findings. The existing findings for these analyzers are also no longer
accessible. You can access them again in the future by configuring the account as the
delegated administrator. If you know that you won't use the same account as a delegated
administrator, consider deleting the analyzers before changing the delegated administrator.
This deletes all findings generated. When the new delegated administrator creates new
analyzers, new instances of the same findings are generated. You don't lose any findings,
they just get generated for the new analyzer in a different account. And you can continue to
access findings for the organization using the organization management account, which also
has administrator permissions. The new delegated administrator must create new analyzers for
IAM Access Analyzer to start monitoring resources in your organization.

If the delegated administrator leaves the AWS organization, the delegated administration
privileges are removed from the account. All analyzers in the account with the organization
as the zone of trust move to a disabled state. The existing findings for these analyzers are
also no longer accessible.

The first time that you configure analyzers in the management account, you can choose
**Add delegated administrator** on the **Analyzer
settings** page in the IAM Access Analyzer console.

###### Note

IAM Access Analyzer charges for unused access analyzers based on the number of IAM roles
and users analyzed per analyzer per month. If you create an unused access analyzer in
the management account and the delegated administrator account, you will be charged for
both unused access analyzers. For more details about pricing, see [IAM Access Analyzer
pricing](https://aws.amazon.com/iam/access-analyzer/pricing "https://aws.amazon.com/iam/access-analyzer/pricing").

After you change the delegated administrator, the new administrator must create analyzers
to start monitoring access to the resources in your organization.
