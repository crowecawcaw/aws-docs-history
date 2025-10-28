# Amazon Connect Agent Workspace Voice API

The SDK provides an `VoiceClient` which serves as an interface that your
app in Amazon Connect Agent Workspace can use to make data requests on voice contact.

The `VoiceClient` accepts an optional constructor argument,
`ConnectClientConfig` which itself is defined as:

```

export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};

```

If you do not provide a value for this config, then the client will default to using
the **AmazonConnectProvider** set in the global provider scope. You can
also manually configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```

import { VoiceClient } from "@amazon-connect/voice";

const voiceClient = new VoiceClient();

```

###### Note

For the zero-arg constructor demonstrated above to work correctly, you must first
instantiate the [app](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which will set up the default AmazonConnectProvider. This is the
recommended option.

Alternatively, providing a constructor argument:

```

import { VoiceClient } from "@amazon-connect/voice";

const voiceClient = new VoiceClient({
    context: sampleContext,
    provider: sampleProvider
});

```

The following sections describe API calls for working with the Agent API.

###### Contents

- [createOutboundCall()](3p-apps-voice-requests-createoutboundcall.md "3p-apps-voice-requests-createoutboundcall.md")
- [getInitialCustomerPhoneNumber()](3p-apps-voice-requests-getinitialcustomerphonenumber.md "3p-apps-voice-requests-getinitialcustomerphonenumber.md")
- [getOutboundCallPermission()](3p-apps-voice-requests-getoutboundcallpermission.md "3p-apps-voice-requests-getoutboundcallpermission.md")
- [getPhoneNumber()

* Deprecated](3p-apps-voice-requests-getphonenumber.md "3p-apps-voice-requests-getphonenumber.md")

- [listDialableCountries()](3p-apps-voice-requests-listdialablecountries.md "3p-apps-voice-requests-listdialablecountries.md")
