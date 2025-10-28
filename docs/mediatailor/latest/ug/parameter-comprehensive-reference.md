# MediaTailor parameter reference and

limitations

Before configuring dynamic ad variables, understand the parameter formatting
requirements and limitations that apply to all MediaTailor configurations.

AWS Elemental MediaTailor provides comprehensive information about parameter character restrictions,
length limitations, and supported formats for both manifest query parameters and ADS
parameters.

## Manifest query parameter

character restrictions

Manifest query parameters support specific characters and have defined length
limitations.

###### Supported characters (without URL-encoding)

You can use the following characters directly in manifest query parameters:

- Alphanumeric characters (A-Z, a-z, 0-9)
- Periods (.)
- Hyphens (-)
- Underscores (\_)
- Backslashes (\)

###### Supported characters with URL-encoding

The following special characters are supported when URL-encoded:

- period (.) = %2E
- dash (-) = %2D
- underscore (\_) = %5F
- percent (%) = %25
- tilde (~) = %7E
- forward slash (/) = %2F
- asterisk (\*) = %2A
- equals (=) = %3D
- question (?) = %3F

###### URL-encoding support

MediaTailor supports the percent (%) sign when you use it in URL-encoding (for
example, hello%20world = hello world). You can use any URL-encoded characters,
as long as they are valid URL-encodings according to the HTTP specification.

###### Unsupported characters

You cannot use the following characters in manifest query parameters without
URL-encoding: `:`, `?`, `&`,
`=`, `%`, `/` (forward slash).

###### Important

MediaTailor doesn't support double characters such as %%% or ==. You can't use full
URLs as manifest query parameter values due to character restrictions.

###### Length limitations

The total length of all manifest query parameters (keys and values combined)
must not exceed 2000 characters.

## ADS parameter length limitations

The following length limitations apply to parameters used in requests to the ADS:

- **ADS parameter name**: Maximum 10,000
  characters
- **ADS parameter value**: Maximum 25,000
  characters
- **ADS URL**: Maximum 25,000 characters
