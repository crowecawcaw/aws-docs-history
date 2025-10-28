End of support notice: On May 20, 2026, AWS will end support for
AWS IoT Events. After May 20, 2026, you will no longer be able to access the AWS IoT Events console or AWS IoT Events
resources. For more information, see [AWS IoT Events end of
support](iotevents-end-of-support.md "iotevents-end-of-support.md").

# Create a detector model in AWS IoT Events

In this topic, you define a _detector model_ (a model of your equipment
or process) using _states_.

For each state, you define conditional (Boolean) logic that evaluates the incoming inputs
to detect a significant event. When an event is detected, it changes the state and can
initiate additional actions. These events are known as transition events.

In your states, you also define events that can run actions whenever the detector enters
or exits that state or when an input is received (these are known as `OnEnter`,
`OnExit` and `OnInput` events). The actions run only if the event's
conditional logic evaluates to `true`.

###### To create a detector model

1. The first detector state has been created for you. To modify it, select the circle
   with label **State_1** in the main editing space.
2. In the **State** pane, enter the **State name** and
   **OnEnter**, choose **Add event**.
3. On the **Add OnEnter event** page, enter an **Event
   name** and the **Event condition**. In this example, enter
   `true` to indicate the event is always initiated when the
   state
   is entered.
4. Under **Event actions**, choose **Add
   action**.
5. Under **Event actions**, do the following:
   1. Select **Set variable**
   2. For **Variable operation**, choose **Assign
      value**.
   3. For **Variable name**, enter the name of the variable to
      set.
   4. For **Variable value**, enter the value `0`
      (zero).

6. Choose **Save**.

A variable, like the one you defined, can be set (given a value) in any event in the
detector model. The variable's value can only be referenced (for example, in an event's
conditional logic) after the detector has reached a state and run an action where it is
defined or set. 7. In the **State** pane, choose the **X** next to
**State** to return to the **Detector model
palette**. 8. To create a second detector state, in the **Detector model palette**,
choose **State** and drag it into the main editing space. This creates a
state titled `untitled_state_1`. 9. Pause on the first state (**Normal**). An arrow appears on the
circumference of the state. 10. Click and drag the arrow from the first state to the second state. A directed line
from the first state to the second state (labeled **Untitled**)
appears. 11. Select the **Untitled** line. In the **Transition
event** pane, enter an **Event name** and **Event
trigger logic**. 12. In the **Transition event** pane, choose **Add
action**. 13. On the **Add transition event actions** pane, choose **Add
action**. 14. For **Choose an action**, choose **Set variable**.

    1. For **Variable operation**, choose **Assign
     value**.
    2. For **Variable name**, enter the name of the variable.
    3. For **Assign value**, enter the value such as:
     `$variable.pressureThresholdBreached + 3`
    4. Choose **Save**.

15. Select the second state **untitled_state_1**.
16. In the **State** pane, enter the **State name** and
    for **On Enter**, choose **Add event**.
17. On the **Add OnEnter event** page, enter the **Event
    name** and **Event condition**. Choose **Add
    action**.
18. For **Choose an action**, choose **Send SNS
    message**.
    1.  For **SNS topic**, enter the target ARN of your Amazon SNS
        topic.
    2.  Choose **Save**.

19. Continue to add the events in the example.
    1.  For **OnInput**, choose **Add event**, and enter
        and save the following event information.

    ```

      Event name: Overpressurized
      Event condition: $input.PressureInput.sensorData.pressure > 70
      Event actions:
        Set variable:
          Variable operation: Assign value
          Variable name: pressureThresholdBreached
          Assign value: 3
    ```

    2.  For **OnInput**, choose **Add event**, and enter
        and save the following event information.

    ```
      Event name: Pressure Okay
      Event condition: $input.PressureInput.sensorData.pressure <= 70
      Event actions:
        Set variable:
          Variable operation: Decrement
          Variable name: pressureThresholdBreached
    ```

    3.  For **OnExit**, choose **Add event**, and enter
        and save the following event information using the ARN of the Amazon SNS topic that you
        created.

    ```

      Event name: Normal Pressure Restored
      Event condition: true
      Event actions:
        Send SNS message:
          Target arn: `arn:aws:sns:us-east-1:123456789012:pressureClearedAction`
    ```

20. Pause on the second state (**Dangerous**). An arrow appears on
    the circumference of the state
21. Click and drag the arrow from the second state to the first state. A directed line
    with label **Untitled** appears.
22. Choose the **Untitled** line and in the **Transition
    event** pane, enter an **Event name** and **Event
    trigger logic** using the following information.

```
{
  Event name: BackToNormal
  Event trigger logic: $input.PressureInput.sensorData.pressure <= 70 && $variable.pressureThresholdBreached <= 0
}
```

For more information about why we test for the `$input` value and the
`$variable` value in the trigger logic, see the entry for availability of
variable values in [AWS IoT Events detector model restrictions and
limitations](iotevents-restrictions-detector-model.md "iotevents-restrictions-detector-model.md"). 23. Select the **Start** state. By default, this state was created when
you created a detector model). In the **Start** pane, choose the
**Destination state** (for example,
**Normal**). 24. Next, configure your detector model to listen for inputs. In the upper-right corner,
choose **Publish**. 25. On the **Publish detector model** page, do the following.

    1. Enter a **Detector model name**, a
     **Description**, and the name of a **Role**. This
     role is created for you.
    2. Choose **Create a detector for each unique key value**. To create
     and use your own **Role**, follow the steps in [Setting up permissions for AWS IoT Events](iotevents-permissions.md "iotevents-permissions.md") and enter it
     as the **Role** here.

26. For **Detector creation key**, choose the name of one of the
    attributes of the input you defined earlier. The attribute that you choose as the detector
    creation key must be present in each message input, and must be unique to each device that
    sends messages. This example uses the **motorid** attribute.
27. Choose **Save and publish**.

###### Note

The number of unique detectors created for a given detector model is based on the input
messages sent. When a detector model is created, a key is selected from the input
attributes. This key determines which detector instance to use. If the key hasn't been seen
before (for this detector model), a new detector instance is created. If the key has been
seen before, we use the existing detector instance corresponding to this key value.

You can make a backup copy of your detector model definition (in JSON) recreate or update
the detector model or use as a template to create another detector model.

You can do this from the console or by using the following CLI command. If necessary,
change the name of the detector model to match what you used when you published it in the
previous step.

```
aws iotevents describe-detector-model  --detector-model-name motorDetectorModel > motorDetectorModel.json
```

This creates a file (`motorDetectorModel.json`) that has contents
similar to the following.

```
{
    "detectorModel": {
        "detectorModelConfiguration": {
            "status": "ACTIVE",
            "lastUpdateTime": 1552072424.212,
            "roleArn": "arn:aws:iam::123456789012:role/IoTEventsRole",
            "creationTime": 1552072424.212,
            "detectorModelArn": "arn:aws:iotevents:us-west-2:123456789012:detectorModel/motorDetectorModel",
            "key": "motorid",
            "detectorModelName": "motorDetectorModel",
            "detectorModelVersion": "1"
        },
        "detectorModelDefinition": {
            "states": [
                {
                    "onInput": {
                        "transitionEvents": [
                            {
                                "eventName": "Overpressurized",
                                "actions": [
                                    {
                                        "setVariable": {
                                            "variableName": "pressureThresholdBreached",
                                            "value": "$variable.pressureThresholdBreached + 3"
                                        }
                                    }
                                ],
                                "condition": "$input.PressureInput.sensorData.pressure > 70",
                                "nextState": "Dangerous"
                            }
                        ],
                        "events": []
                    },
                    "stateName": "Normal",
                    "onEnter": {
                        "events": [
                            {
                                "eventName": "init",
                                "actions": [
                                    {
                                        "setVariable": {
                                            "variableName": "pressureThresholdBreached",
                                            "value": "0"
                                        }
                                    }
                                ],
                                "condition": "true"
                            }
                        ]
                    },
                    "onExit": {
                        "events": []
                    }
                },
                {
                    "onInput": {
                        "transitionEvents": [
                            {
                                "eventName": "Back to Normal",
                                "actions": [],
                                "condition": "$variable.pressureThresholdBreached <= 1 && $input.PressureInput.sensorData.pressure <= 70",
                                "nextState": "Normal"
                            }
                        ],
                        "events": [
                            {
                                "eventName": "Overpressurized",
                                "actions": [
                                    {
                                        "setVariable": {
                                            "variableName": "pressureThresholdBreached",
                                            "value": "3"
                                        }
                                    }
                                ],
                                "condition": "$input.PressureInput.sensorData.pressure > 70"
                            },
                            {
                                "eventName": "Pressure Okay",
                                "actions": [
                                    {
                                        "setVariable": {
                                            "variableName": "pressureThresholdBreached",
                                            "value": "$variable.pressureThresholdBreached - 1"
                                        }
                                    }
                                ],
                                "condition": "$input.PressureInput.sensorData.pressure <= 70"
                            }
                        ]
                    },
                    "stateName": "Dangerous",
                    "onEnter": {
                        "events": [
                            {
                                "eventName": "Pressure Threshold Breached",
                                "actions": [
                                    {
                                        "sns": {
                                            "targetArn": "arn:aws:sns:us-west-2:123456789012:MyIoTButtonSNSTopic"
                                        }
                                    }
                                ],
                                "condition": "$variable.pressureThresholdBreached > 1"
                            }
                        ]
                    },
                    "onExit": {
                        "events": [
                            {
                                "eventName": "Normal Pressure Restored",
                                "actions": [
                                    {
                                        "sns": {
                                            "targetArn": "arn:aws:sns:us-west-2:123456789012:IoTVirtualButtonTopic"
                                        }
                                    }
                                ],
                                "condition": "true"
                            }
                        ]
                    }
                }
            ],
            "initialStateName": "Normal"
        }
    }
}
```
