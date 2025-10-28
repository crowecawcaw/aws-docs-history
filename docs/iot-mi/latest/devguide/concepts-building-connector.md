# Build a C2C (Cloud-to-Cloud) connector

The following sections cover the steps to build a C2C (Cloud-to-Cloud) connector for
managed integrations for AWS IoT Device Management.

###### Topics

- [Prerequisites](#c2c-connector-prerequisites "#c2c-connector-prerequisites")
- [C2C connector requirements](#c2c-connector-requirements "#c2c-connector-requirements")
- [OAuth 2.0 requirements for account linking](concepts-account-linking.md "concepts-account-linking.md")
- [Implement C2C connector interface operations](connector-operations-overview.md "connector-operations-overview.md")
- [Invoke your C2C connector](allow-iot-smart-home.md "allow-iot-smart-home.md")
- [Add permissions to your IAM Role](adding-permissions-to-iam-role.md "adding-permissions-to-iam-role.md")
- [Manually test your C2C connector](manually-testing-connector.md "manually-testing-connector.md")

## Prerequisites

Before you create a C2C (Cloud-to-Cloud) connector, you need the following:

- An AWS account to host your C2C connector and to register it
  through managed integrations. For more information, see [Create an
  AWS account](../../../accounts/latest/reference/manage-acct-creating.md "../../../accounts/latest/reference/manage-acct-creating.md").
- When you build your connector, you need certain IAM permissions. To use the
- Ensure that the third-party cloud providers that the connector is intended for, support OAuth 2.0 authorization. For more information, see [OAuth 2.0 requirements for account linking](concepts-account-linking.md "concepts-account-linking.md").

In
addition, to test the connector, the developer of the connector must have the following:

    + A client ID from the third-party cloud to associate with your C2C connector
    + A client secret from the third-party cloud to associate with your C2C connector
    + An OAuth 2.0 authorization URL
    + An OAuth 2.0 token URL

- Any API keys required by your third-party API
- Any API keys that are required by your third-party API registration or allowlisting for the OAuth callback URL hosted by AWS. Some third parties explicitly allowlist
  an OAuth redirect URL, while others have a workflow where users can log in and register the OAuth URL. Consult with the specific third party to understand what is required to
  allowlist the managed integrations OAuth redirection endpoint

### Required permissions

When you build your connector, you need certain IAM permissions. In addition to the `iotmanagedintegrations:` permissions for the
actions, you need the following permissions:

- [CreateAccountAssociation](../APIReference/API_CreateAccountAssociation.md "../APIReference/API_CreateAccountAssociation.md"), [CreateConnectorDestination](../APIReference/API_CreateConnectorDestination.md "../APIReference/API_CreateConnectorDestination.md"),
  [GetAccountAssociation](../APIReference/API_GetAccountAssociation.md "../APIReference/API_GetAccountAssociation.md"), and
  [StartAccountAssociationRefresh](../APIReference/API_StartAccountAssociationRefresh.md "../APIReference/API_StartAccountAssociationRefresh.md"), require
  `secretsmanager:GetSecretValue`
- [CreateCloudConnector](../APIReference/API_CreateCloudConnector.md "../APIReference/API_CreateCloudConnector.md") requires `lambda:Invoke`

For more information about `iotmanagedintegrations:` permissions and actions, see
[Actions defined by AWS Managed integrations](../../../service-authorization/latest/reference/list_awsiotmanagedintegrations.md#awsiotmanagedintegrations-actions-as-permissions "../../../service-authorization/latest/reference/list_awsiotmanagedintegrations.md#awsiotmanagedintegrations-actions-as-permissions")

## C2C connector requirements

The [C2C connector](concepts-c2c-connector.md#concepts-what-is-c2c-connector "concepts-c2c-connector.md#concepts-what-is-c2c-connector") you develop
facilitates the bidirectional communication between managed integrations for AWS IoT Device Management and a third-party vendor cloud. The
connector must implement interfaces for managed integrations for AWS IoT Device Management to perform actions on
behalf of end users. These interfaces provide the functionality to discover end-user devices,
initiate device commands that are sent from managed integrations for AWS IoT Device Management, and identify users based on an
access token. To support the device operations, the connector must manage the translation of
the request and response messages between managed integrations for AWS IoT Device Management and the related third party
platform.

###### The following are requirements for the C2C connector:

- The third-party Authorization server must conform to OAuth 2.0 standards as well as
  the configurations listed in [OAuth configuration requirements](concepts-account-linking.md#oauth-config-requirements "concepts-account-linking.md#oauth-config-requirements").
- A C2C connector will be required to interpret identifiers from AWS implementations of the
  Matter Data Model and
  must emit the responses and events that are compliant with AWS implementations of the
  Matter Data Model. For
  more information, see [AWS implementation of the Matter data model](matter-data-model.md "matter-data-model.md")
- A C2C connector must be able to call the managed integrations for AWS IoT Device Management APIs with `SigV4`
  authentication. For asynchronous events sent with the SendConnectorEvent API, the same
  AWS account credentials used to register the connector must be used to sign the
  related SendConnectorEvent request.
- The connector must implement the `AWS.ActivateUser`, `AWS.DiscoverDevices`, `AWS.SendCommand`, and `AWS.DeactivateUser` operations.
- When your C2C connector receives third-party events related to device command responses or
  device discovery, it must forward them to managed integrations with the `SendConnectorEvent` API. For more
  information on these events and the `SendConnectorEvent` API, see [SendConnectorEvent](https://amazonaws.com/iot-mi/latest/APIReference/API_SendConnectorEvent.html "https://amazonaws.com/iot-mi/latest/APIReference/API_SendConnectorEvent.html").

###### Note

The
`SendConnectorEvent` API is part of managed integrations SDK and is used, instead of manual building and signing of requests.
