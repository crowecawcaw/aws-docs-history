# Manage AWS IoT FleetWise vehicle models

You use signals to create vehicle models that help standardize the format of your
vehicles. Vehicle models enforce consistent information across multiple vehicles of the
same type, so that you can process data from fleets of vehicles. Vehicles created from
the same vehicle model inherit the same group of signals. For more information, see
[Manage AWS IoT FleetWise vehicles](vehicles.md "vehicles.md").

Each vehicle model has a status field that contains the state of the vehicle model.
The state can be one of the following values:

- `ACTIVE` – The vehicle model is active.
- `DRAFT` – The configuration of the vehicle model is saved.

###### Important

- You must have a signal catalog before you can create a vehicle model using
  the `CreateModelManifest` API operation. For more information,
  see [Create an AWS IoT FleetWise signal catalog](create-signal-catalog.md "create-signal-catalog.md").
- If you use the AWS IoT FleetWise console to create a vehicle model, AWS IoT FleetWise
  automatically activates the vehicle model for you.
- If you use the `CreateModelManifest` API operation to create a
  vehicle model, the vehicle model stays in the `DRAFT`
  state.
- You can't create vehicles from vehicle models that are in the
  `DRAFT` state. Use the `UpdateModelManifest` API
  operation to change vehicle models to the `ACTIVE` state.
- You can't edit vehicle models that are in the `ACTIVE`
  state.

###### Topics

- [Create an AWS IoT FleetWise vehicle model](create-vehicle-model.md "create-vehicle-model.md")
- [Update an AWS IoT FleetWise vehicle model](update-vehicle-model-cli.md "update-vehicle-model-cli.md")
- [Delete an AWS IoT FleetWise vehicle model](delete-vehicle-model.md "delete-vehicle-model.md")
- [Get AWS IoT FleetWise vehicle model
  information](get-vehicle-model-information.md "get-vehicle-model-information.md")
