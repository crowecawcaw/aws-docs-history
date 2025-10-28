# AWS implementation of the Matter data model

The AWS implementation of the Matter Data Model manages all communication between managed integrations and third-party cloud
providers.

For more information, see [Matter Data Model: Developer Resources](https://csa-iot.org/resources/developer-resources/page/2/?dr_keywords&dr_solution%5B0%5D=935&dr_lang=1019 "https://csa-iot.org/resources/developer-resources/page/2/?dr_keywords&dr_solution%5B0%5D=935&dr_lang=1019").

**Device Hierarchy**

There are two data elements used to describe a device:
`endpoint` and `cluster`.

**`endpoint`**

The `endpoint` represents the logical interfaces or services offered by the
feature.

```
{
    "id": { "type":"string"},
    "clusters": Cluster[]
}
```

**`cluster`**

The `cluster` represents the device capabilities.

```
{
    "id": "hexadecimalString",
   "revision": "string"        // optional
    "attributes": AttributeMap<String attributeId, JSONNode>,
   "commands": CommandMap<String commandId, JSONNode>,
   "events": EventMap<String eventId, JsonNode>
}
```

For the `cluster` data element, there are three items that comprise that item:
`attribute`, `command`, and `event`. They can be used to
interact with and monitor the device.

- **Attribute**: States that are held by the device, such
  as the current brightness level attribute of a dimmable light.
  - ```
    {
        "id" (hexadecimalString): (JsonNode) value
    }
    ```

  ```

  ```

- **Command**: Tasks that may be performed, such as locking
  a door on a door lock. Commands may generate responses and results.
  - ```
    "id": {
        "fieldId": "fieldValue",
        ...
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
  transitions. While `attributes` represent the current states, events are a
  journal of the past, and include a monotonically increasing counter, a timestamp, and a
  priority. They enable capturing state transitions, as well as data modeling that is not
  readily achieved with `attributes`.
  - ```
    "id": {
        "fieldId": "fieldValue",
        ...
    }
    ```

  ```

  ```
