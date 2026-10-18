

# Tag Image Builder output resources
<a name="tag-resources"></a>

Tagging your resources can be useful for filtering and tracking resource costs, or other categories. You can also control access based on tags. For more information about tag-based authorization, see [Authorization based on Image Builder tags](security_iam_service-with-iam.md#security-iam-service-with-ib-tags)

Image Builder supports the following dynamic tags:
+ `- {{imagebuilder:buildDate}}`

  Resolves to the build date/time at build time.
+ `- {{imagebuilder:buildVersion}}`

  Resolves to a build version, which is a number that is located at the end of an Image Builder Amazon Resource Name (ARN.) For example, `"arn:aws:imagebuilder:us-west-2:123456789012:component/myexample-component/2019.12.02/1"` shows the build version as `1`.

To help you keep track of Amazon Machine Images (AMIs) that you've distributed, Image Builder automatically adds the following tags to your output AMIs.
+ `"CreatedBy":"EC2 Image Builder"`
+ `"Ec2ImageBuilderArn":"arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image/{{simple-recipe-linux}}/{{1.0.0/10}}"`. This tag contains the ARN of the Image Builder image resource that was used to create the AMI.

**Topics**
+ [Tag a resource](#cli-tag-resource)
+ [Untag a resource](#cli-untag-resource)
+ [List the tags for a resource](#cli-list-tags-for-resource)

## Tag a resource
<a name="cli-tag-resource"></a>

------
#### [ AWS CLI ]

The following example shows how to add tags to a resource in EC2 Image Builder. You must provide the `resourceArn` and the tags to apply to it.

The example `tag-resource.json` contents are as follows:

```
{
    "resourceArn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}",
    "tags": {
        "KeyName": "KeyValue"
    }
}
```

Run the following command, which references the preceding `tag-resource.json` file.

```
aws imagebuilder tag-resource --cli-input-json file://tag-resource.json
```

------
#### [ PowerShell ]

The following example shows how to use the [Add-EC2IBResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Add-EC2IBResourceTag.html) cmdlet to add tags to a resource by specifying its Amazon Resource Name (ARN):

```
Add-EC2IBResourceTag -ResourceArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}} `
    -Tag @{{{KeyName}}="{{KeyValue}}"}
```

------

## Untag a resource
<a name="cli-untag-resource"></a>

------
#### [ AWS CLI ]

The following example shows how to remove a tag from a resource. You must provide the `resourceArn` and the keys to remove the tag.

The example `untag-resource.json` contents are as follows:

```
{
    "resourceArn": "arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}",
    "tagKeys": [
        "KeyName"
    ]
}
```

Run the following command, which references the preceding `untag-resource.json` file.

```
aws imagebuilder untag-resource --cli-input-json file://untag-resource.json
```

------
#### [ PowerShell ]

The following example shows how to use the [Remove-EC2IBResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2IBResourceTag.html) cmdlet to remove a tag from a resource by specifying its Amazon Resource Name (ARN):

```
Remove-EC2IBResourceTag -ResourceArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}} `
    -TagKey {{KeyName}}
```

------

## List the tags for a resource
<a name="cli-list-tags-for-resource"></a>

------
#### [ AWS CLI ]

The following example shows how to list all the tags for a specific resource.

```
aws imagebuilder list-tags-for-resource --resource-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBResourceTag](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBResourceTag.html) cmdlet to list all the tags for a specific resource by specifying its Amazon Resource Name (ARN):

```
Get-EC2IBResourceTag -ResourceArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}
```

------