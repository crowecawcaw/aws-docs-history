Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [Migrating from Amazon CodeCatalyst](../userguide/migration.md "../userguide/migration.md").

# Troubleshooting problems with billing

associated with your space

In CodeCatalyst, you can add an AWS account to your space to grant permissions to
resources and for billing purposes. The following information can help you troubleshoot
common issues with associated accounts in CodeCatalyst.

###### Topics

- [I cannot access the
  Amazon CodeCatalyst Spaces page in the AWS Management Console](#billing-troubleshoot-console "#billing-troubleshoot-console")
- [I cannot change the
  billing tier for my space](#billing-troubleshoot-need-associated-account "#billing-troubleshoot-need-associated-account")

## I cannot access the

Amazon CodeCatalyst Spaces page in the AWS Management Console

**Problem:** When I try to access the Amazon CodeCatalyst page in the AWS Management Console to add an account to my CodeCatalyst space or add roles to an account in AWS, I
receive a permissions error.

**Possible fixes:**

For your space, you can add authorized AWS accounts to add them to your project
if you have the **Space administrator** role. You must also have an
AWS account where you have administrative permissions or can work with your AWS
administrator. You must first make sure you are signed in to the AWS Management Console with the same
account that you want to manage. After you are signed in to the AWS Management Console, you can open
the console and try again.

Open the Amazon CodeCatalyst page in the AWS Management Console at [https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/](https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/ "https://us-west-2.console.aws.amazon.com/codecatalyst/home?region=us-west-2#/").

## I cannot change the

billing tier for my space

**Problem:** I am able to view billing for my space
but cannot change the subscription tier from Free to Standard.

**Possible fixes:** For your space, you can change
subscription tiers or authorize billing accounts if you have the
**Space administrator** role.

Before you can change your CodeCatalyst plan from the Free tier, you must first have an
account added to your space. Next, you must set up the account for billing by
turning on the Standard tier.

This does not change the billing tier for the space. It authorizes the Standard
tier for the account, so the **Space administrator** will be able to
upgrade to the Standard tier.

You must have the **Space administrator** role in CodeCatalyst and have
administrator permissions for your account in AWS to manage billing.
