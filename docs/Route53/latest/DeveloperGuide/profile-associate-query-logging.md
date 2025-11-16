# Associate Resolver query logging

configurations to a Route 53 Profile

For instructions on how to create a Resolver query logging configuration, see [Configuring (Resolver query
logging)](resolver-query-logging-configurations-managing.md#resolver-query-logs-configuring "resolver-query-logging-configurations-managing.md#resolver-query-logs-configuring"), and then choose a tab to
associate Resolver configuration to a Route 53 Profile by using the Route 53 console, or
AWS CLI.

- [Console](#profile-query-log-config-console "#profile-query-log-config-console")
- [CLI](#profile-query-log-config-CLI "#profile-query-log-config-CLI")

Console

###### To associate query

logging configurations

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. On the navigation bar, choose the Region where you created the
   Profile.
3. On the **Profile name** page, choose the **Resolver
   query log configurations** tab, and then **Associate**.
4. On the **Associate query logging configurations** page, in the
   **Resolver query log configurations** table, you can select
   up to three configurations that you previously created. If you want to
   associate more than three query logging configurations, use the API. For more
   information, see [AssociateResourceToProfile](../APIReference/API_route53profiles_AssociateResourceToProfile.md "../APIReference/API_route53profiles_AssociateResourceToProfile.md").
5. To create new Resolver query logging configurations, see [Configuring (Resolver query
   logging)](resolver-query-logging-configurations-managing.md#resolver-query-logs-configuring "resolver-query-logging-configurations-managing.md#resolver-query-logs-configuring").
6. Choose **Associate**
7. The association progress is displayed in the **Status**
   column on the **Resolver query log configurations** tab.

CLI
You can associate a query log configuration to a Profile by running a AWS CLI command
like the following and using your own values for `name`
`profile-id` and `resource-arn`.

`aws route53profiles associate-resource-to-profile --name
 `test-resource-association`--profile-id
`rp-4987774726example`--resource-arn
`arn:aws:route53resolver:us-east-1:123456789012:resolver-query-log-config/rqlc-cfe7f72example``

The following is an example output after you run the command:

```
{
    "ProfileResourceAssociation": {
        "CreationTime": 1710851226.613,
        "Id": "rpr-001913120b8example",
        "ModificationTime": 1710851226.613,
        "Name": "test-resource-association",
        "OwnerId": "123456789012",
        "ProfileId": "rp-4987774726example",
        "ResourceArn": "arn:aws:route53resolver:us-east-1:123456789012:resolver-query-log-config/rqlc-cfe7f72example",
        "ResourceType": "RESOLVER_QUERY_LOG_CONFIG",
        "Status": "CREATING",
        "StatusMessage": "Creating rp-4987774726example to rqlc-cfe7f72example association"
    }
}
```
