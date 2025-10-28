# Built-in utilities

The `util` variable contains general utility methods to help you work with
data. Unless otherwise specified, all utilities use the UTF-8 character set.

## Encoding utils

**`util.urlEncode(String)`**

Returns the input string as an
`application/x-www-form-urlencoded` encoded string.

**`util.urlDecode(String)`**

Decodes an `application/x-www-form-urlencoded` encoded
string back to its non-encoded form.

**`util.base64Encode(string) :
 string`**

Encodes the input into a base64-encoded string.

**`util.base64Decode(string) :
 string`**

Decodes the data from a base64-encoded string.

## ID generation utils

**`util.autoId()`**

Returns a 128-bit randomly generated UUID.

**`util.autoUlid()`**

Returns a 128-bit randomly generated ULID (Universally Unique
Lexicographically Sortable Identifier).

**`util.autoKsuid()`**

Returns a 128-bit randomly generated KSUID (K-Sortable Unique
Identifier) base62 encoded as a String with a length of 27.

## Error utils

**`util.error(String, String?, Object?,
 Object?)`**

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

`errorInfo` will **not** be
filtered based on the query selection set.

**`util.appendError(String, String?, Object?,
 Object?)`**

Appends a custom error. This can be used in request or response
mapping templates if the template detects an error with the request or
with the invocation result. Additionally, an `errorType`
field, a `data` field, and an `errorInfo` field can
be specified. Unlike `util.error(String, String?, Object?,
 Object?)`, the template evaluation will not be interrupted, so
that data can be returned to the caller. The `data` value will
be added to the corresponding `error` block inside
`errors` in the GraphQL response.

###### Note

`data` will be filtered based on the query selection
set. The `errorInfo` value will be added to the
corresponding `error` block inside `errors` in
the GraphQL response.

`errorInfo` will **not** be
filtered based on the query selection set.

## Type and pattern matching utils

**`util.matches(String, String) :
 Boolean`**

Returns true if the specified pattern in the first argument matches
the supplied data in the second argument. The pattern must be a regular
expression such as `util.matches("a*b", "aaaaab")`. The
functionality is based on [Pattern](https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html "https://docs.oracle.com/javase/7/docs/api/java/util/regex/Pattern.html"), which you can reference for further
documentation.

**`util.authType()`**

Returns a String describing the multi-auth type being used by a
request, returning back either "IAM Authorization", "User Pool
Authorization", "Open ID Connect Authorization", or "API Key
Authorization".

## Return value behavior

utils

**`util.escapeJavaScript(String)`**

Returns the input string as a JavaScript escaped string.

## Resolver authorization

utils

**`util.unauthorized()`**

Throws `Unauthorized` for the field being resolved. Use
this in request or response mapping templates to determine whether to
allow the caller to resolve the field.
