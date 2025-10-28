# Request production access (Moving out of the

Amazon SES sandbox)

To help prevent fraud and abuse, and to help protect your reputation as a sender, we apply
certain restrictions to new Amazon SES accounts.

We place all new accounts in the Amazon SES _sandbox_. The sandbox status
for your account is unique per each AWS Region. While your account is in the sandbox, you
can use all of the features of Amazon SES. However, when your account is in the sandbox, we apply
the following restrictions to your account:

- You can only send mail **to** verified email
  addresses and domains, or to [the Amazon SES mailbox
  simulator](send-an-email-from-console.md#send-email-simulator "send-an-email-from-console.md#send-email-simulator").
- You can send a maximum of 200 messages per 24-hour period.
- You can send a maximum of 1 message per second.
- For sending authorization, neither you nor the delegate sender can send email to
  non-verified email addresses.
- For account-level suppression, bulk actions and SES API calls related to
  suppression list management are disabled.
  When your account has moved out of the sandbox and into production, you can send email to
  any recipient, regardless of whether the recipient's address or domain is verified. However,
  you still have to verify all identities that you use as "From", "Source", "Sender", or
  "Return-Path" addresses.

Complete the procedures in this section to request that your account be removed from the
sandbox and placed into production.

###### Tip

- If you’re a new customer and haven’t created any identities yet, then the
  SES account set up wizard in the console will be enabled to help you get
  started. See [Set up your SES
  account](setting-up.md#quick-start-verify-email-addresses "setting-up.md#quick-start-verify-email-addresses") for instructions on how to access the wizard.
- If you’ve already created one or more identities, you’ll see the **Get
  set up** page instead of the account set up wizard.
  - If one of your identities is a verified domain, you’ll be able to
    request production access directly from the **Get set
    up** page as well. This is because verifying your domain
    with SES before requesting production access is a best practice
    that helps to get your production access request approved faster so you
    can start sending email right away.

###### Note

- If you're using Amazon SES to send email from an Amazon EC2 instance, you might also
  need to request that the throttle be removed from port 25 on your Amazon EC2
  instance. For more information, see [How do I remove the throttle on port 25 from my EC2 instance?](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/ "https://aws.amazon.com/premiumsupport/knowledge-center/ec2-port-25-throttle/") in
  the AWS Knowledge Center.

###### To request production access (remove your account from the sandbox) using the

AWS Management Console

1. Open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation panel, choose **Account
   dashboard**.
3. In the warning box at the top of the console that says, "Your Amazon SES account
   is in the sandbox", on the right-hand side, choose **View Get set up
   page** followed by **Request production
   access**.
4. In the account details modal, select either the **Marketing** or
   **Transactional** radio button that best describes the majority
   of mail you'll be sending.
   - _Marketing email_ - Sent on a one-to-many basis to a
     targeted list of prospects or customers containing marketing and promotional
     content such as to make a purchase, download information, etc.
   - _Transactional email_ - Sent on a one-to-one basis
     unique to each recipient usually triggered by a user action such as a
     website purchase, a password reset request, etc.

5. In **Website URL**, enter the URL of your website to help us
   better understand the kind of content you plan on sending.
6. In **Additional contacts**, tell us where you want to receive
   communications about your account. This can be a comma-separated list of up to 4
   email addresses.
7. In **Preferred contact language**, choose whether you want to
   receive communications in **English** or
   **Japanese**.
8. In **Acknowledgement**, check the box that you agree to only send
   email to individuals who've explicitly requested it and confirm that you have a
   process in place for handling bounce and complaint notifications.
9. Choose the **Submit request** button - a banner will display to
   confirm your request was submitted and is currently under review.
   Once you submit a review of your account details, you can’t edit your details until the
   review is complete. The AWS Support team provides an initial response to your request within
   24 hours.

In order to prevent our systems from being used to send unsolicited or malicious content,
we have to consider each request carefully. If we're able to do so, we'll grant your request
within this 24-hour period. However, if we need to obtain additional information from you,
it might take longer to resolve your request.

Optionally, you can also submit your request for production access using the AWS CLI.
Submitting your request using the AWS CLI is helpful when you want to request production
access for a large number of identities, or when you want to automate the process of setting
up Amazon SES.

###### To request that your account be removed from the Amazon SES sandbox using the

AWS CLI

1. **Prerequisite**: you have to install and configure the AWS CLI.
   For more information, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").
2. At the command line, enter the following command:

```
aws sesv2 put-account-details \
--production-access-enabled \
--mail-type `TRANSACTIONAL` \
--website-url `https://example.com` \
--additional-contact-email-addresses `info@example.com` \
--contact-language `EN`
```

In the preceding command, do the following:

    1. Replace `TRANSACTIONAL` with the type of email
     that you plan to send through Amazon SES. You can specify either
     `TRANSACTIONAL` or `MARKETING`. If more than one
     value applies, specify the option that applies to the majority of the email
     that you plan to send.
    2. Replace `https://example.com` with the URL of
     your website. Providing this information helps us better understand the type
     of content that you plan to send.
    3. Replace `info@example.com` with the email
     addresses where you want to receive communications about your account. This
     can be a comma-separated list of up to 4 email addresses.
    4. Replace `EN` with your preferred language. You
     can specify `EN` for English or `JA` for
     Japanese.

Once you submit a review of your account details, you can’t edit your details until the
review is complete. The AWS Support team provides an initial response to your request within
24 hours.

In order to prevent our systems from being used to send unsolicited or malicious content,
we have to consider each request carefully. If we're able to do so, we'll grant your request
within this 24-hour period. However, if we need to obtain additional information from you,
it might take longer to resolve your request.
