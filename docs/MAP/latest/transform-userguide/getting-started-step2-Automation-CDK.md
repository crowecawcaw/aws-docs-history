

# AWS Cloud Development Kit (AWS CDK)

The AWS Cloud Development Kit (AWS CDK) (AWS CDK) is an open-source software development framework to define your cloud application resources using familiar programming languages. A tag in AWS CDK is applied to a given construct that also applies to all of its taggable children. These tags are included in the AWS CloudFormation template synthesized from your application and are applied to the AWS resources it deploys. For more information about AWS CDK tagging, see [Tagging](https://docs.aws.amazon.com/cdk/v2/guide/tagging.html) in the *AWS Cloud Development Kit (AWS CDK) v2 developer guide*. 



Replace `migra-abcdefg123456` with the tag value needed for your migrated resource followed by your PRM ID in the following example:

```typescript
import { Tags } from 'aws-cdk-lib';

Tags.of(myConstruct).add('aws-apn-id', '{{migra-abcdefg123456}}');
```

**Note**  
The Migration Acceleration Program requires that you tag resources with the `aws-apn-id` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

Depending on your migrated resource and PRM ID, the tag value can be any of the following: 


+ `mig{{PRM ID}}`
+ `sap{{PRM ID}}`
+ `oracle{{PRM ID}}`



**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes. For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your PRM ID, see [PRM ID length](mpe-length.md).