# Disable block public access for Amazon EBS snapshots

Disable block public access for snapshots to allow public sharing of snapshots in the
Region. After this feature is disabled, users can publicly share snapshots in the Region.

###### Important

Enabling block public access for snapshots in _block all sharing_
mode does not change the permissions for snapshots that are already publicly shared.
Instead, it prevents these snapshots from be publicly visible and publicly accessible.
Therefore, the attributes for these snapshots still indicate that they are publicly
shared, even though they are not publicly available.

If disable block public access, these snapshots will become publicly available
again.

###### Note

This setting is configured at the account level, either directly in the account or by
using a declarative policy. It must be configured in each AWS Region where you want to
allow the public sharing of snapshots. Using a declarative policy allows you to apply the
setting across multiple Regions simultaneously, as well as across multiple accounts
simultaneously. When a declarative policy is in use, you can't modify the setting directly
within an account. This topic describes how to configure the setting directly within an
account. For information about using declarative policies, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md")
in the _AWS Organizations User Guide_.

Console

###### To disable block public access for snapshots

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **EC2 Dashboard**, and then in
   **Account attributes** (on the right-hand side), choose
   **Data protection and security**.
3. In the **Block public access for EBS snapshots** section, choose
   **Manage**.
4. Clear **Block public access** and choose **Update**.

AWS CLI

###### To disable block public access for snapshots

Use the [disable-snapshot-block-public-access](../../../cli/latest/reference/ec2/disable-snapshot-block-public-access.md "../../../cli/latest/reference/ec2/disable-snapshot-block-public-access.md")
command.

- For a specific Region

```
aws ec2 disable-snapshot-block-public-access --region `us-east-1`
```

The following is example output.

```
{
    "State": "unblocked"
}
```

- For all Regions

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
        aws ec2 disable-snapshot-block-public-access \
            --region $region \
            --output text)
        echo -e "$region \t $output"
    );
done
```

The following is example output.

```
Region           Public Access State
--------------   ----------------------
ap-south-1       unblocked
eu-north-1       unblocked
eu-west-3        unblocked
```

PowerShell

###### To disable block public access for snapshots

Use the [Disable-EC2SnapshotBlockPublicAccess](../../../powershell/latest/reference/items/Disable-EC2SnapshotBlockPublicAccess.md "../../../powershell/latest/reference/items/Disable-EC2SnapshotBlockPublicAccess.md") cmdlet.

- For a specific Region

```
Disable-EC2SnapshotBlockPublicAccess -Region `us-east-1`
```

The following is example output.

```
Value
-----
unblocked
```

- For all Regions

```
(Get-EC2Region -Region `us-east-1`).RegionName | `
    ForEach-Object {
    [PSCustomObject]@{
        Region            = $_
        PublicAccessState = (Disable-EC2SnapshotBlockPublicAccess -Region $_)
    }
} | `
Format-Table -AutoSize
```

The following is example output.

```
Region         PublicAccessState
------         -----------------
ap-south-1     unblocked
eu-north-1     unblocked
eu-west-3      unblocked
...
```
