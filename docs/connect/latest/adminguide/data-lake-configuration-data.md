# Configuration data in the Amazon Connect

analytics data lake

This topic details the content in the Amazon Connect analytics data lake configuration
tables. The tables list the column, type, and description of the content.

There are two ways to access the analytics data lake and configure data to be
shared:

- [Option 1: Use the Amazon Connect
  console](access-datalake.md#option1-configure-data-to-be-shared "access-datalake.md#option1-configure-data-to-be-shared")
- [Option 2: Use CLI or
  CloudShell](access-datalake.md#option2-configure-data-to-be-shared "access-datalake.md#option2-configure-data-to-be-shared")
  If you are unable to access the scheduling tables by using Option 1, try using
  Option 2.

###### Contents

- [Agent Hierarchy Groups](#agent-hierarchy-groups "#agent-hierarchy-groups")
- [Routing profiles](#data-lake-routing-profiles "#data-lake-routing-profiles")
- [Users](#data-lake-users "#data-lake-users")

## Agent Hierarchy Groups

Table Name: agent_hierarchy_groups

Composite Primary Key: agent_hierarchy_group_id

| Column                             | Type      | Description                                                                                                                                                                                          |
| ---------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| instance_id                        | string    | The ID of the Amazon Connect instance.                                                                                                                                                               |
| instance_arn                       | string    | The ARN of the Amazon Connect instance.                                                                                                                                                              |
| aws_account_id                     | string    | The ID of the AWS account that owns the contact.                                                                                                                                                     |
| agent_hierarchy_group_id           | string    | The identifier of the hierarchy group for the user.                                                                                                                                                  |
| agent_hierarchy_group_arn          | string    | The ARN of the hierarchy group.                                                                                                                                                                      |
| agent_hierarchy_group_name         | string    | The name of the hierarchy group.                                                                                                                                                                     |
| last_modified_region               | string    | The AWS Region where this resource was last<br>modified.                                                                                                                                             |
| last_modified_timestamp            | timestamp | The Timestamp when this resource was last modified.                                                                                                                                                  |
| data_lake_last_processed_timestamp | Timestamp | Timestamp, which shows the last time the record was touched<br>by the data lake. This can include transformation and backfill.<br>This field cannot be used to determine reliably data<br>freshness. |

## Routing profiles

Table Name: routing_profiles

Composite Primary Key: agent_routing_profile_id

| Column                             | Type      | Description                                                                                                                                                                                          |
| ---------------------------------- | --------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| agent_routing_profile_id           | string    | The identifier of the routing profile.                                                                                                                                                               |
| agent_routing_profile_arn          | string    | The ARN of the routing profile.                                                                                                                                                                      |
| routing_profile_name               | string    | The name of the routing profile.                                                                                                                                                                     |
| instance_id                        | string    | The ID of the Amazon Connect instance.                                                                                                                                                               |
| instance_arn                       | string    | The ARN of the Amazon Connect instance.                                                                                                                                                              |
| agent_availability_timer           | string    | Whether agents with this routing profile will have their<br>routing order calculated based on *longest idle<br>time<br>• or *time since their last inbound<br>contact\*.                             |
| default_outbound_queue_id          | string    | The default outbound queue for the routing profile.                                                                                                                                                  |
| routing_profile_description        | string    | Description of the routing profile.                                                                                                                                                                  |
| last_modified_region               | string    | The AWS Region where this resource was last modified.                                                                                                                                                |
| last_modified_timestamp            | Timestamp | The Timestamp when this resource was last modified.                                                                                                                                                  |
| is_active                          | Boolean   | Whether the agent exists or has been deleted.                                                                                                                                                        |
| data_lake_last_processed_timestamp | Timestamp | Timestamp, which shows the last time the record was touched<br>by the data lake. This can include transformation and backfill.<br>This field cannot be used to determine reliably data<br>freshness. |

## Users

Table Name: users

Composite Primary Key: user_id

| Column                             | Type          | Description                                                                                                                                                                                          |
| ---------------------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| user_id                            | string        | The identifier of the user account.                                                                                                                                                                  |
| user_arn                           | string        | The ARN of the user account.                                                                                                                                                                         |
| directory_user_id                  | string        | The identifier of the user account in the directory used for<br>identity management.                                                                                                                 |
| agent_hierarchy_group_id           | string        | The identifier of the hierarchy group for the user.                                                                                                                                                  |
| agent_hierarchy_group_arn          | string        | The identifier of level 1 hierarchy group for the<br>user.                                                                                                                                           |
| agent_hierarchy_group_level_1_id   | string        | The identifier of level 1 hierarchy group for the user.                                                                                                                                              |
| agent_hierarchy_group_level_2_id   | string        | The identifier of level 2 hierarchy group for the user.                                                                                                                                              |
| agent_hierarchy_group_level_3_id   | string        | The identifier of level 3 hierarchy group for the user.                                                                                                                                              |
| agent_hierarchy_group_level_4_id   | string        | The identifier of level 4 hierarchy group for the user.                                                                                                                                              |
| agent_hierarchy_group_level_5_id   | string        | The identifier of level 5 hierarchy group for the user.                                                                                                                                              |
| agent_email                        | string        | The user's email address.                                                                                                                                                                            |
| agent_secondary_email              | string        | The user's secondary email address.                                                                                                                                                                  |
| first_name                         | string        | The first name of the agent.                                                                                                                                                                         |
| last_name                          | string        | The last name of the agent.                                                                                                                                                                          |
| mobile                             | string        | The user's mobile number.                                                                                                                                                                            |
| agent_username                     | string        | The user name of the agent, as entered in their Amazon Connect user<br>account.                                                                                                                      |
| instance_id                        | string        | The ID of the Amazon Connect instance.                                                                                                                                                               |
| instance_arn                       | string        | The ARN of the Amazon Connect instance.                                                                                                                                                              |
| agent_routing_profile_id           | string        | The ID of the routing profile for the agent.                                                                                                                                                         |
| agent_routing_profile_arn          | string        | The ARN of the routing profile for the agent.                                                                                                                                                        |
| agent_security_profile_ids         | array<string> | The IDs of the security profiles for the user.                                                                                                                                                       |
| agent_security_profile_arns        | array<string> | The ARNs of the security profiles for the user.                                                                                                                                                      |
| last_modified_region               | string        | The AWS Region where this resource was last modified.                                                                                                                                                |
| last_modified_timestamp            | Timestamp     | The Timestamp when this resource was last modified.                                                                                                                                                  |
| after_contact_work_time_limit      | int           | The After Call Work (ACW) timeout setting, in seconds.                                                                                                                                               |
| auto_accept                        | Boolean       | The Auto accept setting.                                                                                                                                                                             |
| desk_phone_number                  | string        | The phone number for the user's desk phone.                                                                                                                                                          |
| phone_type                         | string        | The phone type.                                                                                                                                                                                      |
| is_active                          | Boolean       | Whether the agent exists or has been deleted.                                                                                                                                                        |
| data_lake_last_processed_timestamp | Timestamp     | Timestamp, which shows the last time the record was touched<br>by the data lake. This can include transformation and backfill.<br>This field cannot be used to determine reliably data<br>freshness. |
