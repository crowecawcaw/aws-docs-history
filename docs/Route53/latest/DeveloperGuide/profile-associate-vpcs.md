

# Associate a Route 53 Profile to VPCs

To associate a Route 53 Profile to a VPC, follow the guidance in this topic. Choose a tab to associate a Route 53 Profile to a VPC by using the Route 53 console, or AWS CLI. 
+ [Console](#profile-associate-vpcs-console)
+ [CLI](#profile-associate-vpcs-CLI)

------
#### [ Console ]<a name="profile-associate-vpcs-procedure"></a>

**To associate VPCs**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. On the navigation bar, choose the Region where you created the Profile.

1. On the **<Profile name>** page, choose the **VPCs** tab, and then **Associate**.

1. On the **Associate VPCs** page you can select up to 10 VPCs you have previously created. If you want to associate more than 10 VPCs, use the APIs. For more information, see [AssociateProfile](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53profiles_AssociateProfile.html).

1. (Optional) In the **Review profile prioritization** table, set the **Priority** for the new association, and change the priority of the Profiles that are already associated to the VPC if needed. To change a priority, choose the **Edit priority** (pencil) icon in the **Priority** column, enter a value from 100 to 9900, and then choose **Submit edit**. A lower value means a higher priority, and each Profile associated to a VPC must have a unique priority. For more information, see [How Route 53 Profile settings are prioritized](profiles.md#profiles-priority).

1. Choose **Associate**

1. The association progress is displayed in the **Status** column on the **VPCs** page.

------
#### [ CLI ]

To associate a Profile to a VPC, use the [associate-profile](https://docs.aws.amazon.com/cli/latest/reference/route53profiles/associate-profile.html) AWS CLI command. For example, the following command associates Profile `rp-4987774726example` to VPC `vpc-0af3b96b3example`. Use your own values for `name`, `profile-id`, and `resource-id`.

`aws route53profiles associate-profile --name test-association --profile-id rp-4987774726example --resource-id vpc-0af3b96b3example`

The following is an example output after you run the command:

```json
{
    "ProfileAssociation": {
        "CreationTime": 1709338817.148,
        "Id": "rpassoc-489ce212fexample",
        "ModificationTime": 1709338817.148,
        "Name": "test-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceId": "vpc-0af3b96b3example",
        "Priority": 100,
        "Status": "CREATING",
        "StatusMessage": "Creating Profile Association"
    }
}
```

To set the order in which VPC Resolver evaluates the Profiles associated to the VPC, add the `--priority` parameter with a value from 100 to 9900. A lower value means a higher priority. If the VPC has no other Profile associations, you can omit `--priority`, and the association gets priority 100. If the VPC already has a Profile association, `--priority` is required and must be different from the priority of every other Profile association for the VPC.

------