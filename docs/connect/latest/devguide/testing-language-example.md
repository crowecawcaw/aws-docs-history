# Example test

The following example demonstrates a JSON string representing the content of a test case configuration. It
illustrates a simple test case that mocks the hours of operation when the test is initiated and then validates
that a welcome prompt is played. Additionally, it simulates a contact's DTMF input to be placed in a queue and
connected to an agent. The test will then verify if the queue placement is correct before concluding the test
case. Overall, this test case configuration consists of three interactions with three simulated actions. Following is
an example of the JSON representation for this test case.

```
{
    "Version": "2019-10-30",
    "Metadata": {},
    "Observations": [
        {
            "Identifier": "TriggerHoursCheck",
            "Event": {
                "Identifier": "evt-hours",
                "Type": "TestInitiated",
                "Actor": "System",
                "Properties": {}
            },
            "Actions": [
                {
                    "Identifier": "ActionId",
                    "Type": "OverrideSystemBehavior",
                    "Parameters": {
                        "ActionType": "OverrideSystemBehavior",
                        "Behavior": {
                            "Type": "FlowAction",
                            "Properties": {
                                "ActionType": "CheckHoursOfOperation",
                                "ActionParameters": {
                                    "HoursOfOperationId": "arn:aws:connect:us-west-2:123456789012:instance/abc123/flow/BasicHours"
                                },
                                "Strategy": {
                                    "Type": "SubstituteResource",
                                    "SubstituteArn": "arn:aws:connect:us-west-2:123456789012:instance/abc123/flow/AlwaysOnHours"
                                }
                            }
                        }
                    },
                    "Transitions": {}
                }
            ],
            "Transitions": {
                "NextObservations": [
                    "Welcome Message"
                ]
            }
        },
        {
            "Identifier": "Welcome Message",
            "Event": {
                "Identifier": "evt-welcome",
                "Type": "MessageReceived",
                "Actor": "System",
                "Properties": {
                    "Text": "Press 1 to be connected to an agent",
                    "MatchingCriteria": { "Type": "Similarity" }
                }
            },
            "Actions": [
                {
                    "Identifier": "Send dtmf input",
                    "Type": "SendInstruction",
                    "Parameters": {
                        "ActionType": "SendInstruction",
                        "Actor": "Customer",
                        "Instruction": {
                            "Type": "DtmfInput",
                            "Properties": {
                                "Value": "1"
                            }
                        }
                    },
                    "Transitions": {}
                }
            ],
            "Transitions": {
                "NextObservations": [
                    "Trigger Queue Announcement"
                ]
            }
        },
        {
            "Identifier": "Trigger Queue Announcement",
            "Event": {
                "Identifier": "evt-queue",
                "Type": "MessageReceived",
                "Actor": "System",
                "Properties": {
                    "Text": "Thank you for calling. Your call is very important to us and will be answered in the order it was received.",
                    "MatchingCriteria": { "Type": "Similarity" }
                }
            },
            "Actions": [
                {
                    "Identifier": "assertqueue",
                    "Type": "Assert",
                    "Parameters": {
                        "Namespace": "$.Queue.Name",
                        "Operator": "Equals",
                        "Operand": "Basic Queue"
                    },
                    "Transitions": {
                        "NextAction": "endthetest"
                    }
                },
                {
                    "Identifier": "endthetest",
                    "Type": "TestControl",
                    "Parameters": {
                        "ActionType": "TestControl",
                        "Command": {
                            "Type": "EndTest"
                        }
                    },
                    "Transitions": {}
                }
            ],
            "Transitions": {
                "NextObservations": []
            }
        }
    ]
}
```
