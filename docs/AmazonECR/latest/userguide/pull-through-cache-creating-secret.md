

# Storing your upstream repository credentials in an AWS Secrets Manager secret
<a name="pull-through-cache-creating-secret"></a>

When creating a pull through cache rule for an upstream repository that requires authentication, you must store the credentials in a Secrets Manager secret. There may be a cost for using an Secrets Manager secret. For more information, see [AWS Secrets Manager pricing](https://aws.amazon.com/secrets-manager/pricing/).

The following procedures walk you through how to create an Secrets Manager secret for each supported upstream repository. You can optionally use the create pull through cache rule workflow in the Amazon ECR console to create the secret instead of creating the secret using the Secrets Manager console. For more information, see [Creating a pull through cache rule in Amazon ECR](pull-through-cache-creating-rule.md).

------
#### [ Docker Hub ]

**To create a Secrets Manager secret for your Docker Hub credentials (AWS Management Console)**To create a Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your Docker Hub credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your Docker Hub username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your Docker Hub access token as the value. For more information on creating a Docker Hub access token, see [Create and manage access tokens](https://docs.docker.com/security/for-developers/access-tokens/) in the Docker documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following.

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------
#### [ GitHub Container Registry ]

**To create an Secrets Manager secret for your GitHub Container Registry credentials (AWS Management Console)**To create an Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your GitHub credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your GitHub username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your GitHub access token as the value. For more information on creating a GitHub access token, see [Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) in the GitHub documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------
#### [ Microsoft Azure Container Registry ]

**To create an Secrets Manager secret for your Microsoft Azure Container Registry credentials (AWS Management Console)**To create an Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your Microsoft Azure credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your Microsoft Azure Container Registry username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your Microsoft Azure Container Registry access token as the value. For more information on creating an Microsoft Azure access token, see [Create token - portal](https://learn.microsoft.com/en-us/azure/container-registry/container-registry-repository-scoped-permissions#create-token---portal) in the Microsoft Azure documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------
#### [ GitLab Container Registry ]

**To create an Secrets Manager secret for your GitLab Container Registry credentials (AWS Management Console)**To create an Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your GitLab credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your GitLab Container Registry username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your GitLab Container Registry access token as the value. For more information on creating a GitLab Container Registry access token, see [Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens.html), [Group access tokens](https://docs.gitlab.com/ee/user/group/settings/group_access_tokens.html), or [Project access tokens](https://docs.gitlab.com/ee/user/project/settings/project_access_tokens.html), in the GitLab documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------
#### [ Chainguard Registry ]

**To create an Secrets Manager secret for your Chainguard credentials (AWS Management Console)**To create an Secrets Manager secret (AWS Management Console)

1. Open the Secrets Manager console at [https://console.aws.amazon.com/secretsmanager/](https://console.aws.amazon.com/secretsmanager/).

1. Choose **Store a new secret**.

1. On the **Choose secret type** page, do the following.

   1. For **Secret type**, choose **Other type of secret**.

   1. In **Key/value pairs**, create two rows for your Chainguard credentials. You can store up to 65536 bytes in the secret.

      1. For the first key/value pair, specify `username` as the key and your Chainguard Registry username as the value.

      1. For the second key/value pair, specify `accessToken` as the key and your Chainguard Registry access token as the value. For more information on creating a Chainguard Registry pull token, see [Authenticating with a Pull Token ](https://edu.chainguard.dev/chainguard/chainguard-images/chainguard-registry/authenticating/#authenticating-with-a-pull-token) in the Chainguard documentation.

   1. For **Encryption key**, keep the default **aws/secretsmanager** AWS KMS key value and then choose **Next**. There is no cost for using this key. For more information, see [Secret encryption and decryption in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security-encryption.html) in the *AWS Secrets Manager User Guide*.
**Important**  
You must use the default `aws/secretsmanager` encryption key to encrypt your secret. Amazon ECR doesn't support using a customer managed key (CMK) for this.

1. On the **Configure secret** page, do the following:

   1. Enter a descriptive **Secret name** and **Description**. Secret names must contain 1-512 Unicode characters and be prefixed with `ecr-pullthroughcache/`.
**Important**  
The Amazon ECR AWS Management Console only displays Secrets Manager secrets with names using the `ecr-pullthroughcache/` prefix.

   1. (Optional) In the **Tags** section, add tags to your secret. For tagging strategies, see [Tag Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets_tagging.html) in the *AWS Secrets Manager User Guide*. Don't store sensitive information in tags because they aren't encrypted.

   1. (Optional) In **Resource permissions**, to add a resource policy to your secret, choose **Edit permissions**. For more information, see [Attach a permissions policy to an Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_resource-policies.html) in the *AWS Secrets Manager User Guide*.

   1. (Optional) In **Replicate secret**, to replicate your secret to another AWS Region, choose **Replicate secret**. You can replicate your secret now or come back and replicate it later. For more information, see [Replicate a secret to other Regions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create-manage-multi-region-secrets.html) in the *AWS Secrets Manager User Guide*.

   1. Choose **Next**.

1. (Optional) On the **Configure rotation** page, you can turn on automatic rotation. You can also keep rotation off for now and then turn it on later. For more information, see [Rotate Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/rotating-secrets.html) in the *AWS Secrets Manager User Guide*. Choose **Next**.

1. On the **Review** page, review your secret details, and then choose **Store**.

   Secrets Manager returns to the list of secrets. If your new secret doesn't appear, choose the refresh button.

------