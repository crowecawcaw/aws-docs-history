# `aws:loop` – Iterate over

steps in an automation

This action iterates over a subset of steps in an automation runbook. You can choose a
`do while` or `for each` style loop. To construct a `do
 while` loop, use the `LoopCondition` input parameter. To construct
a `for each` loop, use the `Iterators` and
`IteratorDataType` input parameters. When using an `aws:loop`
action, only specify either the `Iterators` or `LoopCondition`
input parameter. The maximum number of iterations is 100.

The `onCancel` property can only be used for steps defined within a loop.
The `onCancel` property isn't supported for the `aws:loop` action.
The `onFailure` property can be used for an `aws:loop` action,
however it will only be used if an unexpected error occurs causing the step to fail. If
you define `onFailure` properties for the steps within a loop, the
`aws:loop` action inherits those properties and reacts accordingly when a
failure occurs.

###### Examples

The following are examples of how to construct the different types of loop
actions.

do while

```
name: RepeatMyLambdaFunctionUntilOutputIsReturned
action: aws:loop
inputs:
    Steps:
    - name: invokeMyLambda
        action: aws:invokeLambdaFunction
        inputs:
        FunctionName: LambdaFunctionName
        outputs:
        - Name: ShouldRetry
            Selector: $.Retry
            Type: Boolean
    LoopCondition:
        Variable: "{{ invokeMyLambda.ShouldRetry }}"
        BooleanEquals: true
    MaxIterations: 3
```

for each

```
name: stopAllInstancesWithWaitTime
action: aws:loop
inputs:
    Iterators: "{{ DescribeInstancesStep.InstanceIds }}"
    IteratorDataType: "String"
    Steps:
    - name: stopOneInstance
        action: aws:changeInstanceState
        inputs:
        InstanceIds:
            - "{{stopAllInstancesWithWaitTime.CurrentIteratorValue}}"
        CheckStateOnly: false
        DesiredState: stopped
    - name: wait10Seconds
        action: aws:sleep
        inputs:
        Duration: PT10S
```

###### Input

The input is as follows.

Iterators

The list of items for the steps to iterate over. The maximum number of
iterators is 100.

Type: StringList

Required: No

IteratorDataType

An optional parameter to specify the data type of the
`Iterators`. A value for this parameter can be provided along
with the `Iterators` input parameter. If you don’t specify a
value for this parameter and `Iterators`, then you must specify a
value for the `LoopCondition` parameter.

Type: String

Valid values: Boolean | Integer | String | StringMap

Default: String

Required: No

LoopCondition

Consists of a `Variable` and an operator condition to evaluate.
If you don’t specify a value for this parameter, then you must specify
values for the `Iterators` and `IteratorDataType`
parameters. You can use complex operator evaluations by using a combination
of `And`, `Not`, and `Or` operators. The
condition is evaluated after the steps in the loop complete. If the
condition is `true` and the `MaxIterations` value has
not been reached, the steps in the loop run again. The operator conditions
are as follows:

###### String operations

- StringEquals
- EqualsIgnoreCase
- StartsWith
- EndsWith
- Contains

###### Numeric operations

- NumericEquals
- NumericGreater
- NumericLesser
- NumericGreaterOrEquals
- NumericLesser
- NumericLesserOrEquals

###### Boolean operation

- BooleanEquals

Type: StringMap

Required: No

MaxIterations

The maximum number of times the steps in the loop run. Once the value
specified for this input is reached, the loop stops running even if the
`LoopCondition` is still `true` or if there are
objects remaining in the `Iterators` parameter.

Type: Integer

Valid values: 1 - 100

Required: No

Steps

The list of steps to run in the loop. These function like a nested
runbook. Within these steps you can access the current iterator value for a
`for each` loop using the syntax
`{{loopStepName.CurrentIteratorValue}}`. You can also access
an integer value of the current iteration for both loop types using the
syntax `{{loopStepName.CurrentIteration}}`.

Type: List of steps

Required: Yes

###### Output

CurrentIteration

The current loop iteration as an integer. Iteration values start at

1.

Type: Integer

CurrentIteratorValue

The value of the current iterator as a string. This output is only present
in `for each` loops.

Type: String
