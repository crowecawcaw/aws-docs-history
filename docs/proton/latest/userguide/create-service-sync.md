End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Create a service sync configuration

You can create a service sync configuration using the console or AWS CLI.

AWS Management Console

1. On the **Choose a service template** page, select a template
   and choose **Configure**.
2. On the **Configure service** page, in the **Service
   details** section, enter a new **Service name**.
3. (Optional) Enter a description for the service.
4. In the **Application source code repository** section, choose
   **Choose a linked Git repository** to select a repository you've
   already linked with AWS Proton. If you don't already have a linked repository, choose
   **Link another Git repository** and follow the instructions in
   [Create a link to your repository](ag-create-repo.md "ag-create-repo.md").
5. For **Repository**, choose the name of your source code
   repository from the list.
6. For **Branch**, choose the name of the repository branch for
   your source code from the list.
7. (Optional) In the **Tags** section, choose **Add new
   tag** and enter a key and value to create a customer managed tag.
8. Choose **Next**.
9. On the **Configure service instances** page, in the
   **Service definition source** section, select **Sync your
   service from Git**.
10. In the **Service definition files** section, if you want AWS Proton
    to create your `proton-ops` file, select **I want AWS Proton to
    create the files**. With this option, AWS Proton creates the `spec`
    and `proton-ops` file in the locations you specify. Select **I am
    providing my own files** to create your own OPS file.
11. In the **Service definition repository** section, choose
    **Choose a linked Git repository** to select a repository you've
    already linked with AWS Proton.
12. For **Repository name**, choose the name of your source code
    repository from the list.
13. For **`proton-ops` file branch**, choose the name of
    your branch from the list where AWS Proton will put your OPS and spec file.
14. In the **Service instances** section, each field is
    automatically filled based on the values in the `proton-ops` file.
15. Choose **Next** and review your inputs.
16. Choose **Create**.

AWS CLI

###### Create a service sync configuration using the AWS CLI

- Run the following command.

```
`$` `aws proton create-service-sync-config \
 --resource "`service-arn`" \
 --repository-provider "`GITHUB`" \
 --repository "`example/proton-sync-service`" \
 --ops-file-branch "`main`" \
 --proton-ops-file "`./configuration/custom-proton-ops.yaml`" (optional)`
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
