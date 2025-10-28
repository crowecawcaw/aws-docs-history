# Viewing Compliance History for your AWS Resources with AWS Config

###### Important

The `AWS::Config::ResourceCompliance` resource type is used to store historical compliance results for resources. Recording this resource type is **not required** for Config rules to evaluate resources or for viewing current compliance status in the console.

Recording `AWS::Config::ResourceCompliance` only enables you to view historical compliance changes over time in the resource timeline. If you don't need historical compliance data, you can exclude this resource type. For more information about selecting resources to record, see [Recording AWS Resources](select-resources.md "select-resources.md").

You can view the configuration, relationships, and number of changes made to a resource in
the AWS Config console. You can view the configuration history for a resource using AWS CLI.

###### Topics

- [Viewing Compliance History (Console)](#view-config-details-console "#view-config-details-console")
- [Viewing Compliance History (AWS CLI)](#view-config-details-cli "#view-config-details-cli")
- [For Resources and Rules](#view-compliance-history "#view-compliance-history")

## Viewing Compliance History (Console)

When you look up resources on the **Resource inventory** page, choose the resource
name or ID in the resource identifier column to view the resource's details page. The
details page provides information about the configuration, relationships, and number of
changes made to that resource.

To access the resource timeline from the resource details page, choose the **Resource Timeline** button. The Resource timeline captures
changes as `ConfigurationItems` over a period of time for a specific
resource. You can filter by Configuration events, Compliance events, or CloudTrail
Events.

## Viewing Compliance History (AWS CLI)

The configuration items that AWS Config records are delivered to the specified delivery
channel on demand as a configuration snapshot and as a configuration stream. You can use
the AWS CLI to view history of configuration items for each resource.

#### Viewing Configuration History

Enter the [`get-resource-config-history`](../../../cli/latest/reference/configservice/get-resource-config-history.md "../../../cli/latest/reference/configservice/get-resource-config-history.md") command and specify the
resource type and the resource ID, for example:

```
$ **aws configservice get-resource-config-history --resource-type AWS::EC2::SecurityGroup --resource-id sg-6fbb3807**
{
    "configurationItems": [
        {
            "configurationItemCaptureTime": 1414708529.9219999,
            "relationships": [
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-7a3b232a",
                    "relationshipName": "Is associated with Instance"
                },
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-8b6eb2ab",
                    "relationshipName": "Is associated with Instance"
                },
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-c478efe5",
                    "relationshipName": "Is associated with Instance"
                },
                {
                    "resourceType": "AWS::EC2::Instance",
                    "resourceId": "i-e4cbe38d",
                    "relationshipName": "Is associated with Instance"
                }
            ],
            "availabilityZone": "Not Applicable",
            "tags": {},
            "resourceType": "AWS::EC2::SecurityGroup",
            "resourceId": "sg-6fbb3807",
            "configurationStateId": "1",
            "relatedEvents": [],
            "arn": "arn:aws:ec2:us-east-2:012345678912:security-group/default",
            "version": "1.0",
            "configurationItemMD5Hash": "860aa81fc3869e186b2ee00bc638a01a",
            "configuration": "{\"ownerId\":\"605053316265\",\"groupName\":\"default\",\"groupId\":\"sg-6fbb3807\",\"description\":\"default group\",\"ipPermissions\":[{\"ipProtocol\":\"tcp\",\"fromPort\":80,\"toPort\":80,\"userIdGroupPairs\":[{\"userId\":\"amazon-elb\",\"groupName\":\"amazon-elb-sg\",\"groupId\":\"sg-843f59ed\"}],\"ipRanges\":[\"0.0.0.0/0\"]},{\"ipProtocol\":\"tcp\",\"fromPort\":0,\"toPort\":65535,\"userIdGroupPairs\":[{\"userId\":\"605053316265\",\"groupName\":\"default\",\"groupId\":\"sg-6fbb3807\"}],\"ipRanges\":[]},{\"ipProtocol\":\"udp\",\"fromPort\":0,\"toPort\":65535,\"userIdGroupPairs\":[{\"userId\":\"605053316265\",\"groupName\":\"default\",\"groupId\":\"sg-6fbb3807\"}],\"ipRanges\":[]},{\"ipProtocol\":\"icmp\",\"fromPort\":-1,\"toPort\":-1,\"userIdGroupPairs\":[{\"userId\":\"605053316265\",\"groupName\":\"default\",\"groupId\":\"sg-6fbb3807\"}],\"ipRanges\":[]},{\"ipProtocol\":\"tcp\",\"fromPort\":1433,\"toPort\":1433,\"userIdGroupPairs\":[],\"ipRanges\":[\"0.0.0.0/0\"]},{\"ipProtocol\":\"tcp\",\"fromPort\":3389,\"toPort\":3389,\"userIdGroupPairs\":[],\"ipRanges\":[\"207.171.160.0/19\"]}],\"ipPermissionsEgress\":[],\"vpcId\":null,\"tags\":[]}",
            "configurationItemStatus": "ResourceDiscovered",
            "accountId": "605053316265"
        }
    ],
    "nextToken":
     ..........
```

For detailed explanation of the response fields, see [Components of a Configuration Item](config-item-table.md "config-item-table.md") and [Supported Resource Types for AWS Config](resource-config-reference.md "resource-config-reference.md").

#### Example Amazon EBS Configuration History from

AWS Config

AWS Config generates a set of files that each represent a resource type and lists all
configuration changes for the resources of that type that AWS Config is recording. AWS Config
exports this resource-centric configuration history as an object in the Amazon S3 bucket
that you specified when you enabled AWS Config. The configuration history file for each
resource type contains the changes that were detected for the resources of that type
since the last history file was delivered. The history files are typically delivered
every six hours.

The following is an example of the contents of the Amazon S3 object that describes the
configuration history of all the Amazon Elastic Block Store volumes in the current region for your
AWS account. The volumes in this account include `vol-ce676ccc` and
`vol-cia007c`. Volume `vol-ce676ccc` had two configuration
changes since the previous history file was delivered while volume
`vol-cia007c` had one change.

```
{
    "fileVersion": "1.0",
    "requestId": "asudf8ow-4e34-4f32-afeb-0ace5bf3trye",
    "configurationItems": [
        {
            "snapshotVersion": "1.0",
            "resourceId": "vol-ce676ccc",
            "arn": "arn:aws:us-west-2b:123456789012:volume/vol-ce676ccc",
            "accountId": "12345678910",
            "configurationItemCaptureTime": "2014-03-07T23:47:08.918Z",
            "configurationStateID": "3e660fdf-4e34-4f32-afeb-0ace5bf3d63a",
            "configurationItemStatus": "OK",
            "relatedEvents": [
                "06c12a39-eb35-11de-ae07-adb69edbb1e4",
                "c376e30d-71a2-4694-89b7-a5a04ad92281"
            ],
            "availibilityZone": "us-west-2b",
            "resourceType": "AWS::EC2::Volume",
            "resourceCreationTime": "2014-02-27T21:43:53.885Z",
            "tags": {},
            "relationships": [
                {
                    "resourceId": "i-344c463d",
                    "resourceType": "AWS::EC2::Instance",
                    "name": "Attached to Instance"
                }
            ],
            "configuration": {
                "volumeId": "vol-ce676ccc",
                "size": 1,
                "snapshotId": "",
                "availabilityZone": "us-west-2b",
                "state": "in-use",
                "createTime": "2014-02-27T21:43:53.0885+0000",
                "attachments": [
                    {
                        "volumeId": "vol-ce676ccc",
                        "instanceId": "i-344c463d",
                        "device": "/dev/sdf",
                        "state": "attached",
                        "attachTime": "2014-03-07T23:46:28.0000+0000",
                        "deleteOnTermination": false
                    }
                ],
                "tags": [
                    {
                        "tagName": "environment",
                        "tagValue": "PROD"
                    },
                    {
                        "tagName": "name",
                        "tagValue": "DataVolume1"
                    }
                ],
                "volumeType": "standard"
            }
        },
        {
            "configurationItemVersion": "1.0",
            "resourceId": "vol-ce676ccc",
            "arn": "arn:aws:us-west-2b:123456789012:volume/vol-ce676ccc",
            "accountId": "12345678910",
            "configurationItemCaptureTime": "2014-03-07T21:47:08.918Z",
            "configurationItemState": "3e660fdf-4e34-4f32-sseb-0ace5bf3d63a",
            "configurationItemStatus": "OK",
            "relatedEvents": [
                "06c12a39-eb35-11de-ae07-ad229edbb1e4",
                "c376e30d-71a2-4694-89b7-a5a04w292281"
            ],
            "availibilityZone": "us-west-2b",
            "resourceType": "AWS::EC2::Volume",
            "resourceCreationTime": "2014-02-27T21:43:53.885Z",
            "tags": {},
            "relationships": [
                {
                    "resourceId": "i-344c463d",
                    "resourceType": "AWS::EC2::Instance",
                    "name": "Attached to Instance"
                }
            ],
            "configuration": {
                "volumeId": "vol-ce676ccc",
                "size": 1,
                "snapshotId": "",
                "availabilityZone": "us-west-2b",
                "state": "in-use",
                "createTime": "2014-02-27T21:43:53.0885+0000",
                "attachments": [
                    {
                        "volumeId": "vol-ce676ccc",
                        "instanceId": "i-344c463d",
                        "device": "/dev/sdf",
                        "state": "attached",
                        "attachTime": "2014-03-07T23:46:28.0000+0000",
                        "deleteOnTermination": false
                    }
                ],
                "tags": [
                    {
                        "tagName": "environment",
                        "tagValue": "PROD"
                    },
                    {
                        "tagName": "name",
                        "tagValue": "DataVolume1"
                    }
                ],
                "volumeType": "standard"
            }
        },
        {
            "configurationItemVersion": "1.0",
            "resourceId": "vol-cia007c",
            "arn": "arn:aws:us-west-2b:123456789012:volume/vol-cia007c",
            "accountId": "12345678910",
            "configurationItemCaptureTime": "2014-03-07T20:47:08.918Z",
            "configurationItemState": "3e660fdf-4e34-4f88-sseb-0ace5bf3d63a",
            "configurationItemStatus": "OK",
            "relatedEvents": [
                "06c12a39-eb35-11de-ae07-adjhk8edbb1e4",
                "c376e30d-71a2-4694-89b7-a5a67u292281"
            ],
            "availibilityZone": "us-west-2b",
            "resourceType": "AWS::EC2::Volume",
            "resourceCreationTime": "2014-02-27T20:43:53.885Z",
            "tags": {},
            "relationships": [
                {
                    "resourceId": "i-344e563d",
                    "resourceType": "AWS::EC2::Instance",
                    "name": "Attached to Instance"
                }
            ],
            "configuration": {
                "volumeId": "vol-cia007c",
                "size": 1,
                "snapshotId": "",
                "availabilityZone": "us-west-2b",
                "state": "in-use",
                "createTime": "2014-02-27T20:43:53.0885+0000",
                "attachments": [
                    {
                        "volumeId": "vol-cia007c",
                        "instanceId": "i-344e563d",
                        "device": "/dev/sdf",
                        "state": "attached",
                        "attachTime": "2014-03-07T23:46:28.0000+0000",
                        "deleteOnTermination": false
                    }
                ],
                "tags": [
                    {
                        "tagName": "environment",
                        "tagValue": "PROD"
                    },
                    {
                        "tagName": "name",
                        "tagValue": "DataVolume2"
                    }
                ],
                "volumeType": "standard"
            }
        }
    ]
}

```

## Viewing Compliance History Timeline for

Resources and Rules

AWS Config supports storing compliance state changes of resources as evaluated by AWS Config Rules. The
resource compliance history is presented in the form of a timeline. The timeline captures
changes as `ConfigurationItems` over a period of time for a specific resource.
For information on the contents of `ConfigurationItem`, see [ConfigurationItem](../APIReference/API_ConfigurationItem.md "../APIReference/API_ConfigurationItem.md") in the AWS Config API
Reference.

You can opt in or out to record all resource types in AWS Config. If you have opted to record
all resource types, AWS Config automatically begins recording the resource compliance history as
evaluated by AWS Config Rules. By default, AWS Config records the configuration changes for all supported
resources. You can also select only the specific resource compliance history resource type:
`AWS::Config::ResourceCompliance`. For more information, see [Recording AWS Records](select-resources.md#select-resources-console "select-resources.md#select-resources-console").

Viewing Resource Timeline Using
Resources
Access the resource timeline by selecting a specific resource from the Resource
inventory page.

1. Choose the **Resources** from the left
   navigation.
2. On the Resource inventory page, you can filter by resource category, resource
   type, and compliance status. Choose **Include deleted
   resources** if appropriate.

The table displays the resource identifier for the resource type and the
resource compliance status for that resource. The resource identifier might be a
resource ID or a resource name. 3. Choose a resource from the resource identifier column. 4. Choose the **Resource Timeline** button. You can
filter by Configuration events, Compliance events, or CloudTrail Events.

###### Note

Alternatively, on the Resource inventory page, you can directly choose the
resource name. To access the resource timeline from the resource details
page, choose the **Resource Timeline**
button.

Viewing Resource Timeline Using
Rules
Access the resource timeline by selecting a specific rule from the Rule page.

1. Select the **Rules** from the left
   navigation.
2. On the Rule page, choose a rule evaluating your relevant resources. If no
   rules are displayed on the screen, add rules using the **Add
   rule** button.
3. On the Rule details page, select the resources from the Resources evaluated
   table.
4. Select the **Resource Timeline** button. The
   resource timeline is displayed.
