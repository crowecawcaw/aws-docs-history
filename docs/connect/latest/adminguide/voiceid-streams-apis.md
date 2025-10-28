# Amazon Connect Streams APIs to integrate

Voice ID

###### Note

End of support notice: On May 20, 2026, AWS will end support for Amazon Connect
Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the
Amazon Connect console, access Voice ID features on the Amazon Connect admin website or Contact Control Panel, or access Voice ID
resources. For more information, visit [Amazon Connect
Voice ID end of support](amazonconnect-voiceid-end-of-support.md "amazonconnect-voiceid-end-of-support.md").

Use the following [Amazon Connect
Streams](https://github.com/aws/amazon-connect-streams "https://github.com/aws/amazon-connect-streams") APIs to integrate Voice ID into your existing agent web
applications.

- `enrollSpeakerInVoiceId`: Enroll a customer to Voice ID after
  obtaining their consent to enroll.
- `evaluateSpeakerWithVoiceId`: Check the customer's Voice ID
  authentication status, and to detect fraudsters.
- `optOutVoiceIdSpeaker`: Opt out a customer from
  Voice ID.
- `getVoiceIdSpeakerStatus`: Describe the enrollment status of a
  customer.
- `getVoiceIdSpeakerId`: Get the `SpeakerID` for a
  customer.
- `updateVoiceIdSpeakerId`: Update the `SpeakerID` for
  a customer.
  You can also use the Voice ID widget in the Contact Control Panel (CCP) if you
  don't want to build a custom agent interface. For more information about Voice ID
  in the CCP, see [Enroll callers in Voice ID in the Contact Control Panel
  (CCP)](use-voiceid.md "use-voiceid.md").
