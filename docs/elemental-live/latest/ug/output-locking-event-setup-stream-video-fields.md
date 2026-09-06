

# Step 5: Set up the video encodes
<a name="output-locking-event-setup-stream-video-fields"></a>

This section shows how to set up video encode parameters in an event that implements Elemental Live output locking.

**Note**  
This section refers to *pools*. For an explanation of pools, see [Output locking pools](opl-pools.md).

After you have created the output groups and outputs, follow these guidelines to create the video encodes.

Set up the output encodes (video streams) in the usual way:

1. In each output group, create as many outputs as you [planned for that output group](opl-step-get-ready-outputs.md). When you add an output, Elemental Live creates a new stream in the **Streams** section.

1. Set the following fields in the **Video** tab as specified.     
<a name="table-output-locking-event-setup-stream-video-fields"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/elemental-live/latest/ug/output-locking-event-setup-stream-video-fields.html)

1. You can set other fields in the **Video** section, the fields in the **Audio** section, and the fields in the **Captions** tab to suit your workflow. 