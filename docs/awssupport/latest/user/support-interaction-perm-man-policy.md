

# Option 1: Use the AWS managed policy (recommended)
<a name="support-interaction-perm-man-policy"></a>

If you currently have the AWSSupportAccess managed policy attached, no additional permissions are required. To continue to use the functions included in the [Support Center Console API](aws-support-console.md), you must have the Support Center Console operations in your IAM policies before November 16, 2026. If you use your own policies instead of AWSSupportAccess, add the `support-console:*` actions to them. For more information, see [Adding IAM policies for the Support Center Console API operations](support-console-access-control.md).