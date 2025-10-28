# Tracing calls to downstream HTTP web services with the

X-Ray SDK for Go

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

When your application makes calls to microservices or public HTTP APIs, you can use the
`xray.Client` to instrument those calls as subsegments of your Go application, as
shown in the following example, where _http-client_ is an HTTP client.

The client creates a shallow copy of the provided HTTP client, defaulting to `http.DefaultClient`,
with roundtripper wrapped with `xray.RoundTripper`.

**main.go – HTTP client**

```
myClient := xray.Client(`http-client`)
```

**main.go – Trace downstream HTTP call with ctxhttp library**The following example instruments the outgoing HTTP call with the ctxhttp library using
`xray.Client`. `ctx` can be passed from the upstream call. This ensures that the existing
segment context is used. For example, X-Ray does not allow a new segment to be created within a Lambda function,
so the existing Lambda segment context should be used.

```
resp, err := ctxhttp.Get(ctx, xray.Client(nil), `url`)
```
