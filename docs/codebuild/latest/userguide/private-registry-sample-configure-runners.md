# Configure a private registry

credential for self-hosted runners

Use the following instructions to configure a registry credential for a self-hosted runner.

###### Note

Note that these credentials will only be used if the images are overridden
with those from private registries.

AWS Management Console

1. Open the AWS CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/home](https://console.aws.amazon.com/codesuite/codebuild/home "https://console.aws.amazon.com/codesuite/codebuild/home").
2. Create a build project or select an existing project. For information, see [Create a build project (console)](create-project.md#create-project-console "create-project.md#create-project-console")
   and [Change a build project's settings
   (console)](change-project.md#change-project-console "change-project.md#change-project-console").
3. In **Environment**, choose
   **Additional configuration**.
4. In **Additional configuration**, enter the name or ARN of
   the secret from AWS Secrets Manager for **Registry credential - optional**.

![The registry credential configuration.](images/registry-credential.png)

AWS CLI

1. If you'd like to create a new project, run the
   **create-project** command.

```
aws codebuild create-project \
    --name `project-name` \
    --source type=`source-type`,location=`source-location` \
    --environment "type=`environment-type`,image=`image`,computeType=`compute-type`,registryCredential={credentialProvider=SECRETS_MANAGER,credential=`secret-name-or-arn`},imagePullCredentialsType=CODEBUILD|SERVICE_ROLE" \
    --artifacts type=`artifacts-type` \
    --service-role arn:aws:iam::`account-ID`:role/service-role/`service-role-name`
```

2. If you'd like to update an existing project, run the
   **update-project** command.

```
aws codebuild update-project \
    --name `project-name` \
    --environment "type=`environment-type`,image=`image`,computeType=`compute-type`,registryCredential={credentialProvider=SECRETS_MANAGER,credential=`secret-name-or-arn`}"
```
