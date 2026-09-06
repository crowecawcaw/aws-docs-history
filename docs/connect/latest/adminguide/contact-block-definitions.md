

# Flow block definitions in the flow designer in Connect Customer
<a name="contact-block-definitions"></a>

Use flow blocks to create flows in the flow designer. Drag flow blocks and drop them onto a canvas to arrange a flow.

The following table lists all available flow blocks that you can use. Choose any block name in the Block column for more information.


| Block | Description | 
| --- | --- | 
|  [Connect assistant](connect-assistant-block.md) | Associates an AI agents domain to a contact to enable real-time recommendations. | 
|  [Agentic CX](agentic-cx-block.md) | Connects a contact to an Agentic CX Designer application. The block passes context variables into the application and routes the contact based on the exit condition the application returns. | 
| [Authenticate Customer](authenticate-customer.md)  | Enables the customer to authenticate by using Amazon Cognito and Connect Customer Customer Profiles. | 
| [Call phone number](call-phone-number.md)  | Initiates an outbound call from an outbound whisper flow. | 
| [Cases](cases-block.md)  | Gets, updates, and creates cases.  | 
| [Change routing priority / age](change-routing-priority.md)  | Changes the priority of the contact in queue. You might want to do this, for example, based on the contact's issue or other variable. | 
| [Check call progress](check-call-progress.md)  | Engages with the output provided by an answering machine, and provides branches to route the contact accordingly. This block works with outbound campaigns only. | 
| [Check contact attributes](check-contact-attributes.md)  | Checks the values of contact attributes. | 
|  [Check hours of operation](check-hours-of-operation.md) | Checks whether the contact is occurring within or outside of the hours of operation defined for the queue. | 
|  [Check queue status](check-queue-status.md)  | Checks the status of the queue based on specified conditions. | 
|  [Check Voice ID](check-voice-id.md)  | Branches based on the enrollment status, voice authentication status, or status of detection of fraudsters in a watchlist of the caller returned by Voice ID. | 
|  [Check staffing](check-staffing.md)  | Checks the current working queue, or queue you specify in the block, for whether agents are available, staffed, or online. Staffed availability could be on call, or after contact work status. | 
|  [Contact tags](contact-tags-block.md)  | Create and apply user-defined tags (key:value pairs) to your contacts. | 
|  [Create persistent contact association](create-persistent-contact-association-block.md)  | Specify an attribute to create a persistent contact association, enabling conversations to continue from where they left off. | 
|  [Create task](create-task-block.md)  | Creates a new task, sets the tasks attributes, and initiates a contact flow to start the task. To learn more about Connect Customer Tasks, see [The task channel in Connect Customer](tasks.md).  | 
|  [Customer profiles](customer-profiles-block.md)  | You can retrieve, create, and update a customer profile. | 
|  [Data Table](data-table-block.md)  | Evaluate, list, or write data from data tables within your contact flows. | 
|  [Disconnect / hang up](disconnect-hang-up.md)  | Disconnects a contact. | 
|  [Distribute by percentage](distribute-by-percentage.md)  | Routes customers randomly based on a percentage. | 
|  [End flow / Resume](end-flow-resume.md)  | Ends the current flow without disconnecting the contact. | 
| [External Tool](external-tool.md) | Invokes a tool from an external application integrated through an Amazon Bedrock AgentCore gateway. | 
|  [Get customer input](get-customer-input.md)  | Branches based on customer intent. | 
| [Get metrics](get-queue-metrics.md) | Retrieves real-time metrics about queues and agents in your contact center and returns them as attributes. | 
| [Get stored content](get-stored-content.md) | Retrieves content stored in S3 and returns them as attributes to be used within flows. | 
| [Hold customer or agent](hold-customer-agent.md) | Places a customer or agent on or off hold. | 
| [AWS Lambda function](invoke-lambda-function-block.md) | Calls AWS Lambda, and returns key-value pairs or JSON responses that can be used in a flow. | 
| [Invoke module](invoke-module-block.md) | Calls a published module. | 
| [Interrupt agent](interrupt-agent.md) | Offers a contact to a specific agent even if the agent is at maximum concurrency or in a custom status. | 
| [Loop](loop.md) | Loops through, or repeats, the **Looping** branch for the number of loops specified or the number of elements in the provided array. | 
| [Loop prompts](loop-prompts.md) | Loops a sequence of prompts while a customer or agent is on hold or in queue.  | 
|  [Play prompt](play.md) | Plays an interruptible audio prompt, delivers a text-to-speech message, or delivers a chat response. | 
|  [Resume contact](resume-contact.md) | Resumes a contact from a paused state. | 
|  [Return (from module)](return-module.md) | Exits the flow module after it has run successfully. | 
|  [Send message](send-message.md)  | Sends a message to your customer based on a template or custom message you specify. | 
|  [Set callback number](set-callback-number.md)  | Sets a callback number. | 
|  [Set contact attributes](set-contact-attributes.md)  | Stores key-value pairs as contact attributes. | 
| [Set customer queue flow](set-customer-queue-flow.md) | Specifies the flow to invoke when a customer is transferred to a queue. | 
|  [Set disconnect flow](set-disconnect-flow.md)  | Sets the flow to run after a disconnect event. | 
|  [Set event flow](set-event-flow.md)  | Specifies which flow to run during a contact event. | 
|  [Set hold flow](set-hold-flow.md)  | Links from one flow type to another. | 
|  [Set logging behavior](set-logging-behavior.md)  | Enables flow logs so you can track events as contacts interact with flows. | 
|  [Set recording and analytics behavior](set-recording-behavior.md) | Sets options for recording conversations. | 
|  [Set recording, analytics and processing behavior](set-recording-analytics-processing-behavior.md)  | Sets options to configure recording behavior for agent and customer, enable automated interaction, enable screen recording, set analytics behavior for contacts, and set custom processing behavior. | 
|  [Set routing criteria](set-routing-criteria.md)  | Sets routing criteria on contacts of any channel, such as Voice, Chat, and Task, to define how the contact should be routed within its queue. A routing criteria is a sequence of one or more routing steps. | 
| [Set Touchtone Buffer Behavior](set-touchtone-buffer-behavior.md) | Controls touchtone buffering behavior, enabling customers to type ahead during IVR interactions. | 
|  [Set Voice ID](set-voice-id.md)  | When the call is connected to a flow, sends audio to Connect Customer Voice ID to verify the caller's identity and match against fraudsters on a watch list.  | 
| [Set voice](set-voice.md)  | Sets the text-to-speech (TTS) language and voice to be used in the flow. | 
|  [Set whisper flow](set-whisper-flow.md) | Overrides the default whisper by linking to a whisper flow. | 
|  [Set working queue](set-working-queue.md)  | Specifies the queue to be used when **Transfer to queue** is invoked. | 
|  [Show view](show-view-block.md)  | Configures UI based workflows that you can surface to users in front end applications. | 
|  [Start media streaming](start-media-streaming.md)  | Starts capturing customer audio for a contact. | 
|  [Stop media streaming](stop-media-streaming.md)  | Stops capturing customer audio after it is started with a **Start media streaming** block. | 
|  [Store customer input](store-customer-input.md)  | Stores numerical input to a contact attribute. | 
|  [Transfer to agent (beta)](transfer-to-agent-block.md) | Transfers the customer to an agent. | 
|  [Transfer to flow](transfer-to-flow.md) | Transfers the customer to another flow. | 
|  [Transfer to phone number](transfer-to-phone-number.md) | Transfers the customer to a phone number external to your instance. | 
|  [Transfer to queue](transfer-to-queue.md)  | In most flows, this block ends the current flow and places the customer in queue. When used in a customer queue flow, this block transfers a contact already in a queue to another queue. | 
|  [Wait](wait.md) | Pauses the flow. | 