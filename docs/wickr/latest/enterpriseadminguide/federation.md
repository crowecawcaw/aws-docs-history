This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Federation

The **Federation** section has available options for communications
internal to the Enterprise deployment and external communications with other Wickr Enterprise,
or guest users. Federation is available only if a super admin provisions it.

- **Local Federation:** Choose **Edit** next to Local
  Federation to view the available options. Available options are **Disable
  federation**, **Enable federation**, and **Restricted
  federation**.
- **Permitted Networks:** Only shown when restricted federation is enabled.
  Add labels and Network IDs for other local networks within the Enterprise deployment.
- **Global Federation:** This controls external Wickr Enterprise, and
  AWS Wickr network access if Global Federation has been enabled by the super admin. Should not
  be shown if Global Federation is disabled.
- **Allow guest users:** Only shown when global federation is enabled. This
  allows Wickr users in your network and in the selected security group to collaborate with
  Wickr guest users.
