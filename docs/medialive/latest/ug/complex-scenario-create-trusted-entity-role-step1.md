# Identify the access

requirements

You must identify the services that MediaLive will interact with in your deployment. Then within
each service, you must identify the operations and resources that MediaLive needs access to. Finally,
you must design the IAM policies that handle these requirements.

This requirements analysis must be performed by a person in your organization who
understands your organization's requirements for access to resources. This person must understand
whether there is a requirement that MediaLive channels should be restricted in their access to
resources in other AWS services. For example, this person should determine whether channels
should be restricted in their access to buckets in Amazon S3 so that a specified channel can access
some buckets and not others.

###### To determine the access requirements for MediaLive

1. See the table in [Access requirements for the trusted entity](trusted-entity-requirements.md "trusted-entity-requirements.md") for information about the
   services that MediaLive typically needs access to. Determine which of those services your
   deployment uses and which operations it needs.
2. Within a service, determine the number of policies that you need to create. Do you need
   several different combinations of objects and operations for different workflows, and do you
   need to keep those combinations separate from each for security reasons?

Specifically, determine whether you need access to different resources for different
workflows, and whether it's important to restrict access to specific resources. For example, in
AWS Systems Manager Parameter Store you might have passwords that belong to different workflows, and you
might want to allow only specific users to access the passwords for any given workflow.

If different workflows have different requirements for objects, operations, and resources,
then for that service you need separate policies for each workflow. 3. Design each policy: identify the allowed (or not allowed) objects, operations, and the
allowed (or not allowed) resources in the policy. 4. Determine if any of the policies that you have identified are covered by a managed policy. 5. For each workflow, identify the policies that you need for all the services that the
workflow uses. When you create the policy, you will be able to include several services in the
policy. You don't need to create a policy for each separate service. 6. Identify the number of roles that you need. You need one role for each unique combination
of policies. 7. Assign names to all the policies and roles that you have identified. Make sure that you
don't include sensitive identifying information (such as a customer account name) in these
names.
