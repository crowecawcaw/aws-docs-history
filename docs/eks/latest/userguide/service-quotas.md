

 **Help improve this page** 

To contribute to this user guide, choose the **Edit this page on GitHub** link that is located in the right pane of every page.

# View and manage Amazon EKS and Fargate service quotas
<a name="service-quotas"></a>

Amazon EKS has integrated with Service Quotas, an AWS service that you can use to view and manage your quotas from a central location. For more information, see [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) in the *Service Quotas User Guide*. With Service Quotas integration, you can quickly look up the value of your Amazon EKS and AWS Fargate service quotas using the AWS Management Console and AWS CLI.

## View EKS service quotas in the AWS Management Console
<a name="service-quotas-console"></a>

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas).

1. In the left navigation pane, choose ** AWS services**.

1. From the ** AWS services** list, search for and select **Amazon Elastic Kubernetes Service (Amazon EKS)** or ** AWS Fargate**.

   In the **Service quotas** list, you can see the service quota name, applied value (if it’s available), AWS default quota, and whether the quota value is adjustable.

1. To view additional information about a service quota, such as the description, choose the quota name.

1. (Optional) To request a quota increase, select the quota that you want to increase, select **Request quota increase**, enter or select the required information, and select **Request**.

To work more with service quotas using the AWS Management Console, see the [Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html). To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

## View EKS service quotas with the AWS CLI
<a name="view_eks_service_quotas_with_the_shared_aws_cli"></a>

Run the following command to view your Amazon EKS quotas.

```
aws service-quotas list-aws-default-service-quotas \
    --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
    --service-code eks \
    --output table
```

Run the following command to view your Fargate quotas.

```
aws service-quotas list-aws-default-service-quotas \
    --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
    --service-code fargate \
    --output table
```

**Note**  
The quota returned is the number of Amazon ECS tasks or Amazon EKS Pods that can run concurrently on Fargate in this account in the current AWS Region.

To work more with service quotas using the AWS CLI, see [service-quotas](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/index.html) in the * AWS CLI Command Reference*. To request a quota increase, see the [request-service-quota-increase](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/request-service-quota-increase.html) command in the * AWS CLI Command Reference*.

## Amazon EKS service quotas
<a name="sq-text"></a>

 AWS recommends using the AWS Management Console to view your current quotas. For more information, see [View EKS service quotas in the AWS Management Console](#service-quotas-console).

To view the default EKS service quotas, see [Amazon Elastic Kubernetes Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/eks.html#limits_eks) in the * AWS General Reference*.

These service quotas are listed under **Amazon Elastic Kubernetes Service (Amazon EKS)** in the Service Quotas console. To request a quota increase for values that are shown as adjustable, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

**Note**  
Adjustments to the following components are **not** supported in Service Quotas: \* Pod Identity associations per cluster. For limits, see [Learn how EKS Pod Identity grants pods access to AWS services](pod-identities.md). \* CIDRs for Remote Node Networks or Remote Pod Networks for hybrid nodes. For limits, see [Amazon EKS Hybrid Nodes overview](hybrid-nodes-overview.md).

## AWS Fargate service quotas
<a name="service-quotas-eks-fargate"></a>

The ** AWS Fargate** service in the Service Quotas console lists several service quotas. You can configure alarms that alert you when your usage approaches a service quota. For more information, see [Creating a CloudWatch alarm to monitor Fargate resource usage metrics](monitoring-fargate-usage.md#service-quota-alarm).

New AWS accounts might have lower initial quotas that can increase over time. Fargate constantly monitors the account usage within each AWS Region, and then automatically increases the quotas based on the usage. You can also request a quota increase for values that are shown as adjustable. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

 AWS recommends using the AWS Management Console to view your current quotas. For more information, see [View EKS service quotas in the AWS Management Console](#service-quotas-console).

To view default AWS Fargate on EKS service quotas, see [Fargate service quotas](https://docs.aws.amazon.com/general/latest/gr/eks.html#service-quotas-eks-fargate) in the * AWS General Reference*.

**Note**  
Fargate additionally enforces Amazon ECS tasks and Amazon EKS Pods launch rate quotas. For more information, see [AWS Fargate throttling quotas](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/throttling.html) in the *Amazon ECS guide*.