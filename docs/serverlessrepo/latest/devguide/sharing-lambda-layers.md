# Sharing Lambda Layers

If you've implemented functionality in a Lambda layer, you might want to share your
layer without hosting a global instance of it. Sharing layers in this manner enables
others to deploy an instance of your layer to their own account. This prevents client
applications from depending on a global instance of your layer. The AWS Serverless Application Repository enables you to
share Lambda layers in this manner easily.

For more information about Lambda layers, see [AWS Lambda Layers](../../../lambda/latest/dg/configuration-layers.md "../../../lambda/latest/dg/configuration-layers.md")
in the _AWS Lambda Developer Guide_.

## How It Works

The following are the steps for sharing your layer using the AWS Serverless Application Repository. This allows a
copy of your layer to be created in the user's AWS account.

1. Define a serverless application with an AWS SAM template that includes your
   layer as a resource— that is, either an
   [`AWS::Serverless::LayerVersion`](../../../serverless-application-model/latest/developerguide/sam-resource-layerversion.md "../../../serverless-application-model/latest/developerguide/sam-resource-layerversion.md") or an
   [`AWS::Lambda::LayerVersion`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-lambda-layerversion.md") resource.
2. Publish your application to the AWS Serverless Application Repository, and share it (either publicly or
   privately).
3. A customer deploys your application, which creates a copy of your layer in
   their own AWS account. The customer can now reference the Amazon Resource
   Name (ARN) of the layer in their AWS account in their client application.

## Example

The following is an example AWS SAM template for an application that contains the
Lambda layer that you want to share:

```
Resources:
  SharedLayer:
    Type: AWS::Serverless::LayerVersion
    Properties:
      LayerName: shared-layer
      ContentUri: source/layer-code/
      CompatibleRuntimes:
        - python3.7
Outputs:
  LayerArn:
    Value: !Ref SharedLayer
```

When a customer deploys your application from the AWS Serverless Application Repository, a layer is created in
their AWS account. The ARN of the layer looks something like the following:

`arn:aws:lambda:us-east-1:012345678901:layer:shared-layer:1`

The customer can now reference this ARN in their own client
application, like in this example:

```
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      Handler: index.handler
      Runtime: python3.7
      CodeUrl: source/app-code/
      Layers:
        - arn:aws:lambda:us-east-1:012345678901:layer:shared-layer:1
```
