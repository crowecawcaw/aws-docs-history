# List and view pipeline details

This section describes the various ways that you can find information
and view details for your EC2 Image Builder image pipelines.

###### Pipeline details

- [List image pipelines from the AWS CLI](#cli-list-image-pipelines "#cli-list-image-pipelines")
- [Get image pipeline
  details from the AWS CLI](#cli-get-image-pipeline-details "#cli-get-image-pipeline-details")

## List image pipelines from the AWS CLI

The following example shows how to use the **list-image-pipelines**
command in the AWS CLI to list all of
your image pipelines.

```
aws imagebuilder list-image-pipelines
```

## Get image pipeline

details from the AWS CLI

The following example shows how to use the **get-image-pipeline** command in
the AWS CLI to get the details about an image pipeline through its ARN.

```
aws imagebuilder get-image-pipeline --image-pipeline-arn arn:aws:imagebuilder:us-west-`2:123456789012`:image-pipeline/`my-example-pipeline`
```
