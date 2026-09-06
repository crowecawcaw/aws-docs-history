

# Use AWS Secrets Manager in GitLab
<a name="integrating_gitlab"></a>

AWS Secrets Manager integrates with GitLab. You can leverage Secrets Manager secrets to protect your GitLab credentials so they are no longer hardcoded in GitLab. Instead, [GitLab Runner](https://docs.gitlab.com/runner/) retrieves these secrets from Secrets Manager when your application runs a job in the GitLab CI/CD pipelines.

To use this integration, you'll create an [OpenID Connect (OIDC) identity provider in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) AWS Identity and Access Management and an IAM role. This allows GitLab Runner to access your Secrets Manager secret. For more information about GitLab CI/CD and OIDC, see [GitLab documentation](https://docs.gitlab.com/ci/cloud_services/aws/).

## Considerations
<a name="gitlab-integration-considerations"></a>

If you're using a non-public GitLab instance, you cannot use this Secrets Manager integration. Instead, see [GitLab documentation for non-public instances](https://docs.gitlab.com/ci/cloud_services/aws/#configure-a-non-public-gitlab-instance).

## Prerequisites
<a name="gitlab-integration-prerequisites"></a>

To integrate Secrets Manager with GitLab, complete the following prerequisites:

1. 

**Create an AWS Secrets Manager secret**

   You'll need an Secrets Manager secret which will be retrieved in your GitLab job and removes the need to hard-code these credentials. You'll need the Secrets Manager secret ID when you [configure your GitLab pipeline](#configure-gitlab-pipeline). See [Create an AWS Secrets Manager secret](create_secret.md) for more information.

1. 

**Make GitLab your OIDC provider in the IAM console.**

   In this step, you’ll make GitLab your OIDC provider in the IAM console. For more information, see [Create an OpenID Connect (OIDC) identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html) and [GitLab documentation](https://docs.gitlab.com/ci/cloud_services/aws/).

   When creating the OIDC provider in the IAM console, use the following configurations:

   1. <a name="step2-oidc-provider"></a>Set the `provider URL` to your GitLab instance. For example, **gitlab.example.com**.

   1. <a name="step2-oidc-audience"></a>Set the `audience` or `aud` to **sts.amazonaws.com**.

1. 

**Create an IAM role and policy**

   You'll need to create an IAM role and policy. This role is assumed by GitLab with [AWS Security Token Service (STS)](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html). See [Create a role using custom trust policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-custom.html) for more information.

   1. In the IAM console, use the following settings when creating the IAM role:
      + Set `Trusted entity type` to **Web identity**.
      + Set `Group` to **your GitLab group**.
      + Set `Identity provider` to the same provider URL (the [GitLab instance](#step2-oidc-provider)) you used in step 2.
      + Set `Audience` to the same [audience](#step2-oidc-audience) you used in step 2.

   1. The following is an example of a trust policy that allows GitLab to assume roles. Your trust policy should list your AWS account, GitLab URL, and [project path](https://docs.gitlab.com/user/project/).  
****  

      ```
      {
        "Version":"2012-10-17",		 	 	 
        "Statement": [
          {
            "Effect": "Allow",
            "Action": "sts:AssumeRoleWithWebIdentity",
            "Principal": {
              "Federated": "arn:aws:iam::{{111122223333}}:oidc-provider/{{gitlab.example.com}}"
            },
            "Condition": {
              "StringEquals": {
                "{{gitlab.example.com}}:aud": [
                  "sts.amazon.com"
                ]
              },
              "StringLike": {
                "{{gitlab.example.com}}:sub": [
                  "project_path:{{mygroup/project-*:ref_type:branch-*:ref:main*}}"
                ]
              }
            }
          }
        ]
      }
      ```

   1. You'll also need to create an IAM policy to allow GitLab access to AWS Secrets Manager. You can add this policy to your trust policy. For more information, see [Create IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create-console.html).  
****  

      ```
      {
        "Version":"2012-10-17",		 	 	 
        "Statement": [
          {
            "Effect": "Allow",
            "Action": "secretsmanager:GetSecretValue",
            "Resource": "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{your-secret}}"
          }
        ]
      }
      ```

## Integrating AWS Secrets Manager with GitLab
<a name="integrating-aws-secrets-manager-gitlab"></a>

After completing the prerequisites, you can configure GitLab to use Secrets Manager to protect your credentials.

### Configure GitLab pipeline to use Secrets Manager
<a name="configure-gitlab-pipeline"></a>

You'll need to update your [GitLab CI/CD configuration file](https://docs.gitlab.com/ci/yaml/yaml_optimization/) with the following information:
+ The audience of the token set to STS.
+ The Secrets Manager secret ID.
+ The IAM role you want GitLab Runner to assume when executing jobs in the GitLab pipeline.
+ The AWS Region where the secret is stored.

GitLab fetches the secret from Secrets Manager and stores the value in a temporary file. The path to this file is stored in a CI/CD variable, similar to [file type CI/CD variables](https://docs.gitlab.com/ci/variables/#use-file-type-cicd-variables).

The following is a snippet of the YAML file for a GitLab CI/CD configuration file:

```
variables:
  AWS_REGION: {{us-east-1}}
  AWS_ROLE_ARN: 'arn:aws:iam::{{111122223333}}:role/{{gitlab-role}}'
job:
  id_tokens:
    AWS_ID_TOKEN:
      aud: 'sts.amazonaws.com'
  secrets:
    DATABASE_PASSWORD:
      aws_secrets_manager:
        secret_id: "arn:aws:secretsmanager:{{us-east-1}}:{{111122223333}}:secret:{{secret-name}}"
```

For more information, see [GitLab Secrets Manager integration documentation](https://docs.gitlab.com/ci/secrets/aws_secrets_manager/).

Optionally, you can test your OIDC configuration in GitLab. See [GitLab documentation for testing OIDC configuration](https://docs.gitlab.com/ci/cloud_services/aws/#test-the-oidc-configuration) for more information.

## Troubleshooting
<a name="troubleshooting-integration"></a>

The following can help you troubleshoot common issues you might encounter when integrating Secrets Manager with GitLab.

### GitLab Pipeline issues
<a name="gitlab-pipeline-issues"></a>

If you experience GitLab pipeline issues, ensure the following:
+ Your YAML file is properly formatted. For more information, see [GitLab documentation](https://docs.gitlab.com/ee/ci/yaml/).
+ Your GitLab pipeline is assuming the correct role, has the appropriate permissions, and access to the correct AWS Secrets Manager secret.

### Additional resources
<a name="additional-resources"></a>

The following resources can help you troubleshoot issues with GitLab and AWS Secrets Manager:
+ [GitLab OIDC troubleshooting](https://docs.gitlab.com/ci/cloud_services/aws/#troubleshooting)
+ [Debugging GitLab CI/CD Pipeline](https://docs.gitlab.com/ee/ci/troubleshooting.html)
+ [Troubleshooting](ascp-eks-installation.md#troubleshooting)