# Troubleshooting Network Access Analyzer

The following error messages are returned by Network Access Analyzer:

**The request failed due to insufficient permissions**

Verify that you have the required permissions. For more information, see
[Required API permissions for
Network Access Analyzer](security_iam_required-API-permissions.md "security_iam_required-API-permissions.md").

**The network configuration is not supported**

Verify that you are using resources that are supported by Network Access Analyzer. For more
information, see [Supported path resources](how-network-access-analyzer-works.md#path-components "how-network-access-analyzer-works.md#path-components").

**The request failed due to modifications in network resources during the analysis.**

You can't update your network while the analysis is running.

**The request failed due to missing component [`component`]**

Verify that the resource ARNs are correct. For more information, see the
[Service Authorization Reference](../../../service-authorization/latest/reference.md "../../../service-authorization/latest/reference.md").

**The request failed due to inaccessible resource [`resource`]**

Verify that you have permission to access the specified resource.

**The request failed due to throttling errors from [`service`]**

Check for other applications or services that are currently consuming
read capacity for the specified service.
