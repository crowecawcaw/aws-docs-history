# Tag a new or existing Spot Fleet request and the instances

and volumes it launches

To help categorize and manage your Spot Fleet requests and the instances and volumes that it
launches, you can tag them with custom metadata. You can assign a tag to a Spot Fleet request
when you create it, or afterward. Similarly, you can assign a tag to the instances and
volumes when they're launched by the fleet, or afterward.

When you tag a fleet request, the instances and volumes that are launched by the fleet
are not automatically tagged. You need to explicitly tag the instances and volumes
launched by the fleet. You can choose to assign tags to only the fleet request, or to
only the instances launched by the fleet, or to only the volumes attached to the
instances launched by the fleet, or to all of them.

###### Note

You can only tag volumes that are attached to On-Demand Instances. You can't tag volumes that
are attached to Spot Instances.

You can assign tags using the Amazon EC2 console or a command line tool.

For more information about how tags work, see [Tag your Amazon EC2 resources](Using_Tags.md "Using_Tags.md").

###### Contents

- [Prerequisite](#tag-spot-fleet-prereqs "#tag-spot-fleet-prereqs")
- [Tag a new Spot Fleet and the instances
  and volumes that it launches](#tag-new-spot-fleet-and-resources "#tag-new-spot-fleet-and-resources")
- [Tag an existing Spot Fleet](#tag-existing-spot-fleet "#tag-existing-spot-fleet")
- [View Spot Fleet request tags](#view-spot-fleet-tags "#view-spot-fleet-tags")

## Prerequisite

Grant the user the permission to tag resources. For more information, see [Example: Tag resources](ExamplePolicies_EC2.md#iam-example-taggingresources "ExamplePolicies_EC2.md#iam-example-taggingresources").

###### To grant a user the permission to tag resources

Create an IAM policy that includes the following:

- The `ec2:CreateTags` action. This grants the user permission to
  create tags.
- The `ec2:RequestSpotFleet` action. This grants the user
  permission to create a Spot Fleet request.
- For `Resource`, you must specify `"*"`. This allows
  users to tag all resource types.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "TagSpotFleetRequest",
 "Effect": "Allow",
 "Action": [
 "ec2:CreateTags",
 "ec2:RequestSpotFleet"
 ],
 "Resource": "*"
 }
 ]
}`

```

###### Important

We currently do not support resource-level permissions for the
`spot-fleet-request` resource. If you specify
`spot-fleet-request` as a resource, you will get an unauthorized
exception when you try to tag the fleet. The following example illustrates how
_not_ to set the policy.

```
{
    "Effect": "Allow",
    "Action": [
        "ec2:CreateTags",
        "ec2:RequestSpotFleet"
    ],
    "Resource": "arn:aws:ec2:`us-east-1`:`111122223333`:spot-fleet-request/*"
}
```

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

## Tag a new Spot Fleet and the instances

and volumes that it launches

###### To tag a new Spot Fleet request and the instances and volumes that it launches

using the console

1. Follow the [Create a Spot Fleet request using defined
   parameters](create-spot-fleet.md#create-spot-fleet-advanced "create-spot-fleet.md#create-spot-fleet-advanced") procedure.
2. The way you add a tag depends on whether you manually configured the fleet
   or used a launch template.
   - If you manually configured the fleet, do the following:

   To add a tag, expand **Additional launch
   parameters**, choose **Create tag**,
   and enter the key and value for the tag. Repeat for each tag.

   For each tag, you can tag the Spot Fleet request and the instances with
   the same tag. To tag both, ensure that both
   **Instances** and **Fleet**
   are selected. To tag only the Spot Fleet request, clear
   **Instances**. To tag only the instances
   launched by the fleet, clear **Fleet**.

   ###### Note

   When you manually configure a fleet, there is no option to tag
   volumes. Volume tags are only supported for volumes that are
   attached to On-Demand Instances. When you manually configure a fleet, you
   can't specify On-Demand Instances.
   - If you used a launch template, do the following:

   To add a tag to the fleet request, under
   **Tags**, choose **Create Tag**,
   and enter the key and value for the tag. Repeat for each tag.

   To tag the resources in your fleet, you must specify tags in the
   [launch
   template](create-launch-template.md "create-launch-template.md").

###### To tag a new Spot Fleet request and the instances and volumes that it launches

using the AWS CLI

To tag a Spot Fleet request when you create it, and to tag the instances and volumes
when they are launched by the fleet, configure the Spot Fleet request configuration as
follows:

###### Spot Fleet request tags:

- Specify the tags for the Spot Fleet request in
  `SpotFleetRequestConfig`.
- For `ResourceType`, specify `spot-fleet-request`. If
  you specify another value, the fleet request will fail.
- For `Tags`, specify the key-value pair. You can specify more
  than one key-value pair.

###### Instance tags:

- Specify the tags for the instances in
  `LaunchSpecifications`.
- For `ResourceType`, specify `instance`. If you
  specify another value, the fleet request will fail.
- For `Tags`, specify the key-value pair. You can specify more
  than one key-value pair.

Alternatively, you can specify the tags for the instance in the [launch template](create-launch-template.md "create-launch-template.md") that is
referenced in the Spot Fleet request.

###### Volume tags:

- Specify the tags for the volumes in the [launch template](create-launch-template.md "create-launch-template.md") that is
  referenced in the Spot Fleet request. Volume tagging in
  `LaunchSpecifications` is not supported.

In the following example, the Spot Fleet request is tagged with two tags:
Key=Environment and Value=Production, and Key=Cost-Center and Value=123. The
instances that are launched by the fleet are tagged with one tag (which is the same
as one of the tags for the Spot Fleet request): Key=Cost-Center and Value=123.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::111122223333:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchSpecifications": [
            {
                "ImageId": "ami-0123456789EXAMPLE",
                "InstanceType": "c4.large",
                "TagSpecifications": [
                    {
                        "ResourceType": "instance",
                        "Tags": [
                            {
                                "Key": "`Cost-Center`",
                                "Value": "`123`"
                            }
                        ]
                    }
                ]
            }
        ],
        "SpotPrice": "5",
        "TargetCapacity": 2,
        "TerminateInstancesWithExpiration": true,
        "Type": "maintain",
        "ReplaceUnhealthyInstances": true,
        "InstanceInterruptionBehavior": "terminate",
        "InstancePoolsToUseCount": 1,
        "TagSpecifications": [
            {
                "ResourceType": "spot-fleet-request",
                "Tags": [
                    {
                        "Key": "`Environment`",
                        "Value":"`Production`"
                    },
                    {
                        "Key": "`Cost-Center`",
                        "Value":"`123`"
                    }
                ]
            }
        ]
    }
}
```

###### To tag instances launched by a Spot Fleet using the AWS CLI

To tag instances when they are launched by the fleet, you can either specify
the tags in the [launch template](create-launch-template.md "create-launch-template.md")
that is referenced in the Spot Fleet request, or you can specify the tags in the Spot Fleet
request configuration as follows:

- Specify the tags for the instances in
  `LaunchSpecifications`.
- For `ResourceType`, specify `instance`. If you
  specify another value, the fleet request will fail.
- For `Tags`, specify the key-value pair. You can specify more
  than one key-value pair.

In the following example, the instances that are launched by the fleet are tagged
with one tag: Key=Cost-Center and Value=123.

```
{
    "SpotFleetRequestConfig": {
        "AllocationStrategy": "priceCapacityOptimized",
        "ExcessCapacityTerminationPolicy": "default",
        "IamFleetRole": "arn:aws:iam::111122223333:role/aws-ec2-spot-fleet-tagging-role",
        "LaunchSpecifications": [
            {
                "ImageId": "ami-0123456789EXAMPLE",
                "InstanceType": "c4.large",
                "TagSpecifications": [
                    {
                        "ResourceType": "instance",
                        "Tags": [
                            {
                                "Key": "`Cost-Center`",
                                "Value": "`123`"
                            }
                        ]
                    }
                ]
            }
        ],
        "SpotPrice": "5",
        "TargetCapacity": 2,
        "TerminateInstancesWithExpiration": true,
        "Type": "maintain",
        "ReplaceUnhealthyInstances": true,
        "InstanceInterruptionBehavior": "terminate",
        "InstancePoolsToUseCount": 1
    }
}
```

###### To tag volumes attached to On-Demand Instances launched by a Spot Fleet using the AWS CLI

To tag volumes when they are created by the fleet, you must specify the tags
in the [launch template](create-launch-template.md "create-launch-template.md") that is
referenced in the Spot Fleet request.

###### Note

Volume tags are only supported for volumes that are attached to On-Demand Instances. You
can't tag volumes that are attached to Spot Instances.

Volume tagging in `LaunchSpecifications` is not supported.

## Tag an existing Spot Fleet

###### To tag an existing Spot Fleet request using the console

After you create a Spot Fleet request, you can add tags to the fleet request using
the console.

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Fleet request.
4. Choose the **Tags** tab and choose **Create
   Tag**.

###### To tag an existing Spot Fleet request using the AWS CLI

You can use the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") command to tag existing resources. In the following
example, the existing Spot Fleet request is tagged with Key=purpose and
Value=test.

```
aws ec2 create-tags \
    --resources `sfr-11112222-3333-4444-5555-66666EXAMPLE` \
    --tags Key=`purpose`,Value=`test`
```

## View Spot Fleet request tags

###### To view Spot Fleet request tags using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Spot Requests**.
3. Select your Spot Fleet request and choose the **Tags**
   tab.

###### To describe Spot Fleet request tags

Use the [describe-tags](../../../cli/latest/reference/ec2/describe-tags.md "../../../cli/latest/reference/ec2/describe-tags.md") command to view the tags for the specified resource.
In the following example, you describe the tags for the specified Spot Fleet
request.

```
aws ec2 describe-tags \
    --filters "Name=resource-id,Values=`sfr-11112222-3333-4444-5555-66666EXAMPLE`"
```

```
{
    "Tags": [
        {
            "Key": "Environment",
            "ResourceId": "sfr-11112222-3333-4444-5555-66666EXAMPLE",
            "ResourceType": "spot-fleet-request",
            "Value": "Production"
        },
        {
            "Key": "Another key",
            "ResourceId": "sfr-11112222-3333-4444-5555-66666EXAMPLE",
            "ResourceType": "spot-fleet-request",
            "Value": "Another value"
        }
    ]
}
```

You can also view the tags of a Spot Fleet request by describing the Spot Fleet
request.

Use the [describe-spot-fleet-requests](../../../cli/latest/reference/ec2/describe-spot-fleet-requests.md "../../../cli/latest/reference/ec2/describe-spot-fleet-requests.md") command to view the configuration of the
specified Spot Fleet request, which includes any tags that were specified for the fleet
request.

```
aws ec2 describe-spot-fleet-requests \
    --spot-fleet-request-ids `sfr-11112222-3333-4444-5555-66666EXAMPLE`
```

```
{
    "SpotFleetRequestConfigs": [
        {
            "ActivityStatus": "fulfilled",
            "CreateTime": "2020-02-13T02:49:19.709Z",
            "SpotFleetRequestConfig": {
                "AllocationStrategy": "capacityOptimized",
                "OnDemandAllocationStrategy": "lowestPrice",
                "ExcessCapacityTerminationPolicy": "Default",
                "FulfilledCapacity": 2.0,
                "OnDemandFulfilledCapacity": 0.0,
                "IamFleetRole": "arn:aws:iam::111122223333:role/aws-ec2-spot-fleet-tagging-role",
                "LaunchSpecifications": [
                    {
                        "ImageId": "ami-0123456789EXAMPLE",
                        "InstanceType": "c4.large"
                    }
                ],
                "TargetCapacity": 2,
                "OnDemandTargetCapacity": 0,
                "Type": "maintain",
                "ReplaceUnhealthyInstances": false,
                "InstanceInterruptionBehavior": "terminate"
            },
            "SpotFleetRequestId": "sfr-11112222-3333-4444-5555-66666EXAMPLE",
            "SpotFleetRequestState": "active",
            "Tags": [
                {
                    "Key": "Environment",
                    "Value": "Production"
                },
                {
                    "Key": "Another key",
                    "Value": "Another value"
                }
            ]
        }
    ]
}
```
