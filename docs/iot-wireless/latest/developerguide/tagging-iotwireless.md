

# Tagging your AWS IoT Wireless resources
<a name="tagging-iotwireless"></a>

To help you manage and organize your devices, gateways, destinations, and profiles, you can optionally assign your own metadata to each of these resources in the form of tags. This section describes tags and shows you how to create them. AWS IoT Wireless doesn't have billing groups, and uses the same billing groups as AWS IoT Core. For more information, see [Billing groups](https://docs.aws.amazon.com/iot/latest/developerguide/tagging-iot-billing-groups.html) in the *AWS IoT Core documentation*.

## Tag basics
<a name="tagging-iotwireless-basics"></a>

When you've several AWS IoT Wireless resources of the same type, you can use tags to categorize your resources in different ways (for example, by purpose, owner, or environment). This helps you quickly identify a resource based on the tags you've assigned to it.

Each tag consists of a key and optional value, both of which you define. For example, you can define a set of tags for a group of LoRaWAN devices for which the device firmware is being updated. To more easily manage your resources, we recommend that you create a consistent set of tag keys that meets your needs for each kind of resource.

You can search for and filter resources based on the tags you add or apply. You can also use tags to control access to your resources by using IAM policies and billing group tags to categorize and track your costs.

## Create and manage tags
<a name="tagging-iotwireless-create"></a>

You can create and manage tags using the Tag Editor in the AWS Management Console, the AWS IoT Wireless, or the AWS CLI

**Using the console**  
For ease of use, the Tag Editor in the AWS Management Console provides a central, unified way to create and manage your tags. For more information, see [What is Tag Editor?](https://docs.aws.amazon.com/tag-editor/latest/userguide/tagging.html) in the *Tagging AWS Resources and Tag Editor User Guide*.

**Using the API or CLI**  
You can also use the API or CLI, and associate tags with wireless devices, gateways, profiles, and destinations when you create then by using the `Tags` field in the following commands:
+ [AssociateAwsAccountWithPartnerAccount](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_AssociateAwsAccountWithPartnerAccount.html)
+ [CreateDestination](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDestination.html)
+ [CreateDeviceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateDeviceProfile.html)
+ [CreateFuotaTask](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateFuotaTask.html)
+ [CreateMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateMulticastGroup.html)
+ [CreateServiceProfile](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateServiceProfile.html)
+ [CreateWirelessGateway](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGateway.html)
+ [CreateWirelessGatewayTaskDefinition](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessGatewayTaskDefinition.html)
+ [CreateWirelessDevice](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_CreateWirelessDevice.html)
+ [StartBulkAssociateWirelessDeviceWithMulticastGroup](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_StartBulkAssociateWirelessDeviceWithMulticastGroup.html)

## Update tags or list tags for resources
<a name="tagging-iotwireless-update"></a>

You can add, modify, or delete tags for existing resources that support tagging by using the following commands:
+ [ TagResource](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_TagResource.html)
+ [ ListTagsForResource](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_ListTagsForResource.html)
+ [ UntagResource](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_UntagResource.html)

You can edit tag keys and values, and you can remove tags from a resource at any time. You can set the value of a tag to an empty string, but you can't set the value of a tag to null. If you add a tag that has the same key as an existing tag on that resource, the new value overwrites the old value. If you delete a resource, any tags associated with the resource are also deleted.

## Tag restrictions and limitations
<a name="tagging-iotwireless-restrict"></a>

The following basic restrictions apply to tags:
+ Maximum number of tags per resource — 50.
+ Maximum key length — 127 Unicode characters in UTF-8.
+ Maximum value length — 255 Unicode characters in UTF-8.
+ Tag keys and values are case sensitive.
+ Do not use the `aws:` prefix in your tag names or values. It's reserved for AWS use. You can't edit or delete tag names or values with this prefix. Tags with this prefix don't count against your tags per resource limit.
+ If your tagging schema is used across multiple services and resources, remember that other services might have restrictions on allowed characters. Allowed characters include letters, spaces, and numbers representable in UTF-8, and the following special characters: \+ - = . \_ : / @. 

## Using tags with IAM policies
<a name="tagging-iot-iam"></a>

To specify what resources a user can create, modify, or use, you can apply tag-based resource-level permissions in the IAM policies you use for AWS IoT Wireless API actions. To control user access (permissions) based on a resource's tags, use the `Condition` element (also called the `Condition` block) with the following condition context keys and values in an IAM policy.
+ Use `aws:ResourceTag/{{tag-key}}: {{tag-value}}` to allow or deny user actions on resources with specific tags.
+ Use `aws:RequestTag/{{tag-key}}: {{tag-value}}` to require that a specific tag be used (or not used) when making an API request to create or modify a resource that allows tags.
+ Use `aws:TagKeys: [{{tag-key}}, ...]` to require that a specific set of tag keys be used (or not used) when making an API request to create or modify a resource that allows tags.

**Note**  
The condition context keys and values in an IAM policy apply only to those AWS IoT actions where an identifier for a resource capable of being tagged is a required parameter. For example, the use of [DescribeEndpoint](https://docs.aws.amazon.com/iot-wireless/latest/apireference/API_DescribeEndpoint.html) is not allowed or denied on the basis of condition context keys and values because no taggable resource is referenced in this request.

For more information about using tags, see [Controlling Access Using Tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) in the *AWS Identity and Access Management User Guide*. The [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) section of that guide has detailed syntax, descriptions, and examples of the elements, variables, and evaluation logic of JSON policies in IAM.

The following example policy applies two tag-based restrictions. An IAM user restricted by this policy:
+ Can't give a resource the tag "env=prod" (in the example, see the line `"aws:RequestTag/env" : "prod"`).
+ Can't modify or access a resource that has an existing tag "env=prod" (in the example, see the line `"aws:ResourceTag/env" : "prod"`).

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Deny",
      "Action": "iotwireless:CreateMulticastGroup",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestTag/env": "prod"
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": [
        "iotwireless:CreateMulticastGroup",
        "iotwireless:UpdateMulticastGroup",
        "iotwireless:GetMulticastGroup"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/env": "prod"
        }
      }
    },
    {
      "Effect": "Deny",
      "Action": "iotwireless:ListMulticastGroups",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "iotwireless:CreateMulticastGroup",
        "iotwireless:UpdateMulticastGroup",
        "iotwireless:GetMulticastGroup",
        "iotwireless:ListMulticastGroups"
      ],
      "Resource": "*"
    }
  ]
}
```

You can also specify multiple tag values for a given tag key by enclosing them in a list, like this: 

```
"StringEquals" : {
              "aws:ResourceTag/env" : ["dev", "test"]
}
```

**Note**  
If you allow or deny users access to resources based on tags, you must consider explicitly denying users the ability to add those tags to or remove them from the same resources. Otherwise, it's possible for a user to circumvent your restrictions and gain access to a resource by modifying its tags.