

# Modify instance metadata options for existing instances
<a name="configuring-IMDS-existing-instances"></a>

You can modify the instance metadata options for existing instances.

You can also create an IAM policy that prevents users from modifying the instance metadata options on existing instances. To control which users can modify the instance metadata options, specify a policy that prevents all users other than users with a specified role to use the [ModifyInstanceMetadataOptions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataOptions.html) API. For the example IAM policy, see [Work with instance metadata](ExamplePolicies_EC2.md#iam-example-instance-metadata).

**Note**  
If a declarative policy was used to configure the instance metadata options, you can't modify them directly within the account. For more information, see [Declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative.html) in the *AWS Organizations User Guide.*

## Require the use of IMDSv2
<a name="modify-require-IMDSv2"></a>

Use one of the following methods to modify the instance metadata options on an existing instance to require that IMDSv2 is used when requesting instance metadata. When IMDSv2 is required, IMDSv1 cannot be used.

**Note**  
Before requiring that IMDSv2 is used, ensure that the instance isn't making IMDSv1 calls. The `MetadataNoToken` CloudWatch metric tracks IMDSv1 calls. When `MetadataNoToken` records zero IMDSv1 usage for an instance, the instance is then ready to require IMDSv2.

------
#### [ Console ]

**To require the use of IMDSv2 on an existing instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select your instance.

1. Choose **Actions**, **Instance settings**, **Modify instance metadata options**.

1. In the **Modify instance metadata options** dialog box, do the following:

   1. For **Instance metadata service**, select **Enable**.

   1. For **IMDSv2**, choose **Required**.

   1. Choose **Save**.

------
#### [ AWS CLI ]

**To require the use of IMDSv2 on an existing instance**  
Use the [modify-instance-metadata-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-metadata-options.html) CLI command and set the `http-tokens` parameter to `required`. When you specify a value for `http-tokens`, you must also set `http-endpoint` to `enabled`.

```
aws ec2 modify-instance-metadata-options \
    --instance-id {{i-1234567890abcdef0}} \
    --http-tokens required \
    --http-endpoint enabled
```

------
#### [ PowerShell ]

**To require the use of IMDSv2 on an existing instance**  
Use the [Edit-EC2InstanceMetadataOption](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.html) cmdlet and set the `HttpTokens` parameter to `required`. When you specify a value for `HttpTokens`, you must also set `HttpEndpoint` to `enabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId {{i-1234567890abcdef0}} `
    -HttpTokens required `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

------

## Restore the use of IMDSv1
<a name="modify-restore-IMDSv1"></a>

When IMDSv2 is required on an instance, using an IMDSv1 request will fail. When IMDSv2 is optional, then both IMDSv2 and IMDSv1 will work. Therefore, to restore IMDSv1, set IMDSv2 to optional (`httpTokens = optional`) using one of the following methods.

The `httpTokensEnforced` IMDS property also prevents attempts to enable IMDSv1 on an existing instance. When enabled for an account in a Region, an attempt to set `httpTokens` to `optional` will result in an `UnsupportedOperation` exception. Fore more information, see [Troubleshooting](#troubleshoot-modifying-an-imdsv1-enabled-instance-fails).

**Important**  
If your instance launches are failing due to IMDSv2 enforcement, you have two options to enable launches to succeed:  
**Launch instances as IMDSv2-only** – If the software running on the instances uses IMDSv2 only (no dependency on IMDSv1), then you can launch the instances as IMDSv2 only. To do this, configure IMDSv2 only by setting `httpTokens = required` either in the launch parameters or in the metadata defaults for the account in the Region. 
**Disable enforcement** – If your software still depends on IMDSv1, set `httpTokensEnforced` to `disabled` for the account in the Region. For more information, see [Enforce IMDSv2 at the account level](configuring-IMDS-new-instances.md#enforce-imdsv2-at-the-account-level).

------
#### [ Console ]

**To restore the use of IMDSv1 on an instance**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select your instance.

1. Choose **Actions**, **Instance settings**, **Modify instance metadata options**.

1. In the **Modify instance metadata options** dialog box, do the following:

   1. For **Instance metadata service**, make sure that **Enable** is selected.

   1. For **IMDSv2**, choose **Optional**.

   1. Choose **Save**.

------
#### [ AWS CLI ]

**To restore the use of IMDSv1 on an instance**  
You can use the [modify-instance-metadata-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-metadata-options.html) CLI command with `http-tokens` set to `optional` to restore the use of IMDSv1 when requesting instance metadata.

```
aws ec2 modify-instance-metadata-options \
    --instance-id {{i-1234567890abcdef0}} \
    --http-tokens optional \
    --http-endpoint enabled
```

------
#### [ PowerShell ]

**To restore the use of IMDSv1 on an instance**  
You can use the [Edit-EC2InstanceMetadataOption](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.html) cmdlet with `HttpTokens` set to `optional` to restore the use of IMDSv1 when requesting instance metadata.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId {{i-1234567890abcdef0}} `
    -HttpTokens optional `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

------

## Change the PUT response hop limit
<a name="modify-PUT-response-hop-limit"></a>

For existing instances, you can change the settings of the `PUT` response hop limit.

Currently only the AWS CLI and AWS SDKs support changing the PUT response hop limit.

------
#### [ AWS CLI ]

**To change the PUT response hop limit**  
Use the [modify-instance-metadata-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-metadata-options.html) CLI command and set the `http-put-response-hop-limit` parameter to the required number of hops. In the following example, the hop limit is set to `3`. Note that when specifying a value for `http-put-response-hop-limit`, you must also set `http-endpoint` to `enabled`.

```
aws ec2 modify-instance-metadata-options \
    --instance-id {{i-1234567890abcdef0}} \
    --http-put-response-hop-limit {{3}} \
    --http-endpoint enabled
```

------
#### [ PowerShell ]

**To change the PUT response hop limit**  
Use the [Edit-EC2InstanceMetadataOption](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.html) cmdlet and set the `HttpPutResponseHopLimit` parameter to the required number of hops. In the following example, the hop limit is set to `3`. Note that when specifying a value for `HttpPutResponseHopLimit`, you must also set `HttpEndpoint` to `enabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId {{i-1234567890abcdef0}} `
    -HttpPutResponseHopLimit 3 `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

------

## Enable the IMDS IPv4 and IPv6 endpoints
<a name="enable-ipv6-endpoint-for-existing-instances"></a>

The IMDS has two endpoints on an instance: IPv4 (`169.254.169.254`) and IPv6 (`[fd00:ec2::254]`). When you enable the IMDS, the IPv4 endpoint is automatically enabled. The IPv6 endpoint remains disabled even if you launch an instance into an IPv6-only subnet. To enable the IPv6 endpoint, you need to do so explicitly. When you enable the IPv6 endpoint, the IPv4 endpoint remains enabled.

You can enable the IPv6 endpoint at instance launch or after.

**Requirements for enabling the IPv6 endpoint**
+ The selected instance type is a [Nitro-based instance](instance-types.md#instance-hypervisor-type).
+ The selected subnet supports IPv6, where the subnet is either [dual stack or IPv6 only](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-ip-address-range).

Currently only the AWS CLI and AWS SDKs support enabling the IMDS IPv6 endpoint after instance launch.

------
#### [ AWS CLI ]

**To enable the IMDS IPv6 endpoint for your instance**  
Use the [modify-instance-metadata-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-metadata-options.html) CLI command and set the `http-protocol-ipv6` parameter to `enabled`. Note that when specifying a value for `http-protocol-ipv6`, you must also set `http-endpoint` to `enabled`.

```
aws ec2 modify-instance-metadata-options \
	--instance-id {{i-1234567890abcdef0}} \
	--http-protocol-ipv6 enabled \
	--http-endpoint enabled
```

------
#### [ PowerShell ]

**To enable the IMDS IPv6 endpoint for your instance**  
Use the [Edit-EC2InstanceMetadataOption](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.html) cmdlet and set the `HttpProtocolIpv6` parameter to `enabled`. Note that when specifying a value for `HttpProtocolIpv6`, you must also set `HttpEndpoint` to `enabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId {{i-1234567890abcdef0}} `
    -HttpProtocolIpv6 enabled `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

------

## Turn on access to instance metadata
<a name="enable-instance-metadata-on-existing-instances"></a>

You can turn on access to instance metadata by enabling the HTTP endpoint of the IMDS on your instance, regardless of which version of the IMDS you are using. You can reverse this change at any time by disabling the HTTP endpoint.

Use one of the following methods to turn on access to instance metadata on an instance.

------
#### [ Console ]

**To turn on access to instance metadata**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select your instance.

1. Choose **Actions**, **Instance settings**, **Modify instance metadata options**.

1. In the **Modify instance metadata options** dialog box, do the following:

   1. For **Instance metadata service**, select **Enable**.

   1. Choose **Save**.

------
#### [ AWS CLI ]

**To turn on access to instance metadata**  
Use the [modify-instance-metadata-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-metadata-options.html) CLI command and set the `http-endpoint` parameter to `enabled`.

```
aws ec2 modify-instance-metadata-options \
    --instance-id {{i-1234567890abcdef0}} \
    --http-endpoint enabled
```

------
#### [ PowerShell ]

**To turn on access to instance metadata**  
Use the [Edit-EC2InstanceMetadataOption](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.html) cmdlet and set the `HttpEndpoint` parameter to `enabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId {{i-1234567890abcdef0}} `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

------

## Turn off access to instance metadata
<a name="disable-instance-metadata-on-existing-instances"></a>

You can turn off access to instance metadata by disabling the HTTP endpoint of the IMDS on your instance, regardless of which version of the IMDS you are using. You can reverse this change at any time by enabling the HTTP endpoint.

Use one of the following methods to turn off access to instance metadata on an instance.

------
#### [ Console ]

**To turn off access to instance metadata**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Instances**.

1. Select your instance.

1. Choose **Actions**, **Instance settings**, **Modify instance metadata options**.

1. In the **Modify instance metadata options** dialog box, do the following:

   1. For **Instance metadata service**, clear **Enable**.

   1. Choose **Save**.

------
#### [ AWS CLI ]

**To turn off access to instance metadata**  
Use the [modify-instance-metadata-options](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-metadata-options.html) CLI command and set the `http-endpoint` parameter to `disabled`.

```
aws ec2 modify-instance-metadata-options \
    --instance-id {{i-1234567890abcdef0}} \
    --http-endpoint disabled
```

------
#### [ PowerShell ]

**To turn off access to instance metadata**  
Use the [Edit-EC2InstanceMetadataOption](https://docs.aws.amazon.com/powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.html) cmdlet and set the `HttpEndpoint` parameter to `disabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId {{i-1234567890abcdef0}} `
    -HttpEndpoint disabled).InstanceMetadataOptions
```

------

## Allow access to tags in instance metadata
<a name="modify-access-to-tags-in-instance-metadata-on-existing-instances"></a>

You can allow access to tags in the instance metadata on a running or stopped instance. For each instance, you must explicitly allow access. If access is allowed, instance tag *keys* must comply with specific character restrictions, otherwise you get an error. For more information, see [Enable access to tags in instance metadata](work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS).

## Troubleshooting
<a name="troubleshoot-modifying-an-imdsv1-enabled-instance-fails"></a>

### Modifying an IMDSv1-enabled instance fails
<a name="modifying-an-imdsv1-enabled-instance-fails"></a>

#### Description
<a name="modifying-an-imdsv1-enabled-instance-fails-description"></a>

You get the following error message:

`You can't launch instances with IMDSv1 because httpTokensEnforced is enabled for this account. Either launch the instance with httpTokens=required or contact your account owner to disable httpTokensEnforced using the ModifyInstanceMetadataDefaults API or the account settings in the EC2 console.`

#### Cause
<a name="modifying-an-imdsv1-enabled-instance-fails-cause"></a>

This error is thrown when you attempt to modify an existing instance to be IMDSv1 enabled (`httpTokens = optional`) in an account where the EC2 account settings or an AWS Organization declarative policy enforces the use of IMDSv2 (`httpTokensEnforced = enabled`). 

#### Solution
<a name="modifying-an-imdsv1-enabled-instance-fails-solution"></a>

If you require IMDSv1 support on existing instances, you'll need to disable IMDSv2 enforcement for the account in the Region. To disable IMDSv2 enforcement, set `HttpTokensEnforced` to `disabled`. For more information, see [ModifyInstanceMetadataDefaults](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyInstanceMetadataDefaults.html) in the Amazon EC2 API Reference. If you prefer to configure this setting using the console, see [Enforce IMDSv2 at the account level](configuring-IMDS-new-instances.md#enforce-imdsv2-at-the-account-level).

We recommend that you use IMDSv2 only (`httpTokens=required`). For more information, see [Transition to using Instance Metadata Service Version 2](instance-metadata-transition-to-version-2.md).

 