

# Create the IAM roles for AWS Security Agent
<a name="create-iam-role"></a>

AWS Security Agent assumes IAM service roles in your account. It uses these roles to call its own APIs on behalf of web application users and to reach the AWS resources that you want it to assess. If you schedule penetration tests, Amazon EventBridge Scheduler also assumes a role in your account to start the scheduled runs. There are three roles:
+  **Application role** – One per application. AWS Security Agent assumes this role to give web application users permission to call AWS Security Agent APIs.
+  **Agent Space service role** – One per Agent Space. AWS Security Agent assumes this role to reach the AWS resources you attach to that Agent Space, such as VPCs, secrets, S3 buckets, Lambda functions, and CloudWatch log groups.
+  **Scheduler execution role** – One per Agent Space. EventBridge Scheduler assumes this role to start scheduled penetration test runs in that Agent Space. This role exists only if you enable penetration test scheduling for the Agent Space.

The console creates these roles for you, and generates their permissions from the resources you select. You do not need to write these policies by hand. This topic describes what the console creates, so that you can review and audit it. In the policies that follow, replace `111122223333` with your account ID, `us-east-1` with your Region, and the resource names with your own.

<a name="actor-role"></a>A penetration test can also assume a role in your account to authenticate to your target application. That role is separate from the application role and the Agent Space service role. You configure it per penetration test, as a credential, and you can use an IAM role, an AWS Secrets Manager secret, or a Lambda function. For more information, see [Provide authentication credentials for penetration testing](provide-testing-credentials.md).

## Application role
<a name="application-role"></a>

The application role is created once for your application, when you enable AWS Security Agent. AWS Security Agent assumes it to grant web application users the permissions they need to call AWS Security Agent APIs, including for IAM Identity Center and admin access link sign-in.

### Trust policy
<a name="application-role-trust-policy"></a>

The trust policy allows the AWS Security Agent service principal to assume the role. It also lets the service set the IAM Identity Center identity context on the resulting session. Both statements are required. Without `sts:SetContext`, IAM Identity Center sign-in to the web application fails. The `aws:SourceAccount` and `aws:SourceArn` conditions restrict the role to calls that AWS Security Agent makes on behalf of resources in your own account. For more information, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowServiceAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:securityagent:us-east-1:111122223333:application/*",
            "arn:aws:securityagent:us-east-1:111122223333:agent-space/*"
          ]
        }
      }
    },
    {
      "Sid": "AllowServiceSetContext",
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:SetContext",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ForAllValues:ArnEquals": {
          "sts:RequestContextProviders": "arn:aws:iam::aws:contextProvider/IdentityCenter"
        },
        "ArnLike": {
          "aws:SourceArn": [
            "arn:aws:securityagent:us-east-1:111122223333:application/*",
            "arn:aws:securityagent:us-east-1:111122223333:agent-space/*"
          ]
        }
      }
    }
  ]
}
```

### Permissions policy
<a name="application-role-permissions"></a>

The application role carries two sets of permissions, and it needs both. The first is the AWS managed policy `AWSSecurityAgentWebAppPolicy`, which grants the AWS Security Agent API permissions that web application users need. Use the managed policy rather than writing an equivalent policy yourself, so that your role picks up new permissions as AWS Security Agent adds capabilities. For its contents, see [AWS managed policies for AWS Security Agents](security-iam-awsmanpol.md). The second is a customer managed policy with the following permissions.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "CloudWatchLogsRead",
      "Effect": "Allow",
      "Action": "logs:GetLogEvents",
      "Resource": "arn:aws:logs:us-east-1:111122223333:log-group:*:log-stream:*"
    },
    {
      "Sid": "SecretsManagerCreate",
      "Effect": "Allow",
      "Action": "secretsmanager:CreateSecret",
      "Resource": "arn:aws:secretsmanager:us-east-1:111122223333:secret:*"
    }
  ]
}
```

If you encrypt your Agent Space with a customer managed key, the application role needs additional AWS KMS permissions. For those statements, see [Customer managed keys for AWS Security Agent](customer-managed-keys.md).

### Permissions for penetration test scheduling
<a name="application-role-scheduling-permissions"></a>

To schedule penetration tests in the web application, you need permissions in Amazon EventBridge Scheduler and IAM. `AWSSecurityAgentWebAppPolicy` grants these permissions, so a role that has the managed policy attached receives them automatically. To add these permissions to your own policy instead, see [AWS managed policy: AWSSecurityAgentWebAppPolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-AWSSecurityAgentWebAppPolicy).

## Agent Space service role
<a name="agent-space-service-role"></a>

<a name="penetration-test-service-role"></a>Each Agent Space has one service role. AWS Security Agent assumes it to reach the AWS resources you attached to that Agent Space while it runs an assessment. The role is shared by every capability in the Agent Space, including penetration testing, code review, and threat modeling, so changing its permissions affects all of them.

### Trust policy
<a name="agent-space-service-role-trust-policy"></a>

This role does not use an external ID. The `aws:SourceAccount` and `aws:SourceArn` conditions serve the same purpose for an AWS service principal. For more information, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowSecurityTestingAgentSpaceAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "securityagent.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:securityagent:us-east-1:111122223333:agent-space/*"
        }
      }
    }
  ]
}
```

### Permissions policies
<a name="agent-space-service-role-permissions"></a>

The console attaches a base policy to this role, plus one additional policy for each type of resource you attach to the Agent Space. If you don’t attach a resource type, the role receives no permissions for it. The following table lists the policies and when each one is created.


| Policy name | Created when | Grants | 
| --- | --- | --- | 
|  ` roleName-SecurityAgentBasePolicy`  | Always | Read its own role, read the secrets AWS Security Agent creates for the Agent Space, and write assessment logs | 
|  ` roleName-VpcPolicy`  | You attach a VPC with subnets or security groups | Create and manage elastic network interfaces, and describe VPC configuration | 
|  ` roleName-StaticCloudWatchPolicy`  | You attach CloudWatch log groups | Write to the log groups you selected | 
|  ` roleName-SecretsPolicy`  | You attach Secrets Manager secrets | Read the secrets you selected | 
|  ` roleName-LambdaPolicy`  | You attach Lambda functions | Invoke the functions you selected | 
|  ` roleName-S3Policy`  | You attach S3 buckets | Read the buckets you selected | 

If a resource you attach is encrypted with a customer managed key, the corresponding policy also grants AWS KMS permissions scoped to that key. For more information, see [Customer managed keys for AWS Security Agent](customer-managed-keys.md).

In the policies that follow, `my-agent-space` is the name of your Agent Space and `my-service-role` is the name of the role.

The base policy, which the console always creates:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:GetRole",
        "iam:SimulatePrincipalPolicy"
      ],
      "Resource": "arn:aws:iam::111122223333:role/service-role/my-service-role"
    },
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": [
        "arn:aws:secretsmanager:us-east-1:111122223333:secret:my-agent-space*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": "logs:CreateLogGroup",
      "Resource": "arn:aws:logs:us-east-1:111122223333:log-group:/aws/securityagent/my-agent-space*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": [
        "arn:aws:logs:us-east-1:111122223333:log-group:/aws/securityagent/my-agent-space*:log-stream:my-agent-space*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        }
      }
    }
  ]
}
```

The VPC policy, which lets AWS Security Agent attach an elastic network interface to your VPC so that it can reach targets inside it:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:CreateNetworkInterface",
        "ec2:DescribeDhcpOptions",
        "ec2:DescribeNetworkInterfaces",
        "ec2:DescribeNetworkInterfaceAttribute",
        "ec2:DescribeSubnets",
        "ec2:DescribeSecurityGroups",
        "ec2:DescribeVpcs",
        "ec2:ModifyNetworkInterfaceAttribute",
        "ec2:DeleteNetworkInterface"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "ec2:CreateNetworkInterfacePermission",
      "Resource": "arn:aws:ec2:us-east-1:111122223333:network-interface/*",
      "Condition": {
        "ArnEquals": {
          "ec2:Subnet": [
            "arn:aws:ec2:us-east-1:111122223333:subnet/subnet-1234567890abcdef0"
          ]
        }
      }
    }
  ]
}
```

The CloudWatch Logs policy, scoped to the log groups you selected, with the Agent Space name as the log stream prefix:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "logs:CreateLogGroup",
      "Resource": [
        "arn:aws:logs:us-east-1:111122223333:log-group:my-log-group:*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": [
        "arn:aws:logs:us-east-1:111122223333:log-group:my-log-group:log-stream:my-agent-space/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        }
      }
    }
  ]
}
```

The Secrets Manager policy, scoped to the secrets you selected:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "secretsmanager:GetSecretValue",
      "Resource": [
        "arn:aws:secretsmanager:us-east-1:111122223333:secret:my-secret-AbCdEf"
      ]
    }
  ]
}
```

The Lambda policy, scoped to the functions you selected, such as a function that resolves penetration test credentials:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "lambda:InvokeFunction",
      "Resource": [
        "arn:aws:lambda:us-east-1:111122223333:function:my-function"
      ]
    }
  ]
}
```

The Amazon S3 policy, scoped to the buckets you selected, such as a bucket that holds source code for a code review:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket",
        "arn:aws:s3:::amzn-s3-demo-bucket/*"
      ],
      "Condition": {
        "StringEquals": {
          "aws:ResourceAccount": "111122223333"
        }
      }
    }
  ]
}
```

## Scheduler execution role
<a name="scheduler-execution-role"></a>

Amazon EventBridge Scheduler assumes this role to start scheduled penetration test runs, so the runs start on time without anyone signing in. The console creates the role when you enable penetration test scheduling for an Agent Space. For information about how to enable it, see [(Optional) Enable penetration test scheduling](enable-penetration-test.md#enable-penetration-test-scheduling). Each Agent Space has its own role, named `continuum-schedule-agentSpaceId `, under the `/service-role/` path. The web application finds the role by this name, so don’t rename it.

In the policies that follow, `as-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` is the ID of your Agent Space.

### Trust policy
<a name="scheduler-execution-role-trust-policy"></a>

With the following JSON trust policy, EventBridge Scheduler can assume the role only for schedules in the schedule group for this Agent Space. The schedule group has the same name as the Agent Space ID. For more information, see [Cross-service confused deputy prevention](cross-service-confused-deputy-prevention.md).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowEventBridgeSchedulerAssumeRole",
      "Effect": "Allow",
      "Principal": {
        "Service": "scheduler.amazonaws.com"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "111122223333",
          "aws:SourceArn": "arn:aws:scheduler:us-east-1:111122223333:schedule-group/as-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
        }
      }
    }
  ]
}
```

### Permissions policy
<a name="scheduler-execution-role-permissions"></a>

The console attaches the following JSON customer managed policy, named `continuum-schedule-agentSpaceId-SchedulerPolicy-suffix `. With this policy, the role can start jobs only in this Agent Space. The policy also includes the actions to start code review and threat model jobs and to create design reviews, but scheduled penetration test runs use only `securityagent:StartPentestJob`. For more information about these actions, see the [AWS Security Agent API Reference](https://docs.aws.amazon.com/securityagent/latest/APIReference/Welcome.html).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "TriggerSecurityAgentJobsForAgentSpace",
      "Effect": "Allow",
      "Action": [
        "securityagent:StartPentestJob",
        "securityagent:StartCodeReviewJob",
        "securityagent:StartThreatModelJob",
        "securityagent:CreateDesignReview"
      ],
      "Resource": "arn:aws:securityagent:us-east-1:111122223333:agent-space/as-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  ]
}
```

If you encrypt the Agent Space with a customer managed key, the console adds the following JSON statement to the policy. With this statement, the role can use the key only through AWS Security Agent, and only for data in this Agent Space.

```
{
  "Sid": "AllowKmsKeyDecryptionForAgentSpaceData",
  "Effect": "Allow",
  "Action": [
    "kms:GenerateDataKey",
    "kms:Decrypt"
  ],
  "Resource": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-EXAMPLE11111",
  "Condition": {
    "StringEquals": {
      "aws:ResourceAccount": "111122223333"
    },
    "StringLike": {
      "kms:ViaService": "securityagent.us-east-1.amazonaws.com",
      "kms:EncryptionContext:aws:securityagent:agent-space": "arn:aws:securityagent:us-east-1:111122223333:agent-space/as-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
  }
}
```