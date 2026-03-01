# Understanding how the AWS AppConfig Agent Lambda extension works

If you use AWS AppConfig to manage configurations for a Lambda function
_without_ Lambda extensions, then you must configure your Lambda
function to receive configuration updates by integrating with the [StartConfigurationSession](../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md "../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md") and [GetLatestConfiguration](../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md "../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md") API actions.

Integrating the AWS AppConfig Agent Lambda extension with your Lambda function simplifies this
process. The extension takes care of calling the AWS AppConfig service, managing a local cache of
retrieved data, tracking the configuration tokens needed for the next service calls, and
periodically checking for configuration updates in the background. The following diagram
shows how it works.

![A diagram of how the AWS AppConfig Agent Lambda extension works](images/AppConfigLambdaExtension.png)

1. You configure the AWS AppConfig Agent Lambda extension as a layer of your Lambda function.
2. To access its configuration data, your function calls the AWS AppConfig extension at an
   HTTP endpoint running on `localhost:2772`.
3. The extension maintains a local cache of the configuration data. If the data isn't
   in the cache, the extension calls AWS AppConfig to get the configuration data.
4. Upon receiving the configuration from the service, the extension stores it in the
   local cache and passes it to the Lambda function.
5. AWS AppConfig Agent Lambda extension periodically checks for updates to your configuration
   data in the background. Each time your Lambda function is invoked, the extension checks
   the elapsed time since it retrieved a configuration. If the elapsed time is greater
   than the configured poll interval, the extension calls AWS AppConfig to check for newly
   deployed data, updates the local cache if there has been a change, and resets the
   elapsed time.

###### Note

- Lambda instantiates separate instances corresponding to the concurrency level
  that your function requires. Each instance is isolated and maintains its own local
  cache of your configuration data. For more information about Lambda instances and
  concurrency, see [Managing
  concurrency for a Lambda function](../../../lambda/latest/dg/configuration-concurrency.md "../../../lambda/latest/dg/configuration-concurrency.md").
- The amount of time it takes for a configuration change to appear in a Lambda
  function, after you deploy an updated configuration from AWS AppConfig, depends on the
  deployment strategy you used for the deployment and the polling interval you
  configured for the extension.
