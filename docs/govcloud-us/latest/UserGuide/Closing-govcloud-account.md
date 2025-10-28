# Closing an AWS GovCloud (US) account

The following instructions describe the process to close an AWS GovCloud (US) account.
Because AWS account management functions are not available in the AWS GovCloud (US)
Management Console, closing an AWS GovCloud (US) account may require additional
steps.

###### Note

There is no **Close account** option available in the
AWS GovCloud (US) Management Console as there is in the standard AWS account
Management Console.

Use the following AWS GovCloud (US) account closure procedure that is most applicable to
your business needs.

## Close an AWS GovCloud (US) standalone or

member account

You can close an AWS GovCloud (US) standalone or member account by initiating closure
of its associated standard account.

**To close an AWS GovCloud (US) standalone or member
account**

1. Sign in to the AWS GovCloud (US) account.
2. [Find
   and terminate all active resources](https://aws.amazon.com/premiumsupport/knowledge-center/check-for-active-resources "https://aws.amazon.com/premiumsupport/knowledge-center/check-for-active-resources") currently running in the
   AWS GovCloud (US) account (both Regions if applicable).

###### Important

Before terminating your resources, back up your data where
appropriate. After your account has been closed, you will no longer have
access to the data or AWS services. 3. After you've terminated all active resources from your AWS GovCloud (US)
account, delete all IAM users, and rotate and delete the access keys from
the AWS GovCloud (US) account. 4. Close the standard AWS account using the **Close
account** option available in the standard account Management
Console. After the standard AWS account closure, your AWS GovCloud (US)
account will be closed, without further action needed from you.

If you run into issues with billing/access to the AWS GovCloud (US) Management
Console after this time, please submit an Support case using your standard
AWS account, referencing the issue and the AWS GovCloud (US) account
ID.

###### Notes

- Closing your standard AWS account will not automatically terminate
  all your active resources in the AWS GovCloud (US) account. We recommend
  that you terminate all the resources in your AWS GovCloud (US) account
  before closing the standard AWS account.
- Closed AWS GovCloud (US) member accounts are not automatically removed
  from the AWS GovCloud (US) organization after the post-closure period and
  they remain visible in the AWS GovCloud (US) organization in suspended
  status. You must remove the AWS GovCloud (US) member accounts from your
  AWS GovCloud (US) organization if you wish to delete your AWS GovCloud (US)
  organization.

## Close an AWS GovCloud (US)

management account

You can only close an AWS GovCloud (US) management account after you've deleted the
organization associated with it. After deleting the organization, your management
account will change to a standalone AWS GovCloud (US) account. At this point, you can
initiate the closing of the standalone AWS GovCloud (US) account by closing its
associated standard AWS account.

###### Note

Your AWS GovCloud (US) management account will not close if there are active
member accounts in your AWS GovCloud (US) organization. You will continue to incur
charges for any active resources in the AWS GovCloud (US) management account and
member accounts until they are closed.

**To close an AWS GovCloud (US) management
account**

1. Remove and close all the AWS GovCloud (US) member accounts from the
   AWS GovCloud (US) management account. For more information, see [Removing a member account from your organization](../../../organizations/latest/userguide/orgs_manage_accounts_remove.md "../../../organizations/latest/userguide/orgs_manage_accounts_remove.md").

###### Note

Removing an AWS GovCloud (US) member account does not close the account,
instead it removes the member account from the AWS GovCloud (US)
organization and the member account becomes a standalone AWS account. If
you wish to close the removed member accounts, follow the instructions
in the previous section [Close an AWS GovCloud (US) standalone or
member account](#closing-govcloud-and-standard "#closing-govcloud-and-standard"). 2. Sign in to the AWS GovCloud (US) management account and delete the
AWS GovCloud (US) organization. For more information, see [Deleting an organization](../../../organizations/latest/userguide/orgs_manage_org_delete.md "../../../organizations/latest/userguide/orgs_manage_org_delete.md"). 3. [Find
and terminate all active resources](https://aws.amazon.com/premiumsupport/knowledge-center/check-for-active-resources "https://aws.amazon.com/premiumsupport/knowledge-center/check-for-active-resources"), delete all IAM users, and
rotate and delete the access keys of the AWS GovCloud (US) management
account. 4. Close the standard management account associated with the AWS GovCloud (US)
management account using the **Close account** option
available in the standard account's Management Console. After the standard
management account has been closed, your AWS GovCloud (US) management account
will close within the next billing cycle. For more information, see [Closing a member account in your organization](../../../organizations/latest/userguide/orgs_manage_accounts_close.md "../../../organizations/latest/userguide/orgs_manage_accounts_close.md").

## What to expect after you

close your AWS GovCloud (US) account

After your AWS GovCloud (US) account is closed:

- You will not be able to sign in to the AWS Management Console for your AWS GovCloud (US)
  account.
- You will no longer have access to the data or AWS services in the
  AWS GovCloud (US) account.
- If you had shared resources from your AWS GovCloud (US) account with other
  AWS GovCloud (US) accounts, those other accounts will no longer have access to
  the shared resources after the AWS GovCloud (US) account closure.

## Reopening an AWS GovCloud (US)

account

Within the post-closure period, which are the 90 days after your account is closed,
you can reopen your standard AWS account and AWS GovCloud (US) account by contacting
AWS Support.

###### Important

Re-opening your AWS GovCloud (US) account will only restore data/resources that were
not terminated. If you terminated resources to avoid incurring charges during the
closure process, they will not be restored. To ensure access to important data that
might be needed upon re-opening, it is recommended that you backup that data prior
to terminating AWS GovCloud (US) resources.

After the post-closure period, you cannot reopen your standard AWS account or
AWS GovCloud (US) account.
