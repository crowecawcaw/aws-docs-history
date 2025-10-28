# Getting an activation key for your gateway

To receive an activation key for your gateway, make a web request to the gateway virtual
machine (VM). The VM returns a redirect that contains the activation key, which is passed as one
of the parameters for the `ActivateGateway` API action to specify the configuration
of your gateway. For more information, see [ActivateGateway](../../../storagegateway/latest/APIReference/API_ActivateGateway.md "../../../storagegateway/latest/APIReference/API_ActivateGateway.md") in
the _Storage Gateway API Reference_.

###### Note

Gateway activation keys expire in 30 minutes if unused.

The request that you make to the gateway VM includes the AWS Region where the activation
occurs. The URL that's returned by the redirect in the response contains a query string
parameter called `activationkey`. This query string parameter is your activation key.
The format of the query string looks like the following:
`http://`gateway_ip_address`/?activationRegion=`activation_region``.
The output of this query returns both activation region and key.

The URL also includes `vpcEndpoint`, the VPC Endpoint ID for gateways that
connect using the VPC endpoint type.

###### Note

The AWS Storage Gateway Hardware Appliance, VM image templates, and Amazon EC2 Amazon Machine Images (AMI) come
preconfigured with the HTTP services necessary to receive and respond to the web requests
described on this page. It's not required or recommended to install any additional services on
your gateway.

###### Topics

- [Linux (curl)](#get-activation-key-linux-curl "#get-activation-key-linux-curl")
- [Linux (bash/zsh)](#get-activation-key-linux "#get-activation-key-linux")
- [Microsoft Windows PowerShell](#get-activation-key-powershell "#get-activation-key-powershell")
- [Using your local console](#using-local-console "#using-local-console")

## Linux (curl)

The following examples show you how to get an activation key using Linux (curl).

###### Note

Replace the highlighted variables with actual values for your gateway. Acceptable values
are as follows:

- `gateway_ip_address` - The IPv4 address of your gateway,
  for example `172.31.29.201`
- `gateway_type` - The type of gateway you want to activate,
  such as `STORED`, `CACHED`, `VTL`, `FILE_S3`, or
  `FILE_FSX_SMB`.
- `region_code` - The Region where you want to activate your
  gateway. See [Regional endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") in
  the _AWS General Reference Guide_. If this parameter is not
  specified, or if the value provided is misspelled or doesn't match a valid region, the
  command will default to the `us-east-1` region.
- `vpc_endpoint` - The VPC endpoint name for your gateway,
  for example
  `vpce-050f90485f28f2fd0-iep0e8vq.storagegateway.us-west-2.vpce.amazonaws.com`.

###### Public endpoint

To get an activation key for a public endpoint, use one of the following commands:

###### Standard endpoints

To get the activation key for a standard endpoint:

```
curl "http://`gateway_ip_address`/?activationRegion=`region_code`&no_redirect"
```

###### Dual-stack endpoints

To get the activation key for a dual-stack endpoint:

IPv4

```
curl "http://`gateway_ip_address`/?activationRegion&endpointType=DUALSTACK&ipVersion=ipv4&no_redirect"
```

IPv6

```
curl "http://`gateway_ip_address`/?activationRegion&endpointType=DUALSTACK&ipVersion=ipv6&no_redirect"
```

###### FIPS endpoints

To get the activation key for a FIPS endpoint:

IPv4

```
curl "http://`gateway_ip_address`/?activationRegion&endpointType=FIPS_DUALSTACK&ipVersion=ipv4&no_redirect"
```

IPv6

```
curl "http://`gateway_ip_address`/?activationRegion&endpointType=FIPS_DUALSTACK&ipVersion=ipv6&no_redirect"
```

###### VPC endpoints

To get the activation key for a VPC endpoint:

```
curl "http://`gateway_ip_address`/?activationRegion=`region_code`&vpcEndpoint=`vpc_endpoint`&no_redirect"
```

## Linux (bash/zsh)

The following example shows you how to use Linux (bash/zsh) to fetch the HTTP response,
parse HTTP headers, and get the activation key.

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

The following example shows you how to use Microsoft Windows PowerShell to fetch the HTTP
response, parse HTTP headers, and get the activation key.

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

The following examples show you how to use your local console to generate and display an
activation key.

**Amazon Linux 2 (AL2) based gateways**

You can select either standard or FIPS endpoints for gateways based on AL2.

###### Note

FIPS endpoints are not available in all AWS Regions. For more information, see [FIPS Endpoints by Service](https://aws.amazon.com/compliance/fips/ "https://aws.amazon.com/compliance/fips/").

###### To get an activation key for your AL2-based gateway from your local console

1. Log in to your local console as _admin_.
2. From the **AWS Appliance Activation -
   Configuration** main menu, select `0` to choose **Get
   activation key**.
3. Select **Storage Gateway** for gateway family option.
4. Enter the AWS Region where you want to activate your gateway.
5. For network type, enter `1` for Public or `2` for VPC.
6. For endpoint type, enter `1` for Standard or `2` for Federal Information Processing
   Standard (FIPS).

**Amazon Linux 2023 (AL2023) based gateways**

For gateways based on AL2023, the following endpoints are available:

- Standard endpoints (support IPv4 only)
- FIPS endpoints (support IPv4 only)
- Dual-stack endpoints (support IPv4 and IPv6)
- Dual-stack FIPS endpoints (support IPv4 and IPv6)

For more information, see [Endpoint types](Requirements.md#endpoint-types-fgw "Requirements.md#endpoint-types-fgw").

###### To get an activation key for your AL2023-based gateway from your local console

1. Log in to your local console. If you are connecting to your Amazon EC2 instance from a
   Windows computer, log in as _admin_.
2. From the **AWS Appliance Activation -
   Configuration** main menu, select `0` to choose **Get
   activation key**.
3. Select **Storage Gateway** for gateway family option.
4. Enter the AWS Region where you want to activate your gateway.
5. For network type, enter `1` for Public or `2` for VPC endpoint.
6. For **Select endpoint type**, **Enable FIPS?**, enter `Y` to enable FIPS or `N` to use non-FIPS endpoint.
7. For endpoint type, enter `1` for standard endpoint or `2` for dual-stack endpoint.
   1. For a dual-stack endpoint, for **Select IP version or exit:**, enter `1` for IPv4 or `2` for IPv6.
