

# Associate a conversational analytics connector with a flow
<a name="associate-contactlens-integration"></a>

After you have [configured](configure-external-voice-system.md) your external SBC to point to the conversational analytics integration connector host, you need to configure how the audio will be processed when it reaches Connect Customer conversational analytics. To do this, you define the audio processing steps in an Connect Customer flow. It specifies what steps the call audio will go through, including invoking conversational analytics.

Complete the following steps to create a flow that enables conversational analytics, and then associate the flow with the conversational analytics connector. This flow will be invoked when the conversational analytics connector receives call audio.

1. In the Connect Customer admin website, create a flow that uses the [Set recording and analytics behavior](set-recording-behavior.md). Configure the block to enable **Agent and customer voice recording**, **speech analytics**, and **Automated interaction call recording**. End the flow with the [End flow / Resume](end-flow-resume.md) block. This configuration is shown in the following image. 

   For a list of blocks you can use in a conversational analytics integration, see [Supported flow blocks for conversational analytics integration](contactlens-integration-supportedflowblocks.md).   
![The properties page of the Set recording behavior and analytics block.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contactlens-connector-setblock.png)

   For detailed instructions, see [Enable conversational analytics](enable-analytics.md).

1. On the navigation menu, choose **Channels**, **conversational analytics connectors**. Choose the conversational analytics integration connector that you want to associate with the flow. In the **Flow name** field, start typing the name of your flow to display a list, and then choose the flow.   
![The Connectors page, a list of available flows.](http://docs.aws.amazon.com/connect/latest/adminguide/images/contactlens-connector-flow.png)