CodeWhisperer's features are becoming a part of Amazon Q Developer. [Learn more](whisper-legacy.md "whisper-legacy.md")

# CodeWhisperer is becoming a part of Amazon Q Developer

All of the features of CodeWhisperer are moving to Amazon Q Developer. The purpose of this section
is to explain the relationship between CodeWhisperer and Amazon Q Developer.

Amazon Q Developer is a generative artificial intelligence (AI) powered conversational assistant
that can help you understand, build, extend, and operate AWS applications. To learn more, see
the [Amazon Q Developer User
Guide](../../../amazonq/latest/qdeveloper-ug/what-is.md "../../../amazonq/latest/qdeveloper-ug/what-is.md").

Features of Amazon Q Developer not available in CodeWhisperer include:

- [Chatting about your resources](../../../amazonq/latest/qdeveloper-ug/chat-actions.md "../../../amazonq/latest/qdeveloper-ug/chat-actions.md")
- [Chatting
  about your costs](../../../amazonq/latest/qdeveloper-ug/chat-costs.md "../../../amazonq/latest/qdeveloper-ug/chat-costs.md")
- [Diagnosing console
  errors](../../../amazonq/latest/qdeveloper-ug/diagnose-console-errors.md "../../../amazonq/latest/qdeveloper-ug/diagnose-console-errors.md")
- [Transforming your code](../../../amazonq/latest/qdeveloper-ug/code-transformation.md "../../../amazonq/latest/qdeveloper-ug/code-transformation.md")
- [Developing software](../../../amazonq/latest/qdeveloper-ug/software-dev.md "../../../amazonq/latest/qdeveloper-ug/software-dev.md")

## Migrating to Amazon Q Developer in-place

With in-place migration, you will retain:

- Subscriptions
- Customizations
- Tags
- Other resources related to CodeWhisperer

Before you begin in-place migration you should consider the following:

- After you migrate, all Amazon Q Developer features will be enabled. Amazon Q does not allow you
  to turn off specific features. If you turned off specific features in CodeWhisperer, those
  features will be re-enabled in Amazon Q.
- With Amazon Q Developer Pro, member accounts inherit settings for code references and
  encryption keys from the organization management account. If you set up CodeWhisperer Pro in a
  member account, and your organization management account _is_ set up
  for Amazon Q Developer Pro, then your member account will inherit the settings for code references
  and encryption keys from your organization management account. If you set up CodeWhisperer Pro
  in a member account, and your organization management account _is not_
  set up for Amazon Q Developer Pro, then your member account will take on the Amazon Q Developer Pro
  default settings for code references and encryption keys.
- In-place migration does not automatically enable identity-aware sessions, which are
  necessary to chat with Amazon Q in the AWS management console at the Pro tier. Chatting at
  the Pro tier means higher monthly limits on questions, and for those limits to be per
  user, rather than per account. If you want to use identity-aware sessions, then you must
  [enable them](../../../singlesignon/latest/userguide/awsapps.md#identity-aware-sessions "../../../singlesignon/latest/userguide/awsapps.md#identity-aware-sessions") after you migrate.

For more information about pricing tiers, see [the Amazon Q Developer pricing page](https://aws.amazon.com/q/developer/pricing/ "https://aws.amazon.com/q/developer/pricing/").

The user who performs an in-place migration requires the following permissions:

- `codewhisperer:UpdateProfile`
- `user-subscriptions:CreateClaim`
- `sso:ListApplicationAssignments`
- `sso:PutApplicationAuthenticationMethod`
- `sso:PutApplicationGrant`
- `sso:UpdateApplication`
- `kms:CreateGrant`
- `iam:CreateServiceLinkedRole`

To migrate from CodeWhisperer Pro to Amazon Q Developer Pro in-place, use the following
procedure.

1. Open the CodeWhisperer console.
2. From the banner at the top of the window, choose **Migrate
   profile**.
3. Review the contents of the pop-up window. Then select the box that says **I
   confirm that I understand the implications of migrating my profile.**
4. Choose **Migrate profile**.

## Starting over with Amazon Q Developer

To delete your CodeWhisperer Professional resources and start over with Amazon Q Developer Pro, use
the following procedure.

1. Delete any existing
   customizations.
2. Delete your CodeWhisperer profile.
3. [Subscribe to Amazon Q Developer Pro](../../../amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-management-account.md "../../../amazonq/latest/qdeveloper-ug/q-admin-setup-subscribe-management-account.md").

## Trying Amazon Q features inside CodeWhisperer

You can try out some features of [Amazon Q in the IDE](../../../amazonq/latest/qdeveloper-ug/q-in-IDE.md "../../../amazonq/latest/qdeveloper-ug/q-in-IDE.md") through
CodeWhisperer.

To do this, select **Enable Amazon Q Developer features** in your CodeWhisperer
settings.
