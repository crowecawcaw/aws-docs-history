# Use `GetContextKeysForCustomPolicy` with a CLI

The following code examples show how to use `GetContextKeysForCustomPolicy`.

CLI

**AWS CLI**

**Example 1: To list the context keys referenced by one or more custom JSON policies provided as a parameter on the command line**

The following `get-context-keys-for-custom-policy` command parses each supplied policy and lists the context keys used by those policies. Use this command to identify which context key values you must supply to successfully use the policy simulator commands `simulate-custom-policy` and `simulate-custom-policy`. You can also retrieve the list of context keys used by all policies associated by an IAM user or role by using the `get-context-keys-for-custom-policy` command. Parameter values that begin with `file://` instruct the command to read the file and use the contents as the value for the parameter instead of the file name itself.

```
`aws iam get-context-keys-for-custom-policy \
 --policy-input-list '`{"Version":"2012-10-17", "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/${aws:username}","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}`'`

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

**Example 2: To list the context keys referenced by one or more custom JSON policies provided as a file input**

The following `get-context-keys-for-custom-policy` command is the same as the previous example, except that the policies are provided in a file instead of as a parameter. Because the command expects a JSON list of strings, and not a list of JSON structures, the file must be structured as follows, although you can collapse it into one one.

```
[
    "Policy1",
    "Policy2"
]
```

So for example, a file that contains the policy from the previous example must look like the following. You must escape each embedded double-quote inside the policy string by preceding it with a backslash ''.

```
[ "{\"Version\": \"2012-10-17\", \"Statement\": {\"Effect\": \"Allow\", \"Action\": \"dynamodb:*\", \"Resource\": \"arn:aws:dynamodb:us-west-2:128716708097:table/${aws:username}\", \"Condition\": {\"DateGreaterThan\": {\"aws:CurrentTime\": \"2015-08-16T12:00:00Z\"}}}}" ]
```

This file can then be submitted to the following command.

```
`aws iam get-context-keys-for-custom-policy \
 --policy-input-list `file://policyfile.json``

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
  [GetContextKeysForCustomPolicy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-context-keys-for-custom-policy.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/get-context-keys-for-custom-policy.html")
  in _AWS CLI Command Reference_.

PowerShell

**Tools for PowerShell V4**

**Example 1: This example fetches all the context keys present in the provided policy json.In order to provide multiple policies you can provide as comma separated list of values.**

```
$policy1 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}'
$policy2 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/"}}'
Get-IAMContextKeysForCustomPolicy -PolicyInputList $policy1,$policy2

```

- For API details, see
  [GetContextKeysForCustomPolicy](../../../powershell/v4/reference.md "../../../powershell/v4/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V4)_.

**Tools for PowerShell V5**

**Example 1: This example fetches all the context keys present in the provided policy json.In order to provide multiple policies you can provide as comma separated list of values.**

```
$policy1 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/","Condition":{"DateGreaterThan":{"aws:CurrentTime":"2015-08-16T12:00:00Z"}}}}'
$policy2 = '{"Version":"2012-10-17",		 	 	 "Statement":{"Effect":"Allow","Action":"dynamodb:*","Resource":"arn:aws:dynamodb:us-west-2:123456789012:table/"}}'
Get-IAMContextKeysForCustomPolicy -PolicyInputList $policy1,$policy2

```

- For API details, see
  [GetContextKeysForCustomPolicy](../../../powershell/v5/reference.md "../../../powershell/v5/reference.md")
  in _AWS Tools for PowerShell Cmdlet Reference (V5)_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
