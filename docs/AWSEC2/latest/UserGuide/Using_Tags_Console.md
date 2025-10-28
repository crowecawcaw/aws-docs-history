# Add and remove tags for Amazon EC2 resources

When you create an Amazon EC2 resource, such as an Amazon EC2 instance, you can specify
the tags to add to the resource. You can also use the Amazon EC2 console to display the
tags for a specific Amazon EC2 resource. You can also add or remove tags from an existing
Amazon EC2 resource.

You can use the **Tag Editor** in the AWS Resource Groups console to view,
add, or remove tags across of all of your AWS resources across all Regions.
You can apply or remove tags from multiple types of resources at the same time.
For more information, see the [Tagging AWS Resources User
Guide](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

###### Tasks

- [Add tags using the console](#adding-or-deleting-tags "#adding-or-deleting-tags")
- [Add tags using the AWS CLI](#create-tag-examples "#create-tag-examples")
- [Add tags using PowerShell](#powershell-add-tag-specifications "#powershell-add-tag-specifications")
- [Add tags using CloudFormation](#cloudformation-add-tag-specifications "#cloudformation-add-tag-specifications")

## Add tags using the console

You can add tags to an existing resource directly from the page for a resource.

###### To add tags to an existing resource

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. From the navigation bar, select the Region where the resource is located.
3. In the navigation pane, select a resource type (for example,
   **Instances**).
4. Select the resource from the list.
5. From the **Tags** tab, choose **Manage tags**.
6. Choose **Add new tag** and enter a key and
   a value for the tag.
7. Choose **Save**.

## Add tags using the AWS CLI

You can add tags when you create a resource or to an existing resource.

###### To add a tag on resource creation

Use the `-tag-specifications` option to tag a resource on
creation. A tag specification requires the type of resource to be
tagged, the tag key, and the tag value. The following example creates
a tag and adds it to a tag specification.

```
--tag-specifications 'ResourceType=`instance`,Tags=[{Key=`stack`,Value=`production`}]'
```

###### To add a tag to an existing resource

The following examples demonstrate how to add tags to existing resources using
the [create-tags](../../../cli/latest/reference/ec2/create-tags.md "../../../cli/latest/reference/ec2/create-tags.md") command.

###### Example: Add a tag to a resource

The following command adds the tag `Stack=production` to the specified
image, or overwrites an existing tag for the AMI where the tag key is stack.
If the command succeeds, no output is returned.

```
aws ec2 create-tags \
    --resources `ami-0abcdef1234567890` \
    --tags Key=`stack`,Value=`production`
```

###### Example: Add tags to multiple resources

This example adds (or overwrites) two tags for an AMI and an instance. One of the tags
contains just a key (webserver), with no value (we set the value to
an empty string). The other tag consists of a key (stack) and value
(`Production`). If the command succeeds, no output is returned.

```
aws ec2 create-tags \
    --resources `ami-0abcdef1234567890` `i-1234567890abcdef0` \
    --tags Key=`webserver`,Value=  Key=`stack`,Value=`Production`
```

###### Example: Add tags with special characters

This example adds the tag [Group]=test to an instance. The square
brackets ([ and ]) are special characters,
which must be escaped.

If you are using Linux or OS X, to escape the special characters, enclose the
element with the special character with double quotes ("), and then enclose
the entire key and value structure with single quotes (').

```
aws ec2 create-tags \
    --resources `i-1234567890abcdef0` \
    --tags 'Key="`[Group]`",Value=`test`'
```

If you are using Windows, to escape the special characters, enclose the element
that has special characters with double quotes ("), and then precede each double quote
character with a backslash (`\`) as follows:

```
aws ec2 create-tags ^
    --resources `i-1234567890abcdef0` ^
    --tags Key=\"`[Group]`\",Value=`test`
```

If you are using Windows PowerShell, to escape the special characters, enclose the value
that has special characters with double quotes (`"`), precede each double
quote character with a backslash (`\`), and then enclose the entire key and
value structure with single quotes (`'`) as follows:

```
aws ec2 create-tags `
    --resources `i-1234567890abcdef0` `
    --tags 'Key=\"`[Group]`\",Value=`test`'
```

## Add tags using PowerShell

You can add tags when you create a resource or to an existing resource.

###### To add a tag on resource creation

Use the `-TagSpecification` parameter to tag a resource on
creation. A tag specification requires the type of resource to be
tagged, the tag key, and the tag value. The following example creates
a tag and adds it to a tag specification.

```
$tag = @{Key="`stack`"; Value="`production`"}
$tagspec = new-object Amazon.EC2.Model.TagSpecification
$tagspec.ResourceType = "`instance`"
$tagspec.Tags.Add($tag)
```

The following example specifies this tag in the `-TagSpecification` parameter.

```
-TagSpecification $tagspec
```

###### To add a tag to an existing resource

Use the [New-EC2Tag](../../../powershell/latest/reference/items/New-EC2Tag.md "../../../powershell/latest/reference/items/New-EC2Tag.md")
cmdlet. You must specify the resource, the tag key, and the tag value.

```
New-EC2Tag `
    -Resource `i-1234567890abcdef0` `
    -Tag @{Key="`purpose`"; Value="`production`"}
```

## Add tags using CloudFormation

With Amazon EC2 resource types, you specify tags using either a `Tags` or
`TagSpecifications` property.

The following examples add the tag `Stack=Production` to [AWS::EC2::Instance](../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.md") using its `Tags` property.

###### Example: Tags in YAML

```
Tags:
  - Key: "Stack"
    Value: "Production"
```

###### Example: Tags in JSON

```
"Tags": [
    {
        "Key": "Stack",
        "Value": "Production"
    }
]
```

The following examples add the tag `Stack=Production` to [AWS::EC2::LaunchTemplate LaunchTemplateData](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-launchtemplatedata.md") using its `TagSpecifications`
property.

###### Example: TagSpecifications in YAML

```
TagSpecifications:
  - ResourceType: "instance"
    Tags:
    - Key: "Stack"
      Value: "Production"
```

###### Example: TagSpecifications in JSON

```
"TagSpecifications": [
    {
        "ResourceType": "instance",
        "Tags": [
            {
                "Key": "Stack",
                "Value": "Production"
            }
        ]
    }
]
```
