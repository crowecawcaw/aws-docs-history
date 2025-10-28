# Upgrading an Amazon MQ broker instance type

###### Important

`mq.m7g.x` instances are only available for Amazon MQ for RabbitMQ brokers.
Amazon MQ for ActiveMQ brokers only use `mq.m5.x` instances.

The combined description of the broker instance class (`m7g`)
and size (`large`)
is called the broker instance type (for example, `mq.m7g.large`).
When choosing an instance type,
it is important to consider factors that will affect broker performance:

- the number of clients and queues
- the volume of messages sent
- messages kept in memory
- redundant messages

Smaller broker instance types (`mq.m7g.medium`) are recommended only for testing application performance.
We recommend larger broker instance types (`mq.m7g.large` and above)
for production levels of clients and queues, high throughput, messages in memory, and redundant messages.

We recommend upgrading to a larger instance type (i.e. from `micro` to `large`)
if you are experiencing performance issues, or if you are moving from testing to a production environment.
To upgrade your instance type, you can use the AWS Management Console, the AWS CLI, or the Amazon MQ API.

###### To upgrade to a larger instance type using the AWS Management Console, do the following:

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. In the left navigation pane, choose **Brokers**,
   and then choose the broker that you want to upgrade from the list.
3. On the broker details page, choose **Edit**.
4. Under **Specifications**, for **Broker instance type**
   choose the new instance type from the dropdown list.
5. At the bottom of the page, choose **Schedule modifications**.
6. On the **Schedule broker modifications** page, for **When to apply modifications**,
   choose one of the following.
   - Choose **After the next reboot**, if you want Amazon MQ to complete the upgrade
     during the next scheduled maintenance window.
   - Choose **Immediately**, if you want to reboot the broker and upgrade
     the instance type immediately.

   ###### Important

   Single instance brokers are offline while being rebooted. For cluster brokers,
   only one node is down at a time while the broker reboots.

7. Choose **Apply** to finish applying the changes.

###### To upgrade the instance type of a broker by using the AWS CLI

1. Use the [modify-broker](../../../cli/latest/reference/mq/update-broker.md "../../../cli/latest/reference/mq/update-broker.md") CLI command
   and specify the following parameters, as shown in the example.
   - `--broker-id` – The unique ID that Amazon MQ generates for the broker.
   - `--host-instance-type` – The engine version number for the broker engine to upgrade to.

```
aws mq modify-broker --broker-id `broker-id` --host-instance-type `instance-type`
```

2. (Optional) Use the [reboot-broker](../../../cli/latest/reference/mq/reboot-broker.md "../../../cli/latest/reference/mq/reboot-broker.md") CLI command to
   reboot your broker if, you want to upgrade the instance type immediately.

```
aws mq reboot-broker --broker-id `broker-id`
```

If you do not want to reboot your broker and apply the changes immediately, Amazon MQ will upgrade the broker during the next
scheduled maintenance window.

###### Important

Single instance brokers are offline while being rebooted. For cluster brokers,
only one node is down at a time while the broker reboots.

###### To upgrade the instance-type of a broker by using the Amazon MQ API

1. Use the [UpdateBroker](../api-reference/brokers-broker-id.md#UpdateBroker "../api-reference/brokers-broker-id.md#UpdateBroker") API operation. Specify `broker-id` as a
   path parameter. The following examples assumes a broker in the
   `us-west-2` region. For more information about available
   Amazon MQ endpoints, see [Amazon MQ endpoints
   and quotas](../../../general/latest/gr/amazon-mq.md#amazon-mq_region "../../../general/latest/gr/amazon-mq.md#amazon-mq_region") in the _AWS General Reference_.

```
PUT /v1/brokers/`broker-id` HTTP/1.1
Host: mq.us-west-2.amazonaws.com
Date: Mon, 7 June 2021 12:00:00 GMT
x-amz-date: Mon, 7 June 2021 12:00:00 GMT
Authorization: `authorization-string`
```

Use `host-instance-type` in the request payload to specify the instance type for the broker to upgrade to.

```
{
    "host-instance-type": "`host-instance-type`"
}
```

2. (Optional) Use the [RebootBroker](../api-reference/brokers-broker-id-reboot.md#RebootBroker "../api-reference/brokers-broker-id-reboot.md#RebootBroker") API
   operation to reboot your broker, if you want to upgrade the engine version immediately. `broker-id` is specified as
   a path parameter.

```
POST /v1/brokers/`broker-id`/reboot-broker HTTP/1.1
Host: mq.us-west-2.amazonaws.com
Date: Mon, 7 June 2021 12:00:00 GMT
x-amz-date: Mon, 7 June 2021 12:00:00 GMT
Authorization: `authorization-string`
```

If you do not want to reboot your broker and apply the changes immediately, Amazon MQ will upgrade the broker during the next
scheduled maintenance window.

###### Important

Single instance brokers are offline while being rebooted. For cluster brokers,
only one node is down at a time while the broker reboots.
