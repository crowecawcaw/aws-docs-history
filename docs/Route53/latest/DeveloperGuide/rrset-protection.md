

# Protecting records from changes

To prevent a critical record from being changed or deleted by mistake, add a record set protection for its name and type. While the protection exists, Route 53 rejects any `ChangeResourceRecordSets` request that would create, update, or delete those records. The protection applies to every user and role, including users with full Route 53 permissions. To change a protected record, you first delete its protection.

Use protections for records that rarely change and that would cause an outage if someone changed them by mistake, such as the apex records of a production domain, mail exchanger (MX) records, or records that route traffic to critical endpoints.

**Topics**
+ [How record set protections work](#rrset-protection-how-it-works)
+ [Managing record set protections by using the Route 53 console](#rrset-protection-console)
+ [Managing record set protections by using the AWS CLI](#rrset-protection-cli)
+ [Changing records that are protected](#rrset-protection-blocked-changes)
+ [Deleting a hosted zone that has protections](#rrset-protection-delete-hosted-zone)
+ [Record set protections and accelerated recovery](#rrset-protection-accelerated-recovery)
+ [Permissions for record set protections](#rrset-protection-permissions)
+ [Troubleshooting record set protection errors](#rrset-protection-errors)

## How record set protections work
<a name="rrset-protection-how-it-works"></a>
+ You identify a protection by a record name and a record type in one hosted zone, for example `www.example.com` and `A`.
+ A protection covers every record with that name and type, whatever its set identifier. For example, if `www.example.com` has three weighted `A` records, one protection on `www.example.com` `A` protects all three. You can't protect only some of those records.
+ You can create a protection for a name and type that has no records yet. The protection reserves that name and type: no one can create a record with that name and type until you delete the protection. Reserved names appear in the list of protections but not in the list of records.
+ Route 53 checks protections for every change in a `ChangeResourceRecordSets` request, for `CREATE`, `DELETE`, and `UPSERT`. If any change in the request affects a protected name and type, Route 53 rejects the whole request and makes none of the changes.
+ Route 53 doesn't reject a change that would not modify anything. For example, an `UPSERT` whose values are identical to the existing record succeeds without changing the record.
+ You can add an optional comment of up to 256 characters to each protection. Route 53 includes the comment in the error message when it rejects a change, so use the comment to tell people why the record is protected and whom to contact.
+ You can't update a protection. To change its comment, delete the protection and create it again.
+ You can use protections in public and private hosted zones.
+ You can't delete a hosted zone that has protections. Delete the protections first. For more information about deleting a hosted zone that has protections, see [Deleting a hosted zone that has protections](#rrset-protection-delete-hosted-zone).
+ Requests to create and delete protections are all-or-nothing. Each request either adds or removes every protection in the request, or none of them.
+ Protections don't change how Route 53 answers DNS queries. They only control changes to records.

The following details explain how record set protections behave in specific situations:

**Record types that you can protect**  
You can protect every record type that `ChangeResourceRecordSets` accepts, including the NS and SOA records at the zone apex.

**Who can remove a protection**  
Any principal that has the `route53:DeleteResourceRecordSetProtections` permission on the hosted zone can delete any protection in that zone. A protection is only as strong as the IAM policies that control that permission. For more information about these permissions, see [Permissions for record set protections](#rrset-protection-permissions).

**Records that Route 53 manages**  
Protections apply to changes that you request. A protection on the apex NS or SOA records blocks your changes to them, but it doesn't prevent Route 53 from updating those records as it manages the hosted zone.

**Other services and tools**  
When an AWS CloudFormation stack, the AWS CLI, or an AWS SDK changes a protected record, the change fails with the same `InvalidChangeBatch` error.

**Logging**  
CloudTrail logs requests to create, delete, and list protections. For more information, see [Logging Amazon Route 53 API calls with AWS CloudTrail](logging-using-cloudtrail.md).

## Managing record set protections by using the Route 53 console
<a name="rrset-protection-console"></a>

The hosted zone details page has a **Protections** tab. On the **Records** tab, the **Protection** column shows whether each record is protected. When a record is protected, the console disables **Edit** and **Delete** for it and explains that you must remove the protection first.<a name="rrset-protection-add-procedure"></a>

**To add a protection**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Hosted zones**, and then choose the name of the hosted zone.

1. On the **Protections** tab, choose **Add protection**.

1. Enter the following values:
   + **Record name** – The subdomain to protect, without the hosted zone name. Leave it blank to protect the zone apex.
   + **Record types** – One or more record types. The console creates one protection for each type.
   + (Optional) **Comment** – Why the record is protected. This text appears in error messages when Route 53 blocks a change.

1. Choose **Add protection**.

If a protection already exists for a selected type, the console reports `A protection already exists for {{name}} ({{type}})` and adds none of the protections.

**To protect records when you create them** – On the create record page, in the **Protection** section, select **Enable protection**. The console creates the records and then adds the protections. If you see a message that the records were created but aren't protected, add the protection on the **Protections** tab. You can add protection to at most 100 records in one submission.<a name="rrset-protection-remove-procedure"></a>

**To remove a protection**

1. On the hosted zone's **Protections** tab, select one or more protections.

1. Choose **Remove protection**.

1. Review the records that will be unprotected. A protection covers all records with the same name and type.

1. To confirm, type **confirm**, and then choose **Remove protection**.

The console removes the selected protections in one request of up to 100. If any one of them fails, the console removes none of them.

**To view protections** – Choose the **Protections** tab. The table shows **Record name**, **Record type**, **Protection type**, and **Comment**.

## Managing record set protections by using the AWS CLI
<a name="rrset-protection-cli"></a>

To manage protections programmatically, use the [CreateResourceRecordSetProtections](https://docs.aws.amazon.com/Route53/latest/APIReference/API_CreateResourceRecordSetProtections.html), [DeleteResourceRecordSetProtections](https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteResourceRecordSetProtections.html), and [ListResourceRecordSetProtections](https://docs.aws.amazon.com/Route53/latest/APIReference/API_ListResourceRecordSetProtections.html) actions. The following examples use the AWS CLI.

**Create protections**

The following command creates two protections at the apex of the `example.com` hosted zone: one for the `A` records, with a comment, and one for the `MX` records.

```bash
aws route53 create-resource-record-set-protections \
    --hosted-zone-id Z1D633PJN98FT9 \
    --protections '[{"RecordName":"example.com","RecordType":"A","Comment":"Production apex. Contact the DNS team before changing."},{"RecordName":"example.com","RecordType":"MX"}]'
```

Each element of `--protections` has the following values:

**`RecordName`**  
The name of the records to protect. Specify the full name, such as `www.example.com`.

**`RecordType`**  
The type of the records to protect, such as `A` or `MX`.

**`Comment`**  
(Optional) Up to 256 characters that explain why the records are protected. Route 53 includes the comment in the error message when it rejects a change.

A successful request returns an empty response.

**List protections**

The following command lists the protections in the hosted zone.

```bash
aws route53 list-resource-record-set-protections \
    --hosted-zone-id Z1D633PJN98FT9
```

Example output:

```json
{
    "ResourceRecordSetProtections": [
        {
            "RecordName": "example.com.",
            "RecordType": "A",
            "Comment": "Production apex. Contact the DNS team before changing."
        },
        {
            "RecordName": "example.com.",
            "RecordType": "MX"
        }
    ]
}
```

Route 53 returns `RecordName` in fully qualified form with a trailing dot, as `ListResourceRecordSets` does.

**Delete protections**

The following command deletes the protection for the `A` records at the zone apex.

```bash
aws route53 delete-resource-record-set-protections \
    --hosted-zone-id Z1D633PJN98FT9 \
    --protections '[{"RecordName":"example.com","RecordType":"A"}]'
```

A successful request returns an empty response.

Note the following about listing protections:
+ Route 53 sorts results by record name and then by record type.
+ Route 53 returns at most 300 protections per page. If you omit `MaxResults`, or specify a value greater than 300, the page size is 300.
+ If the response contains `NextToken`, more protections exist. Pass the token in the next request. The AWS CLI pages through all results automatically. Use `--page-size`, `--max-items`, and `--starting-token` to control paging.
+ Use `StartRecordName` and `StartRecordType` to start the listing at that position, inclusive. `StartRecordType` requires `StartRecordName`. When you specify `NextToken`, it takes precedence over both.
+ Use a `NextToken` only with the hosted zone that it was returned for.

## Changing records that are protected
<a name="rrset-protection-blocked-changes"></a>

If any change in a `ChangeResourceRecordSets` request has the same record name and type as a protection, Route 53 rejects the whole request with an `InvalidChangeBatch` error (HTTP 400) and applies none of the changes. The error message has one entry for each blocked change, in the following form:

```
RRSet with DNS name www.example.com., type A is protected and cannot be changed. Protection comment: "Production apex. Contact the DNS team before changing.". Call DeleteResourceRecordSetProtections for this record set before changing it.
```

If the change specifies a set identifier, the message includes the set identifier after the type. If the protection has no comment, the message omits the protection comment.

To change a protected record, delete the protection with `DeleteResourceRecordSetProtections`, make the change, and then create the protection again if you still need it.

## Deleting a hosted zone that has protections
<a name="rrset-protection-delete-hosted-zone"></a>

You can't delete a hosted zone while it has any record set protections, including protections on names that have no records. Route 53 returns an error with the following message:

```
Hosted Zone {{hosted-zone-id}} has resource record set protections. All resource record set protections need to be deleted (DeleteResourceRecordSetProtections) before deleting hosted zone.
```

To delete the hosted zone, list the protections with `ListResourceRecordSetProtections`, delete them with `DeleteResourceRecordSetProtections` (up to 100 per request), delete the records, and then delete the hosted zone.

## Record set protections and accelerated recovery
<a name="rrset-protection-accelerated-recovery"></a>
+ Protections stay in effect when you turn accelerated recovery on or off.
+ While you turn accelerated recovery on or off, requests to create or delete protections can fail with a `Throttling` error. Retry after a short wait.
+ To delete a hosted zone that has accelerated recovery and protections, turn off accelerated recovery, delete the protections, and then delete the hosted zone.
+ During failover, you can still create, delete, and list record set protections. Protections that exist before failover remain in effect.

For more information about accelerated recovery, see [Enabling accelerated recovery for managing public DNS records](accelerated-recovery.md).

## Permissions for record set protections
<a name="rrset-protection-permissions"></a>

The record set protection actions `route53:CreateResourceRecordSetProtections`, `route53:DeleteResourceRecordSetProtections`, and `route53:ListResourceRecordSetProtections` support only the hosted zone resource (`arn:aws:route53:::hostedzone/{{Id}}`). They don't support any service-specific condition keys.
+ A protection is only as strong as your control over `route53:DeleteResourceRecordSetProtections`. Grant it to a small set of administrators, and consider denying it to everyone else, for example with a service control policy.
+ Conditions in a policy on `route53:ChangeResourceRecordSets` don't override a protection. Even a principal with `route53:*` can't change a protected record until the protection is deleted.

For more information about an example policy that denies removing protections, see [Example 5: Deny removal of record set protections](access-control-managing-permissions.md#access-policy-example-deny-delete-rrset-protections).

## Troubleshooting record set protection errors
<a name="rrset-protection-errors"></a>

The following table lists the errors that the record set protection actions return, their causes, and what to do.


| Error | Cause | What to do | 
| --- | --- | --- | 
| `InvalidInput` (400) | A create or delete request contains more than 100 protections, or a list request has an invalid `MaxResults`, `StartRecordName`, or `StartRecordType`. | Split the request into batches of 100 or fewer, or fix the parameter. | 
| `InvalidResourceRecordSetProtectionBatch` (400) | One or more entries are invalid, already have a protection (create), or have no protection (delete). The `Errors` list has one entry for each failing record, with a `Code` of `InvalidInput`, `ProtectionAlreadyExists`, or `ProtectionNotFound`. | Fix or remove the listed entries and send the request again. Route 53 didn't change any protections. | 
| `ProtectionAlreadyExists` (409) | Every entry in a create request already has a protection. | No action is needed if you only wanted the records protected. To change a comment, delete the protection and create it again. | 
| `LimitsExceeded` (400) | The request would take the hosted zone over its protection quota. | Delete protections that you no longer need, or request a higher quota. For more information about the quota, see [Quotas on records](DNSLimitations.md#limits-api-entities-records). | 
| `NoSuchHostedZone` (404) | The hosted zone doesn't exist or isn't in your account. | Check the hosted zone ID. | 
| `PriorRequestNotComplete` (400), `Throttling` (400) | A previous request for the hosted zone hasn't completed, you exceeded the request rate, or accelerated recovery is being turned on or off. | Retry with exponential backoff. | 
| `InvalidPaginationToken` (400) | `NextToken` is invalid or was returned for a different hosted zone. | Start the listing again without `NextToken`. | 

Treat an unknown `ProtectionError` code as an error, because new values can be added.