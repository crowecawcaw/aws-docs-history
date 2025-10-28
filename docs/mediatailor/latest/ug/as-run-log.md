# "As Run" log for AWS Elemental MediaTailor Channel Assembly

The _As Run_ log, in the CloudWatch `MediaTailor/Channel/AsRunLog`
log group, shows information about programs and ad breaks as they play.

When you create a channel, the As Run log is disabled by default. Using the Console or
the AWS Command Line Interface (AWS CLI), you can enable and disable the As Run log state for each channel
in your account.

When you enable the As Run log, MediaTailor automatically creates a service-linked role that
allows MediaTailor to write and manage the As Run log in your CloudWatch Logs account. For more
information about service-linked roles, see [Using service-linked roles for
MediaTailor](using-service-linked-roles.md "using-service-linked-roles.md").

###### Note

The As Run Log currently only supports the default program. For now it doesn't
support the alternateMedia created by program rules. This means that it currently
does not generate the As Run Log for alternateMedia.

###### Topics

- [Enabling the As Run log](enabling-as-run-log.md "enabling-as-run-log.md")
- [Disabling the As Run log](disabling-as-run-log.md "disabling-as-run-log.md")
