# Configure block public access for Amazon EBS snapshots

Enable block public access for snapshots to prevent the public sharing of snapshots in the
Region. After this feature is enabled, requests to publicly share snapshots in the Region are blocked.

###### Important

Enabling block public access for snapshots in _block all sharing_
mode does not change the permissions for snapshots that are already publicly shared.
Instead, it prevents these snapshots from be publicly visible and publicly accessible.
Therefore, the attributes for these snapshots still indicate that they are publicly
shared, even though they are not publicly available.

If you later disable block public access or change the mode to _block new
sharing_, these snapshots will become publicly available again.

###### Note

This setting is configured at the account level, either directly in the account or by
using a declarative policy. It must be configured in each AWS Region where you want to
prevent the public sharing of snapshots. Using a declarative policy allows you to apply
the setting across multiple Regions simultaneously, as well as across multiple accounts
simultaneously. When a declarative policy is in use, you can't modify the setting directly
within an account. This topic describes how to configure the setting directly within an
account. For information about using declarative policies, see [Declarative
policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User Guide_.

Console

###### To configure block public access for snapshots

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **EC2 Dashboard**, and then in
   **Account attributes** (on the right-hand side), choose
   **Data protection and security**.
3. In the **Block public access for EBS snapshots** section, choose
   **Manage**.
4. Select **Block public access** and then choose one of the
   following options:
   - **Block all public access** — To block all public sharing of your
     snapshots. Users in the account can't request new public sharing. Additionally, snapshots that
     were already publicly shared are treated as private and are no longer publicly available.
   - **Block new public sharing** — To block only new public sharing of
     your snapshots. Users in the account can't request new public sharing. However, snapshots that
     were already publicly shared, remain publicly available.

5. Choose **Update**.

AWS CLI

###### To enable or modify block public access for snapshots

Use the [enable-snapshot-block-public-access](../../../cli/latest/reference/ec2/enable-snapshot-block-public-access.md "../../../cli/latest/reference/ec2/enable-snapshot-block-public-access.md")
command. For `--state` specify one of the following values:

- `block-all-sharing` — To block all public sharing of your
  snapshots. Users in the account can't request new public sharing. Additionally, snapshots that
  were already publicly shared are treated as private and are no longer publicly available.
- `block-new-sharing` — To block only new public sharing of
  your snapshots. Users in the account can't request new public sharing. However, snapshots that
  were already publicly shared, remain publicly available.

**To enable or modify block public access for snapshots for a specific Region**

```
aws ec2 enable-snapshot-block-public-access \
    --state `block-new-sharing` \
    --region `us-east-1`
```

The following is example output.

```
{
    "State": "block-new-sharing"
}
```

**To enable or modify block public access for snapshots for all Regions**

```
echo -e "Region   \t Public Access State" ; \
echo -e "-------------- \t ----------------------" ; \
for region in $(
    aws ec2 describe-regions \
        --region `us-east-1` \
        --query "Regions[*].[RegionName]" \
        --output text
    );
    do (output=$(
        aws ec2 enable-snapshot-block-public-access \
            --region $region \
            --state `block-new-sharing` \
            --output text)
        echo -e "$region \t $output"
    );
done
```

The following is example output.

```
Region           Public Access State
--------------   ----------------------
ap-south-1       block-new-sharing
eu-north-1       block-new-sharing
eu-west-3        block-new-sharing
...
```

PowerShell

###### To enable or modify block public access for snapshots

Use the [Enable-EC2SnapshotBlockPublicAccess](../../../powershell/latest/reference/items/Enable-EC2SnapshotBlockPublicAccess.md "../../../powershell/latest/reference/items/Enable-EC2SnapshotBlockPublicAccess.md") command. For `-State` specify one of the
following values:

- `block-all-sharing` — To block all public sharing of your
  snapshots. Users in the account can't request new public sharing. Additionally, snapshots that
  were already publicly shared are treated as private and are no longer publicly available.
- `block-new-sharing` — To block only new public sharing of
  your snapshots. Users in the account can't request new public sharing. However, snapshots that
  were already publicly shared, remain publicly available.

**To enable or modify block public access for snapshots for a specific Region**

```
Enable-EC2SnapshotBlockPublicAccess `
    -Region `us-east-1` `
    -State `block-new-sharing`
```

The following is example output.

```
Value
-----
block-new-sharing
```

**To enable or modify block public access for snapshots for all Regions**

```
(Get-EC2Region -Region `us-east-1`).RegionName | `
    ForEach-Object {
    [PSCustomObject]@{
        Region            = $_
        PublicAccessState = (
            Enable-EC2SnapshotBlockPublicAccess `
                -Region $_ `
                -State `block-new-sharing`)
    }
} | Format-Table -AutoSize
```

The following is example output.

```
Region         PublicAccessState
------         -----------------
ap-south-1     block-new-sharing
eu-north-1     block-new-sharing
eu-west-3      block-new-sharing
...
```
