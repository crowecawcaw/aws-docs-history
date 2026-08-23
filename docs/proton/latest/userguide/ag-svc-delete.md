End of support notice: On October 7, 2026, AWS will end support for AWS Proton. After October
7, 2026, you will no longer be able to access the AWS Proton console or AWS Proton resources. Your deployed infrastructure
will remain intact. For more information, see [AWS Proton Service Deprecation and Migration
Guide](proton-end-of-support.md "proton-end-of-support.md").

# Delete a service

You can delete an AWS Proton service, with its instances and pipeline, by using the AWS Proton console or the AWS CLI.

You can't delete a service that has any service instance with an attached component. To delete such a service, you should first update all attached
components to detach them from their service instances. For more information about components, see [AWS Proton components](ag-components.md "ag-components.md").

AWS Management Console
Delete a service using the console as described in the following steps.

###### In the service detail page.

1. In the [AWS Proton console](https://console.aws.amazon.com/proton/ "https://console.aws.amazon.com/proton/"), choose **Services**.
2. In the list of services, choose the name of the service that you want to delete.
3. On the service detail page, choose **Actions** and then **Delete**.
4. A modal prompts you to confirm the delete action.
5. Follow the instructions and choose **Yes, delete**.

AWS CLI
Delete a service as shown in the following CLI example command and response.

Command:

```
`$` `aws proton delete-service \
 --name "`simple-svc`"`
```

Response:

```
{
    "service": {
        "arn": "arn:aws:proton:region-id:123456789012:service/simple-svc",
        "branchName": "mainline",
        "createdAt": "2020-11-28T22:40:50.512000+00:00",
        "description": "Edit by updating description",
        "lastModifiedAt": "2020-11-29T00:30:39.248000+00:00",
        "name": "simple-svc",
        "repositoryConnectionArn": "arn:aws:codestar-connections:region-id:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "repositoryId": "myorg/myapp",
        "status": "DELETE_IN_PROGRESS",
        "templateName": "fargate-service"
    }
}
```
