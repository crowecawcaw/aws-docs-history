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
**Import leads** page. Use the exact column headers shown below — the system
uses them to map your data to lead fields. All template columns must be present in the
uploaded file; extra columns are ignored.

| Column             | Format                                | Description                                                                                                                                                                                                                  | Example                                                                   |
| ------------------ | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------- |
| `Row ID`           | Unique value                          | A unique identifier for each row. Used for deduplication within the file — if two<br>rows share the same `Row ID`, the second row is rejected with a<br>`DUPLICATE_ROW` error. Not sent to AWS.                              | `1`, `2`, `3`                                                             |
| `Company Name`     | Max 120 characters                    | Legal name of the customer's company.                                                                                                                                                                                        | `Acme Corp`                                                               |
| `Country Code`     | ISO 3166-1 alpha-2 code               | Two-letter country code for the customer's location.                                                                                                                                                                         | `US`                                                                      |
| `City`             | Max 255 characters                    | Customer's city of operation.                                                                                                                                                                                                | `Seattle`                                                                 |
| `State Or Region`  | Free text                             | State, province, or region within the country.                                                                                                                                                                               | `WA`                                                                      |
| `Postal Code`      | Max 20 characters                     | ZIP or postal code.                                                                                                                                                                                                          | `98101`                                                                   |
| `Industry`         | Predefined value                      | Industry vertical. Must match an accepted value. For more information<br>about accepted values, see the [CreateEngagement API reference](../APIReference/API_CreateEngagement.md "../APIReference/API_CreateEngagement.md"). | `Software and Internet`                                                   |
| `Website URL`      | 4–255 characters, URL format          | Customer's company website URL.                                                                                                                                                                                              | `https://acme.com`                                                        |
| `First Name`       | Max 80 characters                     | First name of the primary contact.                                                                                                                                                                                           | `Jane`                                                                    |
| `Last Name`        | Max 80 characters                     | Last name of the primary contact.                                                                                                                                                                                            | `Doe`                                                                     |
| `Email`            | Valid email format, max 80 characters | Business email address of the contact.                                                                                                                                                                                       | `jane.doe@acme.com`                                                       |
| `Business Title`   | Max 80 characters                     | Job title or role of the primary contact.                                                                                                                                                                                    | `CTO`, `VP of Engineering`                                                |
| `Phone`            | E.164 format preferred                | Phone number of the primary contact. Preferred format is E.164:<br>`+` followed by country code and number (for example,<br>`+12065551234`).                                                                                 | `+12065551234`                                                            |
| `Use Case`         | Max 255 characters                    | A description of the AWS use case or workload the lead relates to.                                                                                                                                                           | `Cloud Migration`                                                         |
| `Business Problem` | Max 2000 characters                   | A description of the customer's core business challenge or pain point.                                                                                                                                                       | `Looking to modernize legacy infrastructure and migrate workloads to AWS` |

The service validates each field (required fields, format constraints, and enum values).
Invalid values return specific error codes and messages in the results file. For more
information about accepted field values and constraints, see the
[CreateEngagement API reference](../APIReference/API_CreateEngagement.md "../APIReference/API_CreateEngagement.md").

## Import process

To import leads, navigate to the **Leads** tab in AWS Partner Central and
choose **Import leads**. The import runs through the following steps:

1. **Select your file** — Choose a CSV file (.csv format
   only). The file must contain between 1 and 100 rows of lead data.
2. **Template validation** — The system validates that all
   template column headers are present in the uploaded file. If any are missing, an error is
   displayed with a **Download template** button.
3. **Row validation** — The system detects empty rows and
   duplicate Row IDs and marks them as failed. All other rows proceed to lead creation.
4. **Lead creation** — The system submits rows to create leads.
   You are navigated to the Leads page with one of these outcomes:

   - **All succeeded** — All rows were created
     successfully.
   - **Partial success** — Some rows were created, but
     others failed. A **Download failed records** link is provided.
   - **All failed** — All rows failed. A
     **Download failed records** link is provided.

###### Duplicate prevention

Uploading the same CSV file multiple times on the same day does not create duplicate
leads. Each row generates a deterministic identifier based on its field values. If the same
data was already imported, the service returns the existing lead without creating a duplicate.

## Troubleshooting import errors

When rows fail during import, you can download a results CSV file from the
**Download failed records** link on the Leads page. The file contains all
original columns plus `Error Code` and `Error Message` columns
appended at the end.

| Error code      | Cause                                                                                                                                          | Resolution                                                                                                                                                                                                                                                                                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `MALFORMED_ROW` | The row is entirely empty or contains only whitespace.                                                                                         | Remove the empty row, or populate at least one field.                                                                                                                                                                                                                                                                                                                                     |
| `DUPLICATE_ROW` | The `Row ID` value has already appeared in an earlier row in the same<br>file.                                                                 | Ensure each row has a unique `Row ID`, or remove the duplicate<br>rows.                                                                                                                                                                                                                                                                                                                   |
| `API_ERROR`     | The service rejected the row due to a validation failure (for example, missing<br>required field, invalid format, or unrecognized enum value). | Check the `Error Message` column for the specific field and reason.<br>Common causes: missing Company Name, missing Email, invalid Country Code,<br>invalid Industry value. Fix the data and re-upload. For more information about<br>accepted field values, see the [CreateEngagement API reference](../APIReference/API_CreateEngagement.md "../APIReference/API_CreateEngagement.md"). |

## Failed records CSV

When an import has failures, AWS Partner Central generates a results CSV file that you can
download from the **Download failed records** link on the Leads page.

###### File format

The results CSV contains all of the original template columns with your data
preserved exactly as uploaded, plus two additional columns appended at the end:
`Error Code` and `Error Message`.

###### Re-importing failed rows

To fix and re-import failed rows: download the results CSV, correct the values, and
upload the corrected file. The system automatically strips the `Error Code` and
`Error Message` columns during re-upload — you do not need to remove them
manually.

## Limits

| Limit                     | Value           |
| ------------------------- | --------------- |
| Maximum rows per CSV file | 100             |
| File format               | CSV (.csv) only |
| Minimum rows per file     | 1               |
