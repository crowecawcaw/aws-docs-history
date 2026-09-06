

# CloudFormation
<a name="getting-started-step2-Automation-CFN"></a>

**AWS CloudFormation**

AWS CloudFormation (CloudFormation) enables you to create and provision AWS infrastructure deployments predictably and repeatedly. It helps you leverage AWS products such as Amazon EC2, Amazon Elastic Block Store (EBS), Amazon SNS, Elastic Load Balancing, and Application Auto Scaling to build highly reliable, highly scalable, cost-effective applications in the cloud without worrying about creating and configuring the underlying AWS infrastructure. CloudFormation enables you to use a template file to create and delete a collection of resources together as a single unit (a stack).

You can use the Resource Tags property to apply tags to resources, which can help you identify and categorize those resources. You can only tag CloudFormation supported resources. For information about which resources you can tag with CloudFormation, see the [AWS resources and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the *CloudFormation user guide*. For more information on how to use CloudFormation, see the [Resource tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) in the *CloudFormation user guide*.



Replace `mig12345` with the tag value needed for your migrated resource followed by your MAP term agreement number in following example:

```
{
    "Key" : "map-migrated",
    "Value" : "{{mig12345}}"
}
```

**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

Depending on your migrated resource and MPE ID, the tag value can be any of the following: 



## Short MPE IDs
<a name="cfn-short-ids"></a>
+ `mig{{5-digit MPE ID}}` 
+ `sap{{5-digit MPE ID}}` 
+ `oracle{{5-digit MPE ID}}`

## Long MPE IDs
<a name="cfn-long-ids"></a>
+ `mig{{10 alphanumeric MPE ID characters}}` 
+ `sap{{10 alphanumeric MPE ID characters}}`
+ `oracle{{10 alphanumeric MPE ID characters}}`





**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your MPE ID, see [MPE ID length](mpe-length.md).