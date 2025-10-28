# Associate a Route 53 Profile to VPCs

To associate a Route 53 Profile to a VPC, follow the guidance in this topic.
Choose a tab to associate a Route 53 Profile to a VPC by using the Route 53 console, or AWS CLI.

- [Console](#profile-associate-vpcs-console "#profile-associate-vpcs-console")
- [CLI](#profile-associate-vpcs-CLI "#profile-associate-vpcs-CLI")

Console

###### To associate VPCs

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. On the navigation bar, choose the Region where you created the Profile.
3. On the **<Profile name>** page, choose the **VPCs**
   tab, and then **Associate**.
4. On the **Associate VPCs** page you can select up to 10 VPCs you have previously created. If you want to associate more than
   10 VPCs, use the APIs. For more information, see
   [AssociateProfile](../APIReference/API_route53profiles_AssociateProfile.md "../APIReference/API_route53profiles_AssociateProfile.md").
5. Choose **Associate**
6. The association progress is displayed in the **Status**
   column on the **VPCs** page.

CLI
You can list the Profiles by running a AWS CLI command like the following and using your own values for `name`,
`profile-id`, and `resource-id`:

`aws route53profiles associate-profile --name `test-association`--profile-id`rp-4987774726example`--resource-id`vpc-0af3b96b3example``

The following is an example output after you run the command:

```
{
    "ProfileResourceAssociation": {
        "CreationTime": 1710851216.613,
        "Id": "rpr-001913120a7example",
        "ModificationTime": 1710851216.613,
        "Name": "test-resource-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example",
        "ResourceProperties": "{\"priority\":102}",
        "ResourceType": "FIREWALL_RULE_GROUP",
        "Status": "UPDATING",
        "StatusMessage": "Updating the Profile to DNS Firewall rule group association"
    }
}
```
