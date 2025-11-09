# Reading from Mailchimp

entities

**Prerequisites**

A Mailchimp Object you would like to read from. Refer the supported entities table
below to check the available entities.

**Supported entities**

- [Abuse-reports](https://mailchimp.com/developer/marketing/api/campaign-abuse/ "https://mailchimp.com/developer/marketing/api/campaign-abuse/")
- [Automation](https://mailchimp.com/developer/marketing/api/automation/list-automations/ "https://mailchimp.com/developer/marketing/api/automation/list-automations/")
- [Campaigns](https://mailchimp.com/developer/marketing/api/campaigns/list-campaigns/ "https://mailchimp.com/developer/marketing/api/campaigns/list-campaigns/")
- [Click-details](https://mailchimp.com/developer/marketing/api/link-clickers/ "https://mailchimp.com/developer/marketing/api/link-clickers/")
- [Lists](https://mailchimp.com/developer/marketing/api/link-clickers/ "https://mailchimp.com/developer/marketing/api/link-clickers/")
- [Members](https://mailchimp.com/developer/marketing/api/list-segment-members/ "https://mailchimp.com/developer/marketing/api/list-segment-members/")
- [Open-details](https://mailchimp.com/developer/marketing/api/list-members/ "https://mailchimp.com/developer/marketing/api/list-members/")
- [Segments](https://mailchimp.com/developer/marketing/api/list-segments/ "https://mailchimp.com/developer/marketing/api/list-segments/")
- [Stores](https://mailchimp.com/developer/marketing/api/ecommerce-stores/list-stores/ "https://mailchimp.com/developer/marketing/api/ecommerce-stores/list-stores/")
- [Unsubscribed](https://mailchimp.com/developer/marketing/api/unsub-reports/ "https://mailchimp.com/developer/marketing/api/unsub-reports/")

| Entity              | Can be Filtered | Supports Limit | Supports Order By | Supports Select \* | Supports Partitioning |
| ------------------- | --------------- | -------------- | ----------------- | ------------------ | --------------------- |
| Automation          | Yes             | Yes            | Yes               | Yes                | Yes                   |
| Campaigns           | No              | No             | No                | No                 | No                    |
| Lists               | Yes             | Yes            | No                | Yes                | Yes                   |
| Reports Abuse       | No              | Yes            | No                | Yes                | Yes                   |
| Reports Open        | No              | Yes            | No                | Yes                | Yes                   |
| Reports Click       | Yes             | Yes            | No                | Yes                | Yes                   |
| Reports Unsubscribe | No              | Yes            | No                | Yes                | Yes                   |
| Segment             | No              | Yes            | No                | Yes                | Yes                   |
| Segment Members     | Yes             | Yes            | No                | Yes                | No                    |
| Stores              | Yes             | Yes            | Yes               | Yes                | No                    |

**Example**

```
mailchimp_read = glueContext.create_dynamic_frame.from_options(
            connection_type="mailchimp",
            connection_options={
                  "connectionName": "connectionName",
                  "ENTITY_NAME": "stores",
"INSTANCE_URL": "https://us14.api.mailchimp.com",
                  "API_VERSION": "3.0"
               })
```

**Mailchimp entity and field details**

- [Abuse-reports](https://mailchimp.com/developer/marketing/api/campaign-abuse/ "https://mailchimp.com/developer/marketing/api/campaign-abuse/")
- [Automation](https://mailchimp.com/developer/marketing/api/automation/list-automations/ "https://mailchimp.com/developer/marketing/api/automation/list-automations/")
- [Campaigns](https://mailchimp.com/developer/marketing/api/campaigns/list-campaigns/ "https://mailchimp.com/developer/marketing/api/campaigns/list-campaigns/")
- [Click-details](https://mailchimp.com/developer/marketing/api/link-clickers/ "https://mailchimp.com/developer/marketing/api/link-clickers/")
- [Lists](https://mailchimp.com/developer/marketing/api/link-clickers/ "https://mailchimp.com/developer/marketing/api/link-clickers/")
- [Members](https://mailchimp.com/developer/marketing/api/list-segment-members/ "https://mailchimp.com/developer/marketing/api/list-segment-members/")
- [Open-details](https://mailchimp.com/developer/marketing/api/list-members/ "https://mailchimp.com/developer/marketing/api/list-members/")
- [Segments](https://mailchimp.com/developer/marketing/api/list-segments/ "https://mailchimp.com/developer/marketing/api/list-segments/")
- [Stores](https://mailchimp.com/developer/marketing/api/ecommerce-stores/list-stores/ "https://mailchimp.com/developer/marketing/api/ecommerce-stores/list-stores/")
- [Unsubscribed](https://mailchimp.com/developer/marketing/api/unsub-reports/ "https://mailchimp.com/developer/marketing/api/unsub-reports/")

## Partitioning queries

You can provide the additional Spark options `PARTITION_FIELD`, `LOWER_BOUND`, `UPPER_BOUND`, and `NUM_PARTITIONS` if you want to utilize concurrency in Spark. With these parameters, the original query would be split into `NUM_PARTITIONS` number of sub-queries that can be executed by Spark tasks concurrently.

- `PARTITION_FIELD`: the name of the field to be used to partition the query.
- `LOWER_BOUND`: an **inclusive** lower bound value of the chosen partition field.

For the DateTime field, we accept the value in ISO format.

Example of valid value:

```
"2024-07-01T00:00:00.000Z"
```

- `UPPER_BOUND`: an **exclusive** upper bound value of the chosen partition field.
- `NUM_PARTITIONS`: the number of partitions.

The following table describes the entity partitioning field support details:

| Entity name | Partitioning fields | Data type |
| ----------- | ------------------- | --------- |
|             |                     |           |
|             |                     |
|             |                     |           |

Example:

```
read_read = glueContext.create_dynamic_frame.from_options(
    connection_type="mailchimp",
    connection_options={
        "connectionName": "connectionName",
        "ENTITY_NAME": "automations",
        "API_VERSION": "3.0",
        "INSTANCE_URL": "https://us14.api.mailchimp.com",
        "PARTITION_FIELD": "create_time",
        "LOWER_BOUND": "2024-02-05T14:09:30.115Z",
        "UPPER_BOUND": "2024-06-07T13:30:00.134Z",
        "NUM_PARTITIONS": "3"
    }
```
