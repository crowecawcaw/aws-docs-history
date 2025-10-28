# App Mesh service quotas

###### Important

End of support notice: On September 30, 2026, AWS will discontinue support for AWS App Mesh. After September 30, 2026, you will no longer be able to access the AWS App Mesh console or AWS App Mesh resources. For more information, visit this blog post [Migrating from AWS App Mesh to Amazon ECS Service Connect](https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect "https://aws.amazon.com/blogs/containers/migrating-from-aws-app-mesh-to-amazon-ecs-service-connect").

AWS App Mesh has integrated with Service Quotas, an AWS service that enables
you to view and manage your quotas from a central location. Service quotas are also referred
to as limits. For more information, see [What Is Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md") in the
_Service Quotas User Guide_.

Service Quotas makes it easy to look up the value of all of the App Mesh service
quotas.

###### To view App Mesh service quotas using the AWS Management Console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, choose **AWS services**.
3. From the **AWS services** list, search for and select
   **AWS App Mesh**.

In the **Service quotas** list, you can see the service quota
name, applied value (if it is available), AWS default quota, and whether the quota
value is adjustable. 4. To view additional information about a service quota, such as the description,
choose the quota name.
To request a quota increase, see [Requesting a Quota
Increase](../../../servicequotas/latest/userguide/request-increase.md "../../../servicequotas/latest/userguide/request-increase.md") in the _Service Quotas User Guide_.

###### To view App Mesh service quotas using the AWS CLI

Run the following command.

```
`aws service-quotas list-aws-default-service-quotas \
 --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
 --service-code appmesh \
 --output table`
```

To work more with service quotas using the AWS CLI, see the [Service Quotas AWS CLI
Command Reference](../../../cli/latest/reference/service-quotas/index.md#cli-aws-service-quotas "../../../cli/latest/reference/service-quotas/index.md#cli-aws-service-quotas").
