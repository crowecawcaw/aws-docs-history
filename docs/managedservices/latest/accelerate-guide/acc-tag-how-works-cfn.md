

# Using CloudFormation to create tags for AMS Accelerate
<a name="acc-tag-how-works-cfn"></a>

You can use CloudFormation to apply tags at the stack level (see CloudFormation documentation, [ Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html)) or at the individual resource level (for example, see [ Tagging your Amazon EC2 resources](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Tags.html)).

**Important**  
Some AMS Accelerate service components require tags with the **ams:rt:** prefix. Resource Tagger believes that it owns these tags, and will delete them if no Resource Tagger configuration rules permit them. You always need to deploy a Resource Tagger configuration profile for these tags, even if you are using CloudFormation or Terraform. 