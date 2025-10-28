# Deploy your Infrastructure Composer serverless application to the AWS Cloud

Use AWS Infrastructure Composer to design deployment-ready serverless applications. To deploy, use any AWS CloudFormation compatible
service. We recommend using the [AWS Serverless Application Model (AWS SAM)](../../../serverless-application-model/latest/developerguide/what-is-sam.md "../../../serverless-application-model/latest/developerguide/what-is-sam.md").

AWS SAM is an open-source framework that provides developer tools for building and running serverless
applications on AWS. With AWS SAM's shorthand syntax, developers declare AWS CloudFormation resources and specialized serverless resources that are transformed to infrastructure during deployment.

## Important AWS SAM concepts

Before you use AWS SAM, it's important you become familiar with some of its fundemental concepts.

- **[How AWS SAM works](../../../serverless-application-model/latest/developerguide/what-is-sam-overview.md "../../../serverless-application-model/latest/developerguide/what-is-sam-overview.md")**: This topic, which is
  in the _AWS Serverless Application Model Developer Guide_, provides important information on the
  primary components you use to create your serveless application: The AWS SAM CLI, the AWS SAM project, and the AWS SAM template.
- **[How to use AWS Serverless Application Model (AWS SAM)](../../../serverless-application-model/latest/developerguide/chapter-using-sam.md "../../../serverless-application-model/latest/developerguide/chapter-using-sam.md")**: This topic, which
  is in the _AWS Serverless Application Model Developer Guide_, provides a high-level overview of the steps you need to complete to use AWS SAM to deploy your application to the AWS Cloud.

As you design your application in Infrastructure Composer, you can use the **sam sync** command to have the
AWS SAM CLI automatically detect local changes and deploy those changes to AWS CloudFormation.
To learn more, see [Using sam sync](../../../serverless-application-model/latest/developerguide/using-sam-cli-sync.md "../../../serverless-application-model/latest/developerguide/using-sam-cli-sync.md") in the _AWS Serverless Application Model Developer Guide_.

## Next steps

Refer to [Set up for deploying with the AWS SAM CLI and Infrastructure Composer](other-services-cfn-sam-using.md "other-services-cfn-sam-using.md")
to prepare to deploy your application.
