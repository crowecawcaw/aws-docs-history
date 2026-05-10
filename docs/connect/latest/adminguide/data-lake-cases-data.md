# Cases data in the Connect Customer analytics data lake

This topic details the content in the Connect Customer data lake cases tables. The
tables list the column, type, and description of the content.

There are two ways to access the analytics data lake and configure data to be
shared:

- [Option 1: Use the Connect Customer console](access-datalake.md#option1-configure-data-to-be-shared "access-datalake.md#option1-configure-data-to-be-shared")
- [Option 2: Use CLI or CloudShell](access-datalake.md#option2-configure-data-to-be-shared "access-datalake.md#option2-configure-data-to-be-shared")
  If you are unable to access the scheduling tables by using Option 1, try using
  Option 2.

###### Contents

- [Case events](#data-lake-case-events "#data-lake-case-events")
- [Case related item events](#data-lake-case-related-item-events "#data-lake-case-related-item-events")

## Case events

Table name: `case_events`

Composite primary key: {instance_id, event_id}

| **Column**                 | **Type**      | **Description**                                                                                                                                                                                                            |
| -------------------------- | ------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instance_id                | string        | The ID of the Connect Customer instance.                                                                                                                                                                                   |
| aws_account_id             | string        | The ID of the AWS account that owns the case.                                                                                                                                                                              |
| event_id                   | string        | The unique ID of the case event.                                                                                                                                                                                           |
| case_id                    | string        | The ID of the case.                                                                                                                                                                                                        |
| event_timestamp            | Timestamp     | The timestamp when the event occurred, in UTC.                                                                                                                                                                             |
| changed_field_ids          | array(string) | The list of field IDs that were modified in this event.                                                                                                                                                                    |
| event_type                 | string        | The type of event. Valid values: CASE.CREATED, CASE.UPDATED, CASE.DELETED.                                                                                                                                                 |
| performed_by_iam_principal | string        | The IAM principal ARN of the entity that triggered the event.                                                                                                                                                              |
| performed_by_user_arn      | string        | The ARN of the user that performed the action.                                                                                                                                                                             |
| performed_by_custom_entity | string        | The custom entity that performed the action.                                                                                                                                                                               |
| cases_domain_arn           | string        | The ARN of the Connect Customer Cases domain.                                                                                                                                                                              |
| template_id                | string        | The ID of the case template used to create the case.                                                                                                                                                                       |
| template_name              | string        | The name of the case template. This value is empty if the template has been deleted.                                                                                                                                       |
| last_updated_user          | string        | The last user who updated the case. This references the `last_updated_user` system field value.                                                                                                                            |
| reference_number           | string        | The human-readable reference number for the case. This references the `reference_number` system field value.                                                                                                               |
| status                     | string        | The status of the case. This references the `status` system field value.                                                                                                                                                   |
| assigned_user              | string        | The ARN of the user assigned to the case. This references the `assigned_user` system field value.                                                                                                                          |
| assigned_queue             | string        | The ARN of the queue assigned to the case. This references the `assigned_queue` system field value.                                                                                                                        |
| case_reason                | string        | The reason for opening the case. This references the `case_reason` system field value.                                                                                                                                     |
| case_title                 | string        | The title of the case. This references the `title` system field value.                                                                                                                                                     |
| case_summary               | string        | The summary of the case. This references the `summary` system field value.                                                                                                                                                 |
| customer_profile_arn       | string        | The ARN of the customer profile associated with the case. This references the `customer_id` system field value.                                                                                                            |
| created_timestamp          | Timestamp     | The timestamp when the case was created, in UTC. This references the `created_datetime` system field value.                                                                                                                |
| last_updated_timestamp     | Timestamp     | The timestamp when the case was last updated, in UTC. This references the `last_updated_datetime` system field value.                                                                                                      |
| next_sla_breach_timestamp  | Timestamp     | The timestamp of the next SLA breach deadline, in UTC. This references the `next_sla_breach_datetime` system field value.                                                                                                  |
| last_closed_timestamp      | Timestamp     | The timestamp when the case was last closed, in UTC. This references the `last_closed_datetime` system field value.                                                                                                        |
| last_reopened_timestamp    | Timestamp     | The timestamp when the case was last reopened, in UTC. This references the `last_reopened_datetime` system field value.                                                                                                    |
| custom_fields              | array(struct) | An array of objects containing custom field data associated with the case. Each object includes the field id, field_name, and a type-specific value field (string_value, double_value, boolean_value, or timestamp_value). |

### Sample queries

The following example query in Athena creates a view that flattens custom fields from the case events table:

```
CREATE VIEW case_events_flattened AS
SELECT
    ce.event_id,
    ce.case_id,
    ce.event_timestamp,
    ce.event_type,
    ce.instance_id,
    -- ... other system fields
    -- Flattened custom fields
    cf.id AS custom_field_id,
    cf.field_name AS custom_field_name,
    CASE
        WHEN cf.string_value IS NOT NULL THEN 'string'
        WHEN cf.double_value IS NOT NULL THEN 'double'
        WHEN cf.timestamp_value IS NOT NULL THEN 'timestamp'
        WHEN cf.boolean_value IS NOT NULL THEN 'boolean'
        ELSE 'unknown'
    END AS custom_field_type,
    cf.string_value AS custom_field_string_value,
    cf.double_value AS custom_field_double_value,
    -- Cast milliseconds to timestamp
    CAST(from_unixtime(cf.timestamp_value / 1000.0) AS TIMESTAMP) AS custom_field_timestamp_value,
    cf.boolean_value AS custom_field_boolean_value
FROM "`case_events resource link table name`" ce
CROSS JOIN UNNEST(ce.custom_fields) AS t(cf)

```

The following example creates a view that returns the latest state for each case:

```
CREATE OR REPLACE VIEW latest_case_state AS
SELECT *
FROM (
    SELECT *,
        ROW_NUMBER() OVER (
            PARTITION BY case_id, instance_id
            ORDER BY event_timestamp DESC
        ) AS rn
    FROM "`case_events resource link table name`"
) t
WHERE rn = 1;
```

## Case related item events

Table name: `case_related_item_events`

Composite primary key: {instance_id, event_id}

| **Column**                 | **Type**      | **Description**                                                                                                                                                                                                                    |
| -------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instance_id                | string        | The ID of the Connect Customer instance.                                                                                                                                                                                           |
| aws_account_id             | string        | The ID of the AWS account that owns the related item.                                                                                                                                                                              |
| event_id                   | string        | The unique ID of the related item event.                                                                                                                                                                                           |
| related_item_id            | string        | The ID of the related item.                                                                                                                                                                                                        |
| event_timestamp            | Timestamp     | The timestamp when the event occurred, in UTC.                                                                                                                                                                                     |
| event_type                 | string        | The type of event. Valid values: CASE.RELATED_ITEM.CREATED, CASE.RELATED_ITEM.UPDATED, CASE.RELATED_ITEM.DELETED.                                                                                                                  |
| performed_by_iam_principal | string        | The IAM principal ARN of the entity that triggered the event.                                                                                                                                                                      |
| performed_by_user_arn      | string        | The ARN of the user who performed the action.                                                                                                                                                                                      |
| performed_by_custom_entity | string        | The custom entity identifier that performed the action.                                                                                                                                                                            |
| cases_domain_arn           | string        | The ARN of the Connect Customer Cases domain.                                                                                                                                                                                      |
| associated_case_id         | string        | The ID of the case that this related item is associated with.                                                                                                                                                                      |
| related_item_type          | string        | The type of related item. Valid values: comment, file, sla, connect, contact, custom.                                                                                                                                              |
| created_timestamp          | Timestamp     | The timestamp when the related item was created, in UTC.                                                                                                                                                                           |
| comment_body               | string        | The body text of the comment.                                                                                                                                                                                                      |
| comment_content_type       | string        | The content type of the comment body. For example, Text/Plain.                                                                                                                                                                     |
| related_case_id            | string        | The ID of the related case.                                                                                                                                                                                                        |
| contact_channel            | string        | The communication channel of the contact. For example, VOICE, CHAT, TASK, EMAIL.                                                                                                                                                   |
| contact_id                 | string        | The ID of the contact.                                                                                                                                                                                                             |
| file_arn                   | string        | The ARN of the file attachment.                                                                                                                                                                                                    |
| sla_name                   | string        | The name of the SLA.                                                                                                                                                                                                               |
| sla_status                 | string        | The current status of the SLA. For example, active, overdue, met, notmet.                                                                                                                                                          |
| sla_target_timestamp       | Timestamp     | The timestamp of the target deadline for the SLA, in UTC.                                                                                                                                                                          |
| sla_type                   | string        | The type of SLA metric being tracked. For example, CaseField.                                                                                                                                                                      |
| sla_completion_timestamp   | Timestamp     | The timestamp when the SLA was completed, in UTC.                                                                                                                                                                                  |
| sla_target_field_id        | string        | The ID of the field that the SLA is targeting.                                                                                                                                                                                     |
| sla_target_field_values    | array(string) | The target field values for the sla_target_field_id in order for the SLA to be completed.                                                                                                                                          |
| custom_related_item_fields | array(struct) | An array of objects containing custom field data associated with the related item. Each object includes the field id, field_name, and a type-specific value field (string_value, double_value, boolean_value, or timestamp_value). |
