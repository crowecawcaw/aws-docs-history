# Specifying blueprint

parameters

The configuration file contains blueprint parameter specifications in a
`parameterSpec` JSON object. `parameterSpec` contains one or more
parameter objects.

```
"parameterSpec": {
    "`<parameter_name>`": {
      "type": "`<parameter-type>`",
      "collection": true|false,
      "description": "`<parameter-description>`",
      "defaultValue": "`<default value for the parameter if value not specified>`"
      "allowedValues": "`<list of allowed values>`"
    },
    "`<parameter_name>`": {
       ...
    }
  }

```

The following are the rules for coding each parameter object:

- The parameter name and `type` are mandatory. All other properties are
  optional.
- If you specify the `defaultValue` property, the parameter is optional.
  Otherwise the parameter is mandatory and the data analyst who is creating a workflow
  from the blueprint must provide a value for it.
- If you set the `collection` property to `true`, the parameter
  can take a collection of values. Collections can be of any data type.
- If you specify `allowedValues`, the AWS Glue console displays a dropdown
  list of values for the data analyst to choose from when creating a workflow from the
  blueprint.
  The following are the permitted values for `type`:

| Parameter data type | Notes                                                                                                                                                             |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `String`            | -                                                                                                                                                                 |
| `Integer`           | -                                                                                                                                                                 |
| `Double`            | -                                                                                                                                                                 |
| `Boolean`           | Possible values are `true` and `false`. Generates a check<br>box on the \*_Create a workflow from <blueprint>_<br>• page on the<br>AWS Glue console.              |
| `S3Uri`             | Complete Amazon S3 path, beginning with `s3://`. Generates a text field<br>and **Browse\*<br>• button on the **Create a workflow from<br><blueprint>\*<br>• page. |
| `S3Bucket`          | Amazon S3 bucket name only. Generates a bucket picker on the \*_Create a<br>workflow from <blueprint>_<br>• page.                                                 |
| `IAMRoleArn`        | Amazon Resource Name (ARN) of an AWS Identity and Access Management (IAM) role. Generates a role<br>picker on the **Create a workflow from <blueprint>**<br>page. |
| `IAMRoleName`       | Name of an IAM role. Generates a role picker on the \*_Create a<br>workflow from <blueprint>_<br>• page.                                                          |
