# MediaTailor passing parameters to ADS

AWS Elemental MediaTailor supports setting up dynamic variables in MediaTailor requests to the ADS using the
following steps.

- For information about supported formatting for query parameters, see [MediaTailor parameter reference and
  limitations](parameter-comprehensive-reference.md "parameter-comprehensive-reference.md").
- For configuration aliases and domain variables, see [MediaTailor configuration aliases
  overview](configuration-aliases-overview.md "configuration-aliases-overview.md").
- For additional customizations to the ADS request, see [Advanced usage](#variables-advanced-usage "#variables-advanced-usage").

###### Session initialization methods

MediaTailor supports multiple methods for session initialization and parameter passing:

1. **POST with Request Body:**

```
POST <master>.m3u8
{
    "adsParams": {"param1": "value1", "param2": "value2"},
    "playerParams": {"param3": "value3"}
}
```

2. **Query Parameters in URL:**

```
GET <master>.m3u8?ads.param1=value1&ads.param2=value2&playerParams.param3=value3
```

###### Important

You can only specify parameters once, at initialization time. Configuration
aliases resolve to actual values before forwarding.

###### To pass session and player information to the ADS

1. Work with the ADS to determine the information that it needs to respond to an
   ad query from AWS Elemental MediaTailor.
2. Create a configuration in MediaTailor that uses a template ADS request URL
   that satisfies the ADS requirements. In the URL, include static parameters and
   include placeholders for dynamic parameters. Enter your template URL in the
   configuration's **Ad decision server** field.

In the following example template URL, `correlation` provides
session data, and `deviceType` provides player data:

```
https://my.ads.server.com/path?correlation=[session.id]&deviceType=[player_params.deviceType]
```

3. On the player, configure the session initiation request for AWS Elemental MediaTailor
   to provide parameters for the player data. Include your parameters in the
   session initiation request, and omit them from subsequent requests for the
   session.

The type of call that the player makes to initialize the session determines
whether the player (client) or MediaTailor (server) provides ad-tracking
reporting for the session. For information about these two options, see [Reporting ad tracking data](ad-reporting.md "ad-reporting.md") .

Make one of the following types of calls, depending on whether you want
server- or client-side ad-tracking reporting. In both of the example calls,
`userID` is intended for the ADS and `auth_token` is
intended for the origin:

    * (Option) Call for server-side ad-tracking reporting – Prefix
     the parameters that you want MediaTailor to send to the ADS with
     `ads`. Leave the prefix off for parameters that you want
     MediaTailor to send to the origin server:


    The following examples show incoming requests for HLS and DASH to
     AWS Elemental MediaTailor. MediaTailor uses the `deviceType` in its
     request to the ADS and the `auth_token` in its request to the
     origin server.


    HLS example:



    ```
    GET master.m3u8?ads.deviceType=ipad&auth_token=kjhdsaf7gh
    ```

    DASH example:



    ```
    GET manifest.mpd?ads.deviceType=ipad&auth_token=kjhdsaf7gh
    ```
    * (Option) Call for client-side ad-tracking reporting – Provide
     parameters for the ADS inside an `adsParams` object.


    HLS example:



    ```
    POST master.m3u8
        {
            "adsParams": {
               "deviceType": "ipad"
           }
        }
    ```

    DASH example:



    ```
    POST manifest.mpd
        {
            "adsParams": {
               "deviceType": "ipad"
           }
        }
    ```

When the player initiates a session, AWS Elemental MediaTailor replaces the variables in the
template ADS request URL with the session data and the player's `ads`
parameters. It passes the remaining parameters from the player to the origin server.

###### Example MediaTailor requests with ad variables

The following examples show the calls to the ADS and origin server from
AWS Elemental MediaTailor that correspond to the preceding player's session initialization
call examples:

- MediaTailor calls the ADS with session data and the player's device
  type:

```
https://my.ads.server.com/path?correlation=896976764&deviceType=ipad
```

- MediaTailor calls the origin server with the player's authorization
  token.
  - HLS example:

  ```
  https://my.origin.server.com/master.m3u8?auth_token=kjhdsaf7gh
  ```

  - DASH example:

  ```
  https://my.origin.server.com/manifest.mpd?auth_token=kjhdsaf7gh
  ```

## Advanced usage

You can customize the ADS request in many ways with player and session data. You
only need to include the ADS host name.

The following examples show some of the ways that you can customize your request:

- Concatenate player parameters and session parameters to create new
  parameters. Example:

```
https://my.ads.com?key1=[player_params.value1][session.id]
```

- Use a player parameter as part of a path element. Example:

```
https://my.ads.com/[player_params.path]?key=value
```

- Use player parameters to pass both path elements and the keys themselves,
  rather than just values. Example:

```
https://my.ads.com/[player_params.path]?[player_params.key1]=[player_params.value1]
```
