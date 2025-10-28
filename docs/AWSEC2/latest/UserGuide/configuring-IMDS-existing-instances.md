# Modify instance metadata

options for existing instances

You can modify the instance metadata options for existing instances.

You can also create an IAM policy that prevents users from modifying the instance
metadata options on existing instances. To control which users can modify the
instance metadata options, specify a policy that prevents all users other than users
with a specified role to use the [ModifyInstanceMetadataOptions](../APIReference/API_ModifyInstanceMetadataOptions.md "../APIReference/API_ModifyInstanceMetadataOptions.md") API. For the example IAM policy, see
[Work with instance metadata](ExamplePolicies_EC2.md#iam-example-instance-metadata "ExamplePolicies_EC2.md#iam-example-instance-metadata").

###### Note

If a declarative policy was used to configure the instance metadata options, you can't
modify them directly within the account. For more information, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User
Guide._

## Require the use of IMDSv2

Use one of the following methods to modify the instance metadata options on an
existing instance to require that IMDSv2 is used when requesting
instance metadata. When IMDSv2 is required, IMDSv1 cannot be
used.

###### Note

Before requiring that IMDSv2 is used, ensure that the instance
isn't making IMDSv1 calls. The `MetadataNoToken`
CloudWatch metric tracks IMDSv1 calls. When
`MetadataNoToken` records zero IMDSv1 usage for an
instance, the instance is then ready to require IMDSv2.

Console

###### To require the use of IMDSv2 on an existing

instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select your instance.
4. Choose **Actions**, **Instance
   settings**, **Modify instance metadata
   options**.
5. In the **Modify instance metadata
   options** dialog box, do the following:
   1. For **Instance metadata
      service**, select
      **Enable**.
   2. For **IMDSv2**, choose
      **Required**.
   3. Choose **Save**.

AWS CLI

###### To require the use of IMDSv2 on an existing

instance

Use the [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") CLI command and
set the `http-tokens` parameter to
`required`. When you specify a value for
`http-tokens`, you must also set
`http-endpoint` to `enabled`.

```
aws ec2 modify-instance-metadata-options \
    --instance-id `i-1234567890abcdef0` \
    --http-tokens required \
    --http-endpoint enabled
```

PowerShell

###### To require the use of IMDSv2 on an existing

instance

Use the [Edit-EC2InstanceMetadataOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md") Cmdlet and set the
`HttpTokens` parameter to `required`.
When you specify a value for `HttpTokens`, you must
also set `HttpEndpoint` to
`enabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId `i-1234567890abcdef0` `
    -HttpTokens required `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

## Restore the use of IMDSv1

When IMDSv2 is required, IMDSv1 will not work when requesting instance
metadata. When IMDSv2 is optional, then both IMDSv2 and IMDSv1 will work.
Therefore, to restore IMDSv1, make IMDSv2 optional by using one of the following
methods.

Console

###### To restore the use of IMDSv1 on an instance

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select your instance.
4. Choose **Actions**, **Instance
   settings**, **Modify instance metadata
   options**.
5. In the **Modify instance metadata
   options** dialog box, do the following:
   1. For **Instance metadata
      service**, make sure that
      **Enable** is selected.
   2. For **IMDSv2**, choose
      **Optional**.
   3. Choose **Save**.

AWS CLI

###### To restore the use of IMDSv1 on an instance

You can use the [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") CLI command with
`http-tokens` set to `optional` to
restore the use of IMDSv1 when requesting instance
metadata.

```
aws ec2 modify-instance-metadata-options \
    --instance-id `i-1234567890abcdef0` \
    --http-tokens optional \
    --http-endpoint enabled
```

PowerShell

###### To restore the use of IMDSv1 on an instance

You can use the [Edit-EC2InstanceMetadataOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md") Cmdlet with
`HttpTokens` set to `optional` to
restore the use of IMDSv1 when requesting instance
metadata.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId `i-1234567890abcdef0` `
    -HttpTokens optional `
    -HttpEndpoint enabled).InstanceMetadataOptions

```

## Change the PUT response hop

limit

For existing instances, you can change the settings of the `PUT`
response hop limit.

Currently only the AWS CLI and AWS SDKs support changing the PUT response hop
limit.

AWS CLI

###### To change the PUT response hop limit

Use the [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") CLI command and
set the `http-put-response-hop-limit` parameter to
the required number of hops. In the following example, the hop
limit is set to `3`. Note that when specifying a
value for `http-put-response-hop-limit`, you must
also set `http-endpoint` to
`enabled`.

```
aws ec2 modify-instance-metadata-options \
    --instance-id `i-1234567890abcdef0` \
    --http-put-response-hop-limit `3` \
    --http-endpoint enabled
```

PowerShell

###### To change the PUT response hop limit

Use the [Edit-EC2InstanceMetadataOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md") Cmdlet and set the
`HttpPutResponseHopLimit` parameter to the
required number of hops. In the following example, the hop limit
is set to `3`. Note that when specifying a value for
`HttpPutResponseHopLimit`, you must also set
`HttpEndpoint` to `enabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId `i-1234567890abcdef0` `
    -HttpPutResponseHopLimit 3 `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

## Enable the IMDS

IPv4 and IPv6 endpoints

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

Currently only the AWS CLI and AWS SDKs support enabling the IMDS IPv6
endpoint after instance launch.

AWS CLI

###### To enable the IMDS IPv6 endpoint for your instance

Use the [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") CLI command and
set the `http-protocol-ipv6` parameter to
`enabled`. Note that when specifying a value for
`http-protocol-ipv6`, you must also set
`http-endpoint` to `enabled`.

```
aws ec2 modify-instance-metadata-options \
	--instance-id `i-1234567890abcdef0` \
	--http-protocol-ipv6 enabled \
	--http-endpoint enabled
```

PowerShell

###### To enable the IMDS IPv6 endpoint for your instance

Use the [Edit-EC2InstanceMetadataOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md") Cmdlet and set the
`HttpProtocolIpv6` parameter to
`enabled`. Note that when specifying a value for
`HttpProtocolIpv6`, you must also set
`HttpEndpoint` to `enabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId `i-1234567890abcdef0` `
    -HttpProtocolIpv6 enabled `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

## Turn on access

to instance metadata

You can turn on access to instance metadata by enabling the HTTP endpoint of
the IMDS on your instance, regardless of which version of the
IMDS you are using. You can reverse this change at any time by disabling
the HTTP endpoint.

Use one of the following methods to turn on access to instance metadata on an
instance.

Console

###### To turn on access to instance metadata

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select your instance.
4. Choose **Actions**, **Instance
   settings**, **Modify instance metadata
   options**.
5. In the **Modify instance metadata
   options** dialog box, do the following:
   1. For **Instance metadata
      service**, select
      **Enable**.
   2. Choose **Save**.

AWS CLI

###### To turn on access to instance metadata

Use the [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") CLI command and
set the `http-endpoint` parameter to
`enabled`.

```
aws ec2 modify-instance-metadata-options \
    --instance-id `i-1234567890abcdef0` \
    --http-endpoint enabled
```

PowerShell

###### To turn on access to instance metadata

Use the [Edit-EC2InstanceMetadataOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md") Cmdlet and set the
`HttpEndpoint` parameter to
`enabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId `i-1234567890abcdef0` `
    -HttpEndpoint enabled).InstanceMetadataOptions
```

## Turn off

access to instance metadata

You can turn off access to instance metadata by disabling the HTTP endpoint of
the IMDS on your instance, regardless of which version of the
IMDS you are using. You can reverse this change at any time by enabling
the HTTP endpoint.

Use one of the following methods to turn off access to instance metadata on an
instance.

Console

###### To turn off access to instance metadata

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose
   **Instances**.
3. Select your instance.
4. Choose **Actions**, **Instance
   settings**, **Modify instance metadata
   options**.
5. In the **Modify instance metadata
   options** dialog box, do the following:
   1. For **Instance metadata
      service**, clear
      **Enable**.
   2. Choose **Save**.

AWS CLI

###### To turn off access to instance metadata

Use the [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") CLI command and
set the `http-endpoint` parameter to
`disabled`.

```
aws ec2 modify-instance-metadata-options \
    --instance-id `i-1234567890abcdef0` \
    --http-endpoint disabled
```

PowerShell

###### To turn off access to instance metadata

Use the [Edit-EC2InstanceMetadataOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md") Cmdlet and set the
`HttpEndpoint` parameter to
`disabled`.

```
(Edit-EC2InstanceMetadataOption `
    -InstanceId `i-1234567890abcdef0` `
    -HttpEndpoint disabled).InstanceMetadataOptions
```

## Allow access to tags in instance metadata

You can allow access to tags in the instance metadata on a running or stopped
instance. For each instance, you must explicitly allow access. If access is
allowed, instance tag _keys_ must comply with
specific character restrictions, otherwise you get an error. For more
information, see [Enable access to tags in instance metadata](work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS "work-with-tags-in-IMDS.md#allow-access-to-tags-in-IMDS").
