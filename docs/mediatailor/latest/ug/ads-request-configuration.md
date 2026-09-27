

# Configuring the ADS request
<a name="ads-request-configuration"></a>

Use `AdDecisionServerConfiguration` to control how AWS Elemental MediaTailor calls your ad decision server (ADS). This ensures your ADS receives the context it needs to return relevant ads. Use it to configure any of the following:
+ A `POST` body (for example, an OpenRTB bid request).
+ Custom request headers (for example, `Accept-Language`).
+ A compressed payload.

By default, your ADS receives a `GET` request at the URL specified by `AdDecisionServerUrl`. To customize the request beyond that default, configure the `AdDecisionServerConfiguration` field on the playback configuration.

Use `AdDecisionServerConfiguration.HttpRequest` to configure the ADS request. The `Headers` and `Body` fields support dynamic variables, which MediaTailor substitutes with session-scoped values at request time.

## HttpRequest fields
<a name="ads-request-configuration-fields"></a>

The following table describes the fields under `AdDecisionServerConfiguration.HttpRequest`.


| Field | Type | Description | 
| --- | --- | --- | 
| Method | String enum | The HTTP method MediaTailor uses when it calls the ADS. Valid values are GET and POST. Defaults to GET if omitted. | 
| Headers | Map of string to string | Custom HTTP request headers to attach to the outbound ADS call. Header values support dynamic variable substitution using the {{variable}} template syntax (see [Template variable syntax](#ads-request-configuration-template-syntax)). MediaTailor sends these headers on both GET and POST requests. | 
| Body | String | The request body template. Use this field only when Method is POST. Supports dynamic variable substitution using the {{variable}} template syntax. If a Content-Type header is set in Headers and includes application/json, MediaTailor JSON-escapes substituted values automatically. Otherwise, MediaTailor substitutes values as plain text. | 
| CompressionMethod | String enum | The compression to apply to the request body. Valid values are NONE and GZIP. Defaults to NONE. When set to GZIP, MediaTailor compresses the interpolated body and sets the Content-Encoding: gzip header on the request. Only applies to POST requests. | 

## Template variable syntax
<a name="ads-request-configuration-template-syntax"></a>

`Headers` and `Body` both support dynamic variable substitution using the `{{variable}}` template syntax. This is different from the `[variable]` syntax used by `AdDecisionServerUrl`. The following table summarizes the two conventions.


| Where you reference variables | Syntax | 
| --- | --- | 
| AdDecisionServerUrl | [variable] – for example, [session.user\_agent] | 
| AdDecisionServerConfiguration.HttpRequest.Headers | {{variable}} – for example, {{session.user\_agent}} | 
| AdDecisionServerConfiguration.HttpRequest.Body | {{variable}} – for example, {{session.uuid}} | 

All dynamic variables that MediaTailor supports work in both locations. These include session variables, SCTE-35 variables, player parameters, and configuration aliases. Only the delimiter differs. For the complete list of supported variables, see [MediaTailor session variables for ADS requests](variables-session.md) and [MediaTailor player variables for ADS requests](variables-player.md).

## Forwarding Accept-Language as a request header
<a name="ads-request-configuration-headers-example"></a>

To serve language-specific ads, forward the viewer's language preference to your ADS. The following playback configuration passes the `Accept-Language` header (captured at session initialization) as an HTTP request header on every ADS call:

```
{
    "Name": "customerConfig",
    "VideoContentSourceUrl": "https://origin.example.com/",
    "AdDecisionServerUrl": "https://ads.example.com/vast",
    "AdDecisionServerConfiguration": {
        "HttpRequest": {
            "Method": "GET",
            "Headers": {
                "Accept-Language": "{{session.accept_language}}"
            }
        }
    }
}
```

MediaTailor auto-populates `session.accept_language` from the `Accept-Language` HTTP header that the player sends on the manifest request. Header lookup is case-insensitive. If the player does not send an `Accept-Language` header, `session.accept_language` is empty and the outbound header value is empty.

**CDN and proxy requirements**  
If you use a CDN or proxy in front of the manifest endpoint, configure it to forward the `Accept-Language` header. This ensures the player's language preference reaches MediaTailor.  
The CloudFront managed policy `Managed-Elemental-MediaTailor-PersonalizedManifests` does not forward this header. Use a policy that does (such as `AllViewer`) or add the header to a custom origin request policy allowlist.

## Sending a POST request with a JSON body
<a name="ads-request-configuration-post-example"></a>

The following playback configuration sends a `POST` request with a JSON body and a matching `Content-Type` header:

```
{
    "Name": "customerConfig",
    "VideoContentSourceUrl": "https://origin.example.com/",
    "AdDecisionServerUrl": "https://ads.example.com/ortb",
    "AdDecisionServerConfiguration": {
        "HttpRequest": {
            "Method": "POST",
            "Headers": {
                "Content-Type": "application/json",
                "Accept-Language": "{{session.accept_language}}"
            },
            "Body": "{\"id\": \"{{session.uuid}}\", \"user\": {\"ua\": \"{{session.user_agent}}\", \"ip\": \"{{session.client_ip}}\"}}",
            "CompressionMethod": "GZIP"
        }
    }
}
```

Because `Content-Type` contains `application/json`, MediaTailor JSON-escapes substituted values so special characters (quotes, backslashes) in variable values do not break the JSON document. MediaTailor then gzip-compresses the interpolated body and sets `Content-Encoding: gzip` on the outbound request.

## HttpRequest limitations
<a name="ads-request-configuration-limitations"></a>

The following limitations apply to `AdDecisionServerConfiguration.HttpRequest`:
+ MediaTailor applies `CompressionMethod` only when `Method` is `POST`.
+ Variable substitution in `Headers` and `Body` uses `{{variable}}` syntax. Substitution in `AdDecisionServerUrl` uses `[variable]` syntax. The two are not interchangeable.
+ Variables that are unresolved at request time render as an empty string in both headers and body.