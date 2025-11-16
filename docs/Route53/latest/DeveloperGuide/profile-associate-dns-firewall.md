# Associate DNS Firewall rule groups to a

Route 53 Profile

For instructions for creating a rule group, see [Creating a rule group
and rules](resolver-dns-firewall-rule-group-adding.md "resolver-dns-firewall-rule-group-adding.md"), and then choose a tab
to associate DNS Firewall rule groups to a Route 53 Profile by using the Route 53 console, or
AWS CLI.

- [Console](#profile-rule-group-console "#profile-rule-group-console")
- [CLI](#profile-rule-group-CLI "#profile-rule-group-CLI")

Console

###### To associate

DNS Firewall rule groups

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. On the navigation bar, choose the Region where you created the
   Profile.
3. In the navigation pane, choose **Profiles**
   and on the **Profiles** table, choose the
   linked name of the Profile you want to work with.
4. On the **<Profile name>** page, choose the
   **DNS Firewall rule groups** tab and then
   **Associate**.
5. In the **DNS Firewall rule groups** section you
   can select up to 10 rule groups you have previously created. If
   you want to associate more than 10 rule groups, use the APIs.
   For more information, see [AssociateResourceToProfile](../APIReference/API_route53profiles_AssociateResourceToProfile.md "../APIReference/API_route53profiles_AssociateResourceToProfile.md").

To create new rule groups, see [Creating a rule group
and rules](resolver-dns-firewall-rule-group-adding.md "resolver-dns-firewall-rule-group-adding.md"). 6. Choose **Next**. 7. On the **Define priority** page you can set
the order in which the rule groups are processed by clicking the
pre-assigned priority number and typing in a new one. The
allowed values for the priority are between 100 and 9900.

The rule groups are evaluated starting with the lowest numeric
priority setting and going up. You can change a rule group's
priority at any time, for example to change the order of
processing or make space for other rule groups.

Choose **Submit**. 8. The association progress is displayed in the
**Status** column in the
**DNS Firewall** rule groups dialog box.

CLI
You can associate rule group to a Profile by running a AWS CLI command
like the following and using your own values for `name`
`profile-id`, `resource-arn`, and
`priority`:

`aws route53profiles associate-resource-to-profile --name
 `test-resource-association`--profile-id
`rp-4987774726example`--resource-arn
`arn:aws:route53resolver:us-east-1:123456789012:firewall-rule-group/rslvr-frg-cfe7f72example`  --resource-properties "{\"priority\":
 `102`}"`

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
