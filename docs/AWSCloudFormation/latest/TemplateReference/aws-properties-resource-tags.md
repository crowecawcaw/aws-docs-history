

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# CloudFormation resource tagging
<a name="aws-properties-resource-tags"></a>

You can apply tags to resources by using the `Tags` property in your CloudFormation template, which can help you identify and categorize those resources.

For information about which resources support the `Tags` property, see the individual resources in the [AWS resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-template-resource-type-ref.html). If a resource doesn't yet support the `Tags` property, the resource's service might support tagging using its own API operations. For more information, refer to the documentation for that service.

In addition to any tags you define, CloudFormation automatically creates the following stack-level tags with the `aws:` prefix:
+ `aws:cloudformation:{{logical-id}}`
+ `aws:cloudformation:{{stack-id}}`
+ `aws:cloudformation:{{stack-name}}`

The `aws:` prefix is reserved for AWS use. This prefix is case-insensitive. If you use this prefix in the `Key` or `Value` property, you can't update or delete the tag. Tags with this prefix don't count toward the number of tags per resource.

The propagation of stack-level tags to resources, including tags with the `aws:` prefix, varies by resource type. For example, tags aren't propagated to Amazon EBS volumes that are created from block device mappings. 

**Note**  
Some resources require explicit tag propagation settings. For example, the `AWS::AutoScaling::AutoScalingGroup` resource must have its `PropagateAtLaunch` property set to `true` to propagate tags to its EC2 instances. However, stack-level tags are automatically applied to EC2 instances regardless of the `PropagateAtLaunch` setting.

## Syntax
<a name="w2aac14d552c13c17"></a>

### JSON
<a name="aws-properties-resource-tags-syntax.json"></a>

```
{
  "Key" : {{String}},
  "Value" : {{String}}
}
```

### YAML
<a name="aws-properties-resource-tags-syntax.yaml"></a>

```
Key: {{String}}
Value: {{String}}
```

## Properties
<a name="w2aac14d552c13c19"></a>

`Key`  <a name="cfn-resource-tags-key"></a>
The key name of the tag. You can specify a value that's 1 to 128 Unicode characters in length and can't be prefixed with `aws:`. You can use any of the following characters: the set of Unicode letters, digits, whitespace, `_`, `.`, `:`, `/`, `=`, `+`, `@`, `-`, and `"`.  
*Required*: Yes  
*Type*: String

`Value`  <a name="cfn-resource-tags-value"></a>
The value for the tag. You can specify a value that's 1 to 256 characters in length. You can use any of the following characters: the set of Unicode letters, digits, whitespace, `_`, `.`, `/`, `=`, `+`, and `-`.  
*Required*: Yes  
*Type*: String

## Example
<a name="aws-properties-resource-tags-examples"></a>

This example shows a `Tags` property. You specify this property within the `Properties` section of a resource that supports it. When the resource is created, the `Environment` tag is dynamically set using a parameter, and the `Owner` tag is statically set to `MyName`.

### JSON
<a name="aws-properties-resource-tags-example.json"></a>

```
 1. "Tags" : [
 2.    {
 3.       "Key" : "Environment",
 4.       "Value" : { "Ref": "Environment" }
 5.    },
 6.    {
 7.       "Key" : "Owner",
 8.       "Value" : "MyName"
 9.    }
10. ]
```

### YAML
<a name="aws-properties-resource-tags-example.yaml"></a>

```
1. Tags: 
2.   - Key: Environment
3.     Value: !Ref Environment
4.   - Key: Owner
5.     Value: MyName
```

## See also
<a name="w2aac14d552c13c23"></a>
+ [Configure stack options](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html#configure-stack-options) in the *AWS CloudFormation User Guide*
+ [Viewing CloudFormation stack data and resources on the AWS Management Console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-view-stack-data-resources.html) in the *AWS CloudFormation User Guide*