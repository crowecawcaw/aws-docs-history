# Common data types

The Common Data Types describes miscellaneous common data types in AWS Lake Formation.

## ErrorDetail structure

Contains details about an error.

###### Fields

- `ErrorCode` – UTF-8 string, not less than 1 or more than 255 bytes long, matching the [Single-line string pattern](#aws-glue-api-regex-oneLine "#aws-glue-api-regex-oneLine").

The code associated with this error.

- `ErrorMessage` – Description string, not more than 2048 bytes long, matching the [URI address multi-line string pattern](#aws-glue-api-regex-uri "#aws-glue-api-regex-uri").

A message describing the error.

## String patterns

The API uses the following regular expressions to define what
is valid content for various string parameters and members:

- Single-line string pattern –
  "`[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`"
- URI address multi-line string pattern –
  "`[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`"
- Custom string pattern #3 –
  "`^\w+\.\w+\.\w+$`"
- Custom string pattern #4 –
  "`^\w+\.\w+$`"
- Custom string pattern #5 –
  "`arn:aws:iam::[0-9]*:role/.*`"
- Custom string pattern #6 –
  "`arn:aws:iam::[0-9]*:user/.*`"
- Custom string pattern #7 –
  "`arn:aws:iam::[0-9]*:group/.*`"
- Custom string pattern #8 –
  "`arn:aws:iam::[0-9]*:saml-provider/.*`"
- Custom string pattern #9 –
  "`^([\p{L}\p{Z}\p{N}_.:\/=+\-@%]*)$`"
- Custom string pattern #10 –
  "`^([\p{L}\p{Z}\p{N}_.:\*\/=+\-@%]*)$`"
- Custom string pattern #11 –
  "`[\p{L}\p{N}\p{P}]*`"
