

# Bid construction and templating
<a name="yield-optimization-bid-construction"></a>

This page explains how MediaTailor builds an OpenRTB bid request from your template, how variable interpolation works, and what values MediaTailor sets automatically.

## Configuration fields
<a name="yield-optimization-bid-construction-config-fields"></a>

When you enable Yield Optimization on a playback configuration, you provide four fields:


| Field | Description | Required | 
| --- | --- | --- | 
| PublisherId | Your APS publisher ID (obtained from APS registration). Injected into app.publisher.id on every bid request. | Yes | 
| Region | APS region: AMERICAS, EUROPE, or ASIA\_PACIFIC. Determines the APS endpoint. | Yes | 
| MinimumUnfilledDuration | Minimum unfilled seconds required before MediaTailor triggers a bid request. Also used as imp.video.minduration. | Yes | 
| OpenRtbTemplate | Your ORTB JSON template (max 100 KB). Defines the bid request body. | Yes | 

## How the bid request is constructed
<a name="yield-optimization-bid-construction-how"></a>

When an ad break has unfilled duration remaining, MediaTailor constructs the bid request in these steps:

1. **Template interpolation.** MediaTailor resolves `{{session.*}}`, `{{player_params.*}}`, `{{avail.*}}`, `{{request.*}}`, `{{asset.*}}`, and `{{scte.*}}` placeholders in your template using standard [Mustache templating](https://mustache.github.io/mustache.5.html) syntax. Mustache uses double curly brackets `{{ }}`, which differs from the square brackets `[ ]` used in ADS URL variable substitution.

1. **JSON parsing.** The interpolated template is parsed as JSON.

1. **Field extraction and validation.** MediaTailor extracts mandatory fields and throws a `BidRequestConfigurationError` if any are missing or empty.

1. **Hardcoded field injection.** MediaTailor overrides or injects fields it manages automatically using values from the console configuration and the current avail context (for example, `app.publisher.id` from your configured Publisher ID, `imp.video.maxduration` from the calculated unfilled duration).

1. **Serialization and submission.** The final BidRequest is serialized to JSON and sent as an HTTP POST to the APS endpoint.

**Important**  
If any mandatory field is missing or empty after interpolation, the bid request fails with a `BidRequestConfigurationError` and no request is sent to APS. The error is logged but playback continues normally (fail-open).

## Console default template
<a name="yield-optimization-bid-construction-default-template"></a>

When you enable Yield Optimization in the MediaTailor console, the following pre-filled template is provided as a starting point. You should customize the values for your application:

```
{
  "imp": [
    {
      "bidfloor": 5
    }
  ],
  "app": {
    "id": "{{player_params.app_id}}",
    "name": "{{player_params.app_name}}",
    "bundle": "{{player_params.bundle}}",
    "storeurl": "{{player_params.storeurl}}",
    "domain": "{{player_params.domain}}",
    "content": {
      "genre": "{{asset.genre}}",
      "contentrating": "{{asset.content_rating}}"
    }
  },
  "device": {
    "dnt": "{{player_params.dnt}}",
    "ua": "{{session.user_agent}}",
    "ip": "{{session.client_ip}}",
    "ifa": "{{player_params.device_ifa}}",
    "w": "{{player_params.device_width}}",
    "h": "{{player_params.device_height}}",
    "language": "{{player_params.language}}",
    "model": "{{player_params.model}}",
    "os": "{{player_params.os}}",
    "osv": "{{player_params.osv}}",
    "devicetype": "{{player_params.devicetype}}",
    "make": "{{player_params.make}}"
  },
  "user": {
    "consent": "{{player_params.consent}}"
  },
  "regs": {
    "gdpr": "{{player_params.gdpr}}",
    "us_privacy": "{{player_params.us_privacy}}",
    "gpp": "{{player_params.gpp_consent}}",
    "gpp_sid": "{{player_params.gpp_sid}}"
  }
}
```

**Field-by-field explanation:**


| Field | Category | What to do | 
| --- | --- | --- | 
| imp[0].bidfloor | Optional (default: 1.0) | Set your minimum CPM. Console default is $5. Lower for better fill rates during testing. | 
| app.id | APS Recommended | Your app identifier. Player must send playerParams.app\_id. | 
| app.name | APS Recommended | Your app name. Player must send playerParams.app\_name. | 
| app.bundle | Mandatory | Your app bundle ID. Player must send playerParams.bundle, or replace with a static value (recommended). | 
| app.storeurl | Mandatory | Your app store URL. Player must send playerParams.storeurl, or replace with a static value (recommended). | 
| app.domain | APS Recommended | Your app domain. Player must send playerParams.domain. | 
| app.content.genre | APS Recommended | Populated from content source asset metadata. | 
| app.content.contentrating | APS Recommended | Populated from content source asset metadata. | 
| device.dnt | APS Recommended | Do Not Track flag. Player must send playerParams.dnt. | 
| device.ua | Mandatory | Automatically populated from the viewer's User-Agent header through {{session.user\_agent}}. No player param needed. | 
| device.ip | Mandatory | Automatically populated from the viewer's IP through {{session.client\_ip}}. No player param needed. | 
| device.ifa | APS Recommended | Advertising ID. Player must send playerParams.device\_ifa. | 
| device.w / device.h | APS Recommended | Screen dimensions. Player must send playerParams.device\_width / device\_height. | 
| device.language | APS Recommended | Device language. Player must send playerParams.language. | 
| device.model | APS Recommended | Device model. Player must send playerParams.model. | 
| device.os / device.osv | APS Recommended | OS and version. Player must send playerParams.os / osv. | 
| device.devicetype | Overridable (default: 3) | IAB device type. Player must send playerParams.devicetype. Defaults to 3 (CTV) if empty. | 
| device.make | APS Recommended | Device manufacturer. Player must send playerParams.make. | 
| user.consent | APS Recommended (EU) | GDPR consent string (TCF). Player must send playerParams.consent. | 
| regs.gdpr | APS Recommended (EU) | GDPR flag (0 or 1). Player must send playerParams.gdpr. | 
| regs.us\_privacy | APS Recommended (US) | CCPA string (for example, 1YNY). Player must send playerParams.us\_privacy. | 
| regs.gpp | APS Recommended | Global Privacy Platform consent string. Player must send playerParams.gpp\_consent. Preferred over us\_privacy for better fill rates. | 
| regs.gpp\_sid | APS Recommended | GPP section IDs (for example, [7] for US National). Player must send playerParams.gpp\_sid. | 

**Important**  
The console default uses `{{player_params.*}}` for mandatory fields like `app.bundle` and `app.storeurl`. If your player does not send these parameters, the bid request will fail with `BidRequestConfigurationError`. For fields that are the same for every session (typically `app.bundle`, `app.storeurl`, `app.name`, and other app-level identifiers), consider replacing the placeholder with a static value (for example, `"bundle": "com.yourcompany.app"`). Do not hardcode fields that vary per viewer, such as `device.ua`, `device.ip`, `device.ifa`, GDPR and GPP consent strings, or any regs or user object fields. Those must come from `{{session.*}}` or `{{player_params.*}}`.

**Note**  
The console default does not include `video.mimes` or `video.protocols` in the template. MediaTailor uses hardcoded fallback values (`["video/mp4"]` for mimes, `[1,2,3,4,5,6,7,8]` for protocols) when these are not provided. You can add them to your template if you want to restrict the supported formats.

## Template interpolation (Mustache templating)
<a name="yield-optimization-bid-construction-interpolation"></a>

Your ORTB template uses [Mustache templating](https://mustache.github.io/mustache.5.html) syntax for dynamic value substitution. Placeholders use double curly brackets `{{ }}`.

### Available template variables
<a name="yield-optimization-bid-construction-variables"></a>

Your ORTB template can use the same dynamic variables available in ADS URL templates. These include session variables (for example, `{{session.user_agent}}`, `{{session.client_ip}}`), player parameters (`{{player_params.*}}`), asset metadata (`{{asset.*}}`), avail context (`{{avail.*}}`), and SCTE signal data (`{{scte.*}}`).

For the complete list of available variables and their descriptions, see [MediaTailor dynamic ad variables for ADS requests](variables.md). For how MediaTailor URL-decodes player parameter values before substituting them into the template, see [Encoding and decoding behavior](#yield-optimization-bid-construction-encoding) later on this page.

The most commonly used variables in ORTB templates are:
+ `{{session.user_agent}}`: Viewer's User-Agent header (use for `device.ua`).
+ `{{session.client_ip}}`: Viewer's IP address (use for `device.ip`).
+ `{{player_params.*}}`: Custom values passed by the player during session initialization.
+ `{{asset.*}}`: Content metadata from the origin (for example, `asset.genre`, `asset.content_rating`).

**Warning**  
Always wrap placeholders in quotes, even for numeric fields like `dnt` or `devicetype`. If a placeholder resolves to an empty string and is not quoted (for example, `"dnt": {{player_params.dnt}}`), the result is invalid JSON and the entire bid request fails with a `BidRequestConfigurationError`. Use `"dnt": "{{player_params.dnt}}"` instead. APS accepts numeric fields passed as strings. This behavior is by design because auto-quoting empty-string substitutions would conflict with the raw-JSON mode used elsewhere in the interpolator. The constraint is documented rather than enforced. See also [Encoding and decoding behavior](#yield-optimization-bid-construction-encoding) for how MediaTailor handles player param values before interpolation.

### How to pass player parameters
<a name="yield-optimization-bid-construction-pass-params"></a>

There are two ways to pass player parameters during session initialization.

**Method 1: POST request with JSON body (recommended)**

```
POST https://<mediatailor-endpoint>/v1/session/<config-hash>/<origin-id>/master.m3u8
Content-Type: application/json

{
  "playerParams": {
    "app_id": "558775_example",
    "slot_id": "608109df-2378-4bc5-8da5-24bc355f01a4",
    "os": "Tizen",
    "make": "Samsung",
    "model": "Tizen TV",
    "language": "en",
    "us_privacy": "1YNY"
  }
}
```

This method is preferred because it avoids URL-encoding issues with complex values like user agent strings.

**Method 2: URL query parameters**

```
GET https://<mediatailor-endpoint>/v1/session/<config-hash>/<origin-id>/master.m3u8
  ?playerParams.app_id=558775_example
```

With this method, values must be URL-encoded. MediaTailor URL-decodes them before interpolation.

### Encoding and decoding behavior
<a name="yield-optimization-bid-construction-encoding"></a>

MediaTailor performs **one level of URL decoding** on player parameter values before interpolating them into the template. This applies regardless of how the parameters are passed (POST body or URL query params).

**Examples of decoded values:**


| Value sent | Value after decoding (used in template) | 
| --- | --- | 
| Test%20Os | Test Os | 
| https%3A%2F%2Flocalhost | https://localhost | 
| foo%20bar | foo bar | 
| Mozilla%2F5.0%20(SMART-TV) | Mozilla/5.0 (SMART-TV) | 

**Key points:**
+ MediaTailor decodes to **one level only**. Double-encoded values (for example, `%2520`) will be decoded to `%20`, not to a space.
+ **POST body values** are also decoded. If your POST body contains URL-encoded values, they will be decoded before interpolation.
+ **Plain text values** (no encoding) pass through unchanged.
+ After decoding and interpolation, the entire template is parsed as JSON. Special characters in interpolated values (like unescaped quotes or backslashes) may break JSON parsing.

**Tip**  
If your player sends values that are already plain text (not URL-encoded), they work as-is. You only need to be aware of decoding if your player URL-encodes values before sending them.

### What happens when a variable is missing
<a name="yield-optimization-bid-construction-missing-variable"></a>

If the player does not send a parameter referenced in your template (for example, `{{player_params.app_name}}` but no `app_name` in the player params), the placeholder resolves to an **empty string** `""`.

**Impact:** If the empty string is in a mandatory field (like `app.bundle`), the bid request fails with `BidRequestConfigurationError`. If it's in an optional field, APS receives an empty value which may cause a no-bid (HTTP 204) response.

## What MediaTailor sets automatically
<a name="yield-optimization-bid-construction-auto-set"></a>

The following fields are always set by MediaTailor using values from your console configuration and the current avail context. If you include these in your template, your values are overridden:


| Field | Source | 
| --- | --- | 
| id | Auto-generated: {sessionId}\_{availId} format (for example, abc123-def456\_78901). Useful for correlating bid requests with session logs. | 
| app.publisher.id | Your PublisherId from the console configuration. | 
| imp[0].video.minduration | Your MinimumUnfilledDuration from the console configuration. | 
| imp[0].video.maxduration | Calculated: actual unfilled seconds for this avail. | 
| imp[0].video.maxseq | Calculated: floor(unfilled\_duration / 6). | 
| imp[0].video.poddur | Calculated: actual unfilled seconds for this avail. | 
| ext.integrationType | Always set to "EMT". | 

## Next steps
<a name="yield-optimization-bid-construction-next-steps"></a>
+ For the complete field-by-field reference, see [ORTB field reference](yield-optimization-ortb-reference.md).
+ For copy-paste templates, see [Example templates](yield-optimization-examples.md).