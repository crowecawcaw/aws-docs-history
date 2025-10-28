# Use `GetRolePolicy` with a CLI

The following code examples show how to use `GetRolePolicy`.

CLI

**AWS CLI**

**To get information about a policy attached to an IAM role**

The following `get-role-policy` command gets information about the specified policy attached to the role named `Test-Role`.

```
`aws iam get-role-policy \
 --role-name `Test-Role` \
 --policy-name `ExamplePolicy``

```

Output:

```
{
  "RoleName": "Test-Role",
  "PolicyDocument": {
      "Statement": [
          {
              "Action": [
                  "s3:ListBucket",
                  "s3:Put*",
                  "s3:Get*",
                  "s3:*MultipartUpload*"
              ],
              "Resource": "*",
              "Effect": "Allow",
              "Sid": "1"
          }
      ]
  }
  "PolicyName": "ExamplePolicy"
}
```

For more information, see [Creating IAM roles](id_roles_create.md "id_roles_create.md") in the _AWS IAM User Guide_.

- For API details, see
  [GetRolePolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-role-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example returns the permissions policy document for the policy named `oneClick_lambda_exec_role_policy` that is embedded in the IAM role `lamda_exec_role`. The resulting policy document is URL encoded. It is decoded in this example with the `UrlDecode` .NET method.**

```
$results = Get-IAMRolePolicy -RoleName lambda_exec_role -PolicyName oneClick_lambda_exec_role_policy
$results

```

**Output:**

```
PolicyDocument                                            PolicyName                           UserName
--------------                                            ----------                           --------
%7B%0A%20%20%22Version%22%3A%20%222012-10-17%22%2C%...    oneClick_lambda_exec_role_policy     lambda_exec_role
```

```
[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
[System.Web.HttpUtility]::UrlDecode($results.PolicyDocument)

```

**Output:**

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:*"
      ],
      "Resource": "arn:aws:logs:us-east-1:555555555555:log-group:/aws/lambda/aws-example-function:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket/*"
      ]
    }
  ]
}
```

- For API details, see
  [GetRolePolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example returns the permissions policy document for the policy named `oneClick_lambda_exec_role_policy` that is embedded in the IAM role `lamda_exec_role`. The resulting policy document is URL encoded. It is decoded in this example with the `UrlDecode` .NET method.**

```
$results = Get-IAMRolePolicy -RoleName lambda_exec_role -PolicyName oneClick_lambda_exec_role_policy
$results

```

**Output:**

```
PolicyDocument                                            PolicyName                           UserName
--------------                                            ----------                           --------
%7B%0A%20%20%22Version%22%3A%20%222012-10-17%22%2C%...    oneClick_lambda_exec_role_policy     lambda_exec_role
```

```
[System.Reflection.Assembly]::LoadWithPartialName("System.Web.HttpUtility")
[System.Web.HttpUtility]::UrlDecode($results.PolicyDocument)

```

**Output:**

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "logs:*"
      ],
      "Resource": "arn:aws:logs:us-east-1:555555555555:log-group:/aws/lambda/aws-example-function:*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::amzn-s3-demo-bucket/*"
      ]
    }
  ]
}
```

- For API details, see
  [GetRolePolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
