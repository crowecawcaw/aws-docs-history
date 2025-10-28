End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# View configuration details for a service sync

You can view the configuration details data for a service sync using the console or
AWS CLI.

AWS Management Console

###### Use the console to view configuration details for a service sync

1. In the navigation pane, choose **Services**.
2. To view detail data, choose the name of a service that you created a service
   sync configuration for.
3. In the detail page for the service, select the **Service sync**
   tab to view the configuration detail data for the service sync.

AWS CLI
Use the AWS CLI to get a synced service.

Run the following command.

```
`$` `aws proton get-service-sync-config \
 --service-name "`service name`"`
```

The response is as follows.

```
{
    "serviceSyncConfig": {
        "branch": "main",
        "filePath": "./configuration/custom-proton-ops.yaml",
        "repositoryName": "example/proton-sync-service",
        "repositoryProvider": "GITHUB",
        "serviceName": "service name"
    }
}
```

Use the AWS CLI to get the service sync status.

Run the following command.

```
`$` `aws proton get-service-sync-status \
 --service-name "`service name`"`
```
