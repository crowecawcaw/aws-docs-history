# Usage implication of voice transfer

configurations

Post voice transfer, your inbound voice usage depends on how your external voice
system transfer flow is configured.

For a call transfer, inbound connect voice usage does not occur in the following
scenarios:

- In the [Transfer to phone
  number](transfer-to-phone-number.md "transfer-to-phone-number.md") block, the **Resume
  flow after disconnect** option is set to
  **No**.
- None of the following are true:
  - [Live Media Streaming](enable-live-media-streams.md "enable-live-media-streams.md")
    is active
  - IVR Recording is active
  - [Amazon Connect Voice ID](enable-voiceid.md "enable-voiceid.md") is active (that
    is, the [Set Voice ID](set-voice-id.md "set-voice-id.md") and [Check Voice ID](check-voice-id.md "check-voice-id.md") blocks are in use, which
    triggers internal KVS streaming)
  - One or more agents are on the call (that is, an Amazon Connect agent is on the
    call and uses a [quick connect](quick-connects.md "quick-connects.md") to
    transfer the call to the voice transfer connector)
