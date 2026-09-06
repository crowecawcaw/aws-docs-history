

# Enabling Security Hub
<a name="securityhub-v2-enable"></a>

 You can enable Security Hub for any AWS account. This section of the documentation describes all the steps required to enable Security Hub for an AWS Organization, or a standalone account. 

For a brief demonstration of how to enable Security Hub watch the following video:

[![AWS Videos](http://img.youtube.com/vi/prtnhCfjUpM/0.jpg)](http://www.youtube.com/watch?v=prtnhCfjUpM)


## Enable Security Hub for an AWS Organization
<a name="securityhub-v2-enable-management-account"></a>

This section includes three steps: 
+  In **Step 1**, the AWS organization management account designates a delegated administrator for their AWS Organization, creates the delegated administrator policy, and optionally enables Security Hub for their own account. 
+  In **Step 2**, the delegated administrator for the organization enables Security Hub for their own account. 
+  In **Step 3**, the delegated administrator for the organization configures all member accounts in the organization, for Security Hub and other supported security services. 

### Step 1. Delegating an administrator account and optionally enabling Security Hub in the AWS organization management account
<a name="step-1"></a>

**Note**  
 Complete this step in one Region of the organization management account. 

 When assigning the delegated administrator account for Security Hub, the account you can choose for your delegated administrator depends on how you have configured a delegated administrator for Security Hub CSPM. If you have configured a delegated administrator for Security Hub CSPM, and that account is not the organization management account, then that account is automatically set as the Security Hub delegated administrator and a different account cannot be chosen. If the delegated administrator account for Security Hub CSPM is set as the organization management account or is not set at all, you can choose which account to assign as your Security Hub delegated administrator account, except for the organization management account. 

 For information about designating a delegated administrator in Security Hub, see [Designating a delegated administrator account in Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-set-da.html). For information about creating the delegated administrator policy in Security Hub, see [Creating the delegated administrator policy in Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-policy-statement.html). 

**To designate an administrator for Security Hub**

1.  Sign in to your AWS account with your AWS organization management account credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the Security Hub homepage, choose **Security Hub**, and then choose **Get started**. 

1.  In the **Delegated administrator** section, choose an administrator account based on the provided options. As a best practice, use the same delegated administrator across security services for consistent governance. 

1.  Choose the **Trusted access** checkbox. Choosing this option grants your delegated administrator account the ability to configure certain capabilities, such as GuardDuty Malware Protection, on member accounts. If you uncheck this option, Security Hub cannot enable these features on your behalf and you must enable them directly through the service that the feature is associated with. 

1.  (Optional) For **Account enablement**, select the box to enable Security Hub for your AWS account. 

1.  For **Delegated administrator policy**, choose one of the following options to add the policy statement. 

   1.  (Option 1) Choose **Update this for me**. Select the box under the policy statement to confirm that Security Hub automatically creates a delegation policy granting all required permission to the delegated administrator. 

   1.  (Option 2) Choose **I want to attach this manually**. Choose **Copy and attach**. In the AWS Organizations console, under **Delegated administrator for AWS Organizations**, choose **Delegate**, and paste the resource policy in the delegation policy editor. Choose **Create Policy**. Open the tab where you are in the Security Hub console. 

1.  Choose **Configure**. 

### Step 2. Enable Security Hub in the delegated administrator account
<a name="step-2"></a>

 The delegated administrator account completes this step. After the AWS Organization management account designates a delegated administrator for their organization, the delegated administrator must enable Security Hub for their own account before enabling for the entire AWS Organization. 

**To enable Security Hub in the delegated administrator account**

1.  Sign in to your AWS account with your delegated administrator credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the Security Hub homepage, choose **Get started**. 

1.  The security capabilities section outlines the capabilities that are automatically enabled and included in the base per-resource price of Security Hub. 

1.  (Optional) For **Tags**, determine whether to add a key-value pair to the account setup. 

1.  Choose **Enable Security Hub** to finish enabling Security Hub. 

1.  (Recommended) from the popup choose **Configure my organization** and proceed to Step 3. 

### Step 3. Create a policy that enables Security Hub in all member accounts
<a name="step-3"></a>

 After enabling Security Hub in the delegated administrator account for an organization you need to create a policy that defines which services and capabilities are enabled in the organization member accounts. For more information, see [Enabling a configuration with a type of policy](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-da-policy.html#securityhub-v2-configuration-enable-policy). 

 After you enable Security Hub, the following resources are created in your account: 
+  A service-linked role called [AWSServiceRoleForSecurityHubV2](https://docs.aws.amazon.com/securityhub/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy). 
+  Service-linked configuration recorders. See [Service-linked recorder](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-concepts.html#concept-slcr) in the Security Hub concepts documentation for more details. 
+  A service-linked analyzer. See [Service-linked analyzer](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-concepts.html#concept-sla) in the Security Hub concepts documentation for more details. 

## Enable Security Hub in a standalone account
<a name="securityhub-v2-enable-standalone-account"></a>

 This procedure describes how to enable Security Hub in a standalone account. A standalone account is an AWS account that has not enabled AWS organizations. 

**To enable Security Hub in a standalone account**

1.  Sign in to your AWS account with your account credentials. Open the Security Hub console at [https://console.aws.amazon.com/securityhub/v2/home](https://console.aws.amazon.com/securityhub/v2/home). 

1.  From the Security Hub homepage, choose **Get started**. 

1.  In the **Security capabilities** section do one of the following: 

   1.  (Option 1) Choose **Enable all capabilities**. This turns on all of the Security Hub essential capabilities, threat analytics, and additional capabilities. 

   1.  (Option 2) Choose **Customize capabilities**. Select the capabilities to turn on from the Security management, Threat analytics, and Vulnerability management sections. You cannot deselect any capabilities that are part of the Security Hub essential plan capabilities. 

1.  In the **Regions** section, choose **Enable all Regions** or **Enable specific Regions**. If you choose **Enable all Regions**, you can determine whether to automatically enable new Regions. If you choose **Enable specific Regions**, you must choose which Regions you want to enable. 

1.  (Optional) For **Resource tags**, add tags as key-value pairs to help you easily identify the configuration. 

1.  Choose **Enable Security Hub**. 

 After you enable Security Hub, the following resources are created in each account where you enabled the service: 
+  A service-linked role called [AWSServiceRoleForSecurityHubV2](https://docs.aws.amazon.com/securityhub/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-awssecurityhubv2servicerolepolicy). 
+  Service-linked configuration recorders. See [Service-linked recorder](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-concepts.html#concept-slcr) in the Security Hub concepts documentation for more details. 
+  A service-linked analyzer. See [Service-linked analyzer](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-concepts.html#concept-sla) in the Security Hub concepts documentation for more details. 