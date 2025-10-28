# Opt out of Amazon EFS auto-mounting

You can opt-out of Amazon SageMaker AI auto-mounting Amazon EFS user folders during domain and user profile
creation or for an existing domain or user profile.

## Opt out during domain creation

You can opt out of Amazon EFS auto-mounting when creating a domain using either the console or the
AWS Command Line Interface.

### Console

Complete the following steps to opt out of Amazon EFS auto-mounting when creating a domain from
the console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Complete the steps in [Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md") with the following modification to set up a domain.
   - On the **Configure storage** step, turn off
     **Automatically mount EFS storage and data**.

### AWS CLI

Use the following command to opt out of Amazon EFS auto-mounting during domain creation
using the AWS CLI. For more information about creating a domain using the AWS CLI, see [Use custom setup for Amazon SageMaker AI](onboard-custom.md "onboard-custom.md").

```
aws --region `region` sagemaker create-domain \
--domain-name "my-domain-$(date +%s)" \
--vpc-id `default-vpc-id` \
--subnet-ids `subnet-ids` \
--auth-mode IAM \
--default-user-settings "ExecutionRole=`execution-role-arn`,AutoMountHomeEFS=Disabled" \
--default-space-settings "ExecutionRole=`execution-role-arn`"
```

## Opt out for an existing domain

You can opt out of Amazon EFS auto-mounting for an existing domain using either the console or the
AWS CLI.

### Console

Complete the following steps to opt out of Amazon EFS auto-mounting when updating a domain from
the console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation under **Admin configurations**, choose
   **Domains**.
3. On the **Domains** page, select the domain that you want to opt out of
   Amazon EFS auto-mounting for.
4. On the **Domain details** page, select the **Domain
   settings** tab.
5. Navigate to the **Storage configurations** section.
6. Select **Edit**.
7. From the **Edit storage settings** page, turn off
   **Automatically mount EFS storage and data**.
8. Select **Submit**.

### AWS CLI

Use the following command to opt out of Amazon EFS auto-mounting while updating an existing domain
using the AWS CLI.

```
aws --region `region` sagemaker update-domain \
--domain-id `domain-id` \
--default-user-settings "AutoMountHomeEFS=Disabled"
```

## Opt out during user profile creation

You can opt out of Amazon EFS auto-mounting when creating a user profile using either the console
or the AWS CLI.

### Console

Complete the following steps to opt out of Amazon EFS auto-mounting when creating a user profile
from the console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Complete the steps in
   [Add user profiles](domain-user-profile-add.md "domain-user-profile-add.md")
   with the following modification to create a user profile.
   - On the **Data and Storage** step, turn off **Inherit
     settings from domain**. This allows the user to have a different value
     than the defaults that are set for the domain.
   - Turn off **Automatically mount EFS storage and data**.

### AWS CLI

Use the following command to opt out of Amazon EFS auto-mounting during user profile creation
using the AWS CLI. For more information about creating a user profile using the AWS CLI, see
[Add user profiles](domain-user-profile-add.md "domain-user-profile-add.md").

```
aws --region `region` sagemaker create-user-profile \
--domain-id `domain-id` \
--user-profile-name "`user-profile`-$(date +%s)" \
--user-settings "ExecutionRole=arn:aws:iam::`account-id`:role/`execution-role-name`,AutoMountHomeEFS=Enabled/Disabled/DefaultAsDomain"
```

## Opt out for an existing user profile

You can opt out of Amazon EFS auto-mounting for an existing user profile using either the console
or the AWS CLI.

### Console

Complete the following steps to opt out of Amazon EFS auto-mounting when updating a user profile
from the console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation under **Admin configurations**, choose
   **Domains**.
3. On the **Domains** page, select the domain containing the user profile
   that you want to opt out of Amazon EFS auto-mounting for.
4. On the **Domains details** page, select the **User
   profiles** tab.
5. Select the user profile to update.
6. From the **User Details** tab, navigate to the
   **AutoMountHomeEFS** section.
7. Select **Edit**.
8. From the **Edit storage settings** page, turn off **Inherit
   settings from domain**. This allows the user to have a different value than
   the defaults that are set for the domain.
9. Turn off **Automatically mount EFS storage and data**.
10. Select **Submit**.

### AWS CLI

Use the following command to opt out of Amazon EFS auto-mounting while updating an existing user
profile using the AWS CLI.

```
aws --region `region` sagemaker update-user-profile \
--domain-id `domain-id` \
--user-profile-name `user-profile-name` \
--user-settings "AutoMountHomeEFS=DefaultAsDomain"
```
