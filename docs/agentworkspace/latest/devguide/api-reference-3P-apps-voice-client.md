

# Connect Customer SDK Voice API
<a name="api-reference-3P-apps-voice-client"></a>

The Connect Customer SDK provides a `VoiceClient` which serves as an interface that your app in the Connect Customer agent workspace can use to make data requests on voice contacts.

To create a `VoiceClient`, pass it the `provider` that `AmazonConnectApp.init` returns. For details, see [Initialize the Connect Customer SDK in your application for Connect Customer agent workspace](getting-started-initialize-sdk.md). This is the recommended option.

```
import { AmazonConnectApp } from "@amazon-connect/app";
import { VoiceClient } from "@amazon-connect/voice";

const { provider } = AmazonConnectApp.init({
  onCreate: async (event) => {
    // Your app is ready.
  },
});

const voiceClient = new VoiceClient(provider);
```

The constructor argument has the type `ConnectClientConfig`, which is defined as follows:

```
type ConnectClientConfig =
  | AmazonConnectProvider
  | { context: ModuleContext; provider?: AmazonConnectProvider }
  | { provider: AmazonConnectProvider };
```

You can also pass the provider inside an object, for example `new VoiceClient({ provider })`.

Each operation in the following sections lists the permission that it requires under **Permissions required**. Operations that take a `contactId` or a `participantId` also state their requirement under **Contact scope**.

The following sections describe API calls for working with the Voice API.

**Topics**
+ [canResumeParticipant()](3P-apps-voice-requests-canresumeparticipant.md)
+ [canResumeSelf()](3P-apps-voice-requests-canresumeself.md)
+ [conferenceParticipants()](3P-apps-voice-requests-conferenceparticipants.md)
+ [createOutboundCall()](3P-apps-voice-requests-createoutboundcall.md)
+ [getInitialCustomerPhoneNumber()](3P-apps-voice-requests-getinitialcustomerphonenumber.md)
+ [getOutboundCallPermission()](3P-apps-voice-requests-getoutboundcallpermission.md)
+ [holdParticipant()](3P-apps-voice-requests-holdparticipant.md)
+ [holdSelf()](3P-apps-voice-requests-holdself.md)
+ [getVoiceEnhancementMode()](3P-apps-voice-requests-getvoiceenhancementmode.md)
+ [getVoiceEnhancementPaths()](3P-apps-voice-requests-getvoiceenhancementpaths.md)
+ [isParticipantOnHold()](3P-apps-voice-requests-isparticipantonhold.md)
+ [isSelfOnHold()](3P-apps-voice-requests-isselfonhold.md)
+ [listDialableCountries()](3P-apps-voice-requests-listdialablecountries.md)
+ [offCanResumeParticipantChanged()](3P-apps-voice-requests-offcanresumeparticipantchanged.md)
+ [offCanResumeSelfChanged()](3P-apps-voice-requests-offcanresumeselfchanged.md)
+ [offParticipantHold()](3P-apps-voice-requests-offparticipanthold.md)
+ [offParticipantResume()](3P-apps-voice-requests-offparticipantresume.md)
+ [offSelfHold()](3P-apps-voice-requests-offselfhold.md)
+ [offSelfResume()](3P-apps-voice-requests-offselfresume.md)
+ [offVoiceEnhancementModeChanged()](3P-apps-voice-requests-offvoiceenhancementmodechanged.md)
+ [onCanResumeParticipantChanged()](3P-apps-voice-requests-oncanresumeparticipantchanged.md)
+ [onCanResumeSelfChanged()](3P-apps-voice-requests-oncanresumeselfchanged.md)
+ [onParticipantHold()](3P-apps-voice-requests-onparticipanthold.md)
+ [onParticipantResume()](3P-apps-voice-requests-onparticipantresume.md)
+ [onSelfHold()](3P-apps-voice-requests-onselfhold.md)
+ [onSelfResume()](3P-apps-voice-requests-onselfresume.md)
+ [onVoiceEnhancementModeChanged()](3P-apps-voice-requests-onvoiceenhancementmodechanged.md)
+ [resumeParticipant()](3P-apps-voice-requests-resumeparticipant.md)
+ [resumeSelf()](3P-apps-voice-requests-resumeself.md)
+ [setVoiceEnhancementMode()](3P-apps-voice-requests-setvoiceenhancementmode.md)