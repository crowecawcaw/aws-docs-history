# Migrating to the Amazon Pinpoint API

After April 30, 2018, the Mobile Analytics REST API will automatically redirect requests to the Amazon Pinpoint
API. Events that your application reports to Mobile Analytics are automatically sent to Amazon Pinpoint.

## Migrating Off of the Mobile Analytics Querying API

After April 30, 2018, the Mobile Analytics Querying API will no longer be supported. Amazon Pinpoint offers an
event streams feature that lets you stream events data in real time to Amazon Kinesis Data Streams or
Amazon Data Firehose. Through a Firehose delivery stream, this data can be delivered to Amazon Redshift, Amazon S3, or
Amazon OpenSearch Service. You can then access the data and use it to calculate the KPIs that are
provided by the Querying API.

### KPI Metrics Based on Event Data

Use the following table for guidance when you're calculating KPI metrics that are based on
the event data that's streamed by Amazon Pinpoint.

| Metric                                   | Mobile Analytics KPI                                                                                                             | How to calculate with Amazon Pinpoint events                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Lifetime user count                      | `/kpis/new-users/lifetime-count`                                                                                                 | Obtain the total unique number of `client_id`<br>values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Daily active users (DAU)                 | `/kpis/dau/count`                                                                                                                | For each day, obtain the count of events that have an<br>`event_type` of `_session.start` and a<br>unique value for `client_id`.                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Monthly active users (MAU)               | `/kpis/mau/count`                                                                                                                | For each 30-day interval, obtain the count of events that have an<br>`event_type` of `_session.start` and a<br>unique value for `client_id`.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| New users                                | `/kpis/new-users/count`                                                                                                          | For each day, obtain the count of events that have an `event_type` of<br>`_session.start` and a value for<br>`client_id` that wasn't reported<br>previously.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Session count                            | `/kpis/sessions/count`                                                                                                           | For each day, obtain the count of events that have an<br>`event_type` of<br>`_session.start`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Daily revenue                            | `/kpis/daily-revenue/sum`                                                                                                        | For each day, obtain the events that have an `event_type` of<br>`_monetization.purchase`, and compute the sum of<br>the values that are reported for the `_item_price`<br>attribute.                                                                                                                                                                                                                                                                                                                                                                                                           |
| Paying daily active users (PDAU)         | `/kpis/pdau/count`                                                                                                               | For each day, calculate the DAU metric, but include only those<br>devices that have made one or more purchases in the past. A<br>purchase is indicated by an `event_type` of<br>`_monetization.purchase`.                                                                                                                                                                                                                                                                                                                                                                                      |
| Paying monthly active users (PMAU)       | `/kpis/pmau/count`                                                                                                               | For each day, calculate the MAU metric, but include only those<br>devices that have made one or more purchases in the past. A<br>purchase is indicated by an `event_type` of<br>`_monetization.purchase`.                                                                                                                                                                                                                                                                                                                                                                                      |
| Custom events count                      | `/events/`custom-event-name`/count`                                                                                              | For each day, obtain the count of events that have an `event_type` that<br>matches the name you that you assigned to the custom event.<br>Calculate max, min, and sum values by parsing the values that<br>are assigned to metrics and custom attributes.                                                                                                                                                                                                                                                                                                                                      |
| Week 1, week 2, and week 3 retention     | `/kpis/week-1-retention/count`<br>`/kpis/week-2-retention/count`<br>`/kpis/week-3-retention/count`                               | To calculate the retention for a specific day:<br>1. Obtain the original active users for that day. Active<br>users are indicated by events that have an<br>`event_type` of<br>`_session.start` and a unique value for<br>`client_id`.<br>2. Obtain the subsequent active users from the weeks that followed the day that you're<br>measuring.<br>3. Compare the original active users with the subsequent<br>active users. The retention equals the number of<br>subsequent active users that match one of the original<br>active users. Identify matches by comparing<br>`client_id` values. |
| Day 1, day 3, day 5, and day 7 retention | `/kpis/day-1-retention/count`<br>`/kpis/day-3-retention/count`<br>`/kpis/day-5-retention/count`<br>`/kpis/day-7-retention/count` | To calculate the retention for a specific day:<br>1. Obtain the original active users for that day. Active<br>users are indicated by events that have an<br>`event_type` of<br>`_session.start` and a unique value for<br>`client_id`.<br>2. Obtain the subsequent active users from the days that followed the day that you're<br>measuring.<br>3. Compare the original active users with the subsequent<br>active users. The retention equals the number of<br>subsequent active users that match one of the original<br>active users. Identify matches by comparing<br>`client_id` values.  |

### Example Events

The following examples demonstrate the JSON attributes that you can parse when you query
the data store that holds your event data.

###### Example Session Start Event

```
{
  "application_key": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
  "account_id": "111122223333",
  "event_type": "_session.start",
  "timestamp": 1517537724812,
  "arrival_timestamp": 1517537778048,
  "unique_id": "A1B2C3D4-E5F6-G7H8-I9J0-K1L2M3N4O5P6",
  "cognito_id": "us-east-1:a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6",
  "cognito_identity_pool_id": "us-east-1:a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6",
  "platform": "iOS",
  "model": "iPhone",
  "platform_version": "11.2.2",
  "make": "apple",
  "locale": "en_US",
  "sdk_version": "2.4.16",
  "sdk_name": "aws-sdk-iOS",
  "app_package_name": "com.example.package",
  "app_version_name": "11.02.0",
  "app_version_code": "28198.0",
  "user_agent": "aws-sdk-iOS/2.4.16 iOS/11.2.2 en_US",
  "app_title": "ExampleApp",
  "attributes": {
    "_clientContext": `<client context>`,
    "_session.id": "70cf4faf-BAAABA8A-20180202-021524806",
    "_session.startTime": "1517537724811"
  },
  "metrics": {}
}
```

###### Example Monetization Event

```
{
  "application_key": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
  "account_id": "111122223333",
  "event_type": "_monetization.purchase",
  "timestamp": 1517537662978,
  "arrival_timestamp": 1517537778020,
  "unique_id": "A1B2C3D4-E5F6-G7H8-I9J0-K1L2M3N4O5P6",
  "cognito_id": "us-east-1:a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6",
  "cognito_identity_pool_id": "us-east-1:a1b2c3d4-e5f6-g7h8-i9j0-k1l2m3n4o5p6",
  "platform": "iOS",
  "model": "iPhone",
  "platform_version": "11.2.5",
  "make": "apple",
  "locale": "zh_CN",
  "sdk_version": "2.6.5",
  "sdk_name": "aws-sdk-iOS",
  "app_package_name": "com.example.package",
  "app_version_name": "5.03",
  "app_version_code": "5.03.1",
  "user_agent": "aws-sdk-iOS/2.6.5 iOS/11.2.5 zh_CN",
  "app_title": "ExampleApp",
  "attributes": {
    "_currency": "CNY",
    "_product_id": "product_id",
    "_transaction_id": "123456789012345",
    "_clientContext": `<client context>`,
    "_session.duration": "152021",
    "_session.id": "e79da94c-9BD1DF63-20180202-021345277",
    "_session.startTime": "1517537625277",
    "_item_price_formatted": "¥128.00"
  },
  "metrics": {
    "_item_price": 76.5811965811966,
    "_quantity": 1.0
  }
}
```

In these examples, `<client context>` is the
`x-amz-client-context` request header that you provide when you
submit a `PutEvents` request to the Mobile Analytics REST API. For more information,
see [PutEvents](PutEvents.md "PutEvents.md").
