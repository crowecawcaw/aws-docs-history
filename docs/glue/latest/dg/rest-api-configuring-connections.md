# Configuring a REST API connection

In order to configure an AWS Glue REST API connector, you need to configure an AWS Glue connection type. This
connection type contains details about the properties of how the REST data source operates and interprets
things like authentication, requests, responses, pagination, validations, and entities/ metadata.

For a comprehensive list of the required properties for an AWS Glue REST connection type, see the
[RegisterConnectionType](../webapi/API_DescribeConnectionType.md "../webapi/API_DescribeConnectionType.md") API and the steps for
[Connecting to REST APIs](rest-api-connections.md "rest-api-connections.md").

When creating the REST API connector, the following policy is needed to allow relevant actions:

```
{
    "Version":"2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "glue:RegisterConnectionType",
                "glue:ListConnectionTypes",
                "glue:DescribeConnectionType",
                "glue:CreateConnection",
                "secretsmanager:DescribeSecret",
                "secretsmanager:GetSecretValue",
                "secretsmanager:PutSecretValue",
                "ec2:CreateNetworkInterface",
                "ec2:DescribeNetworkInterfaces",
                "ec2:DeleteNetworkInterface"
            ],
            "Resource": "*"
        }
    ]
}
```
