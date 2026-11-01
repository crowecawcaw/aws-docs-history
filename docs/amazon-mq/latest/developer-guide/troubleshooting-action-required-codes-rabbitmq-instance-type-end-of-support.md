

# Amazon MQ for RabbitMQ: Instance type has reached end of support
<a name="troubleshooting-action-required-codes-rabbitmq-instance-type-end-of-support"></a>

Amazon MQ for RabbitMQ raises a `RABBITMQ_INSTANCE_TYPE_END_OF_SUPPORT` action required code when your broker is running on an instance type that has reached end of support. Support for `mq.t3.micro` ended on October 1, 2026.

Migrate your broker to a supported instance type to keep your client applications connected. You can change your broker's instance type yourself at any time, including after the broker has become unreachable.

The broker isn't deleted. Amazon MQ retains your broker configuration and message data, and doesn't bill you for the broker while it's unreachable.

**Important**  
A broker that remains on an unsupported instance type becomes unreachable. Your client applications can no longer connect to it.

## Resolving RABBITMQ\_INSTANCE\_TYPE\_END\_OF\_SUPPORT
<a name="w2aac40c43c11"></a>

The following procedure changes your broker to a supported instance type. Use it whether your broker is still reachable or has already become unreachable.

**Both steps are required**  
UpdateBroker records the instance type change but doesn't apply it. If your broker is unreachable, it remains unreachable until you complete step 2.

**To change the instance type**

1. Call [UpdateBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#UpdateBroker) with `hostInstanceType` set to a supported instance type, or change the instance type in the Amazon MQ console. For more information about supported instance types, see [RabbitMQ broker instance types](rmq-broker-instance-types.md). For console and AWS CLI procedures, see [Upgrading an Amazon MQ broker instance type](upgrading-instance-type.md).

1. Call [RebootBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id-reboot.html#RebootBroker), or choose **Actions**, **Reboot broker** in the Amazon MQ console.

1. Call [DescribeBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#DescribeBroker) until `brokerState` is `RUNNING` and `actionsRequired` no longer contains `RABBITMQ_INSTANCE_TYPE_END_OF_SUPPORT`.

### What to expect
<a name="w2aac40c43c11b9"></a>

Expect the following during the change:
+ The broker reports `CRITICAL_ACTION_REQUIRED` until the change completes, then returns to `RUNNING`.
+ The change takes several minutes. The broker is unavailable until it completes.
+ Amazon MQ retains your broker configuration and message data.
+ You can't change the broker back to `mq.t3.micro`.

**Important**  
Billing resumes when your broker returns to service, at the rate for the new instance type.

### Handling an incomplete change
<a name="w2aac40c43c11c11"></a>

If your broker doesn't return to `RUNNING`, create a case with Support. Also create a case if DescribeBroker still reports `RABBITMQ_INSTANCE_TYPE_END_OF_SUPPORT` after the reboot completes.

If you need more time before changing your instance type, create a case with Support. Support can restore connectivity to your broker temporarily so that you can retrieve your messages or complete the change.

After your broker moves to a supported instance type, Amazon MQ clears the `CRITICAL_ACTION_REQUIRED` state and your clients can connect again.