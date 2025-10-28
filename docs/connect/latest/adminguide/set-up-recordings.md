# Enable contact recording

To enable the recording of voice conversations, you need to add a [Set recording and analytics
behavior](set-recording-behavior.md "set-recording-behavior.md")
block to your flow. You need to do this regardless of whether your Amazon Connect instance is
enabled for multi-party contacts (enhanced contact monitoring) or third-party
contacts.

###### Important

**Chats**: You only need to perform these steps for
chat conversations if [enhanced contact
monitoring for chat contacts](monitor-conversations.md "monitor-conversations.md") is not enabled for your instance. Otherwise,
chat transcripts are automatically recorded because an S3 bucket was created to
store them when you set up your instance. To stop recording chat transcripts, remove
the S3 bucket.

###### To set up recording of conversations

1. Log in to your Amazon Connect instance using an account that has permissions to edit
   flows.
2. On the navigation menu, choose **Routing**,
   **Flows**.

![Amazon Connect navigation menu, Routing, flows.](images/menu-contact-flows.png) 3. Open the flow that handles customer contacts you want to record. 4. In the flow, before the contact is connected to an agent, add a [Set recording and analytics
behavior](set-recording-behavior.md "set-recording-behavior.md") block to the flow. 5. To configure the [Set recording and analytics
behavior](set-recording-behavior.md "set-recording-behavior.md") block, choose from the
following:

    * Automated interaction call recording




    	+ **On** starts recording customer and IVR
    	 audio immediately.
    	+ **Off** pauses any ongoing IVR
    	 recording.
    * Agent and customer voice recording




    	+ When **On**, you can select from Agent and
    	 Customer, Agent only, or Customer only. This only take effect
    	 after the agent joins the call.
    	+ When **Off**, no recording is captured when
    	 the agent joins the call.
    * To record chat conversations, choose **Agent and
     Customer**.


    ###### Important

    You only need to perform these steps for chat conversations if
     [enhanced contact
     monitoring for chat contacts](monitor-conversations.md "monitor-conversations.md") is not enabled for your
     instance. Otherwise, chat transcripts are automatically recorded
     because an S3 bucket was created to store them when you set up your
     instance. To stop recording chat transcripts, remove the S3 bucket.

6. Choose **Save** and then **Publish** to
   publish the updated flow.
7. [Assign security
   profile permissions](assign-permissions-to-review-recordings.md "assign-permissions-to-review-recordings.md") to managers so they can review recordings.
8. Show managers how to access past recordings in Amazon Connect. See [Review recorded
   conversations](review-recorded-conversations.md "review-recorded-conversations.md").

###### To set up recording behavior for outbound calls

1. Create a flow, using the outbound whisper flow type.
2. Add a [Set recording and analytics
   behavior](set-recording-behavior.md "set-recording-behavior.md") block to that flow.
3. Set up a queue that will be used for making outbound calls. In the
   **Outbound whisper flow** box, choose the flow that has
   [Set recording and analytics
   behavior](set-recording-behavior.md "set-recording-behavior.md") in it.

###### To set up human readable logs that contain key interaction points with

Amazon Lex

1. Log in to the Amazon Connect console.
2. On the navigation menu, choose **Flows**.
3. Scroll down the page, choose **Enable Bot Analytics and Transcripts in
   Amazon Connect**, and then choose **Save**.
4. In the Amazon Connect admin website, [assign
   security profile permissions](assign-permissions-to-review-recordings.md#assign-permissions-to-view-automated-recordings-transcripts "assign-permissions-to-review-recordings.md#assign-permissions-to-view-automated-recordings-transcripts") to managers so they can view details of
   the interaction with DTMF menus and Lex bots and/ or additional information
   about flows.
