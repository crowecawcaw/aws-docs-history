AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

# Working with parameter hierarchies

in Parameter Store

Managing dozens or hundreds of parameters as a flat list is time consuming and
prone to errors. It can also be difficult to identify the correct parameter for a
task. This means you might accidentally use the wrong parameter, or you might create
multiple parameters that use the same configuration data.

You can use parameter hierarchies to help you organize and manage parameters. A
hierarchy is a parameter name that includes a path that you define by using forward
slashes (/).

###### Topics

- [Understanding parameter hierarchy
  through examples](#ps-hierarchy-examples "#ps-hierarchy-examples")
- [Querying parameters in a
  hierarchy](#ps-hierarchy-queries "#ps-hierarchy-queries")
- [Managing parameters using
  hierarchies using the AWS CLI](#sysman-paramstore-walk-hierarchy "#sysman-paramstore-walk-hierarchy")

## Understanding parameter hierarchy

through examples

The following example uses three hierarchy levels in the name to identify the
following:

`/Environment/Type of computer/Application/Data`

`/Dev/DBServer/MySQL/db-string13`

You can create a hierarchy with a maximum of 15 levels. We suggest that you
create hierarchies that reflect an existing hierarchical structure in your
environment, as shown in the following examples:

- Your [Continuous integration](https://aws.amazon.com/devops/continuous-integration/ "https://aws.amazon.com/devops/continuous-integration/") and [Continuous
  delivery](https://aws.amazon.com/devops/continuous-delivery/ "https://aws.amazon.com/devops/continuous-delivery/") environment (CI/CD workflows)

`/Dev/DBServer/MySQL/db-string`

`/Staging/DBServer/MySQL/db-string`

`/Prod/DBServer/MySQL/db-string`

- Your applications that use containers

```
/MyApp/.NET/Libraries/`my-password`
```

- Your business organization

`/Finance/Accountants/UserList`

`/Finance/Analysts/UserList`

`/HR/Employees/EU/UserList`

Parameter hierarchies standardize the way you create parameters and make it
easier to manage parameters over time. A parameter hierarchy can also help you
identify the correct parameter for a configuration task. This helps you to avoid
creating multiple parameters with the same configuration data.

You can create a hierarchy that allows you to share parameters across
different environments, as shown in the following examples that use passwords in
development and staging environment.

`/DevTest/MyApp/database/`my-password``

You could then create a unique password for your production environment, as
shown in the following example:

`/prod/MyApp/database/`my-password``

You aren't required to specify a parameter hierarchy. You can create
parameters at level one. These are called _root_ parameters.
For backward compatibility, all parameters created in Parameter Store before
hierarchies were released are root parameters. The systems treats both of the
following parameters as root parameters.

`/parameter-name`

`parameter-name`

## Querying parameters in a

hierarchy

Another benefit of using hierarchies is the ability to query for all
parameters _under_ a certain level in a
hierarchy by using the [GetParametersByPath](../APIReference/API_GetParametersByPath.md "../APIReference/API_GetParametersByPath.md") API operation. For example, if you run the
following command from the AWS Command Line Interface (AWS CLI), the system returns all parameters
under the `Oncall` level:

```
aws ssm get-parameters-by-path --path /Dev/Web/Oncall
```

Sample output:

```
{
    "Parameters": [
        {
            "Name": "/Dev/Web/Oncall/Week1",
            "Type": "String",
            "Value": "John Doe",
            "Version": 1,
            "LastModifiedDate": "2024-11-22T07:18:53.510000-08:00",
            "ARN": "arn:aws:ssm:us-east-2:123456789012:parameter/Dev/Web/Oncall/Week1",
            "DataType": "text"
        },
        {
            "Name": "/Dev/Web/Oncall/Week2",
            "Type": "String",
            "Value": "Mary Major",
            "Version": 1,
            "LastModifiedDate": "2024-11-22T07:21:25.325000-08:00",
            "ARN": "arn:aws:ssm:us-east-2:123456789012:parameter/Dev/Web/Oncall/Week2",
            "DataType": "text"
        }
    ]
}
```

To view decrypted `SecureString` parameters in a hierarchy, you
specify the path and the `--with-decryption` parameter, as shown in
the following example.

```
aws ssm get-parameters-by-path --path /Prod/ERP/SAP --with-decryption
```

## Managing parameters using

hierarchies using the AWS CLI

This procedure shows how to work with parameters and parameter hierarchies by
using the AWS CLI.

###### To manage parameters using hierarchies

1. Install and configure the AWS Command Line Interface (AWS CLI), if you haven't already.

For information, see [Installing or updating the
latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md"). 2. Run the following command to create a parameter that uses the
`allowedPattern` parameter and the `String`
parameter type. The allowed pattern in this example means the value for
the parameter must be between 1 and 4 digits long.

Linux & macOS

```
aws ssm put-parameter \
    --name "/MyService/Test/MaxConnections" \
    --value 100 --allowed-pattern "\d{1,4}" \
    --type String
```

Windows

```
aws ssm put-parameter ^
    --name "/MyService/Test/MaxConnections" ^
    --value 100 --allowed-pattern "\d{1,4}" ^
    --type String
```

The command returns the version number of the parameter. 3. Run the following command to _attempt_ to overwrite
the parameter you just created with a new value.

Linux & macOS

```
aws ssm put-parameter \
    --name "/MyService/Test/MaxConnections" \
    --value 10,000 \
    --type String \
    --overwrite
```

Windows

```
aws ssm put-parameter ^
    --name "/MyService/Test/MaxConnections" ^
    --value 10,000 ^
    --type String ^
    --overwrite
```

The system returns the following error because the new value doesn't
meet the requirements of the allowed pattern you specified in the
previous step.

```
An error occurred (ParameterPatternMismatchException) when calling the PutParameter operation: Parameter value, cannot be validated against allowedPattern: \d{1,4}
```

4. Run the following command to create a `SecureString`
   parameter that uses an AWS managed key. The allowed pattern in this
   example means the user can specify any character, and the value must be
   between 8 and 20 characters.

Linux & macOS

```
aws ssm put-parameter \
    --name "/MyService/Test/`my-password`" \
    --value "p#sW*rd33" \
    --allowed-pattern ".{8,20}" \
    --type SecureString
```

Windows

```
aws ssm put-parameter ^
    --name "/MyService/Test/`my-password`" ^
    --value "p#sW*rd33" ^
    --allowed-pattern ".{8,20}" ^
    --type SecureString
```

5. Run the following commands to create more parameters that use the
   hierarchy structure from the previous step.

Linux & macOS

```
aws ssm put-parameter \
    --name "/MyService/Test/DBname" \
    --value "SQLDevDb" \
    --type String
```

```
aws ssm put-parameter \
    --name "/MyService/Test/user" \
    --value "SA" \
    --type String
```

```
aws ssm put-parameter \
    --name "/MyService/Test/userType" \
    --value "SQLuser" \
    --type String
```

Windows

```
aws ssm put-parameter ^
    --name "/MyService/Test/DBname" ^
    --value "SQLDevDb" ^
    --type String
```

```
aws ssm put-parameter ^
    --name "/MyService/Test/user" ^
    --value "SA" ^
    --type String
```

```
aws ssm put-parameter ^
    --name "/MyService/Test/userType" ^
    --value "SQLuser" ^
    --type String
```

6. Run the following command to get the value of two parameters.

Linux & macOS

```
aws ssm get-parameters \
    --names "/MyService/Test/user" "/MyService/Test/userType"
```

Windows

```
aws ssm get-parameters ^
    --names "/MyService/Test/user" "/MyService/Test/userType"
```

7. Run the following command to query for all parameters under a single
   level.

Linux & macOS

```
aws ssm get-parameters-by-path \
    --path "/MyService/Test"
```

Windows

```
aws ssm get-parameters-by-path ^
    --path "/MyService/Test"
```

8. Run the following command to delete two parameters.

Linux & macOS

```
aws ssm delete-parameters \
    --names "/IADRegion/Dev/user" "/IADRegion/Dev/userType"
```

Windows

```
aws ssm delete-parameters ^
    --names "/IADRegion/Dev/user" "/IADRegion/Dev/userType"
```
