# Contain

AWS Security Incident Response partners with you to contain events. You can configure the service to take proactive containment actions in your account in response to security findings. You can also perform containment yourself or in partnership with your third party relationships by using the [SSM documents](../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-runbook-reference.md") described in [Supported Containment Actions.](supported-containment-actions.md "supported-containment-actions.md")

###### Important

AWS Security Incident Response does not enable containment capabilities by default.

Two steps are required to enable proactive containment capabilities:

1. **Grant the necessary permissions** to the service using IAM roles. You can create these roles individually per account or across your entire organization by working with AWS CloudFormation stacksets, which create the required roles.
2. **Define your containment preferences** per account or across your organization to authorize proactive containment actions. Account-level preferences supersede organization-level preferences. This may be done by creating an AWS Support Case (Technical: Security Incident Response Service/Other). The available containment preferences are:
   - **Approval Required (default):** Do not perform proactive containment of any resource without explicit authorization on a case-by-case basis.
   - **Contain Confirmed:** Perform proactive containment of a resource confirmed to be compromised.
   - **Contain Suspected:** Perform proactive containment of a resource with a high likelihood of having been compromised, based on analysis performed by AWS Security Incident Response Engineering.
