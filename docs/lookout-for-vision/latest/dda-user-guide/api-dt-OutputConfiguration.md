Defect Detection App is in preview release and is subject to change.

# OutputConfiguration

Specifies the output confguration for the workflow that sends a digital signal
to a device. For example, you can specifiy which pin to trigger when the model
detects an anomalous image. You use an output configuration in a workflow. For
more information, see [Workflow](api-dt-Workflow.md "api-dt-Workflow.md").

## creationTime

The unix timestamp for the creation of the input configuration. Defect Detection App creates this value.

Type: Timestamp

## outputConfigurationId

The ID for the output configuration.

Type: String

## pin

The hardware pin that the workflow sends the signal to.

Type: String

## pulseWidth

The amount of time, in millseconds, that the workflow sends the
signal.

Type: Number

## rule

The rule for when the workflow sends the signal. For example, specify
`Anomaly` to send the signal if the model predicts an anomaly
in an image.

Type: String

Pattern: `All | Normal | Anomaly`

## signalType

The type of the signal that the workflow sends. Possible values are
`GPIO.FALLING` or `GPIO.RISING`.

Type: String

Pattern: `GPIO.FALLING | GPIO.RISING`
