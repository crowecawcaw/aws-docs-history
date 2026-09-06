

# Create an IAM Role for AWS Security Agent
<a name="create-iam-role"></a>

AWS Security Agent uses IAM Roles in three ways:

1.  **Application Role:** Used when creating the AWS Security Agent application. For IAM Identity Center and admin access link use cases, the service assumes this role to grant WebApp users permissions to interact with AWS Security Agent APIs.

1.  **Penetration Test Service Role:** Specified when creating Agent Spaces as a list of available roles. Later, WebApp users select one of these roles when creating a penetration test. AWS Security Agent service assumes this role to access your AWS resources during testing.

1.  **Actor Role:** Used to authenticate and authorize requests to your target web application (for example, AWS API Gateway APIs). These roles are provided during Agent Space creation. The AWS Security Agent agent assumes actor roles to interact with your target application.

## Application Role
<a name="_application_role"></a>

The Application Role is used when creating your AWS Security Agent application in the service. For IAM Identity Center and admin access link authentication scenarios, the AWS Security Agent service assumes this role to grant WebApp users the necessary permissions to interact with AWS Security Agent APIs.

### Required Permissions
<a name="_required_permissions"></a>

This role needs permissions to:
+ Invoke AWS Security Agent API operations
+ Read and write application configuration data
+ Access user session information
+ Manage authentication tokens for WebApp users

### Trust Policy
<a name="_trust_policy"></a>

The trust policy must allow the AWS Security Agent service to assume this role:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

### Permissions Policy
<a name="_permissions_policy"></a>

The role should include permissions for:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "securityagent:GetApplication",
        "securityagent:UpdateApplication",
        "securityagent:ListAgentInstances",
        "securityagent:CreatePentestSession"
      ],
      "Resource": "arn:aws:securityagent:*:*:application/*"
    }
  ]
}
```

**Note**  
Customize the permissions based on your specific application requirements and principle of least privilege.

## Penetration Test Service Role
<a name="_penetration_test_service_role"></a>

The Penetration Test Service Role is specified when creating Agent Spaces as a list of available roles. When WebApp users create a penetration test, they select one of these roles. The AWS Security Agent service then assumes this role to access and test your AWS resources.

### Required Permissions
<a name="_required_permissions_2"></a>

This role needs permissions to access and analyze your AWS resources during penetration testing:
+ Read and describe VPC configurations and network topology
+ Inspect EC2 instances, security groups, and network ACLs
+ Analyze IAM policies and resource permissions
+ Read CloudWatch logs and metrics
+ Access AWS service configurations relevant to security testing

### Trust Policy
<a name="_trust_policy_2"></a>

The trust policy must allow the AWS Security Agent service to assume this role for penetration testing operations:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "your-external-id"
        }
      }
    }
  ]
}
```

**Note**  
Use an External ID for additional security when allowing cross-account or service access.

### Permissions Policy
<a name="_permissions_policy_2"></a>

The role should include read-only access to your AWS resources. Consider using these managed policies:
+  `SecurityAudit` - AWS managed policy for security auditing
+  `ViewOnlyAccess` - Read-only access to most AWS services

Or create a custom policy with specific permissions:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:Describe*",
        "vpc:Describe*",
        "iam:Get*",
        "iam:List*",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams",
        "cloudwatch:Describe*",
        "cloudwatch:Get*",
        "cloudwatch:List*",
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": "*"
    }
  ]
}
```

**Important**  
Grant only the minimum permissions required for your penetration testing scope. Review and adjust permissions based on which AWS services you want to include in security testing.

## Actor Role
<a name="_actor_role"></a>

The Actor Role is used to authenticate and authorize requests to your target web application during penetration testing. These roles are provided during Agent Space creation, and the AWS Security Agent agent assumes them to interact with your target application endpoints (such as AWS API Gateway APIs, Lambda function URLs, or other AWS-hosted applications).

### Required Permissions
<a name="_required_permissions_3"></a>

This role needs permissions to:
+ Invoke API Gateway endpoints
+ Execute Lambda functions
+ Access application-specific AWS resources
+ Authenticate with your target application’s authentication mechanisms
+ Perform HTTP operations against your application endpoints

### Trust Policy
<a name="_trust_policy_3"></a>

The trust policy must allow the AWS Security Agent agent service to assume this role:

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "your-external-id"
        }
      }
    }
  ]
}
```

### Permissions Policy
<a name="_permissions_policy_3"></a>

The permissions depend on your target application architecture. Here are examples for common scenarios:

#### For API Gateway Applications
<a name="_for_api_gateway_applications"></a>

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "execute-api:Invoke"
      ],
      "Resource": "arn:aws:execute-api:us-east-1:*:your-api-id/*"
    }
  ]
}
```

#### For Lambda Function URLs
<a name="_for_lambda_function_urls"></a>

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "lambda:InvokeFunctionUrl",
        "lambda:InvokeFunction"
      ],
      "Resource": "arn:aws:lambda:us-east-1:*:function:your-function-name"
    }
  ]
}
```

#### For Application Load Balancer with Cognito Authentication
<a name="_for_application_load_balancer_with_cognito_authentication"></a>

```
{
  "Version": "2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cognito-idp:InitiateAuth",
        "cognito-idp:RespondToAuthChallenge"
      ],
      "Resource": "arn:aws:cognito-idp:us-east-1:*:userpool/your-user-pool-id"
    }
  ]
}
```

**Important**  
Configure Actor Role permissions to match your target application’s authentication and authorization requirements. The role should have the same level of access as the users or services that the Security Agent will simulate during penetration testing.