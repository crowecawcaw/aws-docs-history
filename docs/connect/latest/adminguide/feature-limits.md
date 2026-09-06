

# Connect Customer feature specifications
<a name="feature-limits"></a>

**Important**  
You can't increase the feature specifications listed here. They are hard limits.

The following tables list the various Connect Customer feature specifications. 

**Topics**
+ [Chat feature specifications](#feature-limits-chat)
+ [Chat message size limits by channel](#chat-message-size-limits)
+ [WhatsApp business messaging feature specifications](#whatsapp-specs)
+ [Email feature specifications](#email-feature-specs)
+ [Task feature specifications](#feature-limits-tasks)
+ [Forecasting, capacity planning, and scheduling](#forecasting-cap-planning-scheduling-specs)
+ [Integration association resource](#integration-association-resource-feature-specs)
+ [Connect Customer conversational analytics](#contact-lens-feature-specs)
+ [Evaluation forms](#evaluationforms-feature-specs)
+ [Connect Customer Rules](#rules-feature-specs)


| Item | Feature Specification  | 
| --- | --- | 
| Agent activity retention  | 24 months from the time the event occurred | 
| Approved origin per Connect Customer instance  | 100 | 
| File types supported for attachments to emails, cases, chats, or tasks | .csv, .doc, .docx, .heic, .jfif, .jpeg, .jpg, .mov, .mp4, .pdf, .png, .ppt, .pptx, .rtf, .txt, .wav, .xls, .xlsx <br />Administrators can also configure custom file extensions through the Connect Customer admin website or the Connect Customer API. For instructions, see [Step 3: Configure attachment file types and size limits](enable-attachments.md#step3-configure-attachment-options).<br />For more information about supported file types for WhatsApp business messaging, see [WhatsApp business messaging feature specifications](#whatsapp-specs) later in this topic. | 
| Maximum file size for an attachment to an email | Default 20 MB (configurable from 1 MB to 20 MB). To configure, use the Connect Customer admin website or the [UpdateAttachedFilesConfiguration](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateAttachedFilesConfiguration.html) API. | 
| Maximum file size for an attachment to a case, chat, or task | Default 20 MB (configurable from 1 MB to 100 MB). To configure, use the Connect Customer admin website or the [UpdateAttachedFilesConfiguration](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateAttachedFilesConfiguration.html) API.<br />For more information about supported file sizes for WhatsApp business messaging, see [WhatsApp business messaging feature specifications](#whatsapp-specs) later in this topic. | 
| Maximum timeout for an attachment scanner | 60 seconds | 
| Maximum size of a real-time metrics report  | 200KB | 
| When the [Multi-Party Calls and Enhanced Monitoring for Voice](monitor-barge.md#monitor-barge-set-up) capability is enabled, voice supports 6 participants. Two supervisors can monitor the call.  | 6<br />For example, you can have a group of 6 participants in the call at the same time. Two supervisors can monitor the call. The two supervisors can do two silent monitor sessions, or one silent monitor and one barge-in session. <br />The total number of participants on a call would look like this:1.  Customer - participant <br />2.  Agent 1 - participant <br />3.  Agent 2 - participant <br />4.  Agent 3 - participant <br />5.  Agent 4 - participant <br />6.  Agent 5 - participant <br />7.  Supervisor who can listen but not barge in the call <br />8.  Supervisor who can listen or barge in the call  | 
| When the [Multi-Party Calls and Enhanced Monitoring for Voice](monitor-barge.md#monitor-barge-set-up) capability is not enabled, voice supports 3 participants on the call, and 5 supervisors monitoring the call.  | 3<br />There can be 3 participants in total:1.  Customer - participant <br />2.  Agent 1 - participant <br />3.  Agent 2 - participant <br />4.  Supervisor who can listen but not barge in the call <br />5.  Supervisor who can listen but not barge in the call <br />6.  Supervisor who can listen but not barge in the call <br />7.  Supervisor who can listen but not barge in the call <br />8.  Supervisor who can listen but not barge in the call  | 
| Quick connects you can assign to a queue | 700 | 
| Participants on a conference call | 6<br />The participants are the customer, agent, and others who can be agents or external third-parties. | 
| Contact record retention for all channels and subtypes (voice, email, tasks, and chat, including SMS, WhatsApp, and Apple Messages for Business). | 24 months from the time the associated contact was initiated. <br />You can choose to stream contact records to Kinesis so you can manage retention and perform advanced analysis. | 
| Maximum size of the returned data in a Lambda function | Less than 32KB of UTF-8 data | 
| Limit on creating and deleting instances | 100 instances can be created or deleted in 30 days<br />Connect Customer enforces a limit on the **total** number of instances that you can create and delete in 30 days. If you exceed this limit, you will get an error message indicating there has been an excessive number of attempts at creating or deleting instances. You must wait 30 days before you can restart creating and deleting instances in your account.<br />For example, if you create 80 instances and delete 20 over the course of 30 days, you must wait an additional 30 days before you can create or delete any more instances. If you create and delete the same instance 100 times in 30 days, the limit also applies.  | 
| Searchable custom contact attributes | 50 | 
| Replica instances (created by using the [ReplicateInstance](https://docs.aws.amazon.com/connect/latest/APIReference/API_ReplicateInstance.html) API) | 5 per account | 
| Traffic distribution groups | 8 per replicated instance | 

## Chat feature specifications
<a name="feature-limits-chat"></a>


| Item | Feature Specification | 
| --- | --- | 
| Attachments per chat conversation | 35 | 
| Active chats per agent | 10 | 
| Participants on a conference chat | 6<br />The participants are the customer, agent, and others who can be agents. | 
| Custom participants (such as a custom bot) on a contact | 1 | 
| Chat contacts that a supervisor can monitor concurrently | Depends on the number of concurrent chats limit set in the supervisor's routing profile | 
| People who can monitor the same agent chat at the same time regardless of whether the [Enable Multi-Party Chats and Enhanced Monitoring for Chat](monitor-barge.md#monitor-barge-set-up) capability is enabled for an instance | 5<br />For example, you can have a group of 5 people monitor a chat at the same time, and then a different group of 5 people monitor a different chat at the same time, and so on.<br />The total number of participants on the chat would look like this:1.  Customer <br />2.  Agent <br />3.  Supervisor who can monitor the chat but not barge in <br />4.  Supervisor who can monitor the chat but not barge in <br />5.  Supervisor who can monitor the chat but not barge in <br />6.  Supervisor who can monitor the chat but not barge in <br />7.  Supervisor who can monitor the chat but not barge in  | 
| Supervisors who can barge in on a chat between an agent and a customer when the [Enable Multi-Party Chats and Enhanced Monitoring for Chat](monitor-barge.md#monitor-barge-set-up) capability enabled for an instance | 1<br />Only 1 supervisor can be in barged in mode for a given chat. | 
| Total duration per chat | Up to 7 days, including wait time+  The default is 25 hours. You configure the chat duration using [StartChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartChatContact.html) API and add the `ChatDurationInMinutes` parameter. <br />+  Minimum configurable chat duration is 1 hour (60 minutes). <br />+  Maximum configurable chat duration is 7 days (10,080 minutes).  | 
| Maximum message size | Varies by channel and direction. See [Chat message size limits by channel](#chat-message-size-limits). | 
| Open websocket connections per chat participant | 5 | 
| Chat Amazon Lex bot integration timeout | 10 seconds<br />The maximum time within which the Amazon Lex bot must respond to the chat customer's prompt. | 
| Past chat transcript file size. This applies to [persistent chat](chat-persistence.md).  | 5MB | 
| Past contacts that can be traversed by Connect Customer chat. This applies to [persistent chat](chat-persistence.md).  | 100 | 
| Communications widgets that can be created and customized per instance  | 20 | 
| File types supported for attachments to cases, chats, or tasks | .csv, .doc, .docx, .heic, .jfif, .jpeg, .jpg, .mov, .mp4, .pdf, .png, .ppt, .pptx, .rtf, .txt, .wav, .xls, .xlsx <br />Administrators can also configure custom file extensions through the Connect Customer admin website or the Connect Customer API. | 
| Maximum file size for an attachment to a case, chat, or task | 20 MB (configurable up to 100 MB) Administrators can configure up to 100 MB through the Connect Customer admin website or the Connect Customer API.  | 

## Chat message size limits by channel
<a name="chat-message-size-limits"></a>

The following table lists the maximum message size for each messaging channel, direction, and receiver.



- **SMS**
  - **Direction:** Inbound / **Message initiator:** End customer / **Receiver:** Agent or Lex (Connect) / **Limit:** 1,024 characters
  - **Direction:** Outbound / **Message initiator:** Agent or Lex bot (Connect) / **Receiver:** End customer / **Limit:** 1,024 characters

- **WhatsApp**
  - **Direction:** Inbound / **Message initiator:** End customer / **Receiver:** Lex (Connect) / **Limit:** 4,096 characters
  - **Message initiator:** End customer / **Receiver:** Agent / **Limit:** 4,096 characters
  - **Direction:** Outbound / **Message initiator:** Agent or Lex bot (Connect) / **Receiver:** End customer / **Limit:** 4,096 characters

- **Apple Messages for Business**
  - **Direction:** Inbound / **Message initiator:** End customer / **Receiver:** Lex (Connect) / **Limit:** 4,096 characters
  - **Message initiator:** End customer / **Receiver:** Agent / **Limit:** 4,096 characters
  - **Direction:** Outbound / **Message initiator:** Agent or Lex bot (Connect) / **Receiver:** End customer / **Limit:** 4,096 characters

- **Chat**
  - **Direction:** Inbound / **Message initiator:** End customer / **Receiver:** Lex (Connect) / **Limit:** 1,024 characters
  - **Message initiator:** End customer / **Receiver:** Agent / **Limit:** 16,384 bytes
  - **Direction:** Outbound / **Message initiator:** Agent or Lex bot (Connect) / **Receiver:** End customer / **Limit:** 16,384 bytes



**Note**  
*Agent* includes human agents and AI agents created through custom participant. For more information, see [Customize chat flow experiences using custom participants](https://docs.aws.amazon.com/connect/latest/adminguide/chat-customize-flow.html). Amazon Lex bots have separate message size limits.

## WhatsApp business messaging feature specifications
<a name="whatsapp-specs"></a>

The following table lists the specifications for WhatsApp business messaging


| **Media type** | **Supported file types** | **Maximum file size** | 
| --- | --- | --- | 
| Image | .jpeg, .jpg, .jfif, .png | 5MB | 
| Video | .mp4, .3gp | 16MB | 
| Document | .txt, .pdf, .ppt, .pptx, .doc, .docx, .xls, .xlsx | 20MB | 
| Audio | .aac, .m4a, .mp3, .amr, .ogg | 16MB | 
| Sticker | Not supported | Not supported | 

## Email feature specifications
<a name="email-feature-specs"></a>


| Item | Feature Specification | 
| --- | --- | 
| Maximum email message body size | 5 MB | 
| Email message body format | HTML (`text/html`) (Default)<br />Plain text (`text/plain`)<br />All email contacts (messages) sent by Connect Customer are handled in HTML (`text/html`) format by default. Additionally, a plain text (`text/plain`) version is stored and available for all email contacts (messages) in Connect Customer for features like the [Flow block in Connect Customer: Get stored content](get-stored-content.md) flow block. | 
| Maximum email message body plus attachments size | 25 MB | 
| File attachments per email contact (message) | 50 attachments | 
| Inline images per email contact (message) | No limit so long as the size of inline images received in the email message does not exceed 5 MB. | 
| Inline image formats supported | `image/jpg`, `image/jpeg`, `image/png`, `image/gif`, `image/svg`, `image/webp`, `image/bmp`, `image/heif`, `image/heic`<br />All inline images are Base64 encoded when storing email messages with Connect Customer. | 
| Email message and attachment retention | This is defined by your Amazon S3 lifecycle configuration. For more information, see [Managing your storage lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html) in the *Amazon Simple Storage Service User Guide*. Contact record retention for all channels and subtypes still applies for email contact data.<br />You can easily download and access email messages and attachments using the [Download recordings and transcripts of past conversations in Connect Customer](download-recordings.md) feature. | 
| Active email contact expiry | 14 days (Default)<br />Customizable up to 90 days using the [Flow block in Connect Customer: Set contact attributes](set-contact-attributes.md) flow block or [Expiry](https://docs.aws.amazon.com/connect/latest/APIReference/API_Expiry.html) API to update the connect:ContactExpiry [segment attribute](connect-attrib-list.md#attribs-segment-attributes).<br />This determines how long an email contact can remain active (for example, waiting in queue or assigned to an agent) before expiring and closing automatically. "No" for adjustability means that you cannot customize or increase this attribute to be greater than 90 days. | 
| Email addresses per email (contact) message | 50 email addresses per email contact (message) total across To and CC.<br />Inbound email contacts (messages) support any combination of 50 email addresses total across To and CC.<br />Outbound email contacts (messages) support only 1 email address in To and up to 49 email addresses in CC.<br />Only 1 from email address per email contact (message).<br />BCC email addresses are not supported in Connect Customer. | 
| Maximum number of characters in email subject | 998 | 
| Maximum length of an email address | 255 | 
| Maximum length of a display name for an email address | 256 | 

## Task feature specifications
<a name="feature-limits-tasks"></a>


| Item | Feature Specification | 
| --- | --- | 
| Task templates per instance | 50 | 
| Task template customized fields per template | 50 | 
| Maximum duration of a task | Default is 7 days, extensible up to 90 days | 
| Maximum number of transfers for a task | 11 transfers | 
| Maximum number of linked tasks on an existing contact | 11 | 

## Forecasting, capacity planning, and scheduling feature specifications
<a name="forecasting-cap-planning-scheduling-specs"></a>


| Item | Feature Specification | 
| --- | --- | 
| Agents per schedule generation run | 5,000 | 
| Agents per staffing group | 350 | 
| Capacity plans per instance | 500 | 
| Capacity scenarios per instance | 500 | 
| Capacity plan user data uploads per instance | 500 | 
| Capacity plan override uploads per instance | 5000 | 
| Concurrent uploads per instance | 20 | 
| Demand groups per forecast group | 25 | 
| File size per upload of agent time off data | 1GB | 
| File size per upload of time off group allowance data | 1GB<br />The .csv file can cover up to 13 months. | 
| File size per upload of capacity plan user data | 1GB | 
| File size per upload of capacity plan overrides | 250MB | 
| File size per upload of forecast overrides | 250MB | 
| File size per upload of historical actuals | 1GB | 
| Historical actuals 15 or 30 minute interval aggregated file size limit | 2GB | 
| Historical actuals daily interval aggregated file size limit | 2GB | 
| Forecast groups per instance | 500 | 
| Forecast override uploads per instance | 500 | 
| Historical actuals 15 or 30 minute interval file count | 300 | 
| Historical actuals daily interval file count | 300 | 
| Queues per forecast group | 200 | 
| Schedules per instance | 1000 | 
| Shift activities per instance | 500 | 
| Shift activities per shift profile | 10 | 
| Shift profiles per instance | 2500 | 
| Shift rotation steps per pattern | 52 | 
| Shift rotation weeks per pattern | 52 | 
| Shift rotations associated with a single shift profile | 1300 | 
| Shift rotations per instance | 1300 | 
| Staffing groups per forecast group | 300 | 
| Staffing groups per instance | 1300 | 
| Staffing groups per supervisor/manager | 250 | 
| Supervisors/managers per staffing group | 100 | 

## Integration association resource feature specifications
<a name="integration-association-resource-feature-specs"></a>

The following table lists feature specifications for the integration association resource. It lists how many of each type of integration association resource can be ingested.


| Item | Feature Specification | 
| --- | --- | 
| Attachment scanner | 1 | 
| Voice ID domain | 1 | 
| Amazon Pinpoint app | 1 | 
| Event | 10<br />The event integration resource is used for task triggers. | 
| agent assist assistant | 1 | 
| agent assist knowledge base | 10 | 
| Cases domain | 1 | 
| agent assist knowledge base | 10 | 

## Connect Customer conversational analytics feature specifications
<a name="contact-lens-feature-specs"></a>


| Item | Feature Specification | 
| --- | --- | 
| Custom vocabularies | 20 | 
| conversational analytics rules for post-call | 500 | 
| conversational analytics rules for post-chat | 500 | 
| conversational analytics rules for real-time | 500 | 

## Evaluation forms feature specifications
<a name="evaluationforms-feature-specs"></a>


| Item | Feature Specification | 
| --- | --- | 
| Maximum number of manual evaluations per agent per month | 2,000 | 
| Maximum number of manually started evaluations filled with assistance of AI per agent per month | 1,000 | 
| Maximum number of automated evaluations filled by Gen AI per agent per month | 2,000 | 
| Maximum number of evaluation forms per instance<br />Historical versions are not counted, only form names are counted. | 400 | 
| Maximum number of versions per form | 50 | 
| Maximum number of sections per form | 100 | 
| Maximum number of questions per form | 100 | 
| Maximum nesting level of sections | 2 (sections can have sub-sections, but sub-sections cannot have sub-sub-sections) | 
| Definition title length | 1-128 characters | 
| Section title length | 1-128 characters | 
| Question title length | 1-350 characters | 
| Section instructions length | up to 1024 characters | 
| Question instructions length | 1-1024 characters | 
| Number of answer options for single select questions | 2-256 answer options | 
| Answer option text length for single select questions | 1-128 characters | 

## Connect Customer Rules feature specifications
<a name="rules-feature-specs"></a>

The following table lists feature specifications for Connect Customer Rules.


| Item | Feature Specification | 
| --- | --- | 
| Conditions in a rule  | 20 | 
| Rules with Natural Language condition for OnPostCallAnalysisAvailable event source | 100 | 
| Rules with Natural Language condition for OnPostChatAnalysisAvailable event source | 100 | 
| Rules with Natural Language condition for OnEmailAnalysisAvailable event source | 15 | 
| Rules for OnPostCallAnalysisAvailable event source | 500 | 
| Rules for OnPostChatAnalysisAvailable event source | 500 | 
| Rules for OnRealTimeCallAnalysisAvailable event source | 500 | 
| Rules for OnRealTimeChatAnalysisAvailable event source | 500 | 
| Rules for OnZendeskTicketCreate event source | 500 | 
| Rules for OnZendeskTicketStatus event source | 500 | 
| Rules for OnSalesforceCaseCreate event source | 500 | 
| Rules for OnContactEvaluationSubmit event source | 500 | 
| Rules for OnCaseUpdate event source | 500 | 
| Rules for OnCaseCreate event source | 500 | 
| Rules for OnMetricDataUpdate event source | 100 | 


| Condition type | Number of entries or selections | Post-call | Post-chat | Real-time | 
| --- | --- | --- | --- | --- | 
| Evaluation - Form score | 20 | N/A | N/A | N/A | 
| Evaluation- Section score | 20 | N/A | N/A | N/A | 
| Evaluation- Question score | 20 | N/A | N/A | N/A | 
| Evaluation - Results available | 20 | N/A | N/A | N/A | 
| Words or phrases - Exact match | 100 | Yes | Yes | Yes | 
| Words or phrases - Semantic match | 4 | Yes | Yes | Not supported | 
| Words or phrases - Pattern match | 100 | Yes | Yes | Yes | 
| Natural Language - Semantic match | 1 | Yes | Yes | No | 
| Queue condition | 100 | Yes | Yes | Yes | 
| Agent condition | 100 | Yes | Yes | Yes | 
| Custom attributes | 5 | Yes | Yes | Yes | 
| Sentiment - Time period | 5 | Yes | Yes | Yes | 
| Sentiment - Entire contact | 5 | Yes | Yes | Not supported | 
| Interruptions | 5 | Yes | Yes | Not supported | 
| Response time | 4 hours | Not supported | Yes | Not supported | 
| Non-talk time | 5 hours | Yes | Not supported | Not supported | 