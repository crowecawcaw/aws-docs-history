

# Managing your AWS Cloud Map service quotas
<a name="service-quotas-manage"></a>

AWS Cloud Map has integrated with Service Quotas, an AWS service that enables you to view and manage your quotas from a central location. For more information, see [What is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) in the *Service Quotas User Guide*.

Service Quotas makes it easy to look up the value of your AWS Cloud Map service quotas.

------
#### [ AWS Management Console ]

**To view AWS Cloud Map service quotas using the AWS Management Console**

1. Open the Service Quotas console at [https://console.aws.amazon.com/servicequotas/](https://console.aws.amazon.com/servicequotas/).

1. In the navigation pane, choose **AWS services**.

1. From the **AWS services** list, search for and select **AWS Cloud Map**.

1. In the service quotas list for AWS Cloud Map, you can see the service quota name, applied value (if it is available), AWS default quota, and whether the quota value is adjustable.

   To view additional information about a service quota, such as the description, choose the quota name to bring up the quota details.

1. (Optional) To request a quota increase, select the quota that you want to increase and choose **Request increase at account-level**.

To work more with service quotas using the AWS Management Console see the [Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html).

------
#### [ AWS CLI ]

**To view AWS Cloud Map service quotas using the AWS CLI**  
Run the following command to view the default AWS Cloud Map quotas.

```
aws service-quotas list-aws-default-service-quotas \
    --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
    --service-code AWSCloudMap \
    --output table
```

Run the following command to view your applied AWS Cloud Map quotas.

```
aws service-quotas list-service-quotas \
    --service-code AWSCloudMap
```

For more information about working with service quotas using the AWS CLI, see the [Service Quotas AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/#cli-aws-service-quotas). To request a quota increase, see the [`request-service-quota-increase`](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/request-service-quota-increase.html) command in the [AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/#cli-aws-service-quotas).

------