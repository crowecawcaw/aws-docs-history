# Update the Lambda Insights extension version on a function

As a best practice, we recommend that you keep your Lambda Insights extension updated to the latest version.
The topics in this page explain how to do so.

###### Note

This page explains how to update the extension version used by a function that is already
using Lambda Insights. For information about how to get started with Lambda Insights, see
[Get started with Lambda Insights](Lambda-Insights-Getting-Started.md "Lambda-Insights-Getting-Started.md").

## Use the Lambda console to update the Lambda Insights extension version

Use the following steps to use the Lambda console to update the Lambda Insights extension version.

###### To update using the Lambda console

1. Open the AWS Lambda console at
   [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/ "https://console.aws.amazon.com/lambda/").
2. Choose the name of your function.
3. In the **Layers** section, choose **Edit**.
4. In the list of layers, search for **LambdaInsightsExtension** and then
   change the layer version to the latest version listed in [Available versions of the Lambda Insights extension](Lambda-Insights-extension-versions.md "Lambda-Insights-extension-versions.md").
5. Choose **Save**.

## Use the AWS CLI to update the Lambda Insights extension version

To use the AWS CLI to update the Lambda Insights extension version,
enter the following command. Replace the ARN value for the layers parameter with the ARN matching your Region
and the extension version that you want to use. For information about the latest release version of the
Lambda Insights extension layer, see [Available versions of the Lambda Insights extension](Lambda-Insights-extension-versions.md "Lambda-Insights-extension-versions.md").

```
aws lambda update-function-configuration \
--function-name `function-name` \
--layers "arn:aws:lambda:`us-west-1`:`111122223333`:layer:LambdaInsightsExtension:`53`"

```

## Use the AWS SAM CLI to update the Lambda Insights extension on one or more functions

To update the Lambda Insights Extension version for all of your Lambda functions, update the `Layers` property in the
`Globals` section of your AWS Serverless Application Model (SAM) template with the
ARN of the Lambda Insights layer. For information about the latest release version of the Lambda Insights extension layer,
see [Available versions of the Lambda Insights extension](Lambda-Insights-extension-versions.md "Lambda-Insights-extension-versions.md").

The following updates all of your Lambda functions.

```
Globals:
  Function:
    Layers:
       - !Sub "arn:aws:lambda:${AWS::Region}:`111122223333`:layer:LambdaInsightsExtension:`53`"
```

The following updates just one function.

```
Resources:
  `MyFunction`:
    Type: AWS::Serverless::Function
    Properties:
      Layers:
        - !Sub "arn:aws:lambda:${AWS::Region}:`111122223333`:layer:LambdaInsightsExtension:`53`"
```

## Use CloudFormation to update the Lambda Insights extension on one or more functions

To update the Lambda Insights Extension version by using CloudFormation, update the extension layer in the `Layers`
property within the function's CloudFormation resource, as in the following example.
For information about the latest release version of the Lambda Insights extension layer,
see [Available versions of the Lambda Insights extension](Lambda-Insights-extension-versions.md "Lambda-Insights-extension-versions.md").

```
Resources:
  `MyFunction`:
    Type: AWS::Lambda::Function
    Properties:
      Layers:
        - !Sub "arn:aws:lambda:${AWS::Region}:`111122223333`:layer:LambdaInsightsExtension:`53`"
```

## Use the AWS CDK to update the Lambda Insights extension on one or more functions

You can update the extension version on the Lambda function by replacing the ARN value for the `layerArn` parameter with
the ARN matching your Region and the extension version that you want to use.
For information about the latest release version of the Lambda Insights extension layer,
see [Available versions of the Lambda Insights extension](Lambda-Insights-extension-versions.md "Lambda-Insights-extension-versions.md").

```
import lambda = require('@aws-cdk/aws-lambda');
const layerArn = 'arn:aws:lambda:`us-west-1`:`111122223333`:layer:LambdaInsightsExtension:`53`';
const layer = lambda.LayerVersion.fromLayerVersionArn(this, 'LayerFromArn', layerArn);
```

## Use Serverless Framework to update the Lambda Insights extension on one or more functions

Follow these steps to use Serverless Framework to update the Lambda Insights extension version on an existing Lambda function.
For more information about Serverless Framework, see the [Serverless Framework documentation](https://serverless.com "https://serverless.com").

This method uses a Lambda Insights plugin for Serverless. For more information, see
[serverless-plugin-lambda-insights](https://www.npmjs.com/package/serverless-plugin-lambda-insights "https://www.npmjs.com/package/serverless-plugin-lambda-insights").

If you don't already have the latest version of the Serverless command-line interface installed, you must
first install it or upgrade it. For more information, see
[Setting Up Serverless Framework With AWS](https://www.serverless.com/framework/docs/getting-started/ "https://www.serverless.com/framework/docs/getting-started/").

###### To update using the Lambda console

1. Update Lambda Insights. If you haven't already done so, add a `custom` section at the end
   of the file and specify the Lambda Insights version inside a `lambdaInsightsVersion` property.

```
custom:
    lambdaInsights:
        lambdaInsightsVersion: `53` #specify the Layer Version
```

2. Re-deploy the Serverless service by entering the following command.

```
serverless deploy
```

## Update the Lambda Insights extension version on a Lambda container image deployment

To update Lambda Insights on a Lambda container image, follow the steps in [Enable Lambda Insights on a Lambda container image deployment](Lambda-Insights-Getting-Started-docker.md "Lambda-Insights-Getting-Started-docker.md") to rebuild the image with
the latest version of Lambda Insights. Then, use the AWS CLI to [update the function code](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-code.html") and provide a container image URI as the value for the `--image-uri` parameter.
