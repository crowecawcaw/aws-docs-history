

# Helper methods for network calls

This section applies if you send an HTTP request to an origin from inside your CloudFront Functions code. You can make network calls on *viewer request* or *viewer response* CloudFront Functions. CloudFront Functions has a module that provides helper methods to make network calls.

To use this module, create a CloudFront function using JavaScript runtime 2.0 and include the following statement in the first line of the function code:

```
import cf from "cloudfront";
```

For more information, see [JavaScript runtime 2.0 features for CloudFront Functions](functions-javascript-runtime-20.md).

The destination of the network call must be an origin that is already configured on the same distribution. You can't pass a URL with a host name. You must pass a path and the ID of the origin. In the CloudFront console this is the **Name** field on the origin, which is the same value that the CloudFront API and AWS CloudFormation call the origin `Id`. For more information, see [Origin settings](DownloadDistValuesOrigin.md).

Sending the call through an origin takes advantage of CloudFront's origin handling capabilities. You don't have to reimplement any of the following in your function code:
+ [Origin access control (OAC)](private-content-restricting-access-to-origin.md) signs the request with SigV4. You can call a private Amazon S3 bucket, a Lambda function URL, or another AWS origin without putting credentials in your function code.
+ With [VPC origins](private-content-vpc-origins.md), you can call a service in a private subnet, so the destination never needs a public endpoint.
+ Connection reuse means CloudFront usually already holds a warm connection to the origin, so the call avoids TCP and TLS setup.
+ [Custom origin headers](add-origin-custom-headers.md) configured on the origin are sent on the call, so shared secrets and routing headers stay in your distribution configuration rather than in function code.
+ [Origin mutual TLS (mTLS)](origin-mtls-authentication.md) configured on the origin applies to the call. CloudFront presents the origin's client certificate, so your function doesn't handle certificates or private keys.

The [response timeout](DownloadDistValuesOrigin.md#DownloadDistValuesOriginResponseTimeout) is the one origin setting that does not carry over. A network call times out after 1 second even when the origin is configured with a longer response timeout.

**Note**  
Distributions on the free pricing plan don't support network calls. For more information, see [CloudFront flat-rate pricing plans](flat-rate-pricing-plan.md).

**Note**  
Network calls are not supported when you test a function with the `TestFunction` API or the **Test** tab in the CloudFront console. In a test, `cf.fetch()` and `cf.beacon()` throw a `TypeError` (`"cloudfront.fetch" is not available in test invocations`). If your function does not catch the error, the test fails. Wrap the call in `try` and `catch` so the rest of the function can be tested.

**Important**  
A function can make one network call per invocation. Both `fetch()` and `beacon()` count toward this one network call. A second network call throws an error.

**Topics**
+ [Choose between a network call and CloudFront KeyValueStore](#network-calls-or-kvs)
+ [`fetch()` method](#network-calls-fetch-method)
+ [`beacon()` method](#network-calls-beacon-method)
+ [How CloudFront builds the request](#network-calls-request)
+ [Limitations](#network-calls-limitations)

## Choose between a network call and CloudFront KeyValueStore
<a name="network-calls-or-kvs"></a>

You can read data inside a function by using either a network call or [Amazon CloudFront KeyValueStore](kvs-with-functions.md). Your choice depends on how often the data changes and how current the answer needs to be.

A network call is most useful in the following situations:
+ When the data changes between requests and you need a current answer at request time, such as whether a token has been revoked or which segment a viewer belongs to.
+ When the dataset is too large to fit in a key value store. A key value store has a maximum total size, so a large dataset such as a full user table or a product catalog has to stay in the service that holds it.

CloudFront KeyValueStore is most useful in the following situations:
+ When the data is static or changes infrequently, such as redirect maps, lookup tables, or feature flags that change daily. CloudFront KeyValueStore reads at the edge with no external call, which gives better performance at lower cost.
+ When you need more than one lookup for a single request. A function can make only one network call per invocation, but it can read from CloudFront KeyValueStore repeatedly.

A function can use both. You might read an experiment configuration from CloudFront KeyValueStore to decide which test is active, then make a network call to assign the viewer a variant.

For more information about CloudFront KeyValueStore, see [Helper methods for key value stores](functions-custom-methods.md).

## `fetch()` method
<a name="network-calls-fetch-method"></a>

Use the `fetch()` method to send a request to an origin and read the response. The method returns a promise, so it must be used with `await` inside an `async` function.

**Request**

```
cf.fetch({{path}}, {{options}})
```

**Important**  
Option names are case sensitive, and unknown options are ignored. For example, `Method: 'POST'` is ignored and the request is sent as `GET`, as with standard `fetch()`. If the call also has a `body`, it throws a `TypeError`, because a body is not allowed with `GET`.

The parameters can contain the following:

`path` (required)  
The URI path, and optionally a query string, of the request. For example, `/v1/authorize?scope=read`. The path must start with `/`. CloudFront sends the request to the origin named in `options.originId` and appends the path to the origin's domain name. If the origin has an [origin path](DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath) configured, the path is appended after the origin path.

`options` (required)  
The options can contain the following:    
`originId` (required)  
The ID of the origin to send the request to. Must exactly match the ID of an origin on the same distribution. In the CloudFront console, this is the **Name** field on the origin.  
`method` (optional)  
The HTTP method. One of `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, or `OPTIONS`. If this is not provided, `GET` is used.  
The value must be upper case. Unlike standard `fetch()`, the method is not normalized, so a value such as `'post'` throws a `TypeError`.  
`headers` (optional)  
Request headers as a plain object. Each property name is a header name and each value is a string, for example `{ 'content-type': 'application/json' }`.  
This format is not the same as `event.request.headers`. In the event structure, headers use the shape `{ 'content-type': { value: 'application/json' } }`. Copying the event shape into the options throws an error.  
For the headers that you can't set, see [How CloudFront builds the request](#network-calls-request).  
`body` (optional)  
The request body. Can be a string, an `ArrayBuffer`, or an `ArrayBufferView` such as a `Uint8Array`. To send JSON, use `JSON.stringify()`.  
A body is not allowed with `GET` or `HEAD`, including when `method` is not provided and the default `GET` is used. A call with a body and one of these methods throws a `TypeError` (`options.body is not allowed with GET or HEAD`).  
`includeBody` (optional)  
Whether CloudFront reads the response body and makes it available to your function. If this is not provided, `false` is used. Set it to `true` when you need the body.  
Without `includeBody: true`, every body accessor reads empty: `text()` resolves to `""`, `json()` resolves to `null`, and `bytes()` and `arrayBuffer()` resolve to empty values. Nothing is consumed, so `bodyUsed` stays `false`.

**Response**

The method returns a promise that resolves to a `Response` object. The object can contain the following:

`status`  
The HTTP status code from the origin as a number.

`ok`  
`true` if `status` is 200 to 299, otherwise `false`.

`headers`  
A read-only property that holds the response headers as a [Headers](https://developer.mozilla.org/en-US/docs/Web/API/Headers) object. It supports the `get()`, `has()`, `getSetCookie()`, `forEach()`, `keys()`, `values()`, and `entries()` methods, and you can iterate over it.  
Header names are case insensitive in `get()` and `has()`. `get()` returns `null` when the header is not present. `getSetCookie()` returns an array of every `Set-Cookie` value.  

```javascript
const type = response.headers.get('content-type');
const cookies = response.headers.getSetCookie();
```

`text()`  
A promise that resolves to the body decoded as UTF-8 text. Invalid byte sequences are replaced.

`json()`  
A promise that resolves to the body parsed as JSON. Rejects with `SyntaxError` if the body is not valid JSON.

`bytes()`  
A promise that resolves to the raw body bytes as a `Uint8Array`. Buffer methods such as `toString('base64')` work on the result.

`arrayBuffer()`  
A promise that resolves to the raw body bytes as an `ArrayBuffer`.

`bodyUsed`  
`true` once the body has been read.

**Important**  
You can read the body only once. After `text()`, `json()`, `bytes()`, or `arrayBuffer()`, any further read rejects with `TypeError: body already read`. Use `bodyUsed` to check whether it has been read. If you need the body more than once, keep the first result in a variable.

A network call response carries its own `x-amz-cf-id`, and it is not the same as the one on the viewer request that triggered your function. They are two separate requests with two separate identifiers. If you are investigating the network call, the identifier from the network call response is the one that matters. You can read it with `response.headers.get('x-amz-cf-id')`.

### Error handling
<a name="network-calls-fetch-errors"></a>

Wrap every `await cf.fetch()` in a `try` and `catch` block. Then decide whether your function should fail open and let the request through, or fail closed and block it. If an error is not caught, the function fails and CloudFront returns HTTP 503 to the viewer. This is the same as any other unhandled function error.

Invalid arguments reject the promise that `fetch()` returns, so an `await` inside a `try` and `catch` block handles both argument errors and errors from the call itself.

The method can throw the following errors:

`TypeError`  
The call is invalid or the origin couldn't be reached. This could be from a bad argument, a disallowed header, a request or response that is too large, an unknown origin ID, or a distribution that does not support network calls.  
It also covers an origin that CloudFront could not reach or complete the call with: a DNS failure, a connection failure, a TLS failure, origin response headers that are too large for CloudFront, or the origin closing the connection. The message names the reason, for example `The request could not be completed due to OriginDnsError`. Origins that resolve to loopback or reserved IP addresses are refused in the same way, with `OriginDnsError`.

`TimeoutError`  
The origin did not return a complete response within 1 second. The limit applies to the whole call, including connection setup and reading the body.

`InternalError`  
The call failed inside CloudFront.

`SyntaxError`  
Thrown by `response.json()` when the body is not valid JSON. Check what your origin returns.

**Note**  
A TLS failure to a distant origin, or an origin on a private IP address, can surface as a `TimeoutError` rather than an origin error, because the 1 second limit is reached first. To call a service in a private network, use [VPC origins](private-content-vpc-origins.md).

**Warning**  
Only one network call is allowed per invocation, so promise combinators can't be used to make more than one. Passing two `cf.fetch()` calls to `Promise.all()` throws an error. For more information about promise combinators and function memory, see [Use async and await](async-await-syntax.md).

**Example: Authorization check that fails closed**  
This function only lets the request through if the authorization service approves it. If the service can't be reached, the request is blocked.  
Replace `/v1/authorize` with the path on your origin, and `auth-service` with the ID of your origin.  
The following JavaScript example sends the viewer's token to an authorization service:  

```javascript
import cf from 'cloudfront';

async function handler(event) {
    const request = event.request;
    const auth = request.headers['authorization'];

    if (!auth) {
        return { statusCode: 401, statusDescription: 'Unauthorized' };
    }

    try {
        const response = await cf.fetch('/v1/authorize', {
            originId: 'auth-service',
            method: 'POST',
            headers: { 'content-type': 'application/json' },
            body: JSON.stringify({ token: auth.value, uri: request.uri }),
            includeBody: true,
        });

        if (!response.ok) {
            console.log('authorize returned ' + response.status);
            return { statusCode: 403, statusDescription: 'Forbidden' };
        }

        const result = await response.json();
        request.headers['x-user-id'] = { value: result.userId };
        return request;
    } catch (e) {
        console.log('Authorization check failed: ' + e.name + ': ' + e.message);
        return { statusCode: 503, statusDescription: 'Service Unavailable' };
    }
}
```

**Example: Read dynamic configuration from Amazon S3**  
This function reads a configuration object from an Amazon S3 origin and uses it to tag the request. The `method` option is omitted because `GET` is the default. If the Amazon S3 bucket is private and origin access control (OAC) is set up on the origin, CloudFront signs the request to the bucket. This function fails open, because a missing configuration should not block the viewer.  
Replace `/config/experiments.json` with the path of your object, and `config-bucket` with the ID of your origin.  
The following JavaScript example reads the configuration object:  

```javascript
import cf from 'cloudfront';

async function handler(event) {
    const request = event.request;

    try {
        const response = await cf.fetch('/config/experiments.json', {
            originId: 'config-bucket',
            includeBody: true,
        });

        if (response.ok) {
            const config = await response.json();
            request.headers['x-experiment'] = { value: config.activeExperiment };
        }
    } catch (e) {
        console.log('Config lookup failed: ' + e.name);
    }

    return request;
}
```

## `beacon()` method
<a name="network-calls-beacon-method"></a>

Use the `beacon()` method to send a request to an origin without waiting for the response. Use it for analytics events, audit records, and anything else where the viewer should not wait on delivery. A beacon counts against the network call quota. Each invocation can make one network call in total, using either `fetch()` or `beacon()`, not one of each. Call `beacon()` inside the handler. It doesn't work from global scope.

**Important**  
A beacon is best effort. Don't use it for anything that must succeed. Argument errors throw immediately and can be caught in a `try` and `catch` block, but failures that happen after the function has moved on are not surfaced to your function. Setting `logDeliveryErrors` to `true` is the only way to see those errors.

**Request**

```
cf.beacon({{path}}, {{options}})
```

The parameters can contain the following:

`path` (required)  
The URI path, and optionally a query string, of the request. For example, `/v1/events?source=edge`. The path must start with `/`. CloudFront sends the request to the origin named in `options.originId` and appends the path to the origin's domain name. If the origin has an [origin path](DownloadDistValuesOrigin.md#DownloadDistValuesOriginPath) configured, the path is appended after the origin path.

`options` (required)  
The options can contain the following:    
`originId` (required)  
The ID of the origin to send the request to. Must exactly match the ID of an origin on the same distribution. In the CloudFront console, this is the **Name** field on the origin.  
`method` (optional)  
The HTTP method. One of `GET`, `HEAD`, `POST`, `PUT`, `PATCH`, `DELETE`, or `OPTIONS`. Must be upper case. If this is not provided, `GET` is used.  
`headers` (optional)  
Request headers as a plain object. Each property name is a header name and each value is a string, for example `{ 'content-type': 'application/json' }`.  
This format is not the same as `event.request.headers`. In the event structure, headers use the shape `{ 'content-type': { value: 'application/json' } }`. Copying the event shape into the options throws an error.  
`body` (optional)  
The request body. Can be a string, an `ArrayBuffer`, or an `ArrayBufferView` such as a `Uint8Array`. To send JSON, use `JSON.stringify()`. A body is not allowed with `GET` or `HEAD`, including the default `GET`, and throws a `TypeError`.  
`logDeliveryErrors` (optional)  
Whether delivery failures are written to CloudWatch Logs. If this is not provided, `false` is used. Set it to `true` to see beacons that fail after your function has returned. The errors go to the same log group as `console.log()` messages from the function. For more information, see [CloudFront Functions logs](edge-functions-logs.md#cloudfront-function-logs).  
A beacon counts as delivered when the origin returns a 2xx or 3xx status. Any other origin status is logged as `"cloudfront.beacon": origin returned {{status}}`.

**Note**  
The `includeBody` option of the `fetch()` method is not supported, because there is no response to read. Passing this option throws a `TypeError`.

**Response**

The method returns `undefined` immediately and your function continues.

**Example: Send an analytics event**  
The handler is not `async`, because there is nothing to await.  
The following JavaScript example sends an event without waiting for a response:  

```javascript
import cf from 'cloudfront';

function handler(event) {
    const request = event.request;

    cf.beacon('/events', {
        originId: 'analytics-service',
        method: 'POST',
        headers: { 'content-type': 'application/json' },
        body: JSON.stringify({ uri: request.uri, viewerIp: event.viewer.ip }),
        logDeliveryErrors: true,
    });

    return request;
}
```

## How CloudFront builds the request
<a name="network-calls-request"></a>

CloudFront constructs each network call from scratch. Except for the proxy headers listed below, it does not copy the viewer's headers, cookies, or query string onto the request. If your origin needs something from the viewer request, pass it explicitly in `headers` or `body`.

You can set the `host` header on a network call to a custom origin that doesn't use origin access control. This differs from the viewer request, where the `host` header in the [Request object](functions-event-structure.md#functions-event-structure-request) is read only. Use it when the destination routes by host, such as a service that serves multiple hostnames from one endpoint. On an Amazon S3 origin or an origin with origin access control, setting `host` throws a `TypeError` (`Host header override is not supported for the provided origin`). An invalid `host` value also throws a `TypeError`.

If the origin has origin access control (OAC) configured, CloudFront signs the network call with SigV4 on your behalf, so you don't implement signing in your function or put credentials in your function code. Signing follows the signing behavior of the origin. With `never`, CloudFront doesn't sign the call. With `no-override`, CloudFront doesn't sign the call when your function sets an `Authorization` header or the origin has an `Authorization` custom header. For more information, see [Advanced settings for origin access control](private-content-restricting-access-to-s3.md#oac-advanced-settings-s3).

CloudFront adds the `x-amz-content-sha256` header for you. It is `UNSIGNED-PAYLOAD` for a call with a body and the hash of an empty string for a call without one. The exception is a `POST` or `PUT` with a body to a Lambda function URL, which doesn't accept unsigned payloads. For those calls, your function must add an `x-amz-content-sha256` header with the SHA-256 digest of the body.

CloudFront copies the following headers from the viewer request. If you supply them in your function, CloudFront ignores them.
+ `X-Forwarded-For`
+ `Via`
+ `CDN-Loop`

In addition to the existing [Disallowed headers](edge-function-restrictions-all.md#function-restrictions-disallowed-headers) for CloudFront Functions, CloudFront doesn't allow the following headers on network calls. Supplying any of them throws a `TypeError`.
+ `Accept-Encoding`
+ `Content-Length`
+ `TE`
+ `Transfer-Encoding`

## Limitations
<a name="network-calls-limitations"></a>
+ Distributions on the free pricing plan do not support network calls. `cf.fetch()` and `cf.beacon()` throw a `TypeError`, for example `"cloudfront.fetch" is not available on the free pricing plan`. For more information, see [CloudFront flat-rate pricing plans](flat-rate-pricing-plan.md).
+ Multi-tenant distributions and distribution tenants do not support network calls. For more information, see [Unsupported features](distribution-config-options.md#unsupported-saas).
+ Call `cf.fetch()` and `cf.beacon()` only inside the handler. They don't work from global scope.
+ Only one network call per invocation.
+ Network calls are not supported when you test a function with the `TestFunction` API or the **Test** tab in the CloudFront console. The call throws a `TypeError`.
+ CloudFront Functions doesn't support response body streaming. `text()` decodes the body as UTF-8 and replaces invalid bytes. `bytes()` and `arrayBuffer()` return the raw bytes.
+ AWS WAF does not inspect network calls. The web ACL associated with your distribution evaluates viewer requests, not requests your function makes.
+ CloudFront doesn't cache network call responses. Every invocation that reaches a network call makes one.
+ [Connection Functions](connection-functions.md) do not support network calls.
+ Distributions that use [continuous deployment](continuous-deployment.md) do not support network calls.

For quotas, including the network call timeout and the maximum request and response body sizes, see [Quotas on CloudFront Functions network calls](cloudfront-limits.md#limits-functions-network-calls).