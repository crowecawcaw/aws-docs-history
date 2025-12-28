# Amazon Connect Agent Workspace Voice API

The Amazon Connect SDK provides an `VoiceClient` which serves as an interface that your app in the
Amazon Connect agent workspace can use to make data requests on voice contact.

The `VoiceClient` accepts an optional constructor argument, `ConnectClientConfig` which itself is defined as:

```

export type ConnectClientConfig = {
    context?: ModuleContext;
    provider?: AmazonConnectProvider;
};

```

If you do not provide a value for this config, then the client will default to using the **AmazonConnectProvider** set in the global provider scope. You can also manually
configure this using **setGlobalProvider**.

You can instantiate the agent client as follows:

```

import { VoiceClient } from "@amazon-connect/voice";

const voiceClient = new VoiceClient({ provider });

```

###### Note

You must first instantiate the [AmazonConnectApp](getting-started-initialize-sdk.md "getting-started-initialize-sdk.md") which initializes the default AmazonConnectProvider and returns `{ provider }` . This is the recommended option.

Alternatively, providing a constructor argument:

```

import { VoiceClient } from "@amazon-connect/voice";

const voiceClient = new VoiceClient({
    context: sampleContext,
    provider: sampleProvider
});

```

###### Note

Third-party applications must be configured with \* permission in order to utilize the VoiceClient APIs.

The following sections describe API calls for working with the Voice API.

###### Contents

- [canResumeParticipant()](3P-apps-voice-requests-canresumeparticipant.md "3P-apps-voice-requests-canresumeparticipant.md")
- [canResumeSelf()](3P-apps-voice-requests-canresumeself.md "3P-apps-voice-requests-canresumeself.md")
- [conferenceParticipants()](3P-apps-voice-requests-conferenceparticipants.md "3P-apps-voice-requests-conferenceparticipants.md")
- [createOutboundCall()](3P-apps-voice-requests-createoutboundcall.md "3P-apps-voice-requests-createoutboundcall.md")
- [getInitialCustomerPhoneNumber()](3P-apps-voice-requests-getinitialcustomerphonenumber.md "3P-apps-voice-requests-getinitialcustomerphonenumber.md")
- [getOutboundCallPermission()](3P-apps-voice-requests-getoutboundcallpermission.md "3P-apps-voice-requests-getoutboundcallpermission.md")
- [holdParticipant()](3P-apps-voice-requests-holdparticipant.md "3P-apps-voice-requests-holdparticipant.md")
- [getVoiceEnhancementMode()](3P-apps-voice-requests-getvoiceenhancementmode.md "3P-apps-voice-requests-getvoiceenhancementmode.md")
- [getVoiceEnhancementPaths()](3P-apps-voice-requests-getvoiceenhancementpaths.md "3P-apps-voice-requests-getvoiceenhancementpaths.md")
- [isParticipantOnHold()](3P-apps-voice-requests-isparticipantonhold.md "3P-apps-voice-requests-isparticipantonhold.md")
- [listDialableCountries()](3P-apps-voice-requests-listdialablecountries.md "3P-apps-voice-requests-listdialablecountries.md")
- [offCanResumeParticipantChanged()](3P-apps-voice-requests-offcanresumeparticipantchanged.md "3P-apps-voice-requests-offcanresumeparticipantchanged.md")
- [offCanResumeSelfChanged()](3P-apps-voice-requests-offcanresumeselfchanged.md "3P-apps-voice-requests-offcanresumeselfchanged.md")
- [offParticipantHold()](3P-apps-voice-requests-offparticipanthold.md "3P-apps-voice-requests-offparticipanthold.md")
- [offParticipantResume()](3P-apps-voice-requests-offparticipantresume.md "3P-apps-voice-requests-offparticipantresume.md")
- [offSelfHold()](3P-apps-voice-requests-offselfhold.md "3P-apps-voice-requests-offselfhold.md")
- [offSelfResume()](3P-apps-voice-requests-offselfresume.md "3P-apps-voice-requests-offselfresume.md")
- [offVoiceEnhancementModeChanged()](3P-apps-voice-requests-offvoiceenhancementmodechanged.md "3P-apps-voice-requests-offvoiceenhancementmodechanged.md")
- [onCanResumeParticipantChanged()](3P-apps-voice-requests-oncanresumeparticipantchanged.md "3P-apps-voice-requests-oncanresumeparticipantchanged.md")
- [onCanResumeSelfChanged()](3P-apps-voice-requests-oncanresumeselfchanged.md "3P-apps-voice-requests-oncanresumeselfchanged.md")
- [onParticipantHold()](3P-apps-voice-requests-onparticipanthold.md "3P-apps-voice-requests-onparticipanthold.md")
- [onParticipantResume()](3P-apps-voice-requests-onparticipantresume.md "3P-apps-voice-requests-onparticipantresume.md")
- [onSelfHold()](3P-apps-voice-requests-onselfhold.md "3P-apps-voice-requests-onselfhold.md")
- [onSelfResume()](3P-apps-voice-requests-onselfresume.md "3P-apps-voice-requests-onselfresume.md")
- [onVoiceEnhancementModeChanged()](3P-apps-voice-requests-onvoiceenhancementmodechanged.md "3P-apps-voice-requests-onvoiceenhancementmodechanged.md")
- [resumeParticipant()](3P-apps-voice-requests-resumeparticipant.md "3P-apps-voice-requests-resumeparticipant.md")
- [setVoiceEnhancementMode()](3P-apps-voice-requests-setvoiceenhancementmode.md "3P-apps-voice-requests-setvoiceenhancementmode.md")
