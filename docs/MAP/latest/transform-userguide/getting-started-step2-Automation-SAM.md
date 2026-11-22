

# AWS Serverless Application Model (SAM)

The AWS Serverless Application Model (SAM) is an open-source framework for building serverless applications. It provides shorthand syntax to express functions, APIs, databases, and event source mappings. You can define the application you want and model it using YAML by using a few lines per resource. During deployment, SAM transforms and expands the SAM syntax into AWS CloudFormation syntax, enabling you to build serverless applications faster. For more information about SAM, see the [Globals section of the AWS SAM template](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-template-anatomy-globals.html) in the *AWS Serverless Application Model developer guide*.



Replace `migra-abcdefg123456` with the tag value needed for your migrated resource followed by your MAP term agreement number in the following example to tag resources at the Global and Resource level:

```yaml
Globals:
  Function:
    Tags:
       aws-apn-id: "{{migra-abcdefg123456}}"

  HttpApi:
    Tags:
       aws-apn-id: "{{migra-abcdefg123456}}"
```

**Note**  
The Migration Acceleration Program requires that you tag resources with the `aws-apn-id` tag. This tag is automatically activated for you as a cost allocation tag. Tags that are automatically activated don't count towards your cost allocation tag quota. For more information, see [Quotas and restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-limits.html). 

Depending on your migrated resource and PRM ID, the tag value can be any of the following: 


+ `mig{{PRM ID}}`
+ `sap{{PRM ID}}`
+ `oracle{{PRM ID}}`



**Note**  
Use lowercase letters for the `mig`, `sap`, and `oracle` prefixes. For more information about what tag values you should use, see [Tagging key combinations](setting-up.md). For more information about your PRM ID, see [PRM ID length](mpe-length.md).