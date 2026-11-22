

# Retrieve VCF credentials and access appliances

This page applies to EVS-deployed environments (VCF 5.2.x). For Self-deployed environments that run VCF 9.x, see [Deploy in Self-deployed mode](getting-started-self-deployed.md).

Amazon Elastic VMware Service uses AWS Secrets Manager to create, encrypt, and store managed secrets in your account. The secrets hold the VMware Cloud Foundation (VCF) credentials that you need to access the VCF management appliances (vCenter Server, NSX, and SDDC Manager) and the ESX root password. Retrieve the credentials with the console or the AWS CLI, and then sign in to the appliances.

**Important**  
Amazon EVS doesn’t provide managed rotation of your secrets. We recommend that you rotate your secrets on a regular schedule so that they aren’t long-lived. For more information, see [Manage secrets](evs-env-secret-rotation.md).

## Retrieve the VCF credentials
<a name="access-vcf-retrieve"></a>

You can retrieve the credentials by using the Amazon EVS console or the AWS CLI.

**Example**  

1. Open the [Amazon EVS console](https://console.aws.amazon.com/evs).

1. In the navigation pane, choose **Environments**.

1. Choose your environment ID to open the environment details page.

1. Choose the **Management appliances** tab. The tab shows the VCF management appliances in your environment with their DNS host names and related credentials.

1. Note the credentials for the appliance that you want to access. Then, in the Secrets Manager console, open that secret and retrieve the secret value. For the steps, see [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the * AWS Secrets Manager User Guide*.

1. Open a terminal session.

1. Find the secret for the appliance. The following command lists the secrets in your account in the Region of the environment.

   Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws secretsmanager list-secrets --region <region-code>
   ```

1. Retrieve the secret value.

   In the following command, replace `<secret-name>` with the name or ARN of the secret. Replace `<region-code>` with the Region where you created the environment.

   ```bash
   aws secretsmanager get-secret-value --secret-id <secret-name> --region <region-code>
   ```

   For more information, see [Get secrets from AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets.html) in the * AWS Secrets Manager User Guide*.

## Sign in to the VCF management appliances
<a name="access-vcf-sign-in"></a>

After you retrieve the credentials, use them to sign in to SDDC Manager, vCenter Server, and NSX Manager. Use the DNS host names that you specified when you created the environment. For the steps to sign in to SDDC Manager and vCenter Server, see the following pages in the Broadcom documentation:
+  [Log in to the SDDC Manager User Interface](https://techdocs.broadcom.com/us/en/vmware-cis/vcf/vcf-5-2-and-earlier/5-2/map-for-administering-vcf-5-2/getting-started-with-sddc-manager-admin/log-in-to-the-sddc-manager-dashboard-admin.html) 
+  [How to Use and Configure Your vSphere Client](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/vcenter-and-host-management/using-the-vsphere-client/working-with-the-vsphere-client.html#GUID-CE128B59-E236-45FF-9976-D134DADC8178-en) 

You have retrieved the VCF credentials and signed in to the VCF management appliances.

You monitor the VCF components in SDDC Manager, not in the Amazon EVS console. For more information, see [Monitor environment status](evs-env-status-check.md).

To reach the console of an ESX host for troubleshooting, use the Amazon EC2 serial console. For more information, see [Troubleshoot hosts](troubleshoot-hosts.md).

## Next steps
<a name="access-vcf-next"></a>

After you sign in to the appliances, continue with the following tasks.
+ If you haven’t done so, associate the Amazon EVS VLAN subnets with a route table. NSX connectivity requires this association. For instructions, see [Associate VLAN subnets with a route table](evs-env-config-custom-rt.md).
+ Migrate your workloads to Amazon EVS with VMware HCX. For more information, see [Migrate workloads with HCX](migrate-evs-hcx.md).