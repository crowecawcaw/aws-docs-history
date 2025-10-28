# Configuring a standard or control in context

When you use [central configuration](central-configuration-intro.md "central-configuration-intro.md") in AWS Security Hub CSPM, the delegated Security Hub CSPM administrator
can create configuration policies that specify how Security Hub CSPM, security standards, and security controls are configured for an organization. The
delegated administrator can associate policies with specific accounts and organizational units (OU). The policies take effect in
your home Region and all linked Regions. The delegated administrator can update configuration policies as necessary.

On the Security Hub CSPM console, the delegated administrator can update configuration policies in two ways—from the **Configuration** page,
or in context with existing workflows. The latter can be beneficial because, as
you view security findings, you can discover which standards and controls are most relevant to your environment and configure them at the same time.

In-context configuration is available only on the Security Hub CSPM console. Programmatically, the delegated administrator must invoke the
[UpdateConfigurationPolicy](../../1.0/APIReference/API_UpdateConfigurationPolicy.md "../../1.0/APIReference/API_UpdateConfigurationPolicy.md")
operation of the Security Hub CSPM API to change how specific standards or controls are configured in the organization.

Follow these steps to configure a Security Hub CSPM standard or control in context.

###### To configure a standard or control in context (console)

1. Open the AWS Security Hub CSPM console at [https://console.aws.amazon.com/securityhub/](https://console.aws.amazon.com/securityhub/ "https://console.aws.amazon.com/securityhub/").

Sign in using the credentials of the delegated Security Hub CSPM administrator account in the home Region. 2. In the navigation pane, choose one of the follow options:

    * To configure a standard, choose **Security standards**, and choose a specific standard.
    * To configure a control, choose **Controls**, and choose a specific control.

3. The console
   lists your existing Security Hub CSPM configuration policies and the status of the selected standard or control in each one. Choose the options to enable or disable the standard or control in each existing configuration policy. For controls, you can
   also choose to customize [control parameters](custom-control-parameters.md "custom-control-parameters.md"). You can't create a new policy during in-context
   configuration. To create a new policy, you must go to the **Configuration** page, choose the **Policies** tab, and
   then choose **Create policy**.
4. After making your changes, choose **Next**.
5. Review your changes, and choose **Apply**. The updates
   affect all accounts and OUs that are associated with a changed configuration policy. The updates also take effect in the home
   Region and all linked Regions.
