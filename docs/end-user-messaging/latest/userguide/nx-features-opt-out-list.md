

# Opt-out lists
<a name="nx-features-opt-out-list"></a>

An *opt-out list* is list of destination phone numbers that should not have messages sent to them. When you send SMS messages, destination identities are automatically added to the opt-out list if they reply to your originator phone number with the keyword STOP (unless you enable the self-managed opt-out option). If you attempt to send a message to a destination number that is on an opt-out list, and the opt-out list is associated with the phone number used to send the message, AWS End User Messaging doesn't attempt to send the message.

If a phone number is in the opt-out list then the message is not sent, regardless if there is an override to allow the phone number to receive messages. The phone number has to be removed from the opt-out list for it start receiving messages again.

By default, opt-outs are managed by AWS automatically. You can choose to disable this automatic opt-out handling by enabling self-managed opt-outs. Your account can contain both numbers for which opt-outs are managed by AWS, and numbers for which you manage opt-outs yourself.

**Topics**
+ [Required opt-out list keywords](nx-features-opt-out-lists-keywords.md)
+ [Self managed opt-outs](nx-features-opt-out-lists-self-managed-about.md)
+ [Set up self managed opt-outs](nx-features-opt-out-lists-self-managed.md)
+ [Create an opt-out list](nx-features-opt-out-lists-create.md)
+ [View the details of an opt-out list](nx-features-opt-out-lists-view.md)
+ [View origination identities](nx-features-opt-out-lists-originators.md)
+ [Add a destination phone number to an opt-out list](nx-features-opt-out-lists-add-number.md)
+ [Search for a destination phone number](nx-features-opt-out-lists-search.md)
+ [Remove a destination phone number](nx-features-opt-out-lists-remove-number.md)
+ [Managing opt-out list phone numbers](nx-features-opt-out-lists-manage-numbers.md)
+ [Delete an opt-out list](nx-features-opt-out-lists-delete.md)
+ [Manage tags for an opt-out list](nx-features-opt-out-lists-tags.md)
+ [List shared opt-out lists](nx-features-opt-out-lists-shared.md)