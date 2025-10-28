# Cross-service confused deputy prevention in

Amazon DataZone

The confused deputy problem is a security issue where an entity that doesn't have
permission to perform an action can coerce a more-privileged entity to perform the action.
In AWS, cross-service impersonation can result in the confused deputy problem.
Cross-service impersonation can occur when one service (the calling service) calls another
service (the called service). The calling service can be manipulated to use its permissions
to act on another customer's resources in a way it should not otherwise have permission to
access. To prevent this, AWS provides tools that help you protect your data for all
services with service principals that have been given access to resources in your
account.

We recommend using the aws:SourceAccount global condition context key
in resource policies to limit the permissions that Amazon DataZone gives another service to the
resource. Use aws:SourceAccount if you want to allow
any resource in that account to be associated with the cross-service use.
