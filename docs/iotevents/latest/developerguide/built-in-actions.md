End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Use the AWS IoT Events built-in timer and variable actions

AWS IoT Events supports the following actions that let you use a timer
or set a variable:

- [setTimer](#iotevents-set-timer "#iotevents-set-timer") to create a
  timer.
- [resetTimer](#iotevents-reset-timer "#iotevents-reset-timer") to reset the
  timer.
- [clearTimer](#iotevents-clear-timer "#iotevents-clear-timer") to delete the
  timer.
- [setVariable](#iotevents-set-variable "#iotevents-set-variable") to create a
  variable.

## Set timer action

Set timer action
The `setTimer` action lets you create a timer with duration
in seconds.

More information (2)
When you create a timer, you must specify the following
parameters.

**`timerName`**

The name of the timer.

**`durationExpression`**

(Optional) The duration of the timer, in seconds.

The evaluated result of a duration expression is rounded
down to the nearest whole number. For example, if you set
the timer to 60.99 seconds, the evaluated result of the
duration expression is 60 seconds.

For more information, see [SetTimerAction](../apireference/API_SetTimerAction.md "../apireference/API_SetTimerAction.md") in the
_AWS IoT Events API Reference_.

## Reset timer action

Reset timer action
The `resetTimer` action lets you set the timer to the
previously evaluated result of the duration expression.

More information (1)
When you reset a timer, you must specify the following
parameter.

**`timerName`**

The name of the timer.

AWS IoT Events doesn't reevaluate the duration expression when you
reset the timer.

For more information, see [ResetTimerAction](../apireference/API_ResetTimerAction.md "../apireference/API_ResetTimerAction.md") in the
_AWS IoT Events API Reference_.

## Clear timer action

Clear timer action
The `clearTimer` action lets you delete an existing
timer.

More information (1)
When you delete a timer, you must specify the following
parameter.

**`timerName`**

The name of the timer.

For more information, see [ClearTimerAction](../apireference/API_ClearTimerAction.md "../apireference/API_ClearTimerAction.md") in the
_AWS IoT Events API Reference_.

## Set variable action

Set variable action
The `setVariable` action lets you create a variable with a
specified value.

More information (2)
When you create a variable, you must specify the following
parameters.

**`variableName`**

The name of the variable.

**`value`**

The new value of the variable.

For more information, see [SetVariableAction](../apireference/API_SetVariableAction.md "../apireference/API_SetVariableAction.md") in the
_AWS IoT Events API Reference_.
