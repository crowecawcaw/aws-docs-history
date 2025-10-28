End of support notice:
On December 15, 2025, AWS will end support for AWS IoT Analytics. After December 15, 2025, you will no longer
be able to access the AWS IoT Analytics console, or AWS IoT Analytics resources.
For more information, see
[AWS IoT Analytics end of support](iotanalytics-end-of-support.md "iotanalytics-end-of-support.md").

# AddAttributes activity

An `addAttributes` activity adds attributes based on existing attributes in the
message. This lets you alter the shape of the message before it's stored. For example, you can
use `addAttributes` to normalize data coming from different generations of device
firmware.

Consider the following input message.

```
{
    "device": {
        "id": "device-123",
        "coord": [ 47.6152543, -122.3354883 ]
    }
}
```

The `addAttributes` activity looks like the following.

```
{
    "addAttributes": {
        "name": "MyAddAttributesActivity",
        "attributes": {
            "device.id": "id",
            "device.coord[0]": "lat",
            "device.coord[1]": "lon"
        },
        "next": "MyRemoveAttributesActivity"
    }
}
```

This activity moves the device ID to the root level and extracts the value in the
`coord` array, promoting them to top-level attributes called `lat` and
`lon`. As a result of this activity, the input message is transformed to the
following example.

```
{
    "device": {
        "id": "device-123",
        "coord": [ 47.6, -122.3 ]
    },
    "id": "device-123",
    "lat": 47.6,
    "lon": -122.3
}
```

The original device attribute is still present. If you want to remove it, you can use the
`removeAttributes` activity.
