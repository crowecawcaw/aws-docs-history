

# Customer profiles contact data in the Connect Customer data lake
<a name="data-lake-customer-profiles-contact-data"></a>

The following table contains customer profiles contact data.

**Topics**
+ [Customer profiles contact event](#data-lake-customer-profiles-contact-event)

## Customer profiles contact event
<a name="data-lake-customer-profiles-contact-event"></a>

**Table name:** `customer_profiles_contact_event`

**Description:** Contains a snapshot of Customer Profiles data for each contact at disconnect time, including calculated attribute values (orders total price value and call count) and segment memberships (lifetime value tier and repeat caller status). One record is created per contact.

**Primary key:** `instance_id, event_id`

**Partition key:** `initiation_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `contact_id` — Joins to Contact Record, Contact Statistic Record, Contact Evaluation Record, Contact Lens, Contact Flow Events, AI Agent, AI Session


|  **Column**  |  **Type**  |  **Nullable**  |  **Description**  | 
| --- | --- | --- | --- | 
|  instance\_id  |  string  |  No  |  The ID of the Connect Customer instance.  | 
|  event\_id  |  string  |  No  |  The ID of the customer profiles contact event.  | 
|  aws\_account\_id  |  string  |  No  |  The ID of the AWS account that owns the contact.  | 
|  instance\_arn  |  string  |  No  |  The ARN of the Connect Customer instance.  | 
|  contact\_id  |  string  |  No  |  The ID of the contact this snapshot is associated with.  | 
|  profile\_id  |  string  |  No  |  The Customer Profile ID associated with this contact at disconnect time.  | 
|  domain\_name  |  string  |  No  |  The Customer Profiles domain identifier.  | 
|  initiation\_timestamp  |  Timestamp  |  No  |  The contact initiation Timestamp. Used as partition key. Never changes after creation.  | 
|  disconnect\_timestamp  |  Timestamp  |  Yes  |  The contact disconnect Timestamp.  | 
|  event\_timestamp  |  Timestamp  |  No  |  Timestamp when this snapshot record was generated or last updated.  | 
|  orders\_total\_price\_sum  |  double  |  Yes  |  The sum of order values associated with the customer profile.  | 
|  call\_count  |  bigint  |  Yes  |  The number of distinct calls a customer has made in the configured time period (7 days by default, which you can update in Customer Profiles).  | 
|  lifetime\_value\_segment  |  array(string)  |  No  |  Lifetime value segment memberships at disconnect time. Possible values: \_default\_lifetime\_value\_high, \_default\_lifetime\_value\_medium, \_default\_lifetime\_value\_low.  | 
|  repeat\_caller\_segment  |  array(string)  |  No  |  Repeat caller segment memberships at disconnect time. Possible values: \_default\_repeat\_caller, \_default\_non\_repeat\_caller.  | 
|  data\_lake\_last\_processed\_timestamp  |  Timestamp  |  Yes  |  Timestamp showing the last time the data lake processed the record. Cannot reliably be used to determine data freshness.  | 

### Things to know
<a name="data-lake-customer-profiles-contact-event-things-to-know"></a>
+ One record is expected per contact at disconnect time.
+ The `initiation_timestamp` is the partition key and never changes, even if the record is updated. Use this field for efficient time range queries.
+ Segment columns (`lifetime_value_segment` and `repeat_caller_segment`) contain the segment names the customer matched at disconnect time. These are separate columns to support independent filtering and grouping in analytics.
+ Default segment thresholds for lifetime value can be customized by modifying the underlying calculated attributes in Customer Profiles.

### Sample queries
<a name="data-lake-customer-profiles-contact-event-sample-queries"></a>

The following example query in Amazon Athena returns customer profiles contact events for a specific instance:

```
SELECT
    contact_id,
    profile_id,
    orders_total_price_sum,
    call_count,
    lifetime_value_segment,
    repeat_caller_segment,
    disconnect_timestamp
FROM "{{customer-profiles-contact-event-resource-link-table-name}}"
WHERE instance_id = '{{your-instance-id}}'
    AND initiation_timestamp >= TIMESTAMP '{{start-date}}'
    AND initiation_timestamp < TIMESTAMP '{{end-date}}'
ORDER BY initiation_timestamp DESC;
```

The following example query in Amazon Athena joins customer profiles data with contact records:

```
SELECT
    cr.contact_id,
    cr.agent_username,
    cr.queue_name,
    cr.agent_interaction_duration_ms,
    cp.lifetime_value_segment,
    cp.repeat_caller_segment,
    cp.orders_total_price_sum
FROM "{{contact-record-resource-link-table-name}}" cr
JOIN "{{customer-profiles-contact-event-resource-link-table-name}}" cp
    ON cr.instance_id = cp.instance_id
    AND cr.contact_id = cp.contact_id
WHERE cr.instance_id = '{{your-instance-id}}'
    AND cr.initiation_timestamp >= TIMESTAMP '{{start-date}}'
    AND cr.initiation_timestamp < TIMESTAMP '{{end-date}}';
```

### Related topics
<a name="data-lake-customer-profiles-contact-event-related"></a>
+ [Create an evaluation form in Connect Customer](create-evaluation-forms.md)
+ [Default calculated attributes in Connect Customer Customer Profiles](customerprofiles-default-calculated-attributes.md)
+ [Default segments](https://docs.aws.amazon.com/connect/latest/adminguide/customerprofiles-default-segments.html)
+ [Enable Customer Profiles for your Connect Customer instance](enable-customer-profiles.md)