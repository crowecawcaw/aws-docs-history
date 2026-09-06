

Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md).

# Deploying an CloudFormation stack
<a name="deploy-action-cfn"></a>

This section describes how to deploy a AWS CloudFormation stack using a CodeCatalyst workflow. To accomplish this, you must add the **Deploy CloudFormation stack** action to your workflow. The action deploys a CloudFormation stack of resources into AWS based on a template that you provide. The template can be a:
+ CloudFormation template – For more information, see [Working with CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html).
+ AWS SAM template – For more information, see [AWS Serverless Application Model (AWS SAM) specification](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification.html).
**Note**  
To use a AWS SAM template, you must first package your AWS SAM application using the `[sam package](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-package.html)` operation. For a tutorial that shows you how to do this packaging automatically as part of a Amazon CodeCatalyst workflow, see [Tutorial: Deploy a serverless application](deploy-tut-lambda.md).

If the stack already exists, the action runs the CloudFormation `[CreateChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_CreateChangeSet.html)` operation, and then the `[ExecuteChangeSet](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ExecuteChangeSet.html)` operation. The action then waits for the changes to be deployed and marks itself as either succeeded for failed, depending on the results.

Use the **Deploy CloudFormation stack** action if you already have an CloudFormation or AWS SAM template that contains resources you'd like to deploy, or you plan on generating one automatically as part of a workflow [build action](build-add-action.md) using tools like AWS SAM and [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html).

There are no restrictions on the template you can use—whatever you can author in CloudFormation or AWS SAM you can use with the **Deploy CloudFormation stack** action.

**Tip**  
For a tutorial that shows you how to deploy a serverless application using the **Deploy CloudFormation stack** action, see [Tutorial: Deploy a serverless application](deploy-tut-lambda.md).

**Topics**
+ [Runtime image used by the 'Deploy CloudFormation stack' action](#deploy-action-cfn-runtime)
+ [Tutorial: Deploy a serverless application](deploy-tut-lambda.md)
+ [Adding the 'Deploy CloudFormation stack' action](deploy-action-cfn-adding.md)
+ [Configuring rollbacks](deploy-consumption-enable-alarms.md)
+ ['Deploy CloudFormation stack' variables](deploy-action-cfn-variables.md)
+ ['Deploy CloudFormation stack' action YAML](deploy-action-ref-cfn.md)

## Runtime image used by the 'Deploy CloudFormation stack' action
<a name="deploy-action-cfn-runtime"></a>

The **Deploy CloudFormation stack** action runs on a [November 2022 image](build-images.md#build.previous-image). For more information, see [Active images](build-images.md#build-curated-images).