• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Use `GetParameter` with an AWS SDK or CLI

The following code examples show how to use `GetParameter`.

CLI

**AWS CLI**

**Example 1: To display the value of a parameter**

The following `get-parameter` example lists the value for the specified single parameter.

```
`aws ssm get-parameter \
 --name `"MyStringParameter"``

```

Output:

```
{
    "Parameter": {
        "Name": "MyStringParameter",
        "Type": "String",
        "Value": "Veni",
        "Version": 1,
        "LastModifiedDate": 1530018761.888,
        "ARN": "arn:aws:ssm:us-east-2:111222333444:parameter/MyStringParameter"
        "DataType": "text"
    }
}
```

For more information, see [Working with Parameter Store](parameter-store-working-with.md "parameter-store-working-with.md") in the _AWS Systems Manager User Guide_.

**Example 2: To decrypt the value of a SecureString parameter**

The following `get-parameter` example decrypts the value of the specified `SecureString` parameter.

```
`aws ssm get-parameter \
 --name `"MySecureStringParameter"` \
 --with-decryption`

```

Output:

```
{
    "Parameter": {
        "Name": "MySecureStringParameter",
        "Type": "SecureString",
        "Value": "16679b88-310b-4895-a943-e0764EXAMPLE",
        "Version": 2,
        "LastModifiedDate": 1582155479.205,
        "ARN": "arn:aws:ssm:us-east-2:111222333444:parameter/MySecureStringParameter"
        "DataType": "text"
    }
}
```

For more information, see [Working with Parameter Store](parameter-store-working-with.md "parameter-store-working-with.md") in the _AWS Systems Manager User Guide_.

**Example 3: To display the value of a parameter using labels**

The following `get-parameter` example lists the value for the specified single parameter with a specified label.

```
`aws ssm get-parameter \
 --name `"MyParameter:label"``

```

Output:

```
{
    "Parameter": {
        "Name": "MyParameter",
        "Type": "String",
        "Value": "parameter version 2",
        "Version": 2,
        "Selector": ":label",
        "LastModifiedDate": "2021-07-12T09:49:15.865000-07:00",
        "ARN": "arn:aws:ssm:us-west-2:786973925828:parameter/MyParameter",
        "DataType": "text"
    }
}
```

For more information, see [Working with parameter labels](sysman-paramstore-labels.md "sysman-paramstore-labels.md") in the _AWS Systems Manager User Guide_.

**Example 4: To display the value of a parameter using versions**

The following `get-parameter` example lists the value for the specified single parameter version.

```
`aws ssm get-parameter \
 --name `"MyParameter:2"``

```

Output:

```
{
    "Parameter": {
        "Name": "MyParameter",
        "Type": "String",
        "Value": "parameter version 2",
        "Version": 2,
        "Selector": ":2",
        "LastModifiedDate": "2021-07-12T09:49:15.865000-07:00",
        "ARN": "arn:aws:ssm:us-west-2:786973925828:parameter/MyParameter",
        "DataType": "text"
    }
}
```

For more information, see [Working with parameter labels](sysman-paramstore-labels.md "sysman-paramstore-labels.md") in the _AWS Systems Manager User Guide_.

- For API details, see
  [GetParameter](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-parameter.html")
  in _AWS CLI Command Reference_.

Rust

**SDK for Rust**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ssm#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/ssm#code-examples").

```
    pub async fn list_path(&self, path: &str) -> Result<Vec<Parameter>, EC2Error> {
        let maybe_params: Vec<Result<Parameter, _>> = TryFlatMap::new(
            self.inner
                .get_parameters_by_path()
                .path(path)
                .into_paginator()
                .send(),
        )
        .flat_map(|item| item.parameters.unwrap_or_default())
        .collect()
        .await;
        // Fail on the first error
        let params = maybe_params
            .into_iter()
            .collect::<Result<Vec<Parameter>, _>>()?;
        Ok(params)
    }


```

- For API details, see
  [GetParameter](https://docs.rs/aws-sdk-ssm/latest/aws_sdk_ssm/client/struct.Client.html#method.get_parameter "https://docs.rs/aws-sdk-ssm/latest/aws_sdk_ssm/client/struct.Client.html#method.get_parameter")
  in _AWS SDK for Rust API reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using this service with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
