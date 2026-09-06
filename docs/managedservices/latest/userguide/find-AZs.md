

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html). 

# Find availability zones (AZs) in AMS
<a name="find-AZs"></a>

**Availability Zone**: All accounts have at least two availability zones. To accurately find your availability zone names, you must first know the associated subnet ID.
+ AMS Console: In the navigation pane click **VPCs**, and then click the relevant VPC, if necessary. On the VPCs details page, select the relevant subnet in the table of subnets to open the subnet details page with the name of the associated availability zone.
+ AMS SKMS API/CLI:

  ```
  aws amsskms list-subnet-summaries --output table
  ```

  ```
  aws amsskms get-subnet --subnet-id {{SUBNET_ID}}
  ```

**Note**  
The AMS API/CLI (amscm and amsskms) endpoints are in the AWS N. Virginia Region, `us-east-1`. Depending on how your authentication is set, and what AWS Region your account and resources are in, you may need to add `--region us-east-1` when issuing commands. You may also need to add `--profile saml`, if that is your authentication method.