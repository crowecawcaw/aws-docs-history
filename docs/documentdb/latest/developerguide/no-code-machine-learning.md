# No-code machine learning with Amazon SageMaker AI Canvas

[Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md") enables you to build your own AI/ML models without having to write a single line of code.
You can build ML models for common use cases such as regression and forecasting and can access and evaluate foundation models (FMs) from Amazon Bedrock.
You can also access public FMs from Amazon SageMaker AI JumpStart for content generation, text extraction, and text summarization to support generative AI solutions.

## How to build no-code ML models with SageMaker AI Canvas

Amazon DocumentDB now integrates with Amazon SageMaker AI Canvas to enable no-code machine learning (ML) with data stored in Amazon DocumentDB.
You can now build ML models for regression and forecasting needs and use foundation models for content summarization and generation using data stored in Amazon DocumentDB without writing a single line of code.

SageMaker AI Canvas provides a visual interface that allows Amazon DocumentDB customers to generate predictions without requiring any AI/ML expertise or write a single line of code.
Customers can now launch the SageMaker AI Canvas workspace from the AWS Management Console, import and join Amazon DocumentDB data for data preparation and model training.
Data in Amazon DocumentDB can now be used in SageMaker AI Canvas to build and augment models to predict customer churn, detect fraud, predict maintenance failures, forecast business metrics, and generate content.
Customers can now publish and share ML-driven insights across teams using SageMaker AI Canvas’s native integration with Quick Suite.
Data ingestion pipelines in SageMaker AI Canvas run on Amazon DocumentDB secondary instances by default, ensuring that the performance of application and SageMaker AI Canvas ingestion workloads are not hindered.

Amazon DocumentDB customers can get started with SageMaker AI Canvas by navigating to the new Amazon DocumentDB No-Code ML Console page and connecting to new or available SageMaker AI Canvas workspaces.

## Configuring the SageMaker AI domain and user profile

You can connect to Amazon DocumentDB clusters from SageMaker AI domains that are running in VPC Only mode.
By launching a SageMaker AI domain in your VPC, you can control the data flow from your SageMaker AI Studio and Canvas environments.
This allows you to restrict internet access, monitor and inspect traffic using standard AWS networking and security capabilities, and connect to other AWS resources through VPC endpoints.
Please refer to [Amazon SageMaker AI Canvas Getting started](../../../sagemaker/latest/dg/canvas-getting-started.md "../../../sagemaker/latest/dg/canvas-getting-started.md") and [Configure Amazon SageMaker AI Canvas in a VPC without internet access](../../../sagemaker/latest/dg/canvas-vpc.md "../../../sagemaker/latest/dg/canvas-vpc.md") located in the _Amazon SageMaker AI Developer Guide_ to create your SageMaker AI domain to connect to your Amazon DocumentDB cluster.

## Configuring IAM access permissions for Amazon DocumentDB and SageMaker AI Canvas

An Amazon DocumentDB user that has `AmazonDocDBConsoleFullAccess` attached to their associated role and identity can access the AWS Management Console.
Add the following actions to the aforementioned role or identity to provide access to no-code machine learning with Amazon SageMaker AI Canvas.

```
"sagemaker:CreatePresignedDomainUrl",
"sagemaker:DescribeDomain",
"sagemaker:ListDomains",
"sagemaker:ListUserProfiles"

```

## Creating database users and roles for SageMaker AI Canvas

You can restrict access to the actions that users can perform on databases using role-based access control (RBAC) in Amazon DocumentDB.
RBAC works by granting one or more roles to a user.
These roles determine the operations that a user can perform on database resources.

As a Canvas user, you connect to a Amazon DocumentDB database with username and password credentials.
You can create a database user/role for a Canvas user that has read access to the specific databases using Amazon DocumentDB RBAC functionality.

For example, use the `createUser` operation:

```
db.createUser({
user: "canvas_user",
pwd: "<insert-password>",
roles: [{role: "read", db: "sample-database-1"}]
})
```

This creates a `canvas_user` which has read permissions to the `sample-database-1` database.
Your Canvas analysts can use this credential to access data in your Amazon DocumentDB cluster.
Refer to [Database access using Role-Based
Access Control](role_based_access_control.md "role_based_access_control.md") to learn more.

## Available regions

The no-code integration is available in regions where both Amazon DocumentDB and Amazon SageMaker AI Canvas are supported.
The regions include:

- us-east-1 (N. Virginia)
- us-east-2 (Ohio)
- us-west-2 (Oregon)
- ap-northeast-1 (Tokyo)
- ap-northeast-2 (Seoul)
- ap-south-1 (Mumbai)
- ap-southeast-1 (Singapore)
- ap-southeast-2 (Sydney)
- eu-central-1 (Frankfurt)
- eu-west-1 (Ireland)

Please refer to [Amazon SageMaker AI Canvas](../../../sagemaker/latest/dg/canvas.md "../../../sagemaker/latest/dg/canvas.md") in the _Amazon SageMaker AI Developer Guide_ for the latest region availability.
