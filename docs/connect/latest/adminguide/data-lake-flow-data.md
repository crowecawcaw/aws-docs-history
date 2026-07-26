# Flow data in the Connect Customer data lake

The following tables contain flow data.

###### Contents

- [Contact flow events](#data-lake-contact-flow-events "#data-lake-contact-flow-events")
- [Connect test case execution results](#data-lake-connect-test-case-execution-results "#data-lake-connect-test-case-execution-results")

## Contact flow events

**Table name:**
`contact_flow_events`

**Description:** Records contact flow execution events, tracking flow traversal including start and end timestamps, flow outcomes, and transitions between flows and queues.

**Primary key:**
`event_id, instance_id`

**Partition key:**
`start_timestamp` (daily)

**Join keys:**

- `instance_id` — Joins to all tables
- `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Lens, Contact Evaluation Record
- `flow_resource_id` — Joins to flow configuration data
- `next_queue_resource_id` — Joins to Contact Record (as `queue_id`), Agent Queue Statistic Record (as `queue_id`)

| **Column**                             | **Type**  | **Nullable** | **Description**                                                                                                                                                                                  |
| -------------------------------------- | --------- | ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| instance\_id                           | string    | No           | The identifier of the Connect Customer instance. You can [find the instance ID](find-instance-arn.md "find-instance-arn.md") in the Amazon Resource Name (ARN)<br>of the instance.               |
| event\_id                              | string    | No           | The ID of the contact as it interacts with the flow.                                                                                                                                             |
| aws\_account\_id                       | string    | No           | The ID of the AWS account that owns the contact.                                                                                                                                                 |
| instance\_arn                          | string    | No           | The ARN of the Connect Customer instance.                                                                                                                                                        |
| contact\_id                            | string    | No           | The ID of the contact in the contact record.                                                                                                                                                     |
| flow\_resource\_id                     | string    | No           | Flow Id                                                                                                                                                                                          |
| module\_resource\_id                   | string    | No           | Module Id                                                                                                                                                                                        |
| resource\_version                      | string    | No           | Version of the contact flow used.                                                                                                                                                                |
| resource\_type                         | string    | No           | Can be flow or module.                                                                                                                                                                           |
| channel                                | string    | No           | The method used to contact your contact center: VOICE, CHAT,<br>TASK, EMAIL.                                                                                                                     |
| start\_timestamp                       | Timestamp | No           | Date and time of the start event in unix epoch, UTC                                                                                                                                              |
| end\_timestamp                         | Timestamp | No           | Date and time of the end event    in unix epoch, UTC.                                                                                                                                            |
| next\_flow\_resource\_id               | string    | No           | Next contact flow resourceId.                                                                                                                                                                    |
| next\_queue\_resource\_id              | string    | No           | Next queue resourceId.                                                                                                                                                                           |
| next\_resource\_type                   | string    | No           | It can be flow or queue.                                                                                                                                                                         |
| flow\_language\_version                | string    | No           | Flow language version.                                                                                                                                                                           |
| flow\_outcome                          | string    | No           | This will contain the system defined and custom outcomes.                                                                                                                                        |
| sub\_type                              | string    | No           | This field can be used to show channel subtype. For example,<br>connect:Guide or connect:SMS or connect:Email.                                                                                   |
| flow\_type                             | string    | No           | Connect Customer includes a set of nine flow types. For more information,<br>see [Choose a flow type](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types").    |
| initiation\_method                     | string    | No           | Every contact in your Connect Customer contact center is initiated by one<br>of the following methods: Inbound, Outbound, Transfer, Callback,<br>API, Queue Transfer, Disconnect.                |
| resource\_published\_timestamp         | Timestamp | No           | "Creation" or "revision" date of the flow<br>itself.                                                                                                                                             |
| data\_lake\_last\_processed\_timestamp | Timestamp | No           | The Timestamp, which shows the last time the data lake processed<br>the record. This can include transformation and backfill. This field<br>cannot reliably be used to determine data freshness. |

## Connect test case execution results

**Table name:**
`connect_test_case_execution_results`

**Description:** Stores test case execution results including status, outcomes, failure reasons, and associated contacts for Connect test automation.

**Primary key:**
`connect_test_case_resource_arn, connect_test_case_execution_start_timestamp, connect_test_case_execution_id`

**Partition key:**
`connect_test_case_execution_start_timestamp` (daily)

**Join keys:**

- `instance_id` — Joins to all tables
- `connect_test_case_associated_initial_contact_id` — Joins to Contact Record (as `contact_id`)
- `connect_test_case_initiating_flow_id` — Joins to Contact Flow Events (as `flow_resource_id`)

Connect Test Case Execution Results| Column | Type | Nullable | Description |
| --- | --- | --- | --- |
| instance\_id | string | Yes | The identifier of the Amazon Connect instance |
| instance\_arn | string | Yes | The ARN of the Amazon Connect instance. |
| aws\_account\_id | string | Yes | The ID of the AWS account that owns the contact. |
| connect\_test\_case\_resource\_arn | string | No | Primary Key<br>• The ARN of the Test Case. |
| connect\_test\_case\_resource\_name | string | Yes | The name of the Test Case. |
| connect\_test\_case\_execution\_start\_timestamp | timestamp | No | Primary Key<br>• The start time of simulated execution. |
| connect\_test\_case\_execution\_end\_timestamp | timestamp | Yes | The end time of simulated execution. |
| connect\_test\_case\_status | string | Yes | Current state of Test. Values: Scheduled, InProgress, Completed, Aborted, Failed |
| connect\_test\_case\_result | string | Yes | The final result of Test execution. Values: Passed, Failed, Skipped, Aborted |
| connect\_test\_case\_execution\_id | string | No | Primary Key<br>• The unique identifier for Test execution. |
| connect\_test\_case\_failure\_reasons | array(string) | Yes | The reasons for failed Test. |
| connect\_test\_case\_type | string | Yes | The type of Test executed. Values: ExperienceTest, FlowTest, BotTest |
| connect\_test\_case\_execution\_method | string | Yes | The method of starting Test execution. Values: Manual, API, Scheduled, ContactRuleTriggered, FlowPublishTriggered |
| connect\_test\_case\_execution\_channel | string | Yes | The channel of simulated interaction. Values: Chat, Voice, Campaign, Task, Email |
| connect\_test\_case\_execution\_channel\_subtype | string | Yes | The channel subtype of simulated interaction. Values: SMS, WhatsApp |
| connect\_test\_case\_associated\_initial\_contact\_id | string | Yes | Initial contact ID to start Test. |
| connect\_test\_case\_associated\_contact\_ids | array(string) | Yes | List of contact IDs created as part of Test. |
| connect\_test\_case\_initiating\_flow\_id | string | Yes | First resource ID Test Execution started with. |
| record\_creation\_timestamp | timestamp | Yes | The time of record creation |
| data\_lake\_last\_processed\_timestamp | Timestamp | Yes | The timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. |
