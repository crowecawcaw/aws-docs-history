

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Create an ELB Stack
<a name="gui-ex-WP-stack-elb-create"></a>

Launch a public ELB.

REQUIRED DATA:
+ `VpcId`: The VPC you are using, this should be the same as the previously used VPC.
+ `ELBSubnetIds`: An array of subnets across which the load balancer will distribute traffic. Choose either public or private subnets. Find Subnet IDs with the For the AMS SKMS API reference, see the **Reports** tab in the AWS Artifact Console. operation (CLI: list-subnet-summaries) or in the AMS Console VPCs -> VPC details page.
+ `VpcId`: The VPC you are using, this should be the same as the previously used VPC.

1. On the **Create RFC** page, select the category **Deployment**, subcategory **Advanced Stack Components**, item **Load balancer (ELB) stack**, and click **Create**. Choose **Advanced** and accept all defaults (including those with no value) except those shown next.

   ```
   Subject:                          WP-ELB-RFC   
   ELBSubnetIds:                     {{PUBLIC_AZ1
                                PUBLIC_AZ2}}
   ELBScheme                         true
   ELBCookieExpirationPeriod         600
   VpcId:                            {{VPC_ID}}
   Name:                             WP-Public-ELB
   ```

1. Click **Submit** when finished.