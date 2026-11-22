

# PID remapping examples

The following examples show the `processors` member of a router output as JSON. You can use them in a `CreateRouterOutput` or `UpdateRouterOutput` request with the AWS CLI or the MediaConnect API.

In the MediaConnect console, you can create the same rules under **Rules** in the **Processors** section. For more information, see [Configuring PID remapping](configuring-pid-remapping.md).

**Topics**
+ [Keep the same PIDs across route changes](#pid-remapping-example-same-pids)
+ [Keep English and Spanish audio and metadata](#pid-remapping-example-languages)
+ [Map streams to fixed PID ranges](#pid-remapping-example-fixed-ranges)
+ [Additional resources](#pid-remapping-examples-additional-resources)

## Keep the same PIDs across route changes
<a name="pid-remapping-example-same-pids"></a>

This example moves every stream to the auto map range.

```json
"processors": {
  "singleProgramTransportStreamPidMap": {
    "rules": [],
    "defaultAction": "mapAuto"
  }
}
```

## Keep English and Spanish audio and metadata
<a name="pid-remapping-example-languages"></a>

This example moves the first video stream to PID 256, moves the English and Spanish audio and metadata streams to the auto map range, and drops the rest.

```json
"processors": {
  "singleProgramTransportStreamPidMap": {
    "rules": [
      { "matchExpression": "index(video, 0)", "action": "mapPid(256)" },
      { "matchExpression": "type(audio) && language(eng, spa)", "action": "mapAuto" },
      { "matchExpression": "type(metadata) && language(eng, spa)", "action": "mapAuto" }
    ],
    "defaultAction": "drop"
  }
}
```

## Map streams to fixed PID ranges
<a name="pid-remapping-example-fixed-ranges"></a>

This example moves the first video stream to PID 256, audio streams to PIDs 257–271, and metadata streams to PIDs 272–287, and drops the rest.

```json
"processors": {
  "singleProgramTransportStreamPidMap": {
    "rules": [
      { "matchExpression": "index(video, 0)", "action": "mapPid(256)" },
      { "matchExpression": "type(audio)", "action": "mapPidRange(257, 271)" },
      { "matchExpression": "type(metadata)", "action": "mapPidRange(272, 287)" }
    ],
    "defaultAction": "drop"
  }
}
```

## Additional resources
<a name="pid-remapping-examples-additional-resources"></a>

For more information about the `processors` member, see the following pages in the *MediaConnect API Reference*:
+ [CreateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_CreateRouterOutput.html)
+ [UpdateRouterOutput](https://docs.aws.amazon.com/mediaconnect/latest/api/API_UpdateRouterOutput.html)

This includes information about how to use the `CreateRouterOutput` and `UpdateRouterOutput` operations and parameters in one of the language-specific AWS SDKs.