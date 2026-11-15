

# Updating the priority of a Route 53 Profile association with a VPC
<a name="profiles-vpc-update-priority"></a>

When more than one Profile is associated to a VPC, the priority of each association determines the order in which VPC Resolver evaluates the Profiles. The priority is a value from 100 to 9900, a lower value means a higher priority, and each Profile association for a VPC must have a unique priority. For more information, see [How Route 53 Profile settings are prioritized](profiles.md#profiles-priority).

Only the account that associated the Profile to the VPC can change the priority of the association. While the change propagates, the association status is `UPDATING`. When the new priority is in effect, the status changes to `COMPLETE`.

If you associate a Profile that another account shared with you to one of your VPCs, your account sets the priority of that association, and only your account can change it. The account that owns the Profile can't change the priority.

Because each Profile association for a VPC must have a unique priority, you can't swap the priorities of two associations in a single request. To swap them, make these three changes:

1. Change the priority of the first association to a temporary value that no other association for the VPC uses.

1. Change the priority of the second association to the original priority of the first association.

1. Change the priority of the first association to the original priority of the second association.

You can make these changes in the console, the AWS CLI, or the API. On the **Associated VPC: <VPC ID>** page in the console, you change one priority at a time.

When you associate a Profile to a VPC in the console, you can also change the priorities of the Profiles that are already associated to the VPC, and the console makes the changes in an order that avoids duplicate priorities. If one of the changes fails, a Profile might be left at a temporary priority, so check the priorities of the VPC's Profiles and set them again. For more information, see [Associate a Route 53 Profile to VPCs](profile-associate-vpcs.md).

Choose a tab to update the priority by using the Route 53 console or the AWS CLI.

------
#### [ Console ]<a name="profiles-vpc-update-priority-procedure"></a>

**To update the priority of a VPC association**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Profiles**.

1. On the navigation bar, choose the Region where you created the Profile.

1. Choose the **Associated VPCs** tab, and then choose the ID of the VPC you want to work with. You can also choose the linked name of a Profile, choose the **VPCs** tab, and then choose the name of the VPC.

1. On the **Associated VPC: <VPC ID>** page, in the **Associated profiles** table, find the Profile whose priority you want to change. If the association status is **Complete** or **Updating**, choose the **Edit priority** (pencil) icon in the **Priority** column.

1. Enter a new **Priority** value from 100 to 9900, and then choose **Submit edit**.

------
#### [ CLI ]

To view the Profiles that are associated to a VPC and the priority of each association, use the [list-profile-associations](https://docs.aws.amazon.com/cli/latest/reference/route53profiles/list-profile-associations.html) AWS CLI command. For example, the following command lists the Profiles that are associated to VPC `vpc-0af3b96b3example`.

`aws route53profiles list-profile-associations --resource-id vpc-0af3b96b3example`

The following is an example output after you run the command:

```
{
    "ProfileAssociations": [
        {
            "CreationTime": 1709338526.311,
            "Id": "rpassoc-7c1a5e93dexample",
            "ModificationTime": 1709338702.645,
            "Name": "shared-services-association",
            "OwnerId": "123456789012",
            "ProfileId": "rp-6ffe47d5example",
            "ResourceId": "vpc-0af3b96b3example",
            "Priority": 100,
            "Status": "COMPLETE",
            "StatusMessage": "Created Profile Association"
        },
        {
            "CreationTime": 1709338817.148,
            "Id": "rpassoc-489ce212fexample",
            "ModificationTime": 1709338974.772,
            "Name": "test-association",
            "OwnerId": "123456789012",
            "ProfileId": "rp-4987774726example",
            "ResourceId": "vpc-0af3b96b3example",
            "Priority": 200,
            "Status": "COMPLETE",
            "StatusMessage": "Created Profile Association"
        }
    ]
}
```

To update the priority of a Profile association with a VPC, use the [update-profile-association](https://docs.aws.amazon.com/cli/latest/reference/route53profiles/update-profile-association.html) AWS CLI command. For example, the following command changes the priority of association `rpassoc-489ce212fexample` to 150.

`aws route53profiles update-profile-association --profile-association-id rpassoc-489ce212fexample --priority 150`

The following is an example output after you run the command:

```
{
    "ProfileAssociation": {
        "CreationTime": 1709338817.148,
        "Id": "rpassoc-489ce212fexample",
        "ModificationTime": 1709339188.402,
        "Name": "test-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceId": "vpc-0af3b96b3example",
        "Priority": 150,
        "Status": "UPDATING",
        "StatusMessage": "Updating Profile Association"
    }
}
```

------