# Opt-out lists in AWS End User Messaging SMS

An _opt-out list_ is list of destination phone numbers that should not
have messages sent to them. When you send SMS messages, destination identities are
automatically added to the opt-out list if they reply to your originator phone number with the
keyword STOP (unless you enable the self-managed opt-out option). If you attempt to send a
message to a destination number that is on an opt-out list, and the opt-out list is
associated with the phone number used to send the message, AWS End User Messaging SMS doesn't attempt to send the
message.

If a phone number is in the opt-out list then the message is not sent, regardless if
there is an [override to allow](protect-rule-override.md#protect-rule-override.title "protect-rule-override.md#protect-rule-override.title") the phone number to receive messages. The phone number has to be removed from the opt-out list for it start receiving messages again.

By default, opt-outs are managed by AWS automatically. You can choose to disable this
automatic opt-out handling by enabling self-managed opt-outs. Your account can contain both
numbers for which opt-outs are managed by AWS, and numbers for which you manage opt-outs
yourself.

###### Topics

- [Required opt-out list keywords](opt-out-list-keywords.md "opt-out-list-keywords.md")
- [Self managed opt-outs](opt-out-list-self-managed.md "opt-out-list-self-managed.md")
- [Set up self managed opt-outs](opt-out-list-managed.md "opt-out-list-managed.md")
- [Create an opt-out list](opt-out-list-create.md "opt-out-list-create.md")
- [View origination identities](opt-out-list-originators.md "opt-out-list-originators.md")
- [View the details of an opt-out list](opt-out-list-view.md "opt-out-list-view.md")
- [Add a destination phone number to an opt-out list](opt-out-list-add-phone-number.md "opt-out-list-add-phone-number.md")
- [Search for a destination phone number](opt-out-list-search.md "opt-out-list-search.md")
- [Remove a destination phone number](opt-out-list-remove-phone-number.md "opt-out-list-remove-phone-number.md")
- [Delete an opt-out list](opt-out-list-delete.md "opt-out-list-delete.md")
- [Manage tags for an opt-out list](opt-out-list-tags.md "opt-out-list-tags.md")
- [List shared opt-out lists](opt-out-list-shared.md "opt-out-list-shared.md")
