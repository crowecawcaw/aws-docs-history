

# Security best practices
<a name="session-credentials-security"></a>
+ Use [least-privilege IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) on the role. Grant only the specific actions and resources your application needs.
+ Add `aws:SourceAccount` and `aws:SourceArn` conditions in your trust policy to limit which accounts and sessions can assume the role. For more information, see [Cross-service confused deputy prevention](https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html) in the *IAM User Guide*.
+ Monitor usage with CloudTrail. The `RoleSessionName` identifies the exact stream session that made each API call. See [Auditing with CloudTrail](session-credentials-cloudtrail.md).