

# Bulk access assignment
<a name="bulk-access-assignment"></a>

As an Amazon Connect Decisions administrator, you can set data access for many users at once from a single CSV file, instead of updating each user one at a time. In one file you can add users and give them a role, grant access to products and sites, and remove access — for up to 50 users at a time. You review exactly what will change for each user before anything is applied.

Bulk assign is available to administrators from the **Users** page. If you do not see **Bulk assign**, contact your AWS account team to have it enabled on your instance. Users must already exist in your IAM Identity Center (IdC) directory. Bulk assign sets what users can see; it does not create accounts and does not send email.

## How it works
<a name="bulk-access-assignment-how-it-works"></a>

Bulk assign has three steps: upload a file, review the changes per user, and apply.

1. On the **Users** page, select **Bulk assign**.

1. Select **Download CSV template** and fill it in using a spreadsheet application. See [Preparing the CSV file](#bulk-access-assignment-preparing-csv). Save the file as CSV.

1. Upload the file and select **Validate**. The file is checked but nothing is changed yet.

1. Review the result. The verdict and a tally line summarize the change, and users are grouped into tabs — **Needs attention**, **New users**, **Access changes**, and **No change**. Each row shows the user, their role, the products and sites added or removed, and the access they will hold after the change. Open a row to see each product and site by its catalogue name.

1. If any line is wrong, the whole file is refused and nothing is applied. Problems are grouped with the CSV line numbers and values that caused them. Fix the file and upload again. You can also select **Download error report** to get just the failing rows.

1. When the file is clean, select **Apply**. The button shows how many users will change. Confirm the change in the dialog. If the file removes any access, or leaves any user with no access, you are asked to type the number of users affected before you can apply.

1. The **Results** step reports the outcome for each user: **Complete**, **Failed**, or **Role set, no access**. If anything failed, select **Download failed rows** to retry just those, or download the full report. Select **Done** to return to the Users page.

## Preparing the CSV file
<a name="bulk-access-assignment-preparing-csv"></a>

The file is a CSV with five columns. The heading row must use these exact names; order and capitalization do not matter.


| Column | What goes in it | 
| --- | --- | 
| action | ASSIGN, GRANT, or REVOKE | 
| user\_email\_id | The user’s email as it appears in your IdC directory | 
| role | Planner, Manager, or Admin — only on an ASSIGN row | 
| product\_id | One product id from your catalogue — only on GRANT or REVOKE rows | 
| site\_id | One site id from your catalogue — only on GRANT or REVOKE rows | 

Each row is one instruction for one user:
+ **ASSIGN** gives a user a role on the instance. This is how you add a user. The user must already be in your IdC directory, and must not already have a role on this instance. Use one ASSIGN row per user. A new Planner must also receive at least one product or site in the same file, because a Planner with no access sees nothing.
+ **GRANT** adds access to one product or one site. The user must already have a role on the instance, or be given one by an ASSIGN row in the same file.
+ **REVOKE** removes access to one product or one site.

A row that names both a product and a site creates two separate grants — one for the product and one for the site. It does not limit that product to that site; products and sites are tracked separately.

## Roles
<a name="bulk-access-assignment-roles"></a>


| Role | What they see | Product and site access | 
| --- | --- | --- | 
| Admin | Administers the instance and sees all data. | Not allowed — an Admin already sees everything. | 
| Manager | Sees all products and sites. | Not required. | 
| Planner | Sees only the products and sites granted to them. | Required — a new Planner needs at least one product or site in the same file. | 

## Limits
<a name="bulk-access-assignment-limits"></a>

These limits are checked when the file is validated and again when it is applied.


| Limit | Value | 
| --- | --- | 
| Users per file | 50 distinct users | 
| Rows per file | 2,000 | 
| File size | 256 KB | 
| File format | CSV | 
| Products per user | 500 (counted after the file is applied, including existing access) | 
| Sites per user | 500 (counted separately from products) | 

A file is limited by the number of users, not rows. If you need to update more than 50 users, split the work into several files of up to 50 users each and upload them one after another. Keep all of one user’s rows in the same file.

## Example
<a name="bulk-access-assignment-example"></a>

The following file adds three Planners, grants each of them access, and removes two items from an existing Planner. Use ids from your own catalogue.


| action | user\_email\_id | role | product\_id | site\_id | 
| --- | --- | --- | --- | --- | 
| ASSIGN | planner.northeast@example.com | Planner |  |  | 
| ASSIGN | planner.west@example.com | Planner |  |  | 
| GRANT | planner.northeast@example.com |  | SKU\_PEG\_400101 |  | 
| GRANT | planner.northeast@example.com |  |  | RDC-NORTHEAST | 
| GRANT | planner.west@example.com |  | SKU\_DNK\_430401 |  | 
| REVOKE | existing.planner@example.com |  | SKU\_VOM\_410201 |  | 

Because this file removes access, the review shows a warning and the confirmation asks you to type the number of users the file changes.

## Working from Excel or Google Sheets
<a name="bulk-access-assignment-working-from-excel-or-google-sheets"></a>
+ Save or export as CSV. A file that is not a .csv, or a spreadsheet file renamed to .csv, is refused.
+ Keep the heading row exactly as in the template. Extra columns are refused; a trailing empty column is allowed.
+ Blank lines are skipped. Line numbers in error messages count from the heading row, so the first data row is line 2.

## Validation messages
<a name="bulk-access-assignment-validation-messages"></a>

If any line is wrong, the whole file is refused and nothing is applied. Each problem is reported with the CSV line numbers it affects and the value that caused it. The messages are grouped below by when they are found.

Problems with the file itself — reported before any row is read.


| What you see | How to fix it | 
| --- | --- | 
| Use a .csv file. | Save or export as CSV. Renaming another file type does not work. | 
| This file is too large. | The file is over 256 KB. Split it into smaller files. | 
| This file has no rows. | The file is empty or has only a heading row. | 
| The column headings are wrong. | Use the five headings from the template and remove any extra columns. | 
| This file has too many rows. | The file is over 2,000 rows. Split it. | 
| This file is not valid CSV. | Re-export the file from your spreadsheet application. | 
| Too many users in one file. Split it by user. | Keep each file to 50 users or fewer. Keep all of one user’s rows in the same file. | 

Problems with a row — the row’s shape is wrong.


| What you see | How to fix it | 
| --- | --- | 
| Action must be ASSIGN, GRANT or REVOKE. | Correct the spelling in the action column. | 
| This email is not valid. | Fix the address in user\_email\_id. | 
| Add a role to this ASSIGN row. | Put Planner, Manager, or Admin in the role column. | 
| Leave product and site empty on ASSIGN rows. | Move the access to separate GRANT rows. | 
| Leave role empty on GRANT and REVOKE rows. | Roles are set only by ASSIGN rows. | 
| Add a product or a site. | Every GRANT or REVOKE row needs a product or a site. | 
| This row is repeated. | Delete the duplicate row. | 
| This access is granted and revoked in the same file. | Decide which you mean and delete the other row. | 
| This user is assigned two different roles. | Keep one ASSIGN row per user. | 

Problems found against your directory and catalogue — checked against IdC, the users on this instance, and your product and site catalogue.


| What you see | How to fix it | 
| --- | --- | 
| This email is not in your Identity Center directory. | Add the user to IdC first, then upload again. | 
| More than one Identity Center user has this email. Ask your Identity Center administrator to resolve it. | Resolve the duplicate entry in the directory. | 
| This user already has a role on this instance. | Remove the ASSIGN row; to change a role, use the Users page. | 
| This user has no role on this instance. Add an ASSIGN row. | Add an ASSIGN row for the user in the same file. | 
| This role does not exist. | Use Planner, Manager, or Admin. | 
| Admins already see all data. | Remove the access row for the Admin. | 
| This user already sees all data. | Remove the access row. | 
| Planners need at least one product or site. Add a GRANT row. | Give the new Planner at least one product or site. | 
| This product does not exist. / This site does not exist. | Check the id against your catalogue. | 
| This user would hold too many products or sites. | Reduce what the user is given, or revoke what they no longer need. Products and sites are limited to 500 each, per user. | 
| Could not check the file. | Your directory or catalogue could not be read, so no per-row result is shown. Try again. | 

Problems while applying — reported in the **Results** step if something fails after you select **Apply**.


| What you see | How to fix it | 
| --- | --- | 
| This user was not found. Access was not applied. | Nothing was written for the user. Download the failed rows and try again. | 
| The role was not assigned. You can try this user again. | Nothing was written for the user. Retry with the failed rows. | 
| Access could not be saved. Try these rows again. | The user may have a role but no access, shown as Role set, no access. Upload the failed rows again. | 
| This role no longer exists. | The role was removed between validating and applying. Re-validate the file. | 
| Could not apply the changes. | Nothing was written. Try again. | 
| The request failed. Some changes may have been applied. Check the users list. | Changes already applied stay applied. Check the Users page, then upload again — rows already satisfied show as No change. | 

## Results
<a name="bulk-access-assignment-results"></a>

The Results step reports an outcome for each user:
+ **Complete** — the user’s role and access were applied.
+ **Failed** — nothing was written for the user. Download the failed rows and try them again.
+ **Role set, no access** — the user was given a role but their access could not be saved, so they can sign in but see no data. Upload the failed rows again to grant their access.