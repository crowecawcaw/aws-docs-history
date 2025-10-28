# Searching for Parameter Store parameters in

Systems Manager

When you have a lot of parameters in your account, it can be difficult to find
information about a single or several parameters at a time. In this case, you can
use filter tools to search for the ones you need information about, according to
search criteria you specify. You can use the AWS Systems Manager console, the AWS Command Line Interface
(AWS CLI), the AWS Tools for PowerShell, or the [DescribeParameters](../APIReference/API_DescribeParameters.md "../APIReference/API_DescribeParameters.md") API to
search for parameters.

###### Topics

- [Searching for a parameter using the
  console](#parameter-search-console "#parameter-search-console")
- [Searching for a parameter using the
  AWS CLI](#parameter-search-cli "#parameter-search-cli")

## Searching for a parameter using the

console

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").
2. In the navigation pane, choose **Parameter Store**.
3. Select in the search box and choose how you want to search. For
   example, `Type` or `Name`.
4. Provide information for the search type you selected. For
   example:
   - If you're searching by `Type`, choose from
     `String`, `StringList`, or
     `SecureString`.
   - If you're searching by `Name`, choose
     `contains`, `equals`, or
     `begins-with`, and then enter all or part of a
     parameter name.

   ###### Note

   In the console, the default search type for
   `Name` is `contains`.

5. Press **Enter**.

The list of parameters is updated with the results of your search.

###### Note

Your search might contain more results than are displayed on the first
page of results. Use the right arrow (**>**) at
the topic of the parameter list (if available) to view the next set of
results.

## Searching for a parameter using the

AWS CLI

Use the `describe-parameters` command to view information about one
or more parameters in the AWS CLI.

The following examples demonstrate various options you can use to view
information about the parameters in your AWS account. For more information
about these options, see [describe-parameters](../../../cli/latest/reference/ssm/describe-parameters.md "../../../cli/latest/reference/ssm/describe-parameters.md") in the
_AWS Command Line Interface User Guide_.

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Replace the sample values in the following commands with values
reflecting parameters that have been created in your account.

Linux & macOS

```
aws ssm describe-parameters \
    --parameter-filters "Key=Name,Values=`MyParameterName`"
```

Windows

```
aws ssm describe-parameters ^
    --parameter-filters "Key=Name,Values=`MyParameterName`"
```

###### Note

For `describe-parameters`, the default search type for
`Name` is `Equals`. In your parameter
filters, specifying
`"Key=Name,Values=`MyParameterName`"`
is the same as specifying
`"Key=Name,Option=Equals,Values=`MyParameterName`"`.

```
aws ssm describe-parameters \
    --parameter-filters "Key=Name,Option=Contains,Values=`Product`"
```

```
aws ssm describe-parameters \
    --parameter-filters "Key=Type,Values=String"
```

```
aws ssm describe-parameters \
    --parameter-filters "Key=Path,Values=`/Production/West`"
```

```
aws ssm describe-parameters \
    --parameter-filters "Key=Tier,Values=Standard"
```

```
aws ssm describe-parameters \
    --parameter-filters "Key=tag:`tag-key`,Values=`tag-value`"
```

```
aws ssm describe-parameters \
    --parameter-filters "Key=KeyId,Values=`key-id`"
```

###### Note

In the last example, `key-id` represents
the ID of an AWS Key Management Service (AWS KMS) key used to encrypt a
`SecureString` parameter created in your account.
Alternatively, you can enter `alias/aws/ssm` to
use the default AWS KMS key for your account. For more information,
see [Creating a SecureString
parameter using the AWS CLI](param-create-cli.md#param-create-cli-securestring "param-create-cli.md#param-create-cli-securestring").

If successful, the command returns output similar to the
following.

```
{
    "Parameters": [
        {
            "Name": "/Production/West/Manager",
            "Type": "String",
            "LastModifiedDate": 1573438580.703,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mateo.Jackson",
            "Version": 1,
            "Tier": "Standard",
            "Policies": []
        },
        {
            "Name": "/Production/West/TeamLead",
            "Type": "String",
            "LastModifiedDate": 1572363610.175,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mateo.Jackson",
            "Version": 1,
            "Tier": "Standard",
            "Policies": []
        },
        {
            "Name": "/Production/West/HR",
            "Type": "String",
            "LastModifiedDate": 1572363680.503,
            "LastModifiedUser": "arn:aws:iam::111122223333:user/Mateo.Jackson",
            "Version": 1,
            "Tier": "Standard",
            "Policies": []
        }
    ]
}
```
