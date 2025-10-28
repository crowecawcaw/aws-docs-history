# Required opt-out keywords

Where required by local laws and regulations (such as in the US and Canada), SMS and MMS
recipients can use their devices to opt out by replying to the message with any of the
following:

###### Note

You can add custom keywords to phone numbers and phone pools to opt-out.

- ARRET
- CANCEL
- END
- OPT-OUT
- OPTOUT
- QUIT
- REMOVE
- STOP
- TD
- UNSUBSCRIBE
  To opt out, the recipient must reply to the same phone number that AWS End User Messaging SMS used to
  deliver the message. After opting out, the recipient no longer receives SMS or MMS messages
  from your AWS account.

###### Note

For US toll-free numbers, opt-outs are managed at the carrier level. The only
supported opt-out keyword for a US toll-free number is STOP. You can't add
additional opt-out keywords, or change the response message that your recipients get
when they opt-out. A user can resubscribe by sending a new message to the toll-free
using either UNSTOP or START as the keyword.

To configure allowing a user to resubscribe add the keywords UNSTOP,
START or both to your toll-free number and set the keyword action to `Opt-in`.
