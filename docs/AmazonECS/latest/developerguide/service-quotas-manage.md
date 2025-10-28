# Managing your Amazon ECS and AWS Fargate service

quotas in the AWS Management Console

Amazon ECS has integrated with Service Quotas, an AWS service that enables you to view and
manage your quotas from a central location. For more information, see [What is
Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md") in the _Service Quotas User Guide_.

Service Quotas makes it easy to look up the value of your Amazon ECS service quotas.

AWS Management Console

###### To view Amazon ECS and Fargate service quotas using the

AWS Management Console

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/ "https://console.aws.amazon.com/servicequotas/").
2. In the navigation pane, choose **AWS
   services**.
3. From the **AWS services** list, search for
   and select **Amazon Elastic Container Service (Amazon ECS)** or
   **AWS Fargate**.

In the **Service quotas** list, you can see
the service quota name, applied value (if it is available),
AWS default quota, and whether the quota value is
adjustable. 4. To view additional information about a service quota, such as
the description, choose the quota name. 5. (Optional) To request a quota increase,
select the quota that you want to increase, select
**Request quota increase**, enter or select
the required information, and select
**Request**.

To work more with service quotas using the AWS Management Console see the [Service Quotas User Guide](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md"). To request a quota increase, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the
_Service Quotas User Guide_.

AWS CLI

###### To view Amazon ECS and Fargate service quotas using the

AWS CLI

Run the following command to view the default Amazon ECS quotas.

```
`aws service-quotas list-aws-default-service-quotas \
 --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
 --service-code ecs \
 --output table`
```

Run the following command to view the default Fargate quotas.

```
`aws service-quotas list-aws-default-service-quotas \
 --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
 --service-code fargate \
 --output table`
```

Run the following command to view your applied Fargate
quotas.

```
`aws service-quotas list-service-quotas \
 --service-code fargate`
```

###### Note

Amazon ECS doesn't support applied quotas.

For more information about working with service quotas using the
AWS CLI, see the [Service Quotas AWS CLI Command Reference](../../../cli/latest/reference/service-quotas/index.md#cli-aws-service-quotas "../../../cli/latest/reference/service-quotas/index.md#cli-aws-service-quotas"). To request a quota increase,
see the [`request-service-quota-increase`](../../../cli/latest/reference/service-quotas/request-service-quota-increase.md "../../../cli/latest/reference/service-quotas/request-service-quota-increase.md") command in
the [AWS CLI Command Reference](../../../cli/latest/reference/service-quotas/index.md#cli-aws-service-quotas "../../../cli/latest/reference/service-quotas/index.md#cli-aws-service-quotas").
