# Use `GetContextKeysForPrincipalPolicy` with a CLI

The following code examples show how to use `GetContextKeysForPrincipalPolicy`.

CLI

**AWS CLI**

**To list the context keys referenced by all policies associated with an IAM principal**

The following `get-context-keys-for-principal-policy` command retrieves all policies that are attached to the user `saanvi` and any groups she is a member of. It then parses each and lists the context keys used by those policies. Use this command to identify which context key values you must supply to successfully use the `simulate-custom-policy` and `simulate-principal-policy` commands. You can also retrieve the list of context keys used by an arbitrary JSON policy by using the `get-context-keys-for-custom-policy` command.

```
`aws iam get-context-keys-for-principal-policy \
 --policy-source-arn `arn:aws:iam::123456789012:user/saanvi``

```

Output:

```
{
    "ContextKeyNames": [
        "aws:username",
        "aws:CurrentTime"
    ]
}
```

For more information, see [Using the IAM Policy Simulator (AWS CLI and AWS API)](access_policies_testing-policies.md#policies-simulator-using-api "access_policies_testing-policies.md#policies-simulator-using-api") in the _AWS IAM User Guide_.

- For API details, see
  [GetContextKeysForPrincipalPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-context-keys-for-principal-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-context-keys-for-principal-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example fetches all the context keys present in the provided policy json and the policies attached to IAM entity(user/role etc.). For -PolicyInputList you can provide multiple values list as comma separated values.**

```
$policy1 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}'
$policy2 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/"}}'
Get-IAMContextKeysForPrincipalPolicy -PolicyInputList $policy1,$policy2 -PolicySourceArn arn:aws:iam::852640994763:user/TestUser

```

- For API details, see
  [GetContextKeysForPrincipalPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example fetches all the context keys present in the provided policy json and the policies attached to IAM entity(user/role etc.). For -PolicyInputList you can provide multiple values list as comma separated values.**

```
$policy1 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}'
$policy2 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/"}}'
Get-IAMContextKeysForPrincipalPolicy -PolicyInputList $policy1,$policy2 -PolicySourceArn arn:aws:iam::852640994763:user/TestUser

```

- For API details, see
  [GetContextKeysForPrincipalPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
