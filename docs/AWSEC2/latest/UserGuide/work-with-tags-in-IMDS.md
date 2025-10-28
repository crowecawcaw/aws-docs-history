# View tags for your EC2 instances using instance metadata

You can access an instance's tags from the instance metadata. By accessing tags from the
instance metadata, you no longer need to use the `DescribeInstances` or
`DescribeTags` API calls to retrieve tag information, which reduces your
API transactions per second, and lets your tag retrievals scale with the number of
instances that you control. Furthermore, local processes that are running on an instance
can view the instance's tag information directly from the instance metadata.

By default, tags are not available from the instance metadata; you must explicitly allow
access. You can allow access at instance launch, or after launch on a running or stopped
instance. You can also allow access to tags by specifying this in a launch template.
Instances that are launched by using the template allow access to tags in the instance
metadata.

If you add or remove an instance tag, the instance metadata is updated while the instance is
running, without needing to stop and then start the instance.

###### Tasks

- [Enable access to tags in instance metadata](#allow-access-to-tags-in-IMDS "#allow-access-to-tags-in-IMDS")
- [Retrieve tags from instance metadata](#retrieve-tags-from-IMDS "#retrieve-tags-from-IMDS")
- [Disable access to tags in instance metadata](#turn-off-access-to-tags-in-IMDS "#turn-off-access-to-tags-in-IMDS")

## Enable access to tags in instance metadata

By default, there is no access to instance tags in the instance metadata. For each
instance, you must explicitly enable access.

###### Note

If you allow access to tags in instance metadata, instance tag _keys_ are subject to specific restrictions. Non-compliance will
result in failed launches for new instances or an error for existing instances.
The restrictions are:

- Can only include letters (`a-z`, `A-Z`), numbers
  (`0-9`), and the following characters: `+ - = . , _
: @`.
- Can't contain spaces or `/`.
- Can't consist only of `.` (one period), `..`
  (two periods), or `_index`.
  For more information, see [Tag restrictions](Using_Tags.md#tag-restrictions "Using_Tags.md#tag-restrictions").

Console

###### To enable access to tags in instance metadata during instance launch

1. Follow the procedure to [launch an instance](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").
2. Expand **Advanced details**, and for **Allow tags in
   metadata**, choose
   **Enable**.
3. In the **Summary panel**, review your instance configuration, and
   then choose **Launch instance**. For more
   information, see [Launch an EC2 instance using the launch
   instance wizard in the console](ec2-launch-instance-wizard.md "ec2-launch-instance-wizard.md").

###### To enable access to tags in instance metadata after instance launch

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select your instance, and then choose **Actions**, **Instance
   settings**, **Allow tags in instance
   metadata**.
4. To allow access to tags in instance metadata, select the **Allow**
   checkbox.
5. Choose **Save**.

AWS CLI

###### To enable access to tags in instance metadata during instance launch

Use the [run-instances](../../../cli/latest/reference/ec2/run-instances.md "../../../cli/latest/reference/ec2/run-instances.md")
command and add the following `--metadata-options` option.

```
--metadata-options "InstanceMetadataTags=enabled"
```

###### To enable access to tags in instance metadata after instance launch

Use the following [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") command.

```
aws ec2 modify-instance-metadata-options \
    --instance-id `i-1234567890abcdef0` \
    --instance-metadata-tags enabled
```

###### To verify that access to tags in instance metadata is enabled

Use the [describe-instances](../../../cli/latest/reference/ec2/describe-instances.md "../../../cli/latest/reference/ec2/describe-instances.md")
command and check the value of `InstanceMetadataTags`.

```
aws ec2 describe-instances \
    --instance-ids `i-1234567890abcdef0` \
    --query "Reservations[*].Instances[].MetadataOptions[].InstanceMetadataTags"

```

The following is example output. The value is either `enabled`
or `disabled`.

```
[
    "enabled"
]
```

PowerShell

###### To enable access to tags in instance metadata during instance launch

Use the [New-EC2Instance](../../../powershell/latest/reference/items/New-EC2Instance.md "../../../powershell/latest/reference/items/New-EC2Instance.md")
cmdlet and add the following `-MetadataOptions_InstanceMetadataTags`
parameter.

```
-MetadataOptions_InstanceMetadataTags enabled
```

###### To enable access to tags in instance metadata after instance launch

Use the [Edit-EC2InstanceMetadataOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md") cmdlet.

```
Edit-EC2InstanceMetadataOption `
    -InstanceId `i-1234567890abcdef0` `
    -InstanceMetadataTags enabled
```

###### To verify that access to tags in instance metadata is enabled

Use the [Get-EC2Instance](../../../cli/latest/reference/ec2/Get-EC2Instance.md "../../../cli/latest/reference/ec2/Get-EC2Instance.md")
cmdlet and check the value of `InstanceMetadataTags`.

```
(Get-EC2Instance `
    -InstanceId `i-1234567890abcdef0`).Instances.MetadataOptions.InstanceMetadataTags.Value
```

The following is example output. The value is either `enabled`
or `disabled`.

```
enabled
```

## Retrieve tags from instance metadata

After you allow access to instance tags in the instance metadata, you can access the
`tags/instance` category from the instance metadata. For more information, see
[Access instance metadata for an EC2 instance](instancedata-data-retrieval.md "instancedata-data-retrieval.md").

IMDSv2

###### Linux

Run the following command from your Linux instance to list all
the tag keys for the instance.

```
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
    && curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/tags/instance
```

This example gets the value of a key obtained in the previous example.
The IMDSv2 request uses the stored token that was created using the
command in the previous example. The token must not be expired.

```
curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/tags/instance/`tag-key`
```

###### Windows

Run the following cmdlet from your Windows instance to list all
the tag keys for the instance.

```
$token = Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token-ttl-seconds" = "21600"} `
    -Method PUT -Uri http://169.254.169.254/latest/api/token
```

```
Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/tags/instance
```

This example gets the value of a key obtained in the previous example.
The IMDSv2 request uses the stored token that was created using the
command in the previous example. The token must not be expired.

```
Invoke-RestMethod `
    -Headers @{"X-aws-ec2-metadata-token" = $token} `
    -Method GET -Uri http://169.254.169.254/latest/meta-data/tags/instance/`tag-key`
```

IMDSv1

###### Linux

Run the following command from your Linux instance to list all
the tag keys for the instance.

```
curl http://169.254.169.254/latest/meta-data/tags/instance
```

This example gets the value of a key obtained in the previous example.

```
curl http://169.254.169.254/latest/meta-data/tags/instance/`tag-key`
```

###### Windows

Run the following cmdlet from your Windows instance to list all
the tag keys for the instance.

```
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/tags/instance
```

This example gets the value of a key obtained in the previous example.

```
Invoke-RestMethod -Uri http://169.254.169.254/latest/meta-data/tags/instance/`tag-key`
```

## Disable access to tags in instance metadata

You can disable access to instance tags in the instance metadata. You don't need
to disable access to instance tags on instance metadata at launch because it's
turned off by default.

Console

###### To disable access to tags in instance metadata

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **Instances**.
3. Select an instance, and then choose **Actions**, **Instance settings**, **Allow tags in instance metadata**.
4. To turn off access to tags in instance metadata, clear the **Allow**
   checkbox.
5. Choose **Save**.

AWS CLI

###### To disable access to tags in instance metadata

Use the following [modify-instance-metadata-options](../../../cli/latest/reference/ec2/modify-instance-metadata-options.md "../../../cli/latest/reference/ec2/modify-instance-metadata-options.md") command.

```
aws ec2 modify-instance-metadata-options \
    --instance-id `i-1234567890abcdef0` \
    --instance-metadata-tags disabled
```

PowerShell

###### To disable access to tags in instance metadata

Use the [Edit-EC2InstanceMetadataOption](../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md "../../../powershell/latest/reference/items/Edit-EC2InstanceMetadataOption.md")
cmdlet.

```
Edit-EC2InstanceMetadataOption `
    -InstanceId `i-1234567890abcdef0` `
    -InstanceMetadataTag disabled
```
