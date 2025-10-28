Defect Detection App is in preview release and is subject to change.

# GET /snapshotfile/{path}

Gets a TAR archive file that contains a snapshot of the station logs. You get the location
of the TAR archive file from a call to [GET /snapshot](api-get-snapshot.md "api-get-snapshot.md").

The log files contain AWS IoT Greengrass logs, local server logs, and system information (memory, CPU,
I/O, processes, disk).

## Endpoint

```
GET /snapshotfile/{path}
```

## Request

parameters

None

## Response

A TAR archive file that contains the log snapshot.

Format: String
