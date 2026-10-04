

# Setup Voice
<a name="nx-voice"></a>

Voice lets you deliver audio messages to your recipients by placing an automated phone call. AWS End User Messaging converts a text script into speech, so you can reach recipients on mobile phones and landlines without recording audio yourself. Common use cases include spoken one-time passcodes and verification codes, time-sensitive alerts, appointment and payment reminders, and reaching recipients who cannot receive SMS.

You send voice messages with the AWS End User Messaging SMS and Voice v2 API (the `sms-voice` namespace, which you call as `aws pinpoint-sms-voice-v2` on the AWS CLI). The main send operation is `SendVoiceMessage`, which uses Amazon Polly to convert your text script into a voice message and places the call from one of your origination phone numbers.

**Key concepts**


| Concept | Description | 
| --- | --- | 
| Origination phone number | The phone number that a voice call is placed from. You lease a voice-capable phone number and send from it. | 
| Amazon Polly voice | The text-to-speech voice that reads your message. You choose a voice and language, and AWS End User Messaging renders your script as speech with Amazon Polly. | 
| Configuration set | A set of rules applied to the messages you send, including where to send call and delivery events, such as CloudWatch, Amazon SNS, or Amazon Data Firehose. | 
| Sandbox | The restricted environment a new account starts in, where you send only to verified destination numbers while you build and test. You request production access to lift the restrictions. | 

**How this guide is organized**

Use the following table to find where to start.


| Section | What you'll do | Start here if | 
| --- | --- | --- | 
| [How to get set up](nx-voice-get-set-up.md) | Set up a voice-capable origination number, create a configuration set, and send a test voice message. | You are new to voice and want a working test call. | 
| [Send a message](nx-voice-send.md) | Send voice messages from your application, including choosing a voice and language. | You have an origination number and want to send from your own code. | 
| [Scale](nx-voice-scale.md) | Move out of the sandbox, monitor delivery, and manage spending and quotas. | You are sending in production and want to keep it healthy and grow. | 