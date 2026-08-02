Amazon Q Business is no longer open to new customers. For capabilities similar to Q Business, explore Amazon Quick. [Learn more](qbusiness-availability-change.md "qbusiness-availability-change.md").

# Downloading images to add to responses (API operations)

If you have implemented your own application with the Amazon Q Business Chat and ChatSync
APIs, you can use the [GetMedia](../api-reference/API_GetMedia.md "../api-reference/API_GetMedia.md") API operation
to download the images to add to chat responses. You can find the `mediaId`
using the Chat, ChatSync and ListMessages API operations. The `mediaId` is
listed in the `textMessageSegments` as part of the source attribution.

###### Note

The `mediaBytes` field in the GetMedia API response contains binary image data that may not require base64 decoding, depending on your implementation.

```
aws qbusiness get-media \
--application-id `app-12345abcde` \
--conversation-id `conv-67890fghij` \
--media-id `media-12345abcde` \
--message-id `msg-67890fghij`

```
