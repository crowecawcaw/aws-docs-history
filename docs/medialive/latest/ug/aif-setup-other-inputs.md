# Setting up automatic input failover with RTMP

and RTP inputs

To use RTMP push inputs and RTP inputs with automatic input failover in MediaLive, you
must make sure that the upstream system provides sources in the correct way, and you
must set up the inputs and the channels in a specific way.

###### Note

The information in this section assumes that you are familiar with the general
steps for [creating an input](create-input.md "create-input.md") and [creating a channel](creating-channel-scratch.md "creating-channel-scratch.md").

###### To plan the inputs for the input failover pair

1. Arrange with your upstream system for them to provide you with the appropriate
   number of sources for the content:
   - If you are setting up automatic input failover in a single-input
     channel, you need two sources—one for each input.
   - If you are setting up automatic input failover in a standard channel,
     you need four sources—two for each input.

2. Make sure that the upstream system sets up the paths correctly. The first
   input must have a different network path to MediaLive, compared to the second input.
   MediaLive can't enforce this rule, but the point of automatic input failover is that
   the sources arrive via different paths. If they don't, then when the route
   fails, both inputs will fail, and you will not have achieved resiliency.
3. Make sure that the input type for the sources is the same. For example, two
   RTMP inputs.
4. Make sure that all the sources contain exactly identical video, audio,
   captions, and metadata.

###### To create the inputs for the input failover pair

1. Follow the procedure in [Working with inputs](creating-input.md "creating-input.md") to create one input
   of the appropriate type. For example, one RTMP input.
   - In a standard channel, set up the input with two sources.
   - In a single-pipeline channel, set up the input with one source.
   - Give the input a name such as `primary
input`.

2. Create a second input of the same type. Create the input in the same way as in
   Step 1.

Give the input a name such as `secondary input`.

###### To attach the inputs to the channel

1. In the **Input attachments** section of the **Create
   channel** page, follow the usual procedure to attach the primary
   input. Ignore the **Automatic input failover settings** for
   now.
2. Follow the same procedure to attach the secondary input.
3. In the **Input attachments** section, in the list of input
   attachments, choose the first input you attached.
4. In the **Automatic input failover settings** section, choose
   **Enable automatic input failover settings**. As soon as
   you enable this field, this input is labeled as **Primary** in
   the list of input attachments.
5. For **Secondary input**, choose the secondary input. (When
   you do this, this input is labeled as **Secondary** in the list
   of attachments.)
6. For **Input preference**, choose the desired option. This
   field controls the behavior when MediaLive has switched over to the secondary input
   and then the primary input becomes healthy again.
   - **EQUAL_INPUT_PREFERENCE** – MediaLive remains on
     the secondary input. The primary input continues to be processed, but it
     is not active.
   - **PRIMARY_INPUT_PREFERENCE** – MediaLive switches
     back to the primary input. The primary input becomes the active
     input.

7. For **Failover conditions**, enable the conditions that you
   want MediaLive to use to identify input loss. The fields include help that describes
   how the conditions work.
