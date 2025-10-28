# Integrate application with Amazon Connect

Agent Workspace voice data

To integrate your application with voice data from Amazon Connect Agent Workspace, instantiate
the voice client as follows:

```

import { VoiceClient } from "@amazon-connect/voice";
const voiceClient = new VoiceClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must
first instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md")
which will set up the default AmazonConnectProvider. This is the recommended
option.

Alternatively, see the [API reference](api-reference-3p-apps-events-and-requests.md "api-reference-3p-apps-events-and-requests.md") to customize your client’s configuration. Once the voice
client is instantiated, you can use it to make requests.

## Example voice

request

The following voice event and request are non-exhaustive. For a full list of
available voice events and requests, see the [API
reference](api-reference-3p-apps-events-and-requests.md "api-reference-3p-apps-events-and-requests.md").

```

import { VoiceClient } from "@amazon-connect/voice";
import { AppContactScope } from "@amazon-connect/app";

const voiceClient = new VoiceClient();
const phoneNumber = await voiceClient.getPhoneNumber(AppContactScope.CurrentContactId);

console.log(`Got the phone number: ${phoneNumber}`);

```
