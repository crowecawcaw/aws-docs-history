

# Connections for API targets in Amazon EventBridge
<a name="eb-target-connection"></a>

To enable event buses and pipes to target custom resources, such as HTTPS APIs, you create connections. A *connection* defines the authorization method and credentials for EventBridge to use in connecting to a given resource. If you are connecting to a private API, such as a private API in an Amazon Virtual Private Cloud (Amazon VPC), you can also use the connection to define secure point-to-point network connectivity. 

You can create connections to target:
+ Public APIs, such as third-party SaaS applications.
+ Private APIs, such as custom resources that reside in an Amazon VPC or on-premise.

  EventBridge creates connections to private HTTPS endpoints by utilizing *resource configurations* created in Amazon VPC Lattice. A resource configuration is a logical object that identifies a resource, and specifies who can access it and how.

Use connections with:
+ API destinations in EventBridge

  When you create an API destination, you specify a connection to use for it. You can choose an existing connection from your account, or create a connection when you create an API destination. 

  For more information, see [API destinations](eb-api-destinations.md).
+ HTTP Endpoint tasks in AWS Step Functions

  An HTTP Endpoint task is a type of Task workflow state that lets you call HTTPS APIs in your workflows. These APIs can be public, such as Salesforce and Stripe, or private APIs that reside in an Amazon VPC or on-premise. The task uses a connection to specify the authorization type and credentials to use for authorizing the API. For private APIs, the connection also defines the network path to the API.

  For more information, see [Call HTTPS APIs in Step Functions workflows](https://docs.aws.amazon.com/step-functions/latest/dg/connect-third-party-apis.html) in the *Step Functions User Guide*.

![EventBridge and Step Functions use connections as authorization and network connectivity configurations for HTTPS endpoints.](http://docs.aws.amazon.com/eventbridge/latest/userguide/images/connections-overview_eventbridge_conceptual.svg)


Connections are reusable. You can use the same connection to the same API for multiple EventBridge API destinations or Step Functions tasks, as long as the authentication method is the same. If API destinations or tasks require different authentication, then you must create separate connections.

## Storing connection authorization parameters in AWS Secrets Manager
<a name="connection-secrets"></a>

When you configure the authorization settings and create a connection, it creates a secret in AWS Secrets Manager to securely store the authorization information. You can also add additional parameters to include in the connection as appropriate for your HTTPS endpoint target.

EventBridge connections support the following authentication methods: basic, OAuth, and API Key. For more information, see [Connection authorization methods](eb-target-connection-auth.md).

While by default EventBridge uses an AWS owned key to encrypt and decrypt the connection secret, you can specify a customer managed key for EventBridge to use instead. For more information, see [Encrypting connections](encryption-connections.md).