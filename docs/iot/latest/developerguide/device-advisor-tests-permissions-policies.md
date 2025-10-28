# Permissions and policies

You can use the following tests to determine if the policies attached to your
devices’ certificates follow standard best practices.

**MQTT over WebSocket** is not supported at this time.

**"Device certificate attached policies don’t contain wildcards"**

Validates if the permission policies associated with a device follow
best practices and do not grant the device more permissions than
needed.

_API test case definition:_

###### Note

`EXECUTION_TIMEOUT` has a default value of 1 minute. We
recommend setting a timeout of at least 30 seconds.

```
"tests":[
   {
        "name":`"my_security_device_policies"`,
        "configuration": {
            // optional:
            "EXECUTION_TIMEOUT":"60"    // in seconds
        },
        "test": {
            "id": "Security_Device_Policies",
            "version": "0.0.0"
        }
    }
]
```
