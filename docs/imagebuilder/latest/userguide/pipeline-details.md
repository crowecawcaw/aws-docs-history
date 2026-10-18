

# List and view pipeline details
<a name="pipeline-details"></a>

This section describes the various ways that you can find information and view details for your EC2 Image Builder image pipelines.

**Topics**
+ [List image pipelines](#cli-list-image-pipelines)
+ [Get image pipeline details](#cli-get-image-pipeline-details)

## List image pipelines
<a name="cli-list-image-pipelines"></a>

------
#### [ AWS CLI ]

The following example shows how to use the **list-image-pipelines** command in the AWS CLI to list all of your image pipelines.

```
aws imagebuilder list-image-pipelines
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBImagePipelineList](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBImagePipelineList.html) cmdlet to list all of your image pipelines:

```
Get-EC2IBImagePipelineList
```

------

## Get image pipeline details
<a name="cli-get-image-pipeline-details"></a>

------
#### [ AWS CLI ]

The following example shows how to use the **get-image-pipeline** command in the AWS CLI to get the details about an image pipeline through its ARN.

```
aws imagebuilder get-image-pipeline --image-pipeline-arn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}
```

------
#### [ PowerShell ]

The following example shows how to use the [Get-EC2IBImagePipeline](https://docs.aws.amazon.com/powershell/latest/reference/items/Get-EC2IBImagePipeline.html) cmdlet to get the details of an image pipeline by specifying its Amazon Resource Name (ARN):

```
Get-EC2IBImagePipeline -ImagePipelineArn arn:aws:imagebuilder:{{us-west-2}}:{{123456789012}}:image-pipeline/{{my-example-pipeline}}
```

------