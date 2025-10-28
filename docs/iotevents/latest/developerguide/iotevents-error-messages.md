End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Common AWS IoT Events issues and solutions

See the following section to troubleshoot errors and find possible solutions to resolve
issues with AWS IoT Events.

###### Errors

- [Detector model creation errors](#create-detector-model "#create-detector-model")
- [Updates from a deleted detector model](#update-detector-model "#update-detector-model")
- [Action trigger failure (when meeting a condition)](#no-action "#no-action")
- [Action trigger failure (when breeching a threshold)](#trigger-action "#trigger-action")
- [Incorrect state usage](#wrong-state "#wrong-state")
- [Connection message](#connection-aborted-error "#connection-aborted-error")
- [InvalidRequestException message](#invalid-request "#invalid-request")
- [Amazon CloudWatch Logs action.setTimer errors](#cw-logs-timer "#cw-logs-timer")
- [Amazon CloudWatch payload errors](#cw-logs-payload "#cw-logs-payload")
- [Incompatible data types](#troubleshoot-expressions-incompatible-data-types "#troubleshoot-expressions-incompatible-data-types")
- [Failed to send message to AWS IoT Events](#failed-to-send-to-iot-events "#failed-to-send-to-iot-events")

## Detector model creation errors

I get errors when I attempt to create a detector model.

When you create a detector model, you must consider the following
limitations.

- Only one action is allowed in each `action` field.
- The `condition` is required for `transitionEvents`. It's
  optional for `OnEnter`, `OnInput`, and `OnExit` events.
- If the `condition` field is empty, the evaluated result of the condition
  expression is equivalent to `true`.
- The evaluated result of the condition expression should be a Boolean value. If
  the result isn't a Boolean value, it's equivalent to
  `false` and doesn't trigger the `actions`
  or transition to the `nextState` specified in the event.
  For more information, see [AWS IoT Events detector model restrictions and
  limitations](iotevents-restrictions-detector-model.md "iotevents-restrictions-detector-model.md").

## Updates from a deleted detector model

I updated or deleted a detector model a few minutes ago but I'm still getting state
updates from the old detector model through MQTT messages or SNS alerts.

If you update, delete, or recreate a detector model (see [UpdateDetectorModel](../apireference/API_UpdateDetectorModel.md "../apireference/API_UpdateDetectorModel.md")), there is a delay before all detector
instances are deleted and the new model is used. During this time, inputs
might continue to be processed by the instances of the previous version of
the detector model. You might continue to receive alerts defined by the
previous detector model. Wait for at least seven minutes before you recheck
the update or report an error.

## Action trigger failure (when meeting a condition)

The detector fails to trigger an action or transition to a new state when the
condition is met.

Verify that the evaluated result of the detector's conditional expression is a Boolean
value. If the result isn't a Boolean value, it's equivalent to
`false` and doesn't trigger the `action` or
transition to the `nextState` specified in the event. For more
information, see [Conditional
expression syntax](iotevents-conditional-expressions.md "iotevents-conditional-expressions.md").

## Action trigger failure (when breeching a threshold)

The detector doesn't trigger an action or an event transition when the variable in a
conditional expression reaches a specified value.

If you update `setVariable` for `onInput`, `onEnter`,
or `onExit`, the new value isn't used when evaluating any
`condition` during the current processing cycle. Instead, the
original value is used until the current cycle is complete. You can change
this behavior by setting the `evaluationMethod` parameter in the
detector model definition. When `evaluationMethod` is set to
`SERIAL`, variables are updated and event conditions
evaluated in the order that the events are defined. When
`evaluationMethod` is set to `BATCH` (the
default), variables are updated and events performed only after all event
conditions are evaluated.

## Incorrect state usage

The detector enters the wrong states when I attempt to send
messages to inputs by using `BatchPutMessage`.

If you use [BatchPutMessage](../apireference/API_iotevents-data_BatchPutMessage.md "../apireference/API_iotevents-data_BatchPutMessage.md") to
send multiple messages to inputs, the order in which the messages or inputs are processed
isn't guaranteed. To guarantee ordering, send messages one at time and wait each time for
`BatchPutMessage` to acknowledge success.

## Connection message

I get a `('Connection aborted.', error(54,
 'Connection reset by peer'))` error when I attempt to call or invoke an API.

Verify that OpenSSL uses TLS 1.1 or a later version to establish the connection. This
should be the default under most Linux distributions or Windows version 7
and later. Users of macOS might need to upgrade OpenSSL.

## InvalidRequestException message

I get InvalidRequestException when I attempt to call
`CreateDetectorModel` and `UpdateDetectorModel` APIs.

Check the following to help resolve the issue. For more information, see [CreateDetectorModel](../apireference/API_CreateDetectorModel.md "../apireference/API_CreateDetectorModel.md") and [UpdateDetectorModel](../apireference/API_UpdateDetectorModel.md "../apireference/API_UpdateDetectorModel.md").

- Make sure that you don't use both `seconds` and
  `durationExpression` as the parameters of `SetTimerAction` at the
  same time.
- Make sure that your string expression for `durationExpression` is valid.
  The string expression can contain numbers, variables
  (`$variable.<variable-name>`), or input values
  (`$input.<input-name>.<path-to-datum>`).

## Amazon CloudWatch Logs `action.setTimer` errors

You can set up Amazon CloudWatch Logs to monitor AWS IoT Events detector model instances. The following are
common errors generated by AWS IoT Events, when you use `action.setTimer`.

- **Error:** Your duration expression for the timer
  named `<timer-name>` could not be
  evaluated
  to a number.

Make sure that your string expression for
`durationExpression` can be converted to a number. Other data types, such as
Boolean, aren't allowed.

- **Error:** The evaluated result of your duration
  expression for the timer named `<timer-name>` is greater than 31622440. To ensure
  accuracy, make sure that your duration expression refers to a value between
  60‐31622400.

Make sure that the duration of your timer
is less than or equal to 31622400 seconds. The evaluated result of the duration is rounded
down to the nearest whole number.

- **Error:** The evaluated result of your duration
  expression for the timer named `<timer-name>` is less than 60. To ensure accuracy,
  make sure that your duration expression refers to a value between 60‐31622400.

Make sure that the duration of your timer
is greater than or equal to 60 seconds. The evaluated result of the duration is rounded
down to the nearest whole number.

- **Error:** Your duration expression for the timer
  named `<timer-name>` could not be
  evaluated. Check the variable names, input names, and paths to the data to make
  sure that you refer to the existing variables and inputs.

Make sure that your string expression
refers to the existing variables and inputs. The string expression can contain numbers,
variables (`$variable.`variable-name``), and input
 values
 (`$input.`input-name`.`path-to-datum``).

- **Error:** Failed to set the timer named
  `<timer-name>`. Check your duration expression, and try again.

See the [SetTimerAction](../apireference/API_SetTimerAction.md "../apireference/API_SetTimerAction.md") action to ensure
that you specified the correct parameters, and then set the timer again.

For more information, see [Enable Amazon CloudWatch logging
when developing AWS IoT Events detector models](best-practices.md#best-practices-cw-logs "best-practices.md#best-practices-cw-logs").

## Amazon CloudWatch payload errors

You can set up Amazon CloudWatch Logs to monitor AWS IoT Events detector model instances. The following are
common errors and warnings generated by AWS IoT Events, when you configure the action payload.

- **Error:** We couldn't evaluate your expression for the
  action. Make sure that the variable names, input names, and paths to the data refer to the
  existing variables and input values. Also, verify that the size of the payload
  is less than 1 KB, the maximum allowed size of a payload.

Make sure that you enter the correct
variable names, input names, and paths to the data. You might also receive this error
message if the action payload is larger than 1 KB.

- **Error:** We couldn't parse your content expression for
  the payload of `<action-type>`. Enter a content expression with the correct
  syntax.

The content expression can contain strings
(`'`string`'`), variables
(`$variable.`variable-name``), input values
 (`$input.`input-name`.`path-to-datum``),
string concatenations, and strings that contain `${}`.

- **Error:** Your payload expression
  {`expression`} isn't valid. The defined payload type is JSON,
  so you must specify an expression that AWS IoT Events would evaluate to a string.

If the specified payload type is JSON, AWS IoT Events first checks if the service can
evaluate your expression to a string. The evaluated result can't be
a Boolean or number. If the validation fails, you might receive this
error.

- **Warning:** The action was executed, but we
  couldn't evaluate your content expression for the action payload to valid JSON.
  The defined payload type is JSON.

Make sure that AWS IoT Events can evaluate your content expression for the action
payload to valid JSON, if you define the payload type as
`JSON`. AWS IoT Events runs the action even if AWS IoT Events can't
evaluate the content expression to valid JSON.

For more information, see [Enable Amazon CloudWatch logging
when developing AWS IoT Events detector models](best-practices.md#best-practices-cw-logs "best-practices.md#best-practices-cw-logs").

## Incompatible data types

Message: Incompatible data
types [`<inferred-types>`] found for `<reference>` in the following expression:
`<expression>`

You might receive this error for one of the
following reasons:

- The evaluated results of your references are not compatible with other operands in
  your expressions.
- The type of the argument passed to a function is not supported.
  When you use references in expressions, check the following:

- When you use a reference as an operand with one or more operators, make sure that
  all data types that you reference are compatible.

For example, in the following expression, integer `2` is an operand of both the `==`
and `&&` operators. To ensure that the operands are compatible,
`$variable.testVariable + 1` and `$variable.testVariable` must reference an integer or decimal.

In addition, integer `1` is an operand of the `+` operator.
Therefore, `$variable.testVariable` must reference an integer or decimal.

```
‘$variable.testVariable + 1 == 2 && $variable.testVariable’
```

- When you use a reference as an argument passed to a function, make sure that the
  function supports the data types that you reference.

For example, the following
`timeout("`time-name`")` function requires a
string with double quotes as the argument. If you use a reference for the
`timer-name` value, you must reference a string with double
quotes.

```
timeout("`timer-name`")
```

###### Note

For the `convert(`type`, `expression`)` function,
if you use a reference for the `type` value,
the evaluated result of your reference must be `String`, `Decimal`, or `Boolean`.
For more information, see [AWS IoT Events reference for inputs and variables in
expressions](iotevents-expressions.md#expression-reference "iotevents-expressions.md#expression-reference").

## Failed to send message to AWS IoT Events

Message: Failed to send message to Iot Events

You might experience this error for the following reasons:

- The input message payload does not contain the `Input attribute Key`.
- The `Input attribute Key` is not in the same JSON path as specified in the input
  definition.
- The input message does not match with the schema, as defined in the AWS IoT Events input.

###### Note

The data ingestion from other services will also experience failure.

For example in AWS IoT Core, the AWS IoT rule will fail with the following message `Verify the Input Attribute key.`

To resolve this, ensure that the input payload message schema conforms to
the AWS IoT Events Input definition and the `Input attribute Key` location
matches. For more information, see [Create an input for models in AWS IoT Events](create-input-overview.md "create-input-overview.md")
to learn how to define AWS IoT Events Inputs.
