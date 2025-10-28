# MediaTailor parameter troubleshooting

guide

AWS Elemental MediaTailor provides guidance for troubleshooting common parameter-related issues in
MediaTailor, including character restrictions, URL encoding problems, and configuration alias
errors.

## Character restriction

errors

Parameter values that contain unsupported characters may cause errors or
unexpected behavior.

###### Common symptoms

The following symptoms may indicate character restriction issues:

- Parameters not appearing in manifest URLs
- HTTP 400 errors during session initialization
- Truncated or corrupted parameter values
- ADS requests failing due to malformed URLs

###### Resolution steps

To resolve character restriction errors:

1. Review parameter values for unsupported characters: `:`,
   `?`, `&`, `=`, `%`,
   `/`
2. Apply proper URL-encoding for special characters (see [MediaTailor parameter reference and
   limitations](parameter-comprehensive-reference.md "parameter-comprehensive-reference.md"))
3. Avoid double characters such as `%%%` or `==`
4. Consider alternative parameter formats if full URLs cannot be used

###### Example URL encoding example

Instead of using:

```
manifest.redirect_url=https://example.com/path?param=value
```

Use URL-encoded format:

```
manifest.redirect_url=https%3A%2F%2Fexample.com%2Fpath%3Fparam%3Dvalue
```

## Length limitation

errors

Parameters that exceed length limits may be truncated or cause errors.

###### Length limits

The following length limits apply (see [MediaTailor parameter reference and
limitations](parameter-comprehensive-reference.md "parameter-comprehensive-reference.md") for complete
details):

- Manifest query parameters (total): 2000 characters
- ADS parameter names: 10,000 characters
- ADS parameter values: 25,000 characters
- ADS URLs: 25,000 characters

###### Resolution strategies

To handle length limitations:

1. Use shorter parameter names and values where possible
2. Split large parameter values into multiple smaller parameters
3. Use configuration aliases to map short aliases to longer values (see [MediaTailor configuration aliases
   overview](configuration-aliases-overview.md "configuration-aliases-overview.md"))
4. Consider using external storage for large data with parameter
   references

## Configuration alias

errors

Configuration alias issues can result in HTTP 400 errors or unexpected parameter
values.

###### Common configuration alias errors

The following errors commonly occur with configuration aliases:

- HTTP 400 error: Missing or invalid alias value
- Domain variables not resolving correctly
- Player parameters not being replaced with alias values

###### Resolution checklist

To resolve configuration alias errors:

1. Verify all domain variables are defined as
   `ConfigurationAliases`
2. Ensure player parameter variables use `player_params.`
   prefix
3. Confirm the list of aliased values is exhaustive for domain variables in
   critical URLs (`VideoContentSourceUrl`,
   `AdSegmentUrlPrefix`,
   `ContentSegmentUrlPrefix`)
4. Check that session initialization requests specify valid alias
   values
5. Validate JSON structure of ConfigurationAliases parameter

For detailed troubleshooting guidance, see [MediaTailor configuration aliases
troubleshooting guide](configuration-aliases-troubleshooting.md "configuration-aliases-troubleshooting.md").

###### Example Configuration alias validation

Ensure your configuration includes all required aliases:

```
"ConfigurationAliases": {
    "player_params.origin_domain": {
        "pdx": "abc.mediapackage.us-west-2.amazonaws.com",
        "iad": "xyz.mediapackage.us-east-1.amazonaws.com"
        // Must include all possible values used in session initialization
    }
}
```

## Parameter processing flow

issues

Understanding the parameter processing flow helps troubleshoot issues with
parameter forwarding and transformation.

###### Parameter processing order

MediaTailor processes parameters in the following order:

1. Session initialization parameter validation
2. Configuration alias resolution (if applicable)
3. Parameter filtering (ADS vs origin vs manifest)
4. URL encoding and formatting
5. Parameter application to URLs

###### Debugging parameter flow

To debug parameter processing issues:

1. Verify parameters are correctly specified in session initialization
2. Check that configuration aliases resolve to expected values
3. Confirm parameters appear in the correct URLs (manifest, ADS,
   origin)
4. Validate URL encoding is applied correctly

###### Example Parameter flow example

Session initialization:

```
POST master.m3u8
{
    "playerParams": {"origin_domain": "pdx"},
    "manifestParams": {"test": "123"}
}
```

After alias resolution and processing:

- Origin request:
  `https://abc.mediapackage.us-west-2.amazonaws.com/out/v1/abcd`
- Manifest URL:
  `/v1/master/.../index.m3u8?aws.sessionId=session&test=123`

## Security

considerations and best practices

MediaTailor implements security measures for parameter handling to prevent common
security issues.

###### Security measures

MediaTailor implements the following security measures:

1. Input size limitations to prevent database bloat
2. Proper encoding and sanitization of user input
3. URL-encoding of input to prevent response corruption

###### Best practices

Follow these best practices for secure parameter handling:

- Validate parameter values on the client side before sending
- Use configuration aliases to limit possible parameter values
- Avoid including sensitive information in parameters
- Monitor parameter usage for unusual patterns
- Keep parameter values within recommended length limits
