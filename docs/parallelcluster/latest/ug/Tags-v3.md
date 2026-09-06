

# `Tags` section
<a name="Tags-v3"></a>

**(Optional), Array** Defines the tags that are used by CloudFormation and propagated to all the cluster resources. For more information, see [CloudFormation resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *AWS CloudFormation User Guide*.

```
Tags:
  - Key: {{string}}
    Value: {{string}}
```

[Update policy: This setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3)

## `Tags` properties
<a name="Tags-v3.properties"></a>

`Key` (**Required**, `String`)  
Defines the name of the tag.  
[Update policy: This setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3)

`Value` (**Required**, `String`)  
Defines the value of the tag.  
[Update policy: This setting can be changed during an update.](using-pcluster-update-cluster-v3.md#update-policy-setting-supported-v3)

**Note**  
Starting with AWS ParallelCluster 3.15.0, Tag updates are supported with the following limitations:  
EBS Volume on HeadNode - Will only retain the tags from when the cluster was created; updating tags on this EBS volume is not supported.
Running Nodes - Tag updates will not be applied to running compute or login nodes.