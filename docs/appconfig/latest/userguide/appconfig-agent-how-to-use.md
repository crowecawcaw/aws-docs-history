

# How to use AWS AppConfig Agent to retrieve configuration data
<a name="appconfig-agent-how-to-use"></a>

The AWS AppConfig Agent is the recommended method for retrieving AWS AppConfig feature flags or free form configuration data. The agent is supported on all forms of AWS Compute including Amazon EC2, Amazon ECS, Amazon EKS, and Lambda. After you complete the initial agent set up, using the agent to retrieve configuration data is simpler than directly calling AWS AppConfig APIs. The agent automatically implements best practices and may lower your cost of using AWS AppConfig as a result of fewer API calls to retrieve configurations.

**Note**  
Retrieving configuration data from a separate AWS account isn't supported.

## Using AWS AppConfig Agent for user- or entity-based gradual deployments
<a name="appconfig-entity-based-gradual-deployments"></a>

AWS AppConfig Agent supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests.

With entity-based gradual deployments, AWS AppConfig Agent evaluates a unique identifier (`Entity-Id`) supplied with each HTTP request. Based on this identifier, the agent consistently serves either the new or previous configuration version throughout the deployment period. This process ensures that once a user receives the updated configuration, they continue to receive it. It also ensures that rollback alarms have sufficient time and data to detect issues.

Consider entity-based gradual deployments if a configuration directly changes user-facing behavior and if the change in blast radius (impacting specific users fully rather than all users partially) is acceptable for your application.

**Important**  
Note the following important information about entity-based gradual deployments:  
Entity-based gradual deployments require AWS AppConfig Agent version 2.0.136060 or later.
`Entity-Id` accepts a maximum string size of 2 KB.
Unique identifiers must not be hard-coded or low cardinality.
Identifiers aren't sent to the AWS AppConfig service. AWS AppConfig Agent evaluates unique identifiers client-side.
During a deployment, AWS AppConfig Agent keeps track of entities and deployed configurations. This tracking is maintained only during a deployment period. The tracking ends when the deployment completes.
Each instance of AWS AppConfig polls for deployment state independently, so agents may briefly serve different versions of the same entity as the deployment percentage changes. This window is determined by the poll interval and a short synchronization period. You can reduce it by setting `RequiredMinimumPollIntervalInSeconds` in the [StartConfigurationSession](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html) API action. However, shorter intervals increase API call rates, which can raise costs and risk throttling. Choose a poll interval that meets your requirements. For more information, see [StartConfigurationSession](https://docs.aws.amazon.com/cli/latest/reference/appconfigdata/start-configuration-session.html) in the AWS CLI Reference.

### Enabling entity-based gradual deployments
<a name="appconfig-entity-based-gradual-deployments-enabling"></a>

To enable entity-based gradual deployments:

1. Update to AWS AppConfig Agent version 2.0.136060 or later.

1. Provide a unique identifier in the `Entity-Id` HTTP header when retrieving configuration data.

The following example request uses an email address for `Entity-Id`

```
GET /applications/myapp/environments/prod/configurations/featureflags HTTP/1.1
Host: localhost:2772
Entity-Id: example@AWS-example-email.com
```

You can include the `Entity-Id` header in requests to:

/applications/{Application}/environments/{Environment}/configurations/{Configuration}

To view code samples with `Entity-Id`, see [Using AWS AppConfig Agent to read a freeform configuration profile](appconfig-code-samples-agent-read-configuration.md).

The `Entity-Id` value can be any string that uniquely identifies an entity in your system, such as:
+ Customer ID
+ Email address
+ Account ID
+ Backend job ID
+ Session-scoped identifier (if appropriate)