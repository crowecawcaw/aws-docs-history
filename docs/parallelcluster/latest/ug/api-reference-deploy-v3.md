# Deploy the AWS ParallelCluster API with AWS CLI

In this section, you will learn how to deploy with AWS CLI.

Configure AWS Credentials to be used with the CLI if you haven't already done so.

```
`$` `aws configure`
```

Run the following commands to deploy the API:

```
`$` `REGION=`<region>``
`$` `API_STACK_NAME=`<stack-name>``  # This can be any name
`$` `VERSION=3.14.1`
`$` `aws cloudformation create-stack \
   --region ${REGION} \
   --stack-name ${API_STACK_NAME} \
   --template-url https://${REGION}-aws-parallelcluster.s3.${REGION}.amazonaws.com/parallelcluster/${VERSION}/api/parallelcluster-api.yaml \
   --capabilities CAPABILITY_NAMED_IAM CAPABILITY_AUTO_EXPAND`
`$` `aws cloudformation wait stack-create-complete --stack-name ${API_STACK_NAME} --region ${REGION}`
```

**Customize your deployment**

You can use the CloudFormation parameters exposed by the template to customize the API deployment.
To configure the value of a parameter when you deploy through the CLI, the following option
can be used: `--parameters ParameterKey=KeyName,ParameterValue=Value`.

The following parameters are optional:

- **Region** - Use the `Region` parameter to
  specify whether the API is able to control resources in all AWS Regions (default) or
  in a single AWS Region. Set this value to the AWS Region the API is being deployed
  to in order to restrict access.
- **ParallelClusterFunctionRole** - This overrides the
  IAM role that gets assigned to the AWS Lambda function that implements AWS ParallelCluster
  features. The parameter accepts the ARN of an IAM role. This role needs to be configured
  to have AWS Lambda as the IAM principal. Also, since this role will replace the default
  role of the API Lambda function, it must have at least the default permissions required by
  the API as listed in [AWS ParallelCluster example pcluster user policies](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-example-user-policies").
- **ParallelClusterFunctionAdditionalPolicies** - ARN of the
  additional IAM policy to be attached to the AWS ParallelCluster API function role. Only one
  policy can be specified.
- **CustomDomainName, CustomDomainCertificate, CustomDomainHostedZoneId** -
  Use these parameters to set a custom domain for the Amazon API Gateway endpoint. `CustomDomainName` 
  is the name of the domain to use, `CustomDomainCertificate` is the ARN of an AWS
  managed certificate for this domain name and `CustomDomainHostedZoneId` is the
  ID of the [Amazon Route 53](../../../Route53/latest/DeveloperGuide/Welcome.md "../../../Route53/latest/DeveloperGuide/Welcome.md")
  hosted zone that you want to create records in.

###### Warning

You can configure custom domain settings to enforce a minimum version of Transport
Layer Security (TLS) for the API. For more information, see [Choosing
a minimum TLS version for a custom domain in API Gateway](../../../apigateway/latest/developerguide/apigateway-custom-domain-tls-version.md "../../../apigateway/latest/developerguide/apigateway-custom-domain-tls-version.md").

- **EnableIamAdminAccess** - By default the AWS Lambda
  function that processes AWS ParallelCluster API operations is configured with an IAM role
  that prevents any privileged IAM access (`EnableIamAdminAccess=false`).
  This makes the API unable to process operations that require the creation of IAM roles
  or policies. Because of this, the creation of clusters or custom images is successful
  only when IAM roles are provided as input as part of the resource configuration.

When `EnableIamAdminAccess` is set to `true` the AWS ParallelCluster
API is granted permissions to manage the creation of IAM roles required to deploy clusters
or generate custom AMIs.

###### Warning

When this is set to true it grants IAM admin privileges to the AWS Lambda function
that processes AWS ParallelCluster operations.

Refer to [AWS ParallelCluster user example policies for managing IAM
resources](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-user-policy-manage-iam "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-user-policy-manage-iam") for additional details
on the features that can be unlocked when you enable this mode.

- **PermissionsBoundaryPolicy** - This optional parameter
  accepts an existing IAM policy ARN that will be set as permissions boundary for all the
  IAM roles created by the PC API infrastructure and as a condition on the administrative
  IAM permissions so that only roles with this policy can be created by the PC API.

Refer to [PermissionsBoundary
mode](iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-permissionsboundary-mode "iam-roles-in-parallelcluster-v3.md#iam-roles-in-parallelcluster-v3-permissionsboundary-mode") for additional details
on the restrictions imposed by this mode.

- **CreateApiUserRole** - By default, the deployment of
  the AWS ParallelCluster API includes the creation of an IAM role which is set as the
  only role authorized to invoke the API. The Amazon API Gateway endpoint is configured with a
  resource based policy to grant invoke permission to the created user only. To change
  this, set `CreateApiUserRole=false` and then grant API access to selected
  IAM users. For more information, see [Control access for invoking an API](../../../apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.md "../../../apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.md") in the _Amazon API Gateway Developer
  Guide_.

###### Warning

When `CreateApiUserRole=true` access to the API endpoint is not restricted by
Amazon API Gateway resource policies, all IAM roles that have unconstrained `execute-api:Invoke` 
permission can access AWS ParallelCluster features. For more information, see [Controlling access to an API with API Gateway resource policies](../../../apigateway/latest/developerguide/apigateway-resource-policies.md "../../../apigateway/latest/developerguide/apigateway-resource-policies.md") in the
_API Gateway Developer Guide_.

###### Warning

The `ParallelClusterApiUserRole` has permission to invoke all AWS ParallelCluster
API operations. To restrict access to a subset of API resources, see the [Control who can call an API Gateway API method with IAM policies](../../../apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.md#api-gateway-who-can-invoke-an-api-method-using-iam-policies "../../../apigateway/latest/developerguide/api-gateway-control-access-using-iam-policies-to-invoke-api.md#api-gateway-who-can-invoke-an-api-method-using-iam-policies") in the
_API Gateway Developer Guide_.

- **IAMRoleAndPolicyPrefix** - This optional parameter accepts
  a string containing a maximum of 10 characters that will be used as the prefix for both IAM
  roles and policies created as part of the PC API infrastructure.
