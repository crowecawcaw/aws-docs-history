# Get a device's location history from a

tracker

Your Amazon Location tracker resource maintains the location history of all your
tracked devices for a period of 30 days. You can retrieve device location history,
including all associated metadata, from your tracker resource. The following
examples use the AWS CLI, or the Amazon Location APIs.

API
**To get the device location history from a
tracker using the Amazon Location APIs**

Use the `GetDevicePositionHistory` operation from the
Amazon Location Trackers APIs.

The following example uses an API URI request to get the device
location history of `ExampleDevice` from a
tracker called `ExampleTracker` starting from
`19:05:07` (inclusive) and ends at `19:20:07`
(exclusive) on `2020–10–02`.

```
POST /tracking/v0/trackers/`ExampleTracker`/devices/`ExampleDevice`/list-positions
Content-type: application/json
{
  "StartTimeInclusive": "2020-10-02T19:05:07.327Z",
  "EndTimeExclusive": "2020-10-02T19:20:07.327Z"
}
```

AWS CLI
**To get the device location history from a
tracker using AWS CLI commands**

Use the `get-device-position-history` command.

The following example uses an AWS CLI to get the device location history
of `ExampleDevice` from a tracker called
`ExampleTracker` starting from
`19:05:07` (inclusive) and ends at `19:20:07`
(exclusive) on `2020–10–02`.

```
aws location \
    get-device-position-history \
        --device-id "`ExampleDevice`" \
        --start-time-inclusive "2020-10-02T19:05:07.327Z" \
        --end-time-exclusive "2020-10-02T19:20:07.327Z" \
        --tracker-name "``ExampleTracker``"
```
