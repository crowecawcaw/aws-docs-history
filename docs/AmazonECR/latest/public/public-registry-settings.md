# Updating registry settings in Amazon ECR

public

Your public registry provides settings to configure a custom alias and display
name.

By default, your public registry is assigned a **default alias**
after your first public repository is created. You can request a **custom
alias** for your registry, and if approved, both the default alias and
custom alias can be used to access your public repositories. The registry
**display name** appears on each repository in the
Amazon ECR Public Gallery as well.

When requesting a custom alias, the following words or phrases should be
avoided:

- An alias that includes `aws`, `amazon`, or the name of
  an AWS service
- An alias using a company name for which you do not have permission to
  use
- Generic names, such as `test`, `public`, and
  `marketplace`
- Offensive, inappropriate, or non-inclusive words and phrases

## Prerequisites

Before you can update your public registry settings in Amazon ECR, you must first have
the required IAM permissions. See, [Required IAM permissions for Amazon ECR
public registries](public-registry-settings-iam.md "public-registry-settings-iam.md") to ensure you have the necessary
permissions before continuing with the steps outlined on this page.

## Update your registry

settings

Use the following steps to edit your public registry settings.

###### To edit public registry settings (AWS Management Console)

1. Open the Amazon ECR console at
   [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/ "https://console.aws.amazon.com/ecr/").
2. From the navigation bar, choose the Region to edit your public registry
   settings in.
3. In the navigation pane, choose **Registries**.
4. On the **Registries** page, select your
   **Public** registry and then choose
   **Edit**.
5. For **Custom alias**, enter a custom alias to
   request.
6. For **Display name**, enter a display name for your
   registry.
7. Choose **Save changes**.
