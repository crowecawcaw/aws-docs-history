# Managed integrations data model

The managed integrations data model manages all communication between the end user and
managed integrations.

**Device Hierarchy**

The `endpoint` and `capability` data elements are used to describe a device in the managed integrations data model.

**`endpoint`**

The `endpoint` represents the logical interfaces or services offered by the
feature.

```
{
    "endpointId": { "type":"string" },
    "capabilities": Capability[]
}
```

**`Capability`**

The `capability` represents the device capabilities.

```
{
    "$id": "string",                // Schema identifier (e.g. /schema-versions/capability/matter.OnOff@1.4)
    "name": "string",               // Human readable name
    "version": "string",            // e.g. 1.0
    "properties": Property[],
    "actions": Action[],
    "events": Event[]
}
```

For the `capability` data element, there are three items that comprise that
item: `property`, `action`, and `event`. They can be used to
interact with and monitor the device.

- **Property**: States that are held by the device, such as
  the current brightness level attribute of a dimmable light.
  - ```
    {
        "name":                      // Property Name is outside of Property Entity
        "value": Value,              // value represented in any type e.g. 4, "A", []
        "lastChangedAt": Timestamp   // ISO 8601 Timestamp upto milliseconds yyyy-MM-ddTHH:mm:ss.ssssssZ
        "mutable": boolean,
        "retrievable": boolean,
        "reportable": boolean

    ```

  }

  ```

  ```

- **Action**: Tasks that may be performed, such as locking
  a door on a door lock. Actions may generate responses and results.
  - ```
    {
        "name": { "$ref": "/schema-versions/definition/aws.name@1.0" }, //required
        "parameters": Map<String name, JSONNode value>,
        "responseCode": HTTPResponseCode,
        "errors": {
            "code": "string",
            "message": "string"
        }
    }
    ```

  ```

  ```

- **Event**: Essentially a record of past state
  transitions. While `property` represent the current states, events are a
  journal of the past, and include a monotonically increasing counter, a timestamp, and a
  priority. They enable capturing state transitions, as well as data modeling that is not
  readily achieved with `property`.
  - ```
    {
        "name": { "$ref": "/schema-versions/definition/aws.name@1.0" },        //required
        "parameters": Map<String name, JSONNode value>
    }
    ```

  ```

  ```
