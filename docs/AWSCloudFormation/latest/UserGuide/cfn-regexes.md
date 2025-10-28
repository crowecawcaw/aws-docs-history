# Using regular expressions in CloudFormation templates

You can use regular expressions (commonly known as regexes) in a number of places within
your CloudFormation templates, such as for the `AllowedPattern` property when creating
a template [parameter](parameters-section-structure.md "parameters-section-structure.md").

All regular expressions in CloudFormation conform to the Java regex syntax. For a comprehensive
description of the Java regex syntax and its constructs, see [java.util.regex.Pattern](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html "https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/regex/Pattern.html").

If you write your CloudFormation template in JSON syntax, you must escape any backslash
characters (\) in your regular expression by adding an additional backslash. This is because
JSON interprets backslashes as escape characters, and you need to escape them to ensure
they're treated as literal backslashes in the regular expression.

For example, if you include a `\d` in your regular expression to match a digit
character, you will need to write it as `\\d` in your JSON template.

In the following example, the `AllowedPattern` property specifies a regular
expression that matches four consecutive digit characters (`\d{4}`). However, since
the regular expression is defined in a JSON template, the backslash character needs to be
escaped with an additional backslash (`\\d`).

```
{
  "Parameters": {
    "MyParameter": {
      "Type": "String",
      "AllowedPattern": "\\d{4}"
    }
  }
}
```

If you write your CloudFormation template in YAML syntax, you must surround the regular
expression with single quotation marks (''). No additional escaping is required.

```
Parameters:
  MyParameter:
    Type: String
    AllowedPattern: '\d{4}'
```

###### Note

Regular expressions in CloudFormation are only supported for validation purposes in specific
contexts like `AllowedPattern`. They are not supported as pattern matching
operations in CloudFormation intrinsic functions, such as `Fn::Equals`, which
perform exact string comparison only, not pattern matching.
