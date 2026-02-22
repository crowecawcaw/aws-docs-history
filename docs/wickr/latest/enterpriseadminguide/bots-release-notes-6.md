This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Bots 6.24 release

The following release notes include information for bots release 6.24. For information on
the release timeline, see [Change log](#bots-release-notes-6.24-change-log "#bots-release-notes-6.24-change-log").

**Platform versions**

|     |      |
| --- | ---- |
| Bot | 6.24 |

**New features:**

- Support for multi-region federation. Enterprise customers can now federate with
  AWS Wickr customers in AWS Canada (Central) and London regions in addition to Northern
  Virginia.
- To improve the health capabilities of Wickr bots, we added the ability to send events
  generated on a bot to an Amazon Simple Notification Service (SNS) topic. This topic can be used to send events to an
  email address or any other endpoint that can subscribe to events pushed to the defined SNS
  topic.
  **Changes, enhancements, and resolved issues:**

- Fixed an issue where Wickr conversations were not being restored correctly for new
  instances of a bot. This issue would present itself if you created a new instance of a bot and
  then tried to send a message from the bot to a secure room or group conversation. The bot would
  not have restored the connection list and would not have a record of the conversation.
- Fixed an issue where the downloading of files from clients in different domains was not
  working for bots. This change will make sure files are downloaded when a bot downloads a file
  from a Wickr client from another federated domain.
- When a bot receives a file with a long file name, approximately 255 characters, it adds
  some information to the file name which may make the file name larger than 255 characters. The
  bot would end up dropping the file in this case, due to operating system limitations. This fix
  will remove any characters at the end of the file name to keep the length under 255
  characters.
  **Improvements:**

The new bot API allows bot developers to set the avatar associated with the bot client.
Details of this API will be defined in the WickrIO documentation.

## Change log

**Change log for 6.24 release and release notes**

| Change          | Description                                           | Date               |
| --------------- | ----------------------------------------------------- | ------------------ |
| Bots update     | Multi-region updates; Send events to Amazon SNS topic | September 29, 2023 |
| Initial release | Initial release of September release notes            | September 13, 2023 |
