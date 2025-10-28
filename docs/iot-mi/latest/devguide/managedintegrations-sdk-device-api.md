# Low level C-Function APIs

Integrate your device-specific code with managed integrations using the provided low level C-Function
APIs. This section describes the API operations available for each cluster in the AWS data
model for efficient device to cloud interactions. Learn how to implement callback functions,
emit events, notify attribute changes, and register clusters for your device endpoints.

###### Key API components include:

1. Callback function pointer structures for attributes and commands
2. Event emission functions
3. Attribute change notification functions
4. Cluster registration functions
   By implementing these APIs, you create a bridge between your device's physical operations
   and the managed integrations cloud features, ensuring seamless communication and control.

The following section illustrates the [OnOff cluster](https://github.com/project-chip/connectedhomeip/blob/v1.3.0.0/data_model/clusters/OnOff.xml "https://github.com/project-chip/connectedhomeip/blob/v1.3.0.0/data_model/clusters/OnOff.xml") API.

## OnOff cluster API

The [OnOff.xml](https://github.com/project-chip/connectedhomeip/blob/5bb5c9e23d532cea40476fc0bd1d3008522792ba/data_model/clusters/OnOff.xml "https://github.com/project-chip/connectedhomeip/blob/5bb5c9e23d532cea40476fc0bd1d3008522792ba/data_model/clusters/OnOff.xml") cluster supports these attributes and commands:
.

- Attributes:
  - `OnOff (boolean)`
  - `GlobalSceneControl (boolean)`
  - `OnTime (int16u)`
  - `OffWaitTime (int16u)`
  - `StartUpOnOff (StartUpOnOffEnum)`

- Commands:

      + `Off : () -> Status`
      + `On : () -> Status`
      + `Toggle : () -> Status`
      + `OffWithEffect : (EffectIdentifier: EffectIdentifierEnum, EffectVariant:
       enum8) -> Status`
      + `OnWithRecallGlobalScene : () -> Status`
      + `OnWithTimedOff : (OnOffControl: OnOffControlBitmap, OnTime: int16u,
       OffWaitTime: int16u) -> Status`

  For each command, we provide the 1:1 mapped function pointer that you can use to
  hook your implementation.

All the callbacks for attributes and commands are defined within a C struct named after
the cluster.

```
struct iotmiDev_clusterOnOff
{
  /*
    - Each attribute has a getter callback if it's readable

    - Each attribute has a setter callback if it's writable

    - The type of `value` are derived according to the data type of
      the attribute.

    - `user` is the pointer passed during an endpoint setup

    - The callback should return iotmiDev_DMStatus to report success or not.

    - For unsupported attributes, just leave them as NULL.
   */
  iotmiDev_DMStatus (*getOnTime)(uint16_t *value, void *user);
  iotmiDev_DMStatus (*setOnTime)(uint16_t value, void *user);
  /*
    - Each command has a command callback

    - If a command takes parameters, the parameters will be defined in a struct
      such as `iotmiDev_OnOff_OnWithTimedOffRequest` below.

    - `user` is the pointer passed during an endpoint setup

    - The callback should return iotmiDev_DMStatus to report success or not.

    - For unsupported commands, just leave them as NULL.
   */
  iotmiDev_DMStatus (*cmdOff)(void *user);
  iotmiDev_DMStatus (*cmdOnWithTimedOff)(const iotmiDev_OnOff_OnWithTimedOffRequest *request, void *user);
};
```

In addition to the C struct, attribute change reporting functions are defined for all
attributes.

```
/* Each attribute has a report function for the customer to report
   an attribute change. An attribute report function is thread-safe.
   */
void iotmiDev_OnOff_OnTime_report_attr(struct iotmiDev_Endpoint *endpoint, uint16_t newValue, bool immediate);

```

Event reporting functions are defined for all cluster-specific events. Since the
OnOff cluster does not define any events, below is an example from the
`CameraAvStreamManagement` cluster.

```
/* Each event has a report function for the customer to report
   an event. An event report function is thread-safe.
   The iotmiDev_CameraAvStreamManagement_VideoStreamChangedEvent struct is
   derived from the event definition in the cluster.
 */
void iotmiDev_CameraAvStreamManagement_VideoStreamChanged_report_event(struct iotmiDev_Endpoint *endpoint, const iotmiDev_CameraAvStreamManagement_VideoStreamChangedEvent *event, bool immediate);
```

Each cluster also has a register function.

```
iotmiDev_DMStatus iotmiDev_OnOffRegisterCluster(struct iotmiDev_Endpoint *endpoint, const struct iotmiDev_clusterOnOff *cluster, void *user);
```

The user pointer passed to the register function will be passed to the callback
functions.
