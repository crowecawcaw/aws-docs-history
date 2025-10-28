# Add annotations and metadata to segments with the

X-Ray SDK for .NET

###### Note

End-of-support notice – On February 25th, 2027, AWS X-Ray will discontinue support for AWS X-Ray SDKs and daemon. After February 25th, 2027, you will no longer receive updates or releases. For more information on the support timeline, see
[X-Ray SDK and daemon end of support timeline](xray-daemon-eos.md "xray-daemon-eos.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

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

###### Sections

- [Recording annotations with the
  X-Ray SDK for .NET](#xray-sdk-dotnet-segment-annotations "#xray-sdk-dotnet-segment-annotations")
- [Recording metadata with the
  X-Ray SDK for .NET](#xray-sdk-dotnet-segment-metadata "#xray-sdk-dotnet-segment-metadata")

## Recording annotations with the

X-Ray SDK for .NET

Use annotations to record information on segments or subsegments that you want indexed for
search.

The following are required for all annotations in X-Ray:

###### Annotation Requirements

- **Keys** – The key for an X-Ray annotation can have
  up to 500 alphanumeric characters. You cannot use spaces or symbols other
  than a dot or period ( . )
- **Values** – The value for an X-Ray annotation can have up to 1,000 Unicode
  characters.
- The number of **Annotations** – You can use up to 50 annotations per
  trace.

###### To record annotations outside of a AWS Lambda function

1. Get an instance of `AWSXRayRecorder`.

```
using Amazon.XRay.Recorder.Core;
...
AWSXRayRecorder recorder = AWSXRayRecorder.Instance;
```

2. Call `addAnnotation` with a String key and a Boolean, Int32, Int64, Double,
   or String value.

```
recorder.AddAnnotation("mykey", "my value");
```

The following example shows how to call `putAnnotation` with a String key
that includes a dot, and a Boolean, Number, or String value.

```
document.putAnnotation("testkey.test", "my value");
```

###### To record annotations inside of a AWS Lambda function

Both segments and subsegments inside a Lambda function are managed by the Lambda runtime environment. If you want to add an annotation to a segment
or subsegment inside a Lambda function, you must do the following:

1. Create the segment or subsegment inside the Lambda function.
2. Add the annotation to the segment or subsegment.
3. End the segment or subsegment.

The following code example shows you how to add an annotation to a subsegment inside a Lambda function:

```
#Create the subsegment
AWSXRayRecorder.Instance.BeginSubsegment("custom method");
#Add an annotation
AWSXRayRecorder.Instance.AddAnnotation("My", "Annotation");
try
{
  YourProcess(); #Your function
}
catch (Exception e)
{
  AWSXRayRecorder.Instance.AddException(e);
}
finally #End the subsegment
{
  AWSXRayRecorder.Instance.EndSubsegment();
}
```

The X-Ray SDK records annotations as key-value pairs in an `annotations` object in
the segment document. Calling the `addAnnotation` operation twice with the same key overwrites
a previously recorded value on the same segment or subsegment.

To find traces that have annotations with specific values, use the
`annotation[`key`]` keyword in a [filter expression](xray-console-filters.md "xray-console-filters.md").

## Recording metadata with the

X-Ray SDK for .NET

Use metadata to record information on segments or subsegments that you don't need to index for use inside a search. Metadata values can be strings, numbers,
booleans, or any other object that can be serialized into a JSON object or array.

###### To record metadata

1. Get an instance of `AWSXRayRecorder`, as shown in the following code example:

```
using Amazon.XRay.Recorder.Core;
...
AWSXRayRecorder recorder = AWSXRayRecorder.Instance;
```

2. Call `AddMetadata` with a string namespace, string key, and an object
   value, as shown in the following code example:

```
recorder.AddMetadata("`my namespace`", "`my key`", "`my value`");
```

You can also call the `AddMetadata` operation using just a key and value pair, as shown in the following code example:

```
recorder.AddMetadata("`my key`", "`my value`");
```

If you don't specify a value for the namespace, the X-Ray SDK uses `default`. Calling
the `AddMetadata` operation twice with the same key overwrites a previously recorded value on
the same segment or subsegment.
