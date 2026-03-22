# Working with RDS Proxy events

An _event_ indicates a change in an environment such as an AWS
environment or a service or application from a software as a service (SaaS) partner. Or, it
can be one of your own custom applications or services. For example, Amazon RDS
generates an event when you create or modify an RDS Proxy. Amazon RDS delivers events to
Amazon EventBridge in near-real time. Following, you can find a list of RDS Proxy events that you
can subscribe to and an example of an RDS Proxy event.

For more information about working with events, see the following:

- For instructions on how to view events by using the AWS Management Console, AWS CLI, or RDS API, see [Viewing Amazon RDS events](USER_ListEvents.md "USER_ListEvents.md").
- To learn how to configure Amazon RDS to send events to EventBridge, see [Creating a rule that triggers on an Amazon RDS event](rds-cloud-watch-events.md "rds-cloud-watch-events.md").

## RDS Proxy events

The following table shows the event category and a list of events when an RDS Proxy is the source type.

| Category             | RDS event ID   | Message                                                                                                                                                                                                                                                                               | Notes                                                                                                                                                                                                                                                 |
| -------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| configuration change | RDS-EVENT-0204 | RDS modified DB proxy `name`.                                                                                                                                                                                                                                                         | None                                                                                                                                                                                                                                                  |
| configuration change | RDS-EVENT-0207 | RDS modified the end point of the DB proxy `name`.                                                                                                                                                                                                                                    | None                                                                                                                                                                                                                                                  |
| configuration change | RDS-EVENT-0213 | RDS detected the addition of the DB instance and automatically added it to the target group of the DB proxy `name`.                                                                                                                                                                   | None                                                                                                                                                                                                                                                  |
| configuration change | RDS-EVENT-0214 | RDS detected deletion of DB instance `name` and<br>automatically removed it from target group `name`<br>of DB proxy `name`.                                                                                                                                                           | None                                                                                                                                                                                                                                                  |
| configuration change | RDS-EVENT-0215 | RDS detected deletion of DB cluster `name` and<br>automatically removed it from target group `name`<br>of DB proxy `name`.                                                                                                                                                            | None                                                                                                                                                                                                                                                  |
| creation             | RDS-EVENT-0203 | RDS created DB proxy `name`.                                                                                                                                                                                                                                                          | None                                                                                                                                                                                                                                                  |
| creation             | RDS-EVENT-0206 | RDS created endpoint `name` for DB<br>proxy `name`.                                                                                                                                                                                                                                   | None                                                                                                                                                                                                                                                  |
| deletion             | RDS-EVENT-0205 | RDS deleted DB proxy `name`.                                                                                                                                                                                                                                                          | None                                                                                                                                                                                                                                                  |
| deletion             | RDS-EVENT-0208 | RDS deleted endpoint `name` for DB proxy<br>`name`.                                                                                                                                                                                                                                   | None                                                                                                                                                                                                                                                  |
| failure              | RDS-EVENT-0243 | RDS failed to provision capacity for proxy `name`<br>because there aren't enough IP addresses available in your subnets:<br>`name`. To fix the issue, make sure that your<br>subnets have the minimum number of unused IP addresses as recommended in the<br>RDS Proxy documentation. | To determine the recommended number for your instance class, see [Planning for IP address capacity](rds-proxy-network-prereqs.md#rds-proxy-network-prereqs.plan-ip-address "rds-proxy-network-prereqs.md#rds-proxy-network-prereqs.plan-ip-address"). |
| failure              | RDS-EVENT-0275 | RDS throttled some connections to DB proxy<br>`name`. The number of simultaneous connection<br>requests from the client to the proxy has exceeded the limit.                                                                                                                          | None                                                                                                                                                                                                                                                  |

The following is an example of an RDS Proxy event in JSON format. The event shows that RDS modified the endpoint named `my-endpoint` of the RDS Proxy named `my-rds-proxy`. The event ID is RDS-EVENT-0207.

```
{
  "version": "0",
  "id": "68f6e973-1a0c-d37b-f2f2-94a7f62ffd4e",
  "detail-type": "RDS DB Proxy Event",
  "source": "aws.rds",
  "account": "123456789012",
  "time": "2018-09-27T22:36:43Z",
  "region": "us-east-1",
  "resources": [
     "arn:aws:rds:us-east-1:123456789012:db-proxy:my-rds-proxy"
  ],
  "detail": {
    "EventCategories": [
      "configuration change"
    ],
    "SourceType": "DB_PROXY",
    "SourceArn": "arn:aws:rds:us-east-1:123456789012:db-proxy:my-rds-proxy",
    "Date": "2018-09-27T22:36:43.292Z",
    "Message": "RDS modified endpoint my-endpoint of DB Proxy my-rds-proxy.",
    "SourceIdentifier": "my-endpoint",
    "EventID": "RDS-EVENT-0207"
  }
}
```
