• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# `aws:deleteImage` – Delete

an Amazon Machine Image

Deletes the specified Amazon Machine Image (AMI) and all related snapshots.

###### Note

The `aws:deleteImage` action supports automatic throttling retry. For
more information, see [Configuring automatic retry for
throttled operations](automation-throttling-retry.md "automation-throttling-retry.md").

###### Input

This action supports only one parameter. For more information, see the
documentation for [DeregisterImage](../../../AWSEC2/latest/APIReference/API_DeregisterImage.md "../../../AWSEC2/latest/APIReference/API_DeregisterImage.md") and [DeleteSnapshot](../../../AWSEC2/latest/APIReference/API_DeleteSnapshot.md "../../../AWSEC2/latest/APIReference/API_DeleteSnapshot.md").

YAML

```
name: deleteMyImage
action: aws:deleteImage
maxAttempts: 3
timeoutSeconds: 180
onFailure: Abort
inputs:
  ImageId: ami-12345678
```

JSON

```
{
    "name": "deleteMyImage",
    "action": "aws:deleteImage",
    "maxAttempts": 3,
    "timeoutSeconds": 180,
    "onFailure": "Abort",
    "inputs": {
        "ImageId": "ami-12345678"
    }
}
```

ImageId

The ID of the image to be deleted.

Type: String

Required: Yes

###### Output

None
