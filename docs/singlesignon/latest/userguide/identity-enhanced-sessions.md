# Enabling identity-enhanced console sessions

An identity-enhanced session for the console enhances a user's AWS console session
 by providing some additional user context to personalize that user's experience.
 This capability is currently supported for Amazon Q Developer Pro users of [Amazon Q on
 AWS apps and websites](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-on-aws.html "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-on-aws.html").

You can enable identity-enhanced console sessions without making any changes to
 existing access patterns or federation into the AWS console. If your users sign in
 to the AWS console with IAM (for example, if they sign in as IAM users or
 through federated access with IAM), they can continue using these methods. If your
 users sign in to the AWS access portal, they can continue using their IAM Identity Center user
 credentials.

###### Topics

* [Prerequisites and
 considerations](#prereqs-and-considerations "#prereqs-and-considerations")
* [How to enable
 identity-enhanced-console sessions](#enable-identity-enhanced-sessions-q "#enable-identity-enhanced-sessions-q")
* [How identity-enhanced console sessions
 work](#how-identity-enhanced-sessions-work "#how-identity-enhanced-sessions-work")

## Prerequisites and
 considerations


Before you enable identity-enhanced console sessions, review the following
 prerequisites and considerations:



* If your users access Amazon Q on AWS apps and websites through an
 Amazon Q Developer Pro subscription, you must enable identity-enhanced console
 sessions.


###### Note

Amazon Q Developer users can access Amazon Q without identity-enhanced
 sessions, but they will not have access to their Amazon Q Developer Pro
 subscriptions.
* Identity-enhanced console sessions require an [organization
 instance](organization-instances-identity-center.md "organization-instances-identity-center.md") of IAM Identity Center.
* Integration with Amazon Q isn't supported if you enable IAM Identity Center in an
 opt-in AWS Region.
* To enable identity-enhanced console sessions, you must have the following
 permissions:




	+ `sso:CreateApplication`
	+ `sso:GetSharedSsoConfiguration`
	+ `sso:ListApplications`
	+ `sso:PutApplicationAssignmentConfiguration`
	+ `sso:PutApplicationAuthenticationMethod`
	+ `sso:PutApplicationGrant`
	+ `sso:PutApplicationAccessScope`
	+ `signin:CreateTrustedIdentityPropagationApplicationForConsole`
	+ `signin:ListTrustedIdentityPropagationApplicationsForConsole`
* To enable your users to use identity-enhanced console sessions, you must
 grant them the `sts:setContext` permission in an
 identity-based policy. For information, see [Granting users permissions to use identity-enhanced console
 sessions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_control-access_sts-setcontext.html").

## How to enable
 identity-enhanced-console sessions


You can enable identity-enhanced console sessions in the Amazon Q console or in the
 IAM Identity Center console.


###### Enable identity-enhanced console sessions in the Amazon Q console

Before you enable identity-enhanced console sessions, you must have an
 organization instance of IAM Identity Center with an identity source connected. If you've
 already configured IAM Identity Center, skip to step 3.

1. Open the IAM Identity Center console. Choose **Enable**, and create
 an organization instance of IAM Identity Center. For information, see [Enable IAM Identity Center](enable-identity-center.md "enable-identity-center.md").
2. Connect your identity source to IAM Identity Center and provision users into IAM Identity Center.
 You can connect your existing identity source to IAM Identity Center or use the
 Identity Center directory if you are not already using another identity
 source. For more information, see [IAM Identity Center identity source tutorials](tutorials.md "tutorials.md").
3. After you finish setting up IAM Identity Center, open the Amazon Q console and follow
 the steps in [Subscriptions](https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-management-account.html "https://docs.aws.amazon.com/amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-management-account.html") in the *Amazon Q Developer User
 Guide*. Make sure to enable identity-enhanced console
 sessions.


###### Note

If you do not have sufficient permissions to enable identity-enhanced
 console sessions, you might need to ask an IAM Identity Center administrator to
 perform this task for you in the IAM Identity Center console. For more
 information, see the next procedure.

###### Enable identity-enhanced console sessions in the IAM Identity Center console

If you are an IAM Identity Center administrator, you might be asked by another
 administrator to enable identity-enhanced console sessions in the IAM Identity Center
 console. 

1. Open the IAM Identity Center console.
2. In the navigation pane, choose **Settings**.
3. Under **Enable identity-enhanced sessions**, choose
 **Enable**.
4. In the second message, choose **Enable**.
5. After you finish enabling identity-enhanced console sessions, a
 confirmation message appears at the top of the
 **Settings** page.
6. In the **Details** section, the status for
 **Identity-enhanced sessions** is
 **Enabled**.

## How identity-enhanced console sessions
 work


IAM Identity Center enhances a user's current console session to include the active IAM Identity Center
 user's ID and the IAM Identity Center session ID.


Identity-enhanced console sessions include the following three values:



* **Identity store user ID** ([identitystore:UserId](condition-context-keys-sts-idc.md#condition-keys-identity-store-user-id "condition-context-keys-sts-idc.md#condition-keys-identity-store-user-id")) - This value is
 used to uniquely identify a user in the identity source that is
 connected to IAM Identity Center.
* **Identity store directory ARN** ([identitystore:IdentityStoreArn](condition-context-keys-sts-idc.md#condition-keys-identity-store-arn "condition-context-keys-sts-idc.md#condition-keys-identity-store-arn")) - This value is the
 ARN of the identity store that is connected to IAM Identity Center, and where you can
 look up attributes for `identitystore:UserId`.
* **IAM Identity Center session ID** - This value indicates whether
 the user's IAM Identity Center session is still valid.

The values are the same, but obtained in different ways and added at different
 points of the process, depending on how the user signs in:



* **IAM Identity Center (AWS access portal)**: In this case, the user's
 identity store user ID and ARN values are already provided in the active
 IAM Identity Center session. IAM Identity Center enhances the current session by adding only the
 session ID.
* **Other sign-in methods**: If the user signs in to
 AWS as an IAM user, with an IAM role, or as a federated user with
 IAM, none of these values are provided. IAM Identity Center enhances the current
 session by adding the identity store user ID, identity store directory
 ARN, and the session ID.
