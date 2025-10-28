# Edit a keyword in a phone pool

Use the AWS End User Messaging SMS console or AWS CLI to edit keyword responses for your phone pool.

Edit a keyword (Console)
Use the AWS End User Messaging SMS console to edit keywords in your pool.

###### To edit a keyword

1. Open the AWS End User Messaging SMS console at
   [https://console.aws.amazon.com/sms-voice/](https://console.aws.amazon.com/sms-voice/ "https://console.aws.amazon.com/sms-voice/").
2. In the navigation pane, under **Configurations**,
   choose **Phone pools**.
3. On the **Phone Pools** page, choose the pool that
   contains the keyword.
4. On the **Keywords** tab, choose the keyword to
   edit and then **Edit keyword**.
5. In the **Custom Keyword** pane modify any of the
   following:
   - **Keyword** – The keyword to
     edit.
   - **Response message** – The message
     to send back to the recipient.
   - **Keyword action** – The action to
     perform when the keyword is received.

6. Choose **Save keyword**.

Add or edit a keyword (AWS CLI)
You can use the [put-keyword](../../../cli/latest/reference/pinpoint-sms-voice-v2/put-keyword.md "../../../cli/latest/reference/pinpoint-sms-voice-v2/put-keyword.md") command to create a new keyword or edit. If the keyword
already exists then it will be over written.

To create a keyword, run the following command in the AWS CLI:

```
`$` aws pinpoint-sms-voice-v2 put-keyword \
`>` --origination-identity `OriginationIdentity` \
`>` --keyword `Keyword` \
`>` --keyword-message `KeywordMessage` \
`>` --keyword-action `KeywordAction`
```

In the preceding command, make the following changes:

- Replace `OriginationIdentity` with the
  unique ID or Amazon Resource Name (ARN) of the pool that you want to
  add the keyword to.
- Replace `Keyword` with the new
  keyword.
- Replace `KeywordMessage` with the message
  to use when responding to the keyword.
- Replace `KeywordAction` the action
  (`AUTOMATIC_RESPONSE`, `OPT_OUT`,
  `OPT_IN`) to perform when the keyword is
  received.
