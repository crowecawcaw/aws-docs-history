

# Working with Tags by Using the Amazon WorkSpaces Applications API, an AWS SDK, or AWS CLI
<a name="basic-tagging-API-SDK-CLI"></a>

If you're using the WorkSpaces Applications API, an AWS SDK, or the AWS Command Line Interface (AWS CLI), you can use the following WorkSpaces Applications operations with the `tags` parameter to add tags when you create new resources. 

**Note**  
You can use spaces in tag keys and values. To indicate a space when you use the AWS CLI, use "\\s" (without the quotation marks).


| Task | AWS CLI | API Operation | 
| --- | --- | --- | 
| Add one or more tags for a new fleet | [create-fleet](https://docs.aws.amazon.com/cli/latest/reference/appstream/create-fleet.html)  | [CreateFleet](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateFleet.html#AppStream2-CreateFleet-request-Tags) | 
| Add one or more tags for a new image builder | [create-imagebuilder](https://docs.aws.amazon.com/cli/latest/reference/appstream/create-imagebuilder.html) | [CreateImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImageBuilder.html#AppStream2-CreateImageBuilder-request-Tags) | 
| Add one or more tags for a new stack | [create-stack](https://docs.aws.amazon.com/cli/latest/reference/appstream/create-stack.html) | [CreateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStack.html#AppStream2-CreateStack-request-Tags) | 

You can use the following WorkSpaces Applications operations to add, edit, remove, or list tags for existing resources: 


| Task | AWS CLI | API Operation | 
| --- | --- | --- | 
| Add or overwrite one or more tags for a resource | [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/appstream/tag-resource.html)  | [TagResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_TagResource.html) | 
| Remove one or more tags for a resource | [untag-resource](https://docs.aws.amazon.com/cli/latest/reference/appstream/untag-resource.html) | [UntagResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_UntagResource.html) | 
| List one or more tags for a resource | [list-tags-for-resource](https://docs.aws.amazon.com/cli/latest/reference/appstream/list-tags-for-resource.html) | [ListTagsForResource](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ListTagsForResource.html) | 

When you use the WorkSpaces Applications API, an AWS SDK, or AWS CLI actions to add, edit, remove, or list tags for an existing WorkSpaces Applications resource, specify the resource by using its Amazon Resource Name (ARN). An ARN uniquely identifies an AWS resource and uses the following general syntax.

```
arn:aws:appstream:{{region}}:{{account}}:{{resourceType}}/{{resourceName}}
```

**{{region}}**  
The AWS Region in which the resource was created (for example, `us-east-1`).

**{{account}}**  
The AWS account ID, with no hyphens (for example, `123456789012`).

**{{resourceType}}**  
The type of resource. You can tag the following WorkSpaces Applications resource types: `image-builder`, `image`, `fleet`, and `stack`.

**{{resourceName}}**  
The name of the resource.

For example, you can obtain the ARN for an WorkSpaces Applications fleet by using the AWS CLI [describe-fleets ](https://docs.aws.amazon.com/cli/latest/reference/appstream/describe-fleets.html)command. Copy the following command.

```
aws appstream describe-fleets
```

For an environment that contains a single fleet named `TestFleet`, the ARN for this resource would appear in the JSON output similar to the following. 

```
"Arn": "arn:aws:appstream:us-east-1:123456789012:fleet/TestFleet"
```

After you obtain the ARN for this resource, you can add two tags by using the [tag-resource](https://docs.aws.amazon.com/cli/latest/reference/appstream/tag-resource.html) command: 

```
aws appstream tag-resource --resource arn:awsappstream:us-east-1:123456789012:fleet/TestFleet --tags Environment=Test,Department=IT
```

The first tag, `Environment=Test`, indicates that the fleet is in a test environment. The second tag, `Department=IT`, indicates that the fleet is in the IT department. 

You can use the following command to list the two tags that you added to the fleet.

```
aws appstream list-tags-for-resource --resource arn:aws:appstream:us-east-1:123456789012:fleet/TestFleet
```

For this example, the JSON output appears as follows: 

```
{
    "Tags": {
       "Environment" : "Test",
       "Department" : "IT"
    }
}
```