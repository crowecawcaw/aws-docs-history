

# Configuration data in the Connect Customer data lake
<a name="data-lake-configuration-data"></a>

This topic details the content in the Connect Customer data lake configuration tables. The tables list the column, type, and description of the content.

There are two ways to access the analytics data lake and configure data to be shared: 
+ [Option 1: Use the Connect Customer console](access-datalake.md#option1-configure-data-to-be-shared)
+ [Option 2: Use CLI or CloudShell](access-datalake.md#option2-configure-data-to-be-shared)

If you are unable to access the scheduling tables by using Option 1, try using Option 2.

**Topics**
+ [Agent Hierarchy Groups](#agent-hierarchy-groups)
+ [Routing profiles](#data-lake-routing-profiles)
+ [Users](#data-lake-users)

## Agent Hierarchy Groups
<a name="agent-hierarchy-groups"></a>

**Table name:** `agent_hierarchy_groups`

**Description:** Dimension table containing the hierarchy group definitions for organizing agents, including group names, ARNs, and active status.

**Primary key:** `agent_hierarchy_group_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `agent_hierarchy_group_id` — Joins to users table, Agent Statistic Record and Agent Queue Statistic Record (as `agent_hierarchy_level_*_id`)


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
| instance\_id | string |  Yes  | The ID of the Connect Customer instance. | 
| instance\_arn | string |  Yes  | The ARN of the Connect Customer instance. | 
| aws\_account\_id | string |  Yes  | The ID of the AWS account that owns the contact. | 
| agent\_hierarchy\_group\_id | string |  No  | The identifier of the hierarchy group for the user. | 
| agent\_hierarchy\_group\_arn | string |  Yes  | The ARN of the hierarchy group. | 
| agent\_hierarchy\_group\_name | string |  Yes  | The name of the hierarchy group. | 
| last\_modified\_region | string |  Yes  | The AWS Region where this resource was last modified. | 
| last\_modified\_timestamp | timestamp |  Yes  | The Timestamp when this resource was last modified. | 
|  is\_active  |  Boolean  |  Yes  |  Whether the agent hierarchy group exists or has been deleted.  | 
|  data\_lake\_last\_processed\_timestamp |  Timestamp  |  Yes  |  Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness. | 

## Routing profiles
<a name="data-lake-routing-profiles"></a>

**Table name:** `routing_profiles`

**Description:** Dimension table containing routing profile configurations, including profile name, default outbound queue, and availability timer settings.

**Primary key:** `agent_routing_profile_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `agent_routing_profile_id` — Joins to users table, Agent Statistic Record and Agent Queue Statistic Record (as `routing_profile_id`)


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  agent\_routing\_profile\_id  |  string  |  No  |  The identifier of the routing profile.  | 
|  agent\_routing\_profile\_arn  |  string  |  Yes  |  The ARN of the routing profile.  | 
|  routing\_profile\_name  |  string  |  Yes  |  The name of the routing profile.  | 
|  instance\_id  |  string  |  Yes  |  The ID of the Connect Customer instance.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  agent\_availability\_timer  |  string  |  Yes  |  Whether agents with this routing profile will have their routing order calculated based on longest idle time or time since their last inbound contact.  | 
|  default\_outbound\_queue\_id  |  string  |  Yes  |  The default outbound queue for the routing profile.  | 
|  routing\_profile\_description  |  string  |  Yes  |  Description of the routing profile.  | 
|  last\_modified\_region  |  string  |  Yes  |  The AWS Region where this resource was last modified.  | 
|  last\_modified\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when this resource was last modified.  | 
|  is\_active  |  Boolean  |  Yes  |  Whether the agent exists or has been deleted.  | 
|  data\_lake\_last\_processed\_timestamp |  Timestamp  |  Yes  |  Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness. | 

## Users
<a name="data-lake-users"></a>

**Table name:** `users`

**Description:** Master dimension table for agent data containing user identity, contact information, hierarchy assignments, routing profile, security profiles, and phone configuration.

**Primary key:** `user_id`

**Join keys:**
+ `instance_id` — Joins to all tables
+ `user_id` — Joins to Contact Record (as `agent_id`), Agent Statistic Record, Agent Queue Statistic Record, Contact Evaluation Record
+ `user_arn` — Joins to Agent Event (as `agent_arn`), scheduling tables (as `agent_arn`)
+ `agent_routing_profile_id` — Joins to routing\_profiles
+ `agent_hierarchy_group_id` — Joins to agent\_hierarchy\_groups


|  Column  |  Type  |  Nullable  |  Description  | 
| --- | --- | --- | --- | 
|  user\_id  |  string  |  No  |  The identifier of the user account.  | 
|  user\_arn  |  string  |  Yes  |  The ARN of the user account.  | 
|  directory\_user\_id  |  string  |  Yes  |  The identifier of the user account in the directory used for identity management.  | 
|  agent\_hierarchy\_group\_id  |  string  |  Yes  |  The identifier of the hierarchy group for the user. | 
|  agent\_hierarchy\_group\_arn  |  string  |  Yes  |  The identifier of level 1 hierarchy group for the user. | 
|  agent\_hierarchy\_group\_level\_1\_id |  string  |  Yes  |  The identifier of level 1 hierarchy group for the user.  | 
|  agent\_hierarchy\_group\_level\_2\_id |  string  |  Yes  |  The identifier of level 2 hierarchy group for the user.  | 
| agent\_hierarchy\_group\_level\_3\_id |  string  |  Yes  |  The identifier of level 3 hierarchy group for the user.  | 
|  agent\_hierarchy\_group\_level\_4\_id  |  string  |  Yes  |  The identifier of level 4 hierarchy group for the user.  | 
|  agent\_hierarchy\_group\_level\_5\_id |  string  |  Yes  |  The identifier of level 5 hierarchy group for the user.  | 
|  agent\_email  |  string  |  Yes  |  The user's email address.  | 
|  agent\_secondary\_email  |  string  |  Yes  |  The user's secondary email address.  | 
|  first\_name  |  string  |  Yes  |  The first name of the agent.  | 
|  last\_name  |  string  |  Yes  |  The last name of the agent.  | 
|  mobile  |  string  |  Yes  |  The user's mobile number.  | 
|  agent\_username  |  string  |  Yes  |  The user name of the agent, as entered in their Connect Customer user account.  | 
|  instance\_id  |  string  |  Yes  |  The ID of the Connect Customer instance.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  agent\_routing\_profile\_id  |  string  |  Yes  |  The ID of the routing profile for the agent.  | 
|  agent\_routing\_profile\_arn  |  string  |  Yes  |  The ARN of the routing profile for the agent.  | 
|  agent\_security\_profile\_ids  |  array<string>  |  Yes  |  The IDs of the security profiles for the user.  | 
|  agent\_security\_profile\_arns  |  array<string>  |  Yes  |  The ARNs of the security profiles for the user.  | 
|  last\_modified\_region  |  string  |  Yes  |  The AWS Region where this resource was last modified.  | 
|  last\_modified\_timestamp  |  Timestamp  |  Yes  |  The Timestamp when this resource was last modified.  | 
|  after\_contact\_work\_time\_limit  |  int  |  Yes  |  The After Call Work (ACW) timeout setting, in seconds.  | 
|  auto\_accept  |  Boolean  |  Yes  |  The Auto accept setting.  | 
|  desk\_phone\_number  |  string  |  Yes  |  The phone number for the user's desk phone.  | 
|  phone\_type  |  string  |  Yes  |  The phone type.  | 
|  is\_active  |  Boolean  |  Yes  |  Whether the agent exists or has been deleted.  | 
|  data\_lake\_last\_processed\_timestamp |  Timestamp  |  Yes  |  Timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot be used to determine reliably data freshness. | 
|  agent\_voice\_enhancement\_mode  |  string  |  Yes  |  The voice enhancement mode used by the agent. Valid values: VOICE\_ISOLATION \| NOISE\_SUPPRESSION \| NONE. A value of null indicates this mode has not yet been set for this user.  | 