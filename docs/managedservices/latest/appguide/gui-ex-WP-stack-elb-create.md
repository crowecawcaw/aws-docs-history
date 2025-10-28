# Create an ELB Stack

Launch a public ELB.

REQUIRED DATA:

- `VpcId`: The VPC you are using, this should be the same as the previously used VPC.
- `ELBSubnetIds`: An array of subnets across which the load balancer will distribute traffic. Choose either public or private subnets.
  Find Subnet IDs with the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (CLI: list-subnet-summaries) or in the AMS Console VPCs -> VPC details page.
- `VpcId`: The VPC you are using, this should be the same as the previously used VPC.

1. On the **Create RFC** page, select the category **Deployment**,
   subcategory **Advanced Stack Components**, item **Load balancer (ELB) stack**, and click **Create**.
   Choose **Advanced** and accept all defaults (including those with no value) except those shown next.

```
**Subject**:                          WP-ELB-RFC
**ELBSubnetIds**:                     `PUBLIC_AZ1
 PUBLIC_AZ2`
**ELBScheme**                         true
**ELBCookieExpirationPeriod**         600
**VpcId**:                            `VPC_ID`
**Name**:                             WP-Public-ELB
```

2. Click **Submit** when finished.
