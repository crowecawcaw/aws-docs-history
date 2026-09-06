

# Resource tags data in the Connect Customer data lake
<a name="data-lake-resource-tags-data"></a>

The following table contains resource tag data.

## Resource tags
<a name="data-lake-resource-tags"></a>

**Table name:** `amazon_connect_resource_tags`

**Description:** Tracks tag changes on Connect resources using a slowly changing dimension (SCD) pattern. Each tag modification creates a new record, enabling tag history analysis.

**Primary key:** `instance_id, aws_account_id, resource_arn, record_creation_timestamp`

**Partition key:** `record_creation_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `resource_arn` — Joins to any Connect resource ARN (agents, queues, flows, and so on)


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  aws\_account\_id  |  string  |  No  |  The ID of the AWS account that owns the resource.  | 
|  instance\_arn  |  string  |  Yes  |  The ARN of the Connect Customer instance.  | 
|  record\_creation\_timestamp  |  Timestamp  |  No  |  The timestamp when tags changed on the resource.  | 
|  resource\_arn  |  string  |  No  |  The ARN of the Connect Customer resource.  | 
|  tags  |  map(string,string)  |  Yes  |  The tags associated with the Connect Customer resource.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  The timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness.  | 