

# AWS Cloud Development Kit (AWS CDK)
<a name="getting-started-step2-Automation-CDK"></a>

The AWS Cloud Development Kit (AWS CDK) (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages. A tag in AWS CDK is applied to a given construct that also applies to all of its taggable children. These tags are included in the AWS CloudFormation template synthesized from your application and are applied to the AWS resources it deploys. For more information about AWS CDK tagging, see [Tagging](https://docs.aws.amazon.com/cdk/v2/guide/tagging.html) in the *AWS Cloud Development Kit (AWS CDK) v2 developer guide*. 



Replace `mig12345` with the tag value needed for your migrated resource followed by your MAP term agreement number in following example:

```
import { Tags } from 'aws-cdk-lib';

Tags.of(myConstruct).add('map-migrated', '{{mig12345}}');
```

**Note**  
The Migration Acceleration Program requires that you tag resources with the `map-migrated` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

Depending on your migrated resource and MPE ID, the tag value can be any of the following: 



## Short MPE IDs
<a name="cdk-short-ids"></a>
+ `mig{{5-digit MPE ID}}` 
+ `sap{{5-digit MPE ID}}` 
+ `oracle{{5-digit MPE ID}}`

## Long MPE IDs
<a name="cdk-long-ids"></a>
+ `mig{{10 alphanumeric MPE ID characters}}` 
+ `sap{{10 alphanumeric MPE ID characters}}`
+ `oracle{{10 alphanumeric MPE ID characters}}`



**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes and uppercase letters for the alphanumeric MPE IDs (long MPE IDs). For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your MPE ID, see [MPE ID length](mpe-length.md).