

# Set up your instance for Resolutions

 Resolutions runs on Connect Customer features that have their own setup guides: AI agents, Customer Profiles, Cases, email, and attachments. Set up each feature by following its guide, which stays current as the feature changes. This page lists the features that Resolutions needs, and covers only the configuration that Resolutions depends on and those guides don't include. It's for Connect Customer administrators. 

## Prerequisites checklist
<a name="resolutions-prerequisites-prerequisites-checklist"></a>

 Complete the features in this order. Some steps fail in ways that are hard to diagnose when you complete them out of order. 


| Feature | Set it up with | Required for | Additional configuration for Resolutions | 
| --- | --- | --- | --- | 
| AI agents |  [Initial set-up for AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html)  | Authoring Work plans | [AI agents](#resolutions-prereq-ai-agents) | 
| Customer Profiles |  [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md)  | Creating Resolutions Cases |  [Enable Customer Profiles before Cases](#resolutions-prereq-profiles)  | 
| Cases |  [Enable Cases using the Connect Customer console](enable-cases.md)  | Associating a Work plan with a Case template | [Cases](#resolutions-prereq-cases) | 
| Email |  [Set up email in Connect Customer](setup-email-channel.md)  | Work plans that start from inbound email or send email | [Email](#resolutions-prereq-email) | 
| Attachments | [Enable attachments](enable-attachments.md) | Work plans that read customer attachments |  [Attachments](#resolutions-prereq-attachments)  | 
| Resolutions access |  [Grant access to Resolutions](resolutions-grant-access.md)  | Authoring Work plans | None | 
| Inbound contact flow |  [Start Work plans from inbound email](resolutions-start-work-plan.md)  | Starting Work plans | None | 

**Note**  
 Enabling Cases and enabling email need IAM permissions beyond a typical operations role. Each feature's guide lists the permissions it needs. If your role has fewer permissions, ask an administrator to complete those steps. 

## AI agents
<a name="resolutions-prereq-ai-agents"></a>

 The Resolutions AI assistant runs on Connect AI agents. Without an AI agents domain on your instance, Resolutions can't generate a Work plan, and authoring stops at the first question. 

 If you encrypt the AI agents domain with a customer managed AWS KMS key, grant the permissions that [Initial set-up for AI agents](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html) lists for using AI agents with chat, tasks, and email. Resolutions works through Tasks and email, so it needs those permissions. 

## Enable Customer Profiles before Cases
<a name="resolutions-prereq-profiles"></a>

 Cases requires a Customer Profiles domain. If you enable Cases first, enabling Cases still appears to succeed, and you can still build Case templates. The problem appears later, when Resolutions Case creation fails with the error `Field(s) customer_id are required`. 

 Before you enable Cases, confirm that a Customer Profiles domain exists in the same AWS Region as your instance. 

```
aws customer-profiles list-domains --region {{your-region}}
```

## Cases
<a name="resolutions-prereq-cases"></a>

 Resolutions needs Cases enabled with a domain. You don't need to create Case fields or a Case template in advance. Resolutions generates both from your standard operating procedure (SOP) when you author a Work plan. 

**Note**  
 If you build a Case template by hand instead of using the generated one, mark as required only the fields that are known when the Resolutions Case is created. A Work plan fills in some fields as it runs. A required field with no value at creation time prevents the Resolutions Case from being created. 

## Email
<a name="resolutions-prereq-email"></a>

 Complete this section if your Work plans start from inbound customer email or send email to customers. Set up the email channel by following [Set up email in Connect Customer](setup-email-channel.md) and [Enable email for your Connect Customer instance](enable-email1.md). Then check the following. 

### Move Amazon SES out of the sandbox before you test outbound email
<a name="resolutions-prerequisites-move-amazon-ses-out-of-the-sandbox-before-you-test-outbound-email"></a>

 The email setup guide asks you to move Amazon SES out of sandbox mode. If you skip this step, inbound email still starts the Work plan. Steps that email the customer fail, unless the recipient address or domain is verified in Amazon SES. The symptom is a Work plan that starts correctly and then stalls at its first email Step. 

To check your status, run the following command.

```
aws sesv2 get-account --region {{your-region}}
```

 `ProductionAccessEnabled: false` means that your account is in the sandbox. Sandbox status applies per account and per Region. Approval for production access isn't immediate, so [request it](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html) well ahead of launch. For early testing, verify the recipient addresses that you plan to email. 

### Outbound queue and whisper flow for Work plan email
<a name="resolutions-prerequisites-outbound-queue-and-whisper-flow-for-work-plan-email"></a>

 Email that a Work plan sends is an outbound email contact, and it routes through a queue. The queue's **Outbound email flow** links each email to its Resolutions Case. A Work plan advances by watching for updates on the Resolutions Case. When it emails a customer for missing information, it waits for the reply to arrive on that Resolutions Case before it continues. 

 When you configure a Step that emails customers, you choose the queue that sends its email in the Step's **CreateContact** configuration. You have two options. 


| Option | What Resolutions does | What you do | 
| --- | --- | --- | 
| Ask Resolutions to create a dedicated outbound queue |  Creates the queue and an outbound whisper flow, and sets the flow as the queue's Outbound email flow  | Nothing | 
| Choose an existing queue | Sends the Step's email through the queue |  Set the queue's Outbound email flow to a flow that links each email to its Resolutions Case. Use the [sample outbound whisper flow](#resolutions-prerequisites-sample-outbound-whisper-flow).  | 

 If the outbound email isn't linked to the Resolutions Case, the customer's reply isn't associated with the Resolutions Case either. Resolutions tracks progress only through updates on the Resolutions Case, so it can't see the reply or tell that the customer answered. The Step that waits for the reply doesn't complete, and the Resolutions Case shows no record of the exchange. A Work plan waits at most 7 days between Step completions, and a Work plan runs for at most 90 days before it closes. 

**Warning**  
 If you choose an existing queue, Resolutions can't detect a missing link, because the queue's **Outbound email flow** is configured outside the Work plan. Set the queue's outbound email flow before you send your first test request. 

 The queue's outbound email flow also runs for email that agents send from that queue. For more information, see [Set up email in Connect Customer](setup-email-channel.md). If an existing queue already uses an outbound flow, add the Cases block from the sample to that flow instead of replacing it. 

 A Work plan sets its own from address in the Step flow, so the queue's **Default email address** doesn't affect Work plan email. 

### Sample outbound whisper flow
<a name="resolutions-prerequisites-sample-outbound-whisper-flow"></a>

 The following flow turns on flow logging, finds the Resolutions Case related to the contact, and links the outbound email to it. Every error branch ends the flow. 

 **To set the sample flow on an existing queue** 

1.  In the Connect Customer admin website, choose **Routing**, **Flows**, and create a flow of type **Outbound whisper flow**. 

1. Import the following sample flow, and then publish the flow.

1.  Choose **Routing**, **Queues**, and open the queue that the Step's **CreateContact** configuration uses. 

1.  Under **Outbound email configuration**, set **Outbound email flow** to the flow that you published, and then save the queue. 

1.  Send a test request. After the Work plan emails the customer, reply to the email. Confirm that the reply appears on the same Resolutions Case and that the Work plan moves to the next Step. 

```json
{
  "Version": "2019-10-30",
  "StartAction": "3eab3bcf-82ac-40c2-a58c-945ab5ae951e",
  "Metadata": {
    "entryPointPosition": { "x": 40, "y": 40 },
    "ActionMetadata": {
      "3eab3bcf-82ac-40c2-a58c-945ab5ae951e": { "position": { "x": 148, "y": 160 } },
      "a5a625ea-8a23-4027-ab87-3de51f64343c": { "position": { "x": 399.2, "y": 76 } },
      "d3b9b9ab-b037-45aa-9a9e-82f18b96790c": { "position": { "x": 846.4, "y": 156 } }
    },
    "Annotations": [],
    "name": "Resolutions outbound email",
    "description": "Links each outbound email to its Resolutions Case",
    "type": "outboundWhisper",
    "status": "PUBLISHED",
    "hash": {}
  },
  "Actions": [
    {
      "Identifier": "3eab3bcf-82ac-40c2-a58c-945ab5ae951e",
      "Type": "UpdateFlowLoggingBehavior",
      "Parameters": { "FlowLoggingBehavior": "Enabled" },
      "Transitions": { "NextAction": "a5a625ea-8a23-4027-ab87-3de51f64343c" }
    },
    {
      "Identifier": "a5a625ea-8a23-4027-ab87-3de51f64343c",
      "Type": "GetCaseId",
      "Parameters": {
        "LinkContactToCase": "true",
        "ContactToLink": "Current",
        "ContactToSearch": "Related"
      },
      "Transitions": {
        "NextAction": "d3b9b9ab-b037-45aa-9a9e-82f18b96790c",
        "Errors": [
          { "NextAction": "d3b9b9ab-b037-45aa-9a9e-82f18b96790c", "ErrorType": "ContactNotLinked" },
          { "NextAction": "d3b9b9ab-b037-45aa-9a9e-82f18b96790c", "ErrorType": "MultipleFound" },
          { "NextAction": "d3b9b9ab-b037-45aa-9a9e-82f18b96790c", "ErrorType": "NoneFound" },
          { "NextAction": "d3b9b9ab-b037-45aa-9a9e-82f18b96790c", "ErrorType": "NoMatchingError" }
        ]
      }
    },
    {
      "Identifier": "d3b9b9ab-b037-45aa-9a9e-82f18b96790c",
      "Type": "EndFlowExecution",
      "Parameters": {},
      "Transitions": {}
    }
  ]
}
```

### Verify the email channel before you test a Work plan
<a name="resolutions-prerequisites-verify-the-email-channel-before-you-test-a-work-plan"></a>

 Send a plain test email to your Connect Customer email address and confirm that a contact arrives in the instance. Email configuration problems and Work plan problems look the same from the outside, so ruling out the email channel first saves diagnosis time. 

## Attachments
<a name="resolutions-prereq-attachments"></a>

 Complete this section if your Work plans read attachments that customers send, for example to extract details from an attached document. Enable attachments, including the CORS policy on the attachments bucket, by following [Enable attachments](enable-attachments.md). Without the CORS policy, the email channel stops working. 

### Attachment limits for Work plans
<a name="resolutions-prerequisites-attachment-limits-for-work-plans"></a>

 A Work plan can read a smaller set of attachments than the email channel accepts. 


| Limit | What a Work plan can read | What the email channel accepts | 
| --- | --- | --- | 
| Maximum size of one attachment | 4.5 MB | 20 MB by default | 
| File formats | .pdf, .txt, .csv, .html, .md, .xls, .xlsx | The instance's allowed file types for email | 

 For the email channel's limits, see [Connect Customer feature specifications](feature-limits.md). If you customize the allowed file types for the Email channel, keep the formats that a Work plan reads. 

**Note**  
 To use HTML (`text/html`) and Markdown (`text/markdown`) attachments, enable the `.html` and `.md` file extensions on your instance. On the **Attachments** page, choose the channel that receives the attachments, such as **Email**, and add the extensions in **Add file extensions**. For instructions, see [Enable attachments](enable-attachments.md). 

 An attachment that the email channel accepts, but that is larger than 4.5 MB or in another format, arrives normally. The contact and the Resolutions Case are created, but extraction from the attachment fails. This looks like a broken Work plan rather than a problem with the attachment. 