

This guide documents the new AWS Wickr administration console, released on March 13, 2025. For documentation on the classic version of the AWS Wickr administration console, see [Classic Administration Guide](https://docs.aws.amazon.com/wickr/latest/adminguide-classic/what-is-wickr.html).

# Data retention data format
<a name="dataretention-data-formats"></a>

The following table lists all data retention output message types.


| msgtype | Type | Description | 
| --- | --- | --- | 
| 1000 | Text message | Standard text message. | 
| 3000 | Verification | Key verification between users. | 
| 4001 | Create room | A new room or group was created. | 
| 4002 | Modify members | Members added or removed. | 
| 4003 | User left | A user voluntarily left a room. | 
| 4004 | Modify room | Room settings or saved items changed. | 
| 4005 | Delete room | A room was permanently deleted. | 
| 4011 | Delete/Recall | A message was deleted or recalled. | 
| 4012 | Attributes | A message was starred or unstarred. | 
| 4014 | Private property | A conversation was pinned or unpinned. | 
| 6000 | File transfer | A file was sent. | 
| 7000 | Call | Voice or video call event. | 
| 8000 | Location | A static location was shared. | 
| 9000 | Edit | Text edit, link preview, or location update. | 
| 9100 | Reaction | Emoji reaction added or removed. | 
| 9200 | Read receipt | A message was marked as read. | 

The following are data retention output examples for different types of messages.

**Topics**
+ [Text message](dataretention-text-message.md)
+ [Text messages with links](dataretention-text-message-links.md)
+ [File transfer messages](dataretention-file-transfer-messages.md)
+ [Verification messages](dataretention-verification-messages.md)
+ [Control messages](dataretention-control-messages.md)
+ [Modify room members message](dataretention-modify-room-members.md)
+ [User left room](dataretention-user-left-room.md)
+ [Modify room parameters message](dataretention-modify-room-parameters.md)
+ [Modify saved item in room](dataretention-modify-saved-item.md)
+ [Delete room message](dataretention-delete-room-message.md)
+ [Delete or recall message](dataretention-delete-recall-message.md)
+ [Message attribute change](dataretention-message-attribute-change.md)
+ [Modify private property](dataretention-modify-private-property.md)
+ [Calling messages](dataretention-calling-messages.md)
+ [Location messages](dataretention-location-messages.md)
+ [Link previews](dataretention-link-previews.md)
+ [Text edit messages](dataretention-text-edit-messages.md)
+ [Reaction messages](dataretention-reaction-messages.md)
+ [Read receipt messages](dataretention-read-receipt-messages.md)