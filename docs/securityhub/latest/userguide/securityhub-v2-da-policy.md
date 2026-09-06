

# Managing configuration of member accounts in an AWS Organization
<a name="securityhub-v2-da-policy"></a>

 The delegated administrator for an AWS Organization can configure security capabilities across member accounts and Regions. Two types of configurations are available: **Policies** and **Deployments**. **Policies** generate AWS Organizations policies for accounts and Regions for AWS Security Hub and Amazon Inspector. **Deployments** are a one-time action to enable a security capability across selected accounts and Regions for Amazon GuardDuty and AWS Security Hub CSPM. Unlike policies, you cannot view or edit deployments and deployments do not apply to newly enabled accounts. As an alternative, auto-enable features for new member accounts are available in Amazon GuardDuty and AWS Security Hub CSPM. 

## Security Hub configuration catalog
<a name="securityhub-v2-configuration-catalog"></a>

 The configuration catalog of Security Hub offers multiple options to help configure your AWS Organization accounts for the security capabilities provided by Security Hub. 

 The following are the options available in the Security Hub configuration catalog.

### Security Hub (essential and additional capabilities)
<a name="securityhub-v2-configuration-catalog-SH"></a>

 This is the recommended configuration to deploy for Security Hub. 

 **Type**: Policy and Deployments 

 **Description**: This configuration turns on Security Hub's essential security management, posture management, threat analytics, and vulnerability management capabilities. It optionally enables additional capabilities. 

### Threat analytics from GuardDuty
<a name="securityhub-v2-configuration-catalog-ta"></a>

 **Type**: Deployment 

 **Description**: Turn on selected Amazon GuardDuty capabilities to continuously monitor, analyze, and process AWS data sources and logs in your AWS environment. 

### Posture management from AWS Security Hub CSPM
<a name="securityhub-v2-configuration-catalog-CSPM"></a>

 **Type**: Deployment 

 **Description**: This configuration turns on Security Hub CSPM's standards and controls, which detect when your AWS accounts and resources deviate from security best practices. 

### Vulnerability management from Amazon Inspector
<a name="securityhub-v2-configuration-catalog-vuln"></a>

 **Type**: Policy 

 **Description**: This configuration turns on selected Amazon Inspector capabilities that automatically discover workloads, instances, container images, and other resources, and scans them for vulnerabilities and network exposure. 

## Enabling a configuration with a type of policy
<a name="securityhub-v2-configuration-enable-policy"></a>

 The following procedure describes how to create a configuration with a type of policy for your AWS Organization accounts. To create a configuration policy, you must first create the delegated administrator policy in the AWS Organization management account. For information about creating the delegated administrator policy in Security Hub, see [Creating the delegated administrator policy in Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-policy-statement.html). 

**To create a policy that enables and disables member accounts**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  Choose an item with a type of **policy** or **policy and deployment** from the Configuration catalog. To fully configure Security Hub, choose **Security Hub (essential and additional capabilities)**. 

1.  On the **Configure Security Hub** page, in the **Details** section, enter a name and a description for the policy. 

1.  In the **Security capabilities** section, choose one of the following: 
   + **Enable all capabilities** – Turns on all Security Hub essential capabilities, threat analytics, and additional capabilities.
   + **Customize capabilities** – Select capabilities from the Security management, Threat analytics, and Vulnerability management sections. You cannot deselect capabilities that are part of the Security Hub essential plan.

1.  In the **Account selection** section, choose one of the following options: 
   + **All organizational units and accounts** – Applies the configuration to your entire organization.
   + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
   + **No organizational units or accounts** – Does not apply the configuration to any organizational unit or account.

1.  In the **Regions** section, choose one of the following: 
   + **Enable all Regions** – Optionally choose whether to automatically enable new Regions.
   + **Disable all Regions** – Optionally choose whether to automatically disable new Regions.
   + **Specify Regions** – Choose which Regions to enable and disable.

1.  (Optional) For **Advanced settings**, see [Inheritance operators](https://docs.aws.amazon.com/organizations/latest/userguide/policy-operators.html) in the *AWS Organizations User Guide*. 

1.  (Optional) For **Resource tags**, add tags as key-value pairs to help you identify the configuration. 

1.  Choose **Next**. 

1.  Review your changes, and then choose **Apply**. 

    The configuration status of your policy displays at the top of the Policies page. Each capability provides a status indicating whether it was configured successfully or has deployment failures. For any failures, choose the failure link to see more details. To view the effective policy at the account level, review the **Organization** tab on the **Configurations** page. 

## Enabling a configuration with a type of deployment
<a name="securityhub-v2-configuration-enable-deployment"></a>

The following procedure describes how to create a configuration with a type of deployment for your AWS Organization accounts.

**To create a deployment that enables member accounts**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  Choose an item with a type of **deployment** from the Configuration catalog. 

1.  In the **Security capabilities** section, select the security capabilities to turn on. 

1.  In the **Account selection** section, choose one of the following options: 
   + **All organizational units and accounts** – Applies the deployment to your entire organization.
   + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the deployment applies.
   + **No organizational units or accounts** – Does not apply the deployment to any organizational unit or account.

1.  In the **Regions** section, choose one of the following: 
   + **Enable all Regions** – Optionally choose whether to automatically enable new Regions.
   + **Disable all Regions** – Optionally choose whether to automatically disable new Regions.
   + **Specify Regions** – Choose which Regions to enable and disable.

1.  Choose **Configure**. 

## Editing a configuration policy
<a name="securityhub-v2-configuration-edit"></a>

 You can edit the capabilities, Regions, and accounts associated with a configuration policy. When you open a policy for editing, the console displays the current configuration. 

**Note**  
 Changes apply only to the capabilities you select in the updated policy. Unselected capabilities retain their existing configuration across the accounts and Regions in the policy. 

**To edit a configuration policy**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  In the **Configured policies** tab, choose the radio button for the policy you want to edit, and then choose **Edit**. 

1.  In the **Capability** section, choose one of the following: 
   + **Configure and enable all capabilities** – Enables all capabilities in the policy.
   + Select individual capabilities and choose **Enable**, **Disable**, or **Custom** for each one.

1.  In the **Account selection** section, choose one of the following options: 
   + **All organizational units and accounts** – Applies the policy to your entire organization.
   + **Specific organizational units and accounts** – Use the search bar or organizational structure tree to select the organizational units and accounts where the policy applies.
   + **No organizational units or accounts** – Removes the policy from all targets.

1.  In the **Regions** section, configure which Regions the policy applies to. The options depend on your **Capability** selections. 

    **If you chose to enable all capabilities:** 
   + **Across all selected capabilities** – Sets the same Region configuration for all capabilities.
   + **Per capability** – Lets you choose Regions individually for each capability.

    Then choose **Enable all Regions** (with the option to automatically enable new Regions) or **Enable in some Regions** to select specific Regions. 

    **If you chose mixed actions (enable, disable, or custom) for individual capabilities:** 
   + If all selected capabilities share the same action, choose **Across all selected capabilities** to set Regions uniformly. To set Regions for each capability individually, choose **Per capability**.
   + If capabilities have different actions, you must assign Regions for each capability individually.
   +  For capabilities with the **Custom** action, choose **Across all selected capabilities** to set Regions uniformly for all capabilities. To configure Regions for each capability separately, choose **Per capability**. 

1.  Choose **Next**. 

1.  Review your changes, and then choose **Update**. The updated policy configures the target accounts. 

## Deleting a configuration policy
<a name="securityhub-v2-configuration-delete"></a>

 You can delete a configuration policy. When you delete a policy, the service removes all attached accounts and organizational units from the policy. 

**To delete a configuration policy**

1.  Sign in using your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the navigation pane, choose **Management**, and then choose **Configurations**. 

1.  In the **Configured policies** tab, select the policy you want to delete, and then choose **Delete**. 

1.  Enter `delete` in the confirmation box, and then choose **Delete**. 