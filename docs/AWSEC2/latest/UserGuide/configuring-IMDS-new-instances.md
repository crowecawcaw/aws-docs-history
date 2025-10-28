# Configure instance metadata options

for new instances

You can configure the following instance metadata options for new
instances.

###### Options

- [Require the use of
  IMDSv2](#configure-IMDS-new-instances "#configure-IMDS-new-instances")
- [Enable the
  IMDS IPv4 and IPv6 endpoints](#configure-IMDS-new-instances-ipv4-ipv6-endpoints "#configure-IMDS-new-instances-ipv4-ipv6-endpoints")
- [Turn
  off access to instance metadata](#configure-IMDS-new-instances--turn-off-instance-metadata "#configure-IMDS-new-instances--turn-off-instance-metadata")
- [Allow
  access to tags in instance metadata](#configure-IMDS-new-instances-tags-in-instance-metadata "#configure-IMDS-new-instances-tags-in-instance-metadata")

###### Note

The settings for these options are configured at the account level, either directly in the
account or by using a declarative policy. They must be configured in each
AWS Region where you want to configure instance metadata options. Using a
declarative policy allows you to apply the settings across multiple Regions
simultaneously, as well as across multiple accounts simultaneously. When a
declarative policy is in use, you can't modify the settings directly within an
account. This topic describes how to configure the settings directly within an
account. For information about using declarative policies, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User
Guide._

## Require the use of

IMDSv2

You can use the following methods to require the use of IMDSv2 on your
new instances.

###### To require IMDSv2

- [Set IMDSv2 as the
  default for the account](#set-imdsv2-account-defaults "#set-imdsv2-account-defaults")
- [Configure
  the instance at launch](#configure-IMDS-new-instances-instance-settings "#configure-IMDS-new-instances-instance-settings")
- [Configure
  the AMI](#configure-IMDS-new-instances-ami-configuration "#configure-IMDS-new-instances-ami-configuration")
- [Use an IAM
  policy](#configure-IMDS-new-instances-iam-policy "#configure-IMDS-new-instances-iam-policy")

### Set IMDSv2 as the

default for the account

You can set the default version for the instance metadata service (IMDS)
at the account level for each AWS Region. This means that when you launch
a _new_ instance, the instance metadata
version is automatically set to the account-level default. However, you can
manually override the value at launch or after launch. For more information
about how the account-level settings and manual overrides affect an
instance, see [Order of precedence
for instance metadata options](configuring-instance-metadata-options.md#instance-metadata-options-order-of-precedence "configuring-instance-metadata-options.md#instance-metadata-options-order-of-precedence").

###### Note

Setting the account-level default does not reset _existing_ instances. For example, if you set
the account-level default to IMDSv2, any existing instances that
are set to IMDSv1 are not affected. If you want to change the
value on existing instances, you must manually change the value on the
instances themselves.

You can set the account default for the instance metadata version to
IMDSv2 so that all _new_ instances
in the account launch with IMDSv2 required, and IMDSv1 will
be disabled. With this account default, when you launch an instance, the
following are the default values for the instance:

- Console: **Metadata version** is set to
  **V2 only (token required)** and
  **Metadata response hop limit** is set to
  **2**.
- AWS CLI: `HttpTokens` is set to `required` and
  `HttpPutResponseHopLimit` is set to `2`.

###### Note

Before setting the account default to IMDSv2, ensure that your
instances do not depend on IMDSv1. For more information, see
[Recommended path to
requiring IMDSv2](instance-metadata-transition-to-version-2.md#recommended-path-for-requiring-imdsv2 "instance-metadata-transition-to-version-2.md#recommended-path-for-requiring-imdsv2").

Console

###### To set IMDSv2 as the default for the account for

the specified Region

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. To change the AWS Region, use the Region selector in
   the upper-right corner of the page.
3. In the navigation pane, choose **EC2
   Dashboard**.
4. Under **Account attributes**, choose
   **Data protection and
   security**.
5. Next to **IMDS defaults**, choose
   **Manage**.
6. On the **Manage IMDS defaults** page,
   do the following:
   1. For **Instance metadata
      service**, choose
      **Enabled**.
   2. For **Metadata version**,
      choose **V2 only (token
      required)**.
   3. For **Metadata response hop limit**, specify
      **2** if your instances will host
      containers. Otherwise, select **No
      preference**. When no preference is
      specified, at launch, the value defaults to
      **2** if the AMI has the setting
      `ImdsSupport: v2.0`; otherwise it
      defaults to **1**.
   4. Choose **Update**.

AWS CLI

###### To set IMDSv2 as the default for the account for

the specified Region

Use the [modify-instance-metadata-defaults](../../../cli/latest/reference/ec2/modify-instance-metadata-defaults.md "../../../cli/latest/reference/ec2/modify-instance-metadata-defaults.md") command and
specify the Region in which to modify the IMDS account level
settings. Include `--http-tokens` set to
`required` and
`--http-put-response-hop-limit` set to
`2` if your instances will host containers.
Otherwise, specify `-1` to indicate no
preference. When `-1` (no preference) is
specified, at launch, the value defaults to `2`
if the AMI has the setting `ImdsSupport: v2.0`;
otherwise it defaults to `1`.

```
aws ec2 modify-instance-metadata-defaults \
    --region `us-east-1` \
    --http-tokens required \
    --http-put-response-hop-limit `2`
```

The following is example output.

```
{
    "Return": true
}
```

###### To view the default account settings for the instance

metadata options for the specified Region

Use the [get-instance-metadata-defaults](../../../cli/latest/reference/ec2/get-instance-metadata-defaults.md "../../../cli/latest/reference/ec2/get-instance-metadata-defaults.md") command and
specify the Region.

```
aws ec2 get-instance-metadata-defaults --region `us-east-1`
```

The following is example output.

```
{
    "AccountLevel": {
        "HttpTokens": "required",
        "HttpPutResponseHopLimit": 2
    },
    "ManagedBy": "account"
}
```

The `ManagedBy` field indicates the entity that
configured the settings. In this example, `account`
indicates that the settings were configured directly in the
account. A value of `declarative-policy` would mean
the settings were configured by a declarative policy. For more
information, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User Guide_.

###### To set IMDSv2 as the default for the account for

all Regions

Use the [modify-instance-metadata-defaults](../../../cli/latest/reference/ec2/modify-instance-metadata-defaults.md "../../../cli/latest/reference/ec2/modify-instance-metadata-defaults.md") command to
modify the IMDS account level settings for all Regions.
Include `--http-tokens` set to
`required` and
`--http-put-response-hop-limit` set to
`2` if your instances will host containers.
Otherwise, specify `-1` to indicate no
preference. When `-1` (no preference) is
specified, at launch, the value defaults to `2`
if the AMI has the setting `ImdsSupport: v2.0`;
otherwise it defaults to `1`.

```
echo -e "Region          \t Modified" ; \
echo -e "--------------  \t ---------" ; \
for region in $(
    aws ec2 describe-regions \
        --region us-east-1 \
        --query "Regions[*].[RegionName]" \
        --output text
    );
    do (output=$(
        aws ec2 modify-instance-metadata-defaults \
            --region $region \
            --http-tokens required \
            --http-put-response-hop-limit `2` \
            --output text)
        echo -e "$region        \t $output"
    );
done
```

The following is example output.

```
Region                   Modified
--------------           ---------
ap-south-1               True
eu-north-1               True
eu-west-3                True
...
```

###### To view the default account settings for the instance

metadata options for all Regions

Use the [get-instance-metadata-defaults](../../../cli/latest/reference/ec2/get-instance-metadata-defaults.md "../../../cli/latest/reference/ec2/get-instance-metadata-defaults.md") command.

```
echo -e "Region   \t Level          Hops    HttpTokens" ; \
echo -e "-------------- \t ------------   ----    ----------" ; \
for region in $(
    aws ec2 describe-regions \
        --region us-east-1 \
        --query "Regions[*].[RegionName]" \
        --output text
    );
    do (output=$(
        aws ec2 get-instance-metadata-defaults \
            --region $region \
            --output text)
        echo -e "$region \t $output"
    );
done
```

The following is example output.

```
Region           Level          Hops    HttpTokens
--------------   ------------   ----    ----------
ap-south-1       ACCOUNTLEVEL   2       required
eu-north-1       ACCOUNTLEVEL   2       required
eu-west-3        ACCOUNTLEVEL   2       required
...
```

PowerShell

###### To set IMDSv2 as the default for the account for

the specified Region

Use the [Edit-EC2InstanceMetadataDefault](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataDefault.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataDefault.md") command and
specify the Region in which to modify the IMDS account level
settings. Include `-HttpToken` set to
`required` and
`-HttpPutResponseHopLimit` set to
`2` if your instances will host containers.
Otherwise, specify `-1` to indicate no
preference. When `-1` (no preference) is
specified, at launch, the value defaults to `2`
if the AMI has the setting `ImdsSupport: v2.0`;
otherwise it defaults to `1`.

```
Edit-EC2InstanceMetadataDefault `
    -Region `us-east-1` `
    -HttpToken required `
    -HttpPutResponseHopLimit `2`
```

The following is example output.

```
True
```

###### To view the default account settings for the instance

metadata options for the specified Region

Use the [Get-EC2InstanceMetadataDefault](../../../powershell/latest/reference/items/Get-EC2InstanceMetadataDefault.md "../../../powershell/latest/reference/items/Get-EC2InstanceMetadataDefault.md") command and
specify the Region.

```
Get-EC2InstanceMetadataDefault -Region `us-east-1` | Format-List
```

The following is example output.

```
HttpEndpoint            :
HttpPutResponseHopLimit : `2`
HttpTokens              : required
InstanceMetadataTags    :
```

###### To set IMDSv2 as the default for the account for

all Regions

Use the [Edit-EC2InstanceMetadataDefault](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataDefault.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataDefault.md") Cmdlet to
modify the IMDS account level settings for all Regions.
Include `-HttpToken` set to `required`
and `-HttpPutResponseHopLimit` set to
`2` if your instances will host containers.
Otherwise, specify `-1` to indicate no
preference. When `-1` (no preference) is
specified, at launch, the value defaults to `2`
if the AMI has the setting `ImdsSupport: v2.0`;
otherwise it defaults to `1`.

```
(Get-EC2Region).RegionName | `
    ForEach-Object {
    [PSCustomObject]@{
        Region   = $_
        Modified = (Edit-EC2InstanceMetadataDefault `
                -Region $_ `
                -HttpToken required `
                -HttpPutResponseHopLimit `2`)
    }
} | `
Format-Table Region, Modified -AutoSize
```

Expected output

```
Region         Modified
------         --------
ap-south-1         True
eu-north-1         True
eu-west-3          True
...
```

###### To view the default account settings for the instance

metadata options for all Regions

Use the [Get-EC2InstanceMetadataDefault](../../../powershell/latest/reference/items/Get-EC2InstanceMetadataDefault.md "../../../powershell/latest/reference/items/Get-EC2InstanceMetadataDefault.md") Cmdlet.

```
(Get-EC2Region).RegionName | `
    ForEach-Object {
    [PSCustomObject]@{
        Region = $_
        HttpPutResponseHopLimit = (Get-EC2InstanceMetadataDefault -Region $_).HttpPutResponseHopLimit
        HttpTokens              = (Get-EC2InstanceMetadataDefault -Region $_).HttpTokens
    }
} | `
Format-Table -AutoSize
```

Example output

```
Region         HttpPutResponseHopLimit HttpTokens
------         ----------------------- ----------
ap-south-1                           2 required
eu-north-1                           2 required
eu-west-3                            2 required
...
```

### Configure

the instance at launch

When you [launch an
instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md"), you can configure the instance to require the use of
IMDSv2 by configuring the following fields:

- Amazon EC2 console: Set **Metadata version** to
  **V2 only (token required)**.
- AWS CLI: Set `HttpTokens` to
  `required`.

When you specify that IMDSv2 is required, you must also enable the
Instance Metadata Service (IMDS) endpoint by setting **Metadata
accessible** to **Enabled** (console) or
`HttpEndpoint` to `enabled` (AWS CLI).

In a container environment, when IMDSv2 is required, we recommend
setting the hop limit to `2`. For more information, see [Instance metadata access considerations](instancedata-data-retrieval.md#imds-considerations "instancedata-data-retrieval.md#imds-considerations").

Console

###### To require the use of IMDSv2 on a new

instance

- When launching a new instance in the Amazon EC2 console,
  expand **Advanced details**, and do the
  following:

      + For **Metadata accessible**,
       choose **Enabled**.
      + For **Metadata version**,
       choose **V2 only (token
       required)**.
      + (Container environment) For **Metadata
       response hop limit**, choose
       **2**.

  For more information, see [Advanced details](ec2-instance-launch-parameters.md#liw-advanced-details "ec2-instance-launch-parameters.md#liw-advanced-details").

AWS CLI

###### To require the use of IMDSv2 on a new

instance

The following [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") example launches a
`c6i.large` instance with
`--metadata-options` set to
`HttpTokens=required`. When you specify a
value for `HttpTokens`, you must also set
`HttpEndpoint` to `enabled`.
Because the secure token header is set to
`required` for metadata retrieval requests,
this requires the instance to use IMDSv2 when
requesting instance metadata.

In a container environment, when IMDSv2 is required,
we recommend setting the hop limit to `2` with
`HttpPutResponseHopLimit=2`.

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --instance-type `c6i.large` \
	...
    --metadata-options "HttpEndpoint=enabled,HttpTokens=required,HttpPutResponseHopLimit=2"
```

PowerShell

###### To require the use of IMDSv2 on a new

instance

The following [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") Cmdlet example launches a
`c6i.large` instance with
`MetadataOptions_HttpEndpoint` set to
`enabled` and the
`MetadataOptions_HttpTokens` parameter to
`required`. When you specify a value for
`HttpTokens`, you must also set
`HttpEndpoint` to `enabled`.
Because the secure token header is set to
`required` for metadata retrieval requests,
this requires the instance to use IMDSv2 when
requesting instance metadata.

```
New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `c6i.large` `
    -MetadataOptions_HttpEndpoint enabled `
    -MetadataOptions_HttpTokens required
```

AWS CloudFormation
To specify the metadata options for an instance using AWS CloudFormation,
see the [AWS::EC2::LaunchTemplate MetadataOptions](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.md") property
in the _AWS CloudFormation User Guide_.

### Configure

the AMI

When you register a new AMI or modify an existing AMI, you can set the
`imds-support` parameter to `v2.0`. Instances
launched from this AMI will have **Metadata version** set
to **V2 only (token required)** (console) or
`HttpTokens` set to `required` (AWS CLI). With these
settings, the instance requires that IMDSv2 is used when requesting
instance metadata.

Note that when you set `imds-support` to `v2.0`,
instances launched from this AMI will also have **Metadata response
hop limit** (console) or
`http-put-response-hop-limit` (AWS CLI) set to
**2**.

###### Important

Do not use this parameter unless your AMI software supports
IMDSv2. After you set the value to `v2.0`, you can't
undo it. The only way to "reset" your AMI is to create a new AMI from
the underlying snapshot.

###### To configure a new AMI for IMDSv2

Use one of the following methods to configure a new AMI for
IMDSv2.

AWS CLI
The following [register-image](../../../cli/latest/reference/ec2/register-image.md "../../../cli/latest/reference/ec2/register-image.md") example registers an AMI using the
specified snapshot of an EBS root volume as device
`/dev/xvda`. Specify `v2.0` for the
`imds-support` parameter so that instances
launched from this AMI will require that IMDSv2 is used
when requesting instance metadata.

```
aws ec2 register-image \
    --name `my-image` \
    --root-device-name /dev/xvda \
    --block-device-mappings DeviceName=/dev/xvda,Ebs={SnapshotId=snap-`0123456789example`} \
    --architecture x86_64 \
    **--imds-support v2.0**
```

PowerShell
The following [Register-EC2Image](../../../powershell/latest/reference/items/Register-EC2Image.md "../../../powershell/latest/reference/items/Register-EC2Image.md") Cmdlet example registers an AMI
using the specified snapshot of an EBS root volume as device
`/dev/xvda`. Specify `v2.0` for the
`ImdsSupport` parameter so that instances
launched from this AMI will require that IMDSv2 is used
when requesting instance metadata.

```
Register-EC2Image `
    -Name '`my-image`' `
    -RootDeviceName /dev/xvda `
    -BlockDeviceMapping  (
    New-Object `
        -TypeName Amazon.EC2.Model.BlockDeviceMapping `
        -Property @{
        DeviceName = '/dev/xvda';
        EBS        = (New-Object -TypeName Amazon.EC2.Model.EbsBlockDevice -Property @{
                SnapshotId = 'snap-`0123456789example`'
                VolumeType = 'gp3'
                } )
        }  ) `
    -Architecture X86_64 `
    -ImdsSupport v2.0

```

###### To configure an existing AMI for IMDSv2

Use one of the following methods to configure an existing AMI for
IMDSv2.

AWS CLI
The following [modify-image-attribute](../../../cli/latest/reference/ec2/modify-image-attribute.md "../../../cli/latest/reference/ec2/modify-image-attribute.md") example modifies an existing
AMI for IMDSv2 only. Specify `v2.0` for the
`imds-support` parameter so that instances
launched from this AMI will require that IMDSv2 is used
when requesting instance metadata.

```
aws ec2 modify-image-attribute \
    --image-id `ami-0abcdef1234567890` \
    **--imds-support v2.0**
```

PowerShell
The following [Edit-EC2ImageAttribute](../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md "../../../powershell/latest/reference/items/Edit-EC2ImageAttribute.md") Cmdlet example modifies an
existing AMI for IMDSv2 only. Specify `v2.0`
for the `imds-support` parameter so that instances
launched from this AMI will require that IMDSv2 is used
when requesting instance metadata.

```
Edit-EC2ImageAttribute `
    -ImageId `ami-0abcdef1234567890` `
    **-ImdsSupport 'v2.0'**
```

### Use an IAM

policy

You can create an IAM policy that prevents users from launching new
instances unless they require IMDSv2 on the new instance.

###### To enforce the use of IMDSv2 on all new instances by using an

IAM policy

To ensure that users can only launch instances that require the use of
IMDSv2 when requesting instance metadata, you can specify that
the condition to require IMDSv2 must be met before an instance
can be launched. For the example IAM policy, see [Work with instance metadata](ExamplePolicies_EC2.md#iam-example-instance-metadata "ExamplePolicies_EC2.md#iam-example-instance-metadata").

## Enable the

IMDS IPv4 and IPv6 endpoints

The IMDS has two endpoints on an instance: IPv4 (`169.254.169.254`)
and IPv6 (`[fd00:ec2::254]`). When you enable the IMDS, the IPv4
endpoint is automatically enabled. The IPv6 endpoint remains disabled even if
you launch an instance into an IPv6-only subnet. To enable the IPv6 endpoint,
you need to do so explicitly. When you enable the IPv6 endpoint, the IPv4
endpoint remains enabled.

You can enable the IPv6 endpoint at instance launch or after.

###### Requirements for enabling the IPv6 endpoint

- The selected instance type is a [Nitro-based instance](instance-types.md#instance-hypervisor-type "instance-types.md#instance-hypervisor-type").
- The selected subnet supports IPv6, where the subnet is either [dual stack or IPv6 only](../../../vpc/latest/userguide/configure-subnets.md#subnet-ip-address-range "../../../vpc/latest/userguide/configure-subnets.md#subnet-ip-address-range").

Use any of the following methods to launch an instance with the IMDS IPv6
endpoint enabled.

Console

###### To enable the IMDS IPv6 endpoint at instance launch

- [Launch the
  instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md") in the Amazon EC2 console with the following
  specified under **Advanced
  details**:
  - For **Metadata IPv6 endpoint**,
    choose **Enabled**.

For more information, see [Advanced details](ec2-instance-launch-parameters.md#liw-advanced-details "ec2-instance-launch-parameters.md#liw-advanced-details").

AWS CLI

###### To enable the IMDS IPv6 endpoint at instance launch

The following [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md") example launches a
`c6i.large` instance with the IPv6 endpoint
enabled for the IMDS. To enable the IPv6 endpoint, for
the `--metadata-options` parameter, specify
`HttpProtocolIpv6=enabled`. When you specify a
value for `HttpProtocolIpv6`, you must also set
`HttpEndpoint` to `enabled`.

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --instance-type `c6i.large` \
    ...
    **--metadata-options "HttpEndpoint=enabled,HttpProtocolIpv6=enabled"**
```

PowerShell

###### To enable the IMDS IPv6 endpoint at instance launch

The following [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") Cmdlet example launches a
`c6i.large` instance with the IPv6 endpoint
enabled for the IMDS. To enable the IPv6 endpoint,
specify `MetadataOptions_HttpProtocolIpv6` as
`enabled`. When you specify a value for
`MetadataOptions_HttpProtocolIpv6`, you must also
set `MetadataOptions_HttpEndpoint` to
`enabled`.

```
New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `c6i.large` `
    -MetadataOptions_HttpEndpoint enabled `
    -MetadataOptions_HttpProtocolIpv6 enabled
```

## Turn

off access to instance metadata

You can turn off access to the instance metadata by disabling the IMDS when
you launch an instance. You can turn on access later by re-enabling the IMDS.
For more information, see [Turn on access
to instance metadata](configuring-IMDS-existing-instances.md#enable-instance-metadata-on-existing-instances "configuring-IMDS-existing-instances.md#enable-instance-metadata-on-existing-instances").

###### Important

You can choose to disable the IMDS at launch or after launch. If you
disable the IMDS _at launch_, the following
might not work:

- You might not have SSH access to your instance. The
  `public-keys/0/openssh-key`, which is your instance's
  public SSH key, will not be accessible because the key is normally
  provided and accessed from EC2 instance metadata.
- EC2 user data will not be available and will not run at instance
  start. EC2 user data is hosted on the IMDS. If you disable the IMDS,
  you effectively turn off access to user data.
  To access this functionality, you can re-enable the IMDS after
  launch.

Console

###### To turn off access to instance metadata at launch

- [Launch the
  instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md") in the Amazon EC2 console with the following
  specified under **Advanced
  details**:
  - For **Metadata accessible**,
    choose **Disabled**.

For more information, see [Advanced details](ec2-instance-launch-parameters.md#liw-advanced-details "ec2-instance-launch-parameters.md#liw-advanced-details").

AWS CLI

###### To turn off access to instance metadata at launch at

launch

Launch the instance with `--metadata-options` set
to `HttpEndpoint=disabled`.

```
aws ec2 run-instances \
    --image-id `ami-0abcdef1234567890` \
    --instance-type `c6i.large` \
    ...
    **--metadata-options "HttpEndpoint=disabled"**
```

PowerShell

###### To turn off access to instance metadata at launch at

launch

The following [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md") Cmdlet example launches an instance
with `MetadataOptions_HttpEndpoint` set to
`disabled`.

```
New-EC2Instance `
    -ImageId `ami-0abcdef1234567890` `
    -InstanceType `c6i.large` `
    -MetadataOptions_HttpEndpoint disabled
```

AWS CloudFormation
To specify the metadata options for an instance using AWS CloudFormation, see
the [AWS::EC2::LaunchTemplate MetadataOptions](../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-ec2-launchtemplate-metadataoptions.md") property in
the _AWS CloudFormation User Guide_.

## Allow

access to tags in instance metadata

By default, instance tags are not accessible in the instance metadata. For
each instance, you must explicitly allow access. If access is allowed, instance
tag _keys_ must comply with specific character
restrictions, otherwise the instance launch will fail. For more information, see
[Enable access to tags in instance metadata](work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS").
