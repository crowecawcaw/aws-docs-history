End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Delete a template sync configuration

Delete a template sync configuration using the console or CLI.

AWS Management Console

###### Delete a template sync configuration using the console.

1. In the template details page, choose the **Sync** tab.
2. In the **Sync details** section, choose
   **Disconnect**.

AWS CLI
The following example commands and responses show how to use
the AWS CLI to delete synced template configurations.

Run the following command.

```
`$` `aws proton delete-template-sync-config \
 --template-name "`env-template`" \
 --template-type "`ENVIRONMENT`"`
```

The response is as follows.

```
{
    "templateSyncConfig": {
        "templateName": "`env-template`",
        "templateType": "`ENVIRONMENT`"
    }
}
```
