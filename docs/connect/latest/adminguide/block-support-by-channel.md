

# Supported channels for flow blocks in Connect Customer
<a name="block-support-by-channel"></a>

The following table lists all available flow blocks, and whether they support routing a contact through the specified channels. 


| Block | Voice | Chat | Task | Email | 
| --- | --- | --- | --- | --- | 
|  [Connect assistant](connect-assistant-block.md) | Yes | Yes | No - Error branch | Yes | 
|  [Agentic CX](agentic-cx-block.md) | Yes | Yes | No - Error branch | No - Error branch | 
| [Authenticate Customer](authenticate-customer.md)  | No - Error branch | Yes | No - Error branch | No - Error branch | 
| [Call phone number](call-phone-number.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
| [Cases](cases-block.md)  | Yes | Yes | Yes | Yes | 
| [Change routing priority / age](change-routing-priority.md)  | Yes | Yes | Yes | Yes | 
| [Check call progress](check-call-progress.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
| [Check contact attributes](check-contact-attributes.md)  | Yes | Yes | Yes | Yes | 
|  [Check hours of operation](check-hours-of-operation.md) | Yes | Yes | Yes | Yes | 
|  [Check queue status](check-queue-status.md)  | Yes | Yes | Yes | Yes | 
|  [Check Voice ID](check-voice-id.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Check staffing](check-staffing.md)  | Yes | Yes | Yes | Yes | 
|  [Contact tags](contact-tags-block.md)  | Yes | Yes | Yes | Yes | 
| [Create persistent contact association](create-persistent-contact-association-block.md)  | No - Error branch | Yes | No - Error branch | No - Error branch | 
|  [Create task](create-task-block.md)  | Yes | Yes | Yes | Yes | 
|  [Customer profiles](customer-profiles-block.md)  | Yes | Yes | Yes | Yes | 
|  [Disconnect / hang up](disconnect-hang-up.md)  | Yes | Yes | Yes | Yes | 
|  [Distribute by percentage](distribute-by-percentage.md)  | Yes | Yes | Yes | Yes | 
|  [End flow / Resume](end-flow-resume.md)  | Yes | Yes | Yes | Yes | 
|  [Get customer input](get-customer-input.md)  | Yes | Yes when Amazon Lex is used<br />Otherwise, No - Error branch | No | No | 
| [Get metrics](get-queue-metrics.md) | Yes | Yes | Yes | Yes | 
| [Hold customer or agent](hold-customer-agent.md) | Yes | No - Error branch | No - Error branch | No - Error branch | 
| [AWS Lambda function](invoke-lambda-function-block.md) | Yes | Yes | Yes | Yes | 
| [Invoke module](invoke-module-block.md) | Yes | Yes | Yes | Yes | 
| [Interrupt agent](interrupt-agent.md) | Yes | Yes | Yes | Yes | 
| [Loop](loop.md) | Yes | Yes | Yes | Yes | 
| [Loop prompts](loop-prompts.md) | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Play prompt](play.md) | Yes | Yes | No - takes the **Success** branch, but it has no effect | No - takes the **Success** branch, but it has no effect | 
|  [Resume contact](resume-contact.md)  | No - Error branch | No - Error branch | Yes | No - Error branch | 
|  [Return (from module)](return-module.md)  | Yes | Yes | Yes | Yes | 
|  [Set callback number](set-callback-number.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Set contact attributes](set-contact-attributes.md)  | Yes | Yes | Yes | Yes | 
| [Set customer queue flow](set-customer-queue-flow.md) | Yes | Yes | Yes | Yes | 
|  [Set disconnect flow](set-disconnect-flow.md)  | Yes | Yes | Yes | Yes | 
|  [Set hold flow](set-hold-flow.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Set logging behavior](set-logging-behavior.md)  | Yes | Yes | Yes | Yes | 
|  [Set recording and analytics behavior](set-recording-behavior.md) | Yes | Yes | No - Error branch | No - Error branch | 
|  [Set recording, analytics and processing behavior](set-recording-analytics-processing-behavior.md)  | Yes | Yes | Yes | Yes | 
|  [Set routing criteria](set-routing-criteria.md) | Yes | Yes | Yes | Yes | 
|  [Set Voice ID](set-voice-id.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
| [Set voice](set-voice.md)  | Yes | No - Success branch | No - Success branch | No - Success branch | 
|  [Set whisper flow](set-whisper-flow.md) | Yes | Yes | Yes | Yes | 
|  [Set working queue](set-working-queue.md)  | Yes | Yes | Yes | Yes | 
|  [Show view](show-view-block.md)  | No - Error branch | Yes | No - Error branch | Yes | 
|  [Start media streaming](start-media-streaming.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Stop media streaming](stop-media-streaming.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Store customer input](store-customer-input.md)  | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Transfer to agent (beta)](transfer-to-agent-block.md) | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Transfer to flow](transfer-to-flow.md) | Yes | Yes | Yes | Yes | 
|  [Transfer to phone number](transfer-to-phone-number.md) | Yes | No - Error branch | No - Error branch | No - Error branch | 
|  [Transfer to queue](transfer-to-queue.md)  | Yes | Yes | Yes | Yes | 
|  [Wait](wait.md) | No - Error branch | Yes | Yes | Yes | 