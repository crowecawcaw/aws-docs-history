# Known issues for the CloudHSM CLI for AWS CloudHSM

The following issues impact the CloudHSM CLI for AWS CloudHSM.

###### Topics

- [The key-reference filter fails to select session keys](#ki-cli-1 "#ki-cli-1")

## The `key-reference` filter fails to select session keys

Commands that use `key-reference` to filter session (ephemeral) keys fail
with the error `UX000: Ephemeral key is not expected because we cannot build it without
 HSM Connection`.

The [key
set-attribute](cloudhsm_cli-key-set-attribute.md "cloudhsm_cli-key-set-attribute.md") command is not affected and can select session keys by `key-reference`.

- **Workaround:** Use attribute-based filters (such as
  `attr.label`) to select session keys. If multiple session keys share
  identical attributes, use [key
  set-attribute](cloudhsm_cli-key-set-attribute.md "cloudhsm_cli-key-set-attribute.md") with the `key-reference` filter to assign
  unique labels first, then filter by label.
- **Resolution status:** We are working on a fix to enable
  `key-reference` filters for session keys across all applicable CloudHSM CLI
  commands.
