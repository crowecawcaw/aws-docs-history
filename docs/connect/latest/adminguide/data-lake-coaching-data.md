

# Coaching data in the Connect Customer data lake

The following table contains coaching data.

## Coaching session record
<a name="data-lake-coaching-session-record"></a>

**Table name:** `coaching_session_record`

**Description:** Stores coaching session and topic data, including lifecycle timestamps, acknowledgements, feedback, and goal outcomes.

**Primary key:** `instance_id, coaching_session_id, record_type, record_id`

**Partition key:** `session_created_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `coaching_session_id` — Joins to Coaching Session Record
+ `participant_user_id`, `coach_user_id`, `created_by_user_id`, `last_modified_by_user_id` — Join to users (as `user_id`)
+ `evaluation_form_item_reference_id`, `evaluation_form_version` — Join to Contact Evaluation Record (as `item_reference_id`, `form_version`)


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The identifier of the Connect Customer instance. You can [find the instance ID](find-instance-arn.md) in the Amazon Resource Name (ARN) of the instance.  | 
|  aws\_account\_id  |  string  |  No  |  The ID of the AWS account that owns the Connect Customer instance.  | 
|  instance\_arn  |  string  |  No  |  The Amazon Resource Name (ARN) of the Connect Customer instance.  | 
|  coaching\_session\_id  |  string  |  No  |  The unique identifier of the coaching session.  | 
|  record\_type  |  string  |  No  |  The row type. Valid values: SESSION\_PARTICIPANT, TOPIC.  | 
|  record\_id  |  string  |  No  |  The participant user ID for SESSION\_PARTICIPANT rows or the topic ID for TOPIC rows.  | 
|  to\_delete  |  Boolean  |  No  |  Indicates that the record was deleted.  | 
|  session\_created\_timestamp  |  Timestamp  |  No  |  Timestamp when the coaching session was created.  | 
|  session\_last\_modified\_timestamp  |  Timestamp  |  No  |  Timestamp when the coaching session was last modified.  | 
|  session\_title  |  string  |  Yes  |  The customer-provided title of the coaching session.  | 
|  session\_status  |  string  |  Yes  |  The session state. Valid values: SHARED, COMPLETE.  | 
|  session\_location  |  string  |  Yes  |  The customer-provided location of the coaching session.  | 
|  created\_by\_user\_id  |  string  |  Yes  |  The Connect Customer user ID of the person who created the coaching session.  | 
|  last\_modified\_by\_user\_id  |  string  |  Yes  |  The Connect Customer user ID of the person who last modified the coaching session.  | 
|  session\_scheduled\_timestamp  |  Timestamp  |  Yes  |  Timestamp scheduled for the coaching session.  | 
|  session\_due\_timestamp  |  Timestamp  |  Yes  |  Timestamp by which the coaching session is due.  | 
|  session\_shared\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the coaching session was shared with the participant.  | 
|  session\_completion\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the coach completed the coaching session.  | 
|  session\_follow\_up\_timestamp  |  Timestamp  |  Yes  |  Timestamp selected for follow-up measurement of topic metrics.  | 
|  participant\_user\_id  |  string  |  Yes  |  The Connect Customer user ID of the participant.  | 
|  participant\_acknowledgement\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the participant acknowledged the coaching session.  | 
|  participant\_acknowledgement\_comment  |  string  |  Yes  |  Comment provided when the participant acknowledged the coaching session.  | 
|  coach\_user\_id  |  string  |  Yes  |  The Connect Customer user ID of the coach assigned to the session.  | 
|  coach\_acknowledgement\_timestamp  |  Timestamp  |  Yes  |  Timestamp when the coach acknowledged the coaching session.  | 
|  coach\_acknowledgement\_comment  |  string  |  Yes  |  Comment provided when the coach acknowledged the coaching session.  | 
|  session\_feedback  |  string  |  Yes  |  The customer-provided feedback recorded for the coaching session.  | 
|  completed\_after\_due\_date  |  Boolean  |  Yes  |  Indicates whether the session was completed after session\_due\_timestamp.  | 
|  all\_goals\_status  |  string  |  Yes  |  The aggregate goal status of the coaching session. Valid values: MET, NOT\_MET. Null when the outcome cannot be determined.  | 
|  label  |  string  |  Yes  |  The customer-provided label of the coaching topic.  | 
|  topic\_source  |  string  |  Yes  |  The origin of the topic. Valid values: CUSTOM, EVALUATION\_FORM.  | 
|  topic\_type  |  string  |  Yes  |  The topic classification. Valid values: STRENGTH, OPPORTUNITY. Null when the topic is unclassified.  | 
|  scoring\_mode  |  string  |  Yes  |  The evaluation-form scoring mode for the topic. Valid values: PERCENTAGE, POINTS\_BASED.  | 
|  metric\_at\_creation  |  double  |  Yes  |  The topic metric captured when the coaching session was created.  | 
|  goal\_metric  |  double  |  Yes  |  The target metric value for the topic.  | 
|  metric\_at\_completion  |  double  |  Yes  |  The topic metric collected at session completion.  | 
|  metric\_at\_follow\_up  |  double  |  Yes  |  The topic metric collected at follow-up.  | 
|  goal\_status  |  string  |  Yes  |  The topic's goal status. Valid values: MET, NOT\_MET. Null when the outcome cannot be determined.  | 
|  evaluation\_form\_id  |  string  |  Yes  |  The ID of the evaluation form associated with the topic.  | 
|  evaluation\_form\_version  |  bigint  |  Yes  |  The version of the evaluation form associated with the topic.  | 
|  evaluation\_form\_item\_reference\_id  |  string  |  Yes  |  The hierarchical path of the evaluation-form item, including the form ID, with components separated by \|.  | 
|  evaluation\_form\_item\_title  |  string  |  Yes  |  The title of the evaluation-form item associated with the topic.  | 
|  evaluation\_form\_item\_type  |  string  |  Yes  |  The type of the referenced evaluation-form item. Valid values: QUESTION, SECTION, FORM.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  No  |  Timestamp of the last time the data lake processed the record. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.  | 

### Sample queries
<a name="data-lake-coaching-session-record-sample-queries"></a>

The following example query in Amazon Athena lists shared coaching sessions that are past due:

```
SELECT
    coaching_session_id,
    session_title,
    coach_user_id,
    participant_user_id,
    session_due_timestamp
FROM "{{coaching-session-record-resource-link-table-name}}"
WHERE instance_id = '{{instance-id}}'
    AND to_delete = false
    AND record_type = 'SESSION_PARTICIPANT'
    AND session_status = 'SHARED'
    AND session_due_timestamp < CURRENT_TIMESTAMP
ORDER BY session_due_timestamp;
```

The following example query in Amazon Athena ranks evaluation-form topics by the number of completed coaching sessions:

```
SELECT
    evaluation_form_id,
    evaluation_form_version,
    evaluation_form_item_reference_id,
    MAX(evaluation_form_item_title) AS topic_title,
    COUNT(DISTINCT coaching_session_id) AS coaching_session_count
FROM "{{coaching-session-record-resource-link-table-name}}"
WHERE instance_id = '{{instance-id}}'
    AND to_delete = false
    AND record_type = 'TOPIC'
    AND topic_source = 'EVALUATION_FORM'
    AND session_status = 'COMPLETE'
    AND session_completion_timestamp >= TIMESTAMP '{{start-date}}'
    AND session_completion_timestamp < TIMESTAMP '{{end-date}}'
GROUP BY evaluation_form_id, evaluation_form_version, evaluation_form_item_reference_id
ORDER BY coaching_session_count DESC;
```

The following example query in Amazon Athena compares topic metrics for sessions completed during a time range:

```
SELECT
    coaching_session_id,
    record_id AS topic_id,
    label,
    topic_source,
    scoring_mode,
    metric_at_creation,
    goal_metric,
    metric_at_completion,
    metric_at_follow_up,
    goal_status
FROM "{{coaching-session-record-resource-link-table-name}}"
WHERE instance_id = '{{instance-id}}'
    AND to_delete = false
    AND record_type = 'TOPIC'
    AND session_status = 'COMPLETE'
    AND session_completion_timestamp >= TIMESTAMP '{{start-date}}'
    AND session_completion_timestamp < TIMESTAMP '{{end-date}}'
ORDER BY coaching_session_id, topic_id;
```