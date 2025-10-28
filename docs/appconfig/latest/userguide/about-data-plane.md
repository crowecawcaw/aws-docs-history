# Retrieving configuration data without AWS AppConfig Agent

The recommended way to retrieve configuration data from AWS AppConfig is by using the
Amazon-developed and managed AWS AppConfig Agent. With the agent, you can cache configuration data
locally and asynchronously poll the AWS AppConfig data plane service for updates. This
caching/polling process ensures that your configuration data is always available for your
application while minimizing latency and cost. If you prefer not to use the agent, you can
call public APIs directly from the AWS AppConfig data plane service.

The data plane service uses two API actions, [StartConfigurationSession](../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md "../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md") and [GetLatestConfiguration](../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md "../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md"). The data plane service also uses [separate endpoints](../../../general/latest/gr/appconfig.md#appconfigdata_data_plane "../../../general/latest/gr/appconfig.md#appconfigdata_data_plane") from the AWS AppConfig control plane.

###### Note

The data plane service replaces the previous process of retrieving configuration data by
using the `GetConfiguration` API action. The `GetConfiguration` API is
deprecated.

###### How it works

Here's how the process of directly calling AWS AppConfig APIs using the data plane service
works.

Your application retrieves configuration data by first establishing a configuration
session using the [StartConfigurationSession](../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md "../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md") API operation. Your session's client then makes periodic
calls to [GetLatestConfiguration](../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md "../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md") to check for and retrieve the latest data available.

When calling `StartConfigurationSession`, your code sends the following
information:

- Identifiers (ID or name) of an AWS AppConfig application, environment, and configuration
  profile that the session tracks.
- (Optional) The minimum amount of time the session's client must wait between calls to
  `GetLatestConfiguration`.
  In response, AWS AppConfig provides an `InitialConfigurationToken` to be given to the
  session's client and used the first time it calls `GetLatestConfiguration` for that
  session.

###### Important

This token should only be used once in your first call to
`GetLatestConfiguration`. You _must_ use the new token in
the `GetLatestConfiguration` response (`NextPollConfigurationToken`)
in each subsequent call to `GetLatestConfiguration`. To support long poll use
cases, the tokens are valid for up to 24 hours. If a `GetLatestConfiguration`
call uses an expired token, the system returns `BadRequestException`.

When calling `GetLatestConfiguration`, your client code sends the most recent
`ConfigurationToken` value it has and receives in response:

- `NextPollConfigurationToken`: the `ConfigurationToken` value to
  use on the next call to `GetLatestConfiguration`.
- `NextPollIntervalInSeconds`: the duration the client should wait before
  making its next call to `GetLatestConfiguration`.
- The configuration: the latest data intended for the session. This may be empty if the
  client already has the latest version of the configuration.

###### Important

Note the following important information.

- The [StartConfigurationSession](../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md "../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md") API should only be called once per application,
  environment, configuration profile, and client to establish a session with the service.
  This is typically done in the startup of your application or immediately prior to the
  first retrieval of a configuration.
- If your configuration is deployed using a `KmsKeyIdentifier`, your
  request to receive the configuration must include permission to call
  `kms:Decrypt`. For more information, see [Decrypt](../../../kms/latest/APIReference/API_Decrypt.md "../../../kms/latest/APIReference/API_Decrypt.md") in the
  _AWS Key Management Service API Reference_.
- The API operation previously used to retrieve configuration data,
  `GetConfiguration`, is deprecated. The `GetConfiguration` API
  operation does not support encrypted configurations.

## (Example) Retrieving a

configuration by calling AWS AppConfig APIs

The following AWS CLI example demonstrates how to retrieve configuration data by using the
AWS AppConfig Data `StartConfigurationSession` and
`GetLatestConfiguration` API operations. The first command starts a
configuration session. This call includes the IDs (or names) of the AWS AppConfig application, the
environment, and the configuration profile. The API returns an
`InitialConfigurationToken` used to fetch your configuration data.

```
aws appconfigdata start-configuration-session \
    --application-identifier `application_name_or_ID` \
    --environment-identifier `environment_name_or_ID` \
    --configuration-profile-identifier `configuration_profile_name_or_ID`
```

The system responds with information in the following format.

```
{
   "InitialConfigurationToken": `initial configuration token`
}
```

After starting a session, use [InitialConfigurationToken](../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md#API_appconfigdata_StartConfigurationSession_ResponseSyntax "../../2019-10-09/APIReference/API_appconfigdata_StartConfigurationSession.md#API_appconfigdata_StartConfigurationSession_ResponseSyntax") to call [GetLatestConfiguration](../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md "../../2019-10-09/APIReference/API_appconfigdata_GetLatestConfiguration.md") to fetch your configuration data. The configuration data
is saved to the `mydata.json` file.

```
aws appconfigdata get-latest-configuration \
    --configuration-token `initial configuration token` mydata.json
```

The first call to `GetLatestConfiguration` uses the
`ConfigurationToken` obtained from `StartConfigurationSession`. The
following information is returned.

```
{
    "NextPollConfigurationToken" : `next configuration token`,
    "ContentType" : `content type of configuration`,
    "NextPollIntervalInSeconds" : `60`
}
```

Subsequent calls to `GetLatestConfiguration`
_must_ provide `NextPollConfigurationToken` from the previous
response.

```
aws appconfigdata get-latest-configuration \
    --configuration-token `next configuration token` mydata.json
```

###### Important

Note the following important details about the `GetLatestConfiguration` API
operation:

- The `GetLatestConfiguration` response includes a
  `Configuration` section that shows the configuration data. The
  `Configuration` section only appears if the system finds new or updated
  configuration data. If the system doesn't find new or updated configuration data, then
  the `Configuration` data is empty.
- You receive a new `ConfigurationToken` in every response from
  `GetLatestConfiguration`.
- We recommend tuning the polling frequency of your
  `GetLatestConfiguration` API calls based on your budget, the expected
  frequency of your configuration deployments, and the number of targets for a
  configuration.
