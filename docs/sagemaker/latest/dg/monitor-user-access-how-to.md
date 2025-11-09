# Turn on sourceIdentity in CloudTrail logs for SageMaker AI

Studio Classic

With Amazon SageMaker Studio Classic, you can monitor user resource access. However, the
AWS CloudTrail logs for resource access only list the Studio Classic execution IAM
role as the identifier. When a single execution IAM role is shared between several user
profiles, you must use the `sourceIdentity` configuration to get information about
the specific user that accessed the AWS resources.

The following topics explain how to turn on or off the `sourceIdentity`
configuration.

###### Topics

- [Prerequisites](#monitor-user-access-prereq "#monitor-user-access-prereq")
- [Turn on sourceIdentity](#monitor-user-access-enable "#monitor-user-access-enable")
- [Turn off sourceIdentity](#monitor-user-access-disable "#monitor-user-access-disable")

## Prerequisites

- Install and configure the AWS Command Line Interface following the steps in [Installing
  or updating the latest version of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md").
- Ensure that Studio Classic users in your domain don’t have a policy that allows them to
  update or modify the domain.
- To turn on or turn off `sourceIdentity` propagation, all apps in the
  domain must be in the `Stopped` or `Deleted` state. For more
  information about how to stop and shut down apps, see [Shut down and Update Studio Classic
  Apps](studio-tasks-update-apps.md "studio-tasks-update-apps.md").
- If source identity propagation is turned on, all execution roles must have the
  following trust policy permissions: 
  - Any role that the domain's execution role assumes must have
    the `sts:SetSourceIdentity` permission in the trust policy. If this
    permission is missing, your actions fail with `AccessDeniedException` or
    `ValidationError` when you call the job creation API. The following
    example trust policy includes the `sts:SetSourceIdentity`
    permission.

  JSON

  ```
  `{
   "Version":"2012-10-17",
   "Statement": [
   {
   "Effect": "Allow",
   "Principal": {
   "Service": "sagemaker.amazonaws.com"
   },
   "Action": [
   "sts:AssumeRole",
   "sts:SetSourceIdentity"
   ]
   }
   ]
  }`

  ```

  - When you assume a role with another role, called role chaining, do the
    following:
    - Permissions for `sts:SetSourceIdentity` are required in both the
      permissions policy of the principal that is assuming the role, and in the role
      trust policy of the target role. Otherwise, the assume role operation will
      fail.
    - This role chaining can happen in Studio Classic or any other downstream
      service, such as Amazon EMR. For more information about role chaining, see [Roles terms and concepts](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md").

## Turn on sourceIdentity

The ability to propagate the user profile name as the `sourceIdentity` in
Studio Classic is turned off by default.

To enable the ability to propagate the user profile name as the
`sourceIdentity`, use the AWS CLI during domain creation and domain update. This
feature is enabled at the domain level and not at the user profile level.

After you enable this configuration, administrators can view the user profile in the
AWS CloudTrail log for the service accessed. The user profile is given as the
`sourceIdentity` value in the `userIdentity` section. For more
information about using AWS CloudTrail logs with SageMaker AI, see [Log Amazon SageMaker AI
API Calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").

You can use the following code to enable the propagation of the user profile name as the
`sourceIdentity` during domain creation using the `create-domain` API.

```

create-domain
--domain-name <value>
--auth-mode <value>
--default-user-settings <value>
--subnet-ids <value>
--vpc-id <value>
[--tags <value>]
[--app-network-access-type <value>]
[--home-efs-file-system-kms-key-id <value>]
[--kms-key-id <value>]
[--app-security-group-management <value>]
[--domain-settings "ExecutionRoleIdentityConfig=USER_PROFILE_NAME"]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]

```

You can enable the propagation of the user profile name as the
`sourceIdentity` during domain update using the `update-domain`
API.

To update this configuration, all apps in the domain must be in the `Stopped`
or `Deleted` state. For more information about how to stop and shut down apps,
see [Shut
down and Update Studio Classic Apps](studio-tasks-update-apps.md "studio-tasks-update-apps.md").

Use the following code to enable the propagation of the user profile name as the
`sourceIdentity`.

```

update-domain
--domain-id <value>
[--default-user-settings <value>]
[--domain-settings-for-update "ExecutionRoleIdentityConfig=USER_PROFILE_NAME"]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]

```

## Turn off sourceIdentity

You can also turn off the propagation of the user profile name as the
`sourceIdentity` using the AWS CLI. This occurs during domain update by passing
the `ExecutionRoleIdentityConfig=DISABLED` value for
the `--domain-settings-for-update` parameter as part of the
`update-domain` API call.

In the AWS CLI, use the following code to disable the propagation of the user profile name
as the `sourceIdentity`.

```
update-domain
 --domain-id <value>
[--default-user-settings <value>]
[--domain-settings-for-update "ExecutionRoleIdentityConfig=DISABLED"]
[--cli-input-json <value>]
[--generate-cli-skeleton <value>]
```
