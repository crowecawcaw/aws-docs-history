# Security best practices

- Use [least-privilege
  IAM policies](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") on the role. Grant only the specific actions and resources your
  application needs.
- Add `aws:SourceAccount` and `aws:SourceArn` conditions in your
  trust policy to limit which accounts and sessions can assume the role. For more
  information, see [Cross-service confused deputy
  prevention](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") in the _IAM User Guide_.
- Monitor usage with CloudTrail. The `RoleSessionName` identifies the exact stream
  session that made each API call. See [Auditing with CloudTrail](session-credentials-cloudtrail.md "session-credentials-cloudtrail.md").
