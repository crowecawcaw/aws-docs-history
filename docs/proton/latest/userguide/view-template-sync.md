End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# View template sync configuration details

View template sync configuration detail data using the console or CLI.

AWS Management Console

###### Use the console to view template sync configuration details.

1. In the navigation pane, choose **(Environment or Service)
   templates**.
2. To view detail data, choose the name of a template that you created a template
   sync configuration for.
3. In the detail page for the template, select the **Sync** tab to
   view the template sync configuration detail data.

AWS CLI
Use the AWS CLI to view a synced template.

Run the following command.

```
`$` `aws proton get-template-sync-config \
 --template-name "`svc-template`" \
 --template-type "`SERVICE`"`
```

The response is as follows.

```
{
    "templateSyncConfigDetails": {
        "branch": "main",
        "repositoryProvider": "GITHUB",
        "repositoryName": "myrepos/myrepo",
        "subdirectory": "`svc-template`",
        "templateName": "`svc-template`",
        "templateType": "`SERVICE`"
    }
}
```

Use the AWS CLI to get template sync status.

For `template-version`, enter the template major version.

Run the following command.

```
`$` `aws proton get-template-sync-status \
 --template-name "`env-template`" \
 --template-type "`ENVIRONMENT`" \
 --template-version "`1`"`
```
