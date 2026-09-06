

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# `aws:deleteImage` – Delete an Amazon Machine Image
<a name="automation-action-delete"></a>

Deletes the specified Amazon Machine Image (AMI) and all related snapshots.

**Note**  
The `aws:deleteImage` action supports automatic throttling retry. For more information, see [Configuring automatic retry for throttled operations](automation-throttling-retry.md).

**Input**  
This action supports only one parameter. For more information, see the documentation for [DeregisterImage](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeregisterImage.html) and [DeleteSnapshot](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteSnapshot.html).

------
#### [ YAML ]

```
name: deleteMyImage
action: aws:deleteImage
maxAttempts: 3
timeoutSeconds: 180
onFailure: Abort
inputs:
  ImageId: ami-12345678
```

------
#### [ JSON ]

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

------

ImageId  
The ID of the image to be deleted.  
Type: String  
Required: Yes

**Output**  
None