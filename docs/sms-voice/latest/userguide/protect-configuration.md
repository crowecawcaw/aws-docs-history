# Using protect configurations in AWS End User Messaging SMS

Use protect configurations to control which destination countries AWS End User Messaging SMS can send your
messages to. By controlling which countries you allow messages to be sent to, you can avoid
sending to countries with high message prices or countries you don't operate in. Each
protect configuration contains individual allow and block country rules for SMS, MMS, and
voice. Create separate protect configurations for each messaging use case to improve
detection accuracy. Separating use cases like marketing notifications from login/sign-up
enables more precise risk evaluation. Additionally, when one use case faces AIT, other use
cases continue to deliver messages without any message filtering.

You can use a protect configurations as the _account default_, with a
configuration set, or in the _ProtectConfigurationId_ parameter of the
`SendMediaMessage`, `SendTextMessage`, or
`SendVoiceMessage` commands. When set as an _account
default_, a protect configuration will also affect messages sent through
Amazon SNS, Amazon Cognito and `SendMessages`.

The selection process for the _effective_ protection configuration for
a sending request is as follows:

1. _ProtectConfigurationId_ – If a protection configuration
   is specified in the API request parameters, it will be used.
2. _ConfigurationSetName_ – If no protection configuration
   is specified in the API request parameters, but a configuration set is specified and
   it has an associated protection configuration, then the protection configuration
   associated with this configuration set will be used.
3. _Account default_ – If a protection configuration is not
   specified or available from 1 or 2, the _account default_
   protection configuration will be used.

###### Note

To use a protect configuration with other AWS services to send messages,
like Amazon SNS or Amazon Pinpoint, you need to set your protect configuration as the
_account default_. 4. _None_ – The protect configuration will only be used if
specified in a `SendTextMessage` API request.
A protect configuration can be associated to multiple configuration sets, while a
configuration set can only be associated with one protect configuration. There can only be
one _account default_ protect configuration at any time.

The following example for `SendMediaMessage` has both a configuration set and
protect configuration specified in the command. The protect configuration specified in the
_ProtectConfigurationId_ parameter is used regardless of whether the
configuration set has an associated protect configuration or if there is an
_account default_ protect configuration.

```
aws pinpoint-sms-voice-v2 --region '`us-east-1`' send-media-message --destination-phone-number `+12065550150` --origination-identity `+14255550120` --message-body '`text body`' --media-urls '`s3://s3-bucket/media_file.jpg`' --configuration-set-name `ConfigSetName` --protect-configuration-id `ProtectConfigId`
```

Depending on your use case we recommend the following:

- If you only need one set of country rules for all SMS, MMS, and voice you should
  create a protect configuration and associate it as your account _account
  default_.
  1.  Create a protect configuration by following the directions in [Create a protect configuration in
      AWS End User Messaging SMS](protect-configuration-create.md "protect-configuration-create.md") and set the association as
      _account default_.
  2.  Edit the _Allow_, _Block_,
      _Monitor_, and _Filter_ country
      rules for SMS, MMS, and voice by following the directions in [Change a protect configuration
      country rules in AWS End User Messaging SMS](protect-configuration-edit-countries.md "protect-configuration-edit-countries.md").
  3.  Your _account default_ protect configuration is now
      used for any message you send unless overridden by using the
      _ConfigurationSetName_ or
      _ProtectConfigurationId_.

- If your use case requires more granular controls and event logging you can
  associate the protect configuration with a configuration set.
  1.  If you don't already have a configuration set created then follow the
      directions at [Create a configuration set in AWS End User Messaging SMS](configuration-set-create.md "configuration-set-create.md") and we also recommend you setup an
      event destination to log SMS, MMS, and voice events.
  2.  Create a protect configuration by following the directions in [Create a protect configuration in
      AWS End User Messaging SMS](protect-configuration-create.md "protect-configuration-create.md") and set the association as
      _configuration set_ and choose one or more
      configuration sets.
  3.  Edit the _Allow_, _Block_,
      _Monitor_, and _Filter_ country
      rules for SMS, MMS, and voice by following the directions in [Change a protect configuration
      country rules in AWS End User Messaging SMS](protect-configuration-edit-countries.md "protect-configuration-edit-countries.md").
  4.  To use the protect configuration you need to pass the
      _ConfigurationSetName_ in the of the
      `SendMediaMessage`, `SendTextMessage`, or
      `SendVoiceMessage` commands.

- If your use case requires more granular controls you can create the protect
  configuration and use the protect configuration in the
  _ProtectConfigurationId_ API parameter.
  1.  Create a protect configuration by following the directions in [Create a protect configuration in
      AWS End User Messaging SMS](protect-configuration-create.md "protect-configuration-create.md") and set the association as
      _No association_.
  2.  Edit the _Allow_, _Block_,
      _Monitor_, and _Filter_ country
      rules for SMS, MMS, and voice by following the directions in [Change a protect configuration
      country rules in AWS End User Messaging SMS](protect-configuration-edit-countries.md "protect-configuration-edit-countries.md").
  3.  To use the protect configuration you need to pass the
      _ProtectConfigurationId_ in the of the
      `SendMediaMessage`, `SendTextMessage`, or
      `SendVoiceMessage` commands.

###### Topics

- [Create a protect
  configuration](protect-configuration-create.md "protect-configuration-create.md")
- [Change country
  rules](protect-configuration-edit-countries.md "protect-configuration-edit-countries.md")
- [Change
  association](protect-configuration-edit-association.md "protect-configuration-edit-association.md")
- [Delete a protect configuration](protect-configuration-delete.md "protect-configuration-delete.md")
- [Set up deletion protection](protect-configuration-deletion-protection.md "protect-configuration-deletion-protection.md")
- [Rename a protect configuration](protect-configuration-change-name.md "protect-configuration-change-name.md")
- [Manage tags for a protect configuration](protect-configuration-tags.md "protect-configuration-tags.md")
