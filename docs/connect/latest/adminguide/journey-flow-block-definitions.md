# Journey flow block definitions

Use flow blocks to design customer journeys in the Amazon Connect Flow Designer. Drag blocks
onto the canvas and connect them to define how each journey progresses. The following table lists
all available flow blocks that you can use. Choose any block name in the Block column for more
information.

| Block                                                                                                                             | Description                                                                                  |
| --------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| [Send communication](journey-flow-block-send-communication.md "journey-flow-block-send-communication.md")                         | Sends an outbound communication such as voice, SMS, WhatsApp, or email.                      |
| [Set attributes](journey-flow-block-set-attributes.md "journey-flow-block-set-attributes.md")                                     | Stores key-value pairs for use across a journey.                                             |
| [Check attributes](journey-flow-block-check-attributes.md "journey-flow-block-check-attributes.md")                               | Branches the flow based on comparisons between attribute values.                             |
| [Check communication status](journey-flow-block-check-communication-status.md "journey-flow-block-check-communication-status.md") | Evaluates the delivery or contact status of a previous communication.                        |
| [Distribute by percentage](journey-flow-block-distribute-by-percentage.md "journey-flow-block-distribute-by-percentage.md")       | Routes profiles randomly to branches based on configured percentages (e.g. for A/B testing). |
| [Loop](journey-flow-block-loop.md "journey-flow-block-loop.md")                                                                   | Repeats a branch for a defined number of iterations before continuing.                       |
| [Wait](journey-flow-block-wait.md "journey-flow-block-wait.md")                                                                   | Waits for a specified period of time and optionally for specified events.                    |
| [Custom action](journey-flow-block-custom-action.md "journey-flow-block-custom-action.md")                                        | Invokes an Lambda function and uses returned data in the flow.                               |
| [Customer profiles](journey-flow-block-customer-profiles.md "journey-flow-block-customer-profiles.md")                            | Checks segment membership or attributes from Amazon Connect Customer Profiles.               |
| [End flow](journey-flow-block-end-flow.md "journey-flow-block-end-flow.md")                                                       | Ends the current journey flow.                                                               |
