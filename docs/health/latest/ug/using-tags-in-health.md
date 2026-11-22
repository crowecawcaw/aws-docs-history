

# Using tags in AWS Health

After you enable tags in AWS Health and configure your tag keys (see [Enabling tag enrichment](enabling-tag-enrichment.md)), AWS Health adds your tag values to the affected resources (and, in organizational view, affected accounts) of each event. This topic describes how to view and filter events by tag in the AWS Health Dashboard, with the AWS Health API, and with Amazon EventBridge rules.

**Before you begin**

Complete the following:
+ Turn on tags and configure up to 10 tag keys. For more information, see [Enabling tag enrichment](enabling-tag-enrichment.md).
+ Wait until each tag key shows the status of **Onboarded**. Fetching tag values can take up to 24 hours.
+ For EventBridge, make sure each tag key that you want to match is configured with `enabledForEventBridge` set to `true`. For more information, see [Monitoring events in AWS Health with Amazon EventBridge](cloudwatch-events-health.md).

The examples on this page use one Lambda function, `CheckWarehouseInventory`, with the following tags:


| Tag key | Tag value | 
| --- | --- | 
| `Dept` | `OrderFulfillment` | 
| `Env` | `DevTest` | 

Function ARN: `arn:aws:lambda:us-east-1:111122223333:function:CheckWarehouseInventory`

## Using tags in the AWS Health Dashboard
<a name="using-tags-health-dashboard"></a>

**To view tags on an event**

1. Open the AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/home).

1. Choose **Your account health** (account view) or **Your organization health** (organizational view).

1. Choose an event, such as a Lambda runtime deprecation (planned lifecycle event).

1. Choose the **Affected resources** tab. The **Tags** column shows the number of tag values for each resource. Choose the number to see the specific tag and value. For `CheckWarehouseInventory`, you see `Dept` = `OrderFulfillment` and `Env` = `DevTest`.

1. In organizational view, choose the **Affected accounts** tab to see account tags for each affected account.

You can filter events to show only resources with a specific tag value.

**To filter events by tag**

1. On any tab in the AWS Health Dashboard, choose **Search and add filter**.

1. Choose a tag key, enter a value, and then choose **Apply**. Tag keys and values are case sensitive.

The filter also applies to the **Affected resources** tab. You can add tag filters directly on the **Affected resources** tab of an event's details. If you filter on more than one tag key or value, AWS Health returns events that match any of them (OR logic).

## Using tags with the AWS Health API
<a name="using-tags-health-api"></a>

For more information about the AWS Health API, see the [AWS Health API Reference](https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html). The AWS Health API returns tags in the following operations.


| Operation | View | Tag fields returned | 
| --- | --- | --- | 
| `DescribeAffectedEntities` | Account | `resourceTags` | 
| `DescribeAffectedEntitiesForOrganization` | Organization | `resourceTags`, `accountTags` | 
| `DescribeAffectedAccountsForOrganization` | Organization | Account tags | 

The following examples use the AWS Command Line Interface (AWS CLI).

**Note**  
In the code examples, the event ARNs are truncated for readability.

**Example 1: Get affected resources with their tags (account view)**

In the following command, replace `{{resource_region}}` and the event ARN with your values:

```
aws health describe-affected-entities --region us-east-1 \
--filter eventArns=arn:aws:health:{{resource_region}}::event/LAMBDA/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT_e23fb8bb12482<truncated>
```

Each entity in the response includes `resourceTags`:

```json
{
    "entities": [
        {
            "entityArn": "arn:aws:health:eu-west-1:111122223333:entity/g1pVmlLnPUnhWV_<truncated>",
            "eventArn": "arn:aws:health:eu-west-1::event/LAMBDA/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT_e23fb8bb12482cd84e4c8501dd1022a4a2c2268a9daa8<truncated>",
            "entityValue": "arn:aws:lambda:eu-west-1:111122223333:function:CheckWarehouseInventory",
            "awsAccountId": "111122223333",
            "lastUpdatedTime": "2026-06-28T15:20:50.336000-04:00",
            "statusCode": "PENDING",
            "resourceTags": {
                "Dept": "OrderFulfillment",
                "Env": "DevTest"
            }
        }
    ]
}
```

**Example 2: Filter affected resources by tag in the request (account view)**

Use the `tags` field of the entity filter to return only resources that have a matching tag key and value:

```
aws health describe-affected-entities \
--region us-east-1 \
--filter '{
"eventArns": ["arn:aws:health:{{resource_region}}::event/LAMBDA/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT_e23fb8bb12482<truncated>"],
"tags": [ { "Dept": "OrderFulfillment" } ]
}'
```

When you combine a tag filter with filters on other fields, AWS Health returns only results that match all of them (AND logic). Conditions within the `tags` field are combined with OR. This applies to multiple values for one tag key, to multiple tag keys, or to both.

For example, a filter on an event ARN and the tag `Env=Prod` returns only resources for that event that are tagged `Env=Prod`. The following filter returns resources tagged with any of `Env=Prod`, `Env=Dev`, `Owner=Finance`, or `Owner=Marketing`:

```json
"tags": [
{ "Env": "Prod" },
{ "Env": "Dev" },
{ "Owner": "Finance" },
{ "Owner": "Marketing" }
]
```

**Example 3: Filter the response (account view)**

You can also filter on the client side with `--query`. This works with any operation that returns tags, including organizational view operations.

Show the resources that have the tags `Dept=OrderFulfillment` and `Env=DevTest` and the status `PENDING`:

```
aws health describe-affected-entities \
--region us-east-1 \
--filter '{"eventArns":["arn:aws:health:{{resource_region}}::event/LAMBDA/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT_e23fb8bb12482cd84e4c8501dd1022a4a2c2268a9daa8e3<truncated>"]}' \
--query "entities[?resourceTags.Dept=='OrderFulfillment' && resourceTags.Env=='DevTest' && statusCode=='PENDING'].[entityValue, resourceTags.Env]" \
--output table
```

**Example 4: Find resources that are missing a tag (account view)**

Find resources that are missing the `Dept` tag, so that you can fix tagging gaps:

```
aws health describe-affected-entities \
--region us-east-1 \
--filter '{"eventArns":["arn:aws:health:eu-west-1::event/LAMBDA/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT_e23fb8bb12482cd84e4c8501dd1022a4a2c2268a9daa8e3<truncated>"]}' \
--query 'entities[?!resourceTags.Dept].entityValue'
```

**Example 5: Describe affected entities at an organization level**

The output of organizational view commands includes the account tags.

```
aws health describe-affected-entities-for-organization \
--region us-east-1 \
--organization-entity-account-filters '[
{
"eventArn": "arn:aws:health:eu-west-1::event/LAMBDA/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT_e23fb8bb12482cd84e4c8501dd1022a4a2c2268a9daa8e3<truncated>",
"awsAccountId": "111122223333"
}
]'
```

Output:

```json
"entities": [
        {
            "entityArn": "arn:aws:health:us-east-1:111122223333:entity/g1RV7YLEvQj4FnfF<truncated>",
            "eventArn": "arn:aws:health:us-east-1::event/LAMBDA/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT/AWS_LAMBDA_PLANNED_LIFECYCLE_EVENT_3d7dfb980d62478ee6cde2801977a894a8236e8<truncated>",
            "entityValue": "arn:aws:lambda:us-east-1:111122223333:function:CheckWarehouseInventory",
            "awsAccountId": "111122223333",
            "lastUpdatedTime": "2026-11-17T00:00:28.764000-05:00",
            "statusCode": "RESOLVED",
            "resourceTags": {
                "Env": "DevTest"
            },
            "accountTags": {
                "AppId": "1234",
                "Environment": "Prod",
                "Jira": "PT",
                "Owner": "John Stiles"
            }
        },
```

## Using tags with Amazon EventBridge
<a name="using-tags-eventbridge"></a>

If any affected resource matches the tags, EventBridge sends the full event, including all affected resources.

**Example: EventBridge rule that matches production resources only**

The following EventBridge event pattern matches AWS Health events for resources tagged `Environment=Production`:

```json
{
"source": ["aws.health"],
"detail-type": ["AWS Health Event"],
"detail": {
"affectedEntities": {
"resourceTags": {
"Environment": ["Production"]
}
}
}
}
```

## Considerations
<a name="tags-considerations"></a>

Keep the following in mind when you use tags with AWS Health events:
+ **Tag lookup by ARN:** AWS Health uses the ARN of each affected resource to find its tags. Resources whose identifiers don't follow the standard ARN format don't have tags associated with them.
+ **Untagged resources are still returned:** Resources that don't have any of your configured tag keys are still included in API responses and events, without tag values.
+ **Only configured keys appear:** AWS Health returns only the tag keys that you configured, up to 10 keys.
+ **EventBridge is opt-in per key:** EventBridge events include only the tag keys that you set with `enabledForEventBridge` set to `true`. The AWS Health Dashboard and AWS Health API include all configured keys.
+ **Updates aren't immediate:** AWS Health refreshes tag information on a schedule. When you change a tag value, it can take up to 24 hours for the new value to appear in the AWS Health Dashboard and AWS Health API. EventBridge events sent after the refresh include the new value.
+ **Account tags are organizational view only:** Account tags are managed in Organizations, so they appear only in organizational view. In account view, you see resource tags only.
+ **Existing integrations keep working:** Tag fields are added to the existing AWS Health event response JSON data structure. Your current API calls and EventBridge rules continue to work without changes.
+ **No tags in email notifications:** Tags aren't included in email notifications.
+ **Use tagging best practices:** Use a consistent tagging strategy across your organization to get more value from your tags. For more information, see [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html).