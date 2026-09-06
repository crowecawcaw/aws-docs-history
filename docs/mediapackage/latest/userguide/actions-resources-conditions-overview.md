

# Actions, resources, and condition keys in MediaPackage
<a name="actions-resources-conditions-overview"></a>

AWS Elemental MediaPackage (service prefix: `mediapackagev2`) provides service-specific resources, actions, and condition context keys for use in IAM permission policies. For the full list, see [Actions, resources, and condition keys for AWS Elemental MediaPackage](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awselementalmediapackage.html) in the *AWS General Reference*.

## MediaPackage Actions
<a name="actions-overview"></a>

MediaPackage defines a set of permissions that you can specify in a policy. These are keywords, each of which maps to a specific MediaPackage operation. When you use an action in a policy, you usually allow or deny access to the API operation or CLI command with the same name. However, in some cases, a single action controls access to more than one operation. Alternatively, some operations require several different actions.

## MediaPackage resources
<a name="resources-arn-format"></a>

The following common Amazon Resource Name (ARN) format identifies resources in AWS:

```
arn:${Partition}:mediapackagev2:${Region}:${AccountID}:channelGroup/${ChannelGroupName}/channel/${ChannelName}/originEndpoint/${OriginEndpointName}
```

For information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*. 

For information about resources, see [IAM JSON Policy Elements: Resource](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_resource.html) in the *IAM User Guide*.

A MediaPackage ARN includes the following:
+ **Partition** ‐ `aws` is a common partition name. If your resources are in the China (Beijing) Region, `aws-cn` is the partition name.
+ **Region** ‐ The AWS Region.
+ **AccountID** ‐ Your AWS account number.
+ **ChannelGroupName** ‐ The name of the channel group.
+ **ChannelName** ‐ The name of the channel.
+ **OriginEndpointName** ‐ The name of the origin endpoint.

## MediaPackage Conditions keys
<a name="conditions-overview"></a>

The access policy language enables you to specify conditions when granting permissions. To specify conditions for when a policy is in effect, you can use the optional Condition element, or Condition block, to specify conditions for when a policy is in effect. You can use predefined AWS‐wide keys and MediaPackage‐specific keys to specify conditions in an MediaPackage access policy. In the Condition element, you build expressions in which you use Boolean operators (equal, less than, etc.) to match your condition against values in the request.