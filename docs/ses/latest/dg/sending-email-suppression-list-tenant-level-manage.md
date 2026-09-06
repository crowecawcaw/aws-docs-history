

# Managing tenant suppression list entries
<a name="sending-email-suppression-list-tenant-level-manage"></a>

You manage entries on a tenant's suppression list by using the same Amazon Simple Email Service (SES) API operations that you use for the account-level suppression list. To target a specific tenant's list, include the `--tenant-name` parameter in each request. When you omit this parameter, the operations target the account-level list. Use the AWS CLI to add, check, remove, and list suppressed addresses for a specific tenant.

**Important**  
Email addresses on the suppression list are stored with case preserved. While email sending functionality treats addresses with different cases as identical, API calls for suppression list management require an exact case match. Make sure that you use the exact case of the email address as it appears in the suppression list when you add, check, or remove entries.

## Prerequisites
<a name="managing-tenant-suppression-prerequisites"></a>

Before you manage tenant suppression list entries, make sure that you meet the following requirements:
+ Tenant-level suppression is enabled for the tenant. For more information, see [Configuring tenant-level suppression](sending-email-suppression-list-tenant-level-configure.md).
+ AWS CLI version 2 is installed and configured with appropriate permissions. For more information, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/).
+ The tenant exists in your SES account.

## Adding an address to a tenant's suppression list
<a name="adding-tenant-suppression-entry"></a>

Use the `PutSuppressedDestination` API operation with the `--tenant-name` parameter to add an email address to a tenant's suppression list.

**To add an address to a tenant's suppression list using the AWS CLI**
+ At the command line, enter the following command:

------
#### [ Linux, macOS, or Unix ]

  ```
  aws sesv2 put-suppressed-destination \
  --email-address {{recipient@example.com}} \
  --reason {{BOUNCE}} \
  --tenant-name {{MyTenant}}
  ```

------
#### [ Windows ]

  ```
  aws sesv2 put-suppressed-destination `
  --email-address {{recipient@example.com}} `
  --reason {{BOUNCE}} `
  --tenant-name {{MyTenant}}
  ```

------

  In the preceding example, replace {{recipient@example.com}} with the email address to add, {{BOUNCE}} with the suppression reason (acceptable values are `BOUNCE` and `COMPLAINT`), and {{MyTenant}} with the name of your tenant.

The command produces no output on success (HTTP 200). The address is now on the tenant's suppression list.

**Note**  
The `--reason` parameter accepts `BOUNCE` or `COMPLAINT`. You can add the same address with different reasons.

## Checking if an address is on a tenant's suppression list
<a name="checking-tenant-suppression-entry"></a>

Use the `GetSuppressedDestination` API operation with the `--tenant-name` parameter to check whether an email address is on a tenant's suppression list.

**To check if an address is on a tenant's suppression list using the AWS CLI**
+ At the command line, enter the following command:

------
#### [ Linux, macOS, or Unix ]

  ```
  aws sesv2 get-suppressed-destination \
  --email-address {{recipient@example.com}} \
  --tenant-name {{MyTenant}}
  ```

------
#### [ Windows ]

  ```
  aws sesv2 get-suppressed-destination `
  --email-address {{recipient@example.com}} `
  --tenant-name {{MyTenant}}
  ```

------

  In the preceding example, replace {{recipient@example.com}} with the email address to check and {{MyTenant}} with the name of your tenant.

If the address is on the tenant's suppression list, the command returns output that resembles the following example:

```
{
    "SuppressedDestination": {
        "EmailAddress": "recipient@example.com",
        "Reason": "BOUNCE",
        "LastUpdateTime": "2026-03-15T10:30:00.000Z",
        "Attributes": {
            "MessageId": "0100018e1234abcd-12345678-abcd-1234-abcd-123456789012-000000",
            "FeedbackId": "0100018e1234abce-12345678-abcd-1234-abcd-123456789012-000000"
        }
    }
}
```

The response includes the following fields:
+ `EmailAddress` – The suppressed email address.
+ `Reason` – Why the address was suppressed (`BOUNCE` or `COMPLAINT`).
+ `LastUpdateTime` – When the entry was last updated.
+ `Attributes` – Contains `MessageId` and `FeedbackId` from the event that caused suppression. These fields are present for automatically suppressed addresses and absent for manually added entries.

**Note**  
If the address is not on the tenant's suppression list, the API returns a `NotFoundException`.

## Removing an address from a tenant's suppression list
<a name="removing-tenant-suppression-entry"></a>

Use the `DeleteSuppressedDestination` API operation with the `--tenant-name` parameter to remove an email address from a tenant's suppression list.

**To remove an address from a tenant's suppression list using the AWS CLI**
+ At the command line, enter the following command:

------
#### [ Linux, macOS, or Unix ]

  ```
  aws sesv2 delete-suppressed-destination \
  --email-address {{recipient@example.com}} \
  --tenant-name {{MyTenant}}
  ```

------
#### [ Windows ]

  ```
  aws sesv2 delete-suppressed-destination `
  --email-address {{recipient@example.com}} `
  --tenant-name {{MyTenant}}
  ```

------

  In the preceding example, replace {{recipient@example.com}} with the email address to remove and {{MyTenant}} with the name of your tenant.

The command produces no output on success (HTTP 200). The address is removed from the tenant's suppression list.

**Important**  
Removing an address from a tenant's suppression list does not remove it from the global suppression list or the account-level suppression list. Each list is managed independently.

## Listing addresses on a tenant's suppression list
<a name="listing-tenant-suppression-entries"></a>

Use the `ListSuppressedDestinations` API operation with the `--tenant-name` parameter to retrieve all suppressed addresses for a specific tenant.

**To list all addresses on a tenant's suppression list using the AWS CLI**
+ At the command line, enter the following command:

------
#### [ Linux, macOS, or Unix ]

  ```
  aws sesv2 list-suppressed-destinations \
  --tenant-name {{MyTenant}}
  ```

------
#### [ Windows ]

  ```
  aws sesv2 list-suppressed-destinations `
  --tenant-name {{MyTenant}}
  ```

------

  In the preceding example, replace {{MyTenant}} with the name of your tenant.

The following example output shows two suppressed addresses:

```
{
    "SuppressedDestinationSummaries": [
        {
            "EmailAddress": "bounce@example.com",
            "Reason": "BOUNCE",
            "LastUpdateTime": "2026-03-10T08:15:00.000Z"
        },
        {
            "EmailAddress": "complaint@example.com",
            "Reason": "COMPLAINT",
            "LastUpdateTime": "2026-03-12T14:30:00.000Z"
        }
    ]
}
```

### Filtering the results
<a name="filtering-tenant-suppression-entries"></a>

You can filter the results by reason, date range, or both.

The following command filters by reason:

------
#### [ Linux, macOS, or Unix ]

```
aws sesv2 list-suppressed-destinations \
--tenant-name {{MyTenant}} \
--reasons BOUNCE COMPLAINT
```

------
#### [ Windows ]

```
aws sesv2 list-suppressed-destinations `
--tenant-name {{MyTenant}} `
--reasons BOUNCE COMPLAINT
```

------

The following command filters by date range:

------
#### [ Linux, macOS, or Unix ]

```
aws sesv2 list-suppressed-destinations \
--tenant-name {{MyTenant}} \
--start-date {{2026-01-01T00:00:00Z}} \
--end-date {{2026-03-31T23:59:59Z}}
```

------
#### [ Windows ]

```
aws sesv2 list-suppressed-destinations `
--tenant-name {{MyTenant}} `
--start-date {{2026-01-01T00:00:00Z}} `
--end-date {{2026-03-31T23:59:59Z}}
```

------

If the response includes a `NextToken` value, use it in a subsequent request to retrieve more results. Use the `--page-size` parameter to control the number of results per page.

**Note**  
The list operation returns summary information only. To get full details including `Attributes`, use `GetSuppressedDestination` for individual addresses.

## Automatic suppression entries
<a name="automatic-tenant-suppression-entries"></a>

SES automatically manages suppression entries based on the tenant's suppression configuration. You don't need to take any action for automatic entries. They appear in the tenant's suppression list alongside manually added entries.

SES automatically adds entries in the following cases:
+ A hard bounce occurs, if bounce suppression is enabled for the tenant.
+ A complaint is received, if complaint suppression is enabled for the tenant.

SES automatically removes entries in the following case:
+ A not-spam report is received for a complaint-suppressed address.