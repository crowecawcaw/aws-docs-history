End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Delete an environment

You can delete an AWS Proton environment by using the AWS Proton console or the
AWS CLI.

###### Note

You can't delete an environment that has any associated component. To delete such an
environment, you should first delete all components that are running in the environment. For
more information about components, see [AWS Proton components](ag-components.md "ag-components.md").

AWS Management Console
Delete an environment using the console as described in the
following two options.

###### In the list of environments.

1. In the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"), choose
   **Environments**.
2. In the list of environments, select the radio button to the left of the
   environment that you want to delete.
3. Choose **Actions** and then **Delete**.
4. A modal prompts you to confirm the delete action.
5. Follow the instructions and choose **Yes, delete**.

###### In the environment detail page.

1. In the [AWS Proton console](https://console.aws.amazon.com//proton/ "https://console.aws.amazon.com//proton/"), choose
   **Environments**.
2. In the list of environments, choose the name of the environment that you want to
   delete.
3. In the environment detail page, choose **Actions** and then
   **Delete**.
4. A modal prompts you to confirm that you want to delete.
5. Follow the instructions and choose **Yes, delete**.

AWS CLI
Use the AWS CLI to delete an environment.

_Don't_ delete an environment if services or service instances
are deployed to the environment.

Run the following command:

```
`$` `aws proton delete-environment \
 --name "`MySimpleEnv`"`
```

Response:

```
{
    "environment": {
        "arn": "arn:aws:proton:region-id:123456789012:environment/MySimpleEnv",
        "createdAt": "2021-04-02T17:29:55.472000+00:00",
        "deploymentStatus": "DELETE_IN_PROGRESS",
        "lastDeploymentAttemptedAt": "2021-04-02T17:48:26.307000+00:00",
        "lastDeploymentSucceededAt": "2021-04-02T17:48:26.307000+00:00",
        "name": "MySimpleEnv",
        "protonServiceRoleArn": "arn:aws:iam::123456789012:role/ProtonServiceRole",
        "templateMajorVersion": "1",
        "templateMinorVersion": "1",
        "templateName": "simple-env"
    }
}
```
