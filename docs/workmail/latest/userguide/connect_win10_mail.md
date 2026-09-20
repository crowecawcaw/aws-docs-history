

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Setting up the Windows 10 Mail app for Amazon WorkMail
<a name="connect_win10_mail"></a>

If you have the Mail app for Microsoft Windows 10, you can add your Amazon WorkMail account.

**To connect your Amazon WorkMail account to your Mail app**

1. In Windows 10, open the Mail app, and then choose **Accounts**.

1. Choose **Add Account**, and then choose **Advanced Setup**.

1. Choose **Exchange ActiveSync**, and then provide the following information.


<table>
<thead>
  <tr><th>Required Information</th><th>Description</th></tr>
</thead>
<tbody>
  <tr><td><b>Email address</b></td><td>Email address associated with your Amazon WorkMail account</td></tr>
  <tr><td><b>Password</b></td><td>Your password</td></tr>
  <tr><td><b>User name</b></td><td>Email address associated with your Amazon WorkMail account</td></tr>
  <tr><td><b>Domain</b></td><td>Leave this field empty</td></tr>
  <tr><td><b>Server</b></td><td>The endpoint matching the AWS Region in which your mailbox is located:<ul><li> US West (Oregon) <br />mobile.mail.us-west-2.awsapps.com </li><li> US East (N. Virginia) <br />mobile.mail.us-east-1.awsapps.com </li><li> Europe (Ireland) <br />mobile.mail.eu-west-1.awsapps.com </li></ul> If you don't know the AWS Region where your mailbox is located, contact your system administrator. </td></tr>
  <tr><td><b>Server requires encrypted (SSL) connection</b></td><td>Select <b>Enabled</b></td></tr>
  <tr><td><b>Account name</b></td><td>Your account name</td></tr>
</tbody>
</table>


1. Choose **Sign in**.