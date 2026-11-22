

The AWS Partner Central API Reference was restructured. For more information about the supported API operations, see the [AWS Partner Central API Reference](https://docs.aws.amazon.com/partner-central/latest/APIReference/Welcome.html).

# Manage customer accounts using the AWS Partner Central Selling API

Use Account Mapping to match the customer accounts in your customer relationship management (CRM) system to AWS customers, enrich them with AWS data, and request account planning sessions. When Account Mapping finds a match, it adds AWS enrichment data to the account, such as program eligibility, AWS Marketplace engagement score, solution score, and account planning qualification. Use the enrichment data to decide which accounts to prioritize, and request a planning session with the AWS Seller for a qualified account.

Each account you submit becomes a *customer account* resource in a catalog. You can submit accounts one at a time with `CreateCustomerAccount`, or many at once from a comma-separated values (CSV) file with `StartCustomerAccountBulkJob`. Every operation requires a `Catalog`: use `AWS` for production data and `Sandbox` for testing.

## Customer account statuses
<a name="customer-account-statuses"></a>

Matching runs in the background, so a new customer account starts as `PENDING`. Each customer account has one of the following values in `EnrichmentStatus`:

`PENDING`  
Matching hasn't finished.

`ENRICHED`  
Account Mapping matched the account to an AWS customer and added enrichment data. Only enriched accounts carry `AwsEnrichment`.

`NO_MATCH_FOUND`  
No AWS customer matched the account. A website URL, domain, and address improve the chance of a match.

`ACTION_REQUIRED`  
The account needs your attention before enrichment can complete. `GetCustomerAccount` returns the reason in `ReasonCode` and the steps to resolve it in `Message`.

An `ACTION_REQUIRED` account has one of the following values in `ReasonCode`:

`DUPLICATE_CUSTOMER_MATCH`  
Another of your customer accounts is already enriched with the same AWS customer. `ExistingCustomerAccountArn` identifies that account.

`PROCESSING_ERROR`  
Account Mapping couldn't process the account. Follow the steps in `Message`.

## Creating a customer account
<a name="creating-customer-accounts"></a>

Use the `CreateCustomerAccount` operation to submit one account. The request contains the following:

`Account`  
The customer details from your system. `CompanyName` is required. You can also provide `WebsiteUrl`, `Domain`, `Duns`, `ParentCompanyName`, `Industry`, `OtherIndustry`, and an `Address`. The more details you provide, the better the match.

`PartnerAccountIdentifier`  
Optional. Your own identifier for the account, such as its CRM record ID. Account Mapping returns it with the account so you can join the results back to your system.

`Tags`  
Optional. Up to 50 tags to apply to the new customer account.

`ClientToken`  
An identifier that makes the request idempotent. Use the same value when you retry a request.

The response contains the Amazon Resource Name (ARN) of the new customer account in `Arn`, its `Id`, and its initial `Status`. To read the result of matching, call `GetCustomerAccount` after matching finishes.

The following example request creates a customer account in the `Sandbox` catalog.

```json
{
   "Catalog": "Sandbox",
   "Account": {
      "CompanyName": "Example Organization",
      "WebsiteUrl": "https://www.example.com",
      "Address": {
         "City": "Seattle",
         "StateOrRegion": "Washington",
         "CountryCode": "US"
      }
   },
   "PartnerAccountIdentifier": "crm-0012345",
   "Tags": [
      { "Key": "Team", "Value": "Sales" }
   ],
   "ClientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

## Getting a customer account
<a name="getting-customer-accounts"></a>

Use the `GetCustomerAccount` operation with the `Id` or `Arn` of a customer account. The response contains the following:
+ The account details you submitted, in `Account`, and your `PartnerAccountIdentifier`.
+ The `EnrichmentStatus`, and the `ReasonCode` and `Message` when the status is `ACTION_REQUIRED`.
+ For an `ENRICHED` account, the enrichment data in `AwsEnrichment`. `Customer` describes the matched AWS customer, such as its industry, segment, geography, country, eligible programs, and account planning qualification. `Insights` describes its top solution: `MarketplaceEngagementScore`, `SolutionCategory`, `SolutionSubCategory`, and `SolutionScore`. Scores are levels (high, medium, or low), not numbers.
+ The `Tags` on the account. If the tags can't be read, the response omits `Tags` and returns the rest of the account.

## Searching customer accounts
<a name="searching-customer-accounts"></a>

Use the `SearchCustomerAccounts` operation to find customer accounts that match conditions you specify. The request can contain the following parameters:

`Filter`  
Conditions on customer account fields. If you omit the filter, the search returns all of your customer accounts in the catalog.

`Sort`  
The field to sort by, `SortBy`, and the direction, `SortOrder`, which is `ASCENDING` or `DESCENDING`. You can sort by `COMPANY_NAME`, `CREATED_DATE`, `LAST_MODIFIED_DATE`, `MARKETPLACE_ENGAGEMENT_SCORE`, or `SOLUTION_SCORE`.

`MaxResults`  
The number of results to return in one page, from 1 to 100.

A filter combines conditions with `AndAllFilters`, `OrAllFilters`, and `NotFilter`. Each condition compares a field with a value using `EqualsTo`, `ContainsAny`, `ContainsAll`, `GreaterThan`, `GreaterThanOrEquals`, `LessThan`, or `LessThanOrEquals`. You can filter on the following fields:
+ `ENRICHMENT_STATUS` and `COMPANY_NAME`
+ Enrichment data: `AWS_INDUSTRY`, `ACCOUNT_PLANNING_QUALIFICATION`, `PROGRAM_ELIGIBILITY`, `GEO`, `COUNTRY`, `SEGMENT`, `SOLUTION_CATEGORY`, `MARKETPLACE_ENGAGEMENT_SCORE`, and `SOLUTION_SCORE`
+ `IMPORT_ID`, which limits results to the accounts that one bulk job created
+ `CREATED_DATE` and `LAST_MODIFIED_DATE`

Each result is a summary. It contains the `Id`, `Arn`, `EnrichmentStatus`, `PartnerAccountIdentifier`, creation and modification dates, the company name you submitted, and a summary of the enrichment data. To read the other account details or the issues on an account, call `GetCustomerAccount`.

The response is paginated. Use the `NextToken` value from each response to retrieve the next page.

The following example returns enriched accounts with a high solution score, highest engagement score first.

```json
{
   "Catalog": "Sandbox",
   "Filter": {
      "AndAllFilters": [
         { "EqualsTo": { "Key": "ENRICHMENT_STATUS", "Value": { "StringValue": "ENRICHED" } } },
         { "EqualsTo": { "Key": "SOLUTION_SCORE", "Value": { "StringValue": "HIGH" } } }
      ]
   },
   "Sort": { "SortBy": "MARKETPLACE_ENGAGEMENT_SCORE", "SortOrder": "DESCENDING" },
   "MaxResults": 50
}
```

## Getting statistics about customer accounts
<a name="customer-account-statistics"></a>

Use the `GetCustomerAccountStatistics` operation to count your customer accounts and group the counts by field, for example to see how many accounts are enriched or how many are eligible for each program. The request can contain the following parameters:

`Filter`  
The same filter that `SearchCustomerAccounts` accepts. Only matching accounts are counted.

`Aggregations`  
Up to 10 aggregations. Each one groups the accounts by one field in `GroupBy`: `ENRICHMENT_STATUS`, `AWS_INDUSTRY`, `SEGMENT`, `REGION`, `GEO`, `COUNTRY`, `SOLUTION_CATEGORY`, `SOLUTION_SCORE`, `MARKETPLACE_ENGAGEMENT_SCORE`, `ACCOUNT_PLANNING_QUALIFICATION`, or `PROGRAM_ELIGIBILITY`.

`IncludeMissing`  
Optional. When `true`, each aggregation also counts the accounts that have no value for the field.

The response contains `TotalCount`, the number of accounts that match the filter, and one result for each aggregation. Each result lists `Buckets`, each with a value and a `Count`, and `OtherCount`, which counts the matching accounts that aren't in a listed bucket.

## Updating and deleting a customer account
<a name="updating-deleting-customer-accounts"></a>

Use the `UpdateCustomerAccount` operation to replace the account details of a customer account. The request contains the complete new `Account`, not only the changed fields, and the account's current `LastModifiedDate` from `GetCustomerAccount`. If the account changed after you read it, the request fails with a `ConflictException`. Read the account again and retry with the new `LastModifiedDate`.

Use the `DeleteCustomerAccount` operation with the `Id` or `Arn` of a customer account to delete it.

## Importing customer accounts in bulk
<a name="importing-customer-accounts"></a>

To submit many accounts at once, put them in a CSV file and start a bulk job. Each row that passes validation becomes one customer account.

### Preparing the CSV file
<a name="customer-account-csv-file"></a>

The file must have a header row. Account Mapping recognizes the following column headers. `Company Name` is the only required column.

```
Partner Account Identifier,Company Name,Website Url,Domain,Duns,Parent Company Name,Industry,Other Industry,Street Address,City,Postal Code,State Or Region,Country Code,Tags
```

Use these headers exactly as shown. If you misspell a header, Account Mapping ignores that column and you lose its data. In the `Tags` column, enter the tags for the row as `Key=Value` pairs separated by semicolons, for example `Team=Sales;Region=West`.

### Starting a bulk job
<a name="starting-customer-account-bulk-job"></a>

Use the `StartCustomerAccountBulkJob` operation with the location of your file in `FileUri` and a `ClientToken`. `FileUri` accepts a presigned `https://` URL to the file in Amazon S3. The response contains the `Id` and `Arn` of the bulk job and its initial `Status`.

A bulk job runs in the background and has one of the following values in `Status`:

`SUBMITTED`  
Account Mapping received the file and processing hasn't started.

`IN_PROGRESS`  
Account Mapping is validating the rows and creating customer accounts.

`COMPLETED`  
Account Mapping processed every row. Some rows can still have failed validation; check `FailureCount`.

`FAILED`  
Account Mapping rejected the whole file and created no customer accounts. `FailureReason` explains why.

### Tracking a bulk job and its results
<a name="tracking-customer-account-bulk-jobs"></a>

Use the following operations to follow a bulk job:

`GetCustomerAccountBulkJob`  
Returns the job's `Status` and its counts: `TotalRecords`, `ProcessedRecords`, `SuccessCount`, `FailureCount`, and `DeletedCount`, the number of accounts from the job that you deleted later. Poll it until the status is `COMPLETED` or `FAILED`.

`ListCustomerAccountBulkJobs`  
Lists your bulk jobs. You can filter by job identifier or status.

`ListCustomerAccountBulkJobResults`  
Lists the outcome of each row. Set `Status` to `SUCCEEDED` or `FAILED` to return only those rows.

`GetCustomerAccountBulkJobReportUrl`  
Returns a short-lived URL to a CSV report of the failed rows. Each row in the report includes its number in your file, its error code, and an error message. The report is available after the job is `COMPLETED` or `FAILED`. Check `ReportStatus`: the URL is present only when it is `AVAILABLE`, and `ExpiresAt` tells you when the URL stops working.

To find the customer accounts that a job created, call `SearchCustomerAccounts` with an `IMPORT_ID` filter set to the job's `Id`.

Starting a job for the same file again creates a new bulk job. It doesn't update customer accounts that an earlier job created. To fix failed rows, correct them in your file and import them again.

## Requesting an account planning session
<a name="requesting-account-planning"></a>

For a qualified customer account, you can ask the AWS Seller who owns the matched AWS customer for an account planning session. You send the request as an engagement invitation with an `AccountPlanningInvitation` payload. The AWS Seller accepts or rejects it.

### Requirements
<a name="account-planning-requirements"></a>

A planning request succeeds only when all of the following are true:
+ Your organization is eligible for the APN Customer Engagements (ACE) program. Otherwise the request fails with a `ValidationException`.
+ You own the customer account. A request for an account you don't own fails with a `ResourceNotFoundException`, the same error as for an account that doesn't exist.
+ The account is qualified for account planning. Otherwise the request fails with a `ValidationException` with the code `ACTION_NOT_PERMITTED`. To find qualified accounts, call `SearchCustomerAccounts` with an `ACCOUNT_PLANNING_QUALIFICATION` filter equal to `QUALIFIED`.
+ You don't already have an open (`PENDING`) planning request for the same account. A second request fails with a `ConflictException`.
+ You have fewer than 50 open planning requests. Otherwise the request fails with a `ServiceQuotaExceededException`.

### Sending a planning request
<a name="sending-account-planning-request"></a>

A planning request takes two calls, in this order:

1. Call `CreateEngagement` with a `Title`, a `Description` that says why you want to plan the account, a `ClientToken`, and one `CustomerAccount` context in `Contexts`. The context carries the customer account's identifier in `AccountIdentifier` and the customer's details in `Customer`. The response contains the engagement `Id`.

1. Call `CreateEngagementInvitation` with that engagement `Id` in `EngagementIdentifier`, a `ClientToken`, and an `Invitation`. Set the receiver to `aws`, the AWS Seller. Any other receiver is rejected. Put the request details in `Payload.AccountPlanningInvitation`:  
`AccountIdentifier`  
The `Id` or `Arn` of the customer account.  
`Customer`  
The customer's company name and, optionally, its industry, website URL, and country code, so that the AWS Seller can tell which account the request is about.  
`SenderContacts`  
One to three people the AWS Seller can contact. Each contact requires an email address. List the person who is requesting the session first.  
`PreferredContact`  
Optional. When you prefer to be contacted: a `Window` of `MORNING`, `AFTERNOON`, or `EVENING`, and a `Timezone` as an IANA time zone name, such as `America/Chicago`. This information is advisory.

Both calls are idempotent for the same `ClientToken`. If `CreateEngagementInvitation` fails, retry it with the same engagement rather than creating a new engagement.

The following example shows a `CreateEngagementInvitation` request.

```json
{
   "Catalog": "AWS",
   "ClientToken": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
   "EngagementIdentifier": "eng-1234567890abcd",
   "Invitation": {
      "Message": "Renewal or expansion planning",
      "Receiver": { "Account": { "AwsAccountId": "aws" } },
      "Payload": {
         "AccountPlanningInvitation": {
            "AccountIdentifier": "cust-acc-1234567890abc",
            "Customer": {
               "CompanyName": "Example Organization",
               "WebsiteUrl": "https://www.example.com",
               "CountryCode": "US"
            },
            "SenderContacts": [
               { "Email": "martha_rivera@example.com", "FirstName": "Martha", "LastName": "Rivera" }
            ],
            "PreferredContact": { "Window": "MORNING", "Timezone": "America/Chicago" }
         }
      }
   }
}
```

### Tracking planning requests
<a name="tracking-account-planning-requests"></a>

To list the planning requests you sent, call `ListEngagementInvitations` with `ParticipantType` set to `SENDER` and `PayloadType` set to `AccountPlanningInvitation`. Each request has one of the following values in `Status`:

`PENDING`  
The AWS Seller hasn't responded. Planning requests don't expire.

`ACCEPTED`  
The AWS Seller accepted the request.

`REJECTED`  
The AWS Seller declined the request. To read the reason, call `GetEngagementInvitation` and check `RejectionReason`. The list results don't include it.

You can receive fewer results than `MaxResults`, or none, on a page even when more results remain, because `PayloadType` is applied after the page is read. Keep requesting pages while the response contains a `NextToken`.

## Tagging customer accounts
<a name="tagging-customer-accounts"></a>

You can add tags when you create a customer account, or later with the `TagResource` operation and the account's `Arn`. Use `UntagResource` to remove tags and `ListTagsForResource` to read them. A customer account can have up to 50 tags.

## Permissions for customer accounts
<a name="customer-account-permissions"></a>

Each operation requires the IAM action of the same name, for example `partnercentral:CreateCustomerAccount`. Planning requests also use the engagement actions `partnercentral:CreateEngagement`, `partnercentral:CreateEngagementInvitation`, `partnercentral:ListEngagementInvitations`, and `partnercentral:GetEngagementInvitation`. The `AWSPartnerCentralOpportunityManagement` and `AWSPartnerCentralFullAccess` managed policies grant all of these actions for the `AWS` and `Sandbox` catalogs.