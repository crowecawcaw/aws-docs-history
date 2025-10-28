# Upgrading an Amazon MQ broker engine version

Amazon MQ regularly provides new broker engine versions for all supported broker engine types. New engine versions
include security patches, bug fixes, and other broker engine improvements.

Amazon MQ organizes version numbers according to semantic versioning specification as
`X.Y.Z`. In Amazon MQ implementations, `X` denotes the
major version, `Y` represents the minor version, and `Z` denotes the patch version number. There are
two types of upgrades:

- Major version upgrade – Occurs when the
  major engine version numbers change. For example, upgrading from version **1**.0 to version **2**.0 is
  considered a major version upgrade.
- Minor version upgrade – Occurs when only the
  minor engine version number changes. For example, upgrading from version 1.**5** to version 1.**6** is considered a minor version upgrade.

You can manually upgrade your broker at any time to the next supported major or minor version. When you turn on
[automatic minor version upgrades](../api-reference/brokers-broker-id.md#brokers-broker-id-prop-updatebrokerinput-autominorversionupgrade "../api-reference/brokers-broker-id.md#brokers-broker-id-prop-updatebrokerinput-autominorversionupgrade"),
Amazon MQ will upgrade your broker to the latest supported patch version.
For all brokers using engine version 3.13 and above, Amazon MQ manages upgrades to the latest supported patch version during the [maintenance window](maintaining-brokers.md "maintaining-brokers.md").
Amazon MQ upgrades your broker to the next minor version when the current minor version reaches end of support.
Both manual and automatic version upgrades occur during the scheduled maintenance window or after you
[reboot your broker](amazon-mq-rebooting-broker.md "amazon-mq-rebooting-broker.md").

The following topics describe how you can manually upgrade the broker engine version, and activate automatic minor version upgrades.

###### Topics

- [Manually upgrading the engine version](#upgrading-brokers-manual-upgrades "#upgrading-brokers-manual-upgrades")
- [Automatically upgrading the minor engine version](#upgrading-brokers-automatic-upgrades "#upgrading-brokers-automatic-upgrades")

## Manually upgrading the engine version

To manually upgrade the engine version of a broker to a new major or minor version, you can use the AWS Management Console, the AWS CLI, or the Amazon MQ API.

###### To upgrade the engine version of a broker by using the AWS Management Console

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. In the left navigation pane, choose **Brokers**,
   and then choose the broker that you want to upgrade from the list.
3. On the broker details page, choose **Edit**.
4. Under **Specifications**, for **Broker engine version**
   choose the new version number from the dropdown list.
5. Scroll to the bottom of the page, and choose **Schedule modifications**.
6. On the **Schedule broker modifications** page, for **When to apply modifications**,
   choose one of the following.
   - Choose **After the next reboot**, if you want Amazon MQ to complete the version upgrade
     during the next scheduled maintenance window.
   - Choose **Immediately**, if you want to reboot the broker and upgrade
     the engine version immediately.

   ###### Important

   Single instance brokers are offline while being rebooted. For cluster brokers,
   only one node is down at a time while the broker reboots.

7. Choose **Apply** to finish applying the changes.

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
   reboot your broker if, you want to upgrade the engine version immediately.

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

## Automatically upgrading the minor engine version

You can control whether automatic minor version upgrade is activated for a broker when you first create the broker, or by
modifying broker preferences. To activate auto minor version upgrades for an existing broker,
you can use the AWS Management Console, the AWS CLI, or the Amazon MQ API.

###### To activate automatic minor version upgrades by using the AWS Management Console

1. Sign in to the [Amazon MQ console](https://console.aws.amazon.com/amazon-mq/ "https://console.aws.amazon.com/amazon-mq/").
2. In the left navigation pane, choose **Brokers**,
   and then choose the broker that you want to upgrade from the list.
3. On the broker details page, choose **Edit**.
4. Under **Maintenance**, choose **Enable automatic minor version upgrades**.

###### Note

If the option is already selected, you do not need to make any changes. 5. Choose **Save** at the bottom of the page.

To activate automatic minor version upgrades via the AWS CLI, use the [update-broker](../../../cli/latest/reference/mq/update-broker.md "../../../cli/latest/reference/mq/update-broker.md") CLI command
and specify the following parameters.

- `--broker-id` – The unique ID that Amazon MQ generates for the broker.
  You can parse the ID from your broker ARN. For example, given the following ARN,
  `arn:aws:mq:us-east-2:123456789012:broker:MyBroker:b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`, the broker ID would be `b-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`.
- `--auto-minor-version-upgrade` – Activates the auto minor version upgrade option.

```
aws mq update-broker --broker-id `broker-id` --auto-minor-version-upgrade
```

###### Note

If you want to deactivate auto minor version upgrades for your ActiveMQ broker, use the `--no-auto-minor-version-upgrade` parameter.

To activate automatic minor version upgrades via the Amazon MQ API, use the
[UpdateBroker](../api-reference/brokers-broker-id.md#UpdateBroker "../api-reference/brokers-broker-id.md#UpdateBroker") API operation.
Specify `broker-id` as a path parameter. The following example assumes a broker in the `us-west-2` region. For more information
about available Amazon MQ endpoints, see [Amazon MQ endpoints and quotas.](../../../general/latest/gr/amazon-mq.md#amazon-mq_region "../../../general/latest/gr/amazon-mq.md#amazon-mq_region")
in the _AWS General Reference_

```
PUT /v1/brokers/`broker-id` HTTP/1.1
Host: mq.us-west-2.amazonaws.com
Date: Mon, 7 June 2021 12:00:00 GMT
x-amz-date: Mon, 7 June 2021 12:00:00 GMT
Authorization: `authorization-string`
```

Use the `autoMinorVersionUpgrade` property in the request payload to activate auto minor version upgrade.

```
{
    "autoMinorVersionUpgrade": "true"
}
```

If you want to deactivate auto minor version upgrades for your broker, set `"autoMinorVersionUpgrade": "false"` in the request payload.
