

# Creating and updating opportunities in bulk

In AWS Partner Central, you can create and update many opportunities at the same time. Instead of entering each opportunity in the console, you prepare one CSV file and submit it as a bulk job. Partner Central processes the file and reports which records succeeded and which failed.

If you use the `AWSPartnerCentralOpportunityManagement` or `AWSPartnerCentralFullAccess` managed policy, you already have the required permissions. If you use a custom IAM policy, add the permissions in [Required permissions](#bulk-actions-permissions).

To create and update opportunities in bulk from your CRM or other tools, use the bulk job operations in the Partner Central Selling API. For details, see [StartOpportunityBulkJob](https://docs.aws.amazon.com/partner-central/latest/APIReference/API_StartOpportunityBulkJob.html) in the AWS Partner Central API Reference.

**Note**  
We upgrade existing AWS Partners to the new opportunities experience automatically. You don't need to change any configuration or take any action.

## Interactive demo
<a name="bulk-actions-demo"></a>

To see the full workflow before you start, view the [Bulk upload opportunities workflow demo](https://awsmarketplace.storylane.io/share/sygxwsvnfi2n) on the Storylane website. The demo walks through creating opportunities from a file, using the agent, and updating opportunities in bulk.

## Create opportunities in bulk
<a name="bulk-import"></a>

You can create opportunities in bulk in two ways: from a file on the Opportunities page, or with the Partner Central agent. Both methods use the same template and the same 500-records-per-file limit.


| Method | Use it to | Where to start | 
| --- | --- | --- | 
| Create opportunities from a file | Create many new opportunities from one CSV file. | Opportunities page > Create opportunity > Create using a file | 
| Create opportunities with the agent | Run a bulk create from a file inside a Partner Central agent or a partner's AI client. | Partner Central agent, or Create opportunity > Create using agent | 

If you have a programmatic workflow that prepares the bulk create template, update it to use the current template, which includes expanded optional fields and the records-per-file limit (max 500 records). To download the current template, on the Opportunities page, choose **Create opportunity**, choose **Create using a file**, and then choose **Download template**.

### File limits
<a name="bulk-create-file-limits"></a>


| Method | Format | Limit | 
| --- | --- | --- | 
| Create opportunities from a file or with an agent | CSV (.csv) | 500 records per file | 

The same limit applies when you use the Partner Central Selling API.

### Create opportunities from a file
<a name="bulk-create-from-file"></a>

Use this method to create up to 500 opportunities from one CSV file.

1. Sign in to AWS Partner Central in the AWS Management Console. In the navigation pane, choose **Sell**, and then choose **Opportunities**.

1. Choose **Create opportunity**, and then choose **Create using a file**. The Create opportunities from a file page shows the steps of the workflow.

1. Choose **Download template**. The template includes every supported column and its required format. Enter your opportunity details, and save the file as CSV (comma delimited). If your data includes non-English characters, save the file with UTF-8 encoding. Always download the latest template when you start a new bulk job.

1. Under **Import file**, choose **Choose file**, and select your completed CSV file.

1. Choose **Create opportunities**. Partner Central submits your file and shows a confirmation with a link to the bulk job.

1. To check progress, open the **File submission history** tab and choose your job ID. Processing takes a few minutes.

1. On the job details page, review how many records succeeded and how many failed. To see why records failed, choose **Download error report**. For more information, see [Track bulk jobs and fix errors](#bulk-track-jobs).

For the columns, formats, and allowed values, see [Opportunity template field reference](#opportunity-fields).

### Create opportunities with the agent
<a name="bulk-create-with-agent"></a>

Use the Partner Central agent in AWS assistant chat, or in your own AI client, to create opportunities from a file in a chat. You upload one CSV file, the agent checks it, and the agent submits the job after you approve it.

To use the agent in your own AI client, see [Getting started with the Partner Central MCP server](https://docs.aws.amazon.com/partner-central/latest/developer-guide/mcp-getting-started.html) in the AWS Partner Central Developer Guide.

**Important**  
Partner Central agent conversations in Partner Central are temporary and aren't saved. Download any report before you close the chat.

1. Open AWS assistant chat in Partner Central. Or, on the Opportunities page, choose **Create opportunity**, and then choose **Create using agent**.

1. Tell the agent that you want to create opportunities in bulk from a file. For example, enter **Submit opportunities using a file**. The agent lists the steps and provides a link to the template.

1. Download the template and enter your opportunity details. Don't change the columns. Save the file as CSV UTF-8. The file supports up to 500 opportunities.

1. Attach your CSV file to the chat, and send it. The agent checks the file format and template columns in about 30 seconds.

1. Review the action, which shows the number of records to create. To submit the job, choose **Approve**. To cancel without creating any opportunities, choose **Dismiss**.

1. After the agent submits the job, it returns the job ID and a link to the job details page. When the job finishes, the agent reports how many opportunities succeeded and how many failed. If the job is still running after about 30 seconds, the agent shows the progress so far. Use the job details page to check the final results.

1. To review failures, choose the **Download error report** link. Correct the rows, and upload the corrected file to the agent.

Your file must meet the following requirements:
+ CSV format, saved as CSV UTF-8.
+ From 1 to 500 records. To submit more than 500 opportunities, split them across multiple files.
+ All required columns from the current template, and no extra columns.

If the file doesn't meet these requirements, the agent doesn't create any opportunities and tells you what to change. The agent checks only the file structure. AWS checks each record after you submit the job, so individual records can still fail.

**Note**  
At launch, the agent supports bulk create only. To update opportunities in bulk, use the Update opportunities method.

**Note**  
If bulk upload isn't available for your account, the agent directs you to upload your opportunity file in Salesforce instead.

## Update opportunities in bulk
<a name="update-opportunities-bulk"></a>

Use this method to change many existing opportunities at the same time. You download your current opportunities, edit them, and then upload the file.

**Note**  
Bulk update doesn't support opportunities in the Launched or Closed Lost stage. Partner Central excludes these opportunities from the downloaded file.


| Method | Use it to | Where to start | 
| --- | --- | --- | 
| Update opportunities in bulk with a file | Change many existing opportunities at the same time. | Opportunities page > Update opportunities | 

### File limits
<a name="bulk-update-file-limits"></a>


| Method | Format | Limit | 
| --- | --- | --- | 
| Update opportunities in bulk | CSV (.csv) | 1,500 records per file | 

The same limit applies when you use the Partner Central Selling API.

### Update opportunities from a file
<a name="bulk-update-from-file"></a>

1. Sign in to AWS Partner Central in the AWS Management Console. In the navigation pane, choose **Sell**, and then choose **Opportunities**.

1. Choose **Update opportunities**.

1. (Optional) On the **Prepare download** step, choose filters to build a file of the opportunities that you want to update. You can filter by stage, target close date, and created date. Choose **Next**.

1. (Optional) On the **Download file** step, choose **Download prepared XLS file**. The file contains the opportunities that match your filters. Choose **Next**.

1. (Optional) Open the file, and edit only the opportunities that need changes. Rows that you don't edit keep their current values. Don't change the columns. Columns highlighted in red are read-only. For tagging and format details, expand **Formatting and tagging instructions** on the page. Save the file as CSV (comma delimited).

1. On the **Manage and upload** step, choose **Choose file**, and select your edited CSV file. Select the confirmation check box, and then choose **Upload CSV file**.

1. To check progress, open the **File submission history** tab and choose your job ID. Review any failed records in the error report.

For the columns, formats, and allowed values, see [Opportunity template field reference](#opportunity-fields).

## Track bulk jobs and fix errors
<a name="bulk-track-jobs"></a>

Partner Central processes each file as a bulk job. You can track every job and review its results.

### View job status
<a name="bulk-view-job-status"></a>

1. On the Opportunities page, choose the **File submission history** tab.

1. Choose the job ID to open the job details page.

1. Review the number of records that succeeded and failed. Records that succeeded also appear on the Opportunities page.

### File submission history tab
<a name="bulk-file-submission-history"></a>

This tab lists every bulk job that you submitted. You can search by job ID or file name, export the list as CSV, or choose **Upload a new file** to start another job.


| Column | Description | 
| --- | --- | 
| Job ID | The unique ID of the bulk job. Choose it to open the job details page. | 
| File name | The name of the CSV file that you uploaded. | 
| Total records | The number of records in the file. | 
| Succeeded | The number of records that became opportunities. | 
| Failed | The number of records that failed validation. | 
| Status | Submitted, In progress, Completed (can still have failed records), or Failed. | 
| Submission date | The date and time that you submitted the file. | 
| Error report | A link to download the error report for jobs with failed records. | 

### Job details page
<a name="bulk-job-details"></a>

The Summary section shows the file name, status, total records, succeeded and failed counts, and submission date. "Succeeded" means the records in the file were turned into opportunities successfully. If any records failed, a banner at the top shows how many, with a **Download error report** button.

The Succeeded opportunities table lists only the records that became opportunities. Failed records don't appear in this table, so download the error report to review them.


| Column | Description | 
| --- | --- | 
| Opportunity ID | The ID of the new opportunity. Choose it to open the opportunity. | 
| Customer company name | The customer from your file. | 
| Partner project title | The project title from your file. | 
| Status | The opportunity review status, for example Pending approval. | 
| Stage | The opportunity stage, for example Prospect. | 
| Target close date | The target close date from your file. | 
| Estimated AWS MRR amount | The expected monthly recurring revenue from your file. | 
| Country | The customer country. | 

### Resubmit failed records
<a name="bulk-resubmit-failed-records"></a>

Partner Central processes each record in a bulk job separately. In a bulk create job, a record can fail after its opportunity is already created in **Draft** status. For example, Partner Central creates the opportunity, but adding a solution or an AWS Marketplace offer fails. In that case, the opportunity stays in Draft status and isn't submitted to AWS.

You can fix these records without creating duplicate opportunities. Fix each opportunity in the console, or fix the records in the error report and upload it again. For the meaning of each error, see the Common errors column in [Opportunity template field reference](#opportunity-fields).

#### About the error report
<a name="bulk-error-report"></a>

After a bulk create or bulk update job finishes, you can download an error report from the job details page. Both types of job produce reports with the same columns. The report has one row for each record that failed. It starts with these columns:
+ `errorCode`: The type of error, for example `VALIDATION_ERROR`.
+ `errorMessage`: What went wrong and how to fix it.
+ `status`: The result of processing the record, for example `FAILED`.
+ `resourceIdentifier`: The ID of the opportunity that the record created or updated. For a bulk create record, the report includes it only if Partner Central created the opportunity before the failure.

The rest of each row contains the values from your original submission, in the same columns as the template that you used.

#### How Partner Central prevents duplicate opportunities
<a name="bulk-prevent-duplicates"></a>

Always include the opportunity ID. When you resubmit a failed record, keep the `resourceIdentifier` column with the opportunity ID from the error report. Partner Central then updates that opportunity instead of creating a new one.

Without the opportunity ID, Partner Central matches a resubmitted record to an earlier one only when the record is unchanged. If you correct any value, for example the postal code, Partner Central rejects the record with a conflict error. If you change the customer name, project title, use case, estimated AWS monthly recurring revenue, or website, Partner Central creates a new opportunity.

Bulk update records already identify each opportunity in the **Opportunity id** column, so resubmitting them doesn't create new opportunities.

#### Option 1: Fix each opportunity in the console
<a name="bulk-resubmit-console"></a>

Use this option when only a few records failed.

1. In the error report, find the opportunity ID in the `resourceIdentifier` column.

1. In Partner Central, open the opportunity.

1. Add or correct the details that the `errorMessage` describes.

1. Submit the opportunity for co-sell.

#### Option 2: Resubmit by using the error report
<a name="bulk-resubmit-error-report"></a>

Use this option when many records failed.

1. On the Opportunities page, choose the **File submission history** tab, and then choose the job ID.

1. Choose **Download error report**.

1. For each row, read the `errorMessage`, and correct the values that it names. Don't change or remove the value in the `resourceIdentifier` column.

1. Upload the corrected error report as a new job, with the same method that you used for the original job. You don't need to remove the `errorCode`, `errorMessage`, or `status` columns.

For a bulk create job, Partner Central uses the `resourceIdentifier` value to update and submit the existing Draft opportunity instead of creating a new one.

For example, the `errorMessage` says "This solution is not one of your account's active solutions." In the **Solution Offered** column, enter a solution ID from your **Solutions** page. If none applies, enter `Other`, and describe the solution in **Other Solution Offered**. Then upload the file.

**Note**  
Spreadsheet applications can remove leading zeros from numbers. Before you upload, make sure that **AWS Account ID** has all 12 digits and that **Postal Code** keeps its leading zeros, for example `02108`. Format these columns as text to keep the zeros.

#### Option 3: Resubmit by using your own file
<a name="bulk-resubmit-own-file"></a>

Use this option for bulk create jobs. To resubmit with your own copy of the bulk create template, complete these steps.

1. Add a column named `resourceIdentifier` to your file.

1. For each record that failed after its opportunity was created, copy the `resourceIdentifier` value from the error report into the new column.

1. Include only the records that failed, and correct the values that the error report names.

1. Upload the file as a new bulk create job.

If you resubmit within 48 hours, Partner Central can match records to the original submission without the `resourceIdentifier` column. After 48 hours, include the `resourceIdentifier` column with the opportunity ID for each record. Otherwise, Partner Central creates duplicate opportunities.

### Cross-field rules
<a name="bulk-cross-field-rules"></a>

Some errors come from how fields relate to each other. Check the related fields together.


| Rule | What it means | How to fix it | 
| --- | --- | --- | 
| Marketing fields | Campaign name, use cases, channels, and AWS funding must be blank when the opportunity isn't from a marketing activity. | Leave the marketing fields blank unless the opportunity is from a marketing activity. | 
| National security | When the opportunity is national security, industry must be Government, visibility must be Full, and the primary need can't be Do Not Need Support from AWS Sales Rep. | Set these fields together. | 
| Primary need and involvement type | A Co-Sell involvement can't be paired with Do Not Need Support from AWS Sales Rep. | Match the primary need to the involvement type before you submit. | 
| Solution at Committed and Launched | A valid solution is required at the Committed and Launched stages. Other isn't allowed. | Tag a valid solution ID before you move the opportunity to these stages. | 
| Stage transition | The requested stage change isn't allowed from the current stage. | Move the opportunity through the stages in order. | 

### Best practices
<a name="bulk-best-practices"></a>
+ Start from the current template. Its columns and formats match the validation rules.
+ Don't add, delete, or reorder template columns. The only exception is the `resourceIdentifier` column when you resubmit failed records.
+ Complete every required field, and check the conditionally required fields.
+ Enter dates as YYYY-MM-DD and phone numbers in international format.
+ Use exact values from the allowed lists for stage, industry, use case, and delivery model.
+ Test a five-row file before you submit 500 (create) or 1,500 (update) rows.

## Opportunity template field reference
<a name="opportunity-fields"></a>

Two templates are available: one for bulk create and one for bulk update. Download the current template each time you start a job. Keep every column in place and don't reorder them. The following tables describe each field: what it's for, when it's required, the example format, and common errors with how to fix them. Dropdown fields reference the complete value lists in [Dropdown value lists](#bulk-dropdown-values).

### Create opportunity template
<a name="bulk-create-template"></a>

Download from the Opportunities page: **Create opportunity** > **Create using a file** > **Download template**. One opportunity per row, up to 500 rows.


| Field | What it's for | Required | Example / format | Common errors and how to fix | 
| --- | --- | --- | --- | --- | 
| Customer Company Name | End customer's legal company name. | Always | Example Corp (text, max 80 chars) | Blank fails the row. Enter the legal name. | 
| Industry Vertical | The customer's industry. | Always | Software and Internet | Not an allowed value fails the row. Use an exact value from Industry Vertical. | 
| Industry Other | Specific industry when Industry Vertical is Other. | When Industry Vertical = Other | Semiconductors (max 255) | Blank when Industry Vertical is Other fails the row. | 
| Does opportunity belong to NatSec? | Whether the opportunity contains classified national security information. | When Industry Vertical = Government | No (Yes/No) | If Yes, industry must be Government, visibility Full, and primary need not "Do Not Need Support from AWS Sales Rep." | 
| Country | Customer country. | Always | United States | Blank or invalid fails the row. Use a value from Country. | 
| State/Province | Customer state or territory. | When Country = United States | Washington | Blank when Country is US fails the row (unless NatSec = Yes). Use an allowed US state. | 
| Postal Code | Customer billing postal code. | Always | 98109 (US: 99999 or 99999-9999) | Wrong format for the country fails the row. Match the country format; format the cell as text if it starts with 0. | 
| Website | Customer website domain. | Always | example.com (valid domain, max 255) | Blank fails the row (unless NatSec = Yes). No social media pages. | 
| Partner Primary Need from AWS | What you need from AWS. | Always | Co-Sell - Technical Consultation | Invalid value fails the row. Don't combine Do Not Need Support with any Co-Sell value. | 
| Partner Project Title | Short project title. | Always | Cloud migration phase 1 (max 60 chars) | Blank fails the row. | 
| Customer Business Problem | The customer's pain point or business problem, and the expected outcome. | Always | 20 to 2,000 characters | Blank or under 20 characters fails the row. | 
| Solution Offered | The solutions you're proposing to the customer. | Always | S-0123456. Separate multiple IDs with a semicolon (;), up to 10. Or enter Other. | An ID that isn't one of your account's active solutions fails the row. Enter a solution ID from your Solutions page, or enter Other and describe it in Other Solution Offered. A valid solution is required at Committed and Launched; Other isn't allowed there. | 
| Other Solution Offered | Free-text solution description. | When Solution Offered = Other | Custom data platform (max 255 chars) | Blank when Solution Offered is Other fails the row. | 
| Next Steps | Next steps for the engagement. | When Primary Need = Co-Sell | Schedule architecture review (max 255 chars) | None common. | 
| Use Case | Primary use case. | Always | Migration / Database Migration | Invalid value fails the row. Use an exact value from Use Case. | 
| Estimated AWS Monthly Recurring Revenue | Approximate monthly AWS service fees at standard pricing, 3 months after launch, in USD. Used to size the opportunity. | Always | 5000 (positive number) | Blank or non-numeric fails the row. | 
| Target Close Date(mm/dd/yyyy) | Expected close date. | Always | 2027-03-31 (YYYY-MM-DD) | Blank, invalid, or out of range fails the row. Enter the date as YYYY-MM-DD, for example 2027-03-31, even though the column header shows mm/dd/yyyy. | 
| Opportunity Type | Type of opportunity. | Always | Net New Business | Invalid value fails the row. | 
| Delivery Model | How the solution is delivered. | Always | SaaS or PaaS | Invalid value fails the row. | 
| Is Opportunity from Marketing Activity? | Whether the opportunity came from a marketing activity. | Always | No (Yes/No) | Invalid value fails the row. | 
| Was Marketing Development Funds Used? | Whether MDF was used. | When marketing activity = Yes | No (Yes/No) | Must be blank when marketing activity = No. | 
| Customer DUNS | Customer DUNS number. | Optional | 123456789 | Must be exactly 9 digits. | 
| Sales Activities | Sales activity to date. | When Primary Need = Co-Sell | Conducted POC / Demo | Invalid value fails the row. | 
| AWS Products | AWS products to tag. | Optional | AWSAmplify;AWSAgentRegistry. Separate multiple product codes with a semicolon (;). | An invalid product code fails the row. Use codes from the published AWS products list. | 
| AWS Marketplace Products | AWS Marketplace products to tag. | Optional | Full AWS Marketplace product ARN. Separate multiple ARNs with a semicolon (;). | A product ID instead of the full ARN, or an invalid ARN, fails the row. | 
| AWS Marketplace Solutions | AWS Marketplace solutions to tag. | Optional | Full AWS Marketplace solution ARN, for example arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/soln-ab1c2de3fgh4i. Separate multiple ARNs with a semicolon (;). | A solution ID instead of the full ARN, or an invalid ARN, fails the row. | 
| Parent Opportunity ID | The opportunity this one renews or expands. | When Opportunity Type = Flat Renewal or Expansion | O46434049 | Doesn't exist or inaccessible fails the row. | 
| Customer First Name | Customer contact first name. | Optional | Jordan (max 80 chars) | None common. | 
| Customer Last Name | Customer contact last name. | Optional | Lee (max 80 chars) | None common. | 
| Customer Title | Customer contact job title. | Optional | CTO (max 80 chars) | None common. | 
| Customer Phone | Customer contact phone. | Optional | \+14255551234 | Must be international format starting with \+, max 40 chars. | 
| Customer Email | Customer contact email. | Optional | jordan.lee@example.com | Must be a valid email, max 80 chars. | 
| AWS Account ID | Customer AWS account ID. | Optional | 111122223333 | Must be 12 digits. | 
| Additional Comments | Free-text notes. | Optional | Created via bulk import | Max 255 characters. | 
| Street Address | Customer street address. | Optional | 410 Terry Ave N | None common. | 
| City | Customer city. | Optional | Seattle | None common. | 
| Competitive Tracking | Competitor in the deal. | Optional | Microsoft Azure | Invalid value fails the row. | 
| Other Competitors | Free-text competitor name. | When Competitive Tracking = \*Other | Competitor X | Blank when Competitive Tracking is \*Other fails the row. | 
| Marketing Campaign | Marketing campaign name. | When marketing activity = Yes | Reinvent 2026 | Must be blank when marketing activity = No. | 
| Marketing Activity Channel | Marketing channels. | When marketing activity = Yes | Email;Social. Separate multiple values with a semicolon (;). | Must be blank when marketing activity = No. A value not on the list fails the row. | 
| Marketing Activity Use-Case | Marketing use cases. | When marketing activity = Yes | AI/ML;Analytics. Separate multiple values with a semicolon (;). | Must be blank when marketing activity = No. | 
| APN Programs | APN program associated with the opportunity. | Optional | Migration Acceleration Program | Invalid program name fails the row. | 
| Partner Account Manager FirstName | PAM first name. | Optional | Sam (max 80 chars) | None common. | 
| Partner Account Manager LastName | PAM last name. | Optional | Rivera (max 80 chars) | None common. | 
| Partner Account Manager Phone Number | PAM phone. | Optional | \+14255550000 | International format starting with \+. | 
| Partner Account Manager Email | PAM email. | Optional | sam.rivera@partner.com | Must be a valid email. | 
| Partner CRM Unique Identifier | Your CRM reference ID for the opportunity. Use a unique value for each opportunity, or leave it blank. | Optional | CRM-00123 (max 64 chars) | Over 64 characters fails the row. | 
| AWS Pricing Calculator estimate(s) | Public AWS Pricing Calculator estimate links. | Optional | https://calculator.aws/\#/estimate?id=20698f28030656162a3dfa859155caeeea7b009f. Separate multiple links with a comma (,). | An invalid or private link fails the row. | 
| AWS Partition | AWS partition for the opportunity. | Optional | aws-eusc (blank for standard) | Only aws-eusc (European Sovereign Cloud) is allowed. | 
| Opportunity Owner FirstName | Opportunity owner first name. | Optional | Partner (max 80 chars) | None common. | 
| Opportunity Owner LastName | Opportunity owner last name. | Optional | Owner (max 80 chars) | None common. | 
| Opportunity Owner Email | Opportunity owner email. | Optional | partner.owner@partner.com | Must be a valid email. | 
| Opportunity Owner Phone Number | Opportunity owner phone. | Optional | \+14255550001 | International format starting with \+. | 

### Update opportunity template
<a name="bulk-update-template"></a>

Download from the Opportunities page: **Update opportunities** > Prepare download > Download file. Edit only the rows you want to change, keep every column, and don't edit the read-only (red) columns. Up to 1,500 rows.


| Field | What it's for | Required / editable | Example / format | Common errors and how to fix | 
| --- | --- | --- | --- | --- | 
| Opportunity id | The opportunity to update. | Required | O82581657279 | Must be an existing O ID you can access. Don't change it. | 
| Date Created (yyyy-mm-dd) | When the opportunity was created. | Read-only | 2026-11-10 | System value; don't edit. | 
| Last Updated Date (yyyy-mm-dd) | When the opportunity was last updated. | Read-only | 2026-11-11 | System value; don't edit. | 
| Customer Company Name | End customer company name. | Editable | Example Corp (max 80) | None common. | 
| Customer Email | Customer contact email. | Editable | contact@example.com | Must be a valid email, max 80 chars. | 
| Partner Project Title | Project title. | Editable | Digital transformation | None common. | 
| Customer Business Problem | The customer's pain point or business problem, and the expected outcome. | Editable | 20 to 2,000 characters | Under 20 characters fails the row. | 
| Does opportunity belong to NatSec? | National security flag. | Editable | No (Yes/No) | See national security cross-field rule. | 
| Sales Activities | Sales activity to date. | Editable (required for Co-Sell) | Conducted POC / Demo | Invalid value fails the row. | 
| Solutions Offered | The solutions tagged to the opportunity. | Editable | S-0100858. Separate multiple IDs with a semicolon (;). Or enter Other. | An ID that isn't one of your account's active solutions fails the row. A valid solution is required at Committed and Launched; Other isn't allowed there. | 
| Other Solution Offered | Free-text solution. | When Solutions Offered = Other | Harness test migration solution | Blank when Solutions Offered is Other fails the row. | 
| AWS Products | AWS product codes. | Editable | AWSAgentRegistry;AWSAmplify | Invalid code fails the row. | 
| AWS Marketplace Products | AWS Marketplace products to tag. | Editable | Full AWS Marketplace product ARN. Separate multiple ARNs with a semicolon (;). | A product ID instead of the full ARN, or an invalid ARN, fails the row. | 
| AWS Marketplace Solutions | AWS Marketplace solutions to tag. | Editable | Full AWS Marketplace solution ARN, for example arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Solution/soln-ab1c2de3fgh4i. Separate multiple ARNs with a semicolon (;). | A solution ID instead of the full ARN, or an invalid ARN, fails the row. | 
| Additional Comments | Free-text notes. | Editable |  | Max 255 characters. | 
| Next Step | Next steps. | Editable | Schedule review | None common. | 
| Stage | Opportunity stage. | Required | Prospect | Launched and Closed Lost aren't supported for bulk update. | 
| Target Close Date (yyyy-mm-dd) | Expected close date. | Required | 2027-03-31 | Must be YYYY-MM-DD within range. | 
| Closed Reason | Why the opportunity was closed-lost. | When Stage = Closed Lost | Price | Required when Stage is Closed Lost. Use a value from Closed Reason. | 
| Estimated AWS Monthly Recurring Revenue | Expected monthly recurring revenue, in USD. | Editable | 1350.75 | Non-numeric fails the row. | 
| Delivery Model | Delivery model. | Required | SaaS or PaaS | Invalid value fails the row. | 
| Is Opportunity from Marketing Activity? | Marketing-sourced flag. | Required | No (Yes/No) | Invalid value fails the row. | 
| Marketing Campaign | Campaign name. | When marketing activity = Yes |  | Must be blank when marketing activity = No. | 
| Marketing Activity Channel | Marketing channel. | When marketing activity = Yes | Email | Must be blank when marketing activity = No. | 
| Marketing Activity Use-Case | Marketing use case. | When marketing activity = Yes | AI/ML | Must be blank when marketing activity = No. | 
| Was Marketing Development Funds Used? | MDF flag. | When marketing activity = Yes | No (Yes/No) | Must be blank when marketing activity = No. | 
| APN Programs | APN program. | Editable | Well-Architected | Invalid program name fails the row. | 
| Other Competitors | Free-text competitor. | When Competitive Tracking = \*Other |  | Blank when Competitive Tracking is \*Other fails the row. | 
| Competitive Tracking | Competitor in the deal. | Editable | Microsoft Azure | Invalid value fails the row. | 
| Use Case | Primary use case. | Editable | Migration / Database Migration | Invalid value fails the row. | 
| Offer ID | AWS Marketplace private offers to associate. | Editable | Full AWS Marketplace offer ARN, for example arn:aws:aws-marketplace:us-east-1:123456789012:AWSMarketplace/Offer/offer-dtn3example1tg. Separate multiple ARNs with a semicolon (;). | A bare offer ID instead of the full ARN, an offer already linked to another opportunity, or a change on a Closed Lost opportunity fails the row. | 
| Partner Primary Need from AWS | What you need from AWS. | Editable | Co-Sell - Technical Consultation | Don't combine Do Not Need Support with any Co-Sell value. | 
| AWS Account ID | Customer AWS account ID. | Editable | 111122223333 | Must be 12 digits. | 
| Opportunity Type | Opportunity type. | Editable | Net New Business | Invalid value fails the row. | 
| Parent Opportunity ID | Parent opportunity. | When Opportunity Type = Flat Renewal or Expansion |  | Doesn't exist or inaccessible fails the row. | 
| Customer DUNS | Customer DUNS. | Editable | 123456789 | Must be exactly 9 digits. | 
| Partner CRM Unique Identifier | Your CRM reference ID for the opportunity. | Editable | HARNESS-MOCK-00202 (max 64 chars) | Over 64 characters fails the row. | 
| Partner Account Manager FirstName | PAM first name. | Editable |  | None common. | 
| Partner Account Manager LastName | PAM last name. | Editable |  | None common. | 
| Partner Account Manager Email | PAM email. | Editable |  | Must be a valid email. | 
| Partner Account Manager Phone Number | PAM phone. | Editable |  | International format starting with \+. | 
| Procurement Type | Procurement type (software revenue). | Editable | Contract | Use Contract, Pay-as-you-go, or Subscription. | 
| Customer Software Value | Software value amount. | Editable | 100000 | Non-numeric fails the row. | 
| Contract Effective Date/Term Start Date (yyyy-mm-dd) | Contract start date. | Required for SRRP when Launched | 2027-01-01 | Required for special-program opportunities at Launched. | 
| Contract Expiration Date (yyyy-mm-dd) | Contract end date. | Required for SRRP when Launched | 2028-01-01 | Required for special-program opportunities at Launched. | 
| Customer Software Value Currency | Currency for software value. | Editable | USD | Use an ISO currency code from Customer Software Value Currency. | 
| AWS pricing calculator estimate URL(s) | Public AWS Pricing Calculator estimate links. | Editable | https://calculator.aws/\#/estimate?id=20698f28030656162a3dfa859155caeeea7b009f | Invalid URL fails the row. | 
| AWS Partition | AWS partition. | Editable | aws-eusc (blank for standard) | Only aws-eusc is allowed. | 
| Opportunity Owner FirstName | Owner first name. | Editable | Partner | None common. | 
| Opportunity Owner LastName | Owner last name. | Editable | Owner | None common. | 
| Opportunity Owner Email Name | Owner email. | Editable | partner.owner@example.com | Must be a valid email. | 
| Opportunity Owner Phone Number | Owner phone. | Editable |  | International format starting with \+. | 
| Status | Opportunity review status. | Read-only | Approved | System value; don't edit. | 
| Country | Customer country. | Editable | United States | Invalid value fails the row. | 
| Customer Website | Customer website. | Editable | example.com | Must be a valid domain. | 

### Find solution IDs, product codes, and AWS Marketplace ARNs
<a name="bulk-find-identifiers"></a>

Several fields tag related items to an opportunity. Each field expects a specific type of identifier.


| Field | Identifier to enter | Where to find it | 
| --- | --- | --- | 
| Solution Offered (create) and Solutions Offered (update) | The Partner Central solution ID, for example S-0123456. Separate multiple IDs with a semicolon (;). | On the Solutions page in Partner Central. You can associate only solutions in Limited or Public status. To get the IDs programmatically, use the ListSolutions operation. | 
| AWS Products | The AWS product code, for example AWSAmplify. Separate multiple codes with a semicolon (;). | The [published AWS products list](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json) on the GitHub website. | 
| AWS Marketplace Products | The full AWS Marketplace product ARN. Separate multiple ARNs with a semicolon (;). | Use the AWS Marketplace Catalog API ListEntities or DescribeEntity operations. | 
| AWS Marketplace Solutions | The full AWS Marketplace solution ARN. Separate multiple ARNs with a semicolon (;). | Use the AWS Marketplace Catalog API ListEntities or DescribeEntity operations. | 
| Offer ID (update template) | The full AWS Marketplace offer ARN, not the bare offer ID. Separate multiple ARNs with a semicolon (;). | Use the AWS Marketplace Catalog API ListEntities operation to list your private offers. | 

### Dropdown value lists
<a name="bulk-dropdown-values"></a>

These fields accept only values from a fixed list (the second tab of each template: **Values** for create, **Dropdown Values** for update). Use the exact spelling.
+ **Industry Vertical** (customer industry): Aerospace; Agriculture; Automotive; Computers and Electronics; Consumer Goods; Education; Energy - Oil and Gas; Energy - Power and Utilities; Financial Services; Gaming; Government; Healthcare; Hospitality; Life Sciences; Manufacturing; Marketing and Advertising; Media and Entertainment; Mining; Non-Profit Organization; Professional Services; Real Estate and Construction; Retail; Software and Internet; Telecommunications; Transportation and Logistics; Travel; Wholesale and Distribution; Other.
+ **Partner Primary Need from AWS** (what you need from AWS): Co-Sell - Architectural Validation; Co-Sell - Business Presentation; Co-Sell - Competitive Information; Co-Sell - Pricing Assistance; Co-Sell - Technical Consultation; Co-Sell - Total Cost of Ownership Evaluation; Co-Sell - Deal Support; Co-Sell - Support for Public Tender / RFx. (Update template also allows: Do Not Need Support from AWS Sales Rep.)
+ **Opportunity Type** (deal type): Net New Business; Flat Renewal; Expansion.
+ **Delivery Model** (how the solution is delivered): SaaS or PaaS; BYOL or AMI; Managed Services; Professional Services; Resell; Other.
+ **Sales Activities** (sales activity to date): Initialized discussions with customer; Customer has shown interest in solution; Conducted POC / Demo; In evaluation / planning stage; Agreed on solution to Business Problem; Completed Action Plan; Finalized Deployment Need; SOW Signed.
+ **Competitive Tracking** (competitor in the deal): Oracle Cloud; On-Prem; Co-location; Akamai; AliCloud; Google Cloud Platform; IBM Softlayer; Microsoft Azure; Other- Cost Optimization; No Competition; \*Other.
+ **Marketing Activity Channel** (marketing channel): AWS Marketing Central; Content Syndication; Display; Email; Live Event; Out Of Home (OOH); Print; Search; Social; Telemarketing; TV; Video; Virtual Event.
+ **Marketing Activity Use-Case** (marketing use case): AI/ML; Analytics; Application Integration; Blockchain; Business Applications; Cloud Financial Management; Compute; Containers; Customer Engagement; Databases; Developer Tools; End User Computing; Front End Web & Mobile; Game Tech; IoT; Management & Governance; Media Services; Migration & Transfer; Networking & Content Delivery; Quantum Technologies; Robotics; Satellite; Security; Serverless; Storage; VR & AR.
+ **Is Opportunity from Marketing Activity?** / **Was Marketing Development Funds Used?** / **Does opportunity belong to NatSec?**: Yes; No.
+ **APN Programs** (create template): APN Immersion Days; APN Solution Space; ATO (Authority to Operate); AWS Marketplace Campaign; Express Migration; ISV Workload Migration; Migration Acceleration Program; Model Provider Rate Card (MPRC); P3; Partner Launch Initiative; Partner Opportunity Acceleration Funded; The Next Smart; VMware Cloud on AWS; Well-Architected; Windows; Workspaces/AppStream Accelerator Program; WWPS NDPP. (Update template also includes: Cloud Adoption Framework Program (CAF); ISV Immersion Day SFID Program.)
+ **AWS Partition**: aws-eusc (European Sovereign Cloud). Leave blank for the standard AWS partition.
+ **Use Case** (primary use case): AI Machine Learning and Analytics; Archiving; Big Data: Data Warehouse / Data Integration / ETL / Data Lake / BI; Blockchain; Business Applications: Mainframe Modernization; Business Applications & Contact Center; Business Applications & SAP Production; Centralized Operations Management; Cloud Management Tools; Cloud Management Tools & DevOps with Continuous Integration & Continuous Delivery (CICD); Configuration, Compliance & Auditing; Connected Services; Containers & Serverless; Content Delivery & Edge Services; Database; Edge Computing / End User Computing; Energy; Enterprise Governance & Controls; Enterprise Resource Planning; Financial Services; Healthcare and Life Sciences; High Performance Computing; Hybrid Application Platform; Industrial Software; IOT; Manufacturing, Supply Chain and Operations; Media & High performance computing (HPC); Migration / Database Migration; Monitoring, logging and performance; Monitoring & Observability; Networking; Outpost; SAP; Security & Compliance; Storage & Backup; Training; VMC; VMWare; Web development & DevOps.
+ **State/Province** (US states and territories, when Country = United States): the 50 states plus Dist. of Columbia, American Samoa, Guam, Northern Mariana Islands, Puerto Rico, U.S. Virgin Islands, Armed Forces Americas, Armed Forces Europe, Armed Forces Pacific. (59 values; see the template's second tab for the exact list.)
+ **Country**: 251 ISO countries (for example United States, Canada, Germany, Japan). The complete list is on the template's second tab.
+ **Closed Reason** (update template, when Stage = Closed Lost): Customer Deficiency; Delay / Cancellation of Project; Legal / Tax / Regulatory; Lost to Competitor - Google; Lost to Competitor - Microsoft; Lost to Competitor - SoftLayer; Lost to Competitor - VMWare; Lost to Competitor - Other; No Opportunity; On Premises Deployment; Partner Gap; Price; Security / Compliance; Technical Limitations; Customer Experience; Other; People/Relationship/Governance; Product/Technology; Financial/Commercial.
+ **Stage** (update template): Prospect; Qualified; Technical Validation; Business Validation; Committed; Launched; Closed Lost. (Launched and Closed Lost aren't supported for bulk update.)
+ **Procurement Type** (update template): Contract; Pay-as-you-go; Subscription.
+ **Customer Software Value Currency** (update template): 168 ISO currency codes (for example USD, EUR, GBP, AUD, CAD, JPY, INR). The complete list is on the template's second tab.
+ **Postal Code** formats (by country, examples on the second tab): United States: 99999 or 99999-9999; United Kingdom: A(A)N(A/N)NAA or A(A)N(A/N) NAA; France/Spain: 99999; Luxembourg/Switzerland/Denmark: 9999; Viet Nam: 999999.

## Required permissions
<a name="bulk-actions-permissions"></a>

The `AWSPartnerCentralOpportunityManagement` and `AWSPartnerCentralFullAccess` managed policies include the actions that bulk opportunity jobs use. If your IAM users or roles use a custom policy instead, your administrator must add these actions:
+ `partnercentral:StartOpportunityBulkJob`
+ `partnercentral:ListOpportunityBulkJobs`
+ `partnercentral:ListOpportunityBulkJobResults`
+ `partnercentral:GetOpportunityBulkJobReportUrl`

To add the actions to a custom policy, use Option 1 or Option 2.

### Add the permissions to a policy
<a name="bulk-actions-add-permissions"></a>

**Option 1, part 1: Create the policy**

1. Sign in to the AWS Management Console as an administrator, and open the [IAM console](https://console.aws.amazon.com/iam/).

1. In the navigation pane, choose **Policies**, then choose **Create policy**.

1. Choose the **JSON** tab, and replace the contents with the following policy.

   ```json
   {
     "Version": "2012-10-17",
     "Statement": [{
       "Sid": "PartnerCentralBulkOpportunities",
       "Effect": "Allow",
       "Action": [
         "partnercentral:StartOpportunityBulkJob",
         "partnercentral:ListOpportunityBulkJobs",
         "partnercentral:ListOpportunityBulkJobResults",
         "partnercentral:GetOpportunityBulkJobReportUrl"
       ],
       "Resource": "*",
       "Condition": {
         "StringEquals": {
           "partnercentral:Catalog": ["AWS"]
         }
       }
     }]
   }
   ```

1. Choose **Next**.

1. For **Policy name**, enter `PartnerCentralBulkOpportunities`, and then choose **Create policy**.

**Option 1, part 2: Attach the policy**

1. In the navigation pane of the IAM console, choose **User groups** or **Users**, and then choose the group or user.

1. On the **Permissions** tab, choose **Add permissions**, then choose **Attach policies directly**.

1. Select **PartnerCentralBulkOpportunities**, and then choose **Add permissions**.

**Option 2: Add the actions to an existing policy**

1. In the navigation pane, choose **Policies**, and then choose the policy that is attached to your users.

1. Choose **Edit**, then choose the **JSON** tab.

1. Add the four actions to the **Action** list of an **Allow** statement.

1. Choose **Next**, and then choose **Save changes**.