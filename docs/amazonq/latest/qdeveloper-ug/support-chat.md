# Using Amazon Q Developer to chat with Support

You can use Amazon Q Developer to create a support case and contact Support from anywhere in the
AWS Management Console, including the AWS Support Center Console. Amazon Q uses the context of your conversation to
draft a support case on your behalf automatically. It also adds your recent conversation to
the support case description. After creating the case, Amazon Q can transfer you to a support
agent in the method of your choice, including live chat in the same interface.

When you create a support case in Amazon Q, the case is also updated in the Support Center Console.
To track updates on cases created with Amazon Q, use the Support Center Console.

The type of Support available to you depends on the support plan for your AWS account. All
AWS users have access to account and billing support as part of the Basic Support plan. For
technical support questions, only users with support plans other than the Basic Support plan
can contact Support with Amazon Q. For more information about AWS Support, see [Getting started with
AWS Support](../../../awssupport/latest/user/getting-started.md "../../../awssupport/latest/user/getting-started.md") in the _AWS Support User Guide_.

###### Tip

Before you create a support ticket, try asking Amazon Q to resolve the issue. For more
information, see [Asking Amazon Q to troubleshoot your resources](chat-actions-troubleshooting.md "chat-actions-troubleshooting.md"). You can also try the **Diagnose
with Amazon Q** button, if it's available. For more information, see [Diagnosing console errors](diagnose-console-errors.md "diagnose-console-errors.md").

## Prerequisites

To create cases in Amazon Q, you must meet the following requirements:

- You have a support plan higher than the Basic Support plan. Only users with
  support plans other than the Basic Support plan can contact Support with Amazon Q.
- You have permissions to chat with Amazon Q. For more information, see [Allow users to chat with Amazon Q](id-based-policy-examples-users.md#id-based-policy-examples-allow-chat "id-based-policy-examples-users.md#id-based-policy-examples-allow-chat").
- You have permissions to create Support cases. For more information, see [Manage
  access to Support Center](../../../awssupport/latest/user/accessing-support.md "../../../awssupport/latest/user/accessing-support.md").

## Specify the right service

When you create a support case with Amazon Q, it populates the service field based on your
question. If Amazon Q chooses the wrong service, update the case with the correct service. If
your question has to do with multiple services, specify the service that's most
applicable.

To contact Support about an Amazon Q feature that is part of another AWS service, create a
support case for the other AWS service, not for Amazon Q. For example, if you're using
Amazon Q network troubleshooting in Amazon VPC Reachability Analyzer, choose Amazon VPC for the service in the support
case.

To contact Support about features in either Amazon Q Developer or Amazon Q Business, create a support case
for Amazon Q.

## Create a support case

To create an Support case with Amazon Q, use the following steps.

1. You can create an Support case through Amazon Q in one of two ways:
   1. Ask for help directly by entering a question such as “I want to speak to
      someone” or “Get support”.

   To provide more context for Amazon Q to create the support case, you can add
   more information when requesting support directly. Following is an example of
   providing more information in a request:

   "I am unable to connect to my bastion instance. I have tried restarting it
   and generating new key pairs but still nothing works. This started this morning
   after a planned deployment. I can confirm that no other network related changes
   were made. Can I talk to someone?" 2. If an Amazon Q response didn’t help you, choose the thumbs-down icon on the
   response and then choose a reason that you're providing the feedback. To
   contact Support, choose **Create a support
   case**.

   The following image shows the **Create a support
   case** button in the Amazon Q chat panel that appears after you leave
   feedback.

   ![The Create a support case button in the Amazon Q chat panel.](images/support-feedback.png)

2. A support case appears in the chat panel. If you had a conversation with Amazon Q
   before requesting support, it will use the context of your conversation to
   autopopulate the fields in the case. To update any field in the support case, choose
   **Edit**. You can also attach files that help explain your issue.

If you didn't chat with Amazon Q before requesting support or Amazon Q otherwise can’t
complete the fields in the support case, you can input your support case information
into the case manually.

The following image is an example of a filled-out support case in the Amazon Q chat
panel.

![A filled-out support case in an Amazon Q chat panel.](images/support-edit.png) 3. After confirming that the support case describes your needs, choose
**Submit** to create the support case. If you no longer want to
create the case, choose **Cancel**. 4. To contact Support, choose the method that you want to use. Depending on your case
details, you can chat, email, or request a phone call from a live support agent:

    1. **Chat** – If you choose to chat with an
     agent, a live support agent will enter the conversation. To end the chat with
     the support agent, choose **End this chat** at any time during
     the chat.


    If you refresh your page, navigate to a different console, or get signed out
     of the console because of session expiration, the conversation will end.


    If you minimize the chat panel or leave the page, you might miss
     notifications and be disconnected because of inactivity. We recommend that you
     keep the chat panel open throughout the duration of your support chat.
    2. **Email** – If you choose to send an
     email message to an agent, a support agent will contact you at the email
     address that's associated with your AWS account.
    3. **Call** – If you choose to call an
     agent, enter your phone number when prompted, and choose
     **Submit**. You will be added to the call queue.

5. You can leave feedback or choose **Skip** to return to the Amazon Q
   chat panel.

## Leave feedback

After the support chat has ended, you can optionally leave feedback.

Rate your experience, enter any additional feedback, and then choose **Submit
feedback**.
