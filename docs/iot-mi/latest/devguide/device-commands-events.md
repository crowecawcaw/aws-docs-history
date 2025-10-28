# Manage IoT device commands and events

Device commands provide the ability to remotely manage a physical device ensuring complete
control over the device in addition to performing critical security, software, and hardware
updates. With a large fleet of devices, knowing when a device performs a command provides
oversight over your entire device implementation. A device command or an automatic update will
trigger a device state change, which in turn will create a new device event. This device event
will trigger a notification automatically sent to a customer-managed destination.

###### Topics

- [Device commands](#device-commands "#device-commands")
- [Device Events](#device-events "#device-events")

## Device commands

A command request is the command being sent to the device. A command request
includes a payload that specifies the action to be taken such as turning on the light bulb. To
send a device command, the `SendManagedThingCommand` API is called on behalf of the
end user by managed integrations and the command request is sent to the device.

The response to a `SendManagedThingCommand` is a `traceId` and you can use this `traceId` to track the command delivery and any
related command response workflows wherever possible.

For more information on the `SendManagedThingCommand` API operation, see [SendManagedThingCommand](../APIReference/API_SendManagedThingCommand.md "../APIReference/API_SendManagedThingCommand.md").

**`UpdateState` action**

To update the state of a device such as the time a light turns on, use the
`UpdateState` action when calling the `SendManagedThingCommand` API.
Provide the data model property and new value you are updating in `parameters`. The
below example illustrates a `SendManagedThingCommand` API request updating the
`OnTime` of a light bulb to `5`.

```
{
  "Endpoints": [
    {
      "endpointId": "1",
      "capabilities": [
        {
          "id": "matter.OnOff",
          "name": "On/Off",
          "version": "1",
          "actions": [
            {
              "name": "UpdateState",
              "parameters": {
                "OnTime": 5
              }
            }
          ]
        }
      ]
    }
  ]
}
```

**`ReadState` action**

To get the latest state of a device including the current values of all data model
properties, use the `ReadState` action when calling the
`SendManagedThingCommand` API. In `propertiesToRead`, you can use the
following options:

- Provide a specific data model property to get the latest value on such as
  `OnOff` determining if a light is on or off.
- Use the wildcard operator (`*`) to read _all_ device state
  properties for a capability.

The below examples illustrate both scenarios for a `SendManagedThingCommand` API
request using the `ReadState` action:

```
{
  "Endpoints": [
    {
      "endpointId": "1",
      "capabilities": [
        {
          "id": "aws.OnOff",
          "name": "On/Off",
          "version": "1",
          "actions": [
            {
              "name": "ReadState",
              "parameters": {
                "propertiesToRead": [ "OnOff" ]
              }
            }
          ]
        }
      ]
    }
  ]
}
```

```
{
  "Endpoints": [
    {
      "endpointId": "1",
      "capabilities": [
        {
          "id": "aws.OnOff",
          "name": "On/Off",
          "version": "1",
          "actions": [
            {
              "name": "ReadState",
              "parameters": {
                "propertiesToRead": [ "*" ]
              }
            }
          ]
        }
      ]
    }
  ]}
```

## Device Events

A device event includes the current state of the device. This can mean the device has
changed state, or is reporting its state even if the state has not changed. It includes property
reports and events that are defined in the data model. An event could be a washing machine cycle
has completed or thermostat has reached the targeted temperature set by the end user.

**Device event notifications**

An end user can subscribe to specific customer-managed destinations that they create for
updates on specific device events. To create a customer-managed destination, call the
`CreateDestination` API. When a device event is reported to managed integrations by the device,
the customer-managed destination is notified if one exists.
