# Selecting the SRT connection mode

When you create an SRT output group, you must choose the connection mode for each output. The connection mode determines how MediaLive and the downstream system establish the SRT connection.

The following table compares the two connection modes:

| Characteristic             | Caller mode                                                                | Listener mode                                                                                                                                                                                                                                                  |
| -------------------------- | -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connection initiation      | MediaLive initiates connections to downstream systems                      | Downstream systems initiate connections to MediaLive                                                                                                                                                                                                           |
| MediaLive role             | Caller and sender                                                          | Listener and sender                                                                                                                                                                                                                                            |
| Downstream role            | Listener and receiver                                                      | Caller and receiver                                                                                                                                                                                                                                            |
| Destination configuration  | You specify the downstream system's IP address and port                    | MediaLive allocates IP addresses; you specify the port                                                                                                                                                                                                         |
| Channel security group     | Not required                                                               | Required for channels using Public delivery method (controls which downstream systems can connect). Not required for VPC delivery or MediaLive Anywhere channels; customers must configure their network to allow SRT connections from the caller destination. |
| Use case                   | Push-style delivery where MediaLive connects to known downstream endpoints | Pull-style delivery where downstream systems connect to MediaLive on demand                                                                                                                                                                                    |
| MediaLive Anywhere support | Supported                                                                  | Supported                                                                                                                                                                                                                                                      |

###### Note

You cannot mix connection modes within a single output. Each output must use either caller mode or listener mode for all its destinations.
