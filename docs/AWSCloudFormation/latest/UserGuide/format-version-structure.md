# CloudFormation template format version syntax

The `AWSTemplateFormatVersion` section (optional) identifies the template
format version that the template conforms to. The latest template format version is
`2010-09-09` and is currently the only valid value.

The template format version isn't the same as the API version. The template format version
can change independently of the API versions.

The value for the template format version declaration must be a literal string. You can't
use a parameter or function to specify the template format version. If you don't specify a
value, CloudFormation assumes the latest template format version. The following snippet is an
example of a valid template format version declaration:

## JSON

```
"AWSTemplateFormatVersion" : "2010-09-09"
```

## YAML

```
AWSTemplateFormatVersion: 2010-09-09
```
