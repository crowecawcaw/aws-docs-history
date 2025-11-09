# Use AMS SSP to provision Amazon Inspector Classic in your AMS account

###### Note

End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the
Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic will no longer be available to new accounts, and accounts that have not completed an
assessment in the last six months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access
the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see
[Amazon Inspector Classic end of support](../../../inspector/v1/userguide/inspector-migration.md "../../../inspector/v1/userguide/inspector-migration.md").

Use AMS Self-Service Provisioning (SSP) mode to access Amazon Inspector Classic capabilities directly in your AMS managed account. Amazon Inspector Classic is an automated security assessment
service that helps improve the security and compliance of
applications deployed on AWS. Amazon Inspector Classic automatically assesses applications for exposure,
vulnerabilities, and deviations from best practices. After performing an assessment, Amazon Inspector Classic produces a
detailed list of security findings prioritized by level of severity. These findings can be reviewed
directly or as part of detailed assessment reports, which are available via the Amazon Inspector Classic console or API.
To learn more, see [Amazon Inspector Classic](../../../inspector/v1/userguide/inspector_introduction.md "../../../inspector/v1/userguide/inspector_introduction.md").

## Amazon Inspector in AWS Managed Services FAQ

**Q: How do I request access to Amazon Inspector Classic in my AMS account?**

Request access to Amazon Inspector Classic by submitting an RFC with the Management | AWS service | Self-provisioned service
| Add (ct-1w8z66n899dct) change type. This RFC provisions the `customer_inspector_admin_role`
IAM role to your account. The role includes the AWS-managed AmazonInspectorFullAccess policy.
Once provisioned in your account, you must onboard the role in your federation solution.

**Q: What are the restrictions to using Amazon Inspector Classic in my AMS account?**

There are no restrictions. Full functionality of Amazon Inspector Classic is available in your AMS account.

**Q: What are the prerequisites or dependencies to using Amazon Inspector Classic in my AMS account?**

There are no prerequisites or dependencies to use Amazon Inspector Classic in your AMS account.

## Use the new Amazon Inspector in AMS

You can now use the new Amazon Inspector in your AMS account.

For Amazon Inspector Classic, the
`customer-inspector-admin-role-ssm-inspector-agent-policy` and
`AmazonInspectorFullAccess` were required. However, there has been an
update to the SSPS role `customer-inspector-admin-role`, which now
includes an additional `policyAmazonInspector2FullAccess`. This new
policy allows API permissions for the new version of Amazon Inspector.
