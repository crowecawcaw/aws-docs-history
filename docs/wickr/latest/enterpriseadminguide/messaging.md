This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Messaging

The **Messaging** section has the following available features for
users:

- **Send Link Preview:** This allows a user to send or receive previews for
  URLs sent within Wickr. The preview is generated from the sending device. Recipients will not
  connect to the underlying URL until selected.
- **Location Sharing:** Allows users to share a link to their GPS
  coordinates in the app.
- **Map Sharing:** If enabled with **Location Sharing**,
  it will allow a user to send a map with their location. This map can be shared for a
  pre-determined amount of time that will update as the user moves.
- **File Attachment & Voice Memo:** If disabled, users will be unable
  to send attachments or voice memos. This also prevents downloading attachments sent by others
  in rooms, groups, or DMs.
  The **Messaging** section has the following additional features:

- **Secure Shredder:** The Wickr shredder will write random data over any
  RAM and Disk Space used by files opened in the app. This does not apply to files exported, only
  files opened in a preview within the Wickr apps.
- **Bot Read Receipts:** Allows bots to automatically “read” messages in a
  room instead of requiring users to @ the bot for interaction.
- **Image/File Download Size:** By default, it will upload and download the
  file uncompressed. If compression is enabled the apps will attempt to compress the data before
  encrypting and uploading.
- **Auto-Destruct:** This is the default maximum for any message sent
  within the network. Users can adjust to any amount lower than this value.
- **Quick Responses:** Allows administrators to set pre-filled messages
  that users can send by clicking within the app. Each quick response supports up to 8,000
  characters, including formatting and emoji. Only ten are allowed per group.
- **Maximum Upload Size:** This is the default maximum number of bytes
  allowed for an upload within the network.
