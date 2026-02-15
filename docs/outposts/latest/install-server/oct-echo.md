# echo

The **echo** command displays the value that you set for a variable using
the [export](oct-export.md "oct-export.md") command.

**Syntax**

```
`Outpost>`echo $`variable-name`
```

**Parameters**

This command takes a variable name. The valid values are:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `AWS_SESSION_TOKEN`
- `AWS_DEFAULT_REGION`

###### Example: Success

```
`Outpost>`echo $AWS_DEFAULT_REGION

`variable name: AWS_DEFAULT_REGION
variable value: `us-west-2`
checksum: `checksum``

```

###### Example: Failure because the variable value was not set using export

```
`Outpost>`echo $AWS_ACCESS_KEY_ID

`error_type: execution_error
error_attributes:
 AWS_ACCESS_KEY_ID: no value set
error_message: No value set for AWS_ACCESS_KEY_ID using export.
checksum: `checksum``

```

###### Example: Failure because the variable name is not valid

```
`Oupost>`echo $`bad_example`

`error_type: invalid_argument
error_attributes:
 `bad_example`: invalid variable name
error_message: Variables can only be AWS credentials.
checksum: `checksum``

```

###### Example: Failure because of a syntax issue

```
`Outpost>`echo AWS_SECRET_ACCESS_KEY

`error_type: invalid_argument
error_attributes:
 AWS_SECRET_ACCESS_KEY: not a variable
error_message: Expecting $ before variable name.
checksum: `checksum``

```
