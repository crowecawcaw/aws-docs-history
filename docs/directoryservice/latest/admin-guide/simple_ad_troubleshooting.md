# Troubleshooting Simple AD

The following can help you troubleshoot some common problems you might encounter when
creating or using your Simple AD Active Directory.

###### Topics

- [Password recovery](#simple_ad_tshoot_password_recovery "#simple_ad_tshoot_password_recovery")
- [I receive a 'KDC can't fulfill requested option'
  error when adding a user to Simple AD](#kdc_requested_option "#kdc_requested_option")
- [I am not able to update the DNS name or IP address
  of an instance joined to my domain (DNS dynamic update)](#dns_dynamic_updates "#dns_dynamic_updates")
- [I can't log onto SQL Server using a SQL Server
  account](#sql_login_fail "#sql_login_fail")
- [My Simple AD is stuck in the 'Requested'
  state](#stuck_in_requested1 "#stuck_in_requested1")
- [I receive an 'AZ constrained' error when I create a
  Simple AD](#contrained_az1 "#contrained_az1")
- [Some of my users can't authenticate with my Simple AD](#kerberos_preauth1 "#kerberos_preauth1")
- [Additional resources](#troubleshoot_general_resources "#troubleshoot_general_resources")
- [Troubleshooting Simple AD directory
  status messages](simple_ad_troubleshooting_reasons.md "simple_ad_troubleshooting_reasons.md")

## Password recovery

If a user forgets a password or is having trouble signing in to your
Simple AD directory, you can reset their password using either the
AWS Management Console, PowerShell or the AWS CLI.

For more information, see [Resetting a Simple AD user
password](simple_ad_manage_users_groups_reset_password.md "simple_ad_manage_users_groups_reset_password.md").

## I receive a 'KDC can't fulfill requested option'

error when adding a user to Simple AD

This can occur when the Samba CLI client does not correctly send the `net` commands to
all domain controllers. If you see this error message when using the `net ads` command
to add a user to your Simple AD directory, use the `-S` argument and specify the IP
address of one of your domain controllers. If you still see the error, try the other
domain controller. You can also use the Active Directory Administration Tools to add
users to your directory. For more information, see [Installing the Active Directory Administration
Tools for Simple AD](simple_ad_install_ad_tools.md "simple_ad_install_ad_tools.md").

## I am not able to update the DNS name or IP address

of an instance joined to my domain (DNS dynamic update)

DNS dynamic updates are not supported in Simple AD domains. You can instead make the
changes directly by connecting to your directory using DNS Manager on an instance that
is joined to your domain.

## I can't log onto SQL Server using a SQL Server

account

You might receive an error if you attempt to use SQL Server Management Studio (SSMS)
with a SQL Server account to log into SQL Server running on a Windows 2012 R2 Amazon EC2
instance. The issue occurs when SSMS runs as a domain user and can result in the error
`Login failed for user`, even when valid credentials are provided. This is a known issue
and AWS is actively working to resolve it.

To work around the issue, you can log into SQL Server with Windows Authentication
instead of SQL Authentication. Or launch SSMS as a local user instead of a Simple AD
domain user.

## My Simple AD is stuck in the 'Requested'

state

If you have a Simple AD that has been in the `Requested` state for more than five
minutes, try deleting the directory and recreating it. If this problem persists, contact
the [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## I receive an 'AZ constrained' error when I create a

Simple AD

Some AWS accounts created before 2012 might have access to Availability Zones in the
US East (N. Virginia), US West (N. California), or Asia Pacific (Tokyo) Region that do not
support Directory Service directories. If you receive an error such as this when creating a
directory, choose a subnet in a different Availability Zone and try to create the
directory again.

## Some of my users can't authenticate with my Simple AD

Your user accounts must have Kerberos preauthentication enabled. This is the default
setting for new user accounts, and it should not be modified. For more information about
this setting, go to [Preauthentication](http://technet.microsoft.com/en-us/library/cc961961.aspx "http://technet.microsoft.com/en-us/library/cc961961.aspx") on Simple AD TechNet.

## Additional resources

The following resources can help you troubleshoot as you work with AWS.

- **[AWS Knowledge
  Center](https://aws.amazon.com/premiumsupport/knowledge-center/ "https://aws.amazon.com/premiumsupport/knowledge-center/")**–Find FAQs and links to other resources to
  help you troubleshoot issues.
- **[AWS Support
  Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/")**–Get technical support.
- **[AWS Premium Support
  Center](https://aws.amazon.com/premiumsupport/ "https://aws.amazon.com/premiumsupport/")**–Get premium technical support.

###### Topics

- [Troubleshooting Simple AD directory
  status messages](simple_ad_troubleshooting_reasons.md "simple_ad_troubleshooting_reasons.md")
