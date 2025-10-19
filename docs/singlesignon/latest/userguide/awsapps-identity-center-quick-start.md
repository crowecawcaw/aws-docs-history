# Quick start: Setting up IAM Identity Center
 to test AWS managed applications


 If your administrator hasn’t already provided you with access to IAM Identity Center, you can use the steps 
 in this topic to set up IAM Identity Center to test AWS managed applications. You'll learn how 
 to enable IAM Identity Center, create a user directly in IAM Identity Center, and assign that user to an AWS managed 
 application.
 


 This topic provides quick-start steps on how to enable IAM Identity Center in either of the following ways: 
 


* With AWS Organizations – If you choose this option, an *organization instance* of IAM Identity Center is
 created.
* Only in your specific AWS account – If you choose this
 option, an *account instance* of IAM Identity Center is
 created.

 For information about these instance types, see [Organization and account instances of IAM Identity Center](identity-center-instances.md "identity-center-instances.md").
 


## Prerequisites


Before you enable IAM Identity Center, confirm the following:



* **You have an AWS account** – If
 you do not have an AWS account, see [Getting
 started with an AWS account](https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html "https://docs.aws.amazon.com/accounts/latest/reference/getting-started.html") in the *AWS Account
 Management Reference Guide.*
* **The AWS managed application works with
 IAM Identity Center** – Review the list of [AWS managed applications
 that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md") to confirm
 that the AWS managed application you want to test works with
 IAM Identity Center.
* **You’ve reviewed Regional
 considerations** – Make sure that the AWS managed
 application you want to test is supported in the AWS Region where you
 enable IAM Identity Center. For more information, see the documentation for the AWS
 managed application.


###### Note

You must deploy your AWS managed application in the same Region
 where you plan to enable IAM Identity Center.

## 
 Setting up an organization instance of IAM Identity Center to test AWS managed applications


###### Note


 This topic describes how to enable IAM Identity Center with AWS Organizations, which is the recommended
 way to enable IAM Identity Center.
 


**Confirm your permissions**


To enable IAM Identity Center with AWS Organizations, you must sign in to the AWS
 Management Console as either of the following:



* A user with administrative permissions in the AWS account
 where IAM Identity Center will be enabled with AWS Organizations.
* The root user (not recommended unless no other administrative
 users exist).


###### Important

The root user has access to all AWS services and
 resources in the account. As a security best practice,
 unless you have no other credentials, do not use your
 account's root credentials to access AWS resources. These
 credentials provide unrestricted account access and are
 difficult to revoke.

### Step 1. Enable IAM Identity Center with AWS Organizations


1. Do one of the following to sign in to the AWS Management Console.




	* **New to AWS (root user)**
	 – Sign in as the account owner by choosing **Root
	 user** and entering your AWS account email
	 address. On the next page, enter your password.
	* **Already using AWS with a standalone
	 AWS account (IAM credentials)** – Sign
	 in using your IAM credentials with administrative
	 permissions.
2. On the AWS Management Console Home page, select the IAM Identity Center service or
 navigate to the 
 [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. Choose **Enable**, and enable IAM Identity Center with AWS Organizations.
 When you do this, you’re creating an [organization
 instance](organization-instances-identity-center.md "organization-instances-identity-center.md") of IAM Identity Center.

### Step 2. Create an administrative user in IAM Identity Center


This procedure describes how to create a user directly in the built-in
 Identity Center directory. This directory isn't connected to any other directory
 that your administrator might use to manage workforce users. After you create
 the user in IAM Identity Center, you'll specify new credentials for this user. When you sign
 in as this user to test your AWS managed application, you'll sign in with the
 new credentials, not with any existing credentials that you use to access
 corporate resources.


###### Note

We recommend that you use this method for creating users for testing
 purposes only.

1. In the navigation pane of the IAM Identity Center console, choose
 **Users**, and then choose **Add
 user**.
2. Follow the guidance in the console to add the user. Keep
 **Send an email to this user with password setup
 instructions** selected and make sure that you specify an
 email address to which you have access.
3. In the navigation pane, choose AWS accounts, select the check box
 next to your account, and choose **Assign users or
 groups**.
4. Choose the **Users** tab, select the check box next
 to the user that you just added, and choose
 **Next**.
5. Choose **Create permission set**, and follow the
 guidance in the console to create the `AdministratorAccess`
 predefined permission set.
6. When you’re done, the new permission set appears in the list. Close
 the **Permission sets** tab in your browser window,
 return to the **Assign users and groups** tab, and
 choose the refresh icon next to **Create permission
 set**.
7. On the **Assign users and groups** browser tab, the
 new permission set appears in the list. Select the check box next to the
 name of the permission set, choose **Next**, and then
 choose **Submit**.
8. Sign out of the console.

### Step 3. Sign in to the AWS access portal as an administrative user


The AWS access portal is a web portal that provides the user that you created with
 access to the AWS Management console. Before you can sign in to the
 AWS access portal, you must accept the invitation to join IAM Identity Center and activate your user
 credentials.


1. Check your email for the subject line **Invitation to join
 AWS IAM Identity Center**.
2. Choose **Accept invitation**, and follow the guidance
 on the sign-up page to set a new password, sign in, and register an MFA
 device for your user.
3. After you register your MFA device, the AWS access portal opens.
4. In the AWS access portal, select your AWS account and choose
 **AdministratorAccess**. You are redirected to the
 AWS Management Console.

### Step 4. Configure the AWS managed application to use IAM Identity Center


1. While you are signed in to the AWS Management Console, open the
 console for the AWS managed application that you plan to use.
2. Follow the guidance in the console to configure the AWS managed
 application to use IAM Identity Center. During this process, you can assign the user
 that you created to the application.

## Setting up an account instance of IAM Identity Center to test AWS managed applications


###### Note

An account instance of IAM Identity Center limits your deployment to a single
 AWS account. You must enable this instance in the same AWS Region as the
 AWS application you want to test.


**Confirm your app**



 All AWS managed applications that work with IAM Identity Center can be used with organization instances of 
 IAM Identity Center. However, only some of these applications can be used with account instances of IAM Identity Center. 
 Review the list of [AWS managed applications
 that you can use with IAM Identity Center](awsapps-that-work-with-identity-center.md "awsapps-that-work-with-identity-center.md").
 


### Step1. Enable an account instance of IAM Identity Center


1. Do one of the following to sign in to the AWS Management Console.




	* **New to AWS (root user)**
	 – Sign in as the account owner by choosing **Root
	 user** and entering your AWS account email
	 address. On the next page, enter your password.
	* **Already using AWS with a standalone
	 AWS account (IAM credentials)** – Sign
	 in using your IAM credentials with administrative
	 permissions.
2. On the AWS Management Console Home page, select the IAM Identity Center service or
 navigate to the 
 [IAM Identity Center console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
3. Choose **Enable**.
4. On the **Enable IAM Identity Center with AWS Organizations** page, 
 choose **enable an account instance of IAM Identity Center**.
5. On the **Enable account instance of IAM Identity Center** page, review the 
 information and optionally add tags that you want to associate with this account instance. 
 Then choose **Enable**.

### Step 2.
 Create a user in IAM Identity Center


This procedure describes how to create a user directly in the built-in
 Identity Center directory. This directory isn't connected to any other directory
 that your administrator might use to manage workforce users. After you create
 the user in IAM Identity Center, you'll specify new credentials for this user. 
 
 When you sign in as this user to test your AWS managed application, you'll sign in with the
 new credentials. The new credentials will not allow you to access other
 corporate resources.


###### Note

We recommend that you use this method for creating users for testing
 purposes only.

1. In the navigation pane of the IAM Identity Center console, choose
 **Users**, and then choose **Add
 user**.
2. Follow the guidance in the console to add the user. Keep
 **Send an email to this user with password setup
 instructions** selected and make sure that you specify an
 email address to which you have access.
3. Sign out of the console.

### Step 3. Sign in to the AWS access portal as your IAM Identity Center user


The AWS access portal is a web portal that provides the user that you created with
 access to the AWS Management console. Before you can sign in to the
 AWS access portal, you must accept the invitation to join IAM Identity Center and activate your user
 credentials.


1. Check your email for the subject line **Invitation to join
 AWS IAM Identity Center**.
2. Choose **Accept invitation**, and follow the guidance
 on the sign-up page to set a new password, sign in, and register an MFA
 device for your user.
3. After you register your MFA device, the AWS access portal opens. When applications 
 are available to you, you’ll find them under the **Applications** tab.


###### Note

AWS applications that support account instances allow users
 to sign in to applications without requiring additional
 permissions. Therefore, the **Accounts** tab
 will remain empty.

### Step 4. Configure the AWS managed application to use IAM Identity Center


1. While you are signed in to the AWS Management Console, open the
 console for the AWS managed application that you plan to use.
2. Follow the guidance in the console to configure the AWS managed
 application to use IAM Identity Center. During this process, you can assign the user
 that you created to the application.
