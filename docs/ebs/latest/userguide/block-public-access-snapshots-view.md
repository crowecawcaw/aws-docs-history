# View the block public access setting for Amazon EBS snapshots

Block public access can be in one of the following states for each Region in your account.

- **Block all sharing** — All public sharing of your snapshots is
  blocked. Users in the account can't request new public sharing. Additionally, snapshots that were already
  publicly shared are treated as private and are not publicly available.
- **Block new sharing** — Only new public sharing of your snapshots
  is blocked. Users in the account can't request new public sharing. However, snapshots that were already
  publicly shared, remain publicly available.
- **Unblocked** — Public sharing is not blocked. Users can publicly
  share snapshots.

Console

###### To view the setting for block public access for snapshots

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. In the navigation pane, choose **EC2 Dashboard**, and then in
   **Account attributes** (on the right-hand side), choose
   **Data protection and security**.
3. The **Block public access for EBS snapshots** section shows the
   current setting.

AWS CLI

###### To view the setting for block public access for snapshots

Use the [get-snapshot-block-public-access-state](../../../cli/latest/reference/ec2/get-snapshot-block-public-access-state.md "../../../cli/latest/reference/ec2/get-snapshot-block-public-access-state.md")
command.

- For a specific Region

```
aws ec2 get-snapshot-block-public-access-state
```

In this example output, the `ManagedBy` field indicates the entity
that configured the setting and `account` indicates that the setting was
configured directly in the account. A value of `declarative-policy`
would mean the setting was configured by a declarative policy. For more
information, see [Declarative policies](../../../organizations/latest/userguide/orgs_manage_policies_declarative.md "../../../organizations/latest/userguide/orgs_manage_policies_declarative.md") in the _AWS Organizations User Guide_.

```
{
    "State": "unblocked",
    "ManagedBy": "account"
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
        aws ec2 get-snapshot-block-public-access-state \
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

###### To view the setting for block public access for snapshots

Use the [Get-EC2SnapshotBlockPublicAccessState](../../../powershell/latest/reference/items/Get-EC2SnapshotBlockPublicAccessState.md "../../../powershell/latest/reference/items/Get-EC2SnapshotBlockPublicAccessState.md") cmdlet.

- For a specific Region

```
Get-EC2SnapshotBlockPublicAccessState -Region `us-east-1`
```

The following is example output.

```
Value
-----
block-new-sharing
```

- For all Regions

```
(Get-EC2Region -Region `us-east-1`).RegionName | `
    ForEach-Object {
    [PSCustomObject]@{
        Region            = $_
        PublicAccessState = (Get-EC2SnapshotBlockPublicAccessState -Region $_)
    }
} | Format-Table -AutoSize
```

The following is example output.

```
Region           Public Access State
--------------   ----------------------
ap-south-1       unblocked
eu-north-1       unblocked
eu-west-3        unblocked
...
```
