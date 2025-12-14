**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Request components in AWS WAF

This section describes the components of the web request that you can specify for
inspection. You specify the request component for match rule statements that
look for patterns inside the web request. These types of statements include
string match, regex match, size constraint, and SQL injection attack statements.
For information on how to use these request component settings, see the
individual rule statements at
[Using match rule statements in AWS WAF](waf-rule-statements-match.md "waf-rule-statements-match.md")

Unless otherwise noted, if a web request doesn't have the request component
that's specified in the rule statement, AWS WAF evaluates the request as not matching the
rule criteria.

###### Note

You specify a single request component for each rule statement that
requires it. To inspect more than one component of a request, create a rule
statement for each component.

The AWS WAF console and API documentation provide guidance for the request component settings in
the following locations:

- **Rule builder** on the console – In the
  **Statement** settings for a regular rule type,
  choose the component that you want to inspect in the
  **Inspect** dialogue under **Request
  components**.
- **API statement contents** –
  `FieldToMatch`
  The rest of this section describes the options for the part of the web request to inspect.

###### Topics

- [HTTP
  method](#waf-rule-statement-request-component-http-method "#waf-rule-statement-request-component-http-method")
- [Single
  header](#waf-rule-statement-request-component-single-header "#waf-rule-statement-request-component-single-header")
- [All headers](#waf-rule-statement-request-component-headers "#waf-rule-statement-request-component-headers")
- [Header order](#waf-rule-statement-request-component-header-order "#waf-rule-statement-request-component-header-order")
- [Cookies](#waf-rule-statement-request-component-cookies "#waf-rule-statement-request-component-cookies")
- [URI fragment](#waf-rule-statement-request-component-uri-fragment "#waf-rule-statement-request-component-uri-fragment")
- [URI
  path](#waf-rule-statement-request-component-uri-path "#waf-rule-statement-request-component-uri-path")
- [JA3 fingerprint](#waf-rule-statement-request-component-ja3-fingerprint "#waf-rule-statement-request-component-ja3-fingerprint")
- [JA4 fingerprint](#waf-rule-statement-request-component-ja4-fingerprint "#waf-rule-statement-request-component-ja4-fingerprint")
- [Query
  string](#waf-rule-statement-request-component-query-string "#waf-rule-statement-request-component-query-string")
- [Single query parameter](#waf-rule-statement-request-component-single-query-param "#waf-rule-statement-request-component-single-query-param")
- [All query parameters](#waf-rule-statement-request-component-all-query-params "#waf-rule-statement-request-component-all-query-params")
- [Body](#waf-rule-statement-request-component-body "#waf-rule-statement-request-component-body")
- [JSON body](#waf-rule-statement-request-component-json-body "#waf-rule-statement-request-component-json-body")

## HTTP

method

Inspects the HTTP method for the request. The HTTP method indicates the
type of operation that the web request is asking your protected resource to
perform, such as `POST` or `GET`.

## Single

header

Inspects a single named header in the request.

For this option, you specify the header name, for
example, `User-Agent` or `Referer`. The string match
for the name is not case sensitive.

## All headers

Inspects all of the request headers, including cookies. You can apply a filter to inspect
a subset of all headers.

For this option, you provide the following specifications:

- **Match patterns** – The filter to use to obtain a subset of
  headers for inspection. AWS WAF looks for these patterns in the
  headers keys.

The match patterns setting can be one of the following:

    + **All** –
     Match all keys. Evaluate the rule inspection criteria for all headers.
    + **Excluded headers** – Inspect only the headers whose keys
     don't match any of the strings that you specify here. The
     string match for a key is not case sensitive.
    + **Included headers** – Inspect only the headers that have a
     key that matches one of the strings that you specify here.
     The string match for a key is not case sensitive.

- **Match scope** – The
  parts of the headers that AWS WAF should inspect with the rule inspection criteria.
  You can specify **Keys**,
  **Values**, or **All**
  to inspect both keys and values for a match.

**All** does not require a match to be found in the keys
and a match to be found in the values. It requires a match to be found in the keys
or the values or both. To require a match in the keys and in the values, use a logical `AND` statement
to combine two match rules, one
that inspects the keys and another that inspects the values.

- **Oversize handling** – How AWS WAF should handle
  requests that have header data that is larger than AWS WAF can
  inspect. AWS WAF can inspect at most the first 8 KB (8,192 bytes) of the request headers and at most the first 200 headers. The content is available for inspection by AWS WAF up to the first limit reached. You can choose to continue the inspection, or to
  skip inspection and mark the request as matching or not matching the rule.
  For more information about handling oversize content, see [Oversize web request components
  in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

## Header order

Inspect a string containing the list of the request's header names, ordered as they
appear in the web request that AWS WAF receives for inspection. AWS WAF
generates the string and then uses that as the field to match component in
its inspection. AWS WAF separates the header names in the string with colons
and with no added spaces, for example `host:user-agent:accept:authorization:referer`.

For this option, you provide the following specifications:

- **Oversize handling** – How AWS WAF should handle
  requests that have header data that is more numerous or larger than AWS WAF can
  inspect. AWS WAF can inspect at most the first 8 KB (8,192 bytes) of the request headers and at most the first 200 headers. The content is available for inspection by AWS WAF up to the first limit reached. You can choose to continue inspecting the headers that are available, or to
  skip inspection and mark the request as matching or not matching the rule.
  For more information about handling oversize content, see [Oversize web request components
  in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

## Cookies

Inspects all of the request cookies. You can apply a filter to inspect a subset of all
cookies.

For this option, you provide the following specifications:

- **Match patterns** –
  The filter to use to obtain a subset of cookies for inspection.
  AWS WAF looks for these patterns in the cookie keys.

The match patterns setting can be one of the following:

    + **All** –
     Match all keys. Evaluate the rule inspection criteria for all cookies.
    + **Excluded cookies** – Inspect only the cookies whose keys
     don't match any of the strings that you specify here.
     The string match for a key is case sensitive and must be exact.
    + **Included cookies** – Inspect only the cookies that have a
     key that matches one of the strings that you specify
     here. The string match for a key is case sensitive and must be exact.

- **Match scope** – The
  parts of the cookies that AWS WAF should inspect with the rule inspection criteria.
  You can specify **Keys**,
  **Values**, or **All**
  for both keys and values.

**All** does not require a match to be found in the keys
and a match to be found in the values. It requires a match to be found in the keys
or the values or both. To require a match in the keys and in the values, use a logical `AND` statement
to combine two match rules, one
that inspects the keys and another that inspects the values.

- **Oversize handling** – How AWS WAF should handle
  requests that have cookie data that is larger than AWS WAF can
  inspect. AWS WAF can inspect at most the first 8 KB (8,192 bytes) of the request cookies and at most the first 200 cookies. The content is available for inspection by AWS WAF up to the first limit reached. You can choose to continue the inspection, or to
  skip inspection and mark the request as matching or not matching the rule.
  For more information about handling oversize content, see [Oversize web request components
  in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

## URI fragment

###### Note

Uri Fragment inspection is available only for CloudFront distributions and
Application Load Balancers.

Inspects the part of a URL that follows the "#" symbol, providing additional information about the resource, for example, #section2. For information, see
[Uniform Resource
Identifier (URI): Generic Syntax](https://tools.ietf.org/html/rfc3986#section-3 "https://tools.ietf.org/html/rfc3986#section-3").

If you don't use a text transformation with this option, AWS WAF doesn't
normalize the URI fragment and inspects it exactly as it receives it from the client
in the request. For information about text transformations, see [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").

###### Rule statement requirements

You must provide a fallback behavior for this rule statement. The fallback behavior is the match status that you want AWS WAF to assign to the web request if URI
is missing the fragment or associated service is not Application Load Balancer or CloudFront. If you choose to match, AWS WAF treats the request as matching the rule statement and applies the rule action to the request.
If you choose to not match, AWS WAF treats the request as not matching the rule statement.

## URI

path

Inspects the part of a URL that identifies a resource, for example,
`/images/daily-ad.jpg`. For information, see [Uniform Resource
Identifier (URI): Generic Syntax](https://tools.ietf.org/html/rfc3986#section-3 "https://tools.ietf.org/html/rfc3986#section-3").

If you don't use a text transformation with this option, AWS WAF doesn't
normalize the URI and inspects it exactly as it receives it from the client
in the request. For information about text transformations, see [Using text transformations in AWS WAF](waf-rule-statement-transformation.md "waf-rule-statement-transformation.md").

## JA3 fingerprint

Inspects the request's JA3 fingerprint.

###### Note

JA3 fingerprint inspection is available only for Amazon CloudFront distributions and Application Load Balancers.

The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an
incoming request. This fingerprint serves as a unique identifier for the
client's TLS configuration. AWS WAF calculates and logs this fingerprint for each
request that has enough TLS Client Hello information for the calculation. Almost
all web requests include this information.

###### How to get the JA3 fingerprint for a client

You can obtain the JA3 fingerprint for a client's requests from the protection pack (web ACL) logs.
If AWS WAF is able to calculate the fingerprint, it includes it in the logs.
For information about the logging fields, see [Log fields for protection pack (web ACL) traffic](logging-fields.md "logging-fields.md").

###### Rule statement requirements

You can inspect the JA3 fingerprint only inside a string match statement
that's set to exactly match the
string that you provide. Provide
the JA3 fingerprint string from the logs in your string match statement
specification, to match with any future requests that have the same TLS configuration. For information about the string match statement,
see [String match rule
statement](waf-rule-statement-type-string-match.md "waf-rule-statement-type-string-match.md").

You must provide a fallback behavior for this rule statement. The fallback behavior is
the match status that you want AWS WAF to assign to the web request if AWS WAF
is unable to calculate the JA3 fingerprint. If you choose to match, AWS WAF
treats the request as matching the rule statement and applies the rule
action to the request. If you choose to not match, AWS WAF treats the request
as not matching the rule statement.

To use this match option, you must log your protection pack (web ACL) traffic. For information, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").

## JA4 fingerprint

Inspects the request's JA4 fingerprint.

###### Note

JA4 fingerprint inspection is available only for Amazon CloudFront distributions and Application Load Balancers.

The JA4 fingerprint is a 36-character hash derived from the TLS Client Hello of an
incoming request. This fingerprint serves as a unique identifier for the
client's TLS configuration. JA4 fingerprinting is an extension of the JA3 fingerprinting
that can result in fewer unique fingerprints for some browsers.
AWS WAF calculates and logs this fingerprint for each
request that has enough TLS Client Hello information for the calculation. Almost
all web requests include this information.

###### How to get the JA4 fingerprint for a client

You can obtain the JA4 fingerprint for a client's requests from the protection pack (web ACL) logs.
If AWS WAF is able to calculate the fingerprint, it includes it in the logs.
For information about the logging fields, see [Log fields for protection pack (web ACL) traffic](logging-fields.md "logging-fields.md").

###### Rule statement requirements

You can inspect the JA4 fingerprint only inside a string match statement
that's set to exactly match the
string that you provide. Provide
the JA4 fingerprint string from the logs in your string match statement
specification, to match with any future requests that have the same TLS configuration. For information about the string match statement,
see [String match rule
statement](waf-rule-statement-type-string-match.md "waf-rule-statement-type-string-match.md").

You must provide a fallback behavior for this rule statement. The fallback behavior is
the match status that you want AWS WAF to assign to the web request if AWS WAF
is unable to calculate the JA4 fingerprint. If you choose to match, AWS WAF
treats the request as matching the rule statement and applies the rule
action to the request. If you choose to not match, AWS WAF treats the request
as not matching the rule statement.

To use this match option, you must log your protection pack (web ACL) traffic. For information, see [Logging AWS WAF protection pack (web ACL) traffic](logging.md "logging.md").

## Query

string

Inspects the part of the URL that appears after a `?`
character, if any.

###### Note

For cross-site scripting match statements, we recommend that you
choose **All query parameters** instead of
**Query string**. Choosing **All query
parameters** adds 10 WCUs to the base cost.

## Single query parameter

Inspects a single query parameter that you have defined as part of the
query string. AWS WAF inspects the value of the parameter that you specify.

For this option, you also specify a **Query argument**.
For example, if the URL is
`www.xyz.com?UserName=abc&SalesRegion=seattle`, you can
specify `UserName` or `SalesRegion` for the query
argument. The maximum length for the name of the argument is 30 characters.
The name is not case sensitive, so if you specify `UserName`,
AWS WAF matches all variations of `UserName`, including
`username` and `UsERName`.

If the query string contains more than one instance of the query argument
that you've specified, AWS WAF inspects all the values for a match, using
OR logic. For example, in the URL
`www.xyz.com?SalesRegion=boston&SalesRegion=seattle`,
AWS WAF evaluates the name that you've specified against `boston`
and `seattle`. If either is a match, the inspection is a
match.

## All query parameters

Inspects all query parameters in the request. This is similar to the single query
parameter component choice, but AWS WAF inspects the values of all arguments
within the query string. For example, if the URL is
`www.xyz.com?UserName=abc&SalesRegion=seattle`, AWS WAF
triggers a match if either the value of `UserName` or
`SalesRegion` match the inspection criteria.

Choosing this option adds 10 WCUs to the base cost.

## Body

Inspects the request body, evaluated as plain text. You can also evaluate
the body as JSON using the JSON content type.

The request body is the part of the request that immediately follows the
request headers. It contains any additional data that is needed for the web
request, for example, data from a form.

- In the console, you select this under the
  **Request option** choice
  **Body**, by selecting the
  **Content type** choice **Plain
  text**.
- In the API, in the rule's `FieldToMatch`
  specification, you specify `Body` to inspect the
  request body as plain text.

For Application Load Balancer and AWS AppSync, AWS WAF can inspect the first 8 KB of the body of a request. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, by default, AWS WAF can inspect the first 16 KB, and
you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. For more information, see
[Considerations for managing body inspection in AWS WAF](web-acl-setting-body-inspection-limit.md "web-acl-setting-body-inspection-limit.md").

You must specify oversize handling for this component type. Oversize handling defines how
AWS WAF handles requests that have body data that is larger than AWS WAF can
inspect. You can choose to continue the inspection, or to skip inspection
and mark the request as matching or not matching the rule. For more
information about handling oversize content, see [Oversize web request components
in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

You can also evaluate the body as parsed JSON. For information
about this, see the section that follows.

## JSON body

Inspects the request body, evaluated as JSON. You can also evaluate the
body as plain text.

The request body is the part of the request that immediately follows the
request headers. It contains any additional data that is needed for the web
request, for example, data from a form.

- In the console, you select this under the
  **Request option** choice
  **Body**, by selecting the
  **Content type** choice
  **JSON**.
- In the API, in the rule's `FieldToMatch`
  specification, you specify `JsonBody`.

For Application Load Balancer and AWS AppSync, AWS WAF can inspect the first 8 KB of the body of a request. For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, by default, AWS WAF can inspect the first 16 KB, and
you can increase the limit up to 64 KB in your protection pack (web ACL) configuration. For more information, see
[Considerations for managing body inspection in AWS WAF](web-acl-setting-body-inspection-limit.md "web-acl-setting-body-inspection-limit.md").

You must specify oversize handling for this component type. Oversize
handling defines how AWS WAF handles requests that have body data that is
larger than AWS WAF can inspect. You can choose to continue the inspection, or
to skip inspection and mark the request as matching or not matching the
rule. For more information about handling oversize content, see [Oversize web request components
in AWS WAF](waf-oversize-request-components.md "waf-oversize-request-components.md").

Choosing this option doubles the match statement's base cost WCUs. For
example, if the match statement base cost is 5 WCUs without JSON parsing, using
JSON parsing doubles the cost to 10 WCUs.

For this option, you provide additional specifications, as described in the following section.

###### How AWS WAF handles JSON body inspection

When AWS WAF inspects the web request body as JSON, it performs steps
to parse the body and extract the JSON elements for inspection. AWS WAF performs these steps in accordance with
your configuration choices.

The following lists the steps that AWS WAF performs.

1. **Parse the body contents** – AWS WAF parses the contents of the web request body in order to extract the JSON elements for inspection. AWS WAF does its best to parse the entire contents of the body, but
   parsing can fail for a variety of error states in the contents. Examples include
   invalid characters, duplicate keys, truncation, and content whose
   root node isn't an object or an array.

The option **Body parsing fallback behavior** determines what AWS WAF does if it fails to completely parse the JSON body:

    * **None (default behavior)** - AWS WAF evaluates
     the content only up to the point where it encountered a parsing
     error.
    * **Evaluate as string** - Inspect the body as
     plain text. AWS WAF applies the text transformations and
     inspection criteria that you defined for the JSON inspection to
     the body text string.
    * **Match** - Treat the web request as matching
     the rule statement. AWS WAF applies the rule action to the
     request.
    * **No match** - Treat the web request as not
     matching the rule statement.

###### Note

This fallback behavior only triggers when AWS WAF encounters an error while parsing the JSON string.

###### Parsing doesn't fully validate the JSON

AWS WAF parsing doesn't fully validate the input JSON string, so parsing can succeed even for invalid JSON.

For example, AWS WAF parses the following invalid JSON without error:

    * Missing comma:
     `{"key1":"value1""key2":"value2"}`
    * Missing colon:
     `{"key1":"value1","key2""value2"}`
    * Extra colons:
     `{"key1"::"value1","key2""value2"}`

For cases such as these where the parsing succeeds but the result isn't completely
valid JSON, the outcome of the subsequent steps in the evaluation can vary. The extraction might miss
some elements, or the rule evaluation might have unexpected results. We recommend that you
validate the JSON that you receive in your application and handle invalid JSON as needed. 2. **Extract the JSON elements** – AWS WAF identifies the subset of JSON elements to inspect according
to your settings:

    * The option **JSON match scope** specifies the types
     of elements in the JSON that AWS WAF should inspect.


    You can specify
     **Keys**, **Values**, or
     **All** for both keys and values.


    **All** does not require a match to be found in the keys
     and a match to be found in the values. It requires a match to be found in the keys
     or the values or both. To require a match in the keys and in the values, use a logical `AND` statement
     to combine two match rules, one
     that inspects the keys and another that inspects the values.
    * The option **Content to inspect** specifies how to filter the element set
     to the subset that you want AWS WAF to inspect.


    You must specify one of the following:




    	+ **Full JSON content** - Evaluate all elements.
    	+ **Only included elements** - Evaluate only
    	 elements whose paths match the JSON Pointer criteria that
    	 you provide. Don't use this option to indicate *all* paths in the JSON.
    	 Instead, use **Full JSON content**.


    	For information about JSON Pointer syntax, see
    	 the Internet Engineering Task Force (IETF) documentation [JavaScript Object
    	 Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901 "https://tools.ietf.org/html/rfc6901").


    	For example, in the console, you can provide the following:



    	```
    	/dogs/0/name
    	/dogs/1/name
    	```

    	In the API or CLI, you can provide the following:



    	```
    	"IncludedPaths": ["/dogs/0/name", "/dogs/1/name"]
    	```

For example, say that the **Content to inspect** setting is **Only included elements**, and the included elements setting is `/a/b`.

For the following example JSON body:

```
{
  "a":{
    "c":"d",
    "b":{
      "e":{
        "f":"g"
      }
    }
  }
}
```

The element sets that AWS WAF would inspect for each **JSON match scope** setting are listed below. Note that the key `b`, which is part of the included elements path, isn't evaluated.

    * **All**: `e`, `f,` and `g`.
    * **Keys**: `e` and `f`.
    * **Values**: `g`.

3. **Inspect the JSON element set** – AWS WAF applies any
   text transformations that you've specified to the extracted JSON elements and
   then matches the resulting element set against the rule statement's
   match criteria. This is the same transformation and evaluation behavior as for other
   web request components. If any of the extracted JSON elements match, the web request is a match for the rule.
