

# Troubleshooting issues with AWS account closure
<a name="troubleshooting_close-account"></a>

This information is about troubleshooting issues with AWS account closure if you signed up for AWS using Sign up for AWS (advanced) or if you activated advanced features for your account. To compare sign-up options, see [Compare sign-up options](sign-up-for-aws.md).

Use the information below to help you diagnose and fix common issues found during the account closure process. For general information about the account closure process, see [Close an AWS account](manage-acct-closing.md).

**Topics**
+ [I don’t know how to delete or cancel my account](#delete-cancel-account)
+ [I don’t see the Close account button on the Accounts page](#no-close-account-button)
+ [I closed my account but still haven’t received an email confirmation](#no-email-confirmation)
+ [I receive a "ConstraintViolationException" error when trying to close my account](#constraint-error)
+ [I receive a "CLOSE\_ACCOUNT\_QUOTA\_EXCEEDED" error when trying to close a member account](#quota-exceeded-error)
+ [Do I need to delete my AWS organization before closing the management account?](#delete-organization)

## I don’t know how to delete or cancel my account
<a name="delete-cancel-account"></a>

To close your account, follow the instructions in [Close an AWS account](manage-acct-closing.md).

## I don’t see the Close account button on the Accounts page
<a name="no-close-account-button"></a>

If you are not signed in as the root user, you will not see the **Close account** button displayed on the **Accounts** page. You must [Sign in to the AWS Management Console as the root user](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) to close your account. If you can’t sign in, see [Troubleshooting issues with the root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshooting_root-user.html).

## I closed my account but still haven’t received an email confirmation
<a name="no-email-confirmation"></a>

This confirmation email is only sent to the root user email address for the AWS account. If you don’t receive this email within a few hours, you can [Sign in to the AWS Management Console as the root user](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) to check that your account is closed. If your account was closed successfully, you will see a message displayed that indicates your account is closed. If the account you closed is a member account, you can verify successful closure by checking if the closed account is labeled as `CLOSED` in the AWS Organizations console. For more information, see [Closing a member account in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html) in the *AWS Organizations User Guide*.

If you are trying to close a **management account** and do not receive an email confirmation about the account closure, your organization most likely has active member accounts. You can only close the management account if your organization doesn’t have any active member accounts. To verify that there are no active member accounts remaining in your organization, go to the AWS Organizations console, and make sure that all member accounts are showing `Closed` next to their account names. After that, you can close the management account.

## I receive a "ConstraintViolationException" error when trying to close my account
<a name="constraint-error"></a>

You are trying to close a management account using the AWS Organizations console, which is not possible. To close a management account, you need to [Sign in to the AWS Management Console as the root user](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) for the management account and close it from the **Accounts** page. For more information, see [Closing a management account in your organization](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close_management.html) in the *AWS Organizations User Guide*.

## I receive a "CLOSE\_ACCOUNT\_QUOTA\_EXCEEDED" error when trying to close a member account
<a name="quota-exceeded-error"></a>

You can only close 20% of member accounts within a rolling 30 day period. This quota is not bound by a calendar month, but starts when you close an account. Within 30 days of that initial account closure, you can't exceed the 20% account closure limit. The minimum account closure is 250 and the maximum account closure is 1000, even if 20% of accounts exceeds 1000. For more information about Organizations quotas, see [Quotas for AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html) in the *AWS Organizations User Guide*.

## Do I need to delete my AWS organization before closing the management account?
<a name="delete-organization"></a>

No, you don’t need to delete your AWS organization before closing the management account. However, you can only close the management account if your organization doesn’t have any active member accounts. To verify that there are no active member accounts remaining in your organization, go to the AWS Organizations console, and make sure that all member accounts are showing `Closed` next to their account names. After that, you can close the management account.