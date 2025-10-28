# Migrating a hosted zone to a different AWS account

When migrating a hosted zone to a different AWS account, follow these recommended steps.

These steps are most suitable for hosted zones with infrequent record changes.
For hosted zones with frequent record updates, consider the following:

- Don't update any resource records during migration.
- Publish resource record changes in both old
  and new hosted zones after the delegation has been transferred.

###### Prerequisites

Install or upgrade the AWS CLI:

For information about downloading, installing, and configuring the AWS CLI, see the [AWS Command Line Interface User Guide](../../../cli/latest/userguide.md "../../../cli/latest/userguide.md").

###### Note

Configure the CLI so that you can use it when you're using both the account that created the hosted zone and the account that you're
migrating the hosted zone to. For more information, see [Configure](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md") in the
_AWS Command Line Interface User Guide_

If you're already using the AWS CLI, we recommend that you upgrade to the latest version of the CLI so that the CLI commands support
the latest Route 53 features.

###### Topics

- [Step 1: Prepare for migration](#hosted-zones-migrating-prepare "#hosted-zones-migrating-prepare")
- [Step 2: Create the new hosted zone](#hosted-zones-migrating-create-hosted-zone "#hosted-zones-migrating-create-hosted-zone")
- [Step 3: (Optional) Migrate health checks](#hosted-zones-migrating-health-checks "#hosted-zones-migrating-health-checks")
- [Step 4: Migrate records from the old hosted zone to the new hosted zone](#hosted-zones-migrating-old-to-new "#hosted-zones-migrating-old-to-new")
- [Step 5: Compare records in the old and new hosted zones](#hosted-zones-migrating-compare "#hosted-zones-migrating-compare")
- [Step 6: Update the domain registration to use name servers for the new hosted zone](#hosted-zones-migrating-update-domain "#hosted-zones-migrating-update-domain")
- [Step 7: Change the TTL for the NS record back to a higher value](#hosted-zones-migrating-change-ttl "#hosted-zones-migrating-change-ttl")
- [Step 8: Re-enable DNSSEC signing and establish the chain of trust (if required)](#hosted-zones-migrating-enable-dnssec "#hosted-zones-migrating-enable-dnssec")
- [Step 9: (Optional) delete the old hosted zone](#hosted-zones-migrating-delete-old-hosted-zone "#hosted-zones-migrating-delete-old-hosted-zone")

## Step 1: Prepare for migration

The preparation steps help you minimize the risks associated with migrating a hosted zone.

###### 1. Monitor zone availability

You can monitor the zone for the availability of your domain names. This can help you address any
issues that might lead to rolling back the migration. You can monitor for your domain names with most
traffic by using CloudWatch or query logging. For more information about setting up query logging,
see [Monitoring Amazon Route 53](monitoring-overview.md "monitoring-overview.md").

The monitoring can be done through a shell script, or through a third party service. It
shouldn't, however, be the only signal to determine if a rollback is required as you
might also get feedback from your customers due to a domain not being available.

###### 2. Lower the TTL setting

The TTL (time to live) setting for a record specifies how long you want DNS resolvers to cache the record and use the cached information. When the TTL expires,
a resolver sends another query to the DNS service provider for a domain to get the latest information.

The typical TTL setting for the NS record is 172800 seconds, or two days. The NS record lists the name servers that the Domain Name System (DNS) can use to get information about
how to route traffic for your domain. Lowering the TTL for the NS record, both with your current
DNS service provider and with Route 53, reduces downtime for your domain if you
discover a problem while you're migrating DNS to Route 53. If you don't lower the TTL, your domain could
be unavailable on the internet for up to two days if something goes wrong.

###### To lower the TTL

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. Choose **Hosted zones** in the navigation pane.
3. Choose the name of the hosted zone.
4. Choose the NS record, and and in the **Record details** pane, choose **Edit record**.
5. Change the value of **TTL (Seconds)**. We recommend that you specify a value between 60 seconds and 900 seconds (15 minutes).
6. Choose **Save**.

###### 3. Remove the DS record from the parent zone (If you have DNSSEC configured)

If you've configured DNSSEC for your domain, remove the Delegation Signer (DS) record from the
parent zone before you migrate your domain to Route 53.

If the parent zone is hosted through Route 53, see [Deleting public keys for a domain](domain-configure-dnssec.md#domain-configure-dnssec-deleting-keys "domain-configure-dnssec.md#domain-configure-dnssec-deleting-keys")
for more information.
If the parent zone is hosted on another registrar, contact them to remove the DS record.

Route 53 does not currently support migrating the DNSSEC setting. As such, you will need to
disable DNSSEC validation performed against your domain prior to the migration by
removing the DS record from the parent zone. After the migration, you can re-enable
DNSSEC validation by configuring DNSSEC on the new hosted zone and adding the respective
DS record to the parent zone.

###### 4. Make sure there are no other ongoing operations relying on the migrating hosted zone

Some operations will rely on DNS resolution in the migrating hosted zone, for example,
the TLS/SSL certificate renewal process may require making DNS record changes and the provider
will try to resolve the DNS record as the validation method. Before the migration,
you should make sure there is no other operation happening, in order to avoid unexpected
impact from the hosted zone migration.

## Step 2: Create the new hosted zone

Create the new hosted zone in the account you want to migrate the hosted zone to.

Choose the tab for the instructions for either the AWS CLI or console.

- [CLI](#migrate-hz-cli "#migrate-hz-cli")
- [Console](#migrate-hz-console "#migrate-hz-console")

CLIEnter the following command:

```
aws route53 create-hosted-zone \
            --name $hosted_zone_name \
            --caller-reference $unique_string

```

For more information, see
[create-hosted-zone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53/create-hosted-zone.html").

Console###### To create the new hosted zone using a different account

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").

Sign in with the account credentials for the account that you want to migrate the hosted zone to. 2. Create a hosted zone. For more information, see [Creating a public hosted zone](CreatingHostedZone.md "CreatingHostedZone.md"). 3. Make note of the hosted zone ID. In some cases, you'll need this information later in the process. 4. Log out of the Route 53 console.

Lower the NS TTL in the new zone as well, similar to Lower TTL setting in preparation
Step 1, Lower the TTL setting.

## Step 3: (Optional) Migrate health checks

You can associate DNS records in the new account with Route 53 health checks from the account you're migrating from.
To migrate a Route 53 health check, you need to
create new health checks in your new account with the same configuration as your existing ones.
For more information, see [Creating Amazon Route 53 health checks](dns-failover.md "dns-failover.md") .

## Step 4: Migrate records from the old hosted zone to the new hosted zone

You can migrate records from an AWS account to another by using the console or the AWS CLI.

Console
If your zone contains just a few records, you can consider to use Route 53 console to list
the records in your old zone, note them down, and create them in the new zone.
If you have migrated the health check in
[Step 3: (Optional) Migrate health checks](#hosted-zones-migrating-health-checks "#hosted-zones-migrating-health-checks"),
when you create the records in the new hosted zone, you should specify the new health check ID.
For more information, see the following topics:

- [Listing records](resource-record-sets-listing.md "resource-record-sets-listing.md")
- [Creating records by using the Amazon Route 53 console](resource-record-sets-creating.md "resource-record-sets-creating.md")
- [Configuring DNS failover](dns-failover-configuring.md "dns-failover-configuring.md")

You should lower the NS TTL in the new zone as well, similar to Lower TTL setting in Step 1.

CLI
If your zone contains a large number of records, you can export the records you want to
migrate to a file, edit the file, and then use the edited file to create records in the
new hosted zone. The following procedure uses AWS CLI commands, though third-party
tools are also available for this purpose.

######

1. Run the following command:

```
aws route53 list-resource-record-sets --hosted-zone-id `hosted-zone-id` > `path-to-output-file`
```

Note the following:

    * For `hosted-zone-id`, specify the ID of the
     old hosted zone that contains the records you want to migrate.
    * For `path-to-output-file`, specify the directory path and file name that you want to
     save the output in.
    * The `>` character sends the output to the specified file.
    * The AWS CLI automatically handles pagination for hosted zones that contain more than 100 records. For more information,
     see [Using the AWS Command Line Interface's pagination options](../../../cli/latest/userguide/pagination.md "../../../cli/latest/userguide/pagination.md") in the
     *AWS Command Line Interface User Guide*.


    If you use another programmatic method to list records, such as one of the AWS SDKs, you can get a maximum of 100 records
     per page of results. If the hosted zone contains more than 100 records, you must submit multiple requests to list all records.

Make a copy of this output. After you create records in the new hosted zone, we recommend that you run the AWS CLI `list-resource-record-sets`
command on the new hosted zone and compare the two outputs to ensure that all the records were created. 2. Edit the records that you want to migrate.

Edit the exported file before you can use it with the
`change-resource-record-sets` command. You can make
these changes using the search and replace function in a text
editor.

###### Note

The following steps describe manual editing using a text editor. Advanced users can automate these transformations using programmatic tools such as jq, Python, or other scripting languages.

Open a copy of the file that you created in step 1 of this procedure that contains the
records that you want to migrate, and make the following
changes:

    * Replace the ResourceRecordSets element at the top of the file with `Changes` element.
    * Optional – add a `Comment` element.
    * Delete the lines related to the NS and SOA records of the hosted zone name. The new hosted zone already has those records.
    * For each record, add an `Action` and a `ResourceRecordSets` element,
     add opening and closing brackets ( `{ }` ) as required to make the JSON code valid.


    ###### Note

    You can use a JSON validator to verify that you have all the braces and brackets in the correct places.
     To find an online JSON validator, search "JSON validator" in your browser.
    * If the hosted zone contains any aliases that refer to other records in the same hosted zone,
     make the following changes:




    	+ Change the hosted zone ID to the ID of the new hosted zone.


    	###### Important

    	If the alias record is pointing to another resource,
    	 for example, a load balancer, do not change the hosted zone ID to the
    	 hosted zone ID of the domain. If you change the hosted zone ID accidentally,
    	 rollback the hosted zone ID to the hosted zone id of the resource itself,
    	 not the hosted zone ID of the domain. The resource hosted zone ID can be found in
    	 the AWS console where the resource was created.
    	+ Move the alias records to the bottom of the file. Route 53 must create the record that
    	 an alias record refers to before it can create the alias record.


    	###### Important

    	If one or more alias records refer to other alias records, the records that are the alias
    	 target must appear in the file before the referencing alias records.
    	 For example, if `alias.example.com` is the alias target for `alias.alias.example.com`,
    	 `alias.example.com` must appear first in the file.
    	+ Delete any alias records that route traffic to a traffic policy instance.
    	 Make note of the records so you can recreate them later.
    * If you migrated health checks in [Step 3: (Optional) Migrate health checks](#hosted-zones-migrating-health-checks "#hosted-zones-migrating-health-checks"),
     change the records to associate with the newly created health check IDs.

The following example shows the edited version of records for a hosted zone for example.com.
The red, italicized text is new:

```
{
    `"Comment": "string",
 "Changes":` [
        {
            `"Action": "CREATE",
 "ResourceRecordSet":{`
                "ResourceRecords": [
                    {
                        "Value": "192.0.2.4"
                    },
                    {
                        "Value": "192.0.2.5"
                    },
                    {
                        "Value": "192.0.2.6"
                    }
                ],
                "Type": "A",
                "Name": "route53documentation.com.",
                "TTL": 300
            `}`
        },
        {
            `"Action": "CREATE",
 "ResourceRecordSet":{`
                "AliasTarget": {
                    "HostedZoneId": "Z3BJ6K6RIION7M",
                    "EvaluateTargetHealth": false,
                    "DNSName": "s3-website-us-west-2.amazonaws.com."
                },
                "Type": "A",
                "Name": "www.route53documentation.com."
            `}`
        }
    ]
}
```

3. Split large files into smaller files

If you have a lot of records or if you have records that have a lot of values (for example, a lot of IP addresses),
you might need to split the file into smaller files. The max values are:

    * Each file can contain a maximum of 1,000 records.
    * The maximum combined length of the values in all `Value` elements is 32,000 bytes.

4. Create records in the new hosted zone

Enter the following CLI:

```
aws route53 change-resource-record-sets \
            --hosted-zone-id `new-hosted-zone-id` \
            --change-batch file:`//path-to-file-that-contains-records`
```

Specify the following values:

    * For ``new-hosted-zone-id``, specify the ID of the new hosted zone.
    * For ``path-to-file-that-contains-records``,
     specify the directory path and file name that you edited in the previous steps.

If you deleted any alias records that route traffic to a traffic policy instance, recreate them using the Route 53 console.
For more information, see [Creating records by using the Amazon Route 53 console](resource-record-sets-creating.md "resource-record-sets-creating.md").

## Step 5: Compare records in the old and new hosted zones

To confirm that you successfully created all of your records in the new hosted zone, enter the following CLI command
to list the records in the new hosted zone and compare the output with the list of records from the old hosted zone.

```
aws route53 list-resource-record-sets \
            --hosted-zone-id `new-hosted-zone-id` \
            --output json > `path-to-output-file`
```

Specify the following values:

- For `new-hosted-zone-id`, specify the ID of the new hosted zone.
- For `path-to-output-file`, specify the directory path and file name that you want to save the output in.
  Use a file name that is different from the file name that you used in Step 4.

The `>` character sends the output to the specified file.

Compare the output with the output from Step 4. Other than the values of the NS and SOA records and any changes that you made in Step 4
(such as different hosted zone IDs or domain names), the two outputs should be identical.

If the records in the new hosted zone don't match the records in the old hosted zone, do one of the following:

- Make minor corrections using the Route 53 console.
  For more information, see [Editing records](resource-record-sets-editing.md "resource-record-sets-editing.md").
- Delete all the records except the NS and SOA records in the new hosted zone,
  and repeat the procedure in Step 4.

## Step 6: Update the domain registration to use name servers for the new hosted zone

When you finish migrating the records to the new hosted zone, change the name servers for the domain registration to use the name servers for the new hosted zone.
For more information, see Making Amazon Route 53 the DNS service for an existing domain.

If your hosted zone is in use - for example, if your users are using the domain name to browse to a website or access a web application - you should
continue monitoring traffic and availability of the hosted zone,
including website or application traffic, email, etc.

- **If the traffic slows or stops** – Change the name service for the
  domain registration back to the previous name servers of the
  old hosted zone. Then determine what went wrong.
- **If the traffic is unaffected** – Continue to the next step.

## Step 7: Change the TTL for the NS record back to a higher value

In the new hosted zone, change the TTL for the NS record to a more typical value, for example, 172800 seconds (two days). This improves latency for your users because
they don't have to wait as often for DNS resolvers to send a query for the name servers for your domain.

###### To change the TTL

1. Sign in to the AWS Management Console and open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. Choose **Hosted zones** in the navigation pane.
3. Choose the name of the hosted zone.
4. Choose the NS record, and and in the **Record details** pane,
   choose **Edit record**.
5. Change the value of **TTL (Seconds)** to the number of seconds that you want DNS resolvers
   to cache the names of the name servers for your domain. We recommend a value of 172800 seconds.
6. Choose **Save**.

## Step 8: Re-enable DNSSEC signing and establish the chain of trust (if required)

You can re-enable DNSSEC signing in two steps:

1. Enable DNSSEC signing for Route 53, and request that Route 53 create a
   key signing key (KSK) based on a customer managed key in AWS Key Management Service.
2. Create a chain of trust for the hosted zone by adding a Delegation Signer (DS) record to the parent zone,
   so DNS responses can be authenticated with trusted cryptographic signatures.

For instructions, see
[Enabling DNSSEC signing and
establishing a chain of
trust](dns-configuring-dnssec-enable-signing.md "dns-configuring-dnssec-enable-signing.md").

## Step 9: (Optional) delete the old hosted zone

When you're confident that you don't need the old hosted zone any longer, you can optionally delete it.
For instructions, see [Deleting a public hosted zone](DeleteHostedZone.md "DeleteHostedZone.md").

###### Important

Don't delete the old hosted zone or any records in that hosted zone for at least 48 hours after
you update the domain registration to use name servers for the new hosted zone.
If you delete the old hosted zone before DNS resolvers stop using the records in that hosted zone,
your domain could be unavailable on the internet until resolvers start using the new hosted zone.
