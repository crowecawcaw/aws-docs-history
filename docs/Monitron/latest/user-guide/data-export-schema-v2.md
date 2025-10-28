Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Understanding the v2 data export

schema

Each measurement data, its corresponding inference result, gateway
connect/disconnect, and sensor connect/disconnect events are exported as one Kinesis
data stream record in JSON format.

###### Topics

- [v2 schema format](#data-export-schema-format-v2 "#data-export-schema-format-v2")
- [v2 schema parameters](#data-export-schema-parameters-v2 "#data-export-schema-parameters-v2")

## v2 schema format

```
{
    "timestamp": "string",
    "eventId": "string",
    "version": "2.0",
    "accountId": "string",
    "projectName": "string",
    "projectId": "string",
    "eventType": "measurement|gatewayConnected|gatewayDisconnected|sensorConnected|sensorDisconnected|assetStateTransition",
    // measurement
    "eventPayload": {
        "siteName": "string",
        "assetName": "string",
        "positionName": "string",
        "companyName": "string",
        "geoLocation": {
            "latitude": number,
            "longitude": number
        },
        "address": "string",
        "serialNumber": "string",
        "make": "string",
        "model": "string",
        "assetPositionURL": "string",
        "sensor": {
            "physicalId": "string",
            "rssi": number
        },
        "gateway": {
            "physicalId": "string"
        },
        "sequenceNo": number,
        "features": {
            "acceleration": {
                "band0To6000Hz": {
                    "xAxis": {
                        "rms": number
                    },
                    "yAxis": {
                        "rms": number
                    },
                    "zAxis": {
                        "rms": number
                    }
                },
                "band10To1000Hz": {
                    "totalVibration": {
                        "absMax": number,
                        "absMin": number,
                        "crestFactor": number,
                        "rms": number
                    },
                    "xAxis": {
                        "rms": number
                    },
                    "yAxis": {
                        "rms": number
                    },
                    "zAxis": {
                        "rms": number
                    }
                }
            },
            "velocity": {
                "band10To1000Hz": {
                    "totalVibration": {
                        "absMax": number,
                        "absMin": number,
                        "crestFactor": number,
                        "rms": number
                    },
                    "xAxis": {
                        "rms": number
                    },
                    "yAxis": {
                        "rms": number
                    },
                    "zAxis": {
                        "rms": number
                    }
                }
            },
            "temperature": number
        }
        "models": {
            "temperatureML": {
                "previousPersistentClassificationOutput": "string",
                "persistentClassificationOutput": "string",
                "pointwiseClassificationOutput": "string"
            },
            "vibrationISO": {
                "isoClass": "string",
                "mutedThreshold": "string",
                "previousPersistentClassificationOutput": "string",
                "persistentClassificationOutput": "string",
                "pointwiseClassificationOutput": "string"
            },
            "vibrationML": {
                "previousPersistentClassificationOutput": "string",
                "persistentClassificationOutput": "string",
                "pointwiseClassificationOutput": "string"
            }
        },
        "assetPositionId": "string"
    }

    // sensorConnected
    "eventPayload": {
        "siteName": "string",
        "assetName": "string",
        "positionName": "string",
        "companyName": "string",
        "geoLocation": {
            "latitude": number,
            "longitude": number
        },
        "address": "string",
        "serialNumber": "string",
        "make": "string",
        "model": "string",
        "assetPositionURL": "string",
        "sensor": {
            "physicalId": "string"
        },
        "assetPositionId": "string"
    }

    // sensorDisconnected
    "eventPayload": {
        "siteName": "string",
        "assetName": "string",
        "positionName": "string",
        "companyName": "string",
        "geoLocation": {
            "latitude": number,
            "longitude": number
        },
        "address": "string",
        "serialNumber": "string",
        "make": "string",
        "model": "string",
        "assetPositionURL": "string",
        "sensor": {
            "physicalId": "string"
        },
        "assetPositionId": "string"
    }

    // gatewayConnected
    "eventPayload": {
        "siteName": "string",
        "gatewayName": "string",
        "gatewayListURL": "string",
        "companyName": "string",
        "geoLocation": {
            "latitude": number,
            "longitude": number
        },
        "address": "string",
        "gateway": {
            "physicalId": "string"
        }
    }

    // gatewayDisconnected
    "eventPayload": {
        "siteName": "string",
        "gatewayName": "string",
        "gatewayListURL": "string",
        "companyName": "string",
        "geoLocation": {
            "latitude": number,
            "longitude": number
        },
        "address": "string",
        "gateway": {
            "physicalId": "string"
        }
    }

    // assetStateTransition
    "eventPayload": {
        "siteName": "string",
        "assetName": "string",
        "positionName": "string",
        "companyName": "string",
        "geoLocation": {
            "latitude": number,
            "longitude": number
        },
        "address": "string",
        "serialNumber": "string",
        "make": "string",
        "model": "string",
        "assetPositionURL": "string",
        "sensor": {
            "physicalId": "string"
        },
        "assetTransitionType": "measurement|userInput",
        "assetState": {
            "newState": "string",
            "previousState": "string"
        },
        "closureCode": {
            "failureMode": "string",
            "failureCause": "string",
            "actionTaken": "string",
            "resolvedModels": list<"string">
        },
        "assetPositionId": "string"
    }
}
```

## v2 schema parameters

The Amazon Monitron Kinesis data export schema v2 includes the following schema
parameters. Some parameters are updates from v1 and some are unique to v2. For
example, `siteName` was a first-level parameter in v1. In v2, it is a
second-level parameter that can be found under the `eventPayload`
entity.

timestamp

- The timestamp when the measurement is received by
  Amazon Monitron service in UTC
- Type: String
- Pattern: yyyy-mm-dd hh:mm:ss.SSS

eventId

- The unique data export event ID assigned for each
  measurement. Can be used to deduplicate the Kinesis stream
  records received.
- Type: String

version

- Schema version
- Type: String
- Value: 1.0 or 2.0

accountId

- The 12-digit AWS account ID for your Monitron
  project
- Type: String

projectName

The project name displayed in the app and console.

Type: String

projectId

The unique ID of your Amazon Monitron project.

Type: String

eventType

- The current event stream. Each event type will have a
  dedicated `eventPayload` format.
- Type: String
- Possible values: `measurement`,
  `gatewayConnected`,
  `gatewayDisconnected`,
  `sensorConnected`,
  `sensorDisconnected`,
  `assetStateTransition`.

**`eventType: measurement`**

eventPayload.features.acceleration.band0To6000Hz.xAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 0–6000 Hz in the x axis
- Type: Number
- Unit: m/s^2

eventPayload.features.acceleration.band0To6000Hz.yAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 0–6000 Hz in the y axis
- Type: Number
- Unit: m/s^2

eventPayload.features.acceleration.band0To6000Hz.zAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 0–6000 Hz in the z axis
- Type: Number
- Unit: m/s^2

eventPayload.features.acceleration.band10To1000Hz.resultantVector.absMax

- The absolute maximum acceleration observed in the
  frequency band 10–1000 Hz
- Type: Number
- Unit: m/s^2

eventPayload.features.acceleration.band10To1000Hz.resultantVector.absMin

- The absolute minimum acceleration observed in the
  frequency band 10–1000 Hz
- Type: Number
- Unit: m/s^2

eventPayload.features.acceleration.band10To1000Hz.resultantVector.crestFactor

- The acceleration crest factor observed in the frequency
  band 10–1000 Hz
- Type: Number

eventPayload.features.acceleration.band10To1000Hz.resultantVector.rms

- The root mean square of the acceleration observed in the
  frequency band 10–1000 Hz
- Type: Number
- m/s^2

eventPayload.features.acceleration.band10To1000Hz.xAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 10–1000 Hz in the x axis
- Type: Number
- m/s^2

eventPayload.features.acceleration.band10To1000Hz.yAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 10–1000 Hz in the y axis
- Type: Number
- m/s^2

eventPayload.features.acceleration.band10To1000Hz.zAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 10–1000 Hz in the z axis
- Type: Number
- m/s^2

eventPayload.features.temperature

- The temperature observed
- Type: Number
- °C/degC

eventPayload.features.velocity.band10To1000Hz.resultantVector.absMax

- The absolute maximum velocity observed in the frequency
  band 10–1000 Hz
- Type: Number
- mm/s

eventPayload.features.velocity.band10To1000Hz.resultantVector.absMin

- The absolute minimum velocity observed in the frequency
  band 10–1000 Hz
- Type: Number
- mm/s

eventPayload.features.velocity.band10To1000Hz.resultantVector.crestFactor

- The velocity crest factor observed in the frequency band
  10–1000 Hz
- Type: Number

eventPayload.features.velocity.band10To1000Hz.resultantVector.rms

- The root mean square of the velocity observed in the
  frequency band 10–1000 Hz
- Type: Number
- mm/s

eventPayload.features.velocity.band10To1000Hz.xAxis.rms

- The root mean square of the velocity observed in the
  frequency band 10–1000 Hz in the x axis
- Type: Number
- mm/s

eventPayload.features.velocity.band10To1000Hz.yAxis.rms

- The root mean square of the velocity observed in the
  frequency band 10–1000 Hz in the y axis
- Type: Number
- mm/s

eventPayload.features.velocity.band10To1000Hz.zAxis.rms

- The root mean square of the velocity observed in the
  frequency band 10–1000 Hz in the z axis
- Type: Number
- mm/s

eventPayload.sequenceNo

- The measurement sequence number
- Type: Number

eventPayload.assetPositionId

- The identifier of the sensor position for which the measurement is sent.
- Type: String

eventPayload.companyName

- The name of the company using the asset.
- Type: String

eventPayload.geoLocation.latitude

- The latitude of the site's physical location.
- Type: Number

eventPayload.geoLocation.longitude

- The longitude of the site's physical location.
- Type: Number

eventPayload.address

- The address of the site.
- Type: String

eventPayload.serialNumber

- The serial number of the asset.
- Type: String

eventPayload.make

- The make of the asset.
- Type: String

eventPayload.model

- The model of the asset.
- Type: String

`**eventType: sensorConnected**`

siteName

- The site name displayed in the app
- Type: String

assetName

- The asset name displayed in the app
- Type: String

positionName

- The sensor position name displayed in the app
- Type: String

assetPositionURL

- The sensor URL displayed in the app
- Type: String

physicalID

- The physical ID of the sensor from which the measurement
  is sent
- Type: String

eventPayload.assetPositionId

- The identifier of the sensor position whose state changed.
- Type: String

eventPayload.companyName

- The name of the company using the asset.
- Type: String

eventPayload.geoLocation.latitude

- The latitude of the site's physical location.
- Type: Number

eventPayload.geoLocation.longitude

- The longitude of the site's physical location.
- Type: Number

eventPayload.address

- The address of the site.
- Type: String

eventPayload.serialNumber

- The serial number of the asset.
- Type: String

eventPayload.make

- The make of the asset.
- Type: String

eventPayload.model

- The model of the asset.
- Type: String

`**eventType: sensorDisconnected**`

siteName

- The site name displayed in the app
- Type: String

assetName

- The asset name displayed in the app
- Type: String

positionName

- The sensor position name displayed in the app
- Type: String

assetPositionURL

- The sensor URL displayed in the app
- Type: String

physicalID

- The physical ID of the sensor from which the measurement
  is sent
- Type: String

eventPayload.assetPositionId

- The identifier of the sensor position whose state changed.
- Type: String

eventPayload.companyName

- The name of the company using the asset.
- Type: String

eventPayload.geoLocation.latitude

- The latitude of the site's physical location.
- Type: Number

eventPayload.geoLocation.longitude

- The longitude of the site's physical location.
- Type: Number

eventPayload.address

- The address of the site.
- Type: String

eventPayload.serialNumber

- The serial number of the asset.
- Type: String

eventPayload.make

- The make of the asset.
- Type: String

eventPayload.model

- The model of the asset.
- Type: String

`**eventType: gatewayConnected**`

eventPayload.siteName

- The site name displayed in the app
- Type: String

eventPayload.gatewayName

- The name of the gateway as displayed in the app
- Type: String

eventPayload.gatewayListURL

- The gateway URL displayed in the app
- Type: String

eventPayload.gateway.physicalID

- The physical ID of the gateway just connected to transmit
  data to the Amazon Monitron service
- Type: String

eventPayload.companyName

- The name of the company using the asset.
- Type: String

eventPayload.geoLocation.latitude

- The latitude of the site's physical location.
- Type: Number

eventPayload.geoLocation.longitude

- The longitude of the site's physical location.
- Type: Number

eventPayload.address

- The address of the site.
- Type: String

`**eventType: gatewayDisconnected**`

siteName

- The site name displayed in the app
- Type: String

gatewayName

- The name of the gateway as displayed in the app
- Type: String

gatewayListURL

- The gateway URL displayed in the app
- Type: String

physicalID

- The physical ID of the gateway just connected to transmit
  data to the Amazon Monitron service
- Type: String

eventPayload.companyName

- The name of the company using the asset.
- Type: String

eventPayload.geoLocation.latitude

- The latitude of the site's physical location.
- Type: Number

eventPayload.geoLocation.longitude

- The longitude of the site's physical location.
- Type: Number

eventPayload.address

- The address of the site.
- Type: String

`**eventType: assetStateTransition**`

eventPayload.siteName

- The site name displayed in the app
- Type: String

eventPayload.assetName

- The asset name displayed in the app
- Type: String

eventPayload.positionName

- The sensor position name displayed in the app
- Type: String

eventPayload.assetPositionURL

- The sensor URL displayed in the app
- Type: String

eventPayload.sensor.physicalID

- The physical ID of the sensor from which the measurement
  is sent
- Type: String

eventPayload.assetTransitionType

- The reason behind the asset state transition
- Type: String
- Possible values: `measurement` or
  `userInput`

eventPayload.assetState.newState

- The new state of the asset
- Type: String

eventPayload.assetState.previousState

- The previous state of the asset
- Type: String

eventPayload.closureCode.failureMode

- The failure mode selected by the user when acknowledging
  this failure
- Type: String
- Possible values: `NO_ISSUE` |
  `BLOCKAGE` | `CAVITATION` |
  `CORROSION` | `DEPOSIT` |
  `IMBALANCE` | `LUBRICATION` |
  `MISALIGNMENT` | `OTHER` |
  `RESONANCE` | `ROTATING_LOOSENESS`
  | `STRUCTURAL_LOOSENESS` | `TRANSMITTED_FAULT` | `UNDETERMINED` eventPayload.closureCode.failureCause <br>• The cause of the failure as selected by the user in the app dropdown when acknowledging a failure. <br>• Type: String <br>• Possible values: `ADMINISTRATION` | `DESIGN` | `FABRICATION` | `MAINTENANCE` | `OPERATION` | `OTHER` | `QUALITY` | `UNDETERMINED` | `WEAR` eventPayload.closureCode.actionTaken <br>• The action taken when closing this anomaly, as selected by the user in the app dropdown. <br>• Type: String <br>• Possible values: `ADJUST` | `CLEAN`
  | `LUBRICATE` | `MODIFY` | `NO_ACTION` | `OTHER` | `OVERHAUL` | `REPLACE` eventPayload.closureCode.resolvedModels <br>• The set of models which called out the issue. <br>• Type: List of Strings <br>• Possible values: `vibrationISO` | `vibrationML` | `temperatureML` eventPayload.assetPositionId <br>• The identifier of the asset position whose state changed. <br>• Type: String models.temperatureML.persistentClassificationOutput <br>• The persistent classification output from the machine learning based temperature model <br>• Type: Number <br>• Valid Values: `UNKNOWN | HEALTHY | WARNING | ALARM` models.temperatureML.pointwiseClassificationOutput <br>• The point–wise classification output from the machine learning based temperature model <br>• Type: String <br>• Valid Values: `UNKNOWN | INITIALIZING | HEALTHY | WARNING | ALARM` models.vibrationISO.isoClass <br>• The ISO 20816 class (a standard for measurement and evaluation of machine vibration) used by the ISO based vibration model <br>• Type: String <br>• Valid Values: `CLASS1 | CLASS2 | CLASS3 | CLASS4` models.vibrationISO.mutedThreshold <br>• The threshold to mute the notification from the ISO based vibration model <br>• Type: String <br>• Valid Values: `WARNING | ALARM` models.vibrationISO.persistentClassificationOutput <br>• The persistent classification output from the ISO based vibration model <br>• Type: String <br>• Valid Values: `UNKNOWN | HEALTHY | WARNING | ALARM` models.vibrationISO.pointwiseClassificationOutput <br>• The point–wise classification output from the the ISO based vibration model <br>• Type: String <br>• Valid Values: `UNKNOWN | HEALTHY | WARNING | ALARM | MUTED_WARNING | MUTED_ALARM` models.vibrationML.persistentClassificationOutput <br>• The persistent classification output from the machine learning based vibration model <br>• Type: String <br>• Valid Values: `UNKNOWN | HEALTHY | WARNING | ALARM` models.vibrationML.pointwiseClassificationOutput <br>• The point–wise classification output from the machine learning based vibration model <br>• Type: String <br>• Valid Values: `UNKNOWN | INITIALIZING | HEALTHY | WARNING | ALARM` assetState.newState <br>• The machine status after processing the measurement <br>• Type: String <br>• Valid Values: `UNKNOWN | HEALTHY | NEEDS_MAINTENANCE
| WARNING | ALARM` assetState.previousState <br>• The machine status before processing the measurement <br>• Type: String <br>• Valid Values: `UNKNOWN | HEALTHY | NEEDS_MAINTENANCE
| WARNING | ALARM` eventPayload.companyName <br>• The name of the company using the asset. <br>• Type: String eventPayload.geoLocation.latitude <br>• The latitude of the site's physical location. <br>• Type: Number eventPayload.geoLocation.longitude <br>• The longitude of the site's physical location. <br>• Type: Number eventPayload.address <br>• The address of the site. <br>• Type: String eventPayload.serialNumber <br>• The serial number of the asset. <br>• Type: String eventPayload.make <br>• The make of the asset. <br>• Type: String eventPayload.model <br>• The model of the asset. <br>• Type: String
