# Fetch a vehicle state snapshot using state templates

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

You can fetch a vehicle's last known state using the[`CreateCommand`](../../../iot/latest/apireference/API_CreateCommand.md "../../../iot/latest/apireference/API_CreateCommand.md") AWS IoT Core control plane API operation or the AWS IoT FleetWise console.

###### Important

A validation exception can occur in any of the following scenarios:

- A state template is provided which is not `ASSOCIATED` with a
  vehicle.
- A request is made to activate a state template but it hasn't
  been `DEPLOYED` on a vehicle.
- A request is made to a state template but it's being `DELETED` on a
  vehicle.
  You can use the AWS IoT FleetWise console to fetch a vehicle's last known state. AWS IoT FleetWise will create a command for you to fetch data.

###### To fetch a vehicle's state

1. Open the [AWS IoT FleetWise console](https://console.aws.amazon.com/iotfleetwise "https://console.aws.amazon.com/iotfleetwise").
2. On the navigation pane, choose **Vehicles**.
3. Choose a vehicle from the list to open its details page.
4. On the **State templates** tab, choose **Fetch data**.
5. Select the IAM role that grants AWS IoT FleetWise permissions to send a command and fetch data. See [Controlling access](controlling-access.md#generate-command-payload "controlling-access.md#generate-command-payload").
6. Choose **Fetch state**.
   To fetch a state snapshot, first create a command resource. You can then send the following command
   to the vehicle for which you want to fetch the state snapshot. For more
   information about using the `CreateCommand` API and its parameters, see
   [Using the
   CreateCommand API](start-stop-data-ingestion.md#start-stop-ingestion-create-command "start-stop-data-ingestion.md#start-stop-ingestion-create-command").

7. ###### Create a command resource

The following example shows how to create the command resource to perform
the fetch operation. You can specify alternative values for mandatory
parameters when you send the command to the vehicle. For more information, see [Create a command resource](create-manage-remote-command-cli.md#create-remote-command-cli "create-manage-remote-command-cli.md#create-remote-command-cli").

```
aws iot create-command \
    --command-id `<COMMAND_ID>` \
    --display-name "FetchSnapshot State Template" \
    --namespace AWS-IoTFleetWise \
    --mandatory-parameters '[
      {
          "name": "$stateTemplate.name",
          "defaultValue": {"S": "ST123"}
      },
      {
          "name": "$stateTemplate.operation",
          "defaultValue": {"S": "fetchSnapshot"}
      }
    ]'
```

Response:

```
{
    "commandId": "`<COMMAND_ID>`",
    "commandArn": "arn:aws:iot:`<REGION>`:`111122223333`:command/`<COMMAND_ID>`"
}
```

2. ###### Start command execution to fetch state snapshot

After the command is created, send the command to the vehicle. If
you didn't specify values for the mandatory parameters when you created the
command resource, you must specify them now. For more information, see [Send a command (AWS CLI)](send-monitor-remote-command-cli.md#send-remote-command-cli "send-monitor-remote-command-cli.md#send-remote-command-cli").

```
aws iot-jobs-data start-command-execution \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/`<COMMAND_ID>` \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/`<VEHICLE_NAME>`
```

Response:

```
{
    "executionId": "`<UNIQUE_UUID>`"
}
```

3. Retrieve the status of the state template operation

After you start the command execution, you can use the
`GetCommandExecution` API to retrieve the state
template.

```
aws iot get-command-execution --execution-id `<EXECUTION_ID>`
```
