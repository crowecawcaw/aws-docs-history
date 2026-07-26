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

**Table name:**
`case_events`

**Description:** Records case lifecycle events (created, updated, deleted), including case metadata, status changes, template information, and custom field values for Connect Cases.

**Primary key:**
`instance_id, event_id`

**Partition key:**
`event_timestamp` (daily)

**Join keys:**

- `instance_id` — Joins to all tables
- `case_id` — Joins to case\_related\_item\_events (as `associated_case_id`)

| **Column**                             | **Type**      | **Nullable** | **Description**                                                                                                                                                                                                                 |
| -------------------------------------- | ------------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instance\_id                           | string        | No           | The ID of the Connect Customer instance.                                                                                                                                                                                        |
| aws\_account\_id                       | string        | Yes          | The ID of the AWS account that owns the case.                                                                                                                                                                                   |
| event\_id                              | string        | No           | The unique ID of the case event.                                                                                                                                                                                                |
| case\_id                               | string        | Yes          | The ID of the case.                                                                                                                                                                                                             |
| event\_timestamp                       | Timestamp     | Yes          | The timestamp when the event occurred, in UTC.                                                                                                                                                                                  |
| changed\_field\_ids                    | array(string) | Yes          | The list of field IDs that were modified in this event.                                                                                                                                                                         |
| event\_type                            | string        | Yes          | The type of event. Valid values: CASE.CREATED, CASE.UPDATED, CASE.DELETED.                                                                                                                                                      |
| performed\_by\_iam\_principal          | string        | Yes          | The IAM principal ARN of the entity that triggered the event.                                                                                                                                                                   |
| performed\_by\_user\_arn               | string        | Yes          | The ARN of the user that performed the action.                                                                                                                                                                                  |
| performed\_by\_custom\_entity          | string        | Yes          | The custom entity that performed the action.                                                                                                                                                                                    |
| cases\_domain\_arn                     | string        | Yes          | The ARN of the Connect Customer Cases domain.                                                                                                                                                                                   |
| template\_id                           | string        | Yes          | The ID of the case template used to create the case.                                                                                                                                                                            |
| template\_name                         | string        | Yes          | The name of the case template. This value is empty if the template has been deleted.                                                                                                                                            |
| last\_updated\_user                    | string        | Yes          | The last user who updated the case. This references the `last_updated_user` system field value.                                                                                                                                 |
| reference\_number                      | string        | Yes          | The human-readable reference number for the case. This references the `reference_number` system field value.                                                                                                                    |
| status                                 | string        | Yes          | The status of the case. This references the `status` system field value.                                                                                                                                                        |
| assigned\_user                         | string        | Yes          | The ARN of the user assigned to the case. This references the `assigned_user` system field value.                                                                                                                               |
| assigned\_queue                        | string        | Yes          | The ARN of the queue assigned to the case. This references the `assigned_queue` system field value.                                                                                                                             |
| case\_reason                           | string        | Yes          | The reason for opening the case. This references the `case_reason` system field value.                                                                                                                                          |
| case\_title                            | string        | Yes          | The title of the case. This references the `title` system field value.                                                                                                                                                          |
| case\_summary                          | string        | Yes          | The summary of the case. This references the `summary` system field value.                                                                                                                                                      |
| customer\_profile\_arn                 | string        | Yes          | The ARN of the customer profile associated with the case. This references the `customer_id` system field value.                                                                                                                 |
| created\_timestamp                     | Timestamp     | Yes          | The timestamp when the case was created, in UTC. This references the `created_datetime` system field value.                                                                                                                     |
| last\_updated\_timestamp               | Timestamp     | Yes          | The timestamp when the case was last updated, in UTC. This references the `last_updated_datetime` system field value.                                                                                                           |
| next\_sla\_breach\_timestamp           | Timestamp     | Yes          | The timestamp of the next SLA breach deadline, in UTC. This references the `next_sla_breach_datetime` system field value.                                                                                                       |
| last\_closed\_timestamp                | Timestamp     | Yes          | The timestamp when the case was last closed, in UTC. This references the `last_closed_datetime` system field value.                                                                                                             |
| last\_reopened\_timestamp              | Timestamp     | Yes          | The timestamp when the case was last reopened, in UTC. This references the `last_reopened_datetime` system field value.                                                                                                         |
| custom\_fields                         | array(struct) | Yes          | An array of objects containing custom field data associated with the case. Each object includes the field id, field\_name, and a type-specific value field (string\_value, double\_value, boolean\_value, or timestamp\_value). |
| data\_lake\_last\_processed\_timestamp | Timestamp     | Yes          | Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.                                          |

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

**Table name:**
`case_related_item_events`

**Description:** Records events for items related to cases, including comments, contacts, file attachments, SLA tracking, and custom related items.

**Primary key:**
`instance_id, event_id`

**Partition key:**
`event_timestamp` (daily)

**Join keys:**

- `instance_id` — Joins to all tables
- `associated_case_id` — Joins to case\_events (as `case_id`)
- `contact_id` — Joins to Contact Record

| **Column**                             | **Type**      | **Nullable** | **Description**                                                                                                                                                                                                                         |
| -------------------------------------- | ------------- | ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instance\_id                           | string        | No           | The ID of the Connect Customer instance.                                                                                                                                                                                                |
| aws\_account\_id                       | string        | Yes          | The ID of the AWS account that owns the related item.                                                                                                                                                                                   |
| event\_id                              | string        | No           | The unique ID of the related item event.                                                                                                                                                                                                |
| related\_item\_id                      | string        | Yes          | The ID of the related item.                                                                                                                                                                                                             |
| event\_timestamp                       | Timestamp     | Yes          | The timestamp when the event occurred, in UTC.                                                                                                                                                                                          |
| event\_type                            | string        | Yes          | The type of event. Valid values: CASE.RELATED\_ITEM.CREATED, CASE.RELATED\_ITEM.UPDATED, CASE.RELATED\_ITEM.DELETED.                                                                                                                    |
| performed\_by\_iam\_principal          | string        | Yes          | The IAM principal ARN of the entity that triggered the event.                                                                                                                                                                           |
| performed\_by\_user\_arn               | string        | Yes          | The ARN of the user who performed the action.                                                                                                                                                                                           |
| performed\_by\_custom\_entity          | string        | Yes          | The custom entity identifier that performed the action.                                                                                                                                                                                 |
| cases\_domain\_arn                     | string        | Yes          | The ARN of the Connect Customer Cases domain.                                                                                                                                                                                           |
| associated\_case\_id                   | string        | Yes          | The ID of the case that this related item is associated with.                                                                                                                                                                           |
| related\_item\_type                    | string        | Yes          | The type of related item. Valid values: comment, file, sla, connect, contact, custom.                                                                                                                                                   |
| created\_timestamp                     | Timestamp     | Yes          | The timestamp when the related item was created, in UTC.                                                                                                                                                                                |
| comment\_body                          | string        | Yes          | The body text of the comment.                                                                                                                                                                                                           |
| comment\_content\_type                 | string        | Yes          | The content type of the comment body. For example, Text/Plain.                                                                                                                                                                          |
| related\_case\_id                      | string        | Yes          | The ID of the related case.                                                                                                                                                                                                             |
| contact\_channel                       | string        | Yes          | The communication channel of the contact. For example, VOICE, CHAT, TASK, EMAIL.                                                                                                                                                        |
| contact\_id                            | string        | Yes          | The ID of the contact.                                                                                                                                                                                                                  |
| file\_arn                              | string        | Yes          | The ARN of the file attachment.                                                                                                                                                                                                         |
| sla\_name                              | string        | Yes          | The name of the SLA.                                                                                                                                                                                                                    |
| sla\_status                            | string        | Yes          | The current status of the SLA. For example, active, overdue, met, notmet.                                                                                                                                                               |
| sla\_target\_timestamp                 | Timestamp     | Yes          | The timestamp of the target deadline for the SLA, in UTC.                                                                                                                                                                               |
| sla\_type                              | string        | Yes          | The type of SLA metric being tracked. For example, CaseField.                                                                                                                                                                           |
| sla\_completion\_timestamp             | Timestamp     | Yes          | The timestamp when the SLA was completed, in UTC.                                                                                                                                                                                       |
| sla\_target\_field\_id                 | string        | Yes          | The ID of the field that the SLA is targeting.                                                                                                                                                                                          |
| sla\_target\_field\_values             | array(string) | Yes          | The target field values for the sla\_target\_field\_id in order for the SLA to be completed.                                                                                                                                            |
| custom\_related\_item\_fields          | array(struct) | Yes          | An array of objects containing custom field data associated with the related item. Each object includes the field id, field\_name, and a type-specific value field (string\_value, double\_value, boolean\_value, or timestamp\_value). |
| data\_lake\_last\_processed\_timestamp | Timestamp     | Yes          | Timestamp, which shows the last time the data lake processed the record. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.                                                  |
