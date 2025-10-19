# Reset the IAM Identity Center user password for an end
 user

This procedure is for administrators who need to reset the password for a user in the
 IAM Identity Center directory. You'll use the IAM Identity Center console to reset passwords.


###### Considerations for identity providers and user types


* Microsoft Active Directory or external
 provider – If you are connecting IAM Identity Center to Microsoft
 Active Directory or an external provider, user password resets must be done from
 within Active Directory or the external provider. This means that passwords for
 those users cannot be reset from the IAM Identity Center console.
* Users in the IAM Identity Center directory – If you are
 an IAM Identity Center user, you can reset your own IAM Identity Center password, see [Resetting your AWS access portal user password](resetpassword-accessportal.md "resetpassword-accessportal.md").
###### To reset a password for an IAM Identity Center end user

###### Important

The instructions on this page apply to [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/ "https://aws.amazon.com/iam/identity-center/"). They do
 not apply to [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM).
 IAM Identity Center users, groups, and user credentials are different from IAM users,
 groups, and IAM user credentials. If you are looking for instructions on
 changing passwords for IAM users, see [Managing passwords for IAM users](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_passwords_admin-change-user.html") in the *AWS Identity and Access Management User
 Guide*.

1. Open the [IAM Identity Center
 console](https://console.aws.amazon.com/singlesignon "https://console.aws.amazon.com/singlesignon").
2. Choose **Users**.
3. Select the username of the user whose password you want to reset.
4. On the user details page, choose **Reset password**.
5. In the **Reset password** dialog box, select one of the
 following choices, and then choose **Reset password**:


	1. **Send an email to the user with instructions to reset the
	 password** – This option automatically sends the user an
	 email addressed from Amazon Web Services that walks them through how to reset
	 their password.
	
	
	###### Warning
	
	As a security best practice, verify that the email address for
	 this user is correct prior to selecting this option. If this
	 password reset email were to be sent to an incorrect or
	 misconfigured email address, a malicious recipient could use it to
	 gain unauthorized access to your AWS environment.
	2. **Generate a one-time password and share the password with the
	 user** – This option provides you with the password
	 details that you can manually send to the user from your email address.
