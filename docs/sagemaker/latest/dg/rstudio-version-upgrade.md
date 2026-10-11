

# Upgrade to the new version
<a name="rstudio-version-upgrade"></a>

Existing domains using version `2025.05.1+513.pro3` can upgrade to `2026.08.2+200.pro1` version in one of two ways:
+ Create a new domain from the AWS CLI with RStudio enabled.
+ Update an existing domain to use the `2026.08.2+200.pro1` version.

The following procedure shows how to delete the RStudio application for an existing domain, set the default version to `2026.08.2+200.pro1`, and then create an RStudio application.

1. Delete the `RStudioServerPro` application and all `RSessionGateway` applications associated with your existing domain. For information about how to find your domain ID, see [View domains](domain-view.md). For more information about deleting applications, see [Shut down RStudio](rstudio-shutdown.md).

   ```
   aws sagemaker delete-app \
       --region {{region}} \
       --domain-id {{domainId}} \
       --user-profile-name domain-shared \
       --app-type RStudioServerPro \
       --app-name default
   ```

1. If your domain is using RStudio version `2025.05.1+513.pro3`, update the domain to set `2026.08.2+200.pro1` as the default Posit Workbench version. The `SageMakerImageArn` value in the following `update-domain` command specifies the RStudio `2026.08.2+200.pro1` version as the default. This ARN must match the Region that your domain is in. For a list of all available ARNs, see [Versioning](rstudio-version.md#rstudio-version-new).

   Pass an execution role ARN for the domain that provides permissions to update the domain. 

   ```
   aws sagemaker update-domain \
       --region {{region}} \
       --domain-id {{domainId}} \
       --domain-settings-for-update "{\"RStudioServerProDomainSettingsForUpdate\":{\"DefaultResourceSpec\": {\"SageMakerImageArn\": \"{{arn-for-2026.08.2+200.pro1-version}}\", \"InstanceType\": \"system\"}, \"DomainExecutionRoleArn\": \"{{execution-role-arn}}\"}}"
   ```

1. Create a new `RStudioServerPro` application in the existing domain.

   ```
   aws sagemaker create-app \
       --region {{region}}
       --domain-id {{domainId}} \
       --user-profile-name domain-shared \
       --app-type RStudioServerPro \
       --app-name default
   ```

Your `RStudioServerPro` application is now updated to version `2026.08.2+200.pro1`. You can now relaunch your `RSessionGateway` applications.