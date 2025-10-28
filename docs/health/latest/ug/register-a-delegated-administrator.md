# Registering a delegated administrator for your

organizational view

After you enable organizational view for your organization, you can register up to five
member accounts in your organization as a delegated administrator. To do this, call the [RegisterDelegatedAdministrator](../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md "../../../organizations/latest/APIReference/API_RegisterDelegatedAdministrator.md") API operation. After you register the member accounts,
they are delegated administer accounts and can access the AWS Health organizational view from
the AWS Health Dashboard. If the account has a [Business](https://aws.amazon.com/premiumsupport/plans/business/ "https://aws.amazon.com/premiumsupport/plans/business/"), [Enterprise On-Ramp](https://aws.amazon.com/premiumsupport/plans/enterprise-onramp "https://aws.amazon.com/premiumsupport/plans/enterprise-onramp"), or [Enterprise](https://aws.amazon.com/premiumsupport/plans/enterprise "https://aws.amazon.com/premiumsupport/plans/enterprise") Support plan, then the
delegated administrators can use the AWS Health API to access the AWS Health organizational
view.

To establish a delegated administrator, from the management account in your organization,
call the following AWS Command Line Interface (AWS CLI) command. You can use this command from the management account
or from an account that can assume the role with the required AWS Identity and Access Management permissions. In the
following example command, replace **ACCOUNT_ID** with the member
account ID that you want to register along with the AWS Health service principal
"health.amazonaws.com".

```
aws organizations register-delegated-administrator --account-id ACCOUNT_ID --service-principal  health.amazonaws.com
```

After a delegated administrator is registered, you have visibility into all AWS Health
events affecting accounts across your organization. You can view historical events over the past
90 days or since the organizational view feature was first enabled, whichever is more recent.
Note that enabling the delegated administrator feature is an asynchronous process and takes up to
a minute to complete.
