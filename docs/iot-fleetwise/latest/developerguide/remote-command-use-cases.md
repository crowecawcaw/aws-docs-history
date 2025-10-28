# Command usage scenarios

###### Important

Access to certain AWS IoT FleetWise features is currently gated. For more information, see [AWS Region and feature availability in AWS IoT FleetWise](fleetwise-regions.md "fleetwise-regions.md").

When using the commands feature, you can create and run commands in the
following scenarios:

- You can omit the parameters during creation and specify only the command ID.
  In this case, you need to specify the parameters to be used when running the
  command on the target device.
- You can specify one or more parameters, and configure default values for them
  when creating the command. Providing default values will help protect you from
  sending inaccurate commands.
- You can specify one or more parameters, and configure values for them when
  creating the command. More than one parameter can be provided but only one of
  them will be executed, and the `Name` field of this parameter must
  use the `$actuatorPath` prefix.
  This section provides some usage scenarios for the `CreateCommand` and the
  `StartCommandExecution` API and using the parameters. It also shows you
  some examples of using commands with state templates.

###### Topics

- [Creating a command with no
  parameters](#remote-command-use-case1 "#remote-command-use-case1")
- [Creating a command with default values
  for parameters](#remote-command-use-case2 "#remote-command-use-case2")
- [Creating a command with parameter
  values](#remote-command-use-case3 "#remote-command-use-case3")
- [Using commands with
  state templates](#remote-command-use-cases-templates "#remote-command-use-cases-templates")

## Creating a command with no

parameters

The following use case shows how you can use the `CreateCommand` API or
the `create-command` CLI to create a command with no parameters. When you
create a command, you only need to provide a command ID and a role ARN.

This use case is especially useful in recurrent use cases, such as when you want
to send the same command multiple times to a vehicle. In this case, the command is
not tied to a specific actuator and gives you the flexibility to execute the command
on any actuator. You must specify the parameters at run time instead when executing
the command using the `StartCommandExecution` API or the
`start-command-execution` CLI, which includes the actuators and
physical signal values.

This use case shows how to create a command without any mandatory
parameters input.

```
aws iot create-command \
    --command-id "UserJourney1" \
    --role-arn "arn:aws:iam:`accountId`:role/`FwCommandExecutionRole`" \
    --description "UserJourney1 - No mandatory parameters" \
    --namespace "AWS-IoT-FleetWise"
```

In this first example, the command that was created above allows you to
execute a command on any actuator without restrictions. To set
`actuator1` to a value of 10, run:

```
aws iot-jobs-data start-command-execution \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/UserJourney1 \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/target-vehicle \
    --parameters '{
        "$actuatorPath.Vehicle.actuator1": {"S": "10"}
    }'
```

Similarly, you can run a command that sets `actuator3` to a
value of `true`.

```
aws iot-jobs-data start-command-execution \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/UserJourney1 \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/target-vehicle \
    --parameters '{
        "$actuatorPath.Vehicle.actuator3": {"S": "true"}
    }'
```

## Creating a command with default values

for parameters

This command only allows you to execute a command on the specified actuator.
Providing default values will help protect you from sending inaccurate commands. For
example, a `LockDoor` command that locks and unlocks doors can be
configured with a default value to avoid the command from accidentally unlocking
doors.

This use case is especially useful when you want to send the same command multiple
times and perform different actions on the same actuator, such as locking and
unlocking the doors of a vehicle. If you want to set the actuator to the default
value, then you don't need to pass qny `parameters` to the
`start-command-execution` CLI. If you do specify a different value
for the `parameters` in the `start-command-execution` CLI, it
will override the default value.

The following command shows how to provide a default value for
actuator1.

```
aws iot create-command \
    --command-id "UserJourney2" \
    --namespace "AWS-IoT-FleetWise" \
    --role-arn "arn:aws:iam:`accountId`:role/`FwCommandExecutionRole`" \
    --mandatory-parameters '[
        {
            "name": "$actuatorPath.Vehicle.actuator1",
            "defaultValue": {"S": "0"}
        }
    ]'
```

The command `UserJourney2` allows you to execute a command
without the need to pass an input value during runtime. In this case, the
execution at runtime will use the default values specified during
creation.

```
aws iot-data start-command-execution \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/UserJourney3 \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/target-vehicle
```

You can also pass a different value for the same actuator, actuator1,
during runtime, which will override the default value.

```
aws iot-jobs-data start-command-execution \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/UserJourney3 \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/target-vehicle \
    --parameters '{
        "$actuatorPath.Vehicle.actuator1": {"S": "139"}
    }'
```

## Creating a command with parameter

values

This command only allows you to execute a command on the specified actuator. It
also forces you to set a value for the actuator during runtime.

This use case is especially useful when you want the end user to only perform
certain specified actions on some of the actuators when running it on the
vehicle.

###### Note

You can have more than name-value pairs for the
`mandatory-parameters` input, with default values for some or all
of them. At runtime, you can then determine the parameter that you want to use
when running on the actuator, provided the actuator name uses the
fully-qualified name with the `$actuatorPath.` prefix.

This command only allows you to execute a command on the specified
actuator. It also forces you to set a value for the actuator during
runtime.

```
aws iot create-command \
    --command-id "UserJourney2" \
    --namespace "AWS-IoT-FleetWise" \
    --role-arn "arn:aws:iam:`accountId`:role/`FwCommandExecutionRole`" \
    --mandatory-parameters '[
        {
            "name": "$actuatorPath.Vehicle.actuator1"
        }
    ]'
```

When running the command, in this case, you must specify a value for
actuator1. The command execution shown below will successfully set the value
of `actuator1` to `10`.

```
aws iot-data start-command-execution \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/UserJourney2 \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/target-vehicle \
    --parameters '{
        "$actuatorPath.Vehicle.actuator1": {"S": "10"}
    }'
```

## Using commands with

state templates

You can also use the commands API operations for state data collection and
processing. For example, you can fetch a one-time state snapshot or to activate or
deactivate state templates to start or stop collecting vehicle state data. The
following examples show how to use the commands feature with state templates.
For more information, see [State template operations for data
collection and processing](state-template-api-operations.md "state-template-api-operations.md")

###### Note

The Name field specified as part of the `mandatory-parameters`
input must use the `$stateTemplate` prefix.

This example shows how to use the `create-command` CLI to
activate state templates.

```
aws iot create-command \
    --command-id `<COMMAND_ID>` \
    --display-name "Activate State Template" \
    --namespace AWS-IoT-FleetWise \
    --mandatory-parameters '[
      {
          "name": "$stateTemplate.name"
      },
      {
          "name": "$stateTemplate.operation",
          "defaultValue": {"S": "activate"}
      }
    ]'
```

Similarly, the following command shows an example of how you can use the
`start-command-execution` CLI for state templates.

```
aws iot-data start-command-execution \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/`<COMMAND_ID>` \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/`<VEHICLE_NAME>` \
    --parameters '{
       "$stateTemplate.name": {"S": "ST345"}
    }'
```

The following command creates multiple state templates without default
values for any of the parameters. It forces you to run the command with
these parameters and the values for them.

```
aws iot create-command \
    --command-id `<COMMAND_ID>` \
    --display-name "Activate State Template" \
    --namespace AWS-IoT-FleetWise \
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

The following command shows how you can use the
`start-command-execution` CLI for the example above.

```
aws iot-data start-command-execution \
    --command-arn arn:aws:iot:`region`:`111122223333`:command/`<COMMAND_ID>` \
    --target-arn arn:aws:iot:`region`:`111122223333`:thing/`<VEHICLE_NAME>` \
    --parameters '{
        "$stateTemplate.name": {"S": "ST345"},
        "$stateTemplate.operation": {"S": "activate"},
        "$stateTemplate.deactivateAfterSeconds" : {"L": "120"}
```
