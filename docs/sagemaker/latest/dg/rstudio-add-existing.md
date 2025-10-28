# Add RStudio support to an existing domain

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

If you have added an RStudio License through AWS License Manager, you can create a
new Amazon SageMaker AI domain with support for RStudio on SageMaker AI. If you have an existing domain that
does not support RStudio, you can add RStudio support to that domain without having to
delete and recreate the domain. 

The following topic outlines how to add this support.

## Prerequisites

You must complete the following steps before you update your current domain to add
support for RStudio on SageMaker AI. 

- Install and configure
  [AWS CLI version 2](../../../cli/latest/userguide/install-cliv2.md "../../../cli/latest/userguide/install-cliv2.md")
- Configure the
  [AWS CLI](../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config "../../../cli/latest/userguide/cli-configure-quickstart.md#cli-configure-quickstart-config") with IAM credentials
- Create a domain execution role following the steps in [Create a SageMaker AI Domain with RStudio using the AWS CLI](rstudio-create-cli.md#rstudio-create-cli-domainexecution "rstudio-create-cli.md#rstudio-create-cli-domainexecution"). This domain-level IAM
  role is required by the RStudioServerPro app. The role requires access to
  AWS License Manager for verifying a valid Posit Workbench license and Amazon CloudWatch Logs
  for publishing server logs.
- Bring your RStudio license to AWS License Manager following the
  steps
  in [RStudio
  license](rstudio-license.md "rstudio-license.md").
- (Optional) If you want to use RStudio in `VPCOnly` mode, complete the steps in
  [RStudio in
  VPC-Only](rstudio-network.md "rstudio-network.md").
- Ensure that the security groups you have configured for each [UserProfile](../APIReference/API_CreateUserProfile.md "../APIReference/API_CreateUserProfile.md") in your domain meet the account-level quotas. When configuring
  the default user profile during domain creation, you can use
  the `DefaultUserSettings` parameter of the [CreateDomain](../APIReference/API_CreateDomain.md "../APIReference/API_CreateDomain.md") API to add `SecurityGroups` that are inherited by all
  the user profiles created in the domain. You can also provide additional security
  groups for a specific user as part of the `UserSettings` parameter of
  the [CreateUserProfile](../APIReference/API_CreateUserProfile.md "../APIReference/API_CreateUserProfile.md") API. If you have added security groups this way, you must
  ensure that the total number of security groups per user profile doesn’t exceed the
  maximum quota of 2 in `VPCOnly` mode and 4 in `PublicInternetOnly`
  mode. If the resulting total number of security groups for any user profile exceeds the
  quota, you can combine multiple security groups’ rules into one security group.

## Add RStudio support to an existing domain

After you have completed the prerequisites, you can add RStudio support to your existing
domain. The following steps outline how to update your existing domain to add support
for RStudio.

### Step 1: Delete all apps in the

domain

To add support for RStudio in your domain, SageMaker AI must update the underlying security groups
for all existing user profiles. To complete this, you must delete and recreate all existing
apps in the domain. The following procedure shows how to delete all of the apps.

1. List all of the apps in the domain.

```
aws sagemaker \
   list-apps \
   --domain-id-equals `<DOMAIN_ID>`
```

2. Delete each app for each user profile in the domain.

```
// JupyterServer apps
aws sagemaker \
    delete-app \
    --domain-id `<DOMAIN_ID>` \
    --user-profile-name `<USER_PROFILE>` \
    --app-type JupyterServer \
    --app-name `<APP_NAME>`

// KernelGateway apps
aws sagemaker \
    delete-app \
    --domain-id `<DOMAIN_ID>` \
    --user-profile-name `<USER_PROFILE>` \
    --app-type KernelGateway \
    --app-name `<APP_NAME>`
```

### Step 2 - Update all user profiles with the new

list of security groups

This is a one-time action that you must complete for all of the existing user profiles in
your domain when you have refactored your existing security groups. This prevents you
from hitting the quota for the maximum number of security groups.
The `UpdateUserProfile` API call fails if the user has any apps that are in
[InService](../APIReference/API_DescribeApp.md#sagemaker-DescribeApp-response-Status "../APIReference/API_DescribeApp.md#sagemaker-DescribeApp-response-Status") status. Delete all apps, then call `UpdateUserProfile` API
to update the security groups.

###### Note

The following requirement for `VPCOnly` mode outlined in [Connect Amazon SageMaker Studio Classic Notebooks in a VPC to External Resources](studio-notebooks-and-internet-access.md#studio-notebooks-and-internet-access-vpc-only "studio-notebooks-and-internet-access.md#studio-notebooks-and-internet-access-vpc-only") is no longer
needed when adding RStudio support because `AppSecurityGroupManagement` is
managed by the SageMaker AI service:

“[TCP
traffic within the security group](../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md#sg-rules-other-instances "../../../AWSEC2/latest/UserGuide/security-group-rules-reference.md#sg-rules-other-instances"). This is required for
connectivity between the JupyterServer app and the KernelGateway apps.
You must allow access to at least ports in the range
`8192-65535`.”

```
aws sagemaker \
    update-user-profile \
    --domain-id `<DOMAIN_ID>`\
    --user-profile-name `<USER_PROFILE>` \
    --user-settings "{\"SecurityGroups\": [\"`<SECURITY_GROUP>`\", \"`<SECURITY_GROUP>`\"]}"
```

### Step 3 - Activate RStudio by calling the

UpdateDomain API

1. Call the [UpdateDomain](../APIReference/API_UpdateDomain.md "../APIReference/API_UpdateDomain.md") API to
   add support for RStudio on SageMaker AI. The `defaultusersettings` parameter is only
   needed if you have refactored the default security groups for your user profiles.
   - For `VPCOnly` mode:

   ```
   aws sagemaker \
       update-domain \
       --domain-id `<DOMAIN_ID>` \
       --app-security-group-management Service \
       --domain-settings-for-update RStudioServerProDomainSettingsForUpdate={DomainExecutionRoleArn=`<DOMAIN_EXECUTION_ROLE_ARN>`} \
       --default-user-settings "{\"SecurityGroups\": [\"`<SECURITY_GROUP>`\", \"`<SECURITY_GROUP>`\"]}"
   ```

   - For `PublicInternetOnly` mode:

   ```
   aws sagemaker \
       update-domain \
       --domain-id `<DOMAIN_ID>` \
       --domain-settings-for-update RStudioServerProDomainSettingsForUpdate={DomainExecutionRoleArn=`<DOMAIN_EXECUTION_ROLE_ARN>`} \
       --default-user-settings "{\"SecurityGroups\": [\"`<SECURITY_GROUP>`\", \"`<SECURITY_GROUP>`\"]}"
   ```

2. Verify that the domain status is `InService`. After the domain status
   is `InService`, support for RStudio on SageMaker AI is added.

```
aws sagemaker \
    describe-domain \
    --domain-id `<DOMAIN_ID>`
```

3. Verify that the RStudioServerPro app’s
   status is `InService` using the following command.

```
aws sagemaker list-apps --user-profile-name domain-shared
```

### Step 4 - Add RStudio access for existing

users

As part of the update in Step 3, SageMaker AI marks the RStudio [AccessStatus](../APIReference/API_RStudioServerProAppSettings.md#sagemaker-Type-RStudioServerProAppSettings-AccessStatus "../APIReference/API_RStudioServerProAppSettings.md#sagemaker-Type-RStudioServerProAppSettings-AccessStatus") of all existing user profiles in the domain as
`DISABLED` by default. This prevents exceeding the number of users allowed by
your current license. To add access for existing users, there is a one-time opt-in step.
Perform the opt-in by calling the [UpdateUserProfile](../APIReference/API_UpdateUserProfile.md "../APIReference/API_UpdateUserProfile.md")
API with the following [RStudioServerProAppSettings](../APIReference/API_UserSettings.md#sagemaker-Type-UserSettings-RStudioServerProAppSettings "../APIReference/API_UserSettings.md#sagemaker-Type-UserSettings-RStudioServerProAppSettings"):

- `AccessStatus` = `ENABLED`
- _Optional_ - `UserGroup` = `R_STUDIO_USER` or
  `R_STUDIO_ADMIN`

```
aws sagemaker \
    update-user-profile \
    --domain-id `<DOMAIN_ID>`\
    --user-profile-name `<USER_PROFILE>` \
    --user-settings "{\"RStudioServerProAppSettings\": {\"AccessStatus\": \"ENABLED\"}}"
```

###### Note

By default, the number of
users that can have access to RStudio is 60.

### Step 5 – Deactivate RStudio access for new

users

Unless otherwise specified when calling `UpdateDomain`, RStudio support is added
by default for all new user profiles created after you have added support for RStudio on
SageMaker AI. To deactivate access for a new user profile, you must explicitly set
the `AccessStatus` parameter to `DISABLED` as part of the
`CreateUserProfile` API call. If the `AccessStatus` parameter is not
specified as part of the `CreateUserProfile` API, the default access status is
`ENABLED`.

```
aws sagemaker \
    create-user-profile \
    --domain-id `<DOMAIN_ID>`\
    --user-profile-name `<USER_PROFILE>` \
    --user-settings "{\"RStudioServerProAppSettings\": {\"AccessStatus\": \"DISABLED\"}}"
```
