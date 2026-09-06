

# Permissions for multilocation canaries
<a name="CloudWatch_Synthetics_MultiLocation_Permissions"></a>

To create and manage multilocation canaries, the IAM principal must have the standard CloudWatch Synthetics permissions (see [Required roles and permissions for CloudWatch canaries](CloudWatch_Synthetics_Canaries_Roles.md)) plus the following:
+ `synthetics:ReplicateCanary`—Allows the CloudWatch Synthetics service to create, update, and delete replicas in replica Regions on your behalf. If your policy already includes `synthetics:*`, this permission is included and no additional action is required.

**Condition keys for multilocation canaries**  
You can use condition keys in IAM policies to control which Regions can be used as replica locations. The following condition keys are available:


| Condition key | Description | Type | Used with | 
| --- | --- | --- | --- | 
| synthetics:AddReplicaLocations | Filters access by the replica Regions specified in the request | ArrayOfString | synthetics:CreateCanary, synthetics:UpdateCanary | 
| synthetics:RemoveReplicaLocations | Filters access by the replica Regions being removed in the request | ArrayOfString | synthetics:UpdateCanary | 

**Example: Allow replication only to specific Regions**  
The following policy allows creating and updating canaries with replicas only in United States and Canada Regions.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "synthetics:CreateCanary",
                "synthetics:UpdateCanary"
            ],
            "Resource": "*",
            "Condition": {
                "ForAllValues:StringLike": {
                    "synthetics:AddReplicaLocations": [
                        "us-*",
                        "ca-*"
                    ]
                }
            }
        }
    ]
}
```

**Example: Deny replication to specific Regions**  
The following policy denies creating or updating canaries with replicas in `eu-west-1` or `ap-southeast-1`.

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Deny",
            "Action": [
                "synthetics:CreateCanary",
                "synthetics:UpdateCanary"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "synthetics:AddReplicaLocations": [
                        "eu-west-1",
                        "ap-southeast-1"
                    ]
                }
            }
        }
    ]
}
```

For more information about CloudWatch Synthetics permissions, see [Required roles and permissions for CloudWatch canaries](CloudWatch_Synthetics_Canaries_Roles.md).