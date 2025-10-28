# Troubleshooting Organizations issues

Use the following information to help you diagnose and fix common issues that you might encounter when working with Security Lake and AWS Organizations. For
more Organizations troubleshooting topics, see the [Troubleshooting](../../../organizations/latest/userguide/orgs_troubleshoot.md "../../../organizations/latest/userguide/orgs_troubleshoot.md") section
of the _AWS Organizations User Guide_.

## An access denied error occurred when

calling the CreateDataLake operation: Your account must be the delegated
administrator account for an organization or a standalone account.

You may receive this error if you delete the organization that a delegated administrator
account belonged to and then try to use that account to set up Security Lake by using
the Security Lake console or the [CreateDataLake](../APIReference/API_CreateDataLake.md "../APIReference/API_CreateDataLake.md") API.

To resolve the error, use a delegated administrator account from a different organization or a standalone account.
