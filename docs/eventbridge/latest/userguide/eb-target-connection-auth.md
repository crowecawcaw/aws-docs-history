# Authorization methods for connections in EventBridge

EventBridge connections support the following authorization methods:

- Basic
- API Key

For Basic and API Key authorization, EventBridge populates the required authorization headers for
you.

- OAuth

For OAuth authorization, EventBridge also exchanges your client ID and secret for an access
token and then manages it securely.

When you create a connection that uses OAuth authorization, you have the option of specifying a public or private authorization endpoint.

## Considerations when using OAuth

Keep in mind the following when using OAuth as an authorization method for connections:

- EventBridge refreshes OAuth tokens:
  - When a `401` or `407` response is returned.
  - Proactively during an HTTPS invocation, if the token is about to expire.

- You can use [Connection events](event-reference.md#event-reference-connections "event-reference.md#event-reference-connections") to be notified when a connection changes state, such as becoming deauthorized.
- We recommend you set the retry policy to greater than 0 for rules using connections that
  require OAuth. That way, if an OAuth token has expired, EventBridge will refresh
  the token when retrying the invocation.

For more information on setting a retry policy for a rule, see [Select targets](eb-create-rule-wizard.md#eb-create-rule-target "eb-create-rule-wizard.md#eb-create-rule-target").

## Considerations for connection authorization

When you create a connection, you can also include the header, body, and query
parameters that are required for authorization with an endpoint. You can use the same
connection for more than one HTTPS endpoint if the authorization for the endpoint is the
same.

When you create a connection and add authorization parameters, EventBridge creates a secret in
AWS Secrets Manager. The cost of both storing and accessing the Secrets Manager secret is included with the
charge for using an API destination.

For information on how to have EventBridge re-authorize the connection once you have updated it to address authorization or connectivity issues, see [Updating
connections](eb-target-connection-edit.md "eb-target-connection-edit.md").

###### Note

To successfully create or update a connection, you must use an account that has
permission to use Secrets Manager. The required permission is included in the [AWS managed policy: AmazonEventBridgeFullAccess](eb-use-identity-based.md#eb-full-access-policy "eb-use-identity-based.md#eb-full-access-policy"). The same
permission is granted to the [service-linked
role](eb-api-destinations.md#eb-api-destination-slr "eb-api-destinations.md#eb-api-destination-slr") that's created in your account for the connection.

For examples of how to create a CloudFormation template that provisions an EventBridge connection with authentication, see
[AWS::Events::Connection](../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-events-connection.md") in the _CloudFormation User
Guide_.
