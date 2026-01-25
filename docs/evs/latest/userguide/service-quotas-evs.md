# Amazon EVS service quotas

Amazon EVS has integrated with Service Quotas, an AWS service that you can use to view and manage your quotas from a central location.
For more information, see [What Is Service Quotas?](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md") in the _Service Quotas User Guide_.

With Service Quotas integration, you can use the AWS Management Console or AWS CLI to look up the value of your Amazon EVS quotas and request a quota increase for adjustable quotas.
For more information, see [Requesting a quota increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_ and [request-service-quota-increase](../../../cli/latest/reference/service-quotas/request-service-quota-increase.md "../../../cli/latest/reference/service-quotas/request-service-quota-increase.md") in the _AWS CLI Command Reference_.

For more information about Amazon EVS service quotas, see [Amazon EVS quotas](../../../general/latest/gr/evs.md#limits_evs "../../../general/latest/gr/evs.md#limits_evs") in the _AWS General Reference Guide_.

###### Important

Ensure that your EC2 Running On-Demand Standard Instance quota reflects the number of vCPUs that you need for all of the EC2 instances that you will use on Amazon EVS.
Each i4i.metal instance uses 128 vCPUs.
For information about increasing EC2 service quotas, see [Request an increase](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#request-increase "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#request-increase") in the _Amazon EC2 User Guide_.

###### Note

If you plan to use EC2 Dedicated Hosts for your Amazon EVS environment, ensure that your EC2 Dedicated i4i Hosts quota reflects the number of Dedicated Hosts that you intend to use for a desired Region. For information about increasing EC2 service quotas, see [Request an increase](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#request-increase "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md#request-increase") in the _Amazon EC2 User Guide_.

###### Note

If configuring HCX internet connectivity, your IPAM quota for Amazon-provided contiguous public IPv4 CIDR block netmask length must be /28 or greater.
For more information, see [Quotas for your IPAM](../../../vpc/latest/ipam/quotas-ipam.md "../../../vpc/latest/ipam/quotas-ipam.md").

###### Note

Amazon CloudWatch collects AWS usage metrics for Amazon EVS resources that have quotas (environment and hosts).
For more information, see [CloudWatch Usage Metrics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.md") in the _Amazon CloudWatch User Guide_.

## View Amazon EVS service quotas in the AWS Management Console

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/eks/quotas "https://console.aws.amazon.com/servicequotas/home/services/eks/quotas").
2. In the left navigation pane, choose **AWS services**.
3. From the **AWS services** list, search for and select **Amazon Elastic VMware Service**.
4. Choose **View quotas**.

In the **Service quotas** list, you can see the service quota name, applied value (if it’s available), AWS default quota, and whether the quota value is adjustable. 5. To view additional information about a service quota, such as the description, choose the quota name. 6. (Optional) To request a quota increase, select the quota that you want to increase, select **Request increase at account level**, enter or select the required information, and select **Request**.

To work more with service quotas using the AWS Management Console, see the [Service Quotas User Guide](../../../servicequotas/latest/userguide/intro.md "../../../servicequotas/latest/userguide/intro.md").
To request a quota increase, see [Requesting a Quota Increase](../../../servicequotas/latest/userguide/request-quota-increase.md "../../../servicequotas/latest/userguide/request-quota-increase.md") in the _Service Quotas User Guide_.

## View Amazon EVS service quotas with the AWS CLI

Run the following command to view your Amazon EVS quotas.

```
aws service-quotas list-aws-default-service-quotas \
    --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
    --service-code evs \
    --output table
```

###### Note

The quota returned is the number of Amazon EVS environments or hosts that can be created in this account in the current AWS Region.

To work more with service quotas using the AWS CLI, see [service-quotas](../../../cli/latest/reference/service-quotas/index.md "../../../cli/latest/reference/service-quotas/index.md") in the _AWS CLI Command Reference_. To request a quota increase, see the [request-service-quota-increase](../../../cli/latest/reference/service-quotas/request-service-quota-increase.md "../../../cli/latest/reference/service-quotas/request-service-quota-increase.md") command in the _AWS CLI Command Reference_.
