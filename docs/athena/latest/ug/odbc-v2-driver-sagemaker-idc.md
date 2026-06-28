# SageMaker Browser IDC

An authentication plugin that connects to Amazon Athena through SageMaker Unified Studio. It opens a
browser for AWS Identity and Access Management Identity Center sign-in using the OAuth 2.0 Authorization Code
flow with PKCE, then exchanges the resulting token for temporary credentials scoped to
your SageMaker Unified Studio domain and Athena project environment.

## Authentication Type

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**             |
| -------------------------- | ------------------ | ----------------- | ----------------------------------------- |
| AuthenticationType         | Required           | `none`            | `AuthenticationType=SageMakerBrowserIdc;` |

## SageMaker domain ID

The identifier of the SageMaker domain to use.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**     |
| -------------------------- | ------------------ | ----------------- | --------------------------------- |
| SageMakerDomainId          | Required           | `none`            | `SageMakerDomainId=d-abcdef1234;` |

## SageMaker project ID

The identifier of the SageMaker project to use.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**      |
| -------------------------- | ------------------ | ----------------- | ---------------------------------- |
| SageMakerProjectId         | Required           | `none`            | `SageMakerProjectId=p-abcdef1234;` |

## SageMaker domain region

The AWS Region where your SageMaker domain is provisioned.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**      |
| -------------------------- | ------------------ | ----------------- | ---------------------------------- |
| SageMakerDomainRegion      | Required           | `none`            | `SageMakerDomainRegion=us-east-1;` |

## SSO OIDC start URL

The issuer URL of the AWS Identity and Access Management Identity Center instance that the SageMaker domain
uses.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example**                                |
| -------------------------- | ------------------ | ----------------- | ------------------------------------------------------------ |
| sso\_oidc\_start\_url      | Required           | `none`            | `sso_oidc_start_url=https://d-1234567890.awsapps.com/start;` |

## SSO OIDC region

The AWS Region where the AWS Identity and Access Management Identity Center instance is provisioned.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| sso\_oidc\_region          | Required           | `none`            | `sso_oidc_region=us-east-1;`  |

## SSO OIDC cache

When enabled, allows the same AWS Identity and Access Management Identity Center access token to be cached to
disk and reused across driver connections. This prevents SQL tools that create multiple
driver connections from launching multiple browser windows.

| **Connection string name** | **Parameter type** | **Default value** | **Connection string example** |
| -------------------------- | ------------------ | ----------------- | ----------------------------- |
| sso\_oidc\_cache           | Optional           | `false`           | `sso_oidc_cache=true;`        |
