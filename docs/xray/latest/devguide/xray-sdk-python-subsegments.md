# Generating custom subsegments with the

X-Ray SDK for Python

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

Subsegments extend a trace's
[segment](xray-concepts.md#xray-concepts-segments "xray-concepts.md#xray-concepts-segments") with details about work done in order to serve
a request. Each time you make a call with an instrumented client, the X-Ray SDK records the information
generated in a subsegment. You can create additional subsegments to group other subsegments, to measure
the performance of a section of code, or to record annotations and metadata.

To manage subsegments, use the `begin_subsegment` and `end_subsegment` methods.

###### Example main.py – Custom subsegment

```
from aws_xray_sdk.core import xray_recorder

`subsegment = xray_recorder.begin_subsegment('annotations')`
subsegment.put_annotation('id', 12345)
`xray_recorder.end_subsegment()`
```

To create a subsegment for a synchronous function, use the
`@xray_recorder.capture` decorator. You can pass a name for the subsegment to the
capture function or leave it out to use the function name.

###### Example main.py – Function subsegment

```
from aws_xray_sdk.core import xray_recorder

`@xray_recorder.capture('## create_user')`
def create_user():
...
```

For an asynchronous function, use the `@xray_recorder.capture_async` decorator,
and pass an async context to the recorder.

###### Example main.py – Asynchronous function subsegment

```
`from aws_xray_sdk.core.async_context import AsyncContext`
from aws_xray_sdk.core import xray_recorder
`xray_recorder.configure(service='my_service', context=AsyncContext())`

`@xray_recorder.capture_async('## create_user')`
async def create_user():
    ...

async def main():
    await myfunc()
```

When you create a subsegment within a segment or another subsegment, the X-Ray SDK for Python
generates an ID for it and records the start time and end time.

###### Example Subsegment with metadata

```
"subsegments": [{
  "id": "6f1605cd8a07cb70",
  "start_time": 1.480305974194E9,
  "end_time": 1.4803059742E9,
  "name": "Custom subsegment for UserModel.saveUser function",
  "metadata": {
    "debug": {
      "test": "Metadata string from UserModel.saveUser"
    }
  },
```
