# Flow block in Amazon Connect: Start media

streaming

This topic defines the flow block for capturing what the customer hears and says
during a contact. You can then analyze this information for training or determining
customer sentiment.

## Description

Captures what the customer hears and says during a contact. You can then perform
analysis on the audio streams to:

- Determine customer sentiment.
- Use the audio for training purposes.
- Identify and flag abusive callers.

## Supported channels

The following table lists how this block routes a contact who is using the
specified channel.

| Channel | Supported?        |
| ------- | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Voice   | Yes               |
| Chat    | No - Error branch |
| Task    | No - Error branch |
| Email   | No - Error branch | ## Flow types You can use this block in the following [flow types](create-contact-flow.md#contact-flow-types "create-contact-flow.md#contact-flow-types"): <br>• Inbound flow <br>• Customer Queue flow <br>• Agent Whisper flow <br>• Customer Whisper flow <br>• Outbound Whisper flow <br>• Transfer to Agent flow <br>• Transfer to Queue flow ## Properties The following image shows the **Properties** page of the **Start media streaming** block. It has two options: start the stream from the customer or to the customer. ![The properties page of the Start media streaming block.](images/start-media-streaming.png) ## Configuration tips <br>• You must enable live media streaming in your instance to successfully capture customer audio. For instructions, see [Set up live media streaming of customer audio in Amazon Connect](customer-voice-streams.md "customer-voice-streams.md"). <br>• Customer audio is captured until a **Stop media streaming** block is invoked, even if the contact is passed to another flow. <br>• You must use a **Stop media streaming** block to stop media streaming. <br>• If this block is triggered during a chat conversation, the contact is routed down the **Error** branch. ## Configured block The following image shows an example of what this block looks like when it is configured. It has the following branches: **Success** and **Error**. ![A configured Start media streaming block.](images/start-media-streaming-configured.png) ## Sample flows Amazon Connect includes a set of sample flows. For instructions that explain how to access the sample flows in the flow designer, see [Sample flows in Amazon Connect](contact-flow-samples.md "contact-flow-samples.md"). Following are topics that describe the sample flows which include this block. [Example flow for testing live media streaming in Amazon Connect](use-media-streams-blocks.md "use-media-streams-blocks.md") |
