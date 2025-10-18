# Initialize Network Flow Monitor for multi-account monitoring

If you want to monitor network flows in Network Flow Monitor for resources that are owned by different accounts,
 you must first configure Amazon CloudWatch with AWS Organizations. To use multiple accounts in Network Flow Monitor, you're required to turn on
 trusted access for CloudWatch, and it's a best practice to also register a delegated administrator.

In addition, if you plan to create monitors for network flows from the console, you must add
 a Network Flow Monitor policy to the role that is attached to your resources. The policy enables you to view resources from 
 other accounts in the console, so that you can add the resources in multiple accounts to a monitor.

To monitor network flows for resources that are owned by different accounts, there are additional configuration 
 steps to take. First, as the management account, you must configure CloudWatch with AWS Organizations to turn on trusted access, 
 and, typically, you'll also register a delegated administrator account. Then, using the delegated administrator account,
 you can add more accounts in your organization, to set the scope for your network observability to include resources
 in those accounts. (You can also add multiple accounts with a management account, but it's a best practice in Organizations
 to use the delegated administrator account when you work with resources in a service. We provide steps that follow that guidance in 
 the instructions here for Network Flow Monitor.)

Note that if you don’t need to monitor network flows for instances from multiple accounts, you can use Network Flow Monitor with a single
 account. The scope for Network Flow Monitor is automatically set to the AWS account that you sign in with.

Use the guidance in the following sections to complete these steps.

###### Contents

* [Multi-account setup overview](#CloudWatch-NetworkFlowMonitor-multi-account.overview "#CloudWatch-NetworkFlowMonitor-multi-account.overview")
* [Configure AWS Organizations](#CloudWatch-NetworkFlowMonitor-multi-account.config-orgs "#CloudWatch-NetworkFlowMonitor-multi-account.config-orgs")
* [Add multiple accounts](#CloudWatch-NetworkFlowMonitor-multi-account.config-scope "#CloudWatch-NetworkFlowMonitor-multi-account.config-scope")
* [Add permissions for the console](#CloudWatch-NetworkFlowMonitor-multi-account.console-perms "#CloudWatch-NetworkFlowMonitor-multi-account.console-perms")

## Overview of steps for using multiple accounts in Network Flow Monitor


To get started with Network Flow Monitor, any account that has not used Network Flow Monitor before must initialize Network Flow Monitor. When you initialize 
 Network Flow Monitor for an account, Network Flow Monitor adds the required service-linked role permissions and creates a scope of the account or 
 accounts to be included in network observability. To work with multiple accounts in Network Flow Monitor, there are additional steps,
 to integrate with AWS Organizations, and then add the accounts to work with.


In summary, you take the following steps:



1. Sign in to the AWS Management Console as the management account, and then do the following:




	* Complete the required steps for integrating with AWS Organizations in CloudWatch.
2. Sign in to the AWS Management Console as the delegated administrator account, and then do the following:




	* Initialize Network Flow Monitor, including adding accounts to include in your scope.
	* Add the required permissions for accessing resources that are in other accounts from the console.

If you're setting up Network Flow Monitor to work with multiple accounts and you’re not familiar with AWS Organizations, review the 
 following resources to learn about concepts such as the management account, trusted access, and the
 delegated administrator account, and to learn how to integrate Organizations with CloudWatch.
 



* [Managing 
 accounts in an organization with AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html "https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts.html") in the AWS Organizations User Guide.
* [Amazon CloudWatch 
 and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudwatch.html "https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudwatch.html") in the AWS Organizations User Guide.

Follow the steps in the following sections for specific guidance in configuring Network Flow Monitor for multiple accounts.


## Configure AWS Organizations in CloudWatch


To configure Network Flow Monitor with AWS Organizations, sign in to the management account, and turn on trusted access for CloudWatch.
 Then, register a delegated administrator account to use for initializing Network Flow Monitor and adding multiple accounts.


If you’ve already configured Organizations in CloudWatch to turn on trusted access for Organizations in CloudWatch and register
 a delegated administrator account, you don’t need to configure anything more for Organizations that is specific to Network Flow Monitor. You 
 can sign in with the delegated administrator 
 account for CloudWatch, and then initialize Network Flow Monitor, including adding multiple accounts for your network observability scope.


If you haven’t yet configured Organizations in CloudWatch, follow the steps here to turn on trusted access and register a delegated 
 administrator account.


### Turn on trusted access in CloudWatch


Before you can use Network Flow Monitor with more than one account in your organization, you must turn on trusted access for 
 AWS Organizations in Amazon CloudWatch. Use the following steps to turn on trusted access in the CloudWatch console.


###### To turn on trusted access

1. Sign in to the console with your organization’s management account.
2. In the CloudWatch console, in the navigation pane, choose **Settings**.
3. Choose the **Organizations** tab.
4. In **Organizational Management Settings**, choose **Turn on**. 
 The **Enable trusted access** page appears.
5. To review the role policy, choose **View permission** details to see the role policy.
6. Choose **Enable trusted access**.

Now, as CloudWatch discovers resources, it automatically updates information about accounts that you have permission 
 to access the resources for in Network Flow Monitor.


### Register a delegated administrator 
 account


As a best practice with AWS Organizations, the management account for your organization should register a member 
 account as a delegated administrator account for CloudWatch. After you register a delegated administrator account
 in CloudWatch, members of your organization can sign in with the delegated administrator 
 account to monitor the network performance for resources in multiple accounts in Network Flow Monitor.


Using the delegated administrator account, you can add multiple accounts for your 
 network observability scope in Network Flow Monitor. Although the management account can also create a scope that includes 
 multiple accounts, we recommend that you follow the best practices for AWS Organizations
 and use a delegated administrator account for adding multiple accounts in Network Flow Monitor. For member accounts that 
 are not the delegated administrator account, the scope is limited to the signed-in account, which 
 is automatically set for the scope. 


A delegated administrator account for Organizations is a member account that shares administrator access for service-managed 
 permissions. The account that you choose to register as a delegated administrator account must be a member account 
 in your organization. A delegated administrator account for your organization can be used outside of CloudWatch, so make 
 sure that you understand this account type before following this procedure. For more information, see 
 [Amazon CloudWatch 
 and AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudwatch.html "https://docs.aws.amazon.com/organizations/latest/userguide/services-that-can-integrate-cloudwatch.html") in the AWS Organizations User Guide.


###### To register a delegated administrator account

1. Open the CloudWatch console at
 [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Settings**.
3. Choose the **Organization** tab.
4. Choose **Register delegated administrator**.
5. In the **Register delegated administrator** window, 
 in the **Delegated administrator account ID** field, enter the 12-digit Organization member account ID.
6. Choose **Register delegated administrator**. 
 At the top of the page, a message appears indicating the account was registered successfully. 
 The **Organization Settings** page appears. To see information about the 
 delegated administrator account, hover over the number below **Delegated administrators**.

To remove or change the delegated administrator account, deregister the account first. For more information, see 
 [Deregistering a delegated administrator account](telemetry-config-turn-on.md#telemetry-config-deregister-administrator "telemetry-config-turn-on.md#telemetry-config-deregister-administrator").


## Add multiple accounts to your scope


To add accounts to your Network Flow Monitor scope, sign in with the delegated administrator account. (You can add accounts to 
 a scope if you're signed in with the management account, but it's a best practice in AWS Organizations to use the delegated 
 administrator account to work with resources.) 


After you sign in with the delegated administrator account, initialize Network Flow Monitor to authorize the required
 service-linked role permissions, set the scope for your network observability by adding accounts, and
 create an initial topology for the accounts in your scope. The account that you sign in with—in 
 this case, the delegated administrator account—is automatically included in your Network Flow Monitor scope. To add accounts 
 to your scope so that you can monitor network flows for resources in multiple accounts, follow the steps here.


###### To add accounts to your scope

1. Sign in to the console with your organization’s management account.
2. In the navigation pane for the CloudWatch console, under **Network Monitoring**, 
 choose **Flow monitors**.
3. Under **Getting started with Network Flow Monitor**, in Step 1, 
 choose **Start initialization**.
4. On the **Network Flow Monitor** page, under **Add accounts**, 
 choose **Add**. The account that you're signed in with is automatically included in the 
 scope and already appears in the **Accounts in scope** table as **(this account)**.
5. On the **Add accounts** dialog page, optionally filter the accounts, and then 
 select up to 99 additional accounts to add to your scope. The maximum number of accounts in a scope is 100.
6. Choose **Add**.
7. Choose **Initialize Network Flow Monitor**. Network Flow Monitor adds the required service-linked role permissions, 
 creates a scope that includes all the accounts you specified, and then creates an initial topology of the resources
 in the accounts in your scope.

## Set up permissions for multi-account resource 
 access (console only)


If you plan to create monitors for network flows from the console, a specific policy is required for each member account
 in your scope. This policy enables you to view resources from other accounts when you add local and remote resources to a monitor. 
 


For each of the account in your scope, create a role, **NetworkFlowMonitorAccountResourceAccess**, and attach the 
 **AmazonEC2ReadOnlyAccess** policy. To see permission details for the policy, see 
 [AmazonEC2ReadOnlyAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.html "https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonEC2ReadOnlyAccess.html") in the AWS Managed Policy Reference Guide.


This policy is in addition to the policy that you must add to each instance so that the Network Flow Monitor agent can send performance 
 metrics from the instance to the Network Flow Monitor ingestion backend server. For more information about requirements for agents, see
 [Install Network Flow Monitor agents on instances](CloudWatch-NetworkFlowMonitor-agents.md "CloudWatch-NetworkFlowMonitor-agents.md").


The following procedure provides a summary of the steps to create the required
 role for accessing resources in your scope in the Network Flow Monitor console. For general guidance on how to create a role in IAM, see
 [Create a role to give permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html")  in the AWS Identity and Access Management User Guide. 


###### To create a role for resource access in the Network Flow Monitor console

1. Sign in to the AWS Management Console and open the IAM console.
2. In the navigation pane of the console, choose **Roles**, and then 
 choose **Create role**.
3. Specify the **AWS account** trusted entity. This trusted entity 
 type enables principals in other AWS accounts to assume the role and access resources in other accounts.
4. Choose **Next**.
5. In the list of AWS managed policies, choose the **AmazonEC2ReadOnlyAccess** policy.
6. Choose **Next**.
7. For role name, enter **NetworkFlowMonitorAccountResourceAccess**.
8. Review the role, and then choose **Create role**.
