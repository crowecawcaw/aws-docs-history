

# In-place upgrade from RabbitMQ 3 to 4
<a name="upgrading-rabbitmq-v3-to-v4-inplace"></a>

 Amazon MQ supports in-place major version upgrades from RabbitMQ 3.13 to RabbitMQ 4.2. RabbitMQ 4.2 is only supported on the `mq.m7g` instance type across all supported instance sizes. 

**Note**  
If your Amazon MQ for RabbitMQ 3 broker has Khepri enabled, there is no in-place upgrade path to RabbitMQ 4. For more information, see [RabbitMQ version upgradability](https://www.rabbitmq.com/docs/upgrade#rabbitmq-version-upgradability). In this case, consider a [blue-green deployment](upgrading-rabbitmq-v3-to-v4-blue-green.md).

**Important**  
 The upgrade duration depends on queue count and queue depth. Brokers with a large number of queues and messages will experience longer downtimes. To minimize downtime, keep your queues short. 

## Step 1: Upgrade the broker instance type
<a name="upgrading-rabbitmq-v3-to-v4-inplace-step1"></a>

 RabbitMQ 4.2 requires the `mq.m7g` instance type. If your broker is already running on an `mq.m7g` instance type, move to [Step 2: Migrate classic queues to quorum queues](#upgrading-rabbitmq-v3-to-v4-inplace-step2). 

 Use the [UpdateBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#UpdateBroker) API operation to modify the broker's instance type to `mq.m7g`. 

 Reboot the broker using the [RebootBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id-reboot.html) API to apply the instance type change, or wait for the next scheduled maintenance window. 

 For more information, see [Upgrading an Amazon MQ broker instance type](upgrading-instance-type.md). 

## Step 2: Migrate classic queues to quorum queues
<a name="upgrading-rabbitmq-v3-to-v4-inplace-step2"></a>

 Classic mirrored queues are not supported in RabbitMQ 4. Amazon MQ will prevent in-place upgrades to RabbitMQ 4 if the broker has classic queues or classic mirrored queues. 

 Amazon MQ provides a queue migration tool to migrate classic queues to quorum queues. This tool is accessible through the RabbitMQ web console under **Admin** > **Queue Migration**, or through the HTTP API. 

 To use the tool see, [Amazon MQ queue migration tool](https://github.com/amazon-mq/rabbitmq-queue-migration). 

## Step 3: Upgrade the engine version from RabbitMQ 3.13 to 4.2
<a name="upgrading-rabbitmq-v3-to-v4-inplace-step3"></a>

**Note**  
Amazon MQ blocks all external traffic to the broker during the upgrade.

**Important**  
If your RabbitMQ 3.13 cluster broker uses a customer managed key (CMK) for encryption, the IAM role used to call `UpdateBroker` to upgrade to version 4.2 must have the following AWS KMS permissions on the broker's encryption key:  
`kms:CreateGrant`
`kms:DescribeKey`
If the calling role does not have these permissions, the `UpdateBroker` API returns a `403` error indicating that grant permissions are needed on the AWS KMS key. To resolve this error, add `kms:CreateGrant` and `kms:DescribeKey` permissions to the IAM role's policy for the broker's AWS KMS key ARN, then retry the upgrade.

 Use the [UpdateBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#UpdateBroker) API to set the pending engine version for the RabbitMQ 3.13 broker to 4.2. 

 Reboot the broker to apply the changes, or wait for the next scheduled maintenance window. 

## Monitoring upgrade progress
<a name="upgrading-rabbitmq-v3-to-v4-inplace-monitoring"></a>

 You can monitor the upgrade progress using the [DescribeBroker](https://docs.aws.amazon.com/amazon-mq/latest/api-reference/brokers-broker-id.html#DescribeBroker) API or the broker quarantine state on the Amazon MQ console. 

 Amazon MQ runs an upgrade eligibility check at the start of the upgrade. If it identifies classic queues or if Khepri is enabled, Amazon MQ puts the broker in `CRITICAL_ACTION_REQUIRED` state with the action required code `RABBITMQ_BROKER_NOT_UPGRADEABLE_TO_V4`. Amazon MQ will not apply the major version upgrade and will make the broker available for publishing and consuming. 

 To continue the upgrade, resolve the underlying issue. For more information, see [RABBITMQ\_BROKER\_NOT\_UPGRADEABLE\_TO\_V4](troubleshooting-action-required-codes-rabbitmq-not-upgradeable-to-v4.md). 

## Updating resource limit configuration after upgrade
<a name="upgrading-rabbitmq-v3-to-v4-inplace-resource-limits"></a>

 Amazon MQ for RabbitMQ 4 introduces [default resource limits](rabbitmq-resource-limits-configuration.md) for connections, channels, consumers per channel, queues, vhosts, shovels, exchanges, and maximum message size. On RabbitMQ 3 brokers, these resources are configured with the [maximum resource limits](rabbitmq-sizing-guidelines.md). After an in-place upgrade to RabbitMQ 4.2, Amazon MQ applies the RabbitMQ 4 default resource limits, which are lower than the maximum resource limits used in RabbitMQ 3. 

**Important**  
If your RabbitMQ 3 broker uses any resource at a count higher than the RabbitMQ 4 default limits, the broker may reject new connections, channels, or queue declarations that exceed the new limits after the upgrade. Review the [default resource limits](rabbitmq-resource-limits-configuration.md) for your instance type and deployment mode before upgrading. After the upgrade completes, update the broker configuration to adjust the resource limits to match your workload requirements. For more information, see [Resource limit configuration](configure-resource-limits.md).