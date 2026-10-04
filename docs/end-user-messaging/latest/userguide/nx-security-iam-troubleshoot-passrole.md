

# I am not authorized to perform iam:PassRole
<a name="nx-security-iam-troubleshoot-passrole"></a>

If you receive an error that you are not authorized to perform the `iam:PassRole` action, your policies must be updated to allow you to pass a role to AWS End User Messaging. Some AWS services let you pass an existing role to that service instead of creating a new service role or service-linked role. To do this, you must have permissions to pass the role to the service. Ask your administrator for assistance.