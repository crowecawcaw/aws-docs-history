# Scheduling the maintenance window for an Amazon MQ broker

Periodically, Amazon MQ performs maintenance to the hardware, operating system,
or the engine software of a message broker during the maintenance window.
For example, if you changed the broker instance type, Amazon MQ will apply your changes
during the next scheduled maintenance window.
The duration of the maintenance can last up to two hours depending on the operations
that are scheduled for your message broker.
You can minimize downtime during a maintenance window by selecting a broker
deployment mode with high availability across multiple Availability Zones (AZ).

Amazon MQ for ActiveMQ provides [active/standby](amazon-mq-broker-architecture.md#active-standby-broker-deployment "amazon-mq-broker-architecture.md#active-standby-broker-deployment")
deployments for high availability.
In active/standby mode, Amazon MQ performs maintenance operations one instance at a time,
and at least one instance remains available.
In addition, you can configure a [network of brokers](network-of-brokers.md "network-of-brokers.md")
with maintenance windows varied across the week.
Amazon MQ for RabbitMQ provides the [cluster](rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-cluster "rabbitmq-broker-architecture.md#rabbitmq-broker-architecture-cluster")
deployments for high availability.
In cluster deployments, Amazon MQ performs maintenance operations
one node at a time by keeping at least two running nodes at all times.

When you first create your broker, you can schedule the maintenance window
to occur once a week at a specified time.
You can only adjust the maintenance window of a broker up to four times
before the next scheduled maintenance window.
Once a broker maintenance window is completed, Amazon MQ resets the limit,
and you can adjust the schedule again before the next maintenance window occurs.
Broker availability is not affected when adjusting the broker maintenance window.

To adjust the broker maintenance window,
you can use the AWS Management Console, the AWS CLI, or the Amazon MQ API.

###### To adjust the broker maintenance window by using the AWS Management Console

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. In the left navigation pane, choose **Brokers**,
   and then choose the broker that you want to upgrade from the list.
3. On the broker details page, choose **Edit**.
4. Under **Maintenance**, do the following.
   1. For **Start day**, choose a day of the week, for example, **Sunday**,
      from the drop-down list.
   2. For **Start time**, choose the hour and minute of the day that you want to schedule for the next
      broker maintenance window, for example, **12**:**00**.

   ###### Note

   The **Start time** options are configured in UTC+0 time zone.

5. Next, select **Schedule modifications**.
   Then choose **After the next reboot** or **Immediately**.
   Choosing **After the next reboot** will immediately update the maintenance
   window without rebooting the broker. Choosing **Immediately**
   will immediately reboot the broker.
6. On the broker details page, under **Maintenance window**, verify that your new preferred schedule is displayed.

###### To adjust the broker maintenance window using the AWS CLI

1. Use the [update-broker](../../../cli/latest/reference/mq/update-broker.md "../../../cli/latest/reference/mq/update-broker.md") CLI command
   and specify the following parameters, as shown in the example.
   - `--broker-id` – The unique ID that Amazon MQ generates for the broker.
     You can parse the ID from your broker ARN. For example, given the following ARN,
     `arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`, the broker ID would be `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`.
   - `--maintenance-window-start-time` – The parameters that determine the weekly maintenance window start time provided in the following structure.
     - `DayOfWeek` – The day of the week, in the following syntax:
       `MONDAY| TUESDAY | WEDNESDAY | THURSDAY | FRIDAY | SATURDAY | SUNDAY`
     - `TimeOfDay` – The time, in 24-hour format.
     - `TimeZone` – (Optional) The time zone, in either the Country/City, or the UTC offset format. Set to UTC by default.

```
aws mq update-broker --broker-id `broker-id` \
--maintenance-window-start-time DayOfWeek=`SUNDAY`,TimeOfDay=`13:00`,TimeZone=`America/Los_Angeles`
```

2. (Optional) Use the [describe-broker](../../../cli/latest/reference/mq/reboot-broker.md "../../../cli/latest/reference/mq/reboot-broker.md") CLI command to
   verify that the maintenance window is successfully updated.

```
aws mq describe-broker --broker-id `broker-id`
```

###### To adjust the broker maintenance window using the Amazon MQ API

1. Use the [UpdateBroker](../api-reference/brokers-broker-id.md#UpdateBroker "../api-reference/brokers-broker-id.md#UpdateBroker") API operation.
   Specify `broker-id` as a path parameter. The following examples assumes a broker in the `us-west-2` region. For more information
   about available Amazon MQ endpoints, see [Amazon MQ endpoints and quotas](../../../general/latest/gr/amazon-mq.md#amazon-mq_region "../../../general/latest/gr/amazon-mq.md#amazon-mq_region")
   in the _AWS General Reference_.

```
PUT /v1/brokers/`broker-id` HTTP/1.1
Host: mq.us-west-2.amazonaws.com
Date: Wed, 7 July 2021 12:00:00 GMT
x-amz-date: Wed, 7 July 2021 12:00:00 GMT
Authorization: `authorization-string`
```

Use the `maintenanceWindowStartTime` parameter and the [`WeeklyStartTime`](../api-reference/brokers-broker-id.md#brokers-broker-id-model-weeklystarttime "../api-reference/brokers-broker-id.md#brokers-broker-id-model-weeklystarttime") resource type in the request payload.

```
{
"maintenanceWindowStartTime": {
    "dayOfWeek": `"SUNDAY"`,
    "timeZone": `"America/Los_Angeles"`,
    "timeOfDay": `"13:00"`
  }
}
```

2. (Optional) Use the [DescribeBroker](../api-reference/brokers-broker-id.md#brokers-broker-id-http-methods "../api-reference/brokers-broker-id.md#brokers-broker-id-http-methods") API
   operation to verify that the maintenance window has been successfully updated. `broker-id` is specified as
   a path parameter.

```
GET /v1/brokers/`broker-id` HTTP/1.1
Host: mq.us-west-2.amazonaws.com
Date: Wed, 7 July 2021 12:00:00 GMT
x-amz-date: Wed, 7 July 2021 12:00:00 GMT
Authorization: `authorization-string`
```
