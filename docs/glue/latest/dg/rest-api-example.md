# Tutorial: Creating a REST API ConnectionType and Connection

**Connecting to the Foo REST API**

We will create an AWS Glue REST API ConnectionType and a corresponding AWS Glue connection for the Foo REST API.
This API has the following properties (which can be retrieved from REST API documentation).

- **Instance URL**: https://foo.cloud.com/rest/v1.
- **Authentication type**: OAuth2 (Client Credentials).
- **REST method**: GET.
- **Pagination type**: Offset with properties “limit” and “offset”
  placed in query parameter of request.
- **Supported entities**:
  - **Bar**: relative path [/bar.json].
  - **Baz**: relative path [/baz.json].

Once all the details are obtained, we can begin creating the AWS Glue connection to the Foo REST API.

**To create a REST API connection**:

1. Create the REST API connection type in AWS Glue by calling the RegisterConnectionType API using
   AWS API, CLI, or SDK. This will create a new ConnectionType resource in AWS Glue.

```
{
    "ConnectionType": "REST-FOO-CONNECTOR",
    "IntegrationType": "REST",
    "Description": "AWS Glue Connection Type for the FOO REST API",
    "ConnectionProperties": {
        "Url": {
            "Name": "Url",
            "Required": true,
            "DefaultValue": "https://foo.cloud.com/rest/v1",
            "PropertyType": "USER_INPUT"
        }
    },
    "ConnectorAuthenticationConfiguration": {
        "AuthenticationTypes": ["OAUTH2"],
        "OAuth2Properties": {
            "OAuth2GrantType": "CLIENT_CREDENTIALS"
        }
    },
    "RestConfiguration": {
        "GlobalSourceConfiguration": {
        "RequestMethod": "GET",
        "ResponseConfiguration": {
            "ResultPath": "$.result",
            "ErrorPath": "$.error.message"
        },
        "PaginationConfiguration": {
            "OffsetConfiguration": {
                "OffsetParameter": {
                    "Key": "offset",
                    "PropertyLocation": "QUERY_PARAM"
                },
                "LimitParameter": {
                    "Key": "limit",
                    "PropertyLocation": "QUERY_PARAM",
                    "DefaultValue": "50"
                }
            }
        }
    },
    "ValidationEndpointConfiguration": {
        "RequestMethod": "GET",
        "RequestPath": "/bar.json?offset=1&limit=10"
    },
    "EntityConfigurations": {
        "bar": {
            "SourceConfiguration": {
                "RequestMethod": "GET",
                "RequestPath": "/bar.json",
                "ResponseConfiguration": {
                    "ResultPath": "$.result",
                    "ErrorPath": "$.error.message"
                }
            },
            "Schema": {
                "name": {
                    "Name": "name",
                    "FieldDataType": "STRING"
                },
                "description": {
                    "Name": "description",
                    "FieldDataType": "STRING"
                },
                "id": {
                    "Name": "id",
                    "FieldDataType": "STRING"
                },
                "status": {
                    "Name": "status",
                    "FieldDataType": "STRING"
                }
            }
        }
    }
}
}
```

2. In AWS Secrets Manager, create a secret. The Secret should contain the connected app Consumer Secret with
   `USER_MANAGED_CLIENT_APPLICATION_CLIENT_SECRET` as key.

###### Note

You must create a secret per connection in AWS Glue 3. Create the AWS Glue connection by calling the CreateConnection API using the AWS API, CLI, or SDK.

    1. Reference the REST connection type name from Step 1 as the “ConnectionType”.
    2. Provide the InstanceUrl and any other ConnectionProperties that were defined during the
     AWS Glue ConnectionType registration process.
    3. Choose from the configured Authentication Types. The REST API Foo uses OAuth2 with the
     ClientCredentials grant type.
    4. Provide the **SecretArn** and other
     **AuthenticationProperties** that are configured. For example,
     we have configured `OAUTH2` as the AuthenticationType so we will set the
     “OAuth2Properties” in the CreateConnectionInput. This will require properties like
     “OAuth2GrantType”, “TokenUrl”, and “OAuth2ClientApplication”.

4. Make the CreateConnection request which will create the AWS Glue connection.

```
{
    "ConnectionInput": {
        "Name": "ConnectionFooREST",
        "ConnectionType": "REST-FOO-CONNECTOR",
        "ConnectionProperties": {},
        "ValidateCredentials": true,
        "AuthenticationConfiguration": {
            "AuthenticationType": "OAUTH2",
            "SecretArn": "arn:aws:secretsmanager:<region>:<accountId>:secret:<secretId>",
            "OAuth2Properties": {
                "OAuth2GrantType": "CLIENT_CREDENTIALS",
                "TokenUrl": "https://foo.cloud.com/oauth/token",
                "OAuth2ClientApplication": {
                    "UserManagedClientApplicationClientId": "your-managed-client-id"
                }
            }
        }
    }
}
```
