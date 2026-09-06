

# Identity-based policies
<a name="auth-and-access_iam-policies"></a>

You can attach permissions policies to [IAM identities: users, user groups, and roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html). In an identity-based policy, you specify which secrets the identity can access and the actions the identity can perform on the secrets. For more information, see [Adding and removing IAM identity permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html).

You can grant permissions to a role that represents an application or user in another service. For example, an application running on an Amazon EC2 instance might need access to a database. You can create an IAM role attached to the EC2 instance profile and then use a permissions policy to grant the role access to the secret that contains credentials for the database. For more information, see [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html). Other services that you can attach roles to include [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/c-getting-started-using-spectrum.html), [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html), and [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html).

You can also grant permissions to users authenticated by an identity system other than IAM. For example, you can associate IAM roles to mobile app users who sign in with Amazon Cognito. The role grants the app temporary credentials with the permissions in the role permission policy. Then you can use a permissions policy to grant the role access to the secret. For more information, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html).

You can use identity-based policies to:
+ Grant an identity access to multiple secrets.
+ Control who can create new secrets, and who can access secrets that haven't been created yet.
+ Grant an IAM group access to secrets.

**Topics**
+ [Example: Permission to retrieve individual secret values](#auth-and-access_examples_identity_read)
+ [Example: Permission to read and describe individual secrets](#auth-and-access_examples-read-and-describe)
+ [Example: Permission to retrieve a group of secret values in a batch](#auth-and-access_examples_batch)
+ [Example: Wildcards](#auth-and-access_examples_wildcard)
+ [Example: Permission to create secrets](#auth-and-access_examples_create)
+ [Example: Deny a specific AWS KMS key to encrypt secrets](#auth-and-access_examples_kmskey)

## Example: Permission to retrieve individual secret values
<a name="auth-and-access_examples_identity_read"></a>

To grant permission to retrieve secret values, you can attach policies to secrets or identities. For help determining which type of policy to use, see [Identity-based policies and resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_identity-vs-resource.html). For information about how to attach a policy, see [Resource-based policies](auth-and-access_resource-policies.md) and [Identity-based policies](#auth-and-access_iam-policies).

This example is useful when you want to grant access to an IAM group. To grant permission to retrieve a group of secrets in a batch API call, see [Example: Permission to retrieve a group of secret values in a batch](#auth-and-access_examples_batch).

**Example Read a secret that is encrypted using a customer managed key**  
If a secret is encrypted using a customer managed key, you can grant access to read the secret by attaching the following policy to an identity. \\    
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement": [
{
  "Effect": "Allow",
  "Action": "secretsmanager:GetSecretValue",
  "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{secretName-AbCdEf}}"
},
{
  "Effect": "Allow",
  "Action": "kms:Decrypt",
  "Resource": "arn:aws:kms:{{us-east-1}}:{{123456789012}}:key/{{key-id}}"
}
]
}
```

## Example: Permission to read and describe individual secrets
<a name="auth-and-access_examples-read-and-describe"></a>

**Example Read and describe one secret**  
You can grant access to a secret by attaching the following policy to an identity.    
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement": [
  {
    "Effect": "Allow",
    "Action": [
      "secretsmanager:GetSecretValue",
      "secretsmanager:DescribeSecret"
      ],
      "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{secretName-AbCdEf}}"
    }
]
}
```

## Example: Permission to retrieve a group of secret values in a batch
<a name="auth-and-access_examples_batch"></a>

**Example Read a group of secrets in a batch**  
You can grant access to retrieve a group of secrets in a batch API call by attaching the following policy to an identity. The policy restricts the caller so that they can only retrieve the secrets specified by {{SecretARN1}}, {{SecretARN2}}, and {{SecretARN3}}, even if the batch call includes other secrets. If the caller also requests other secrets in the batch API call, Secrets Manager won't return them. For more information, see [`BatchGetSecretValue`.](https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_BatchGetSecretValue.html).     
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement": [
{
  "Effect": "Allow",
  "Action": [
    "secretsmanager:BatchGetSecretValue",
    "secretsmanager:ListSecrets"
  ],
  "Resource": "*"
},
{
  "Effect": "Allow",
  "Action": [
    "secretsmanager:GetSecretValue"
  ],
  "Resource": [
    "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{secretName1-AbCdEf}}",
    "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{secretName2-AbCdEf}}",
    "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{secretName3-AbCdEf}}"
    ]
}
]
}
```

## Example: Wildcards
<a name="auth-and-access_examples_wildcard"></a>

You can use wildcards to include a set of values in a policy element. 

**Example Access all secrets in a path**  
The following policy grants access to retrieve all secrets with a name beginning with "{{TestEnv/}}".    
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": {
        "Effect": "Allow",
        "Action": "secretsmanager:GetSecretValue",
        "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{TestEnv/}}*"
    }
}
```

**Example Access metadata on all secrets**  
The following policy grants `DescribeSecret` and permissions beginning with `List`: `ListSecrets` and `ListSecretVersionIds`.    
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement": {
"Effect": "Allow",
"Action": [
  "secretsmanager:DescribeSecret",
  "secretsmanager:List*"
],
"Resource": "*"
}
}
```

**Example Match secret name**  
The following policy grants all Secrets Manager permissions for a secret by name. To use this policy, see [Identity-based policies](#auth-and-access_iam-policies).  
To match a secret name, you create the ARN for the secret by putting together the Region, Account ID, secret name, and the wildcard (`?`) to match individual random characters. Secrets Manager appends six random characters to secret names as part of their ARN, so you can use this wildcard to match those characters. If you use the syntax `"another_secret_name-*"`, Secrets Manager matches not only the intended secret with the 6 random characters, but also matches `"another_secret_name-<anything-here>a1b2c3"`.   
Because you can predict all of the parts of the ARN of a secret except the 6 random characters, using the wildcard character `'??????'` syntax enables you to securely grant permissions to a secret that doesn't yet exist. Be aware, however, if you delete the secret and recreate it with the same name, the user automatically receives permission to the new secret, even though the 6 characters changed.     
****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "secretsmanager:*",
            "Resource": [
                "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{a_specific_secret_name-a1b2c3}}",
                "arn:aws:secretsmanager:{{us-east-1}}:{{123456789012}}:secret:{{another_secret_name-??????}}"
            ]
        }
    ]
}
```

## Example: Permission to create secrets
<a name="auth-and-access_examples_create"></a>

To grant a user permissions to create a secret, we recommend you attach a permissions policy to an IAM group the user belongs to. See [IAM user groups](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html).

**Example Create secrets**  
The following policy grants permission to create secrets and view a list of secrets. To use this policy, see [Identity-based policies](#auth-and-access_iam-policies).    
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement": [
{
  "Effect": "Allow",
  "Action": [
    "secretsmanager:CreateSecret",
    "secretsmanager:ListSecrets"
  ],
  "Resource": "*"
}
]
}
```

## Example: Deny a specific AWS KMS key to encrypt secrets
<a name="auth-and-access_examples_kmskey"></a>

**Important**  
To deny a customer managed key, we recommend you restrict access using a key policy or key grant. For more information, see [Authentication and access control for AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/control-access.html) in the *AWS Key Management Service Developer Guide*.

**Example Deny the AWS managed key `aws/secretsmanager`**  
The following policy denies the use of the AWS managed key `aws/secretsmanager` for creating or updating secrets. This policy requires secrets to be encrypted using a customer managed key. The policy includes two statements:  

1. The first statement, `Sid: "RequireCustomerManagedKeysOnSecrets"`, denies requests for creating or updating secrets using the AWS managed key `aws/secretsmanager`.

1. The second statement, `Sid: "RequireKmsKeyIdParameterOnCreate"`, denies requests for creating secrets that don't include a KMS key, because Secrets Manager would default to using the AWS managed key `aws/secretsmanager`.  
****  

```
{
"Version":"2012-10-17",		 	 	 
"Statement": [
  {
      "Sid": "RequireCustomerManagedKeysOnSecrets",
      "Effect": "Deny",
      "Action": [
          "secretsmanager:CreateSecret",
          "secretsmanager:UpdateSecret"
      ],
      "Resource": "*",
      "Condition": {
          "StringLikeIfExists": {
              "secretsmanager:KmsKeyArn": "<key_ARN_of_the_AWS_managed_key>"
          }
      }
  },
  {
      "Sid": "RequireKmsKeyIdParameterOnCreate",
      "Effect": "Deny",
      "Action": "secretsmanager:CreateSecret",
      "Resource": "*",
      "Condition": {
          "Null": {
              "secretsmanager:KmsKeyArn": "true"
          }
      }
  }
]
}
```