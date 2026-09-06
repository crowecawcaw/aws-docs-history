

# Legal holds and AWS Backup
<a name="legalhold"></a>

## Legal hold overview
<a name="legalhold-overview"></a>

A legal hold is an administrative tool that helps prevent backups from being deleted while under a hold. While the hold is in place, backups under a hold cannot be deleted and lifecycle policies that would alter the backup status (such as transition to a `Deleted` state) are delayed until the legal hold is removed.

Legal holds can be applied to one or more backups (also known as recovery points) created by AWS Backup if their lifecycles allow it. Legal holds do not apply to [continuous backups](https://docs.aws.amazon.com/aws-backup/latest/devguide/point-in-time-recovery.html).

When a legal hold is created, it can take into account specific filtering criteria, such as resource types and resource IDs. Additionally, you can define the creation date range of backups you wish to include in a legal hold. 

Legal holds apply only to the original backup on which they are placed. When a backup is copied across Regions or accounts (if the resource supports it), it does not retain or carry its legal hold with it. A legal hold, like other resources, has a unique ARN (Amazon Resource Name) associated with it. Only recovery points created by AWS Backup can be part of a legal hold.

Note that while [AWS Backup Vault Lock](https://docs.aws.amazon.com/aws-backup/latest/devguide/vault-lock.html) provides additional protections and immutability to a vault, a legal hold provides additional protection against deletion of individual backups (recovery points). The legal hold does not expire and retains the data within the backup indefinitely. The hold remains active until it is released by a user with sufficient permissions.

## Multiple legal holds
<a name="legalhold-multiple"></a>

A backup can have more than one legal hold. Legal holds and backups have a many:many relationship, meaning that a backup can have more than legal hold and a legal hold can include more than one backup.

A backup cannot be deleted as long as it has at least one legal hold. After all legal holds on a backup are removed, it is subject to its retention lifecycle properties. Maintain at least one legal hold to prevent backup deletion. Legal holds can be applied to a recovery point retained past its backup lifecycle retention date (due to an existing legal hold).

Each account can have a maximum of 50 legal holds active at one time.

## Create a legal hold
<a name="legalhold-creation"></a>

A legal hold can be added to an existing backup (recovery point). 

 Backups (recovery points) with a status of `EXPIRED` or `DELETING` will not be included in the legal hold. Recovery points (backups) with the status of `CREATING` may not be included in the legal hold, depending on the time of completion.

Legal holds can be added by users who have the required IAM permissions.

### Create a legal hold using the console
<a name="legalhold-console"></a>

**To create a legal hold**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. In the dashboard in the left of the console, find My Account. Choose **Legal holds**.

1. Choose **Add legal hold**.

1. Three panels are shown: **Legal hold details**, **Legal hold scope**, and **Legal hold tags**.

   1. Under **Legal hold details**, enter a legal hold title and a description for the hold in the text boxes provided.

   1. In the panel **Legal hold scope**, choose how you wish to select the resource to include in the hold. When you create a hold, you choose the method used to select the resources that are within the legal hold. You can choose to include one of the following:
      + Specific resource types and IDs
      + Select backup vaults
      + All resources types or all backup vaults within your account

   1. Specify the date range of your legal hold. Enter the dates in the YYYY:MM:DD format (dates are inclusive).

   1. Optionally, you can add tags for the hold under **Legal hold tags**. Tags can help categorize the hold for future reference and organization. You can add up to 50 tags total.

1. When you are satisfied with the configuration of your new legal hold, click the button **Add new hold**.

### Create a legal hold using the AWS CLI
<a name="create-legalhold-api"></a>

You can create a legal hold using the [create-legal-hold](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-legal-hold.html) command.

```
aws backup create-legal-hold --title "{{my title}}" \
    --description "{{my description}}" \
    --recovery-point-selection "VaultNames={{string}},DateRange={FromDate={{timestamp}},ToDate={{timestamp}}}"
```

## View legal holds
<a name="legalhold-view"></a>

You can see legal hold details in the AWS Backup console or programmatically.

### View legal holds using the console
<a name="legalhold-view-console"></a>

To view all legal holds within an account using the Backup console,

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. Using the left part of the dashboard, under **My account**, click **Legal holds**.

1. The **legal hold** table displays the title, status, description, ID, and creation date of existing holds. Click on the carat (down arrow) next to the table header to filter the table by the selected column.

### View legal holds programatically
<a name="legalhold-view-api"></a>

To view all legal holds programmatically, you can use the following API calls: [ListLegalHolds](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListLegalHolds.html) and [GetLegalHold](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_GetLegalHold.html).

The following JSON template can be used for `GetLegalHold`.

```
GET /legal-holds/{legalHoldId} HTTP/1.1

Request

empty body

Response

{
    Title: string,
    Status: LegalHoldStatus, 
    Description: string, // 280 chars max
    CancelDescription: string, // this is provided during cancel // 280 chars max
    LegalHoldId: string,
    LegalHoldArn: string,
    CreatedTime: number,
    CanceledTime: number,
    
   ResourceSelection: {
        VaultArns: [ string ]
        Resources: [ string ]
   }, 
   ResourceFilters: {
        DateRange: {
          FromDate: number,
          ToDate: number
        }
   }
}
```

The following JSON template can be used for `ListLegalHolds`.

```
GET /legal-holds/
  &maxResults=MaxResults
  &nextToken=NextToken


Request

empty body
url params: 
  MaxResults: number  // optional,
  NextToken: string  // optional

status: Valid values: CREATING | ACTIVE | CANCELED | CANCELING
maxResults: 1-1000



Response

{
  NextToken: token,
  LegalHolds: [
    Title: string,
    Status: string, 
    Description: string, // 280 chars max
    CancelDescription: string, // this is provided during cancel // 280 chars max
    LegalHoldId: string,
    LegalHoldArn: string,
    CreatedTime: number,
    CanceledTime: number,
  ]

}
```

The following are the possible status values.


| Status | Description | 
| --- | --- | 
| CREATING | Requested recovery points are in the process of being held, and delete requests of those recovery points may be successful since the hold hasn't finished being created. | 
| ACTIVE | The legal hold has been created, All recovery points listed under this legal hold are held. | 
| CANCELLING | Legal holds are in the process of being removed, and delete requests of recovery points under the hold may succeed. | 
| CANCELED | Legal hold is fully released and no longer has any effect. Recovery points can be deleted. | 

## View recovery points in legal holds
<a name="legalhold-view-rps"></a>

You can see recovery points in legal holds in the AWS Backup console or programmatically.

### View recovery points in legal holds using the console
<a name="legalhold-view-rps-console"></a>

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. Using the left part of the dashboard, under **My account**, click **Legal holds**.

1. Select a legal hold, then you can view **Legal hold details**, **Resources selected for this hold**, **Recovery points on hold**, and **Tags** for this hold.

### View recovery points in legal holds programmatically
<a name="legalhold-view-rps-api"></a>

To view recovery points in a legal hold programmatically, you can use the [ListRecoveryPointsByLegalHold](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_ListRecoveryPointsByLegalHold.html) API call.

The following is an example request and response for `ListRecoveryPointsByLegalHold`.

```
GET /legal-holds/{legalHoldId}/recovery-points HTTP/1.1

Request

empty body

Response

{
  "RecoveryPoints": [
    {
      "RecoveryPointArn": "string",
      "ResourceArn": "string",
      "ResourceType": "string",
      "BackupVaultName": "string"
    }
  ],
  "NextToken": "string"
}
```

## Release a legal hold
<a name="legalhold-release"></a>

Legal holds remain in effect until they are removed by a user with sufficient permissions. Removing a legal hold is also known as cancelling, deleting, or releasing a legal hold. Removing a legal hold eliminates it from all backups to which it was attached. Any backups that expired during the legal hold are deleted within 24 hours after the legal hold is removed.

### Release a legal hold using the console
<a name="release-legalhold-console"></a>

**To release a hold using the console**

1. Open the AWS Backup console at [https://console.aws.amazon.com/backup](https://console.aws.amazon.com/backup).

1. Enter the description you would like associated with the release.

1. Review the details, then click **Release hold**.

1. When the Release hold dialogue box appears, confirm your intent to release the hold by typing `confirm` into the text box. 

   1. Check the box that acknowledges you are cancelling the hold. 

On the **Legal holds** page you can see all your holds. If the release was successful, the status of that hold will be shown as `Released`.

### Release a legal hold programmatically
<a name="release-legalhold-api"></a>

To remove a hold programmatically, use the API call [CancelLegalHold](https://docs.aws.amazon.com/aws-backup/latest/APIReference/API_CancelLegalHold.html).

Use the following JSON template.

```
DELETE /legal-holds/{legalHoldId}


Request

{
   CancelDescription: String
   DeleteAfterDays: number // optional
}


DeleteAfterDays: optional. 
  Defaults to 180 days. how long to keep legal hold record after canceled.
  This applies to the actual legal hold record only.
  Recovery points are unlocked as soon as cancelation processes and are not subject to this date.

Response 

Empty body

200 if successful
other standard codes
```