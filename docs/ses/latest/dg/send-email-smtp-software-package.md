

# Sending email through Amazon SES using software packages

There are a number of commercial and open source software packages that support sending email through SMTP. Here are some examples:
+ Blogging platforms
+ RSS aggregators
+ List management software
+ Workflow systems

You can configure SMTP-enabled software to send email through Amazon SES. Get the endpoint, user name, and password from [Creating SMTP credentials using Mail Manager](smtp-credentials-mail-manager.md) or [Obtaining Amazon SES SMTP credentials using IAM](smtp-credentials.md). For instructions that are specific to your software, see its documentation.

**Important**  
Do not use your AWS access key ID and secret access key as SMTP credentials. For more information, see [Types of Amazon SES credentials](send-email-concepts-credentials.md).

The following procedure shows how to set up Amazon SES sending in JIRA, a popular issue-tracking solution. With this configuration, JIRA can notify users through email whenever there is a change in the status of a software issue.

**To configure JIRA to send email using Amazon SES**

1. Using your web browser, log in to JIRA with administrator credentials.

1. In the browser window, choose **Administration**.

1. On the **System** menu, choose **Mail**.

1. On the **Mail administration** page, choose **Mail Servers**.

1. Choose **Configure new SMTP mail server**.

1. On the **Add SMTP Mail Server** form, fill in the following fields:

   1. **Name**—A descriptive name for this server.

   1. **From address**—The address from which email will be sent. You must verify this email address with Amazon SES before you can send from it. For more information about verification, see [Verified identities in Amazon SES](verify-addresses-and-domains.md).

   1. **Email prefix**—A string that JIRA prepends to each subject line prior to sending.

   1. **Protocol**—Choose **SMTP**.

   1. **Hostname**—Enter the endpoint from your SMTP credentials.

   1. **SMTP port**—Enter `25` or `587`.
**Note**  
Amazon Elastic Compute Cloud (Amazon EC2) restricts outbound email traffic over port `25` by default. Use port `587` from Amazon EC2 unless you have removed the restriction.

   1. **TLS**—Select this check box.

   1. **User name**—Enter the user name from your SMTP credentials.

   1. **Password**—Enter the password from your SMTP credentials.
**Credentials using IAM**  
If JIRA cannot connect with SMTP and STARTTLS, you can select **SECURE\_SMTP**. Use TLS Wrapper on port `465` or `2465`. This option does not apply to Mail Manager SMTP.

   For credentials using IAM, the following image shows the JIRA settings for TLS Wrapper.  
![JIRA TLS Wrapper configuration for credentials using IAM](https://docs.aws.amazon.com/ses/latest/dg/images/SMTP_jira.png)

1. Choose **Test Connection**. If the test email that JIRA sends through Amazon SES arrives successfully, then your configuration is complete.