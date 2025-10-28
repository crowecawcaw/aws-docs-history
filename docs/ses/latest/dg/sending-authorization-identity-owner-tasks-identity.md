# Providing the delegate

sender with the identity information for Amazon SES sending authorization

After you create your sending authorization policy and attach it to your identity, you can
provide the delegate sender with the Amazon Resource Name (ARN) of the identity. The
delegate sender will pass that ARN to Amazon SES in the email-sending operation or in the header
of the email. To find your identity's ARN, follow these steps.

###### To find the ARN of an identity

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, under **Configuration**, choose
   **Verified identities**.
3. In the list of identities, choose the identity to which you attached the sending
   authorization policy.
4. In the **Summary** pane, the second column, **Amazon
   Resource Name (ARN)**, will contain the identity's ARN. It will look
   similar to
   _arn:aws:ses:us-east-1:123456789012:identity/user@example.com_.
   Copy the entire ARN and give it to your delegate sender.

###### Important

If the identity you're authorizing is duplicated in a secondary region as part
of the [Global endpoints](global-endpoints.md "global-endpoints.md") feature, replace the region
parameter, such as, `us-east-1`, with an asterisk `*` as
in the following example,
`arn:aws:ses:*:123456789012:identity/user@example.com`.
