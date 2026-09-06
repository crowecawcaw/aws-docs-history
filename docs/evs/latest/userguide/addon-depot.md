

# Access the Amazon EVS Custom Addon depot
<a name="addon-depot"></a>

Amazon EVS provides a Custom Addon depot that you can configure as a download source in vSphere Lifecycle Manager (vLCM). Use the `GetDepotUrl` API action to retrieve a URL and authentication token for the depot.

**Note**  
Console support for the Custom Addon depot is not available at this time. Use the AWS CLI or API.

## How the Custom Addon depot works
<a name="_how_the_custom_addon_depot_works"></a>

When you create an Amazon EVS environment, a depot access token is automatically provisioned. You can use the `GetDepotUrl` API action to retrieve a URL that includes this token. Configure this URL as a download source in vLCM to sync and install the Amazon EVS Custom Addon.

**Note**  
The depot access token remains active until explicitly rotated using the `--rotate` flag.

## Prerequisites
<a name="_prerequisites"></a>

Before you can access the Custom Addon depot, you must have the following:
+ An Amazon EVS environment in the `CREATED` state.
+ IAM permissions to call the `evs:GetDepotUrl` action. For more information, see [Amazon EVS identity-based policy examples](security-iam-id-based-policy-examples.md).

## Getting a depot URL
<a name="_getting_a_depot_url"></a>

You can get a depot URL by using the AWS CLI.

### AWS CLI
<a name="shared_aws_cli"></a>

Use the `get-depot-url` command to retrieve a depot URL for your environment.

```
aws evs get-depot-url --environment-id env-abcde12345
```

The response includes the depot URL and authentication token:

```
{
    "depotUrl": "https://example.cloudfront.net/<token>/depot/vmw-depot-index.xml",
    "token": "<authentication-token>"
}
```

## Using the depot URL
<a name="_using_the_depot_url"></a>

After you retrieve the depot URL, configure it as a download source in vSphere Lifecycle Manager (vLCM) to sync and install the Amazon EVS Custom Addon.

1. Log in to the vSphere Client.

1. Navigate to vSphere Lifecycle Manager.

1. Add the depot URL as a new download source.

**Note**  
Your vSphere user must have the `VMware vSphere Lifecycle Manager > Configure` privilege.

For detailed instructions on adding a download source, see [Add a New Download Source](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/8-0/managing-host-and-cluster-lifecycle/working-with-vsphere-lifecycle-manager-depots/add-a-new-download-source.html) in the Broadcom documentation.

## Rotating the depot access token
<a name="_rotating_the_depot_access_token"></a>

To rotate the depot access token, use the `get-depot-url` command with the `--rotate` flag:

```
aws evs get-depot-url --environment-id env-abcde12345 --rotate
```

After rotation, previously issued depot URLs will stop working within 5 minutes. You must configure the new depot URL in vLCM.

## IAM permissions
<a name="_iam_permissions"></a>

To access the Custom Addon depot, your IAM identity must have permission to call the `evs:GetDepotUrl` action on your environment resources. For more information, see [Amazon EVS identity-based policy examples](security-iam-id-based-policy-examples.md).