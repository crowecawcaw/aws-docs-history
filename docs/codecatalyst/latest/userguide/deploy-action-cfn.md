Amazon CodeCatalyst is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Deploying an AWS CloudFormation stack

This section describes how to deploy a AWS CloudFormation stack using a CodeCatalyst workflow. To
accomplish this, you must add the **Deploy AWS CloudFormation stack** action to your
workflow. The action deploys a CloudFormation stack of resources into AWS based on a template that
you provide. The template can be a:

- AWS CloudFormation template – For more information, see [Working with AWS CloudFormation
  templates](../../../AWSCloudFormation/latest/UserGuide/template-guide.md "../../../AWSCloudFormation/latest/UserGuide/template-guide.md").
- AWS SAM template – For more information, see [AWS Serverless Application Model
  (AWS SAM) specification](../../../serverless-application-model/latest/developerguide/sam-specification.md "../../../serverless-application-model/latest/developerguide/sam-specification.md").

###### Note

To use a AWS SAM template, you must first package your AWS SAM application using the
`sam package` operation. For a tutorial that shows you how to do this
packaging automatically as part of a Amazon CodeCatalyst workflow, see [Tutorial: Deploy a serverless application](deploy-tut-lambda.md "deploy-tut-lambda.md").
If the stack already exists, the action runs the CloudFormation `CreateChangeSet` operation, and then the `ExecuteChangeSet` operation. The action then waits for the changes to be
deployed and marks itself as either succeeded for failed, depending on the results.

Use the **Deploy AWS CloudFormation stack** action if you already have an AWS CloudFormation or AWS SAM
template that contains resources you'd like to deploy, or you plan on generating one
automatically as part of a workflow [build action](build-add-action.md "build-add-action.md") using
tools like AWS SAM and [AWS Cloud Development Kit (AWS CDK)](../../../cdk/latest/guide/home.md "../../../cdk/latest/guide/home.md").

There are no restrictions on the template you can use—whatever you can author in
CloudFormation or AWS SAM you can use with the **Deploy AWS CloudFormation stack** action.

###### Tip

For a tutorial that shows you how to deploy a serverless application using the
**Deploy AWS CloudFormation stack** action, see [Tutorial: Deploy a serverless application](deploy-tut-lambda.md "deploy-tut-lambda.md").

###### Topics

- [Runtime image used by the 'Deploy AWS CloudFormation stack'
  action](#deploy-action-cfn-runtime "#deploy-action-cfn-runtime")
- [Tutorial: Deploy a serverless application](deploy-tut-lambda.md "deploy-tut-lambda.md")
- [Adding the 'Deploy AWS CloudFormation stack' action](deploy-action-cfn-adding.md "deploy-action-cfn-adding.md")
- [Configuring rollbacks](deploy-consumption-enable-alarms.md "deploy-consumption-enable-alarms.md")
- ['Deploy AWS CloudFormation stack' variables](deploy-action-cfn-variables.md "deploy-action-cfn-variables.md")
- ['Deploy AWS CloudFormation stack' action YAML](deploy-action-ref-cfn.md "deploy-action-ref-cfn.md")

## Runtime image used by the 'Deploy AWS CloudFormation stack'

action

The **Deploy AWS CloudFormation stack** action runs on a [November 2022 image](build-images.md#build.previous-image "build-images.md#build.previous-image"). For more information, see [Active images](build-images.md#build-curated-images "build-images.md#build-curated-images").
