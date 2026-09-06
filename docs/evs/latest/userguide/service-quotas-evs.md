

# Amazon EVS service quotas
<a name="service-quotas-evs"></a>

Amazon EVS has integrated with Service Quotas, an AWS service that you can use to view and manage your quotas from a central location. For more information, see [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) in the *Service Quotas User Guide*.

With Service Quotas integration, you can use the AWS Management Console or AWS CLI to look up the value of your Amazon EVS quotas and request a quota increase for adjustable quotas. For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide* and [request-service-quota-increase](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/request-service-quota-increase.html) in the * AWS CLI Command Reference*.

For more information about Amazon EVS service quotas, see [Amazon EVS quotas](https://docs.aws.amazon.com/general/latest/gr/evs.html#limits_evs) in the * AWS General Reference Guide*.

**Important**  
Ensure that your EC2 Running On-Demand Standard Instance quota reflects the number of vCPUs that you need for all of the EC2 instances that you will use on Amazon EVS. For information about increasing EC2 service quotas, see [Request an increase](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html#request-increase) in the *Amazon EC2 User Guide*.

**Note**  
If you plan to use EC2 Dedicated Hosts for your Amazon EVS environment, ensure that your EC2 Dedicated Hosts quota reflects the number of Dedicated Hosts that you intend to use for a desired Region. For information about increasing EC2 service quotas, see [Request an increase](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html#request-increase) in the *Amazon EC2 User Guide*.

**Note**  
If configuring HCX internet connectivity, your IPAM quota for Amazon-provided contiguous public IPv4 CIDR block netmask length must be /28 or greater. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html).

**Note**  
Amazon CloudWatch collects AWS usage metrics for Amazon EVS resources that have quotas (environment and hosts). For more information, see [CloudWatch Usage Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html) in the *Amazon CloudWatch User Guide*.

## View Amazon EVS service quotas in the AWS Management Console
<a name="view-service-quotas-console"></a>

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/evs/quotas).

1. In the left navigation pane, choose ** AWS services**.

1. From the ** AWS services** list, search for and select **Amazon Elastic VMware Service**.

1. Choose **View quotas**.

   In the **Service quotas** list, you can see the service quota name, applied value (if it’s available), AWS default quota, and whether the quota value is adjustable.

1. To view additional information about a service quota, such as the description, choose the quota name.

1. (Optional) To request a quota increase, select the quota that you want to increase, select **Request increase at account level**, enter or select the required information, and select **Request**.

To work more with service quotas using the AWS Management Console, see the [Service Quotas User Guide](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html). To request a quota increase, see [Requesting a Quota Increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

## View Amazon EVS service quotas with the AWS CLI
<a name="view-service-quotas-cli"></a>

Run the following command to view your Amazon EVS quotas.

```
aws service-quotas list-aws-default-service-quotas \
    --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
    --service-code evs \
    --output table
```

**Note**  
The quota returned is the number of Amazon EVS environments or hosts that can be created in this account in the current AWS Region.

To work more with service quotas using the AWS CLI, see [service-quotas](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/index.html) in the * AWS CLI Command Reference*. To request a quota increase, see the [request-service-quota-increase](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/request-service-quota-increase.html) command in the * AWS CLI Command Reference*.