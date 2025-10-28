# Viewing and updating Route 53 resources associated to an Amazon Route 53 Profile

Choose the console tab to view the Route 53 Profile resource associations, and optionally edit the
DNS Firewall rule group priority. Choose the CLI tab to use AWS CLI to list the resource
associations and to see an example update to a priority of a DNS Firewall rule group.

- [Console](#profile-list-resource-console "#profile-list-resource-console")
- [CLI](#profile-list-resource-CLI "#profile-list-resource-CLI")

Console

###### To view and update resources associated to a Profile

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Profiles**.
3. On the navigation bar, choose the Region where you created the Profile.
4. Select the button next to the name of the Profile for which you want to view or edit the resource associations.
5. On the **<Profile name>** page choose the tab for the resource you want to view or edit,
   either , **DNS Firewall rule groups**, **Private hosted zones**,
   **Resolver rules**, or **VPC endpoints**.
6. On the tab page for a resource you can view the names, ARN and status for the associated
   resources. You can also choose the gear icon to adjust what is displayed in the
   resource table.

On the **DNS Firewall rule groups** tab page you can also choose the rule group priority entry, and
edit it to a smaller or a bigger number. The rule groups are evaluated in order starting from the lowest priority number in order to the highest priority number.

CLIYou can list resources associated to a Profile by running an AWS CLI command like the following and using your own value for
`profile-id`:

`aws route53profiles list-profile-resource-associations --profile-id `rp-4987774726example``

The following is an example output after you run the command:

```
{
    "ProfileResourceAssociations": [
        {
            "CreationTime": 1710851216.613,
            "Id": "rpr-001913120a7example",
            "ModificationTime": 1710851216.613,
            "Name": "test-resource-association",
            "OwnerId": "123456789012",
            "ProfileId": "rp-4987774726example",
            "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example",
            "ResourceProperties": "{\"priority\":102}",
            "ResourceType": "FIREWALL_RULE_GROUP",
            "Status": "COMPLETE",
            "StatusMessage": "Completed creation of Profile to DNS Firewall rule group association"
        }
    ]
}
```

You can update the priority of a DNS Firewall rule group associated to a Profile by running an AWS CLI command like the following and using your own value for
and using your own values for
`profile-resource-association-id` and `--resource-properties`:

`aws route53profiles update-profile-resource-association --profile-resource-association-id `rpr-001913120a7example`--resource-properties "{\"priority\":`105`}"`

The following is an example output after you run the command:

```
{
    "ProfileResourceAssociation": {
        "CreationTime": 1710851216.613,
        "Id": "rpr-001913120a7example",
        "ModificationTime": 1710852303.798,
        "Name": "test-resource-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example",
        "ResourceProperties": "{\"priority\":105}",
        "ResourceType": "FIREWALL_RULE_GROUP",
        "Status": "UPDATING",
        "StatusMessage": "Updating the Profile to DNS Firewall rule group association"
    }
}
```
