

# Getting started with ambient documentation
<a name="al-getting-started"></a>

This tutorial walks you through the minimum steps to run your first ambient documentation session, from creating a subscription to retrieving the generated clinical note. Each step links to a topic with full details — use this page to understand the overall flow, and the linked topics as reference when you implement each step.

**Topics**
+ [Prerequisites](#al-getting-started-prerequisites)
+ [Step 1: Create a subscription](#al-getting-started-step1)
+ [Step 2: Choose a clinical note template](#al-getting-started-step2)
+ [Step 3: Prepare encounter context (optional)](#al-getting-started-step3)
+ [Step 4: Start a session and stream audio](#al-getting-started-step4)
+ [Step 5: End the session and retrieve outputs](#al-getting-started-step5)
+ [Next steps](#al-getting-started-next-steps)

## Prerequisites
<a name="al-getting-started-prerequisites"></a>

Before you start, make sure you have:
+ An AWS account with access to Amazon Connect Health in a supported Region. See [Supported Regions](what-is-service.md#supported-regions).
+ IAM permissions for the `health-agent:StartMedicalScribeListeningSession` action.
+ An Amazon S3 bucket to receive session outputs.
+ A consent process for your patients. See [Consent and patient notification](ambient-documentation.md#al-consent).

## Step 1: Create a subscription
<a name="al-getting-started-step1"></a>

Associate a provider with the ambient documentation agent by calling the `CreateSubscription` API operation. This gives you a `subscriptionId` that you use to start streaming sessions. For details, see [Subscription management](al-subscription-management.md).

## Step 2: Choose a clinical note template
<a name="al-getting-started-step2"></a>

Decide how the generated note should be structured. For most physical health encounters, the default managed template (`HISTORY_AND_PHYSICAL`) is a good starting point — you can switch to a different managed template or define a custom template later as your requirements become clearer. For details, see [Clinical note templates](al-templates.md).

## Step 3: Prepare encounter context (optional)
<a name="al-getting-started-step3"></a>

If you have background information about the patient that won’t be spoken aloud during the visit — active problems, current medications, the reason for the visit — prepare it as encounter context. This step is optional, but it improves the accuracy of the generated note. For details, see [Encounter context](al-patient-context.md).

## Step 4: Start a session and stream audio
<a name="al-getting-started-step4"></a>

Send a configuration event with your subscription, note template, and any encounter context, then stream audio over HTTP/2 or WebSocket for the duration of the conversation. Send audio in small chunks at close to real time. For details, see [Streaming audio](al-streaming.md).

## Step 5: End the session and retrieve outputs
<a name="al-getting-started-step5"></a>

Send an `END_OF_SESSION` control event when the conversation ends. The service writes the transcript, clinical documentation, and after-visit summary to your configured Amazon S3 bucket. For details, see [Storage and outputs](al-outputs.md).

## Next steps
<a name="al-getting-started-next-steps"></a>

Once your first session succeeds end-to-end:
+ Tune your clinical note template — see [Clinical note templates](al-templates.md).
+ Review the streaming best practices to keep longer sessions healthy — see [Streaming best practices](al-streaming.md#al-streaming-best-practices).
+ If a session fails, check [Troubleshooting ambient documentation](al-troubleshooting.md).