

# Troubleshoot with AI while you wait for a support agent
<a name="ai-troubleshooting-after-case-creation"></a>

If you have an AWS Business Support\+, AWS Enterprise Support, or AWS Unified Operations plan, AI-enhanced troubleshooting continues after you create a support case. You can keep working toward a resolution while you wait for a support agent to be assigned to your case. This feature isn't available with the Basic Support plan.

Troubleshooting with AI doesn't change how long it takes for a support agent to be assigned to your case, or the response times for your support plan. When a support agent is assigned, they can see your full troubleshooting history, so that their first response can build on what you've already tried.

Troubleshooting with AI starts automatically after you submit your case. You can choose whether to interact with it. If you don't, your case isn't affected.

This feature uses the same IAM permissions as AI-enhanced troubleshooting. For more information, see [Set up permissions to use AI-enhanced troubleshooting](support-interaction-perm.md). To turn off this feature, deny the AI-enhanced troubleshooting operations. For more information, see [Denying AI-enhanced troubleshooting operations](support-interaction-deny-ai-operations.md).

**To troubleshoot with AI while you wait for a support agent**

1. Create a support case from a support interaction. For more information, see [Create a support case from a support interaction](create-support-case-from-interaction.md).

1. After you submit your case, AI-enhanced troubleshooting starts automatically. The **Troubleshooting your issue** section shows the progress of the analysis, such as **Understanding your request** and **Working on a solution**.

1. Review the troubleshooting recommendations.
**Note**  
Responses are generated using AWS generative AI capabilities. Verify responses for accuracy. For more information, see the [AWS Responsible AI Policy](https://aws.amazon.com/ai/responsible-ai/policy/).

1. (Optional) To continue troubleshooting, enter more details or follow-up questions in the text field, and then choose the **Send** icon. You can enter up to 8,000 characters.

When a support agent is assigned to your case, AI-enhanced troubleshooting ends for that case, and you can no longer use it in that case. You can continue to communicate with the support agent in your case correspondence.