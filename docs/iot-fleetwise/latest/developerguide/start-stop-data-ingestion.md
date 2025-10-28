# Activate and deactivate state data

collection using state templates

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

The following sections describe how to activate and deactivate data ingestion with
state templates using the AWS CLI.

###### Important

Before you start, make sure that you already created a [state template](state-templates.md "state-templates.md"), and associated it and its
update strategy with a vehicle.

You must activate a state template so the Edge Agent can send signal
updates to the cloud.

To perform these operations with state templates, first create a command resource
and then start the command execution on the vehicle. The following section describes
how to use this API and how to activate and deactivate data ingestion.

###### Topics

- [Using the
  CreateCommand API](#start-stop-ingestion-create-command "#start-stop-ingestion-create-command")
- [Example: Activate a
  state template](#start-stop-ingestion-activate-template "#start-stop-ingestion-activate-template")
- [Example: Deactivate a
  state template](#start-stop-ingestion-deactivate-template "#start-stop-ingestion-deactivate-template")

## Using the

`CreateCommand` API

Create a command resource in the "`AWS-IoTFleetwise`"
namespace, and use the following parameters when you create or send a command
resource for a state template:

- `$stateTemplate.name` – The name of the state template on which
  to perform the operation. The state template must be applied to the
  vehicle before you can perform an operation. For more information, see [Associate an AWS IoT FleetWise state template with a vehicle](state-templates.md#apply-state-templates "state-templates.md#apply-state-templates").
- `$stateTemplate.operation` – The operation to be performed
  on the state template. Use one of the following values for this
  parameter:
  - `activate` – The Edge Agent starts sending signal
    updates to the cloud based on the
    `stateTemplateUpdateStrategy` you specified (on-change or periodic) when you applied the state template to
    the vehicle. For more information, see [Associate an AWS IoT FleetWise state template with a vehicle](state-templates.md#apply-state-templates "state-templates.md#apply-state-templates").

  Also, you can define an automatic state template deactivation
  time to stop updates after a specified time period. If an
  automatic deactivation time is not provided, the state templates will
  keep sending updates until a deactivate call is issued.

  As soon as the `activate` command is received, the
  device should send the signals specified in the state template
  according to the update strategy. AWS IoT FleetWise recommends that when an
  activate command is received by the device, the first message it
  sends should contain a snapshot of all the signals in the
  state template. Subsequent messages should be sent according to
  the update strategy.
  - `deactivate` – The Edge Agent stops sending signal
    updates to the cloud.
  - `fetchSnapshot` – The Edge Agent sends a onetime snapshot
    of the signals defined in the state template regardless of the
    `stateTemplateUpdateStrategy` you specified when
    you applied the state template to the vehicle.

- (Optional) `$stateTemplate.deactivateAfterSeconds` – The
  state template is automatically deactivated after the time specified.
  This parameter can only be used when the value of the
  `$stateTemplate.operation` parameter is “activate”. If
  this parameter isn't specified, or if the value of this parameter is 0,
  the Edge Agent keeps sending signal updates to the cloud until a
  "deactivate" operation is received for the state template. The state
  template is never automatically deactivated.

Minimum value: 0, maximum value: 4294967295.

###### Note

- The API returns success in response to an activation request for a
  template already in the active state.
- The API returns success in response to a deactivation request for a
  template already in the deactivation state.
- The most recent request that you make on a state template is the one
  that takes effect. For example, if you make a request for a state
  template to deactivate in one hour, then make a second request for
  that same template to deactivate in four hours, the four hour deactivation takes
  effect due to it being the most recent request.

###### Important

A validation exception can occur in any of the following scenarios:

- A state template is provided which is not `ASSOCIATED` with a
  vehicle.
- A request is made to activate a state template but it hasn't
  been `DEPLOYED` on a vehicle.
- A request is made to a state template but it's being `DELETED` on a
  vehicle.

## Example: Activate a

state template

To activate a state template, first create a command resource. You can then send the following
command to the vehicle on which you want to activate the state
template. This example shows how you can specify default values for the
parameters when creating a command. These parameters and their values are
used when starting the command execution to activate the state template.

1. ###### Create a command resource

Before you can send a command to the vehicle, you must create a
command resource. You can specify alternative values for mandatory
parameters when you send the command to the vehicle. For more information, see [Create a command resource](create-manage-remote-command-cli.md#create-remote-command-cli "create-manage-remote-command-cli.md#create-remote-command-cli").

###### Important

`$stateTemplate.name` and
`$stateTemplate.operation` parameters must be
provided as a string data type. If any other data type is provided,
or if either of these two parameters is missing, the command
execution fails with a validation exception. The
`$stateTemplate.deactivateAfterSeconds` parameter
must be provided as a `Long` data type.

```
aws iot create-command \
    --description "This command activates a state template on a vehicle"
    --command-id ActivateStateTemplate \
    --display-name "Activate State Template" \
    --namespace AWS-IoTFleetWise \
    --mandatory-parameters '[
    {
        "name": "$stateTemplate.name",
        "defaultValue": {"S": "ST123"}
    },
    {
        "name": "$stateTemplate.operation",
        "defaultValue": {"S": "activate"}
    },
    {
        "name": "$stateTemplate.deactivateAfterSeconds",
        "defaultValue": {"L": "120"}
    }
]'
```

2. ###### Start the command execution on the vehicle

After the command is created, send the command to the vehicle.
If you didn't specify values for the mandatory parameters when you
created the command resource, you must specify them now. For more information, see [Send a command (AWS CLI)](send-monitor-remote-command-cli.md#send-remote-command-cli "send-monitor-remote-command-cli.md#send-remote-command-cli").

###### Important

Make sure that you use the account-specific AWS IoT jobs data plane API
endpoint for the API operation.

```
aws iot-jobs-data start-command-execution \
    --endpoint-url <endpoint-url> \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/ActivateStateTemplate \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/`<VEHICLE_NAME>`
```

3. ###### Retrieve the status of the state template operation

After you start the command execution, you can use the
`GetCommandExecution` API to retrieve the state
template.

```
aws iot get-command-execution --execution-id `<EXECUTION_ID>`
```

## Example: Deactivate a

state template

To deactivate a state template, first create a command resource. You can then send the
following command to the vehicle on which you want to deactivate the state
template. This example shows how you can specify default values for the
parameters when creating a command. These parameters and their values are
used when starting the command execution to deactivate the state
template.

1. ###### Create a command resource

Before you can send a command to the vehicle, you must create a
command resource. You can specify alternative values for mandatory
parameters when you send the command to the vehicle. For more information, see [Create a command resource](create-manage-remote-command-cli.md#create-remote-command-cli "create-manage-remote-command-cli.md#create-remote-command-cli").

```
aws iot create-command \
    --description "This command deactivates a state template on a vehicle"
    --command-id DeactivateStateTemplate \
    --display-name "Deactivate State Template" \
    --namespace AWS-IoTFleetWise \
    --mandatory-parameters '[
    {
        "name": "$stateTemplate.name",
        "defaultValue": {"S": "ST123"}
    },
    {
        "name": "$stateTemplate.operation",
        "defaultValue": {"S": "deactivate"}
    }
]'
```

2. ###### Start the command execution on the vehicle

After the command is created, send the command to the vehicle.
If you didn't specify values for the mandatory parameters when you
created the command resource, you must specify them now. For more information, see [Send a command (AWS CLI)](send-monitor-remote-command-cli.md#send-remote-command-cli "send-monitor-remote-command-cli.md#send-remote-command-cli").

```
aws iot-jobs-data start-command-execution \
    --endpoint-url <endpoint-url> \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/DeactivateStateTemplate \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/`<VEHICLE_NAME>`
```

3. ###### Retrieve the status of the state template operation

After you start the command execution, you can use the
`GetCommandExecution` API to retrieve the state
template.

```
aws iot get-command-execution  --execution-id `<EXECUTION_ID>`
```
