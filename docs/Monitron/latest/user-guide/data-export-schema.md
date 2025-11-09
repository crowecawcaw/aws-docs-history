Amazon Monitron is no longer open to new customers. Existing customers can
continue to use the service as normal. For capabilities similar to Amazon
Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron "https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron").

# Understanding the v1 data export schema

###### Note

Amazon Monitron Kinesis data export schema v1 has been deprecated. Learn more about the
[v2 data export schema](monitron-kinesis-export-v2.md "monitron-kinesis-export-v2.md").

Each measurement data and its corresponding inference result are exported as one
Kinesis data stream record in JSON format.

###### Topics

- [v1 schema format](#data-export-schema-format "#data-export-schema-format")
- [v1 schema parameters](#data-export-schema-parameters "#data-export-schema-parameters")

## v1 schema format

```
{
    "timestamp": "string",
    "eventId": "string",
    "version": "string",
    "projectDisplayName": "string",
    "siteDisplayName": "string",
    "assetDisplayName": "string",
    "sensorPositionDisplayName": "string",
    "sensor": {
        "physicalId": "string",
        "rssi": number
    },
    "gateway": {
        "physicalId": "string"
    },
    "measurement": {
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
                    "resultantVector": {
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
            "temperature": number,
            "velocity": {
                "band10To1000Hz": {
                    "resultantVector": {
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
            }
        },
        "sequenceNo": number
    },
    "models": {
        "temperatureML": {
            "persistentClassificationOutput": "string",
            "pointwiseClassificationOutput": "string"
        },
        "vibrationISO": {
            "isoClass": "string",
            "mutedThreshold": "string",
            "persistentClassificationOutput": "string",
            "pointwiseClassificationOutput": "string"
        },
        "vibrationML": {
            "persistentClassificationOutput": "string",
            "pointwiseClassificationOutput": "string"
        }
    },
    "assetState": {
        "newState": "string",
        "previousState": "string"
    }
}
```

## v1 schema parameters

timestamp

- The timestamp when the measurement is received by Monitron
  service in UTC
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
- Current Value: 1.0

projectDisplayName

- The project name displayed in the App and console
- Type: String

siteDisplayName

- The site name displayed in the App
- Type: String

assetDisplayName

- The asset name displayed in the App
- Type: String

sensorPositionDisplayName

- The sensor position name displayed in the App
- Type: String

sensor.physicalId

- The physical ID of the sensor from which the measurement
  is sent
- Type: String

sensor.rssi

- The sensor bluetooth received signal strength indicator
  value
- Type: Number
- Unit: dBm

gateway.physicalId

- The physical ID of the gateway used to transmit data to
  Amazon Monitron service
- Type: String

measurement.features.acceleration.band0To6000Hz.xAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 0–6000 Hz in the x axis
- Type: Number
- Unit: m/s^2

measurement.features.acceleration.band0To6000Hz.yAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 0–6000 Hz in the y axis
- Type: Number
- Unit: m/s^2

measurement.features.acceleration.band0To6000Hz.zAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 0–6000 Hz in the y axis
- Type: Number
- Unit: m/s^2

measurement.features.acceleration.band10To1000Hz.resultantVector.absMax

- The absolute maximum acceleration observed in the
  frequency band 10–1000 Hz
- Type: Number
- Unit: m/s^2

measurement.features.acceleration.band10To1000Hz.resultantVector.absMin

- The absolute minimum acceleration observed in the
  frequency band 10–1000 Hz
- Type: Number
- Unit: m/s^2

measurement.features.acceleration.band10To1000Hz.resultantVector.crestFactor

- The acceleration crest factor observed in the frequency
  band 10–1000 Hz
- Type: Number

measurement.features.acceleration.band10To1000Hz.resultantVector.rms

- The root mean square of the acceleration observed in the
  frequency band 10–1000 Hz
- Type: Number
- m/s^2

measurement.features.acceleration.band10To1000Hz.xAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 10–1000 Hz in the x axis
- Type: Number
- m/s^2

measurement.features.acceleration.band10To1000Hz.yAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 10–1000 Hz in the y axis
- Type: Number
- m/s^2

measurement.features.acceleration.band10To1000Hz.zAxis.rms

- The root mean square of the acceleration observed in the
  frequency band 10–1000 Hz in the z axis
- Type: Number
- m/s^2

measurement.features.temperature

- The temperature observed
- Type: Number
- °C/degC

measurement.features.velocity.band10To1000Hz.resultantVector.absMax

- The absolute maximum velocity observed in the frequency
  band 10–1000 Hz
- Type: Number
- mm/s

measurement.features.velocity.band10To1000Hz.resultantVector.absMin

- The absolute minimum velocity observed in the frequency
  band 10–1000 Hz
- Type: Number
- mm/s

measurement.features.velocity.band10To1000Hz.resultantVector.crestFactor

- The velocity crest factor observed in the frequency band
  10–1000 Hz
- Type: Number

measurement.features.velocity.band10To1000Hz.resultantVector.rms

- The root mean square of the velocity observed in the
  frequency band 10–1000 Hz
- Type: Number
- mm/s

measurement.features.velocity.band10To1000Hz.xAxis.rms

- The root mean square of the velocity observed in the
  frequency band 10–1000 Hz in the x axis
- Type: Number
- mm/s

measurement.features.velocity.band10To1000Hz.yAxis.rms

- The root mean square of the velocity observed in the
  frequency band 10–1000 Hz in the y axis
- Type: Number
- mm/s

measurement.features.velocity.band10To1000Hz.zAxis.rms

- The root mean square of the velocity observed in the
  frequency band 10–1000 Hz in the z axis
- Type: Number
- mm/s

measurement.sequenceNo

- The measurement sequence number
- Type: Number

models.temperatureML.persistentClassificationOutput

- The persistent classification output from the machine
  learning based temperature model
- Type: Number
- Valid Values: `UNKNOWN | HEALTHY | WARNING |
ALARM`

models.temperatureML.pointwiseClassificationOutput

- The point–wise classification output from the
  machine learning based temperature model
- Type: String
- Valid Values: `UNKNOWN | INITIALIZING | HEALTHY |
WARNING | ALARM`

models.vibrationISO.isoClass

- The ISO 20816 class (a standard for measurement and
  evaluation of machine vibration) used by the ISO based
  vibration model
- Type: String
- Valid Values: `CLASS1 | CLASS2 | CLASS3 | CLASS4 |
FAN_BV2`

models.vibrationISO.mutedThreshold

- The threshold to mute the notification from the ISO based
  vibration model
- Type: String
- Valid Values: `WARNING | ALARM`

models.vibrationISO.persistentClassificationOutput

- The persistent classification output from the ISO based
  vibration model
- Type: String
- Valid Values: `UNKNOWN | HEALTHY | WARNING |
ALARM`

models.vibrationISO.pointwiseClassificationOutput

- The point–wise classification output from the the
  ISO based vibration model
- Type: String
- Valid Values: `UNKNOWN | HEALTHY | WARNING | ALARM |
MUTED_WARNING | MUTED_ALARM`

models.vibrationML.persistentClassificationOutput

- The persistent classification output from the machine
  learning based vibration model
- Type: String
- Valid Values: `UNKNOWN | HEALTHY | WARNING |
ALARM`

models.vibrationML.pointwiseClassificationOutput

- The point–wise classification output from the
  machine learning based vibration model
- Type: String
- Valid Values: `UNKNOWN | INITIALIZING | HEALTHY |
WARNING | ALARM`

assetState.newState

- The machine status after processing the measurement
- Type: String
- Valid Values: `UNKNOWN | HEALTHY | NEEDS_MAINTENANCE
| WARNING | ALARM`

assetState.previousState

- The machine status before processing the
  measurement
- Type: String
- Valid Values: `UNKNOWN | HEALTHY | NEEDS_MAINTENANCE
| WARNING | ALARM`
