**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# Creating an Amazon Pinpoint project with email

support

To send email with Amazon Pinpoint, you start by creating an Amazon Pinpoint project. When you create a
project, you can enable the email channel for it, and then choose the email identity that
you want to use as the sender address. If you haven't already verified an identity to use
with Amazon Pinpoint, you can verify an email address when you create the project.

In Amazon Pinpoint, an _identity_ is an email address or domain that you use to
send email. Before you can send email using Amazon Pinpoint, you must verify each identity that you
plan to use as a _From_, _Source_, _Sender_, or _Return path_ address to prove that you own the identity. For
more information about verifying identities, see [Verifying email identities](channels-email-manage-verify.md "channels-email-manage-verify.md").

###### Note

If your account is still in the Amazon Pinpoint email sandbox, you also need to verify the
identities that you plan to send email to. For more information about the email sandbox,
see [Increasing your sending
quotas](channels-email-manage-limits.md#channels-email-manage-limits-increase "channels-email-manage-limits.md#channels-email-manage-limits-increase").

If you have already created the project you can enable email by following the
directions at [Enabling and disabling the email channel](channels-email-enable.md "channels-email-enable.md").

###### Topics

- [Creating an email project
  when you haven't yet verified an identity](#channels-email-setup-create-not-verified "#channels-email-setup-create-not-verified")
- [Creating an email project
  when you've already verified an identity](#channels-email-setup-create-already-verified "#channels-email-setup-create-already-verified")

## Creating an email project

when you haven't yet verified an identity

If you haven't used Amazon Pinpoint to send email in the past, you probably haven't verified any
identities. The procedure in this section describes the process of creating a project
and verifying a single email address at the same time.

If you've already verified an identity, or if you want to verify an entire domain
instead of a single address, use the procedures in [Verifying a domain](channels-email-manage-verify.md#channels-email-manage-verify-domain "channels-email-manage-verify.md#channels-email-manage-verify-domain") instead.

###### To create a new email project and verify an email address

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose **Create a
   project**.
3. For **Project name**, enter a name, and then choose
   **Create**.

###### Note

The project name can contain up to 64 alphanumeric characters. It can also
include the following characters: comma (,), period (.), at sign (@),
underscore (\_), equals sign (=), and plus sign (+). 4. On the **Configure features** page, under
**Email**, choose **Configure**. 5. On the **Set up email** page, for **Email
address**, enter the email address that you want to use to send
email from this project. Amazon Pinpoint sends an email to the address that you entered.
Open the email, and then click the link in the message to verify the email
address.

## Creating an email project

when you've already verified an identity

If you've already verified an email identity, you can use that identity with your new
project.

###### To create a new email project and choose an existing identity

1. Open the Amazon Pinpoint console at
   [https://console.aws.amazon.com/pinpoint/](https://console.aws.amazon.com/pinpoint/ "https://console.aws.amazon.com/pinpoint/").
2. On the **All projects** page, choose **Create a
   project**.
3. For **Project name**, enter a name, and then choose
   **Create**.

###### Note

The project name can contain up to 64 alphanumeric characters. It can also
include the following characters: comma (,), period (.), at sign (@),
underscore (\_), equals sign (=), and plus sign (+). 4. On the **Configure features** page, choose **Skip
this step**. 5. In the navigation pane, under **Settings**, choose
**Email**. 6. Next to **Identity details**, choose
**Edit**. 7. Choose **Enable the email channel for this project**. 8. For **Identity type**, choose either **Email
address** or **Domain**, depending on the type of
verified identity that you want to use. 9. Choose **Use an existing email address** if you chose
**Email address** in the preceding step, or choose
**Use an existing domain** if you chose
**Domain**. 10. From the list, choose the verified email address or domain that you want to
use. 11. If you're setting up a domain, specify the **Default sender
address** for that domain. 12. (Optional) For **Friendly sender name**, enter the name that
you want to appear in your recipients' email clients. 13. When you finish, choose **Save**.
