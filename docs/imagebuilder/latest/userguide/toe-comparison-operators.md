# Use comparison operators in

AWSTOE component documents

You can use the following comparison operators with the **[Assert](toe-action-modules.md#action-modules-assertion "toe-action-modules.md#action-modules-assertion")**
action module and with conditional expressions that use the
[if Construct](toe-conditional-constructs.md#toe-conditional-if "toe-conditional-constructs.md#toe-conditional-if"). A comparison
operator can operate on a single value, for example `stringIsEmpty`, or it can
compare a baseline value to a second value (variable value) to determine whether the
conditional expression evaluates to `true` or `false`.

If the comparison operates on two values, the second value can be a chaining variable.

When comparing values of a different type, the following value conversions can occur prior
to the comparison:

- For numeric comparisons, if the variable value is a string, AWSTOE converts the string
  to a number prior to the evaluation. If the conversion is not possible, the comparison returns
  `false`. For example, if the variable value is `"1.0"`, the conversion works,
  but if the variable value is `"a10"` the conversion fails.
- For string comparisons, if the variable value is a number, AWSTOE converts it to a string
  prior to the evaluation.

## Compare strings

The following comparison operators work with strings to compare values, to test for
spaces or an empty string, or to compare an input value to a regex pattern. String
comparisons are not case sensitive, and they don't trim spaces from the beginning or
the end of the string inputs.

###### String comparison operators

- [stringIsEmpty](#stringIsEmpty "#stringIsEmpty")
- [stringIsWhitespace](#stringIsWhitespace "#stringIsWhitespace")
- [stringEquals](#stringEquals "#stringEquals")
- [stringLessThan](#stringLessThan "#stringLessThan")
- [stringLessThanEquals](#stringLessThanEquals "#stringLessThanEquals")
- [stringGreaterThan](#stringGreaterThan "#stringGreaterThan")
- [stringGreaterThanEquals](#stringGreaterThanEquals "#stringGreaterThanEquals")
- [patternMatches](#patternMatches "#patternMatches")

**stringIsEmpty**

The `stringIsEmpty` operator returns `true` if the
specified string doesn't contain any characters. For example:

```
# Evaluates to true
stringIsEmpty: ""

# Evaluates to false
stringIsEmpty: " "

# Evaluates to false
stringIsEmpty: "Hello."
```

**stringIsWhitespace**

Tests if the string specified for `stringIsWhitespace` contains
only spaces. For example:

```
# Evaluates to true
stringIsWhitespace: "   "

# Evaluates to false
stringIsWhitespace: ""

# Evaluates to false
stringIsWhitespace: " Hello?"
```

**stringEquals**

Tests if the string specified for `stringEquals` is an exact
match for the string specified in the `value` parameter.
For example:

```
# Evaluates to true
stringEquals: 'Testing, testing...'
value: 'Testing, testing...'

# Evaluates to false
stringEquals: 'Testing, testing...'
value: 'Hello again.'

# Evaluates to false
stringEquals: 'Testing, testing...'
value: 'TESTING, TESTING....'

# Evaluates to false
stringEquals: 'Testing, testing...'
value: '   Testing, testing...'

# Evaluates to false
stringEquals: 'Testing, testing...'
value: 'Testing, testing...   '
```

**stringLessThan**

Tests if the string specified for `stringLessThan` is less than
the string specified in the `value` parameter. For example:

```
# Evaluates to true
# This comparison operator isn't case sensitive
stringlessThan: 'A'
value: 'a'

# Evaluates to true - 'a' is less than 'b'
stringlessThan: 'b'
value: 'a'

# Evaluates to true
# Numeric strings compare as less than alphabetic strings
stringlessThan: 'a'
value: '0'

# Evaluates to false
stringlessThan: '0'
value: 'a'
```

**stringLessThanEquals**

Tests if the string specified for `stringLessThanEquals` is less
than or equal to the string specified in the `value` parameter.
For example:

```
# Evaluates to true - 'a' is equal to 'a'
stringLessThanEquals: 'a'
value: 'a'

# Evaluates to true - since the comparison isn't case sensitive, 'a' is equal to 'A'
stringLessThanEquals: 'A'
value: 'a'

# Evaluates to true - 'a' is less than 'b'
stringLessThanEquals: 'b'
value: 'a'

# Evaluates to true - '0' is less than 'a'
stringLessThanEquals: 'a'
value: '0'

# Evaluates to false - 'a' is greater than '0'
stringLessThanEquals: '0'
value: 'a'
```

**stringGreaterThan**

Tests if the string specified for `stringGreaterThan` is greater than
the string specified in the `value` parameter. For example:

```
# Evaluates to false - since the comparison isn't case sensitive, 'A' is equal to 'a'
stringGreaterThan: 'a'
value: 'A'

# Evaluates to true - 'b' is greater than 'a'
stringGreaterThan: 'a'
value: 'b'

# Evaluates to true - 'a' is greater than '0'
stringGreaterThan: '0'
value: 'a'

# Evaluates to false - '0' is less than 'a'
stringGreaterThan: 'a'
value: '0'
```

**stringGreaterThanEquals**

Tests if the string specified for `stringGreaterThanEquals` is
greater than or equal to the string specified in the `value` parameter.
For example:

```
# Evaluates to true - 'a' is equal to 'A'
stringGreaterThanEquals: 'A'
value: 'a'

# Evaluates to true - 'b' is greater than 'a'
stringGreaterThanEquals: 'a'
value: 'b'

# Evaluates to true - 'a' is greater than '0'
stringGreaterThanEquals: '0'
value: 'a'

# Evaluates to false - '0' is less than 'a'
stringGreaterThanEquals: 'a'
value: '0'
```

**patternMatches**

Tests if the string specified in the `value` parameter matches
the regex pattern specified for `patternMatches`. The comparison
uses to the [Golang regexp package](https://pkg.go.dev/regexp "https://pkg.go.dev/regexp"),
which conforms to the RE2 syntax. For more information about RE2 rules, see the
[google / re2](https://github.com/google/re2/wiki/Syntax "https://github.com/google/re2/wiki/Syntax") repository in _GitHub_.

The following example shows a pattern match that returns `true`:

```
patternMatches: '^[a-z]+$'
value: 'ThisIsValue'
```

## Compare numbers

The following comparison operators work with numbers. The values provided for these
operators must be one of the following types, according to the YAML specification.
Support for numeric comparisons uses the golang big package comparison operator, for example: [func (\*Float) Cmp](https://pkg.go.dev/math/big#Float.Cmp "https://pkg.go.dev/math/big#Float.Cmp").

- Integer
- Float (based on float64, which supports numbers from -1.7e+308 to +1.7e+308)
- A string that matches the following regex pattern: `^[-+]?([0-9]+[.])?[0-9]+$`

###### Number comparison operators

- [numberEquals](#numberEquals "#numberEquals")
- [numberLessThan](#numberLessThan "#numberLessThan")
- [numberLessThanEquals](#numberLessThanEquals "#numberLessThanEquals")
- [numberGreaterThan](#numberGreaterThan "#numberGreaterThan")
- [numberGreaterThanEquals](#numberGreaterThanEquals "#numberGreaterThanEquals")

**numberEquals**

Tests if the number specified for `numberEquals` is equal to
the number specified in the `value` parameter. All of the following
example comparisons return `true`:

```
# Values provided as a positive number
numberEquals: 1
value: 1

# Comparison value provided as a string
numberEquals: '1'
value: 1

# Value provided as a string
numberEquals: 1
value: '1'

# Values provided as floats
numberEquals: 5.0
value: 5.0

# Values provided as a negative number
numberEquals: -1
value: -1
```

**numberLessThan**

Tests if the number specified for `numberLessThan` is less than
the number specified in the `value` parameter. For example:

```
# Evaluates to true
numberLessThan: 2
value: 1

# Evaluates to true
numberLessThan: 2
value: 1.9

# Evaluates to false
numberLessThan: 2
value: '2'
```

**numberLessThanEquals**

Tests if the number specified for `numberLessThanEquals` is less
than or equal to the number specified in the `value` parameter.
For example:

```
# Evaluates to true
numberLessThanEquals: 2
value: 1

# Evaluates to true
numberLessThanEquals: 2
value: 1.9

# Evaluates to true
numberLessThanEquals: 2
value: '2'

# Evaluates to false
numberLessThanEquals: 2
value: 2.1

```

**numberGreaterThan**

Tests if the number specified for `numberGreaterThan` is greater
than the number specified in the `value` parameter. For example:

```
# Evaluates to true
numberGreaterThan: 1
value: 2

# Evaluates to true
numberGreaterThan: 1
value: 1.1

# Evaluates to false
numberGreaterThan: 1
value: '1'
```

**numberGreaterThanEquals**

Tests if the number specified for `numberGreaterThanEquals` is
greater than or equal to the number specified in the `value` parameter.
For example:

```
# Evaluates to true
numberGreaterThanEquals: 1
value: 2

# Evaluates to true
numberGreaterThanEquals: 1
value: 1.1

# Evaluates to true
numberGreaterThanEquals: 1
value: '1'

# Evaluates to false
numberGreaterThanEquals: 1
value: 0.8
```

## Check files

The following comparison operators check the file hash or check if a file or
folder exists.

###### File and folder operators

- [binaryExists](#binaryExists "#binaryExists")
- [fileExists](#fileExists "#fileExists")
- [folderExists](#folderExists "#folderExists")
- [fileMD5Equals](#fileMD5Equals "#fileMD5Equals")
- [fileSHA1Equals](#fileSHA1Equals "#fileSHA1Equals")
- [fileSHA256Equals](#fileSHA256Equals "#fileSHA256Equals")
- [fileSHA512Equals](#fileSHA512Equals "#fileSHA512Equals")

**binaryExists**

Tests whether an application is available in the current path. For example:

```
binaryExists: '`foo`'
```

###### Note

On Linux and macOS systems, for an application named `foo`,
this works the same as the following bash command:
**type `foo` >/dev/null 2>&1**, where **$? == 0**
indicates a successful comparison.

On Windows systems, for an application named `foo`,
this works the same as the PowerShell command
**& C:\Windows\System32\where.exe /Q `foo`** where
**$LASTEXITCODE = 0** indicates a successful comparison.

**fileExists**

Tests whether a file exists at the specified path. You can provide an
absolute or relative path. If the location you specify exists and is a file,
the comparison evaluates to `true`. For example:

```
fileExists: '`/path/to/file`'
```

###### Note

On Linux and macOS systems, this works the same as the following bash command:
**-d `/path/to/file`**, where **$? == 0**
indicates a successful comparison.

On Windows systems, this works the same as the PowerShell command
**Test-Path -Path '`C:\path\to\file`' -PathType 'Leaf'**.

**folderExists**

Tests whether a folder exists at the specified path. You can provide an
absolute or relative path. If the location you specify exists and is a folder,
the comparison evaluates to `true`. For example:

```
folderExists: '`/path/to/folder`'
```

###### Note

On Linux and macOS systems, this works the same as the following bash command:
**-d `/path/to/folder`**, where **$? == 0**
indicates a successful comparison.

On Windows systems, this works the same as the PowerShell command
**Test-Path -Path '`C:\path\to\folder`' -PathType 'Container'**.

**fileMD5Equals**

Tests whether a file’s MD5 hash equals a specified value. For example:

```
fileMD5Equals: '`<MD5Hash>`'
path: '`/path/to/file`'
```

**fileSHA1Equals**

Tests whether a file’s SHA1 hash equals a specified value. For example:

```
fileSHA1Equals: '`<SHA1Hash>`'
path: '`/path/to/file`'
```

**fileSHA256Equals**

Tests whether a file’s SHA256 hash equals a specified value. For example:

```
fileSHA256Equals: '`<SHA256Hash>`'
path: '`/path/to/file`'
```

**fileSHA512Equals**

Tests whether a file’s SHA512 hash equals a specified value. For example:

```
fileSHA512Equals: '`<SHA512Hash>`'
path: '`/path/to/file`'
```
