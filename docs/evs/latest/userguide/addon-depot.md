

# Use the Amazon EVS custom add-on depot

The Amazon Elastic VMware Service custom add-on depot provides the Amazon EVS custom vendor add-on for ESX cluster images. You get the depot URL with the `GetDepotUrl` API action, and then add the URL as a download source in vSphere Lifecycle Manager (vLCM). You use the AWS CLI or the API for this task, because the Amazon EVS console doesn’t provide the URL.

The Amazon EVS custom add-on depot doesn’t provide VMware Cloud Foundation (VCF) software. To compare the software depots, see [Software depots](evs-lifecycle-mgmt.md#evs-lifecycle-depots).

## Amazon EVS AMI and custom vendor add-on
<a name="evs-env-ami-maintenance"></a>

Amazon EVS deploys ESX hosts with a custom Amazon EVS Amazon Machine Image (AMI). The AMI contains the add-on with the packages that ESX needs to run on Amazon EC2.

When you add a host to your environment, the host has the latest available version of the add-on. If the other hosts in your cluster use an older add-on version, adding the new host can fail with an error that the host isn’t compatible with your cluster image. For the steps to fix this issue, see [Troubleshoot hosts](troubleshoot-hosts.md).

When you update an ESX cluster image in vLCM, include the add-on from the Amazon EVS custom add-on depot. Every host then keeps the add-on.

## How the depot URL and token work
<a name="addon-depot-how-it-works"></a>

When you create an Amazon EVS environment, Amazon EVS provisions an access token for the Amazon EVS custom add-on depot. The `GetDepotUrl` API action returns a URL that includes this token. The token stays active until you rotate it.

The URL of the Amazon EVS custom add-on depot is a public address. To sync the add-on, vCenter Server needs outbound internet access to that address.

**Important**  
Protect the URL and the access token like a credential, and don’t share them outside the people who manage your environment.

The URL of the Amazon EVS custom add-on depot includes the access token. If you think that the token was exposed, rotate it. For the steps, see [Rotate the depot access token](#addon-depot-rotate).

## Before you begin
<a name="addon-depot-prereqs"></a>
+ An Amazon EVS environment in the `CREATED` state.
+ IAM permissions to call the `evs:GetDepotUrl` action on the environment. See [IAM permissions](#addon-depot-iam).
+ A vSphere user with the `VMware vSphere Lifecycle Manager > Configure` privilege.

## Get the depot URL
<a name="addon-depot-get-url"></a>

1. Run the `get-depot-url` command for your environment.

   ```bash
   aws evs get-depot-url --environment-id env-abcde12345
   ```

1. Note the URL of the Amazon EVS custom add-on depot in the response.

   The following is example output.

   ```json
   {
       "depotUrl": "https://example.cloudfront.net/EXAMPLE-TOKEN/depot/vmw-depot-index.xml",
       "token": "EXAMPLE-TOKEN"
   }
   ```

## Add the depot URL to vSphere Lifecycle Manager
<a name="addon-depot-use-url"></a>

 **In the vSphere Client** 

1. Sign in to the vSphere Client.

1. Go to vSphere Lifecycle Manager.

1. Add the URL of the Amazon EVS custom add-on depot as a new download source.

1. Sync the download source so that the add-on appears in the vLCM depot.

For detailed steps, see [Add a New Download Source](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle/working-with-vsphere-lifecycle-manager-depots/add-a-new-download-source.html) in the Broadcom documentation.

You have added the Amazon EVS custom add-on depot when the add-on is available in vLCM for your cluster images.

## Rotate the depot access token
<a name="addon-depot-rotate"></a>

1. Run the `get-depot-url` command with the `--rotate` flag.

   ```bash
   aws evs get-depot-url --environment-id env-abcde12345 --rotate
   ```

1. In vLCM, replace the old download source with the new depot URL from the response.

**Important**  
After you rotate the token, the old URLs of the Amazon EVS custom add-on depot stop working within 5 minutes. You must add the new URL in vLCM before you sync the add-on again.

## IAM permissions
<a name="addon-depot-iam"></a>

To get the depot URL, your IAM identity needs permission to call the `evs:GetDepotUrl` action on the environment. The following example policy allows the action on one environment. Replace `<region-code>` with the Region where you created the environment.

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "evs:GetDepotUrl",
            "Resource": "arn:aws:evs:<region-code>:111122223333:environment/env-abcde12345"
        }
    ]
}
```

The example uses the `aws` partition. In other partitions, replace `aws` in the ARN with your partition, for example `aws-us-gov`. Anyone with this permission can get the depot URL, so grant it only to the people who manage the environment. For more policy examples, see [Amazon EVS identity-based policy examples](security-iam-id-based-policy-examples.md).

Next step: to plan an update of your VCF software, see [Update and upgrade](evs-lifecycle-mgmt.md).