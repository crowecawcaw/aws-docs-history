# Setting Up IVS Private Channels

Amazon Interactive Video Service (IVS) offers customers the ability to create private
channels, allowing customers to restrict their streams by channel or viewer. Customers
control access to video playback by enabling _playback
authorization_ on channels and generating signed JSON Web Tokens (JWTs) for
authorized playback requests.

Requiring playback authorization on a channel is optional. When a viewer tries to watch a
stream, if the channel has authorization enabled, Amazon IVS verifies that the viewer has a
valid playback token in the request. A playback token is a JWT that the Amazon IVS customer
signs (with a playback authorization key) and includes with every playback request for a
channel that has playback authorization enabled.

###### Topics

- [How Session Protection
  Works](private-channels-session-protection.md "private-channels-session-protection.md")
- [Workflow for IVS Private Channels](private-channels-workflow.md "private-channels-workflow.md")
- [Create or Import an IVS Playback
  Key](private-channels-create-key.md "private-channels-create-key.md")
- [Enable Playback Authorization on
  IVS Channels](private-channels-enable-playback-auth.md "private-channels-enable-playback-auth.md")
- [Generate and Sign IVS Playback
  Tokens](private-channels-generate-tokens.md "private-channels-generate-tokens.md")
- [List IVS Playback Keys](private-channels-list-keys.md "private-channels-list-keys.md")
- [Delete IVS Playback Keys](private-channels-delete-keys.md "private-channels-delete-keys.md")
- [Get Information about IVS Playback
  Keys](private-channels-get-info.md "private-channels-get-info.md")
- [Revoke IVS Viewer
  Sessions](private-channels-start-session-revocation.md "private-channels-start-session-revocation.md")
