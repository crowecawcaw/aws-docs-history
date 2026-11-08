

# Contacting AWS Support with the AWS assistant
<a name="support"></a>

You can create an AWS Support case from anywhere in the AWS Management Console, including AWS Support Center. The AWS assistant uses the context of your conversation to draft the case and includes the recent conversation in the description. After you submit the case, you can transfer to a support agent using an available contact method, including live chat in the same panel.

You can create and transfer an AWS Support case through the AWS assistant only in the AWS Management Console. You can't use this feature at the Pro tier if your Amazon Q Developer profile is in the Europe (Frankfurt) Region.

Cases created through the AWS assistant also appear in AWS Support Center. Use AWS Support Center to track later updates.

All AWS accounts include account and billing support. Technical support through the AWS assistant requires a support offering above the Basic tier.

**Tip**  
Before creating a case, ask the AWS assistant to troubleshoot the problem or choose **Diagnose with AWS assistant** in the error message when it is available.

## Prerequisites
<a name="support-prerequisites"></a>
+ For technical support, the account has a support offering above the Basic tier.
+ You have permission to use the AWS assistant.
+ You have permission to create AWS Support cases. For more information, see [Managing access to AWS Support Center](https://docs.aws.amazon.com/awssupport/latest/user/accessing-support.html).

## Specify the right service
<a name="support-service"></a>

The AWS assistant selects a service based on your question. Correct the field before submission if it chooses the wrong service. For an issue with an assistant capability owned by another AWS service, select that service. For example, select Amazon Virtual Private Cloud (Amazon VPC) for an issue with network troubleshooting in Amazon VPC Reachability Analyzer. For an issue with the AWS assistant itself, create the case for the AWS assistant.

## Create a support case
<a name="create-support-case"></a>

**To create a support case**

1. In the AWS Management Console, open the AWS assistant chat panel.

1. Enter a request that includes relevant details, such as `I want to speak to someone` or `Get support`.

1. Review the drafted case. To change a field or attach a file, choose **Edit**. If the AWS assistant can't provide a value for a field, enter it manually.

1. Choose **Submit**.

1. Choose an available contact method, such as **Chat**, **Email**, or **Call**.

1. After the interaction, provide feedback or choose **Skip** to return to the AWS assistant.

To stop without creating the case, choose **Cancel** before you submit it.

You can also start a case from a response that didn't help. Choose the thumbs-down icon, select a reason, and choose **Create a support case**. Then continue from the review step.

For details about each contact method, see the following list:

****Chat****  
A support agent joins the conversation. To end the chat, choose **End this chat**. Keep the panel open during the chat. The chat ends if you refresh the page, navigate to a different console, or your console session expires. If you minimize the panel or navigate away from the page, you might miss notifications or be disconnected for inactivity.

****Email****  
An agent sends a message to the address associated with your AWS account.

****Call****  
Enter a phone number and submit it to join the call queue.