# Upgrading an Amazon MQ broker engine version

Amazon MQ regularly provides new broker engine versions for all supported broker engine types. New engine versions
include security patches, bug fixes, and other broker engine improvements.

Amazon MQ organizes version numbers according to semantic versioning specification as
`X.Y.Z`. In Amazon MQ implementations, `X` denotes the
major version, `Y` represents the minor version, and `Z` denotes the patch version number. Amazon MQ supports
two types of upgrades:

- Major version upgrade – Occurs when the
  major engine version numbers change. For example, upgrading from RabbitMQ version **3**.13 to version **4**.2 is
  considered a major version upgrade.
- Minor version upgrade – Occurs when only the
  minor engine version number changes. For example, upgrading from version 3.**11** to version 3.**12** is considered a minor version upgrade.

You can manually upgrade your broker at any time to the next supported major or minor version.
Amazon MQ manages upgrade to the latest supported patch version for all brokers during the scheduled
[maintenance window](maintaining-brokers.md "maintaining-brokers.md").
Both manual and automatic version upgrades occur during the scheduled maintenance window,
or after you [reboot your broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").
Amazon MQ upgrades your broker to the next minor version when the current minor version reaches end of support.

## Manually upgrading the engine version

You can upgrade the engine version of a broker by using the AWS Management Console, the AWS CLI, or the Amazon MQ API.

###### To upgrade the engine version of a broker by using the AWS Management Console

1. On the broker details page, choose **Edit**.
2. Under **Specifications**, for **Broker engine version**
   choose the new version number from the dropdown list.
3. Scroll to the bottom of the page, and choose **Schedule modifications**.
4. On the **Schedule broker modifications** page, for **When to apply modifications**,
   choose one of the following.
   - Choose **After the next reboot**, if you want Amazon MQ to complete the version upgrade
     during the next scheduled maintenance window.
   - Choose **Immediately**, if you want to reboot the broker and upgrade
     the engine version immediately.

   ###### Important

   Single instance brokers are offline while being rebooted. For cluster brokers,
   only one node is down at a time while the broker reboots.

5. Choose **Apply** to finish applying the changes.

###### To upgrade the engine version of a broker by using the AWS CLI

1. Use the [update-broker](../../../cli/latest/reference/mq/update-broker.md "../../../cli/latest/reference/mq/update-broker.md") CLI command
   and specify the following parameters, as shown in the example.
   - `--broker-id` – The unique ID that Amazon MQ generates for the broker.
     You can parse the ID from your broker ARN. For example, given the following ARN,
     `arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`, the broker ID would be `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`.
   - `--engine-version` – The engine version number for the broker engine to upgrade to.

```
aws mq update-broker --broker-id `broker-id` --engine-version `version-number`
```

2. (Optional) Use the [reboot-broker](../../../cli/latest/reference/mq/reboot-broker.md "../../../cli/latest/reference/mq/reboot-broker.md") CLI command to
   reboot your broker if you want to upgrade the engine version immediately.

```
aws mq reboot-broker --broker-id `broker-id`
```

If you do not want to reboot your broker and apply the changes immediately, Amazon MQ will upgrade the broker during the next
scheduled maintenance window.

###### Important

Single instance brokers are offline while being rebooted. For cluster brokers,
only one node is down at a time while the broker reboots.

###### To upgrade the engine version of a broker by using the Amazon MQ API

1. Use the [UpdateBroker](../api-reference/brokers-broker-id.md#UpdateBroker "../api-reference/brokers-broker-id.md#UpdateBroker") API operation.
   Specify `broker-id` as a path parameter. The following examples assumes a broker in the `us-west-2` region. For more information
   about available Amazon MQ endpoints, see [Amazon MQ endpoints and quotas.](../../../general/latest/gr/amazon-mq.md#amazon-mq_region "../../../general/latest/gr/amazon-mq.md#amazon-mq_region")
   in the _AWS General Reference_

```
PUT /v1/brokers/`broker-id` HTTP/1.1
Host: mq.us-west-2.amazonaws.com
Date: Mon, 7 June 2021 12:00:00 GMT
x-amz-date: Mon, 7 June 2021 12:00:00 GMT
Authorization: `authorization-string`
```

Use `engineVersion` in the request payload to specify the version number for the broker to upgrade to.

```
{
    "engineVersion": "`engine-version-number`"
}
```

2. (Optional) Use the [RebootBroker](../api-reference/brokers-broker-id-reboot.md#RebootBroker "../api-reference/brokers-broker-id-reboot.md#RebootBroker") API
   operation to reboot your broker if you want to upgrade the engine version immediately. `broker-id` is specified as
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
