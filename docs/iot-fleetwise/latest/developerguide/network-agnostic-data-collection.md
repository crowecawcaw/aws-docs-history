# Tutorial: Configure network agnostic data collection using a custom decoding interface

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

## Introduction

This tutorial outlines how to configure AWS IoT FleetWise to collect data and run commands using network agnostic data collection, which utilizes a custom decoding interface. With network agnostic data collection, you can use your own methods to decode signals
before sending them to your specified data destination. This saves time since you don't need to create signal decoders specifically for AWS IoT FleetWise. You can have a subset of signals decoded using your own implementation, or you can use `defaultForUnmappedSignals` when you create or update a decoder manifest. This also provides flexibility to collect signals and triggers
across a wide range of sources within the vehicle.

This tutorial
is intended for vehicle signals that are not on a standard Controller Area Network (CAN bus) interface. For example,
data encoded in a custom in-vehicle format or scheme.

## Environment setup

This tutorial assumes you have gone through the steps to set up your environments to access the
AWS IoT FleetWise cloud, and the Edge implementation APIs and code base.

## Data models

The next section illustrates how to model vehicle properties using a custom decoding interface. This applies to data collection as well as command use cases.
It also applies to any underlying data source modeling used in the vehicle, for example,
IDLs.

In the example, there are two vehicle properties: a vehicle sensor (current vehicle position)
to collect and a vehicle actuator (Air Conditioner) to control remotely. Both of those are
defined in this scheme:

```
// Vehicle WGS84 Coordinates
double Latitude;
double Longitude;

// Vehicle AC
Boolean ActivateAC;
```

The next step is to import these definitions into AWS IoT FleetWise using the custom decoding interface
APIs.

### Signal catalog updates

Import these definitions in your signal catalog. If you have a signal catalog in AWS IoT FleetWise
already, use the update API directly. If you don’t have one, first create a signal catalog and
then call the update API.

First, you must create the VSS representation of these vehicle signals. VSS is used as a
Taxonomy to represent vehicle data in AWS IoT FleetWise. Create a json file called 'vehicle-signals.json'
with these contents:

```
// vehicle-signals.json
// Verify that branches and nodes are unique in terms of fully qualified name
// in the signal catalog.
[
 {
    "branch": {
      "fullyQualifiedName": "Vehicle",
      "description": "Vehicle Branch"
    }
  },
  {
    "branch": {
      "fullyQualifiedName": "Vehicle.CurrentLocation",
      "description": "CurrentLocation"
    }
  },
  {
    "sensor": {
      "dataType": "DOUBLE",
      "fullyQualifiedName": "Vehicle.CurrentLocation.Latitude",
      "description": "Latitude"
    }
  },
  {
    "sensor": {
      "dataType": "DOUBLE",
      "fullyQualifiedName": "Vehicle.CurrentLocation.Longitude",
      "description": "Longitude"
    }
  },
  {
    "actuator": {
      "fullyQualifiedName": "Vehicle.ActivateAC",
      "description": "AC Controller",
      "dataType": "BOOLEAN"
    }
  }
]
```

If you don't have a signal catalog in place, then you need to invoke
`create-signal-catalog`:

```
VEHICLE_NODES=`cat vehicle-signals.json`
aws iotfleetwise create-signal-catalog \
        --name my-signal-catalog \
        --nodes "${VEHICLE_NODES}"
```

If you have a signal catalog already, you can add those signals using the
`update-signal-catalog` API:

```
VEHICLE_NODES=`cat vehicle-signals.json`
aws iotfleetwise update-signal-catalog \
        --name my-signal-catalog \
        --nodes-to-add "${VEHICLE_NODES}"
```

### Vehicle model and decoder

After you insert the signals in the signal catalog, the next step is to create a vehicle
model and instantiate those signals. For that, you use the `create-model-manifest`
and `create-decoder-manifest` APIs.

First, format the signal names that you want to insert into the vehicle model:

```
# Prepare the signals for insertion into the vehicle model.
VEHICLE_NODES=`cat vehicle-signals.json`
VEHICLE_NODES=`echo ${VEHICLE_NODES} | jq -r ".[] | .actuator,.sensor | .fullyQualifiedName" | grep Vehicle\\.`
VEHICLE_NODES=`echo "${VEHICLE_NODES}" | jq -Rn [inputs]`
# This is how the vehicle model input looks.
echo $VEHICLE_NODES
# [ "Vehicle.CurrentLocation.Latitude",
#   "Vehicle.CurrentLocation.Longitude",
#   "Vehicle.ActivateAC" ]
# Create the vehicle model with those signals.
aws iotfleetwise create-model-manifest \
    --name `my-model-manifest` \
    --signal-catalog-arn arn:xxxx:signal-catalog/my-signal-catalog \
    --nodes "${VEHICLE_NODES}"

# Activate the vehicle model.
 aws iotfleetwise update-model-manifest \
    --name my-model-manifest --status ACTIVE
```

Now, use the custom decoding interface to create a decoder manifest.

###### Note

You only need to create network interfaces and signals if you want to specify custom IDs, which isn't part of this example.

For information about mapping decoding information when the fully qualified name (FQN) differs from the custom decoding signal ID, see the [_Edge Agent Developer Guide_](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/network-agnostic-dev-guide.md#aaos-vhal "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/network-agnostic-dev-guide.md#aaos-vhal").

```
// Create a network interface that is of type : CUSTOM_DECODING_INTERFACE
// custom-interface.json
[
  {
    "interfaceId": "NAMED_SIGNAL",
    "type": "CUSTOM_DECODING_INTERFACE",
    "customDecodingInterface": {
      "name": "NamedSignalInterface"
    }
  },
  {
    "interfaceId": "AC_ACTUATORS",
    "type": "CUSTOM_DECODING_INTERFACE",
    "customDecodingInterface": {
      "name": "NamedSignalInterface"
    }
  }
]
// custom-decoders.json
// Refer to the fully qualified names of the signals, make them of
// type CUSTOM_DECODING_SIGNAL, and specify them as part of the same interface ID
// that was defined above.
[
    {
      "fullyQualifiedName": "Vehicle.CurrentLocation.Longitude",
      "interfaceId": "NAMED_SIGNAL",
      "type": "CUSTOM_DECODING_SIGNAL",
      "customDecodingSignal": {
        "id": "Vehicle.CurrentLocation.Longitude"
      }
    },
    {
      "fullyQualifiedName": "Vehicle.CurrentLocation.Latitude",
      "interfaceId": "NAMED_SIGNAL",
      "type": "CUSTOM_DECODING_SIGNAL",
      "customDecodingSignal": {
        "id": "Vehicle.CurrentLocation.Latitude"
      }
    },
    {
        "fullyQualifiedName": "Vehicle.ActivateAC",
        "interfaceId": "AC_ACTUATORS",
        "type": "CUSTOM_DECODING_SIGNAL",
        "customDecodingSignal": {
          "id": "Vehicle.ActivateAC"
        }
    }
]
# Create the decoder manifest.
 CUSTOM_INTERFACE=`cat custom-interface.json`
 CUSTOM_DECODERS=`cat custom-decoders.json`

aws iotfleetwise create-decoder-manifest \
   --name my-decoder-manifest \
   --model-manifest-arn arn:xxx:model-manifest/my-model-manifest \
   --network-interfaces "${CUSTOM_INTERFACE}" \
   --signal-decoders "${CUSTOM_DECODERS}"

 # Activate the decoder manifest.
 aws iotfleetwise update-decoder-manifest \
    --name my-decoder-manifest \
    --status ACTIVE
```

At this point, you have fully modeled these signals in AWS IoT FleetWise. Next you create the vehicle
and associate it with the model you created. You use the `create-vehicle` API
for that:

```
aws iotfleetwise create-vehicle \
    --decoder-manifest-arn arn:xxx:decoder-manifest/my-decoder-manifest \
    --association-behavior ValidateIotThingExists \
    --model-manifest-arn arn:xxx:model-manifest/my-model-manifest \
    --vehicle-name "my-vehicle"
```

The next step is to focus on the AWS IoT FleetWise Edge code base and write the necessary code
extension.

###### Note

For information about the Edge implementation, see the [_Edge Agent Developer Guide_](https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/network-agnostic-dev-guide.md#implementing-your-own-sensors-and-actuators "https://github.com/aws/aws-iot-fleetwise-edge/blob/main/docs/dev-guide/network-agnostic-dev-guide.md#implementing-your-own-sensors-and-actuators").

## Send command

Now, compile the software (make sure you add your headers and C++ files to the CMake
file), and then go back to the cloud APIs to test a command on this actuator:

```
// Create a command targeting your vehicle.
aws iot create-command --command-id activateAC \
    --namespace "AWS-IoT-Fleetwise" \
    --endpoint-url endpoint-url \
    --role-arn ${SERVICE_ROLE_ARN} \
    --mandatory-parameters '[ { "name": "$actuatorPath.Vehicle.ActivateAC", "defaultValue": {"B": "false"} } ]' \
// You will receive the command ARN.

{
    "commandId": "activateAC",
    "commandArn": "arn:aws:iot:xxx:command/activateAC"
}

// You can send the command to activate the AC targeting your vehicle.

JOBS_ENDPOINT_URL=`aws iot describe-endpoint --endpoint-type iot:Jobs | jq -j .endpointAddress`
aws iot-jobs-data start-command-execution \
    --command-arn arn:aws:iot:xxx:command/activateAC \
    --target-arn arn:xxx:vehicle/my-vehicle \
    --parameters '{ "$actuatorPath.Vehicle.ActivateAC" : {"B": "true"}}' \
    --endpoint-url https://${JOBS_ENDPOINT_URL}
// You will receive the corresponding execution ID.
{
    "executionId": "01HSK4ZH6ME7D43RB2BV8JC51D"
}

// If you have the AWS IoT FleetWise Edge Agent running, you can see the logs.
[AcCommandDispatcher.cpp:26] [setActuatorValue()]:
[Actuator Vehicle.ActivateAC executed successfully for command ID 01HSK4ZH6ME7D43RB2BV8JC51D]
```
