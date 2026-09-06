

# Default customer whisper flow in Connect Customer: play a beep sound
<a name="default-customer-whisper"></a>

This flow uses a [Set whisper flow](set-whisper-flow.md) block to play a message for the customer when the customer and agent are joined. It uses a "beep" sound to notify a customer that their call has been connected to an agent. 

Use the [Set whisper flow](set-whisper-flow.md) block to override or disable the default customer whisper in a voice conversation.

**Important**  
Chat conversations do not include a default whisper. You need to include a [Set whisper flow](set-whisper-flow.md) for default agent or customer whispers to play. For instructions, see [Set the default whisper flow in Connect Customer for a chat conversation](set-default-whisper-flow-for-chat.md).