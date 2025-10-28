# Troubleshooting delegated administrator and

AWS Organizations issues

You can use the information on this page to resolve common delegated administrator
issues in Audit Manager.

###### Topics

- [I can't set up Audit Manager with my delegated
  administrator account](#delegated-admin-setup "#delegated-admin-setup")
- [When I create an assessment,
  I can't see the accounts from my organization under Accounts in scope](#cannot-see-accounts-from-organization "#cannot-see-accounts-from-organization")
- [I get an access denied error when I try to generate an
  assessment report using my delegated administrator account](#delegated-admin-access-denied-error "#delegated-admin-access-denied-error")
- [What happens in Audit Manager if I unlink a
  member account from my organization?](#delegated-admin-unlink-account "#delegated-admin-unlink-account")
- [What happens if I relink a member
  account to my organization?](#delegated-admin-relink-account "#delegated-admin-relink-account")
- [What happens if I migrate a member
  account from one organization to another?](#delegated-admin-migrate-account "#delegated-admin-migrate-account")

## I can't set up Audit Manager with my delegated

administrator account

Although multiple delegated administrators are supported in AWS Organizations, Audit Manager allows
only one delegated administrator. If you attempt to designate multiple delegated
administrators in Audit Manager, you receive the following error message:

- Console: `You have exceeded the allowed number of delegated
administrators for the delegated service`
- CLI: `An error occurred (ValidationException) when calling the
RegisterAccount operation: Cannot change delegated Admin for an active
account 11111111111 from 2222222222222 to 333333333333`

Choose the one individual account that you want to use as your delegated
administrator in Audit Manager. Make sure that you register the delegated administrator
account in Organizations first, and then [add the same
account as a delegated administrator](add-delegated-admin.md "add-delegated-admin.md") in Audit Manager.

## When I create an assessment,

I can't see the accounts from my organization under _Accounts in scope_

If you want your Audit Manager assessment to include multiple accounts from your
organization, you must specify a delegated administrator.

Make sure that you configured a delegated administrator account for Audit Manager. For
instructions, see [Adding a delegated administrator](add-delegated-admin.md "add-delegated-admin.md").

Some issues to keep in mind:

- You can't use your AWS Organizations management account as a delegated
  administrator in Audit Manager.
- If you want to enable Audit Manager in more than one AWS Region, you must
  designate a delegated administrator account separately in each Region. In
  your Audit Manager settings, designate the same delegated administrator account
  across all Regions.
- When you designate a delegated administrator, make sure that the delegated
  administrator account has access on the KMS key that you provide when
  setting up Audit Manager. To learn how to review and change your encryption settings,
  see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md").

## I get an _access denied_ error when I try to generate an

assessment report using my delegated administrator account

You will get an `access denied` error if your assessment was created by
a delegated administrator account that the KMS key that's specified in your Audit Manager
settings doesn't belong to. To avoid this error, when you designate a delegated
administrator for Audit Manager, make sure that the delegated administrator account has
access on the KMS key that you provided when setting up Audit Manager.

You might also receive an `access denied` error if you don't have write
permissions for the S3 bucket that you're using as your assessment report
destination.

If you get an `access denied` error, make sure that you meet the
following requirements:

- Your KMS key in your Audit Manager settings gives permissions to the delegated
  administrator. You can configure this by following the instructions in
  [Allowing users in other accounts to use a KMS key](../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md "../../../kms/latest/developerguide/key-policy-modifying-external-accounts.md") in the
  _AWS Key Management Service Developer Guide._ For
  instructions on how to review and change your encryption settings in Audit Manager,
  see [Configuring your data encryption settings](settings-KMS.md "settings-KMS.md").
- You have a permissions policy that grants you write access for the
  assessment report destination. More specifically, your permissions policy
  contains an `s3:PutObject` action, specifies the ARN of the S3
  bucket, and includes the KMS key that's used to encrypt your assessment
  reports. For an example policy that you can use, see [Example 2 (Assessment report destination permissions)](security_iam_id-based-policy-examples.md#full-administrator-access-assessment-report-destination "security_iam_id-based-policy-examples.md#full-administrator-access-assessment-report-destination").

###### Note

If you change your Audit Manager data encryption settings, these changes apply to the
new assessments that you create moving forward. This includes any assessment
reports that you create from your new assessments.

The changes don't apply to existing assessments that you created before you
changed your encryption settings. This includes new assessment reports that you
create from existing assessments, in addition to existing assessment reports.
Existing assessments—and all their assessment reports—continue to use the old
KMS key. If the IAM identity that’s generating the assessment report doesn’t
have permissions to use the old KMS key, you can grant permissions at the key
policy level.

## What happens in Audit Manager if I unlink a

member account from my organization?

When you unlink a member account from an organization, Audit Manager receives a
notification about this event. Audit Manager then automatically removes that AWS account
from the _accounts in scope_ lists of your existing
assessments. When you specify the scope of new assessments moving forward, the
unlinked account no longer appears in the list of eligible AWS accounts.

When Audit Manager removes an unlinked member account from the _accounts in scope_ lists of your assessments, you aren't notified of
this change. Moreover, the unlinked member account isn't notified that Audit Manager is no
longer enabled on their account.

## What happens if I relink a member

account to my organization?

When you relink a member account to your organization, that account isn't
automatically added to the scope of your existing Audit Manager assessments. However, the
relinked member account now appears as an eligible AWS account when you specify
the _accounts in scope_ of your assessments.

- For existing assessments, you can manually edit the assessment scope to
  add the relinked member account. For instructions, see [Step 2: Edit AWS accounts in scope](edit-assessment.md#edit-accounts "edit-assessment.md#edit-accounts").
- For new assessments, you can add the relinked account during assessment
  setup. For instructions, see [Step 2: Specify AWS accounts in scope](create-assessments.md#specify-accounts "create-assessments.md#specify-accounts").

## What happens if I migrate a member

account from one organization to another?

If a member account has Audit Manager enabled in organization 1 and then migrates to
organization 2, Audit Manager is not enabled for organization 2 as a result.
