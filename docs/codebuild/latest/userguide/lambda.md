# Run builds on AWS Lambda compute

AWS Lambda compute offers optimized start-up speeds for your builds. AWS Lambda supports faster builds due to a lower start-up latency.
AWS Lambda also automatically scales, so builds aren’t waiting in queue to run. However, there are some use-cases which AWS Lambda does not support,
and if they impact you, use the EC2 compute. For more information, see [Limitations of AWS Lambda compute](#lambda.limitations "#lambda.limitations").

###### Topics

- [Which tools and runtimes will be included in the curated runtime environment docker images which run on AWS Lambda?](#lambda.tools "#lambda.tools")
- [What if the curated image doesn't include the tools I need?](#lambda.custom "#lambda.custom")
- [Which regions support AWS Lambda compute in CodeBuild?](#lambda.regions "#lambda.regions")
- [Limitations of AWS Lambda compute](#lambda.limitations "#lambda.limitations")
- [Deploy a Lambda function using AWS SAM with CodeBuild Lambda Java](sample-lambda-sam-gradle.md "sample-lambda-sam-gradle.md")
- [Create a single page React app with CodeBuild Lambda Node.js](sample-lambda-react-nodejs.md "sample-lambda-react-nodejs.md")
- [Update a Lambda function configuration with CodeBuild Lambda Python](sample-lambda-boto3-python.md "sample-lambda-boto3-python.md")

## Which tools and runtimes will be included in the curated runtime environment docker images which run on AWS Lambda?

AWS Lambda supports the following tools: AWS CLI v2, AWS SAM CLI, git, go, Java, Node.js, Python, pip, Ruby, and .NET.

## What if the curated image doesn't include the tools I need?

If the curated image doesn't include the tools you need, you can provide a custom environment Docker image that includes the necessary tools.

###### Note

Lambda does not support functions that use multi-architecture container images. For more information,
see [Create a Lambda function using a container image](../../../lambda/latest/dg/images-create.md#images-reqs "../../../lambda/latest/dg/images-create.md#images-reqs") in the _AWS Lambda Developer Guide_.

Note that you require the following Amazon ECR permissions to use custom images for Lambda compute:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ecr:GetAuthorizationToken"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "ecr:BatchCheckLayerAvailability",
 "ecr:GetDownloadUrlForLayer",
 "ecr:BatchGetImage"
 ],
 "Resource": "arn:aws:ecr:us-east-1:`111122223333`:repository/`image-repo`"
 }
 ]
}`

```

Also note that `curl` or `wget` must be installed in order to use custom images.

## Which regions support AWS Lambda compute in CodeBuild?

In CodeBuild, AWS Lambda compute is supported in the following AWS Regions: US East (N. Virginia), US East (Ohio), US West (Oregon), Asia Pacific (Mumbai),
Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Europe (Frankfurt), Europe (Ireland), and South America (São Paulo). For more information about AWS Regions
where CodeBuild is available, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/ "https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/").

## Limitations of AWS Lambda compute

There are some use-cases which AWS Lambda does not
support, and if they impact you, use the EC2 compute:

- AWS Lambda doesn't support tools that require root permissions. For tools such
  as `yum` or `rpm`, use the EC2 compute type or other
  tools that don't require root permissions.
- AWS Lambda doesn't support Docker builds or runs.
- AWS Lambda doesn't support writing to files outside `/tmp`. The included package
  managers are configured to use the `/tmp` directory by default for downloading and referencing packages.
- AWS Lambda doesn't support the environment type `LINUX_GPU_CONTAINER` and isn't supported on Windows Server Core 2019.
- AWS Lambda doesn't support caching, custom build timeouts, queue timeout, build badges, privileged mode, custom runtime environments, or runtimes longer than 15 minutes.
- AWS Lambda doesn't support VPC connectivity, a fixed range of CodeBuild source IP addresses, EFS, installing certificates, or SSH access with Session Manager.
