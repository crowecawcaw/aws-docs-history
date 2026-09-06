

# CloudWatch Logs updates to AWS service linked roles
<a name="cwl-slrpolicy-updates"></a>



View details about updates to AWS service linked role for CloudWatch Logs since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the CloudWatch Logs Document history page.




| Change | Description | Date | 
| --- | --- | --- | 
|  [ AWSServiceRoleForLogDelivery service-linked role policy](using-service-linked-roles-cwl.md#slr-permissions) – Update to an existing policy | CloudWatch Logs added `kms:GenerateDataKey` and `kms:Decrypt` permissions to the IAM policy associated with the **AWSServiceRoleForLogDelivery** service-linked role. These permissions are scoped with the `kms:ViaService` condition key to only allow use through Firehose. This change enables CloudWatch Logs to deliver logs to Firehose delivery streams that use server-side encryption with customer managed keys (SSE-CMK). | May 15, 2026 | 
|  [ AWSServiceRoleForLogDelivery service-linked role policy](AWS-logs-infrastructure-Firehose.md) – Update to an existing policy | CloudWatch Logs changed the permissions in the IAM policy associated with the **AWSServiceRoleForLogDelivery** service-linked role. The following change was made:+ The `firehose:ResourceTag/LogDeliveryEnabled": "true"` condition key was changed to `aws:ResourceTag/LogDeliveryEnabled": "true"`.  | July 15, 2021 | 
| CloudWatch Logs started tracking changes | CloudWatch Logs started tracking changes for its AWS managed policies. | June 10, 2021 | 