

# Troubleshooting Organizations issues
<a name="securitylake-orgs-troubleshoot"></a>

Use the following information to help you diagnose and fix common issues that you might encounter when working with Security Lake and AWS Organizations. For more Organizations troubleshooting topics, see the [Troubleshooting](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_troubleshoot.html) section of the *AWS Organizations User Guide*.

## An access denied error occurred when calling the CreateDataLake operation: Your account must be the delegated administrator account for an organization or a standalone account.
<a name="securitylake-orgs-delegated-admin-invalid"></a>

You may receive this error if you delete the organization that a delegated administrator account belonged to and then try to use that account to set up Security Lake by using the Security Lake console or the [CreateDataLake](https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CreateDataLake.html) API.

To resolve the error, use a delegated administrator account from a different organization or a standalone account.