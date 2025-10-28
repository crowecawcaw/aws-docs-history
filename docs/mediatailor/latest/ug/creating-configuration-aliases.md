# Creating and using configuration

aliases with MediaTailor

Before you start to use domain variables, you create configuration aliases for your
configuration. You use the configuration aliases as domain replacement variables at
session initialization time.

###### Restrictions

Note the following restrictions when using configuration aliases:

- All dynamic variables used in the domain must be defined as a
  `ConfigurationAliases` dynamic variable.
- The player parameter variables must be prefixed with
  `player_params.`. For example,
  `player_params.origin_domain`.
- The list of aliased values must be exhaustive for domain variables in critical
  URLs (`VideoContentSourceUrl`, `AdSegmentUrlPrefix`,
  `ContentSegmentUrlPrefix`).
- If a request is made for a domain variable in critical URLs that either
  doesn't specify the dynamic variable or uses an invalid alias, the request will
  fail with an HTTP `400` status code. Non-critical fields
  (`SlateAdUrl`, `TranscodeProfileName`, bumper URLs)
  will log warnings but not fail the request.

###### Fallback behavior for missing aliases

When configuration aliases are not found or are invalid, MediaTailor implements the
following fallback behavior:

- **Domain variables:** If a domain variable alias
  is missing or invalid, the request fails with HTTP 400 status code. All domain
  variables must have valid aliases defined.
- **Non-domain variables:** For variables used in
  non-domain portions of URLs (such as path elements or query parameters), missing
  aliases result in empty string replacement.
- **Configuration validation:** MediaTailor validates
  that all required aliases are present during configuration creation and update
  operations.

## Step 1: Create

configuration aliases

To create configuration aliases to use for domain replacement using the MediaTailor
console, perform the following procedure.

Console ###### To create configuration aliases using the console

1. Open the MediaTailor console at [https://console.aws.amazon.com/mediatailor/](https://console.aws.amazon.com/mediatailor/ "https://console.aws.amazon.com/mediatailor/").
2. On the **Configuration aliases** section on the
   **Configurations** page, choose **Add player
   parameter**.
3. For **Player parameter**, enter the name of the player
   parameter that you want to use as a dynamic variable. For example,
   `player_params.origin_domain`.
4. For **Aliases**, enter the aliases and their values that
   you want to use for the player parameter.
5. Choose **OK**.

AWS Elemental MediaTailor displays the new parameter in the table in the
**Configuration aliases** section. 6. Repeat the preceding steps to add more player parameters. 7. Choose **Save**.

API ###### To create configuration aliases using the API

When you create or update a MediaTailor configuration, use the `ConfigurationAliases` parameter with the following JSON structure:

```
{
                "ConfigurationAliases": {
                "player_params.origin_domain": {
                "pdx": "abc.mediapackage.us-west-2.amazonaws.com",
                "iad": "xyz.mediapackage.us-east-1.amazonaws.com"
                },
                "player_params.ad_type": {
                "customized": "abc12345",
                "default": "defaultAdType"
                }
                }
                }
```

## Step 2: Use

configuration aliases in session initialization

After you set up the configuration aliases, you can use them as replacement
variables for domains in your session initialization request. This enables you to
dynamically configure the domains for your session.

###### Example Basic configuration aliases example

Here's a basic example of a configuration that includes configuration aliases
and dynamic domain variables:

```
PUT /playbackConfiguration
{
    "Name": "aliasedConfig",
    "AdDecisionServerUrl": "https://abc.execute-api.us-west-2.amazonaws.com/ads?sid=[session.id]&ad_type=[player_params.ad_type]",
    "VideoContentSourceUrl": "https://[player_params.origin_domain].mediapackage.[player_params.region].amazonaws.com/out/v1/[player_params.endpoint_id]",
    "ConfigurationAliases": {
        "player_params.origin_domain": {
            "pdx": "abc",
            "iad": "xyz"
        },
        "player_params.region": {
            "pdx": "us-west-2",
            "iad": "us-east-1"
        },
        "player_params.endpoint_id": {
            "pdx": "abcd",
            "iad": "wxyz"
        },
        "player_params.ad_type": {
            "customized": "abc12345",
            "default": "defaultAdType"
        }
    }
}
```

###### Example Session initialization with aliases

Using the preceding configuration, a session initialization request using the
player variables and aliases would look similar to the following:

```
POST index.m3u8
{
    "playerParams": {
        "origin_domain": "pdx",
        "region": "pdx",
        "endpoint_id": "pdx",
        "ad_type": "customized"
    }
}
```

MediaTailor replaces the alias strings with the mapped values in the
configuration aliases configuration.

The request to the ADS will look like the following:

```
https://abc.execute-api.us-west-2.amazonaws.com/ads?sid=[session.id]&ad_type=abc12345
```

The request to the origin for the manifests will look like the
following:

```
https://abc.mediapackage.us-west-2.amazonaws.com/out/v1/abcd
```
