# Invoking AWS ParallelCluster API

The AWS ParallelCluster Amazon API Gateway endpoint is configured with [`AWS_IAM` authorization type](../../../apigateway/latest/developerguide/permissions.md#api-gateway-control-access-iam-permissions-model-for-calling-api "../../../apigateway/latest/developerguide/permissions.md#api-gateway-control-access-iam-permissions-model-for-calling-api"), and requires all requests to be SigV4 signed with valid
IAM credentials ([API
reference: making http requests](../../../apigateway/api-reference/making-http-requests.md "../../../apigateway/api-reference/making-http-requests.md")).

When deployed with default settings, API invoke permissions are only granted to the default
IAM user created with the API.

To retrieve the ARN of the default IAM user, run:

```
`$` `REGION=`<region>``
`$` `API_STACK_NAME=`<stack-name>``
`$` `aws cloudformation describe-stacks --region ${REGION} --stack-name ${API_STACK_NAME} --query "Stacks[0].Outputs[?OutputKey=='ParallelClusterApiUserRole'].OutputValue" --output text`
```

To obtain temporary credentials for the default IAM user, run the [STS AssumeRole](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sts/assume-role.html") command.

To retrieve the AWS ParallelCluster API endpoint run the following command:

```
`$` `REGION=`<region>``
`$` `API_STACK_NAME=`<stack-name>``
`$` `aws cloudformation describe-stacks --region ${REGION} --stack-name ${API_STACK_NAME} --query "Stacks[0].Outputs[?OutputKey=='ParallelClusterApiInvokeUrl'].OutputValue" --output text`
```

The AWS ParallelCluster API can be invoked by any HTTP client that complies with the OpenAPI
specifications that can be found here:

```
https://`<REGION>`-aws-parallelcluster.s3.`<REGION>`.amazonaws.com/parallelcluster/`<VERSION>`/api/ParallelCluster.openapi.yaml
```

Requests need to be SigV4 signed as documented [here](../../../apigateway/api-reference/signing-requests.md "../../../apigateway/api-reference/signing-requests.md").

At this time, we do not offer any official API client implementation. However, you can use the
[OpenAPI Generator](https://openapi-generator.tech/ "https://openapi-generator.tech/") to easily generate API clients
from the OpenAPI model. Once the client is generated, SigV4 signing needs to be added if
not provided out of the box.

A reference implementation for a Python API client can be found in the [AWS ParallelCluster
repository](https://github.com/aws/aws-parallelcluster/tree/develop/api/client/src "https://github.com/aws/aws-parallelcluster/tree/develop/api/client/src"). To learn more about how you can use the Python API client, see the [Using the AWS ParallelCluster API](tutorials_06_API_use.md "tutorials_06_API_use.md") tutorial.

To implement more advanced access control mechanisms, such as Amazon Cognito or Lambda Authorizers,
or to further protect the API with AWS WAF or API keys, follow the [Amazon API Gateway
documentation](../../../apigateway/latest/developerguide/apigateway-control-access-to-api.md "../../../apigateway/latest/developerguide/apigateway-control-access-to-api.md").

###### Warning

An IAM user that is authorized to invoke the AWS ParallelCluster API, can indirectly
control all AWS resources managed by AWS ParallelCluster in the AWS account. This includes
the creation of AWS resources that the user can't control directly due to restrictions
on the user IAM policy. For example, the creation of a AWS ParallelCluster cluster, depending
on its configuration, might include the deployment of Amazon EC2 instances, Amazon Route 53, Amazon Elastic File System
file systems, Amazon FSx file systems, IAM roles, and resources from other AWS services used
by AWS ParallelCluster that the user might not have direct control over.

###### Warning

When you create a cluster with `AdditionalIamPolicies` specified in the configuration,
the additional policies must match one of the following patterns:

```
- !Sub arn:${AWS::Partition}:iam::${AWS::AccountId}:policy/parallelcluster*
- !Sub arn:${AWS::Partition}:iam::${AWS::AccountId}:policy/parallelcluster/*
- !Sub arn:${AWS::Partition}:iam::aws:policy/CloudWatchAgentServerPolicy
- !Sub arn:${AWS::Partition}:iam::aws:policy/AmazonSSMManagedInstanceCore
- !Sub arn:${AWS::Partition}:iam::aws:policy/AWSBatchFullAccess
- !Sub arn:${AWS::Partition}:iam::aws:policy/AmazonS3ReadOnlyAccess
- !Sub arn:${AWS::Partition}:iam::aws:policy/service-role/AWSBatchServiceRole
- !Sub arn:${AWS::Partition}:iam::aws:policy/service-role/AmazonEC2ContainerServiceforEC2Role
- !Sub arn:${AWS::Partition}:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy
- !Sub arn:${AWS::Partition}:iam::aws:policy/service-role/AmazonEC2SpotFleetTaggingRole
- !Sub arn:${AWS::Partition}:iam::aws:policy/EC2InstanceProfileForImageBuilder
- !Sub arn:${AWS::Partition}:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

If you need other additional policies, you can do one of the following:

- Edit the `DefaultParallelClusterIamAdminPolicy` in:

```
https://`<REGION>`-aws-parallelcluster.s3.`<REGION>`.amazonaws.com/parallelcluster/`<VERSION>`/api/parallelcluster-api.yaml
```

Add the policy in the `ArnLike/iam:PolicyARN` section.

- Don't specify policies for `AdditionalIamPolicies` in the configuration
  file and manually add policies to the AWS ParallelCluster Instance Role created within
  the cluster.
