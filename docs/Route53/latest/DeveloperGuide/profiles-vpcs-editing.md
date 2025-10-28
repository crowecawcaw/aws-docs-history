# Viewing VPCs associated to an Amazon Route 53 Profile

Choose the console tab to view and edit Route 53 Profile to VPC associations. Choose the CLI tab to
use AWS CLI to list Profile to VPC associations, or to get information about a specific
association

- [Console](#profiles-vpcs-editing-console "#profiles-vpcs-editing-console")
- [CLI](#profiles-vpcs-editing-CLI "#profiles-vpcs-editing-CLI")

Console

###### To view VPCs associated to a Profile

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Profiles**.
3. On the navigation bar, choose the Region where you created the Profile.
4. Select the button next to the name of the Profile for which you want to view the associated VPCs.
5. On the **<Profile name>** page choose the **VPCs** tab.
6. On the tab page for VPCs you can view the names, ARN and status for the associated VPCs.

CLI
You can list the VPCs the Profile is associated to by running an AWS CLI command like the
following:

`aws route53profiles list-profile-associations`

The following is an example output after you run the command:

```
{
    "ProfileAssociations": [
        {
            "CreationTime": 1709338817.148,
            "Id": "rpassoc-489ce212fexample",{
    "ProfileAssociations": [
        {
            "CreationTime": 1709338817.148,
            "Id": "rpassoc-489ce212fexample",
            "ModificationTime": 1709338974.772,
            "Name": "test-association",
            "OwnerId": "123456789012",
            "ProfileId": "rp-4987774726example",
            "ResourceId": "vpc-0af3b96b3example",
            "Status": "COMPLETE",
            "StatusMessage": "Created Profile Association"
        }
    ]
}
            "ModificationTime": 1709338974.772,
            "Name": "test-association",
            "OwnerId": "123456789012",
            "ProfileId": "rp-4987774726example",
            "ResourceId": "vpc-0af3b96b3example",
            "Status": "COMPLETE",
            "StatusMessage": "Created Profile Association"
        }
    ]
}
```

You can get information about a particular VPS the Profile is associated to by running an
AWS CLI command like the following and using your own value for
`profile-association-id`:

`aws route53profiles get-profile-association --profile-association-id `rpassoc-489ce212fexample``

The following is an example output after you run the command:

```
   "ProfileAssociation": {
        "CreationTime": 1709338817.148,
        "Id": "rrpassoc-489ce212fexample",
        "ModificationTime": 1709338974.772,
        "Name": "test-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceId": "vpc-0af3b96b3example",
        "Status": "COMPLETE",
        "StatusMessage": "Created Profile Association"
    }   ]
}
```

## Disassociating a VPC from an Amazon Route 53 Profile

Choose a tab to dissociate a Route 53 Profile from a VPC by using the Route 53 console, or AWS CLI.

- [Console](#profile-disassociating-vpc-console "#profile-disassociating-vpc-console")
- [CLI](#profile-disassociating-vpc-CLI "#profile-disassociating-vpc-CLI")

Console

###### To disassociate a VPC associated to a

Route 53 Profile

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Profiles**.
3. On the navigation bar, choose the Region where the Profile from which you want to disassociate a VPC was created.
4. Select the button next to the name of the Profile from which you want to disassociate a VPC.
5. On the **<Profile name>** page choose the **VPCs** tab.
6. On the VPCs tab page for the resource, choose the VPC you want to disassociate and then **Disassociate**.
7. In the **Disassociate resources** dialog, type in `confirm`, and then choose
   **Disassociate**.

CLIYou can dissociate a Profile from a VPC by running an AWS CLI command like the following and using your own value for
`profile-id` and `--resource-id`:

`aws route53profiles disassociate-profile --profile-id `rp-4987774726example`--resource-id`vpc-0af3b96b3example``

he following is an example output after you run the command:

```
"ProfileAssociation": {
        "CreationTime": 1710851336.527,
        "Id": "rpassoc-489ce212fexample",
        "ModificationTime": 1710851401.362,
        "Name": "test-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceId": "vpc-0af3b96b3example",
        "Status": "DELETING",
        "StatusMessage": "Deleting Profile Association"
    }
```
