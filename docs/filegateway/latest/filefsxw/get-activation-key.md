

Amazon FSx File Gateway is no longer available to new customers. Existing customers of FSx File Gateway can continue to use the service normally. For capabilities similar to FSx File Gateway, visit [this blog post](https://aws.amazon.com/blogs/storage/switch-your-file-share-access-from-amazon-fsx-file-gateway-to-amazon-fsx-for-windows-file-server/).

# Getting an activation key for your gateway
<a name="get-activation-key"></a>

To receive an activation key for your gateway, make a web request to the gateway virtual machine (VM). The VM returns a redirect that contains the activation key, which is passed as one of the parameters for the `ActivateGateway` API action to specify the configuration of your gateway. For more information, see [ActivateGateway](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_ActivateGateway.html) in the *Storage Gateway API Reference*.

**Note**  
Gateway activation keys expire in 30 minutes if unused.

The request that you make to the gateway VM includes the AWS Region where the activation occurs. The URL that's returned by the redirect in the response contains a query string parameter called `activationkey`. This query string parameter is your activation key. The format of the query string looks like the following: `http://{{gateway_ip_address}}/?activationRegion={{activation_region}}`. The output of this query returns both activation region and key.

The URL also includes `vpcEndpoint`, the VPC Endpoint ID for gateways that connect using the VPC endpoint type.

**Note**  
The AWS Storage Gateway Hardware Appliance, VM image templates, and Amazon EC2 Amazon Machine Images (AMI) come preconfigured with the HTTP services necessary to receive and respond to the web requests described on this page. It's not required or recommended to install any additional services on your gateway.

**Topics**
+ [Linux (curl)](#get-activation-key-linux-curl)
+ [Linux (bash/zsh)](#get-activation-key-linux)
+ [Microsoft Windows PowerShell](#get-activation-key-powershell)
+ [Using your local console](#using-local-console)

## Linux (curl)
<a name="get-activation-key-linux-curl"></a>

The following examples show you how to get an activation key using Linux (curl).

**Note**  
Replace the highlighted variables with actual values for your gateway. Acceptable values are as follows:  
{{gateway\_ip\_address}} - The IPv4 address of your gateway, for example `172.31.29.201`
{{gateway\_type}} - The type of gateway you want to activate, such as `STORED`, `CACHED`, `VTL`, `FILE_S3`, or `FILE_FSX_SMB`.
{{region\_code}} - The Region where you want to activate your gateway. See [Regional endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) in the *AWS General Reference Guide*. If this parameter is not specified, or if the value provided is misspelled or doesn't match a valid region, the command will default to the `us-east-1` region.
{{vpc\_endpoint}} - The VPC endpoint name for your gateway, for example `vpce-050f90485f28f2fd0-iep0e8vq.storagegateway.us-west-2.vpce.amazonaws.com`.

**To get the activation key for a public endpoint:**

```
curl "http://{{gateway_ip_address}}/?activationRegion={{region_code}}&no_redirect"
```

**To get the activation key for a VPC endpoint:**

```
curl "http://{{gateway_ip_address}}/?activationRegion={{region_code}}&vpcEndpoint={{vpc_endpoint}}&no_redirect"
```

## Linux (bash/zsh)
<a name="get-activation-key-linux"></a>

The following example shows you how to use Linux (bash/zsh) to fetch the HTTP response, parse HTTP headers, and get the activation key.

```
  
function get-activation-key() {
  local ip_address=$1
  local activation_region=$2
  if [[ -z "$ip_address" || -z "$activation_region" || -z "$gateway_type" ]]; then
    echo "Usage: get-activation-key ip_address activation_region gateway_type"
    return 1
  fi

  if redirect_url=$(curl -f -s -S -w '%{redirect_url}' "http://$ip_address/?activationRegion=$activation_region&gatewayType=$gateway_type"); then
    activation_key_param=$(echo "$redirect_url" | grep -oE 'activationKey=[A-Z0-9-]+')
    echo "$activation_key_param" | cut -f2 -d=
  else
    return 1
  fi
}
```

## Microsoft Windows PowerShell
<a name="get-activation-key-powershell"></a>

The following example shows you how to use Microsoft Windows PowerShell to fetch the HTTP response, parse HTTP headers, and get the activation key.

```
function Get-ActivationKey {
  [CmdletBinding()]
  Param(
    [parameter(Mandatory=$true)][string]$IpAddress, 
    [parameter(Mandatory=$true)][string]$ActivationRegion,
    [parameter(Mandatory=$true)][string]$GatewayType
  )
  PROCESS {
    $request = Invoke-WebRequest -UseBasicParsing -Uri "http://$IpAddress/?activationRegion=$ActivationRegion&gatewayType=$GatewayType" -MaximumRedirection 0 -ErrorAction SilentlyContinue
    if ($request) {
      $activationKeyParam = $request.Headers.Location | Select-String -Pattern "activationKey=([A-Z0-9-]+)"
      $activationKeyParam.Matches.Value.Split("=")[1]
    }
  }
}
```

## Using your local console
<a name="using-local-console"></a>

The following example shows you how to use your local console to generate and display an activation key.

**To get an activation key for your gateway from your local console**

1. Log in to your local console as *admin*.

1. After you log in and see the **AWS Appliance Activation - Configuration** main menu, select `0` to choose **Get activation key**.

1. Select **Storage Gateway** for gateway family option. 

1. When prompted, enter the AWS Region where you want to activate your gateway.

1. Enter `1` for Public or `2` for VPC endpoint as the network type.

1. Enter `1` for Standard or `2` for Federal Information Processing Standard (FIPS) as the endpoint Type.