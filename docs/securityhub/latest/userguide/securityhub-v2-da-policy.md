

# Managing configuration of member accounts in an AWS Organization
<a name="securityhub-v2-da-policy"></a>

 The delegated administrator for an AWS Organization can configure security capabilities across member accounts and Regions. You can currently control configuration for AWS Security Hub, AWS Security Hub CSPM, Amazon Inspector, and Amazon GuardDuty. 

## Security Hub configuration catalog
<a name="securityhub-v2-configuration-catalog"></a>

 The configuration catalog of Security Hub offers multiple options to help configure your AWS Organization accounts for the security capabilities provided by Security Hub. 

 The following table lists the options in the Security Hub configuration catalog. To view the steps for a configuration, choose its name, and then expand its section. 


**Security Hub configuration catalog options**  

| Configuration | Type | Description | 
| --- | --- | --- | 
| [Security Hub (essential and add-on capabilities)](#securityhub-v2-configuration-enable-policy) | Policy | This is the recommended configuration to deploy for Security Hub.<br />This configuration turns on Security Hub's essential security management, posture management, threat analytics, and vulnerability management capabilities. It optionally enables add-on capabilities. | 
| [Threat analytics from Amazon GuardDuty](#securityhub-v2-configuration-enable-guardduty) | Policy | Turn on selected Amazon GuardDuty capabilities to continuously monitor, analyze, and process AWS data sources and logs in your AWS environment. | 
| [Posture management from AWS Security Hub CSPM](#securityhub-v2-configuration-enable-cspm) | Policy | This configuration turns on Security Hub CSPM's standards and controls, which detect when your AWS accounts and resources deviate from security best practices. | 
| [Vulnerability management from Amazon Inspector](#securityhub-v2-configuration-enable-inspector) | Policy | This configuration turns on selected Amazon Inspector capabilities that automatically discover workloads, instances, container images, and other resources, and scans them for vulnerabilities and network exposure. | 

## Enabling configurations for member accounts
<a name="securityhub-v2-configuration-enable-overview"></a>

 You can create a configuration for your AWS Organization accounts from the configuration catalog. Before you create a configuration, you must create the delegated administrator policy in the AWS Organization management account. For information about creating the delegated administrator policy in Security Hub, see [Creating the delegated administrator policy in Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-policy-statement.html). 

 When you create your first configuration, Security Hub automatically enables the required AWS Organizations policy types for your organization. 

 Each configuration starts from the **Configurations** page in the Security Hub console. To open this page, in the navigation pane, choose **Management**, and then choose **Configurations**. 

 We recommend that you use the Security Hub configuration to manage your organization's configuration. It includes configuration options for AWS Security Hub CSPM, Amazon Inspector, and Amazon GuardDuty, so you can manage all of these services from one configuration. To manage only one of these services, use the steps for that service's configuration. 

**Important**  
If you're enabling Security Hub for the first time, you must use the steps in [Enabling a configuration for Security Hub](#securityhub-v2-configuration-enable-policy).

To view the steps for a configuration, expand its section.

### Enabling a configuration for Security Hub
<a name="securityhub-v2-configuration-enable-policy"></a>

 This configuration turns on Security Hub essential security management, posture management, threat analytics, and vulnerability management capabilities. It optionally enables add-on capabilities. 

**To create a policy that enables member accounts**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  From the **Configuration catalog**, choose **Security Hub (essential and add-on capabilities)**. 

1.  On the **Configure Security Hub** page, configure the following settings: 

   1.  For **Configuration action**, choose **Enable**. 

   1.  Add-on capabilities are charged separately from the essential plan. Some are billed through Security Hub, and others through their respective services, such as Amazon GuardDuty and Amazon Inspector. For **Security capabilities**, choose one of the following options: 
      + **Enable essential** – Turns on only the essential capabilities that are included in the base price. This option doesn't turn on any add-on capabilities.
      + **Enable all** – Turns on the essential capabilities and all add-on capabilities, which incur additional charges.
      + **Enable specific** – Choose which capabilities to turn on from the **Essential capabilities** and **Add-on capabilities** sections. Add-on capabilities that you choose incur additional charges.

   1.  For **Account selection**, choose one of the following options: 
      + **All organizational units and accounts** – Applies the configuration to your entire organization.
      + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
      + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

   1.  For **Region selection**, choose one of the following options: 
      + **Enable in all currently available Regions** – Optionally, select **Auto-enable new Regions**. Auto-enabling new Regions doesn't turn on threat analytics or posture management features in those Regions.
      + **Enable in some Regions** – For **Enabled Regions**, choose the Regions to enable.

   1.  (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  For **Details**, enter a **Name** for the policy, and optionally a **Description**. The name must be unique for all policies in your organization. 

   1.  For **Resource tags**, optionally add tags as key-value pairs to help you identify the configuration. Then, choose **Next**. 

1.  If **Security Hub CSPM checks** is selected, the **Configure Posture Management** page appears. This capability is selected by default, and you can clear it only when you choose **Enable specific**. Configure the following settings: 

   1.  For **Security standards**, choose the standards to enable. By default, AWS Foundational Security Best Practices v1.0.0 and CIS AWS Foundations Benchmark v5.0.0 are selected. (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  For **Controls**, choose one of the following options: 
      + **Enable all controls** – Evaluates all controls in your enabled standards, including newly released controls. We recommend this option.
      + **Customize** – Choose **Enable all by default (disable specific)** or **Disable all by default (enable specific)**. Then, select the controls to disable or enable.

       (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  (Optional) For **Custom control parameters**, select **Customize control parameters**. Choose a control, and then set its parameter values. To customize more controls, choose **Customize additional control**. Controls that you don't customize use their default parameter values. 

   1.  (Optional) To apply different settings in specific Regions, in **Region-specific customizations**, choose **Add region customization**. In the dialog box, for **Regions**, choose the Regions. Configure **Security standards**, **Controls**, and **Custom control parameters** as described in the previous substeps. Then, choose **Save**. 

       A customization must differ from the baseline settings before you can save it. Each Region can belong to only one customization. Regions without a customization use the baseline standards and controls. 

   1.  Choose **Next**. 

1.  (Optional) On the **Configure Cross-Region aggregation** page, for **Home Region**, choose **No home Region** or the current Region. You can only choose the current Region as your home Region. To use a different home Region, open Security Hub in that Region. Then, choose **Next**. 

1.  On the **Review and apply** page, review your settings. To change the settings for a step, choose **Edit** for that step. Then, choose **Apply**. 

    Security Hub creates a separate policy for each capability area. Each policy name is your policy name followed by the capability area. For example, {{name}} - Security management, {{name}} - Vulnerability management, and {{name}} - Posture management. 

    The configuration status of your policy displays at the top of the Policies page. Each capability provides a status indicating whether it was configured successfully. To view the effective policy at the account level, review the **Organization** tab on the **Configurations** page. 

**Note**  
After you enable and configure Security Hub, you can use the following configurations to apply additional settings for individual services.

### Configuring AWS Security Hub CSPM
<a name="securityhub-v2-configuration-enable-cspm"></a>

 This configuration turns on AWS Security Hub CSPM standards and controls, which detect when your AWS accounts and resources deviate from security best practices. 

 To manage this service along with the other Security Hub capabilities, we recommend that you use the steps in [Enabling a configuration for Security Hub](#securityhub-v2-configuration-enable-policy) instead. 

**To create a configuration for AWS Security Hub CSPM**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  From the **Configuration catalog**, choose **Posture management from AWS Security Hub CSPM**. 

1.  On the **Configure CSPM policy** page, configure the following settings: 

   1.  For **Details**, enter a **Name** for the policy, and optionally a **Description**. The name must be unique for all policies in your organization. 

   1.  For **Resource tags**, optionally add tags as key-value pairs to help you identify the configuration. Then, choose **Next**. 

1.  On the **Accounts and Regions** page, configure the following settings: 

   1.  For **Account selection**, choose one of the following options: 
      + **All organizational units and accounts** – Applies the configuration to your entire organization.
      + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
      + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

   1.  For **Regions**, choose one of the following options: 
      + **Enable in all currently available Regions** – Enables AWS Security Hub CSPM in all currently available Regions. We recommend this option. Optionally, select **Auto-enable new Regions** to automatically enable AWS Security Hub CSPM in new Regions.
      + **Specify Regions in which to enable or disable** – Choose the Regions in which to enable or disable AWS Security Hub CSPM.
      + **Disable in all currently available Regions** – Disables AWS Security Hub CSPM in all currently available Regions.

   1.  (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  Choose **Next**. 

1.  On the **Standards and controls** page, configure the following settings: 

   1.  For **Security standards**, choose the standards to enable. By default, AWS Foundational Security Best Practices v1.0.0 and CIS AWS Foundations Benchmark v5.0.0 are selected. (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  For **Controls**, choose one of the following options: 
      + **Enable all controls** – Evaluates all controls in your enabled standards, including newly released controls. We recommend this option.
      + **Customize** – Choose **Enable all by default (disable specific)** or **Disable all by default (enable specific)**. Then, select the controls to disable or enable.
      + **Disable all controls** – Disables all controls in your enabled standards.

   1.  (Optional) For **Custom control parameters**, select **Customize control parameters**. Choose a control, and then set its parameter values. To customize more controls, choose **Customize additional control**. Controls that you don't customize use their default parameter values. 

   1.  Choose **Next**. 

1.  On the **Regional overrides** page, optionally add Region-specific customizations. To apply different settings in specific Regions, choose **Add region customization**. In the dialog box, for **Regions**, choose the Regions. Configure **Security standards**, **Controls**, and **Custom control parameters** as described in the previous step. Then, choose **Save**. 

    A customization must differ from the baseline settings before you can save it. Each Region can belong to only one customization. Regions without a customization inherit the baseline standards and controls. 

    Choose **Next**. 

1.  On the **Review and create** page, review your settings. To change the settings for a step, choose **Edit** for that step. Then, choose **Create**. 

### Configuring Amazon Inspector
<a name="securityhub-v2-configuration-enable-inspector"></a>

 This configuration turns on selected Amazon Inspector capabilities that automatically discover workloads, instances, container images, and other resources, and scans them for vulnerabilities and network exposure. 

 To manage this service along with the other Security Hub capabilities, we recommend that you use the steps in [Enabling a configuration for Security Hub](#securityhub-v2-configuration-enable-policy) instead. 

**To create a configuration for Amazon Inspector**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  From the **Configuration catalog**, choose **Vulnerability management from Amazon Inspector**. 

1.  On the **Configure vulnerability management policy** page, configure the following settings: 

   1.  For **Capability selection**, select the capabilities for this policy to configure. You can select **EC2 scanning**, **ECR scanning**, **Lambda scanning**, **Lambda code scanning**, **Code security**, and **Machine images**. **Lambda code scanning**, **Code security**, and **Machine images** incur additional charges. For each capability that you select, choose one of the following options for **Policy action**: 
      + **Enable** – Enforces the capability as enabled. Member accounts can't disable it.
      + **Disable** – Enforces the capability as disabled. Member accounts can't enable it.
      + **Custom** – Enables the capability in some Regions and disables it in others.

       To set all capabilities to the same policy action, under **Quick actions**, choose **Enable all** or **Disable all**. You can then change the policy action for individual capabilities. This policy doesn't configure capabilities that you don't select. 

       If you enable **Code security**, it requires additional configuration. For more information, see [Amazon Inspector Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) in the *Amazon Inspector User Guide*. 

   1.  For **Account selection**, choose one of the following options: 
      + **All organizational units and accounts** – Applies the configuration to your entire organization.
      + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
      + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

   1.  For **Region selection**, choose how to set Regions: 
      + If all selected capabilities use the same policy action, choose **Across all selected capabilities** to use the same Regions for all capabilities. To set Regions for each capability, choose **Per capability**.
      + If the selected capabilities use different policy actions, the console uses **Per capability**, and **Across all selected capabilities** isn't available. Expand each capability to set its Regions.

       For **Regions**, set the Regions based on the policy action: 
      + **Enable** – Choose **Enable in all currently available Regions** or **Enable in some Regions**. We recommend the first option. Optionally, select **Auto-enable new Regions**.
      + **Disable** – Choose **Disable in all currently available Regions** or **Disable in some Regions**. We recommend the first option. Optionally, select **Auto-disable new Regions**.
      + **Custom** – For **Enabled Regions**, choose **Enable all Regions and auto-enable new Regions** or **Enable specific Regions**. For **Disabled Regions**, choose the Regions to disable. If you select a Region as both enabled and disabled, the Region is disabled.

   1.  (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  For **Details**, enter a **Name** for the policy, and optionally a **Description**. The name must be unique for all policies in your organization. 

   1.  For **Resource tags**, optionally add tags as key-value pairs to help you identify the configuration. Then, choose **Next**. 

1.  On the **Review and create** page, review your settings. To change your settings, choose **Edit**. Then, choose **Create**. 

### Configuring Amazon GuardDuty
<a name="securityhub-v2-configuration-enable-guardduty"></a>

 This configuration turns on selected Amazon GuardDuty capabilities to continuously monitor, analyze, and process AWS data sources and logs in your AWS environment. 

 To manage this service along with the other Security Hub capabilities, we recommend that you use the steps in [Enabling a configuration for Security Hub](#securityhub-v2-configuration-enable-policy) instead. 

**To create a configuration for Amazon GuardDuty**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  From the **Configuration catalog**, choose **Threat analytics from Amazon GuardDuty**. 

1.  On the **Configure threat detection policy** page, configure the following settings: 

   1.  For **Region scope**, choose one of the following options: 
      + **Set a default for all Regions** – Applies one default configuration to every AWS Region. You can override specific Regions in **Regional overrides**.
      + **No default — manage only specific Regions** – This policy manages only the Regions that you add in **Regional overrides**. It doesn't manage other Regions. You must add at least one regional override.

   1.  If you chose **Set a default for all Regions**, for **Default configuration**, select the protection plans for this policy to manage. For each protection plan that you select, choose one of the following options for **Policy action**: 
      + **Enable** – Enforces the protection plan as enabled. Member accounts can't disable it.
      + **Disable** – Enforces the protection plan as disabled. Member accounts can't enable it.

       To set all protection plans to the same policy action, under **Quick actions**, choose **Enable all** or **Disable all**. You can then change the policy action for individual protection plans. This policy doesn't manage protection plans that you don't select. **Foundational threat detection** is always selected. It must be enabled if you enable any other protection plan. 

   1.  For **Regional overrides**, choose **Add regional override**. This step is optional if you set a default, and required if you chose **No default — manage only specific Regions**. In the dialog box, choose the Regions for the override. Under **Protection plans**, select the protection plans and policy actions in the same way as for the default configuration. Then, choose **Save**. 

       A regional override fully replaces the default configuration for the Regions that you choose. Specify every protection plan that you want this policy to manage in those Regions. The same configuration applies to all of the Regions in the override. 

   1.  For **Account selection**, choose one of the following options: 
      + **All organizational units and accounts** – Applies the configuration to your entire organization.
      + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
      + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

   1.  For **Details**, enter a **Name** for the policy, and optionally a **Description**. The name must be unique for all policies in your organization. 

   1.  For **Resource tags**, optionally add tags as key-value pairs to help you identify the configuration. Then, choose **Next**. 

1.  On the **Review and create** page, review your settings. To change your settings, choose **Edit**. Then, choose **Create**. 

    After you create the policy, it manages the auto-enable settings for GuardDuty protection plans. While the policy is active, you can't change these settings independently on the **Protection plans** page in the GuardDuty console. 

## Editing a configuration policy
<a name="securityhub-v2-configuration-edit"></a>

 You can edit the capabilities, Regions, and accounts associated with a configuration policy. When you open a policy for editing, the console displays its current configuration. 

 On the **Configured policies** tab of the **Configurations** page, each policy has a policy type: Security Hub, Security Hub CSPM, Inspector, or GuardDuty. Your organization might have several policies. Choose the policy that you want to edit, and then expand the following section that matches its policy type. 

### Editing a Security Hub policy
<a name="securityhub-v2-configuration-edit-sh"></a>

**To edit a Security Hub policy**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  In the **Configured policies** tab, choose the radio button for the policy you want to edit, and then choose **Edit**. 

1.  On the **Edit security management policy** page, configure the following settings: 

   1.  For **Capability selection**, select the capabilities for this policy to configure. **Security Hub** is always selected. You can also select **Network reachability scanning**. For each capability that you select, choose one of the following options for **Policy action**: 
      + **Enable** – Enforces the capability as enabled. Member accounts can't disable it.
      + **Disable** – Enforces the capability as disabled. Member accounts can't enable it.
      + **Custom** – Enables the capability in some Regions and disables it in others.

       To set all capabilities to the same policy action, under **Quick actions**, choose **Enable all** or **Disable all**. You can then change the policy action for individual capabilities. 

       Enabling **Network reachability scanning** grants AWS permissions to run network tests against resources that are supported by this feature. 

   1.  For **Account selection**, choose one of the following options: 
      + **All organizational units and accounts** – Applies the configuration to your entire organization.
      + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
      + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

   1.  For **Region selection**, choose how to set Regions: 
      + If all selected capabilities use the same policy action, choose **Across all selected capabilities** to use the same Regions for all capabilities. To set Regions for each capability, choose **Per capability**.
      + If the selected capabilities use different policy actions, the console uses **Per capability**, and **Across all selected capabilities** isn't available. Expand each capability to set its Regions.

       For **Regions**, set the Regions based on the policy action: 
      + **Enable** – Choose **Enable in all currently available Regions** or **Enable in some Regions**. We recommend the first option. Optionally, select **Auto-enable new Regions**.
      + **Disable** – Choose **Disable in all currently available Regions** or **Disable in some Regions**. We recommend the first option. Optionally, select **Auto-disable new Regions**.
      + **Custom** – For **Enabled Regions**, choose **Enable all Regions and auto-enable new Regions** or **Enable specific Regions**. For **Disabled Regions**, choose the Regions to disable. If you select a Region as both enabled and disabled, the Region is disabled.

   1.  (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  For **Details**, enter a **Name** for the policy, and optionally a **Description**. The name must be unique for all policies in your organization. Then, choose **Next**. 

1.  On the **Review and apply** page, review your changes. To change your settings, choose **Edit**. Then, choose **Update**. 

### Editing an AWS Security Hub CSPM policy
<a name="securityhub-v2-configuration-edit-cspm"></a>

**To edit an AWS Security Hub CSPM policy**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  In the **Configured policies** tab, choose the radio button for the policy you want to edit, and then choose **Edit**. 

1.  On the **Configure CSPM policy** page, for **Details**, enter a **Name** for the policy, and optionally a **Description**. The name must be unique for all policies in your organization. Then, choose **Next**. 

1.  On the **Accounts and Regions** page, configure the following settings: 

   1.  For **Account selection**, choose one of the following options: 
      + **All organizational units and accounts** – Applies the configuration to your entire organization.
      + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
      + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

   1.  For **Regions**, choose one of the following options: 
      + **Enable in all currently available Regions** – Enables AWS Security Hub CSPM in all currently available Regions. We recommend this option. Optionally, select **Auto-enable new Regions** to automatically enable AWS Security Hub CSPM in new Regions.
      + **Specify Regions in which to enable or disable** – Choose the Regions in which to enable or disable AWS Security Hub CSPM.
      + **Disable in all currently available Regions** – Disables AWS Security Hub CSPM in all currently available Regions.

   1.  (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  Choose **Next**. 

1.  On the **Standards and controls** page, configure the following settings: 

   1.  For **Security standards**, choose the standards to enable. By default, AWS Foundational Security Best Practices v1.0.0 and CIS AWS Foundations Benchmark v5.0.0 are selected. (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  For **Controls**, choose one of the following options: 
      + **Enable all controls** – Evaluates all controls in your enabled standards, including newly released controls. We recommend this option.
      + **Customize** – Choose **Enable all by default (disable specific)** or **Disable all by default (enable specific)**. Then, select the controls to disable or enable.
      + **Disable all controls** – Disables all controls in your enabled standards.

   1.  (Optional) For **Custom control parameters**, select **Customize control parameters**. Choose a control, and then set its parameter values. To customize more controls, choose **Customize additional control**. Controls that you don't customize use their default parameter values. 

   1.  Choose **Next**. 

1.  On the **Regional overrides** page, optionally add Region-specific customizations. To apply different settings in specific Regions, choose **Add region customization**. In the dialog box, for **Regions**, choose the Regions. Configure **Security standards**, **Controls**, and **Custom control parameters** as described in the previous step. Then, choose **Save**. 

    A customization must differ from the baseline settings before you can save it. Each Region can belong to only one customization. Regions without a customization inherit the baseline standards and controls. 

    Choose **Next**. 

1.  On the **Review and create** page, review your changes. To change the settings for a step, choose **Edit** for that step. Then, choose **Update**. 

### Editing an Amazon Inspector policy
<a name="securityhub-v2-configuration-edit-inspector"></a>

**To edit an Amazon Inspector policy**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  In the **Configured policies** tab, choose the radio button for the policy you want to edit, and then choose **Edit**. 

1.  On the **Edit vulnerability management policy** page, configure the following settings: 

   1.  For **Capability selection**, select the capabilities for this policy to configure. You can select **EC2 scanning**, **ECR scanning**, **Lambda scanning**, **Lambda code scanning**, **Code security**, and **Machine images**. **Lambda code scanning**, **Code security**, and **Machine images** incur additional charges. For each capability that you select, choose one of the following options for **Policy action**: 
      + **Enable** – Enforces the capability as enabled. Member accounts can't disable it.
      + **Disable** – Enforces the capability as disabled. Member accounts can't enable it.
      + **Custom** – Enables the capability in some Regions and disables it in others.

       To set all capabilities to the same policy action, under **Quick actions**, choose **Enable all** or **Disable all**. You can then change the policy action for individual capabilities. This policy doesn't configure capabilities that you don't select. 

       If you enable **Code security**, it requires additional configuration. For more information, see [Amazon Inspector Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) in the *Amazon Inspector User Guide*. 

   1.  For **Account selection**, choose one of the following options: 
      + **All organizational units and accounts** – Applies the configuration to your entire organization.
      + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
      + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

   1.  For **Region selection**, choose how to set Regions: 
      + If all selected capabilities use the same policy action, choose **Across all selected capabilities** to use the same Regions for all capabilities. To set Regions for each capability, choose **Per capability**.
      + If the selected capabilities use different policy actions, the console uses **Per capability**, and **Across all selected capabilities** isn't available. Expand each capability to set its Regions.

       For **Regions**, set the Regions based on the policy action: 
      + **Enable** – Choose **Enable in all currently available Regions** or **Enable in some Regions**. We recommend the first option. Optionally, select **Auto-enable new Regions**.
      + **Disable** – Choose **Disable in all currently available Regions** or **Disable in some Regions**. We recommend the first option. Optionally, select **Auto-disable new Regions**.
      + **Custom** – For **Enabled Regions**, choose **Enable all Regions and auto-enable new Regions** or **Enable specific Regions**. For **Disabled Regions**, choose the Regions to disable. If you select a Region as both enabled and disabled, the Region is disabled.

   1.  (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

   1.  For **Details**, enter a **Name** for the policy, and optionally a **Description**. The name must be unique for all policies in your organization. Then, choose **Next**. 

1.  On the **Review and apply** page, review your changes. To change your settings, choose **Edit**. Then, choose **Update**. 

### Editing an Amazon GuardDuty policy
<a name="securityhub-v2-configuration-edit-guardduty"></a>

**To edit an Amazon GuardDuty policy**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  In the **Configured policies** tab, choose the radio button for the policy you want to edit, and then choose **Edit**. 

1.  On the **Edit threat detection policy** page, configure the following settings: 

   1.  For **Region scope**, choose one of the following options: 
      + **Set a default for all Regions** – Applies one default configuration to every AWS Region. You can override specific Regions in **Regional overrides**.
      + **No default — manage only specific Regions** – This policy manages only the Regions that you add in **Regional overrides**. It doesn't manage other Regions. You must add at least one regional override.

   1.  If you chose **Set a default for all Regions**, for **Default configuration**, select the protection plans for this policy to manage. For each protection plan that you select, choose one of the following options for **Policy action**: 
      + **Enable** – Enforces the protection plan as enabled. Member accounts can't disable it.
      + **Disable** – Enforces the protection plan as disabled. Member accounts can't enable it.

       To set all protection plans to the same policy action, under **Quick actions**, choose **Enable all** or **Disable all**. You can then change the policy action for individual protection plans. This policy doesn't manage protection plans that you don't select. **Foundational threat detection** is always selected. It must be enabled if you enable any other protection plan. 

   1.  For **Regional overrides**, choose **Add regional override**. This step is optional if you set a default, and required if you chose **No default — manage only specific Regions**. In the dialog box, choose the Regions for the override. Under **Protection plans**, select the protection plans and policy actions in the same way as for the default configuration. Then, choose **Save**. 

       A regional override fully replaces the default configuration for the Regions that you choose. Specify every protection plan that you want this policy to manage in those Regions. The same configuration applies to all of the Regions in the override. 

   1.  For **Account selection**, choose one of the following options: 
      + **All organizational units and accounts** – Applies the configuration to your entire organization.
      + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
      + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

   1.  For **Details**, enter a **Name** for the policy, and optionally a **Description**. The name must be unique for all policies in your organization. Then, choose **Next**. 

1.  On the **Review and create** page, review your changes. To change your settings, choose **Edit**. Then, choose **Update**. 

    When you update the policy, you change the auto-enable settings that it manages for GuardDuty protection plans. These settings on the **Protection plans** page in the GuardDuty console remain managed by the policy, and you can't change them independently. 

## Deleting a configuration policy
<a name="securityhub-v2-configuration-delete"></a>

 You can delete a configuration policy. When you delete a policy, the service removes all attached accounts and organizational units from the policy. 

**To delete a configuration policy**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  In the **Configured policies** tab, select the policy you want to delete, and then choose **Delete**. 

1.  Enter `delete` in the confirmation box, and then choose **Delete**. 