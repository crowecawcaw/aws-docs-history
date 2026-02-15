# Spot Instance quotas

There are quotas for the number of running Spot Instances and pending Spot Instance requests per AWS account
per Region. After a pending Spot Instance request is fulfilled, the request no longer counts
towards the quota because the running instance is counted towards the quota.

Spot Instance quotas are managed in terms of the _number of virtual
central processing units (vCPUs)_ that your running Spot Instances are either using
or will use pending the fulfillment of open Spot Instance requests. If you terminate your Spot Instances
but do not cancel the Spot Instance requests, the requests count against your Spot Instance vCPU quota
until Amazon EC2 detects the Spot Instance terminations and closes the requests.

We provide the following quota types for Spot Instances.

| Name                                                            | Default | Adjustable                                                                                                                                                                 |
| --------------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| All DL Spot Instance Requests                                   | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-85EED4F7 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-85EED4F7") |
| All F Spot Instance Requests                                    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-88CF9481 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-88CF9481") |
| All G and VT Spot Instance Requests                             | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3819A6DF "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-3819A6DF") |
| All Inf Spot Instance Requests                                  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B5D1601B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B5D1601B") |
| All P Spot Instance Requests                                    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7212CCBC "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-7212CCBC") |
| All Standard (A, C, D, H, I, M, R, T, Z) Spot Instance Requests | 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-34B43A08 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-34B43A08") |
| All Trn Spot Instance Requests                                  | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6B0D517C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-6B0D517C") |
| All X Spot Instance Requests                                    | 0       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E3A00192 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-E3A00192") |

Even though Amazon EC2 automatically adjusts your Spot Instance quotas based on your
usage, you can request a quota increase if necessary. For example, if you intend to
launch more Spot Instances than your current quota allows, you can request a quota increase. You
can also request a quota increase if you submit a Spot Instance request and you receive the error
`Max spot instance count exceeded`. To request a quota increase, use the
Service Quotas console described in [Amazon EC2 service quotas](ec2-resource-limits.md "ec2-resource-limits.md").

You can launch any combination of instance types that meet your changing application needs.
For example, with an All Standard Spot Instance Requests quota of 256 vCPUs, you could request 32
`m5.2xlarge` Spot Instances (32 x 8 vCPUs) or 16 `c5.4xlarge` Spot Instances (16
x 16
vCPUs).

With Amazon CloudWatch metrics integration, you can monitor EC2 usage against your quotas.
You can also configure alarms to warn about approaching quotas. For more information, see [Service
Quotas and Amazon CloudWatch alarms](../../../servicequotas/latest/userguide/configure-cloudwatch.md "../../../servicequotas/latest/userguide/configure-cloudwatch.md") in the _Service
Quotas User Guide_.
