# Edit domain settings

You can edit the settings of a domain from the SageMaker AI console or the AWS CLI. The
following considerations apply when updating the settings of a domain.

- If `DefaultUserSettings` and `DefaultSpaceSettings` are set,
  they cannot be unset.
- `DefaultUserSettings.ExecutionRole` can only be updated if there are no
  applications running in any user profile within the domain. This value cannot be
  unset.
- `DefaultSpaceSettings.ExecutionRole` can only be updated if there are
  no applications running in any of shared spaces within the domain. This value cannot
  be unset.
- If the domain was created in **VPC only** mode, SageMaker AI
  automatically applies updates to the security group settings defined for the
  domain to all shared spaces created in the domain.
- `DomainId` and `DomainName` cannot be edited.
  The following section shows how to edit domain settings from the SageMaker AI console or the
  AWS CLI.

## Console

You can edit the domain from the SageMaker AI console using the following procedure.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin
   configurations**.
3. Under **Admin configurations**, choose
   **domains**.
4. From the list of domains, select the domain for which you want to
   open the **domain settings** page.
5. On the **domain details** page, you can configure and
   manage your domain details by choosing the appropriate tab.
6. To configure the general settings, on the **domain
   details** page choose the **domain settings**
   tab then choose **Edit**.

## AWS CLI

Run the following command from the terminal of your local machine to update a
domain from the AWS CLI. For more information about the structure of
`default-user-settings`, see [CreateDomain](../APIReference/API_CreateDomain.md#API_CreateDomain_RequestSyntax "../APIReference/API_CreateDomain.md#API_CreateDomain_RequestSyntax").

```
aws sagemaker update-domain \
--domain-id `domain-id` \
--default-user-settings `default-user-settings` \
--default-space-settings `default-space-settings` \
--domain-settings-for-update `settings-for-update` \
--region `region`
```
