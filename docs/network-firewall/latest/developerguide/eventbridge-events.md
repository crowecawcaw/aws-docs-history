

# Managing AWS Network Firewall events using Amazon EventBridge
<a name="eventbridge-events"></a>

AWS Network Firewall sends events directly to the EventBridge default event bus when firewall state changes occur. You can use these events to automate responses, send notifications, or integrate with other AWS services when your firewall configuration or attachment status changes.

## Event types
<a name="eventbridge-events-types"></a>

The following table describes the event types that AWS Network Firewall publishes to EventBridge default event bus for firewall state changes.


| Event type | Description | 
| --- | --- | 
| Firewall Configuration Changed | Published when the firewall configuration changes, such as when a firewall policy or rule group is updated. | 
| Firewall Attachment Status Changed | Published when the status of a firewall endpoint attachment changes. | 
| Firewall Transit Gateway Attachment Status Changed | Published when the status of a transit gateway attachment to the firewall changes. | 

## Event examples
<a name="eventbridge-events-examples"></a>

The following examples show the structure of events that AWS Network Firewall publishes to EventBridge.

### Firewall Configuration Changed
<a name="eventbridge-firewall-configuration-changed"></a>

Events published when a firewall configuration changes, such as when a firewall policy or rule group is updated.

------
#### [ Update Events ]

This event is published when a firewall policy or rule group is updated, changing the configuration synchronization status. The example shows a policy update that transitions the configuration sync status from `IN_SYNC` to `PENDING`.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Firewall Configuration Changed",
  "source": "aws.network-firewall",
  "account": "111122223333",
  "time": "2026-01-28T00:39:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:network-firewall:us-east-1:111122223333:firewall/firewallname"
  ],
  "detail": {
    "data": [
      {
        "Availability Zone": "us-east-1c",
        "Configuration Resource ARN": "arn:aws:network-firewall:us-east-1:111122223333:firewall-policy/policyname",
        "Current Configuration Sync Status": "PENDING",
        "Previous Configuration Sync Status": "IN_SYNC",
        "Previous Configuration Update Token": "3855de80-2c83-4383-9d43-11ae9010855e"
      },
      {
        "Availability Zone": "us-east-1c",
        "Configuration Resource ARN": "arn:aws:network-firewall:us-east-1:aws-managed:stateful-rulegroup/statefulrulegroupname",
        "Current Configuration Sync Status": "PENDING"
      }
    ],
    "metadata": {
      "State Change ID": "08c4c78d4580bd12cde6c94eee221f4e15f592825eb299572c04ddd7a9a4a7f2"
    },
    "version": "1.0.0"
  }
}
```

------

### Firewall Attachment Status Changed
<a name="eventbridge-firewall-attachment-status-changed"></a>

Events published when the status of a firewall endpoint attachment changes during the firewall lifecycle.

------
#### [ Creating Events ]

This event is published when a firewall endpoint attachment is being created in an availability zone. The `Current Attachment Status` field shows `CREATING`.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Firewall Attachment Status Changed",
  "source": "aws.network-firewall",
  "account": "111122223333",
  "time": "2026-01-28T00:39:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:network-firewall:us-east-1:111122223333:firewall/firewallname"
  ],
  "detail": {
    "data": [
      {
        "Availability Zone": "us-east-1c",
        "Current Attachment Status": "CREATING"
      }
    ],
    "metadata": {
      "State Change ID": "ec543b4702a2f9b277ddc1edfced32f5920431fca62d83d3052be5c637360b9f"
    },
    "version": "1.0.0"
  }
}
```

------
#### [ Ready Events ]

This event is published when a firewall endpoint attachment completes creation and becomes ready for traffic. The status transitions from `CREATING` to `READY`.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Firewall Attachment Status Changed",
  "source": "aws.network-firewall",
  "account": "111122223333",
  "time": "2026-01-28T00:39:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:network-firewall:us-east-1:111122223333:firewall/firewallname"
  ],
  "detail": {
    "data": [
      {
        "Availability Zone": "us-east-1c",
        "Current Attachment Status": "READY",
        "Endpoint ID": "vpce-1234567890abcdefg",
        "Previous Attachment Status": "CREATING"
      }
    ],
    "metadata": {
      "State Change ID": "59d86fd2f87cf005a2d41cffa8c86980f3648e9e2359b6c21068b6fbd31f6bd4"
    },
    "version": "1.0.0"
  }
}
```

------
#### [ Deleting Events ]

This event is published when a firewall endpoint attachment is being deleted. The status transitions from `READY` to `DELETING`.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Firewall Attachment Status Changed",
  "source": "aws.network-firewall",
  "account": "111122223333",
  "time": "2026-01-28T00:39:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:network-firewall:us-east-1:111122223333:firewall/firewallname"
  ],
  "detail": {
    "data": [
      {
        "Availability Zone": "us-east-1c",
        "Current Attachment Status": "DELETING",
        "Endpoint ID": "vpce-1234567890abcdefg",
        "Previous Attachment Status": "READY"
      }
    ],
    "metadata": {
      "State Change ID": "b6602d36c880bd5c6e6bdd62206cc6554c162019569f2170502f85c1b9332a33"
    },
    "version": "1.0.0"
  }
}
```

------

### Firewall Transit Gateway Attachment Status Changed
<a name="eventbridge-firewall-tgw-attachment-status-changed"></a>

Events published when the status of a transit gateway attachment to the firewall changes during the attachment lifecycle.

------
#### [ Creating Events ]

This event is published when a transit gateway attachment to the firewall is being created. The `Current Transit Gateway Attachment Status` field shows `CREATING`.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Firewall Transit Gateway Attachment Status Changed",
  "source": "aws.network-firewall",
  "account": "111122223333",
  "time": "2026-01-28T00:39:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:network-firewall:us-east-1:111122223333:firewall/firewallname"
  ],
  "detail": {
    "data": {
      "Attachment ID": "tgw-attach-1234567890abcdefg",
      "Current Transit Gateway Attachment Status": "CREATING"
    },
    "metadata": {
      "State Change ID": "4331b74ee5b5860fe659341efd09798857de175a8a4da7128ad0439e6ef710e7"
    },
    "version": "1.0.0"
  }
}
```

------
#### [ Pending Events ]

This event is published when a transit gateway attachment is waiting for acceptance. The status transitions from `CREATING` to `PENDING_ACCEPTANCE`.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Firewall Transit Gateway Attachment Status Changed",
  "source": "aws.network-firewall",
  "account": "111122223333",
  "time": "2026-01-28T00:39:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:network-firewall:us-east-1:111122223333:firewall/firewallname"
  ],
  "detail": {
    "data": {
      "Attachment ID": "tgw-attach-1234567890abcdefg",
      "Current Transit Gateway Attachment Status": "PENDING_ACCEPTANCE",
      "Previous Transit Gateway Attachment Status": "CREATING"
    },
    "metadata": {
      "State Change ID": "ce5a91c102a91bb94527baa4290b39dd3be79a9f3452f644c11145cf4755e13c"
    },
    "version": "1.0.0"
  }
}
```

------
#### [ Ready Events ]

This event is published when a transit gateway attachment completes and becomes ready for traffic. The status transitions from `CREATING` to `READY`.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Firewall Transit Gateway Attachment Status Changed",
  "source": "aws.network-firewall",
  "account": "111122223333",
  "time": "2026-01-28T00:39:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:network-firewall:us-east-1:111122223333:firewall/firewallname"
  ],
  "detail": {
    "data": {
      "Attachment ID": "tgw-attach-1234567890abcdefg",
      "Current Transit Gateway Attachment Status": "READY",
      "Previous Transit Gateway Attachment Status": "CREATING"
    },
    "metadata": {
      "State Change ID": "466efda83ad59a8d543eac712f5ad96465ac4ad87f5dab196cbf1be92f4d9918"
    },
    "version": "1.0.0"
  }
}
```

------
#### [ Deleting Events ]

This event is published when a transit gateway attachment is being deleted. The status transitions from `READY` to `DELETING`.

```
{
  "version": "0",
  "id": "01234567-0123-0123-0123-0123456789ab",
  "detail-type": "Firewall Transit Gateway Attachment Status Changed",
  "source": "aws.network-firewall",
  "account": "111122223333",
  "time": "2026-01-28T00:39:59Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:network-firewall:us-east-1:111122223333:firewall/firewallname"
  ],
  "detail": {
    "data": {
      "Attachment ID": "tgw-attach-1234567890abcdefg",
      "Current Transit Gateway Attachment Status": "DELETING",
      "Previous Transit Gateway Attachment Status": "READY"
    },
    "metadata": {
      "State Change ID": "5e68266934a286c64a5cc0593505f1ad2a0a959bef915e74aa6612bfb5accc6b"
    },
    "version": "1.0.0"
  }
}
```

------