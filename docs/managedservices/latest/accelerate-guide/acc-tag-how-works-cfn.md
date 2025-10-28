# Using CloudFormation to create tags for AMS Accelerate

You can use AWS CloudFormation to apply tags at the stack level (see AWS CloudFormation documentation, [Resource tag](../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.md")) or at the individual resource level (for example, see [Tagging your
Amazon EC2 resources](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md")).

###### Important

Some AMS Accelerate service components require tags with the **ams:rt:** prefix.
Resource Tagger believes that it owns these tags, and will delete them if no Resource Tagger configuration rules permit them.
You always need to deploy a Resource Tagger configuration profile for these tags, even if you are using AWS CloudFormation or Terraform.
