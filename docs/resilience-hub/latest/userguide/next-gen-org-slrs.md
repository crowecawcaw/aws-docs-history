

# Service-Linked Roles
<a name="next-gen-org-slrs"></a>

Service-Linked Roles (`AWSServiceRoleForResilienceHub`) are IAM roles that are automatically created in every member account when you enable trusted access for `resiliencehub.amazonaws.com` from the management account. These roles provide the delegated administrator with read-only cross-account visibility into member account resources without requiring manual IAM configuration.

SLRs are created automatically when a new account joins the organization.

Individual service owners in member accounts still create their own invoker roles for running assessments on their services. The SLR provides cross-account visibility for the DA; it does not replace the invoker role used for discovery and assessment. For invoker role setup, see [Setting up Next generation Resilience Hub](next-gen-setting-up.md).