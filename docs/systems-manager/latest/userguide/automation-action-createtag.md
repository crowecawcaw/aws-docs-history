• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# `aws:createTags` –

Create tags for AWS resources

Creates new tags for Amazon Elastic Compute Cloud (Amazon EC2) instances or AWS Systems Manager managed
instances.

###### Note

The `aws:createTags` action supports automatic throttling retry. For
more information, see [Configuring automatic retry for
throttled operations](automation-throttling-retry.md "automation-throttling-retry.md").

###### Input

This action supports most Amazon EC2 `CreateTags` and Systems Manager
`AddTagsToResource` parameters. For more information, see [CreateTags](../../../AWSEC2/latest/APIReference/api_createtags.md "../../../AWSEC2/latest/APIReference/api_createtags.md") and [AddTagsToResource](../../../AWSEC2/latest/APIReference/api_addtagstoresource.md "../../../AWSEC2/latest/APIReference/api_addtagstoresource.md").

The following example shows how to tag an Amazon Machine Image (AMI) and an instance as
production resources for a particular department.

YAML

```
name: createTags
action: aws:createTags
maxAttempts: 3
onFailure: Abort
inputs:
  ResourceType: EC2
  ResourceIds:
  - ami-9a3768fa
  - i-02951acd5111a8169
  Tags:
  - Key: production
    Value: ''
  - Key: department
    Value: devops
```

JSON

```
{
    "name": "createTags",
    "action": "aws:createTags",
    "maxAttempts": 3,
    "onFailure": "Abort",
    "inputs": {
        "ResourceType": "EC2",
        "ResourceIds": [
            "ami-9a3768fa",
            "i-02951acd5111a8169"
        ],
        "Tags": [
            {
                "Key": "production",
                "Value": ""
            },
            {
                "Key": "department",
                "Value": "devops"
            }
        ]
    }
}
```

ResourceIds

The IDs of the resource(s) to be tagged. If resource type isn't “EC2”,
this field can contain only a single item.

Type: String List

Required: Yes

Tags

The tags to associate with the resource(s).

Type: List of Maps

Required: Yes

ResourceType

The type of resource(s) to be tagged. If not supplied, the default value
of “EC2” is used.

Type: String

Required: No

Valid Values: `EC2` | `ManagedInstance` |
`MaintenanceWindow` | `Parameter`

###### Output

None
