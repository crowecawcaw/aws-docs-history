

# Changing your email address for an organization with AWS Organizations
<a name="about-email-verification-change-email"></a>

To change the email address that is associated with your management account, see [Update the AWS account name, email address, or password for the root user](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html) in the *AWS Account Management Reference Guide*.

If you change the email address of the management account, the account's status reverts to "email unverified," and you must complete the verification process for your new email address. 

**Note**  
If you invited accounts to join your organization before you have changed the management account's email address, and those invitations have not yet been accepted, they can’t be accepted until you verify the management account’s new email address. You must first [resend the verification request](about-email-verification-resend.md). After you have completed the process by responding to the email, accounts you have invited can accept the invitations.