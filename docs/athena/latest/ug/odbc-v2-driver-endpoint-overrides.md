# Endpoint overrides

## Athena endpoint override

The `endpointOverride ClientConfiguration` class uses this value override
the default HTTP endpoint for the Amazon Athena client. For more information, see [AWS
Client configuration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md") in the _AWS SDK for C++ Developer Guide_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                      |
| -------------------------- | ------------------ | ----------------- | -------------------------------------------------- |
| EndpointOverride           | Optional           | `none`            | `EndpointOverride=athena.us-west-2.amazonaws.com;` |

## Athena streaming endpoint override

The `ClientConfiguration.endpointOverride` method uses this value to
override the default HTTP endpoint for the Amazon Athena streaming client. For more
information, [AWS Client
configuration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md") in the _AWS SDK for C++ Developer Guide_. The
Athena Streaming service is available through port 444.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                                   |
| -------------------------- | ------------------ | ----------------- | --------------------------------------------------------------- |
| StreamingEndpointOverride  | Optional           | `none`            | `StreamingEndpointOverride=athena.us-west-1.amazonaws.com:444;` |

## AWS STS endpoint override

The `ClientConfiguration.endpointOverride` method uses this value to
override the default HTTP endpoint for the AWS STS client. For more information, see
[AWS Client configuration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md") in the _AWS SDK for C++ Developer Guide_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                      |
| -------------------------- | ------------------ | ----------------- | -------------------------------------------------- |
| StsEndpointOverride        | Optional           | `none`            | `StsEndpointOverride=sts.us-west-1.amazonaws.com;` |

## Lake Formation endpoint override

The `ClientConfiguration.endpointOverride` method uses this value to
override the default HTTP endpoint for the Lake Formation client. For more information, see [AWS
Client configuration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md") in the _AWS SDK for C++ Developer Guide_.

| **Connection string name**    | **Parameter type** | **Default value** | **Connection string example**                                          |
| ----------------------------- | ------------------ | ----------------- | ---------------------------------------------------------------------- |
| LakeFormationEndpointOverride | Optional           | `none`            | `LakeFormationEndpointOverride=lakeformation.us-west-1.amazonaws.com;` |

## SSO endpoint override

The `ClientConfiguration.endpointOverride` method uses this value to
override the default HTTP endpoint for the SSO client. For more information, see [AWS
Client configuration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md") in the _AWS SDK for C++ Developer Guide_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                             |
| -------------------------- | ------------------ | ----------------- | --------------------------------------------------------- |
| SSOEndpointOverride        | Optional           | `none`            | `SSOEndpointOverride=portal.sso.us-east-2.amazonaws.com;` |

## SSO OIDC endpoint override

The `ClientConfiguration.endpointOverride` method uses this value to
override the default HTTP endpoint for the SSO OIDC client. For more information, see
[AWS Client configuration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md") in the _AWS SDK for C++ Developer Guide_.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                          |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------------ |
| SSOOIDCEndpointOverride    | Optional           | `none`            | `SSOOIDCEndpointOverride=oidc.us-east-2.amazonaws.com` |

## SSO Admin endpoint override

The `ClientConfiguration.endpointOverride` method uses this value to
override the default HTTP endpoint for SSO Admin client. For more information, see
[ClientConfiguration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md").

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                          |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------------ |
| SSOAdminEndpointOverride   | Optional           | none              | `SSOAdminEndpointOverride=sso.us-east-2.amazonaws.com` |

## S3 endpoint override

The `ClientConfiguration.endpointOverride` method uses this value to
override the default HTTP endpoint for S3 client. The endpoint that the driver will use
to download query results when it uses the Amazon S3 fetcher. If this parameter is not
specified, the driver uses a default Amazon S3 endpoint. For more information, see [ClientConfiguration](../../../sdk-for-cpp/v1/developer-guide/client-config.md "../../../sdk-for-cpp/v1/developer-guide/client-config.md").

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                   |
| -------------------------- | ------------------ | ----------------- | ----------------------------------------------- |
| S3EndpointOverride         | Optional           | none              | `S3EndpointOverride=s3.us-east-2.amazonaws.com` |
