Defect Detection App is in preview release and is subject to change.

# InputConfiguration

Specifies the digital input signal that starts the running of a workflow. For
more information, see [Workflow](api-dt-Workflow.md "api-dt-Workflow.md"). You use an input configuration in a
workflow. For more information, see [Workflow](api-dt-Workflow.md "api-dt-Workflow.md").

## creationTime

The unix timestamp for the creation of the input configuration. Defect Detection App creates this value.

Type: Timestamp

## debounceTime

The time, in milliseconds, that must pass after a signal is received before
a subsequent signal is accepted.

Type: Number

## inputConfigurationId

The ID for the input configuration.

Type: String

## pin

The hardware pin for the signal.

Type: String

## signalType

The type of the signal that triggers the workflow. Possible values are
`GPIO.FALLING` or `GPIO.RISING`.

Type: String

Pattern: `GPIO.FALLING | GPIO.RISING`
