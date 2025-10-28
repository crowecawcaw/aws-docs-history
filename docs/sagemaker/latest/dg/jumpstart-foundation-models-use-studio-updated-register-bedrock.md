# Use your

SageMaker JumpStart Models in Amazon Bedrock

You can register the models that you've deployed from Amazon SageMaker JumpStart to Amazon Bedrock. With
Amazon Bedrock, you can host your model behind multiple endpoints. You can also use Amazon Bedrock
features, such as Agents and Knowledge Bases. For more information about using
Amazon Bedrock's models, see [https://docs.aws.amazon.com/bedrock/latest/userguide/amazon-bedrock-marketplace.html](../../../bedrock/latest/userguide/amazon-bedrock-marketplace.md "../../../bedrock/latest/userguide/amazon-bedrock-marketplace.md").

###### Important

To migrate your models to Amazon Bedrock, we recommend attaching [AmazonBedrockFullAccess](../../../aws-managed-policy/latest/reference/AmazonBedrockFullAccess.md "../../../aws-managed-policy/latest/reference/AmazonBedrockFullAccess.md") policy to your IAM role. If you can't
attach the managed policy, make sure your IAM role has the following
permissions:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BedrockAll",
 "Effect": "Allow",
 "Action": [
 "bedrock:*"
 ],
 "Resource": "*"
 },
 {
 "Sid": "DescribeKey",
 "Effect": "Allow",
 "Action": [
 "kms:DescribeKey"
 ],
 "Resource": "arn:*:kms:*:::*"
 },
 {
 "Sid": "APIsWithAllResourceAccess",
 "Effect": "Allow",
 "Action": [
 "iam:ListRoles",
 "ec2:DescribeVpcs",
 "ec2:DescribeSubnets",
 "ec2:DescribeSecurityGroups"
 ],
 "Resource": "*"
 },
 {
 "Sid": "MarketplaceModelEndpointMutatingAPIs",
 "Effect": "Allow",
 "Action": [
 "sagemaker:CreateEndpoint",
 "sagemaker:CreateEndpointConfig",
 "sagemaker:CreateModel",
 "sagemaker:CreateInferenceComponent",
 "sagemaker:DeleteInferenceComponent",
 "sagemaker:DeleteEndpoint",
 "sagemaker:UpdateEndpoint"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:endpoint/*",
 "arn:aws:sagemaker:*:*:endpoint-config/*",
 "arn:aws:sagemaker:*:*:model/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "bedrock.amazonaws.com"
 }
 }
 },
 {
 "Sid": "BedrockEndpointTaggingOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:AddTags",
 "sagemaker:DeleteTags"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:endpoint/*",
 "arn:aws:sagemaker:*:*:endpoint-config/*",
 "arn:aws:sagemaker:*:*:model/*"
 ]
 },
 {
 "Sid": "MarketplaceModelEndpointNonMutatingAPIs",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeEndpoint",
 "sagemaker:DescribeEndpointConfig",
 "sagemaker:DescribeModel",
 "sagemaker:DescribeInferenceComponent",
 "sagemaker:ListEndpoints",
 "sagemaker:ListTags"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:endpoint/*",
 "arn:aws:sagemaker:*:*:endpoint-config/*",
 "arn:aws:sagemaker:*:*:model/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "bedrock.amazonaws.com"
 }
 }
 },
 {
 "Sid": "BedrockEndpointInvokingOperations",
 "Effect": "Allow",
 "Action": [
 "sagemaker:InvokeEndpoint",
 "sagemaker:InvokeEndpointWithResponseStream"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:*:endpoint/*"
 ],
 "Condition": {
 "StringEquals": {
 "aws:CalledViaLast": "bedrock.amazonaws.com"
 }
 }
 },
 {
 "Sid": "DiscoveringMarketplaceModel",
 "Effect": "Allow",
 "Action": [
 "sagemaker:DescribeHubContent"
 ],
 "Resource": [
 "arn:aws:sagemaker:*:aws:hub-content/SageMakerPublicHub/Model/*",
 "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
 ]
 },
 {
 "Sid": "AllowMarketplaceModelsListing",
 "Effect": "Allow",
 "Action": [
 "sagemaker:ListHubContents"
 ],
 "Resource": "arn:aws:sagemaker:*:aws:hub/SageMakerPublicHub"
 },
 {
 "Sid": "RetrieveSubscribedMarketplaceLicenses",
 "Effect": "Allow",
 "Action": [
 "license-manager:ListReceivedLicenses"
 ],
 "Resource": [
 "*"
 ]
 },
 {
 "Sid": "PassRoleToSageMaker",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": [
 "arn:aws:iam::*:role/*Sagemaker*ForBedrock*"
 ],
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "sagemaker.amazonaws.com",
 "bedrock.amazonaws.com"
 ]
 }
 }
 },
 {
 "Sid": "PassRoleToBedrock",
 "Effect": "Allow",
 "Action": [
 "iam:PassRole"
 ],
 "Resource": "arn:aws:iam::*:role/*AmazonBedrock*",
 "Condition": {
 "StringEquals": {
 "iam:PassedToService": [
 "bedrock.amazonaws.com"
 ]
 }
 }
 }
 ]
 }`

```

###### Important

The Amazon Bedrock Full Access policy only provides permissions to the Amazon Bedrock API. To use Amazon Bedrock
in the AWS Management Console, your IAM role must also have the following permissions:

```
{
        "Sid": "AllowConsoleS3AccessForBedrockMarketplace",
        "Effect": "Allow",
        "Action": [
          "s3:GetObject",
          "s3:GetBucketCORS",
          "s3:ListBucket",
          "s3:ListBucketVersions",
          "s3:GetBucketLocation"
        ],
        "Resource": "*"
    }

```

If you’re writing your own policy, you must include the policy statement
that allows the Amazon Bedrock Marketplace action for the resource. For example, the
following policy allows Amazon Bedrock to use the `InvokeModel` operation
for a model that you’ve deployed to an endpoint.

JSON

```
`{

 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "BedrockAll",
 "Effect": "Allow",
 "Action": [
 "bedrock:InvokeModel"
 ],
 "Resource": [
 "arn:aws:bedrock:us-east-1:`111122223333`:marketplace/`model-endpoint`/all-access"
 ]
 },
 {
 "Sid": "VisualEditor1",
 "Effect": "Allow",
 "Action": ["sagemaker:InvokeEndpoint"],
 "Resource": "arn:aws:sagemaker:us-east-1:`111122223333`:endpoint/*",
 "Condition": {
 "StringEquals": {
 "aws:ResourceTag/project": "`example-project-id`",
 "aws:CalledViaLast": "bedrock.amazonaws.com"
 }
 }
 }
 ]

}`

```

After you've deployed a model, you might be able to use it in Amazon Bedrock. To see if
you can use it in Amazon Bedrock, navigate to the model detail card in the Studio UI.
If the model card says that it's **Bedrock Ready**, you can
register the model with Amazon Bedrock.

###### Important

By default Amazon SageMaker JumpStart disables network access for the models that you
deploy. If you've enabled network access, you won't be able to use the model
with Amazon Bedrock. If you want to use the model with Amazon Bedrock, you must redeploy it with
network access disabled.

To use it with Amazon Bedrock, navigate to the **Endpoint details**
page and choose **Use with Bedrock** in the upper right corner
of the Studio UI. After you see the pop-up, choose **Register to
Bedrock**.
