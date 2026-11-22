

# Retrieving feature flags and configuration data in AWS AppConfig

Your application retrieves feature flags, free form configuration data, and AI configurations by establishing a configuration session using the AWS AppConfig Data service. We strongly recommend that you use AWS AppConfig Agent to retrieve configuration data. The agent (or the AWS AppConfig Agent Lambda extension for Lambda compute environments) manages a series of API calls and session tokens on your behalf, and it implements best practices for configuration retrieval on your behalf, including the following:
+ **Caching** – The agent caches your configuration data locally, so your application retrieves data from the local cache instead of calling AWS AppConfig on every request. This reduces latency and API calls.
+ **Background polling** – The agent polls AWS AppConfig for configuration updates in the background and refreshes its cache automatically, so your application receives new configuration data without implementing its own polling logic.
+ **Static stability** – If your application can't reach the AWS AppConfig service, the agent continues to serve the last known good configuration from its cache. Your application keeps running with the most recent configuration it received instead of failing.

From a high level, the process works as follows:

1. You configure AWS AppConfig Agent as a local host and have the agent poll AWS AppConfig for configuration updates.

1. The agent calls the [StartConfigurationSession](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.html) and [GetLatestConfiguration](https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.html) API actions and caches your configuration data locally.

1. To retrieve the data, your application makes an HTTP call to the localhost server. AWS AppConfig Agent supports several use cases, as described in [How to use AWS AppConfig Agent to retrieve configuration data](appconfig-agent-how-to-use.md).

If you prefer, you can manually call these API actions to retrieve a configuration. The API process works as follows:

1. Your application establishes a configuration session using the `StartConfigurationSession` API action. Your session's client then makes periodic calls to `GetLatestConfiguration` to check for and retrieve the latest data available.

1. When calling `StartConfigurationSession`, your code sends identifiers (ID or name) of an AWS AppConfig application, environment, and configuration profile that the session tracks.

1. In response, AWS AppConfig provides an `InitialConfigurationToken` to be given to the session's client and used the first time it calls `GetLatestConfiguration` for that session.

1. When calling `GetLatestConfiguration`, your client code sends the most recent `ConfigurationToken` value it has and receives in response:
   + `NextPollConfigurationToken`: the `ConfigurationToken` value to use on the next call to `GetLatestConfiguration`.
   + The configuration: the latest data intended for the session. This may be empty if the client already has the latest version of the configuration.

**Note**  
Retrieving configuration data from a separate AWS account isn't supported.

**Topics**
+ [What is AWS AppConfig Agent?](appconfig-agent.md)
+ [How to use AWS AppConfig Agent to retrieve configuration data](appconfig-agent-how-to-use.md)