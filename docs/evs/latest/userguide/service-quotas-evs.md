

# Service quotas for Amazon EVS

Your AWS account has default quotas, also called limits, for each AWS service, and most quotas are specific to a Region.

Amazon Elastic VMware Service is integrated with Service Quotas, an AWS service that you can use to view and manage your quotas from a central location. For more information, see [What Is Service Quotas?](https://docs.aws.amazon.com/servicequotas/latest/userguide/intro.html) in the *Service Quotas User Guide*.

## Amazon EVS quotas
<a name="evs-quota-values"></a>

The following table shows the Amazon EVS quotas. The columns show the quota name as it appears in the Service Quotas console, the default value, whether you can request an increase, and what the quota limits.


| Name | Default | Adjustable | Description | 
| --- | --- | --- | --- | 
| Environment count per AWS account | 3 in each supported Region | Yes | The maximum number of Amazon EVS environments that you can create in this account in the current Region. | 
| Host count per EVS environment | 5 in each supported Region | Yes | The maximum number of hosts that you can provision in a single Amazon EVS environment. | 

The default values are the initial quotas that AWS sets. Your applied quota values can differ. For the authoritative values, see [Amazon EVS quotas](https://docs.aws.amazon.com/general/latest/gr/evs.html#limits_evs) in the * AWS General Reference*.

## Quotas to check before you add hosts
<a name="evs-quotas-check-first"></a>

Check the following quotas before you create an environment or add a host. If the host count quota or the vCPU quota is too low, the host creation fails.
+  **Host count per EVS environment.** This quota must cover every host that you plan to create in the environment. Include the temporary host that you add when you replace a failed host. For more information, see [Replace a failed host (Self-deployed)](host-replace.md).
+  **EC2 Running On-Demand Standard Instances.** This Amazon EC2 quota is measured in vCPUs. It must cover the vCPUs of all the EC2 instances that you use on Amazon EVS. For example, each `i4i.metal` instance uses 128 vCPUs. For the vCPUs of each instance type, see [Supported VCF versions and instance types](versions-provided.md).
+  **EC2 Dedicated Hosts.** If you plan to use EC2 Dedicated Hosts, this quota must cover the number of Dedicated Hosts that you intend to use in the Region.
+  **IPAM netmask length.** If you configure HCX internet connectivity, your IPAM quota for the Amazon-provided contiguous public IPv4 CIDR block netmask length has a default value of /28, which is enough. You don’t need to request an increase. For more information, see [Quotas for your IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/quotas-ipam.html) in the *Amazon VPC IP Address Manager User Guide*.

For information about increasing EC2 service quotas, see [Request an increase](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-resource-limits.html#request-increase) in the *Amazon EC2 User Guide*.

**Note**  
Amazon CloudWatch collects AWS usage metrics for Amazon EVS resources that have quotas (environments and hosts). For more information, see [CloudWatch Usage Metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Usage-Metrics.html) in the *Amazon CloudWatch User Guide*.

## View and request quotas in the AWS Management Console
<a name="view-service-quotas-console"></a>

To view and request quotas in the Service Quotas console, do the following.

1. Open the [Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/evs/quotas).

1. In the navigation pane, choose ** AWS services**.

1. From the ** AWS services** list, search for and select **Amazon Elastic VMware Service**.

1. Choose **View quotas**.

   In the **Service quotas** list, you can see the service quota name, the applied value (if it’s available), the AWS default quota, and whether the quota value is adjustable.

1. To view more information about a service quota, such as the description, choose the quota name.

1. (Optional) To request a quota increase, do the following.

   1. Select the quota that you want to increase.

   1. Choose **Request increase at account level**.

   1. Enter or select the required information, and then choose **Request**.

For more information, see [Requesting a quota increase](https://docs.aws.amazon.com/servicequotas/latest/userguide/request-quota-increase.html) in the *Service Quotas User Guide*.

## View and request quotas with the AWS CLI
<a name="view-service-quotas-cli"></a>

Run the following command to view the default Amazon EVS quotas.

```bash
aws service-quotas list-aws-default-service-quotas \
    --query 'Quotas[*].{Adjustable:Adjustable,Name:QuotaName,Value:Value,Code:QuotaCode}' \
    --service-code evs \
    --output table
```

The returned value is the number of Amazon EVS environments or hosts that you can create in this account in the current AWS Region.

To request an increase, use the [request-service-quota-increase](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/request-service-quota-increase.html) command in the * AWS CLI Command Reference*. For the other Service Quotas commands, see [service-quotas](https://docs.aws.amazon.com/cli/latest/reference/service-quotas/index.html) in the * AWS CLI Command Reference*.