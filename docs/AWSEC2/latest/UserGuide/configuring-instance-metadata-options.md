

# Configure the Instance Metadata Service options
<a name="configuring-instance-metadata-options"></a>

The Instance Metadata Service (IMDS) runs locally on every EC2 instance. The *instance metadata options* refer to a set of configurations that control the accessibility and behavior of the IMDS on an EC2 instance.

You can configure the following instance metadata options on each instance:

**Instance metadata service (IMDS)**: `enabled` \| `disabled`  
You can enable or disable the IMDS on an instance. When disabled, you or any code won't be able to access the instance metadata on the instance.  
The IMDS has two endpoints on an instance: IPv4 (`169.254.169.254`) and IPv6 (`[fd00:ec2::254]`). When you enable the IMDS, the IPv4 endpoint is automatically enabled. If you want to enable the IPv6 endpoint, you need to do so explicitly.

**IMDS IPv6 endpoint**: `enabled` \| `disabled`  
You can explicitly enable the IPv6 IMDS endpoint on an instance. When the IPv6 endpoint is enabled, the IPv4 endpoint remains enabled. The IPv6 endpoint is only supported on [Nitro-based instances](instance-types.md#instance-hypervisor-type) in [IPv6-supported subnets](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-ip-address-range) (dual stack or IPv6 only).

**Metadata version**: `IMDSv1 or IMDSv2 (token optional)` \| `IMDSv2 only (token required)`  
When requesting instance metadata, IMDSv2 calls require a token. IMDSv1 calls do not require a token. You can configure an instance to allow either IMDSv1 or IMDSv2 calls (where a token is optional), or to only allow IMDSv2 calls (where a token is required).

**Metadata response hop limit**: `1`–`64`  
The hop limit is the number of network hops that the PUT response is allowed to make. You can set the hop limit to a minimum of `1` and a maximum of `64`. In a container environment, a hop limit of `1` can cause issues. For information about how to mitigate these issues, see the information about container environments under [Instance metadata access considerations](instancedata-data-retrieval.md#imds-considerations).

**Access to tags in instance metadata**: `enabled` \| `disabled`  
You can enable or disable access to the instance's tags from an instance's metadata. For more information, see [View tags for your EC2 instances using instance metadata](work-with-tags-in-IMDS.md).

To view an instance's current configuration, see [Query instance metadata options for existing instances](instancedata-data-retrieval.md#query-IMDS-existing-instances).

## Where to configure instance metadata options
<a name="where-to-configure-instance-metadata-options"></a>

Instance metadata options can be configured at different levels, as follows:
+ **Account** – You can set default values for the instance metadata options at the account level for each AWS Region. When an instance is launched, the instance metadata options are automatically set to the account-level values. You can change these values at launch. Account-level default values do not affect existing instances.
+ **AMI** – You can set the `imds-support` parameter to `v2.0` when you register or modify an AMI. When an instance is launched with this AMI, the instance metadata version is automatically set to IMDSv2 and the hop limit is set to 2.
+ **Instance** – You can change all the instance metadata options on an instance at launch, overriding the default settings. You can also change the instance metadata options after launch on a running or stopped instance. Note that changes may be restricted by an IAM or SCP policy.

For more information, see [Configure instance metadata options for new instances](configuring-IMDS-new-instances.md) and [Modify instance metadata options for existing instances](configuring-IMDS-existing-instances.md).

## Order of precedence for instance metadata options
<a name="instance-metadata-options-order-of-precedence"></a>

The value for each instance metadata option is determined at instance launch, following a hierarchical order of precedence. The hierarchy, with the highest precedence at the top, is as follows:
+ **Precedence 1: Instance configuration at launch** – Values can be specified either in the launch template or in the instance configuration. Any values specified here override values specified at the account level or in the AMI.
+ **Precedence 2: Account settings** – If a value is not specified at instance launch, then it is determined by the account-level settings (which are set for each AWS Region). Account-level settings either include a value for each metadata option, or indicate no preference at all.
+ **Precedence 3: AMI configuration** – If a value is not specified at instance launch or at the account level, then it is determined by the AMI configuration. This applies only to `HttpTokens` and `HttpPutResponseHopLimit`.

Each metadata option is evaluated separately. The instance can be configured with a mix of direct instance configuration, account-level defaults, and the configuration from the AMI.

You can change the value of any metadata option after launch on a running or stopped instance, unless changes are restricted by an IAM or SCP policy.

**Note**  
The account-level IMDSv2 enforcement setting is evaluated after the order of precedence has determined the instance's IMDS settings. When IMDSv2 enforcement is enabled, instances enabled with IMDSv1 will fail. For more information about enforcement, see [Enforce IMDSv2 at the account level](configuring-IMDS-new-instances.md#enforce-imdsv2-at-the-account-level).

**Warning**  
If IMDSv2 enforcement is enabled and `httpTokens` has not been set to `required` in either the instance configuration at launch, the account settings, or the AMI configuration, your launch will fail.

**Example 1 – Determine values for metadata options**

In this example, an EC2 instance is launched into a Region where the `HttpPutResponseHopLimit` is set to `1` at the account level. The specified AMI has `ImdsSupport` set to `v2.0`. No metadata options are specified directly on the instance at launch. The instance is launched with the following metadata options:

```
"MetadataOptions": {
    ...
    "HttpTokens": "required",
    "HttpPutResponseHopLimit": 1,
    ...
```

These values were determined as follows:
+ **No metadata options specified at launch:** During the launch of the instance, specific values for the metadata options were not provided either in the instance launch parameters or in the launch template.
+ **Account settings take next precedence:** In the absence of specific values specified at launch, the settings at the account level within the Region take precedence. This means that the default values configured at the account level are applied. In this case, the `HttpPutResponseHopLimit` was set to `1`.
+ **AMI settings take last precedence:** In the absence of a specific value specified at launch or at the account level for `HttpTokens` (the instance metadata version), the AMI setting is applied. In this case, the AMI setting `ImdsSupport: v2.0` determined that `HttpTokens` was set to `required`. Note that while the AMI setting `ImdsSupport: v2.0` is designed to set `HttpPutResponseHopLimit: 2`, it was overridden by the account-level setting `HttpPutResponseHopLimit: 1`, which has higher precedence.

**Example 2 – Determine values for metadata options**

In this example, the EC2 instance is launched with the same settings as in the previous Example 1, but with `HttpTokens` set to `optional` directly on the instance at launch. The instance is launched with the following metadata options:

```
"MetadataOptions": {
    ...
    "HttpTokens": "optional",
    "HttpPutResponseHopLimit": 1,
    ...
```

The value for `HttpPutResponseHopLimit` is determined in the same way as in Example 1. However, the value for `HttpTokens` is determined as follows: Metadata options configured on the instance at launch take first precedence. Even though the AMI was configured with `ImdsSupport: v2.0` (in other words, `HttpTokens` is set to `required`), the value specified on the instance at launch (`HttpTokens` set to `optional`) took precedence.

**Example 3 – Determine values for metadata options with HttpTokensEnforced enabled**

In this example, the account in the Region has `HttpTokens = required` and `HttpTokensEnforced = enabled`.

Consider the following EC2 instance launch attempts:
+ Launch attempt with `HttpTokens` set to `optional` – The launch fails because the account-level enforcement is enabled (`HttpTokensEnforced = enabled`) and the launch parameter takes precedence over the account default.
+ Launch attempt with `HttpTokens` set to `required` – The launch succeeds because it complies with the account-level enforcement. 
+ Launch attempt with no `HttpTokens` value specified – The launch succeeds because the value defaults to `required` based on the account settings. 

### Set the instance metadata version
<a name="metadata-version-order-of-precedence"></a>

When an instance is launched, the value for the instance *metadata version* is either **IMDSv1 or IMDSv2 (token optional)** (`httpTokens=optional`) or **IMDSv2 only (token required) (`httpTokens=required`) **.

At instance launch, you can either manually specify the value for the metadata version, or use the default value. If you manually specify the value, it overrides any defaults. If you opt not to manually specify the value, it will be determined by a combination of default settings.

The following flowchart shows how the metadata version for an instance at launch is determined by the settings at the different levels of the configuration and where enforcement is evaluated. The table that follows provides the specific settings at each level.

![A flowchart that shows the evaluation points for the instance metadata version and IMDSv2 enforcement.](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/images/imds-defaults-launch-flow.png)


The table shows how the metadata version for an instance at launch (indicated by **Resulting instance configuration** in column 4) is determined by the settings at the different levels of configuration. The order of precedence is from left to right, where the first column takes the highest precedence, as follows:
+ Column 1: **Launch parameter** – Represents the setting on the instance that you manually specify at launch.
+ Column 2: **Account level default** – Represents the setting for the account.
+ Column 3: **AMI default** – Represents the setting on the AMI.


| Launch parameter | Account level default | AMI default | Resulting instance configuration | 
| --- | --- | --- | --- | 
| V2 only (token required) | No preference | V2 only | V2 only | 
| V2 only (token required) | V2 only | V2 only | V2 only | 
| V2 only (token required) | V1 or V2 | V2 only | V2 only | 
| V1 or V2 (token optional) | No preference | V2 only | V1 or V2 | 
| V1 or V2 (token optional) | V2 only | V2 only | V1 or V2 | 
| V1 or V2 (token optional) | V1 or V2 | V2 only | V1 or V2 | 
| Not set | No preference | V2 only | V2 only | 
| Not set | V2 only | V2 only | V2 only | 
| Not set | V1 or V2 | V2 only | V1 or V2 | 
| V2 only (token required) | No preference | null | V2 only | 
| V2 only (token required) | V2 only | null | V2 only | 
| V2 only (token required) | V1 or V2 | null | V2 only | 
| V1 or V2 (token optional) | No preference | null | V1 or V2 | 
| V1 or V2 (token optional) | V2 only | null | V1 or V2 | 
| V1 or V2 (token optional) | V1 or V2 | null | V1 or V2 | 
| Not set | No preference | null | V1 or V2 | 
| Not set | V2 only | null | V2 only | 
| Not set | V1 or V2 | null | V1 or V2 | 

## Use IAM condition keys to restrict instance metadata options
<a name="iam-condition-keys-and-imds"></a>

You can use IAM condition keys in an IAM policy or SCP as follows:
+ Allow an instance to launch only if it's configured to require the use of IMDSv2
+ Restrict the number of allowed hops
+ Turn off access to instance metadata

**Topics**
+ [Where to configure instance metadata options](#where-to-configure-instance-metadata-options)
+ [Order of precedence for instance metadata options](#instance-metadata-options-order-of-precedence)
+ [Use IAM condition keys to restrict instance metadata options](#iam-condition-keys-and-imds)
+ [Configure instance metadata options for new instances](configuring-IMDS-new-instances.md)
+ [Modify instance metadata options for existing instances](configuring-IMDS-existing-instances.md)

**Note**  
You should proceed cautiously and conduct careful testing before making any changes. Take note of the following:  
If you enforce the use of IMDSv2, applications or agents that use IMDSv1 for instance metadata access will break.
If you turn off all access to instance metadata, applications or agents that rely on instance metadata access to function will break.
For IMDSv2, you must use `/latest/api/token` when retrieving the token.
(Windows only) If your PowerShell version is earlier than 4.0, you must [update to Windows Management Framework 4.0](https://devblogs.microsoft.com/powershell/windows-management-framework-wmf-4-0-update-now-available-for-windows-server-2012-windows-server-2008-r2-sp1-and-windows-7-sp1/) to require the use of IMDSv2.