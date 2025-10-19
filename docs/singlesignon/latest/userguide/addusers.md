# Add users to your Identity Center directory

Users and groups that you create in your Identity Center directory are available in IAM Identity Center
 only. Use the following procedure to add users to your Identity Center directory.
 Alternatively, you can call the AWS API operation [CreateUser](../IdentityStoreAPIReference/API_CreateUser.md "../IdentityStoreAPIReference/API_CreateUser.md") to add users.


Console
###### To add a user

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Users**.
3. Choose **Add user** and provide the following
 required information:


	1. **Username** – This user name is
	 required to sign in to the AWS access portal and cannot be changed
	 later. It must be between 1 and 100 characters.
	2. **Password** – You can either send
	 an email with the password setup instructions (this is the
	 default option) or generate a one-time password. If you are
	 creating an administrative user and you choose to send an
	 email, make sure that you specify an email address that you
	 can access.
	
	
		1. **Send an email to this user with password
		 setup
		 instructions** – This option
		 automatically sends the user an email addressed from
		 Amazon Web Services, with the subject line **Invitation
		 to join AWS IAM Identity Center**. The email invites the
		 user on behalf of your company to access the IAM Identity Center
		 AWS access portal, and registers a password. The email
		 invitation will expire in seven days. If this
		 happens, you can resend the email by choosing **Reset
		 password**, and then choosing **Send
		 an email to the user with instructions for resetting
		 the
		 password**. Before the user accepts the
		 invitation, you will see **Send email
		 verification link**, which is meant to
		 verify their email address. However, this step is
		 optional and will disappear after the user accepts
		 the invitation and registers a password.
		
		
		###### Note
		
		In certain Regions, IAM Identity Center sends
		 emails to users using Amazon Simple Email Service from another
		 AWS Region. For information about how emails
		 are sent, see [Cross-Region emails with Amazon SES](regions.md#cross-region-calls "regions.md#cross-region-calls").
		
		All emails sent by the IAM Identity Center service will come
		 from either the address `no-reply@signin.aws.com` or `no-reply@login.awsapps.com`. We recommend
		 that you configure your email system so that it
		 accepts emails from these sender email addresses
		 and does not handle them as junk or spam.
		2. **Generate a one-time password that you
		 can share with
		 this user** – This option
		 provides you with the AWS access portal URL and password
		 details that you can manually send to the user from
		 your email address. The user will need to verify
		 their email address. You can initiate the process by
		 choosing **Send email verification link**.
		 The email verification link will expire in seven
		 days. If this happens, you can resend the email
		 verification link by choosing **Reset
		 password**, and then choosing **Generate
		 a
		 one-time password and share the
		 password with the user**.
	3. **Email address** – The email
	 address must be unique.
	4. **Confirm email address**
	5. **First name** – You must enter a
	 name here for automatic provisioning to work. For more
	 information, see [Provision users and groups from an external identity provider using SCIM](provision-automatically.md "provision-automatically.md").
	6. **Last name** – You must enter a
	 name here for automatic provisioning to work.
	7. **Display name**
	
	
	
	###### Note
	
	(Optional) If applicable, you can specify values for
	 additional attributes such as the user's **Microsoft
	 365 immutable
	 ID** to help provide the user with single
	 sign-on access to certain business applications.
4. Choose **Next**.
5. If applicable, select one or more groups to which you want to add
 the user, and choose **Next**.
6. Review the information that you specified for **Step 1:
 Specify user
 details** and **Step 2: Add user to groups -
 optional**. Choose **Edit** by either step
 to make any changes. After you confirm that the correct information
 is specified for both steps, choose **Add user**.


AWS CLI
###### To add a user


 The following `create-user` command creates a new user in
 your Identity Center directory. 



```
aws identitystore create-user \
    --identity-store-id d-1234567890 \
    --user-name johndoe \
    --name "GivenName=John,FamilyName=Doe" \
    --display-name "John Doe" \
    --emails "Type=work,Value=johndoe@example.com"
```

Output:



```
{
    "UserId": "1234567890-abcdef",
    "IdentityStoreId": "d-1234567890"
}
```

###### Note

When you create users with the `create-user` CLI command or
 the [CreateUser](../IdentityStoreAPIReference/API_CreateUser.md "../IdentityStoreAPIReference/API_CreateUser.md") API
 operation, the users do not have passwords. You can update the settings in IAM Identity Center to
 send these users a verification email after their first attempt to sign
 on so they can set up a password. If you do not enable this setting, you
 must generate a one-time password and share it with the user. For more
 information, see [Email one-time password to users created with API or
 CLI](userswithoutpwd.md "userswithoutpwd.md").
