# Updating DevOps Guru settings

You can update the following Amazon DevOps Guru settings:

- Your DevOps Guru coverage. This determines which resources in your account are analyzed.
- Your notifications. This determines which Amazon Simple Notification Service topics are used to notify you
  of important DevOps Guru events.
- Features for enhanced insights. This includes log anomaly detection, encryption, and your AWS Systems Manager integration settings.
  This determines whether DevOps Guru displays log data, whether you use additional security keys, and whether an OpsItem is created in
  Systems Manager OpsCenter for each new insight.

###### Topics

- [Updating your management account
  settings](#update-management-account "#update-management-account")
- [Updating your AWS analysis coverage in DevOps Guru](#update-coverage "#update-coverage")
- [Updating your notifications in DevOps Guru](update-notifications.md "update-notifications.md")
- [Filtering your DevOps Guru notifications](update-notifications-filter.md "update-notifications-filter.md")
- [Updating AWS Systems Manager integration in
  DevOps Guru](#update-systems-manager-integration "#update-systems-manager-integration")
- [Updating log anomaly detection in
  DevOps Guru](#update-log-analysis "#update-log-analysis")
- [Updating encryption settings in
  DevOps Guru](#update-encryption "#update-encryption")

## Updating your management account

settings

You can configure DevOps Guru for accounts in your organization. If you haven't registered a
delegated administrator, you can do so by choosing **Register delegated
administrator**. For more information on registering a delegated
administrator, see [Enable
DevOps Guru](getting-started-enable-service.md "getting-started-enable-service.md").

## Updating your AWS analysis coverage in DevOps Guru

You can update which AWS resources in your account DevOps Guru analyzes. To do this, navigate
to the **Analyzed resources** page in the console and then choose
**Edit**. For more information, see [Viewing resources analyzed by DevOps Guru](view-analyzed-resources.md "view-analyzed-resources.md").

## Updating AWS Systems Manager integration in

DevOps Guru

You can enable the creation of an OpsItem for each new insight in AWS Systems Manager OpsCenter.
OpsCenter is a centralized system where you can view, investigate, and review
operational work items (OpsItems). The OpsItems for your insights can help you manage
work that addresses the anomalous behavior that triggered the creation of each insight.
For more information, see [AWS Systems Manager OpsCenter](../../../systems-manager/latest/userguide/OpsCenter.md "../../../systems-manager/latest/userguide/OpsCenter.md")
and [Working
with OpsItem](../../../systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.md "../../../systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.md") in the _AWS Systems Manager User Guide_.

###### Note

If you change the key or value of the tag field of an OpsItem, then DevOps Guru is not
able to update that OpsItem. For example, if you change a tag of an OpsItem from
`"aws:RequestTag/DevOps-GuruInsightSsmOpsItemRelated": "true"` to
something else, then DevOps Guru cannot update that OpsItem.

###### To manage your Systems Manager integration

1. Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2. Choose **Settings** in the navigation pane.
3. In **AWS Systems Manager integration**, select **Enable DevOps Guru
   to create an AWS OpstItem in OpsCenter for each insight** to have
   an OpsItem created for each new insight. Deselect it to stop having an OpsItem
   created for each new insight.

You are charged for OpsItems created in your account. For more information, see [AWS Systems Manager pricing](https://aws.amazon.com/systems-manager/pricing/ "https://aws.amazon.com/systems-manager/pricing/").

## Updating log anomaly detection in

DevOps Guru

###### To manage your log anomaly detection settings

1. Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2. Choose **Settings** in the navigation pane.
3. In **Log anomaly detection**, select
   **Enable log anomaly detection by granting DevOps Guru permissions to display log data associated with an insight.** to have
   DevOps Guru display log data related to insights.

## Updating encryption settings in

DevOps Guru

You can update encryption settings to use AWS owned keys or AWS KMS customer managed keys.
When switching to a new customer managed AWS KMS key from an existing customer managed AWS KMS key, DevOps Guru automatically starts encrypting newly ingested metadata using the new key.
The historical data will remain encrypted with the previous configured customer managed AWS KMS key.

###### Note

If you revoke the grant, or disable or delete the previous AWS KMS key, DevOps Guru won't be able to
access any of the data encrypted by this key and you might see the `AccessDeniedException` when performing a read operation.

###### To manage your encryption settings

1. Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2. Choose **Settings** in the navigation pane.
3. In the **Encryption** section, choose **Edit encryption**.
4. Select the encrpytion type you would like to use to protect your data. You can use a default AWS owned key, choose an existing customer managed key, or
   create a new customer managed AWS KMS key.
5. Choose **Save**.

Encryption is an important part of DevOps Guru security. For more information, see [Data protection in Amazon DevOps Guru](data-protection.md "data-protection.md").
