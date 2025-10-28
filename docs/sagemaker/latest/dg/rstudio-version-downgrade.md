# Downgrade to the existing version

You can manually downgrade the version of your existing RStudio application to the
`2023.03.3-547.pro5` version.

###### To downgrade to the existing version

1. Delete the `RStudioServerPro` application that's associated with
   your existing domain. For information about how to find your domain ID, see
   [View domains](domain-view.md "domain-view.md").

```
aws sagemaker delete-app \
    --domain-id `domainId` \
    --user-profile-name domain-shared \
    --app-type RStudioServerPro \
    --app-name default
```

2. Pass the corresponding `2023.03.3-547.pro5` ARN for your
   Region as part of the `update-domain` command. For
   a list of all available ARNs, see [Versioning](rstudio-version.md#rstudio-version-new "rstudio-version.md#rstudio-version-new"). You must also pass an execution role
   ARN for the domain that provides permissions to update the domain.

```
aws sagemaker update-domain \
    --region `region` \
    --domain-id `domainId` \
    --domain-settings-for-update "{\"RStudioServerProDomainSettingsForUpdate\":{\"DefaultResourceSpec\": {\"SageMakerImageArn\": \"`arn-for-2023.03.3-547.pro5-version`\", \"InstanceType\": \"system\"}, \"DomainExecutionRoleArn\": \"`execution-role-arn`\"}}"
```

3. Create a new `RStudioServerPro` application in the existing domain.
   The RStudio version defaults to `2023.03.3-547.pro5`.

```
aws sagemaker create-app \
    --domain-id `domainId` \
    --user-profile-name domain-shared \
    --app-type RStudioServerPro \
    --app-name default
```

Your `RStudioServerPro` application is now downgraded to version
`2023.03.3-547.pro5`.
