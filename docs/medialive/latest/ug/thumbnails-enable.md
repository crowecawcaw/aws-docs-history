# Enabling thumbnails in a channel

You must enable the thumbnails feature in each MediaLivechannel.

You can enable or disable thumbnails only when the channel is idle (not
running).

###### Topics

- [Providing IAM access](#thumbnails-enable-iam "#thumbnails-enable-iam")
- [Enabling thumbnails on the
  console](#thumbnails-enable-console "#thumbnails-enable-console")
- [Enabling thumbnails
  programmatically](#thumbnails-enable-progammatically "#thumbnails-enable-progammatically")

## Providing IAM access

For the thumbnails feature to work, MediaLive needs access to Amazon S3:

- If your organization uses the MediaLiveAccessRole trusted entity, go to
  the **Channel and input details** page of the channel
  configuration, and look in the **General info** section. If
  the **Update role** button appears in this section, select
  the button. If the button doesn't appear, then the trusted entity already
  has the access that it needs
- If your organization uses custom trusted entity roles, then an IAM
  administrator must update the appropriate trusted entity roles. For
  information about the operations to add, read [Access requirements for the trusted entity](trusted-entity-requirements.md "trusted-entity-requirements.md"). Search for
  `thumbnails` on that page. For information about
  how to update the role, see [Create the trusted entity - complex option](setup-trusted-entity-complex.md "setup-trusted-entity-complex.md").

## Enabling thumbnails on the

console

###### Note

This section assumes that you are familiar with creating or editing a channel,
as described in [Creating a channel from scratch](creating-channel-scratch.md "creating-channel-scratch.md").

1. Open the MediaLive console at [https://console.aws.amazon.com/medialive/](https://console.aws.amazon.com/medialive/ "https://console.aws.amazon.com/medialive/").
2. On the **Create channel** page or **Edit
   channel** page, choose **General settings**,
   then open the **Thumbnail configuration** section.
3. Select **Enable thumbnail configuration**. In
   **State**, choose **AUTO** or
   **DISABLED**.

## Enabling thumbnails

programmatically

To enable the thumbnails feature, include the `ThumbnailConfiguration`
group of parameters in the JSON for the channel. Set the `State`
parameter to `AUTO` (to enable) or `DISABLED`.

The following example shows the relative location of the parameters in the JSON
for the channel.

```
{
  "ChannelClass": "SINGLE_PIPELINE",
  .
  .
  .
  "EncoderSettings": {
    .
    .
    .
    "TimecodeConfig": {
      "Source": "EMBEDDED"
    },
    "ThumbnailConfiguration": {
      "State": "DISABLED"
     },
    .
    .
    .
```
