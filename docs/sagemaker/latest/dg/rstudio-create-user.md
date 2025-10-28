# Create a user to use RStudio

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

After your RStudio-enabled Amazon SageMaker AI domain is running, you can add user profiles
(UserProfiles) to the domain. The following topics show how to create user profiles that are
authorized to use RStudio, as well as update an existing user profile. For information on how to
delete an RStudio App, UserProfile, or domain, follow the steps in [Delete an
Amazon SageMaker AI domain](gs-studio-delete-domain.md "gs-studio-delete-domain.md").

###### Note

The limit for the total number of UserProfiles in a Amazon SageMaker AI domain is 60.

There are two types of users:

- Unauthorized: This user cannot access the RStudio app.
- Authorized: This user can access the RStudio app and use one of the RStudio license
  seats. By default, a new user is `Authorized` if the domain is enabled for
  RStudio.
  Changing a user's authorization status is only valid from `Unauthorized` to
  `Authorized`. If a user is authorized, they can be given one of the following
  levels of access to RStudio.

- RStudio User: This is a standard RStudio user and can access
  RStudio.
- RStudio Admin: The admin of your Amazon SageMaker AI domain has the ability to create users, add
  existing users, and update the permissions of existing users. Admins can also access the
  RStudio Administrative dashboard. However, this admin is not able to update parameters that
  are managed by Amazon SageMaker AI.

## Methods to create a user

The following topics show how to create a user in your RStudio-enabled
Amazon SageMaker AI domain.

**Create user console**

To create a user in your RStudio-enabled
Amazon SageMaker AI domain from the console, complete the steps in [Add user profiles](domain-user-profile-add.md "domain-user-profile-add.md").

**Create user CLI**

The following command shows how to add users to a Amazon SageMaker AI domain with IAM authentication. A
User can belong to either the `R_STUDIO_USER` or `R_STUDIO_ADMIN` User
group.

```
aws sagemaker create-user-profile --region `<REGION>` \
    --domain-id `<DOMAIN-ID>` \
    --user-profile-name `<USER_PROFILE_NAME-ID>` \
    --user-settings RStudioServerProAppSettings={UserGroup=`<USER-GROUP>`}
```

The following command shows how to add users to a Amazon SageMaker AI domain with authentication using IAM Identity Center.
A user can belong to either the `R_STUDIO_USER` or `R_STUDIO_ADMIN` User
group.

```
aws sagemaker create-user-profile --region `<REGION>` \
    --domain-id `<DOMAIN-ID>` \
    --user-profile-name `<USER_PROFILE_NAME-ID>` \
    --user-settings RStudioServerProAppSettings={UserGroup=`<USER-GROUP>`} \
    --single-sign-on-user-identifier UserName \
    --single-sign-on-user-value `<USER-NAME>`
```
