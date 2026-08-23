End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Edit a template sync configuration

You can edit any of the template sync configuration parameters except
`template-name` and `template-type`.

Learn to edit a template sync configuration using the console or CLI.

AWS Management Console
Edit a template sync configuration branch using the console.

###### In the list of templates.

1. In the [AWS Proton console](https://console.aws.amazon.com/proton/ "https://console.aws.amazon.com/proton/"), choose
   **(Environment or Service) Templates**.
2. In the list of templates, choose the name of the template with the template sync
   configuration that you want to edit.
3. In the template detail page, choose the **Template sync**
   tab.
4. In the **Template sync details** section, choose
   **Edit**.
5. In the **Edit** page, in the **Source code
   repository** section, for **Branch**, select a branch,
   and then choose **Save configuration**.

AWS CLI
The following example command and response shows how you can
edit a template sync configuration `branch` using the CLI.

Run the following command.

```
`$` `aws proton update-template-sync-config \
 --template-name "`env-template`" \
 --template-type "`ENVIRONMENT`" \
 --repository-provider "`GITHUB`" \
 --repository-name "`myrepos/templates`" \
 --branch "`fargate`" \
 --subdirectory "`env-template`"`
```

The response is as follows.

```
{
    "templateSyncConfigDetails": {
        "branch": "`fargate`",
        "repositoryProvider": "`GITHUB`",
        "repositoryName": "`myrepos/myrepo`",
        "subdirectory": "`templates`",
        "templateName": "`env-template`",
        "templateType": "`ENVIRONMENT`"
    }
}
```

You can similarly use the AWS CLI to update synced service templates.
