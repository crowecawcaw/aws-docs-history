

# CloudFormation

**AWS CloudFormation**

AWS CloudFormation (CloudFormation) enables you to create and provision AWS infrastructure deployments predictably and repeatedly. It helps you leverage AWS products such as Amazon EC2, Amazon Elastic Block Store (EBS), Amazon SNS, Elastic Load Balancing, and Application Auto Scaling to build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure. CloudFormation enables you to use a template file to create and delete a collection of resources together as a single unit (a stack).

You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources. You can only tag CloudFormation supported resources. For information about which resources you can tag with CloudFormation, see the [AWS resources and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the *CloudFormation user guide*. For more information on how to use CloudFormation, see the [Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *CloudFormation user guide*.



Replace `migra-abcdefg123456` with the tag value needed for your migrated resource followed by your PRM ID in the following example:

```json
{
    "Key" : "aws-apn-id",
    "Value" : "{{migra-abcdefg123456}}"
}
```

**Note**  
The Migration Acceleration Program requires that you tag resources with the `aws-apn-id` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

Depending on your migrated resource and PRM ID, the tag value can be any of the following: 


+ `mig{{PRM ID}}`
+ `sap{{PRM ID}}`
+ `oracle{{PRM ID}}`





**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes. For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your PRM ID, see [PRM ID length](mpe-length.md).