# Importing leads

The **Import leads** feature in AWS Partner Central lets you create multiple
partner-originated leads at once. Upload a CSV file to import your leads. Each valid row in the
file creates one lead through the APN Customer Engagements (ACE) program. You can import up to
100 leads per file.

After import, you can enrich your leads with AWS engagement signals, including
recommended actions and AWS insights like Marketplace engagement score. Use these insights
to prioritize outreach and identify leads most likely to convert to opportunities.

## CSV template

To ensure your data is formatted correctly, download the CSV template from the
**Import leads** page. The template contains 17 columns. Use the exact column
headers shown below — the system uses them to map your data to lead fields.

### Required fields

The following fields are required. Rows missing any of these fields fail validation and
appear in the failed records CSV.

| Column                   | Format                                | Description                                                                                                                                                                                                                                                        | Example                    |
| ------------------------ | ------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------- |
| `Company Name`           | Max 120 characters                    | Legal name of the customer's company. This value is also used to generate the<br>lead's display title in AWS Partner Central.                                                                                                                                      | `Acme Corp`                |
| `Country`                | Predefined value                      | Two-letter country code for the customer's location, in ISO 3166-1 alpha-2 format.<br>The code must match one of the accepted values. Download the template for the full list.<br>Common values: `US`, `GB`, `DE`,<br>`IN`, `JP`, `AU`, `CA`, `FR`,<br>`SG`, `BR`. | `US`                       |
| `Contact Business Title` | Max 80 characters                     | Job title or role of the primary contact at the customer company. This field is<br>always required — rows without a business title fail with a<br>`MISSING_CONTACT` error.                                                                                         | `CTO`, `VP of Engineering` |
| `Contact First Name`     | Max 80 characters                     | First name of the primary contact. First name, last name, and email are all<br>required for each contact.                                                                                                                                                          | `Jane`                     |
| `Contact Last Name`      | Max 80 characters                     | Last name of the primary contact.                                                                                                                                                                                                                                  | `Doe`                      |
| `Contact Email`          | Valid email format, max 80 characters | Business email address of the contact. Required, and must be a valid email format<br>(for example, `user@domain.com`). A malformed value triggers an<br>`INVALID_EMAIL` error.                                                                                     | `jane.doe@acme.com`        |

### Optional fields

The following fields provide additional context for your leads. Leave them blank if the
information is not available.

| Column             | Format                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | Example                               |
| ------------------ | ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- |
| `Row Id`           | Positive integer              | A unique identifier for each row. Used for deduplication within the file — if two<br>rows share the same `Row Id`, the second row is skipped with a<br>`DUPLICATE_ROW` error. Not sent to AWS.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `1`, `2`, `3`                         |
| `Street Address`   | Max 255 characters            | Full street address of the customer's primary office or location.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   | `123 Main Street`                     |
| `City`             | Max 255 characters            | Customer's city of operation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | `Seattle`                             |
| `State Or Region`  | Free text                     | State, province, or region within the country.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `WA`                                  |
| `Postal Code`      | Max 20 characters             | ZIP or postal code.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 | `98101`                               |
| `Industry`         | Predefined value              | Industry vertical the customer operates in. If provided, must match exactly one of<br>the accepted values. Leave blank if unsure — an unrecognized value triggers an<br>`INVALID_ENUM_VALUE` error. Accepted values: `Aerospace`,<br>`Agriculture`, `Automotive`, `Computers and<br>Electronics`, `Consumer Goods`, `Education`, `Energy -<br>Oil and Gas`, `Energy<br>• Power and Utilities`, `Financial<br>Services`, `Gaming`, `Government`,<br>`Healthcare`, `Hospitality`, `Life Sciences`,<br>`Manufacturing`, `Marketing and Advertising`, `Media and<br>Entertainment`, `Mining`, `Non-Profit Organization`,<br>`Other`, `Professional Services`, `Real Estate and<br>Construction`, `Retail`, `Software and Internet`,<br>`Telecommunications`, `Transportation and Logistics`,<br>`Travel`, `Wholesale and Distribution`. | `Software and Internet`               |
| `Website Url`      | 4–255 characters, URL format  | Customer's company website URL. Must be 4 to 255 characters and use a valid URL<br>format (for example, `https://acme.com`). A value that is too short or not<br>URL-formatted causes the row to fail.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | `https://acme.com`                    |
| `DUNS`             | 9-digit numeric string        | The customer's D-U-N-S Number, a unique business identifier issued by Dun &<br>Bradstreet. Used for firmographic enrichment and deduplication.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | `123456789`                           |
| `Contact Phone`    | E.164 format, up to 15 digits | Phone number of the primary contact. Must follow E.164 international format:<br>a `+` sign followed by the country code and number with no spaces or dashes.<br>An incorrectly formatted phone number causes an `API_ERROR` during lead<br>creation.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `+12065551234`                        |
| `Use Case`         | Free text, max 255 characters | A free-text description of the AWS use case or workload the lead relates to. This value is not validated against a fixed list of values.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | `Migration and Transfer`              |
| `Business Problem` | 20–2000 characters            | A description of the customer's core business challenge or pain point. This<br>helps AWS understand the context of the lead. If provided, must be between 20 and<br>2000 characters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | `Legacy infrastructure modernization` |

## Import process

To import leads, navigate to the **Leads** tab in AWS Partner Central and
choose **Import leads**. The import runs through the following steps:

1. **Select your file** — Choose a CSV file (.csv format
   only). The file must contain between 1 and 100 rows of lead data. If the file format is
   invalid or exceeds the row limit, the **Import leads** button remains
   disabled.
2. **Column mapping** — The system validates that all
   required template column headers are present. If required columns are missing, an error is
   displayed with a **Download template** button so you can start with the
   correct format.
3. **Validation** — Each row is checked for required fields,
   data formatting, valid enum values, and duplicate detection. Rows that fail validation are
   collected into a downloadable failed records file. If all rows fail, you are redirected to
   the Leads page with an error notification.
4. **Lead creation** — Valid rows are submitted to create
   leads. You are navigated to the Leads page with one of three outcomes:

   - **Success** — All rows were created
     successfully.
   - **Partial success** — Some rows were created, but
     others failed. A **Download failed records** link is provided.
   - **Error** — All rows failed. A **Download
     failed records** link is provided.

## Troubleshooting import errors

When rows fail during import, you can download a failed records CSV file that contains all
original columns plus an `Error Code` and `Error Message` column. Use
the error code to identify and fix the issue, then re-upload only the failed rows.

| Error code           | Cause                                                                                                                                       | Resolution                                                                                                                                                                                                                           |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `MALFORMED_ROW`      | The row is entirely empty or contains only whitespace.                                                                                      | Remove the empty row, or populate at least the required fields.                                                                                                                                                                      |
| `MISSING_COMPANY`    | The `Company Name` field is empty.                                                                                                          | Add a valid company name.                                                                                                                                                                                                            |
| `MISSING_COUNTRY`    | The `Country` field is empty.                                                                                                               | Add a valid ISO 3166-1 alpha-2 country code (for example, `US`,<br>`DE`, `JP`).                                                                                                                                                      |
| `MISSING_CONTACT`    | One of the required contact fields is empty: `Contact Business Title`,<br>`Contact First Name`, `Contact Last Name`, or<br>`Contact Email`. | Provide a business title, first name, last name, and email for the<br>contact.                                                                                                                                                       |
| `INVALID_EMAIL`      | The `Contact Email` value is present but not a valid email format.                                                                          | Use a valid email address (for example, `jane.doe@acme.com`).                                                                                                                                                                        |
| `INVALID_ENUM_VALUE` | The `Industry` or `Country` value does not match an<br>accepted value.                                                                      | For `Industry` (optional): use a supported value from the CSV<br>template, or leave the field blank. For `Country` (required): replace with a<br>valid ISO 3166-1 alpha-2 code from the template (for example, `US`,<br>`DE`, `JP`). |
| `DUPLICATE_ROW`      | The `Row Id` value has already appeared in an earlier row in the same<br>file.                                                              | Ensure each row has a unique `Row Id`, or remove the duplicate<br>rows.                                                                                                                                                              |
| `API_ERROR`          | The row passed validation but the lead creation request failed (throttling, server<br>error, or network error).                             | Wait a few minutes and re-import only the failed rows. If the issue persists,<br>contact AWS Partner Central support.                                                                                                                |

## Failed records CSV

When an import partially or totally fails, AWS Partner Central generates a failed records CSV
file that you can download from the **Download failed records** link on the
Leads page. This file contains every row that was not successfully imported, along with the
reason for failure.

###### File format

The failed records CSV contains all of the original 17 template columns with your data
preserved exactly as uploaded, plus two additional columns appended at the end:
`Error Code` and `Error Message`. Rows appear in the same order as
your original file.

###### Validation errors

Rows that fail during the validation step (before lead creation is attempted) include
error codes such as `MISSING_CONTACT`, `MISSING_COMPANY`, or
`INVALID_EMAIL`. For example, if you upload rows without a
`Contact Business Title`, each row appears in the failed records file with
`Error Code` set to `MISSING_CONTACT` and `Error Message`
set to `Contact business title is required.`

###### API errors

Rows that pass validation but fail during lead creation appear with
`Error Code` set to `API_ERROR`. The `Error Message`
contains the specific reason returned by the service. For example, a phone number that does
not follow E.164 format (`+` followed by country code and number) produces an
error message describing the format constraint. Review the error message, correct the data in
the failed records file, and re-upload only the failed rows.

###### Re-importing failed rows

To fix and re-import failed rows, download the failed records CSV, correct the values
flagged in the `Error Code` and `Error Message` columns, remove those
two columns, and upload the corrected file. You do not need to re-import rows that succeeded
in the original upload.

## Limits

| Limit                     | Value           |
| ------------------------- | --------------- |
| Maximum rows per CSV file | 100             |
| File format               | CSV (.csv) only |
| Minimum rows per file     | 1               |
