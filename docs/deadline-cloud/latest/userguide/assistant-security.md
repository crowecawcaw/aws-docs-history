

# Security
<a name="assistant-security"></a>

The Deadline Cloud assistant operates within the existing Deadline Cloud security model:
+ **Read-only access** – The assistant only performs read operations (Get, List, Search) on Deadline Cloud resources and CloudWatch logs. It cannot modify your resources.
+ **Customer-account execution** – All Amazon Bedrock model invocations occur in your AWS account using your credentials and service quotas.
+ **Scoped permissions** – The Amazon Bedrock policy is scoped to cross-region inference profiles for your geographic region. Monitor users cannot access Amazon Bedrock actions beyond `InvokeModelWithResponseStream`.
+ **Session isolation** – Conversations are isolated to individual browser sessions and are not persisted or shared.
+ **Fail closed** – If the assistant cannot determine whether it is enabled (for example, if the `GetMonitorSettings` call fails), the assistant UI is not displayed.
+ **Admin control** – Only administrators can enable or disable the assistant. Monitor users cannot self-escalate access.
+ **Abuse detection** – Amazon Bedrock abuse detection capabilities apply to assistant usage. For more information, see [Abuse detection](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html) in the *Amazon Bedrock User Guide*.

## Model information
<a name="assistant-model-information"></a>

The Deadline Cloud assistant uses Anthropic Claude Sonnet 4.5 (`anthropic.claude-sonnet-4-5-20250929-v1:0`) as its foundation model, accessed through Amazon Bedrock cross-region inference profiles. The assistant also includes a knowledge base built from public Deadline Cloud documentation, public AWS documentation, and public documentation for popular digital content creation applications. This knowledge base is fetched by the assistant at invocation time. AWS did not use customer data from any Deadline Cloud account to build or fine-tune the assistant.

## Data privacy
<a name="assistant-data-privacy"></a>

The Deadline Cloud assistant is subject to the Amazon Bedrock data protection policies. For more information about Amazon Bedrock data protection, see [Data protection](https://docs.aws.amazon.com/bedrock/latest/userguide/data-protection.html) in the *Amazon Bedrock User Guide*.

The assistant holds conversation history in browser memory only. Refreshing or closing the page permanently deletes the conversation. The assistant doesn't persist any conversation data to disk, databases, or AWS services.

If you have Amazon Bedrock model invocation logging enabled in your account, your assistant conversations (including log content sent to the model) are captured in your configured logging destination (your Amazon S3 bucket or CloudWatch Logs log group). Model invocation logging is disabled by default and is entirely under your control. For more information, see [Model invocation logging](https://docs.aws.amazon.com/bedrock/latest/userguide/model-invocation-logging.html) in the *Amazon Bedrock User Guide*.

## Network path
<a name="assistant-network-path"></a>

The Deadline Cloud assistant runs in your browser as part of the Deadline Cloud monitor application. When you interact with the assistant, your browser makes Amazon Bedrock API calls (`InvokeModelWithResponseStream`) directly to the Amazon Bedrock service endpoint by using your monitor user credentials. These calls travel over HTTPS (TLS 1.2 or higher) to the public Amazon Bedrock endpoint in your Region.

Because the assistant runs in the browser, Amazon VPC interface endpoints (AWS PrivateLink) do not apply to assistant traffic. Amazon Bedrock PrivateLink support is designed for server-side workloads running within your Amazon VPC, not browser-based applications.

## Organization-level controls
<a name="assistant-org-level-controls"></a>

In addition to the per-monitor admin toggle, you can enforce organization-wide control over the assistant by using AWS Organizations (Organizations) service control policies (SCPs). An SCP that denies `bedrock:InvokeModelWithResponseStream` prevents the assistant from functioning, even if a monitor administrator enables the feature.

The following example SCP denies all Amazon Bedrock model invocations, which disables the assistant across all accounts in the organization or organizational unit (OU) where the policy is attached:

```
{
    "Version": "2012-10-17", 		 	 	 
    "Statement": [
        {
            "Sid": "DenyBedrockInvocations",
            "Effect": "Deny",
            "Action": "bedrock:InvokeModelWithResponseStream",
            "Resource": "*"
        }
    ]
}
```

For more information about SCPs, see [Service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) in the *Organizations User Guide*.

**Note**  
This SCP blocks all Amazon Bedrock model invocations in the affected accounts, including those not related to Deadline Cloud. To block only the assistant, disable it through the monitor settings instead.

## Audit trail
<a name="assistant-audit-trail"></a>

The assistant's activities are auditable through AWS CloudTrail (CloudTrail):
+ **Amazon Bedrock invocations** – CloudTrail logs each `InvokeModelWithResponseStream` call as a management event. The log entry records the model ID, user identity, timestamp, and source IP. The `additionalEventData.inferenceRegion` field identifies where the request was processed. The CloudTrail event doesn't include prompt or response content.
+ **Deadline Cloud resource reads** – The assistant's read operations on Deadline Cloud resources (such as `GetJob`, `ListTasks`, `ListSessions`, and `SearchTasks`) are logged in CloudTrail as standard Deadline Cloud API calls. You can query these logs to determine which specific jobs, tasks, and sessions the assistant accessed during a conversation.
+ **CloudWatch Logs reads** – The assistant reads worker and task logs by assuming the queue role (using `deadline:AssumeQueueRoleForRead`) or fleet role (using `deadline:AssumeFleetRoleForRead`). These role assumption events are logged in CloudTrail.

## Abuse detection
<a name="assistant-abuse-detection"></a>

The Amazon Bedrock automated abuse detection mechanisms apply to all assistant usage. For more information, see [Abuse detection](https://docs.aws.amazon.com/bedrock/latest/userguide/abuse-detection.html) in the *Amazon Bedrock User Guide*.

## Feedback data
<a name="assistant-feedback-data"></a>

The assistant provides two feedback mechanisms. Each mechanism transmits different data:
+ **Thumbs up/down buttons** – When you click a thumbs up or thumbs down icon on an assistant response, only a sentiment indicator (positive or negative) and a session identifier are recorded as a telemetry event. No conversation content, log data, or prompts are included in the feedback event.
+ **General feedback form** (non-EU and non-UK regions only) – When you submit general feedback through the speech bubble icon, the form transmits only the information that you explicitly enter. This includes a category selection, a subject line, a description, and an optional email address. The form also includes your monitor's Region and the current page path as metadata. No conversation content or log data is included unless you manually type it into the form fields. General feedback is submitted to an AWS feedback service.

General feedback is unavailable in EU and UK regions because of data residency requirements. The thumbs up/down feedback is available in all regions because the telemetry event contains no customer content.