

# Verify environment creation

This page applies to EVS-deployed environments (VCF 5.2.x). For Self-deployed environments that run VCF 9.x, see [Deploy in Self-deployed mode](getting-started-self-deployed.md).

After you create an environment, check that Amazon Elastic VMware Service finished the deployment and that the environment and its hosts are ready.

Environment creation can take several hours. If the environment is still being created, wait and check again.

## Check the environment and its hosts
<a name="verify-env-evs-deployed-procedure"></a>

You can check the environment by using the Amazon EVS console or the AWS CLI.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Select the environment.

1. Choose the **Details** tab.

1. Check that the **Environment status** is **Passed** and the **Environment state** is **Created**. If the **Environment state** still shows **Creating**, refresh the page.

1. Choose the **Hosts** tab and check that the four hosts that you specified are listed.

1. Open a terminal session.

1. Run the following command with your environment ID and the Region that contains your resources.

   Replace the example environment ID with your own value, and replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs get-environment --environment-id env-abcde12345 --region <region-code>
   ```

   The environment is ready to use when `environmentState` is `CREATED`. If it still shows `CREATING`, run the command again. The following is a sample response.

   ```json
   {
       "environment": {
           "environmentId": "env-abcde12345",
           "environmentState": "CREATED",
           "createdAt": "2025-04-13T13:39:49.546000+00:00",
           "modifiedAt": "2025-04-13T13:40:39.355000+00:00",
           "environmentArn": "arn:aws:evs:us-east-2:111122223333:environment/env-abcde12345",
           "environmentName": "testEnv",
           "vpcId": "vpc-1234567890abcdef0",
           "serviceAccessSubnetId": "subnet-01234a1b2cde1234f",
           "vcfVersion": "VCF-5.2.2",
           "termsAccepted": true,
           "licenseInfo": [
               {
                   "solutionKey": "00000-00000-00000-abcde-11111",
                   "vsanKey": "00000-00000-00000-abcde-22222"
               }
           ],
           "siteId": "my-site-id",
           "checks": [],
           "connectivityInfo": {
               "privateRouteServerPeerings": [
                   "rsp-1234567890abcdef0",
                   "rsp-abcdef01234567890"
               ]
           },
           "vcfHostnames": {
               "vCenter": "vcf-vc01",
               "nsx": "vcf-nsx",
               "nsxManager1": "vcf-nsxm01",
               "nsxManager2": "vcf-nsxm02",
               "nsxManager3": "vcf-nsxm03",
               "nsxEdge1": "vcf-edge01",
               "nsxEdge2": "vcf-edge02",
               "sddcManager": "vcf-sddcm01",
               "cloudBuilder": "vcf-cb01"
           },
           "credentials": []
       }
   }
   ```

   The ARN in the sample uses the `aws` partition. In other partitions, the ARN starts with that partition name.

1. List the hosts in the environment and check that the four hosts that you specified are listed.

   Replace the example environment ID with your own value, and replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws evs list-environment-hosts --environment-id env-abcde12345 --region <region-code>
   ```

The environment is ready when its state is **Created** (`CREATED`). In the console, its status also shows **Passed**.

## If the environment status is Failed
<a name="verify-env-evs-deployed-failed"></a>

When the environment status is **Failed**, the console shows the results of the environment status checks. The checks are **Key re-use**, **Host count**, **Key coverage**, and **Reachability**. For what each check means, see [Monitor environment status](evs-env-status-check.md). For causes and solutions, see [Troubleshoot environment status checks](troubleshoot-status-checks.md).

## Next steps
<a name="verify-env-evs-deployed-next"></a>

After you verify the environment, complete the following tasks.
+ Explicitly associate the Amazon EVS VLAN subnets with a route table in your VPC. NSX connectivity requires this association. For more information, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).
+ Retrieve the VMware Cloud Foundation (VCF) credentials and sign in to the management appliances. For more information, see [Retrieve VCF credentials and access appliances](access-vcf.md).
+ If you chose HCX internet connectivity, associate Elastic IP addresses with the public HCX VLAN subnet. For more information, see [Configure HCX public internet connectivity](evs-env-hcx-internet-access.md).
+ If you connect to on-premises networks through a transit gateway, update the transit gateway route tables. For more information, see [Set up VPC Route Server and on-premises connectivity](network-route-server.md).