# Viewing and updating Amazon Route 53 Profiles

Choose the console tab to view and edit Route 53 Profile. Choose the CLI tab to use AWS CLI to list Profiles you own,
are shared by you, or shared to you.

- [Console](#profile-editing-console "#profile-editing-console")
- [CLI](#profile-editing-CLI "#profile-editing-CLI")

Console

###### Viewing and updating Route 53 Profiles

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Profiles**.
3. Select the button next to the name of the Profile you want to view or edit.
4. On the **<Profile name>** page you can view the currently associated
   DNS resources, associate new ones, and edit the tags and VPC
   configurations.

CLI
You can list the Profiles by running a AWS CLI command like the following:

`aws route53profiles list-profiles`

The following is an example output after you run the command:

```
{
    "ProfileSummaries": [
        {
            "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-4987774726example",
            "Id": "rp-4987774726example",
            "Name": "test",
            "ShareStatus": "NOT_SHARED"
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

## Deleting a Amazon Route 53 Profile

Choose a tab to delete a Route 53 Profile by using the Route 53 console, or AWS CLI.

- [Console](#profile-delete-console "#profile-delete-console")
- [CLI](#profile-delete-CLI "#profile-delete-CLI")

Console

###### To delete a Route 53 Profile

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Profiles**.
3. Select the button next to the name of the Profile you want to delete, and then choose **Delete**.

###### Important

You can't delete a Profile if it is associated to VPCs. Additionally, if the Profile is
shared to another AWS account, any VPCs that the Profile
configurations are associated to, will lose those configurations. 4. On the **Delete <Profile name>** dialog, type in
`confirm`, and then choose
**Delete**.

CLI

###### Important

You can't delete a Profile if it is associated to VPCs. Additionally, if the Profile is
shared to another AWS account, any VPCs that the Profile
configurations are associated to, will lose those configurations.

You can delete a Profile by running an AWS CLI command like the following and using your
own value for `profile-id`:

`aws route53profiles delete-profile --profile-id `rp-6ffe47d5example``

The following is an example output after you run the command:

```
{
    "Profile": {
        "Arn": "arn:aws:route53profiles:us-east-1:123456789012:profile/rp-6ffe47d5example",
        "ClientToken": "0a15fec0-05d9-4f78-bec0-EXAMPLE11111",
        "CreationTime": 1710850903.578,
        "Id": "rp-6ffe47d5example",
        "ModificationTime": 1710850903.578,
        "Name": "test",
        "OwnerId": "123456789012",
        "ShareStatus": "NOT_SHARED",
        "Status": "DELETED",
        "StatusMessage": "Deleted Profile"
    }
}
```
