

End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the Amazon WorkMail console or Amazon WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html). 

# Setting up IMAP for Amazon WorkMail
<a name="using_IMAP"></a>

You can connect any IMAP-compatible software to Amazon WorkMail by providing the following information.

**Note**  
If you are using the web application, Microsoft Outlook, an Android or iOS mobile device, or a mail app for Windows 10 or macOS, see [Setting up email clients for Amazon WorkMail](clients.md) for specific guidelines that apply to those applications. The following information is intended for use with all other IMAP-compatible clients.


| Required Information | Description | 
| --- | --- | 
| **Type of account** | IMAP | 
| **Protocol** | IMAPS | 
| **Port** | 993 | 
| **Secure connection** | Select **Required** and **SSL** | 
| **Type of authentication** | PLAIN | 
| **Incoming username** | Email address associated with your Amazon WorkMail account | 
| **Incoming password** | Your password | 
| **Incoming server** | The endpoint matching the AWS Region where your mailbox is located:+  US West (Oregon) <br />imap.mail.us-west-2.awsapps.com <br />+  US East (N. Virginia) <br />imap.mail.us-east-1.awsapps.com <br />+  Europe (Ireland) <br />imap.mail.eu-west-1.awsapps.com  If you don't know the AWS Region where your mailbox is located, contact your system administrator.  | 

To send email, you also need to configure an outgoing SMTP server in your IMAP-compatible software. 


| Required Information | Description | 
| --- | --- | 
| **Protocol** | SMTPS (SMTP, encrypted with TLS) | 
| **Port** | 465 | 
| **Secure connection** | Select **Required** and **SSL** **STARTTLS** is not currently supported by Amazon WorkMail  | 
| **Outgoing username** | Email address associated with your Amazon WorkMail account | 
| **Outgoing password** | Your password | 
| **Outgoing server** | The endpoint matching the AWS Region where your mailbox is located:+  US West (Oregon) <br />smtp.mail.us-west-2.awsapps.com <br />+  US East (N. Virginia) <br />smtp.mail.us-east-1.awsapps.com <br />+  Europe (Ireland) <br />smtp.mail.eu-west-1.awsapps.com  If you don't know the AWS Region where your mailbox is located, contact your system administrator.  | 