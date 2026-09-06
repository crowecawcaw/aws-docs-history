

# Contact analytics data in the Connect Customer data lake
<a name="data-lake-contact-analytics-data"></a>

The following tables contain contact analytics data.

**Topics**
+ [Conversational analytics](#data-lake-contact-lens-conversational-analytics)
+ [Contact evaluation record](#data-lake-contact-evaluation-record)

## Conversational analytics
<a name="data-lake-contact-lens-conversational-analytics"></a>

**Table name:** `contact_lens_conversational_analytics`

**Description:** Contains Contact Lens analytics data including sentiment scores, talk and non-talk time, interruptions, talk speed, and response times for voice and chat contacts.

**Primary key:** `instance_id, contact_id`

**Partition key:** `disconnect_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Evaluation Record, Contact Flow Events, AI Agent, AI Session, AI Prompt, AI Tool


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
|  aws\_account\_id  |  string  |  Yes  |  The ID of the AWS account that owns the contact.  | 
|  version  |  string  |  Yes  |  Indicates real-time or post call/chat analysis.  | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  contact\_id  |  string  |  No  |  The ID of the contact being evaluated.  | 
|  channel  |  string  |  Yes  |  The method used to contact your contact center: VOICE, CHAT.  | 
|  language\_locale  |  string  |  Yes  |  Language used to analyze contact - [AI features](supported-languages.md#supported-languages-contact-lens).  | 
|  feature  |  string  |  Yes  |  Will always have the same value "contact\_lens\_conversational\_analytics". | 
|  categories  |  array(string)  |  Yes  |  Array of categories assigned to the contact.  | 
|  disconnect\_timestamp  |  Timestamp  |  Yes  |  The contact disconnect Timestamp.  | 
|  greeting\_time\_agent\_ms  |  bigint  |  Yes  |  First response time of agents on chat, indicating how quickly they engage with customers after joining the chat.  | 
|  non\_talk\_time\_total\_ms  |  bigint  |  Yes  |  Total non-talk time in a voice conversation. Non-talk time refers to the combined duration of hold time and periods of silence exceeding 3 seconds, during which neither the agent nor the customer is engaged in conversation.  | 
|  talk\_time\_total\_ms  |  bigint  |  Yes  |  Time that was spent talking during a voice contact across either the customer or the agent.  | 
|  talk\_time\_agent\_ms  |  bigint  |  Yes  |  Time that was spent talking during a voice contact by the agent.  | 
|  talk\_time\_customer\_ms  |  bigint  |  Yes  |  Time that was spent talking during a voice contact by the customer.  | 
|  total\_conversation\_duration\_ms  |  bigint  |  Yes  |  The total time from the start of the conversation until the last word spoken by either the agent or the customer.  | 
|  talk\_speed\_agent\_wpm  |  float  |  Yes  |  Words per minute spoken by the agent.  | 
|  talk\_speed\_customer\_wpm  |  float  |  Yes  |  Words per minute spoken by the customer.  | 
|  interruptions\_time\_total\_ms  |  bigint  |  Yes  |  Amount of time agent or customer were speaking at the same time.  | 
|  interruptions\_time\_agent\_ms  |  bigint  |  Yes  |  Amount of time the agent spoke while the customer was already speaking.  | 
|  interruptions\_time\_customer\_ms  |  bigint  |  Yes  |  Amount of time the customer spoke while the agent was already speaking.  | 
|  interruptions\_total\_count  |  bigint  |  Yes  |  Count of times interruptions were detected during a conversation.  | 
|  interruptions\_agent\_count  |  bigint  |  Yes  |  Count of time an agent interruption was detected during a conversation  | 
|  interruptions\_customer\_count  |  bigint  |  Yes  |  Count of times a customer interruption was detected during a conversation  | 
|  sentiment\_overall\_score\_agent  |  float  |  Yes  |  A sentiment score is an analysis of text, and a rating of whether it includes mostly positive, negative, or neutral language. This is overall sentiment score for the agent during the call. The overall sentiment score is the average of the scores assigned during each portion of the call.  | 
|  sentiment\_overall\_score\_customer  |  float  |  Yes  |  A sentiment score is an analysis of text, and a rating of whether it includes mostly positive, negative, or neutral language. This is overall sentiment score for customer during the call. The overall sentiment score is the average of the scores assigned during each portion of the call.  | 
|  sentiment\_interaction\_score\_customer\_with\_agent  |  float  |  Yes  |  A sentiment score is an analysis of text, and a rating of whether it includes mostly positive, negative, or neutral language. This is sentiment score of customer with agent.  | 
|  sentiment\_interaction\_score\_customer\_without\_agent  |  float  |  Yes  |  A sentiment score is an analysis of text, and a rating of whether it includes mostly positive, negative, or neutral language. This is sentiment score of customer without the agent.  | 
|  sentiment\_end\_score\_agent  |  float  |  Yes  |  A sentiment score is an analysis of text, and a rating of whether it includes mostly positive, negative, or neutral language. This is sentiment score for agent at the end of the call.  | 
|  sentiment\_end\_score\_customer  |  float  |  Yes  |  A sentiment score is an analysis of text, and a rating of whether it includes mostly positive, negative, or neutral language. This is sentiment score for customer at the end of the call.  | 
|  response\_time\_average\_agent\_ms  |  bigint  |  Yes  |  For chat, average time to send a response after the customers last message.  | 
|  response\_time\_average\_customer\_ms  |  bigint  |  Yes  |  For chat, average time to send a response after the agents last message.  | 
|  response\_time\_maximum\_agent\_ms  |  bigint  |  Yes  |  For chat, maximum time to send a response after the customers last message.  | 
|  response\_time\_maximum\_customer\_ms  |  bigint  |  Yes  |  For chat, maximum time to send a response after the customers last message.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.  | 

## Contact evaluation record
<a name="data-lake-contact-evaluation-record"></a>

**Table name:** `contact_evaluation_record`

**Description:** Stores contact evaluation data at the form, section, and question level, including scores, answers, and generative AI automation results for quality management.

**Primary key:** `evaluation_id, item_reference_id, instance_id`

**Partition key:** `initiation_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Lens, Contact Flow Events
+ `user_id` — Joins to Agent Statistic Record, Agent Queue Statistic Record, Agent Event, users
+ `evaluator_id` — Joins to Agent Statistic Record, Agent Event, users (as `user_id`)
+ `queue_id` — Joins to Contact Record, Contact Statistic Record, Agent Queue Statistic Record


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
|  aws\_account\_id  |  string  |  Yes  |  The ID of the AWS account that owns the contact.  | 
|  instance\_id  |  string  |  No  |  The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.  | 
|  evaluation\_id  |  string  |  No  |  primary key, ID of the evaluation to disambiguate multiple evaluations done of the call with the same form (by different evaluators).  | 
|  item\_reference\_id  |  string  |  No  |  primary key - might represent form/ section/ sub-section/ question depending on type.  | 
|  item\_type  |  string  |  Yes  |  Defines "Form/Section/sub-section/question or indicates a deleted record.  | 
|  contact\_id  |  string  |  Yes  |  The ID of the contact being evaluated.  | 
|  evaluation\_submitted\_timestamp  |  Timestamp  |  Yes  |  Timestamp when contact was evaluated.  | 
|  score  |  double  |  Yes  |  Score in percentage value for forms/sections/questions.  | 
|  weighted\_score  |  double  |  Yes  |  Score adding up to 100% of form, for example, 2 sections - one of 80, other out of 20.  | 
|  automatic\_fail  |  Boolean  |  Yes  |  Boolean to indicate if automatic fail was applied.  | 
|  evaluator\_id  |  string  |  Yes  |  user\_ID of evaluator.  | 
|  numeric\_answer  |  double  |  Yes  |  Value for question where answer type is numeric.  | 
|  answer\_reference\_id  |  string  |  Yes  |  for single select answer type.  | 
|  to\_delete  |  Boolean  |  Yes  |  Set to true if Form/Section/sub-section/question was deleted.  | 
|  disconnect\_timestamp  |  Timestamp  |  Yes  |  The contact disconnect Timestamp.  | 
|  initiation\_timestamp  |  Timestamp  |  Yes  |  The contact initiation Timestamp.  | 
|  user\_id  |  string  |  Yes  |  The user\_id of person being evaluated.  | 
|  queue\_id  |  string  |  Yes  |  The queue\_id of queue which contact was handled from.  | 
|  channel  |  string  |  Yes  |  The method used to contact your contact center: VOICE, CHAT, TASK, EMAIL.  | 
|  contact\_aggregation\_timestamp  |  Timestamp  |  Yes  |  Timestamp used for building aggregated agent, queue and weekly aggregation tables.  | 
|  evaluated\_contact\_with\_status  |  string  |  Yes  |  The connection status of the evaluated contact at the time of evaluation. Valid Values: disconnected \| notDisconnected. disconnected indicates the evaluated contact had ended (a disconnect timestamp exists). notDisconnected indicates the evaluated contact was still active at the time of evaluation (no disconnect timestamp).  | 
|  evaluation\_source  |  string  |  Yes  |  Indicates the origin of the evaluation process. This field indicates whether the evaluation was performed manually, with the assistance of automation or entirely automatically (without human review before submission). Assistance of automation encompasses pre-configured automation to answer a question (for example, auto-filling an answer based on a conversational analytics category) or asking AI for assistance while evaluating the contact.  | 
|  resubmitted  |  Boolean  |  Yes  |  Indicates whether the evaluation has been resubmitted. This field helps quickly identify evaluations which were resubmitted to perform audits of the evaluation process.  | 
|  evaluation\_type  |  string  |  Yes  |  Helps distinguish between different types of evaluations, such as standard evaluations and calibration evaluations. This provides the ability to only include relevant types of evaluations while performing analysis, for example, only standard evaluations should be used to calculate the aggregated score of an agent.  | 
|  calibration\_session\_id  |  string  |  Yes  |  Holds a unique identifier for a calibration session. This field is essential for identifying evaluations associated with a calibration session.  | 
|  item\_title  |  string  |  Yes  |  Column captures the title of the form item. This can be a form, section, subsection or question title depending on item\_type.  | 
|  form\_version  |  string  |  Yes  |  Indicates the version number of the evaluation form used. This field helps identify different versions of the evaluation form for analysis and reporting. | 
|  acknowledgement\_status  |  string  |  Yes  |  Acknowledgement status of the evaluation. Valid values: ACKNOWLEDGED\|UNACKNOWLEDGED  | 
|  acknowledger\_id  |  string  |  Yes  |  user\_id of the person who acknowledged the evaluation.  | 
|  evaluation\_acknowledged\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the evaluation was acknowledged.  | 
|  acknowledger\_comment  |  string  |  Yes  |  Comment left by the user who acknowledged the evaluation.  | 
|  item\_disabled  |  Boolean  |  Yes  |  The itemDisabled column indicates whether the item is in the disabled state at the time of submission from a condition defined in the evaluation form.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.  | 
|  multi\_select\_answer\_reference\_ids  |  array(string)  |  Yes  |  Value for question where answer type is multi-select.  | 
|  date\_time\_answer  |  Timestamp  |  Yes  |  Value for question where answer type is dateTime.  | 
|  evaluated\_participant\_role  |  string  |  Yes  |  The role of the evaluated contact participant.  | 
|  evaluated\_participant\_id  |  string  |  Yes  |  The ID of the evaluated contact participant.  | 
|  is\_sampled  |  Boolean  |  Yes  |  Whether the evaluation was created by a sampling job.  | 
|  is\_reviewed  |  Boolean  |  Yes  |  Indicates that the evaluation was reviewed.  | 
|  automation\_gen\_ai\_text\_answer  |  string  |  Yes  |  The generative AI-generated answer for an evaluation question where the answer type is text.  | 
|  automation\_gen\_ai\_answer\_reference\_id  |  string  |  Yes  |  The reference ID of the generative AI-generated answer for an evaluation question where the answer type is single select.  | 
|  automation\_gen\_ai\_answer\_justification  |  string  |  Yes  |  The justification provided by generative AI for its automated evaluation answer.  | 
|  is\_automation\_answer\_accepted  |  Boolean  |  Yes  |  Indicates whether the generative AI-generated answer was accepted and used as the final answer for the evaluation question.  | 
|  earned\_points  |  bigint  |  Yes  |  The total points earned for a question, section, or form.  | 
|  max\_base\_point  |  bigint  |  Yes  |  The maximum base points that can be earned for a question, section, or form, excluding bonus points.  | 
|  performance\_category  |  string  |  Yes  |  The performance category for a question, section, or form. Valid values: NEEDS\_IMPROVEMENT \| EXCEEDS\_EXPECTATION.  | 