# Creating a sending

authorization policy in Amazon SES

Similar to creating any authorization policy in Amazon SES, as explained in [Creating an identity
authorization policy](identity-authorization-policies-creating.md "identity-authorization-policies-creating.md"), to authorize a
delegate sender to send emails using an email address or domain (an
_identity_) that you own, you create the policy with SES
sending API actions specified, and then attach that policy to the identity.

For a list of API actions that can be specified in a sending authorization policy, see the
_Action_ row in the [Statements specific to
the policy](policy-anatomy.md#identity-authorization-policy-statements "policy-anatomy.md#identity-authorization-policy-statements")
table.

You can create a sending authorization policy by either using the policy generator or by
creating a custom policy. Procedures specific to creating a sending authorization policy are
provided for either method.

###### Note

- Sending authorization policies that you attach to email address identities
  take precedence over policies that you attach to their corresponding domain
  identities. For example, if you create a policy for
  _example.com_ that disallows a delegate sender, and you
  create a policy for *sender@example.com* that allows the
  delegate sender, then the delegate sender can send email from
  *sender@example.com*, but not from any other address on
  the _example.com_ domain.
- If you create a policy for _example.com_ that allows a
  delegate sender, and you create a policy for
  *sender@example.com* that disallows the delegate sender,
  then the delegate sender can send email from any address on the
  _example.com_ domain, except for
  *sender@example.com*.
- If you're unfamiliar with the structure of SES authorization policies,
  see [Policy anatomy](policy-anatomy.md "policy-anatomy.md").
- If the identity you're authorizing is duplicated in a secondary region as part
  of the [Global endpoints](global-endpoints.md "global-endpoints.md") feature, you'll need to
  create sending authorization policies on the identity in both the primary and
  secondary regions so that the delegate sender has permission to use this
  identity for sending in both regions.

## Creating a sending authorization policy by using the policy generator

You can use the policy generator to create a sending authorization policy by following
these steps.

###### To create a sending authorization policy by using the policy generator

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, under **Configuration**, choose
   **Identities**.
3. In the **Identities** container on the **Verified
   identities** screen, select the verified identity you wish to
   authorize for the delegate sender to send on your behalf.
4. Choose the verified identity's **Authorization** tab.
5. In the **Authorization policies** pane, choose
   **Create policy** and select **Use policy
   generator** from the dropdown.
6. In the **Create statement** pane, choose
   **Allow** in the **Effect** field. (If you
   want to create a policy to restrict your delegate sender, choose
   **Deny** instead.)
7. In the **Principals** field, enter the
   _AWS account ID_ or _IAM user ARN_
   that your delegate sender shared with you to authorize them to send email on
   behalf of your account for this identity, then choose **Add**.
   (If you wish to authorize more than one delegate sender, repeat this step for
   each one.)
8. In the **Actions** field, select the check box for each send
   type you would like to authorize for your delegate sender.
9. (Optional) Expand **Specify conditions** if you wish to add a
   qualifying statement to the delegate sender permission.
   1. Select an operator from the **Operator**
      dropdown.
   2. Select a type from the **Key** dropdown.
   3. Respective to the key type you selected, enter its value in the
      **Value** field. (If you wish to add more
      conditions, choose **Add new condition** and repeat
      this step for each additional one.)

10. Choose **Save statement**.
11. (Optional) Expand **Create another statement** if you wish to
    add more statements to your policy and repeat steps 6 - 10.
12. Choose **Next** and on the **Customize
    policy** screen, the **Edit policy details**
    container has fields where you can change or customize the policy’s
    **Name** and the **Policy document**
    itself.
13. Choose **Next** and on the **Review and
    apply** screen, the **Overview** container will
    show the verified identity you’re authorizing for your delegate sender as well
    as the name of this policy. In the **Policy document** pane
    will be the actual policy you just wrote along with any conditions you added -
    review the policy and if it looks correct, choose **Apply
    policy**. (If you need to change or correct something, choose
    **Previous** and work in the **Edit policy
    details** container.) The policy you just created will allow your
    delegate sender to send on your behalf.
14. (Optional) If your delegate sender also wants to use an SNS topic that they
    own, to receive feedback notifications when they receive bounces or complaints,
    or when emails are delivered, you’ll need to configure their SNS topic in this
    verified identity. (Your delegate sender will need to share with you their SNS
    topic ARN.) Select the **Notifications** tab
    and select **Edit** in the **Feedback
    notifications** container:
    1. On the **Configure SNS topics** pane, in any of the
       feedback fields, (Bounce, Complaint, or Delivery), select **SNS
       topic you don’t own** and enter the **SNS topic
       ARN** owned and shared with you by your delegate sender.
       (Only your delegate sender will get these notifications because they own
       the SNS topic - you, as the identity owner, will not.)
    2. (Optional) If you want your topic notification to include the headers
       from the original email, check the **Include original email
       headers** box directly underneath the SNS topic name of
       each feedback type. This option is only available if you've assigned an
       Amazon SNS topic to the associated notification type. For information
       about the contents of the original email headers, see the
       `mail` object in [Notification contents](notification-contents.md "notification-contents.md").
    3. Choose **Save changes**. The changes you made to your
       notification settings might take a few minutes to take effect.
    4. (Optional) Since your delegate sender will be getting Amazon SNS topic
       notifications for bounces and complaints, you can disable email
       notifications entirely if you don’t want to receive feedback for this
       identity’s sends. To disable email feedback for bounces and complaints,
       under the **Notifications** tab, in the **Email
       Feedback Forwarding** container, choose
       **Edit**, uncheck the **Enabled**
       box, and choose **Save changes**. Delivery status
       notifications will now only be sent to the SNS topics owned by your
       delegate sender.

## Creating a custom sending authorization policy

If you want to create a custom sending authorization policy and attach it to an
identity, you have the following options:

- Using the Amazon SES API – Create a policy in
  a text editor and then attach the policy to the identity by using the
  `PutIdentityPolicy` API described in the [Amazon Simple Email Service API Reference](../APIReference.md "../APIReference.md").
- Using the Amazon SES console – Create a policy
  in a text editor and attach it to an identity by pasting it into the custom
  policy editor in the Amazon SES console. The following procedure describes this
  method.

###### To create a custom sending authorization policy by using the custom policy

editor

1. Sign in to the AWS Management Console and open the Amazon SES console at [https://console.aws.amazon.com/ses/](https://console.aws.amazon.com/ses/ "https://console.aws.amazon.com/ses/").
2. In the navigation pane, under **Configuration**, choose
   **Identities**.
3. In the **Identities** container on the **Verified
   identities** screen, select the verified identity you wish to
   authorize for the delegate sender to send on your behalf.
4. In the details screen of the verified identity you selected in the previous
   step, choose the **Authorization** tab.
5. In the **Authorization policies** pane, choose
   **Create policy** and select **Create custom
   policy** from the dropdown.
6. In the **Policy document** pane, type or paste the text of
   your policy in JSON format. You can also use the policy generator to quickly
   create the basic structure of a policy and then customize it here.
7. Choose **Apply Policy**. (If you ever need to modify your
   custom policy, just select its check box under the
   **Authorization** tab, choose **Edit**,
   and make your changes in the **Policy document** pane followed
   by **Save changes**).
8. (Optional) If your delegate sender also wants to use an SNS topic that they
   own, to receive feedback notifications when they receive bounces or complaints,
   or when emails are delivered, you’ll need to configure their SNS topic in this
   verified identity. (Your delegate sender will need to share with you their SNS
   topic ARN.) Select the **Notifications** tab
   and select **Edit** in the **Feedback
   notifications** container:
   1. On the **Configure SNS topics** pane, in any of the
      feedback fields, (Bounce, Complaint, or Delivery), select **SNS
      topic you don’t own** and enter the **SNS topic
      ARN** owned and shared with you by your delegate sender.
      (Only your delegate sender will get these notifications because they own
      the SNS topic - you, as the identity owner, will not.)
   2. (Optional) If you want your topic notification to include the headers
      from the original email, check the **Include original email
      headers** box directly underneath the SNS topic name of
      each feedback type. This option is only available if you've assigned an
      Amazon SNS topic to the associated notification type. For information
      about the contents of the original email headers, see the
      `mail` object in [Notification contents](notification-contents.md "notification-contents.md").
   3. Choose **Save changes**. The changes you made to your
      notification settings might take a few minutes to take effect.
   4. (Optional) Since your delegate sender will be getting Amazon SNS topic
      notifications for bounces and complaints, you can disable email
      notifications entirely if you don’t want to receive feedback for this
      identity’s sends. To disable email feedback for bounces and complaints,
      under the **Notifications** tab, in the **Email
      Feedback Forwarding** container, choose
      **Edit**, uncheck the **Enabled**
      box, and choose **Save changes**. Delivery status
      notifications will now only be sent to the SNS topics owned by your
      delegate sender.
