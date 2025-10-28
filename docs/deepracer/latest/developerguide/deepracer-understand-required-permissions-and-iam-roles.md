# Required IAM roles

for AWS DeepRacer to call dependent AWS Services

Before you create a model, use the AWS DeepRacer console to set up resources for your account.
As you do this, the AWS DeepRacer console creates the following IAM roles:

[AWSDeepRacerServiceRole](https://console.aws.amazon.com/iam/home#/roles/AWSDeepRacerServiceRole "https://console.aws.amazon.com/iam/home#/roles/AWSDeepRacerServiceRole")
Allows AWS DeepRacer to create required resources and call AWS services on your behalf.

[AWSDeepRacerSageMakerAccessRole](https://console.aws.amazon.com/iam/home#/roles/AWSDeepRacerSageMakerAccessRole "https://console.aws.amazon.com/iam/home#/roles/AWSDeepRacerSageMakerAccessRole")
Allows Amazon SageMaker AI to create required resources and call AWS services on your behalf.

[AWSDeepRacerLambdaAccessRole](https://console.aws.amazon.com/iam/home#/roles/AWSDeepRacerLambdaAccesseRole "https://console.aws.amazon.com/iam/home#/roles/AWSDeepRacerLambdaAccesseRole")
Allows AWS Lambda functions to call AWS services on your behalf.

[AWSDeepRacerCloudFormationAccessRole](https://console.aws.amazon.com/iam/home#/roles/AWSDeepRacerCloudFormationAccessRole "https://console.aws.amazon.com/iam/home#/roles/AWSDeepRacerCloudFormationAccessRole")

Allows AWS CloudFormation to create and manage AWS stacks and resources on your
behalf.

Follow the links to view detailed access permissions in the AWS IAM console.
