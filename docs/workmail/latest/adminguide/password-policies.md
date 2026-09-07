

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Troubleshooting Amazon WorkMail password policies
<a name="password-policies"></a>

If resetting the password is unsuccessful, verify that the new password meets the password policy requirements.

The password policy requirements depend on which directory type your Amazon WorkMail organization uses.

**Amazon WorkMail directory and Simple AD directory password policy**  
By default, passwords for an Amazon WorkMail directory or Simple AD directory must be:


+ Non-empty
+ At least eight characters
+ Less than 64 characters
+ Composed of Basic Latin or Latin-1 supplement characters

Passwords must also contain characters from three out of five of the following groups:
+ Uppercase characters
+ Lowercase characters
+ Numerical digits (0 through 9)
+ Special characters (for example, <, \~, or \!)
+ Latin-1 supplement characters (for example, é, ü, or ñ)

Amazon WorkMail directory password policies can't be changed.

To change a Simple AD password policy, use the AD administration tools on an Amazon Elastic Compute Cloud (Amazon EC2) Windows instance of your Simple AD directory. For more information, see [Installing the Active Directory administration tools](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/simple_ad_install_ad_tools.html) in the *AWS Directory Service Administration Guide*.

**AWS Managed Microsoft AD Directory password policy**  
For information about the default password policy for an AWS Managed Microsoft AD directory, see [Manage Password Policies for AWS Managed Microsoft AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_password_policies.html) in the *AWS Directory Service Administration Guide*.

**AD Connector password policy**  
AD Connector uses the password policy of the Active Directory domain that it is connected to. See the documentation for your Active Directory domain for more information on password policy settings.