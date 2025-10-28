# Requirements for

AWS Elemental MediaConnect

Your deployment might include using a flow from AWS Elemental MediaConnect as an input
to AWS Elemental MediaLive.

Users need permissions to perform actions in MediaConnect when they use the
MediaLive workflow wizard. Users don't need special permissions when they use the
regular MediaLive console to specify a MediaConnect flow in an input or channel.

| Permissions                                                                                                                                                                                           | Service name in IAM | Actions                              |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------- | ------------------------------------ |
| Use the workflow wizard to create a MediaConnect flow, if your organization supports sources from MediaConnect.Use the workflow wizard to delete a workflow that includes a source from MediaConnect. | MediaConnect        | `List*``Describe*``Create*``Delete*` |
