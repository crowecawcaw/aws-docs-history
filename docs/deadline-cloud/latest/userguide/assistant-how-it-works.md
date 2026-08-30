# How the assistant works

When you interact with the assistant, it uses Amazon Bedrock foundation models to
reason about your render job issues. The assistant has read-only access to your
Deadline Cloud resources and CloudWatch logs, and follows a structured
troubleshooting workflow:

1. Analyzes job configuration and lifecycle status
2. Identifies failed tasks and examines failure patterns
3. Retrieves session information and session action details
4. Analyzes CloudWatch logs for error patterns
5. Provides a root cause analysis with specific recommendations
   The assistant can also help with the following tasks:

- Summarizing logs on the current page
- Navigating to relevant resources in the monitor (workers, logs, tasks)
- Answering questions about Deadline Cloud concepts and terminology
- Troubleshooting renderer-specific issues
  All inference occurs within your AWS account using your own Amazon Bedrock service quotas.
  For more information, see [Amazon Bedrock quotas for the Deadline Cloud assistant](deadline-cloud-quotas.md#assistant-bedrock-quotas "deadline-cloud-quotas.md#assistant-bedrock-quotas"). Refreshing the page clears conversation
  history.
