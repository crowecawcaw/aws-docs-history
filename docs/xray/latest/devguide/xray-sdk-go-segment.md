# Add annotations and metadata to segments with the

X-Ray SDK for Go

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

You can record additional information about requests, the
environment, or your application with annotations and metadata. You can add annotations and
metadata to the segments that the X-Ray SDK creates, or to custom subsegments that you create.

**Annotations** are
key-value pairs with string, number, or Boolean values. Annotations are indexed for use with
[filter expressions](xray-console-filters.md "xray-console-filters.md"). Use annotations to record data
that you want to use to group traces in the console, or when calling the [`GetTraceSummaries`](../api/API_GetTraceSummaries.md "../api/API_GetTraceSummaries.md")
API.

**Metadata** are key-value
pairs that can have values of any type, including objects and lists, but are not indexed for use
with filter expressions. Use metadata to record additional data that you want stored in the trace
but don't need to use with search.

In addition to annotations and metadata, you can also [record user ID strings](#xray-sdk-go-segment-userid "#xray-sdk-go-segment-userid") on segments. User IDs are
recorded in a separate field on segments and are indexed for use with search.

###### Sections

- [Recording annotations with the
  X-Ray SDK for Go](#xray-sdk-go-segment-annotations "#xray-sdk-go-segment-annotations")
- [Recording metadata with the
  X-Ray SDK for Go](#xray-sdk-go-segment-metadata "#xray-sdk-go-segment-metadata")
- [Recording user IDs with the X-Ray SDK for Go](#xray-sdk-go-segment-userid "#xray-sdk-go-segment-userid")

## Recording annotations with the

X-Ray SDK for Go

Use annotations to record information on segments that you want indexed for search.

###### Annotation Requirements

- **Keys** – The key for an X-Ray annotation can have
  up to 500 alphanumeric characters. You cannot use spaces or symbols other
  than a dot or period ( . )
- **Values** – The value for an X-Ray annotation can have up to 1,000 Unicode
  characters.
- The number of **Annotations** – You can use up to 50 annotations per
  trace.

To record annotations, call `AddAnnotation` with a string containing the
metadata you want to associate with the segment.

```
xray.AddAnnotation(`key string`, `value interface{}`)
```

The SDK records annotations as key-value pairs in an `annotations` object in
the segment document. Calling `AddAnnotation` twice with the same key overwrites
previously recorded values on the same segment.

To find traces that have annotations with specific values, use the
`annotation[`key`]` keyword in a [filter expression](xray-console-filters.md "xray-console-filters.md").

## Recording metadata with the

X-Ray SDK for Go

Use metadata to record information on segments that you don't need indexed for
search.

To record metadata, call `AddMetadata` with a string containing the metadata
you want to associate with the segment.

```
xray.AddMetadata(`key string`, `value interface{}`)
```

## Recording user IDs with the X-Ray SDK for Go

Record user IDs on request segments to identify the user who sent the request.

###### To record user IDs

1. Get a reference to the current segment from `AWSXRay`.

```
import (
  "context"
  "github.com/aws/aws-xray-sdk-go/xray"
)

mySegment := xray.GetSegment(`context`)
```

2. Call `setUser` with a String ID of the user who sent the request.

```
mySegment.User = "`U12345`"
```

To find traces for a user ID, use the `user` keyword in a [filter expression](xray-console-filters.md "xray-console-filters.md").
