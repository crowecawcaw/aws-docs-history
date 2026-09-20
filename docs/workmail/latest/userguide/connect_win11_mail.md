

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Setting up the Windows 11 Mail app for Amazon WorkMail
<a name="connect_win11_mail"></a>

If you have the Mail app for Microsoft Windows 11, you can add your Amazon WorkMail account.

**Note**  
If you are using the Mail app for Microsoft Windows 11, you may receive incompatibility reports that require a fix when connecting your Amazon WorkMail account to the app. Until a fix is released by Microsoft, you will not be able to connect the Mail app to WorkMail. To ensure that you can resolve the issue as soon as a fix is released, make sure that you install Windows 11 updates as they become available.

**To connect your Amazon WorkMail account to your Mail app**

1. In Windows 11, open the Mail app, and then choose **Accounts**.

1. Choose **Add Account**, and then choose **Advanced Setup**.

1. Choose **Internet email**, and then provide the following information:


<table>
<thead>
  <tr><th>Required Information</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Email address</b></td><td>Email address associated with your Amazon WorkMail account</td></tr>
  <tr><td><b>Password</b></td><td>Your password</td></tr>
  <tr><td><b>User name</b></td><td>Email address associated with your Amazon WorkMail account</td></tr>
  <tr><td><b>Account name</b></td><td>Your account name</td></tr>
  <tr><td><b>Send your message using this name</b></td><td>Your account name</td></tr>
  <tr><td><b>Incoming email server</b></td><td>The endpoint matching the AWS Region in which your mailbox is located:<ul><li> US West (Oregon) <br />imap.mail.us-west-2.awsapps.com </li><li> US East (N. Virginia) <br />imap.mail.us-east-1.awsapps.com </li><li> Europe (Ireland) <br />imap.mail.eu-west-1.awsapps.com  If you don't know the AWS Region where your mailbox is located, contact your system administrator.  </li></ul></td></tr>
  <tr><td><b>Account type</b></td><td>IMAP4</td></tr>
  <tr><td><b>Outgoing (SMTP) email server</b></td><td>The endpoint matching the AWS Region where your mailbox is located:<ul><li> US West (Oregon) <br />smtp.mail.us-west-2.awsapps.com </li><li> US East (N. Virginia) <br />smtp.mail.us-east-1.awsapps.com </li><li> Europe (Ireland) <br />smtp.mail.eu-west-1.awsapps.com  If you don't know the AWS Region where your mailbox is located, contact your system administrator.  </li></ul></td></tr>
</tbody>
</table>


1. Choose **Sign in**.