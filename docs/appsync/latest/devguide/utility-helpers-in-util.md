# Utility helpers in $util

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

The `$util` variable contains general utility methods to help you work with
data. Unless otherwise specified, all utilities use the UTF-8 character set.

## JSON parsing utils

\***\*`$util.parseJson(String) :
 Object`\*\***

Takes "stringified" JSON and returns an object representation of the
result.

\***\*`$util.toJson(Object) : String`\*\***

Takes an object and returns a "stringified" JSON representation of
that object.

## Encoding utils

\***\*`$util.urlEncode(String) :
 String`\*\***

Returns the input string as an
`application/x-www-form-urlencoded` encoded string.

\***\*`$util.urlDecode(String) :
 String`\*\***

Decodes an `application/x-www-form-urlencoded` encoded
string back to its non-encoded form.

\***\*`$util.base64Encode( byte[] ) :
 String`\*\***

Encodes the input into a base64-encoded string.

\***\*`$util.base64Decode(String) :
 byte[]`\*\***

Decodes the data from a base64-encoded string.

## ID generation utils

\***\*`$util.autoId() : String`\*\***

Returns a 128-bit randomly generated UUID.

\***\*`$util.autoUlid() :
 String`\*\***

Returns a 128-bit randomly generated ULID (Universally Unique
Lexicographically Sortable Identifier).

\***\*`$util.autoKsuid() :
 String`\*\***

Returns a 128-bit randomly generated KSUID (K-Sortable Unique
Identifier) base62 encoded as a String with a length of 27.

## Error utils

**`$util.error(String)`**

Throws a custom error. Use this in request or response mapping
templates to detect an error with the request or with the invocation
result.

**`$util.error(String, String)`**

Throws a custom error. Use this in request or response mapping
templates to detect an error with the request or with the invocation
result. You can also specify an `errorType`.

**`$util.error(String, String, Object)`**

Throws a custom error. Use this in request or response mapping
templates to detect an error with the request or with the invocation
result. You can also specify an `errorType` and a
`data` field. The `data` value will be added to
the corresponding `error` block inside `errors` in
the GraphQL response.

###### Note

`data` will be filtered based on the query selection
set.

**`$util.error(String, String, Object, Object)`**

Throws a custom error. This can be used in request or response mapping
templates if the template detects an error with the request or with the
invocation result. Additionally, an `errorType` field, a
`data` field, and an `errorInfo` field can be
specified. The `data` value will be added to the corresponding
`error` block inside `errors` in the GraphQL
response.

###### Note

`data` will be filtered based on the query selection
set. The `errorInfo` value will be added to the
corresponding `error` block inside `errors` in
the GraphQL response.

`errorInfo` will **NOT** be
filtered based on the query selection set.

**`$util.appendError(String)`**

Appends a custom error. This can be used in request or response
mapping templates if the template detects an error with the request or
with the invocation result. Unlike `$util.error(String)`, the
template evaluation will not be interrupted, so that data can be returned
to the caller.

**`$util.appendError(String, String)`**

Appends a custom error. This can be used in request or response
mapping templates if the template detects an error with the request or
with the invocation result. Additionally, an `errorType` can
be specified. Unlike `$util.error(String, String)`, the
template evaluation will not be interrupted, so that data can be returned
to the caller.

**`$util.appendError(String, String, Object)`**

Appends a custom error. This can be used in request or response
mapping templates if the template detects an error with the request or
with the invocation result. Additionally, an `errorType` and a
`data` field can be specified. Unlike
`$util.error(String, String, Object)`, the template
evaluation will not be interrupted, so that data can be returned to the
caller. The `data` value will be added to the corresponding
`error` block inside `errors` in the GraphQL
response.

###### Note

`data` will be filtered based on the query selection
set.

**`$util.appendError(String, String, Object, Object)`**

Appends a custom error. This can be used in request or response
mapping templates if the template detects an error with the request or
with the invocation result. Additionally, an `errorType`
field, a `data` field, and an `errorInfo` field can
be specified. Unlike `$util.error(String, String, Object,
 Object)`, the template evaluation will not be interrupted, so
that data can be returned to the caller. The `data` value will
be added to the corresponding `error` block inside
`errors` in the GraphQL response.

###### Note

`data` will be filtered based on the query selection
set. The `errorInfo` value will be added to the
corresponding `error` block inside `errors` in
the GraphQL response.

`errorInfo` will **NOT** be
filtered based on the query selection set.

## Condition validation utils

**`$util.validate(Boolean, String) : void`**

If the condition is false, throw a CustomTemplateException with the
specified message.

**`$util.validate(Boolean, String, String) : void`**

If the condition is false, throw a CustomTemplateException with the
specified message and error type.

**`$util.validate(Boolean, String, String, Object) : void`**

If the condition is false, throw a CustomTemplateException with the
specified message and error type, as well as data to return in the
response.

## Null behavior utils

**`$util.isNull(Object) : Boolean`**

Returns true if the supplied object is null.

**`$util.isNullOrEmpty(String) : Boolean`**

Returns true if the supplied data is null or an empty string.
Otherwise, returns false.

**`$util.isNullOrBlank(String) : Boolean`**

Returns true if the supplied data is null or a blank string.
Otherwise, returns false.

**`$util.defaultIfNull(Object, Object) : Object`**

Returns the first Object if it is not null. Otherwise, returns second
object as a "default Object".

**`$util.defaultIfNullOrEmpty(String, String) : String`**

Returns the first String if it is not null or empty. Otherwise,
returns second String as a "default String".

**`$util.defaultIfNullOrBlank(String, String) : String`**

Returns the first String if it is not null or blank. Otherwise,
returns second String as a "default String".

## Pattern matching utils

**`$util.typeOf(Object) : String`**

Returns a String describing the type of the Object. Supported type
identifications are: "Null", "Number", "String", "Map", "List",
"Boolean". If a type cannot be identified, the return type is
"Object".

**`$util.matches(String, String) : Boolean`**

Returns true if the specified pattern in the first argument matches
the supplied data in the second argument. The pattern must be a regular
expression such as `$util.matches("a*b", "aaaaab")`. The
functionality is based on [Pattern](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html "https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html"), which you can reference for further
documentation.

**`$util.authType() : String`**

Returns a String describing the multi-auth type being used by a
request, returning back either "IAM Authorization", "User Pool
Authorization", "Open ID Connect Authorization", or "API Key
Authorization".

## Object validation utils

**`$util.isString(Object) : Boolean`**

Returns true if the Object is a String.

**`$util.isNumber(Object) : Boolean`**

Returns true if the Object is a Number.

**`$util.isBoolean(Object) : Boolean`**

Returns true if the Object is a Boolean.

**`$util.isList(Object) : Boolean`**

Returns true if the Object is a List.

**`$util.isMap(Object) : Boolean`**

Returns true if the Object is a Map.

## CloudWatch logging utils

**`$util.log.info(Object) :
 Void`**

Logs the String representation of the provided Object to the requested
log stream when request-level and field-level CloudWatch logging is enabled
with log level `ALL`, `INFO`, or `DEBUG`
on an API.

**`$util.log.info(String, Object...) :
 Void`**

Logs the String representation of the provided Objects to the
requested log stream when request-level and field-level CloudWatch logging is
enabled with log level `ALL` on an API. This utility will
replace all variables indicated by "{}" in the first input format String
with the String representation of the provided Objects in order.

**`$util.log.debug(Object) :
 Void`**

Logs the String representation of the provided Object to the requested
log stream when request-level and field-level CloudWatch logging is enabled
with log level `ALL` or `DEBUG` on an API.

**`$util.log.debug(String, Object...) :
 Void`**

Logs the String representation of the provided Objects to the
requested log stream when field-level CloudWatch logging is enabled with log
level `DEBUG` or log level `ALL` on an API. This
utility will replace all variables indicated by "{}" in the first input
format String with the String representation of the provided Objects in
order.

**`$util.log.error(Object) :
 Void`**

Logs the String representation of the provided Object to the requested
log stream when field-level CloudWatch logging is enabled with **any** log level (`ALL`,
`INFO`, `DEBUG`, etc.) on an API.

**`$util.log.error(String, Object...) :
 Void`**

Logs the String representation of the provided Objects to the
requested log stream when field-level CloudWatch logging is enabled with log
level `ERROR` or log level `ALL` on an API. This
utility will replace all variables indicated by "{}" in the first input
format String with the String representation of the provided Objects in
order.

## Return value behavior utils

\***\*`$util.qr()`** and
`$util.quiet()`\*\*

Runs a VTL statement while suppressing the returned value. This is
useful for running methods without using temporary placeholders, such as
adding items to a map. For example:

```
#set ($myMap = {})
#set($discard = $myMap.put("id", "first value"))
```

Becomes:

```
#set ($myMap = {})
$util.qr($myMap.put("id", "first value"))
```

**`$util.escapeJavaScript(String) : String`**

Returns the input string as a JavaScript escaped
string.

**`$util.urlEncode(String) : String`**

Returns the input string as an
`application/x-www-form-urlencoded` encoded
string.

**`$util.urlDecode(String) : String`**

Decodes an `application/x-www-form-urlencoded`
encoded string back to its non-encoded form.

**`$util.base64Encode( byte[] ) : String`**

Encodes the input into a base64-encoded string.

**`$util.base64Decode(String) : byte[]`**

Decodes the data from a base64-encoded string.

**`$util.parseJson(String) : Object`**

Takes "stringified" JSON and returns an object representation
of the result.

**`$util.toJson(Object) : String`**

Takes an object and returns a "stringified" JSON
representation of that object.

**`$util.autoId() : String`**

Returns a 128-bit randomly generated UUID.

\***\*`$util.autoUlid() :
 String`\*\***

Returns a 128-bit randomly generated ULID (Universally Unique
Lexicographically Sortable Identifier).

\***\*`$util.autoKsuid() :
 String`\*\***

Returns a 128-bit randomly generated KSUID (K-Sortable Unique
Identifier) base62 encoded as a String with a length of 27.

**`$util.unauthorized()`**

Throws `Unauthorized` for the field being
resolved. Use this in request or response mapping templates to
determine whether to allow the caller to resolve the
field.

**`$util.error(String)`**

Throws a custom error. Use this in request or response
mapping templates to detect an error with the request or with
the invocation result.

**`$util.error(String, String)`**

Throws a custom error. Use this in request or response
mapping templates to detect an error with the request or with
the invocation result. You can also specify an
`errorType`.

**`$util.error(String, String, Object)`**

Throws a custom error. Use this in request or response
mapping templates to detect an error with the request or with
the invocation result. You can also specify an
`errorType` and a `data` field. The
`data` value will be added to the corresponding
`error` block inside `errors` in the
GraphQL response. **Note**:
`data` will be filtered based on the query
selection set.

**`$util.error(String, String, Object, Object)`**

Throws a custom error. This can be used in request or
response mapping templates if the template detects an error with
the request or with the invocation result. Additionally, an
`errorType` field, a `data` field, and
a `errorInfo` field can be specified. The
`data` value will be added to the corresponding
`error` block inside `errors` in the
GraphQL response. **Note**:
`data` will be filtered based on the query
selection set. The `errorInfo` value will be added to
the corresponding `error` block inside
`errors` in the GraphQL response. **Note**: `errorInfo` will
**NOT** be filtered based on the
query selection set.

**`$util.appendError(String)`**

Appends a custom error. This can be used in request or
response mapping templates if the template detects an error with
the request or with the invocation result. Unlike
`$util.error(String)`, the template evaluation
will not be interrupted, so that data can be returned to the
caller.

**`$util.appendError(String, String)`**

Appends a custom error. This can be used in request or
response mapping templates if the template detects an error with
the request or with the invocation result. Additionally, an
`errorType` can be specified. Unlike
`$util.error(String, String)`, the template
evaluation will not be interrupted, so that data can be returned
to the caller.

**`$util.appendError(String, String, Object)`**

Appends a custom error. This can be used in request or
response mapping templates if the template detects an error with
the request or with the invocation result. Additionally, an
`errorType` and a `data` field can be
specified. Unlike `$util.error(String, String,
 Object)`, the template evaluation will not be
interrupted, so that data can be returned to the caller. The
`data` value will be added to the corresponding
`error` block inside `errors` in the
GraphQL response. **Note**:
`data` will be filtered based on the query
selection set.

**`$util.appendError(String, String, Object, Object)`**

Appends a custom error. This can be used in request or
response mapping templates if the template detects an error with
the request or with the invocation result. Additionally, an
`errorType` field, a `data` field, and
a `errorInfo` field can be specified. Unlike
`$util.error(String, String, Object, Object)`, the
template evaluation will not be interrupted, so that data can be
returned to the caller. The `data` value will be
added to the corresponding `error` block inside
`errors` in the GraphQL response. **Note**: `data` will be
filtered based on the query selection set. The
`errorInfo` value will be added to the
corresponding `error` block inside
`errors` in the GraphQL response. **Note**: `errorInfo` will
**NOT** be filtered based on the
query selection set.

**`$util.validate(Boolean, String) : void`**

If the condition is false, throw a CustomTemplateException
with the specified message.

**`$util.validate(Boolean, String, String) : void`**

If the condition is false, throw a CustomTemplateException
with the specified message and error type.

**`$util.validate(Boolean, String, String, Object) : void`**

If the condition is false, throw a CustomTemplateException
with the specified message and error type, as well as data to
return in the response.

**`$util.isNull(Object) : Boolean`**

Returns true if the supplied object is null.

**`$util.isNullOrEmpty(String) : Boolean`**

Returns true if the supplied data is null or an empty string.
Otherwise, returns false.

**`$util.isNullOrBlank(String) : Boolean`**

Returns true if the supplied data is null or a blank string.
Otherwise, returns false.

**`$util.defaultIfNull(Object, Object) : Object`**

Returns the first Object if it is not null. Otherwise,
returns second object as a "default Object".

**`$util.defaultIfNullOrEmpty(String, String) : String`**

Returns the first String if it is not null or empty.
Otherwise, returns second String as a "default String".

**`$util.defaultIfNullOrBlank(String, String) : String`**

Returns the first String if it is not null or blank.
Otherwise, returns second String as a "default String".

**`$util.isString(Object) : Boolean`**

Returns true if Object is a String.

**`$util.isNumber(Object) : Boolean`**

Returns true if Object is a Number.

**`$util.isBoolean(Object) : Boolean`**

Returns true if Object is a Boolean.

**`$util.isList(Object) : Boolean`**

Returns true if Object is a List.

**`$util.isMap(Object) : Boolean`**

Returns true if Object is a Map.

**`$util.typeOf(Object) : String`**

Returns a String describing the type of the Object. Supported
type identifications are: "Null", "Number", "String", "Map",
"List", "Boolean". If a type cannot be identified, the return
type is "Object".

**`$util.matches(String, String) : Boolean`**

Returns true if the specified pattern in the first argument
matches the supplied data in the second argument. The pattern
must be a regular expression such as `$util.matches("a*b",
 "aaaaab")`. The functionality is based on [Pattern](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html "https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html"), which you can reference for further
documentation.

**`$util.authType() : String`**

Returns a String describing the multi-auth type being used by
a request, returning back either "IAM Authorization", "User
Pool Authorization", "Open ID Connect Authorization", or "API
Key Authorization".

\***\*`$util.log.info(Object) :
 Void`\*\***

Logs the String representation of the provided Object to the
requested log stream when request-level and field-level CloudWatch
logging is enabled with log level `ALL` on an
API.

\***\*`$util.log.info(String, Object...) :
 Void`\*\***

Logs the String representation of the provided Objects to the
requested log stream when request-level and field-level CloudWatch
logging is enabled with log level `ALL` on an API.
This utility will replace all variables indicated by "{}" in the
first input format String with the String representation of the
provided Objects in order.

\***\*`$util.log.error(Object) :
 Void`\*\***

Logs the String representation of the provided Object to the
requested log stream when field-level CloudWatch logging is enabled
with log level `ERROR` or log level `ALL`
on an API.

\***\*`$util.log.error(String, Object...) :
 Void`\*\***

Logs the String representation of the provided Objects to the
requested log stream when field-level CloudWatch logging is enabled
with log level `ERROR` or log level `ALL`
on an API. This utility will replace all variables indicated by
"{}" in the first input format String with the String
representation of the provided Objects in order.

**`$util.escapeJavaScript(String) : String`**

Returns the input string as a JavaScript escaped string.

## Resolver authorization

**`$util.unauthorized()`**

Throws `Unauthorized` for the field being resolved. Use
this in request or response mapping templates to determine whether to
allow the caller to resolve the field.
