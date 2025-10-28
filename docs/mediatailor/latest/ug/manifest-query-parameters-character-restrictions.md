# MediaTailor parameter

character restrictions and URL-encoding

AWS Elemental MediaTailor supports specific characters in manifest query parameters. You can use
URL-encoding for special characters.

###### Supported characters with URL-encoding

The following special characters are supported with URL-encoding:

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

MediaTailor supports the percent (%) sign when you use it in URL-encoding (for example,
hello%20world = hello world). You can use any URL-encoded characters, as long as
they are valid URL-encodings according to the HTTP specification.

###### Important

MediaTailor doesn't support double characters such as %%% or ==.

###### Security considerations

MediaTailor implements the following security measures for parameter handling:

1. Input size limitations to prevent database bloat
2. Proper encoding and sanitization of user input
3. URL-encoding of input to prevent response corruption
