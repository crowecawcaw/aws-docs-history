# Data Validation Error Export

Error records can be exported by choosing **Download** on the
**Data Validation** report page when the validation is checking
individual data points that failed.

###### Note

The export option is not available when the validation is checking structural,
systemic, or aggregate-level requirements.

Export is available for the following:

- Validation checks for content or quality of existing data
- Validations that involve checking for missing or invalid values in existing
  fields
- Data Quality Validations (such as null checks, and date range validations)

###### Note

The system limits error record downloads to a maximum of 10,000 rows. If the total error count exceeds this limit, a notification will appear on the screen.
Work with your data administrator to review and resolve all errors in the source table.

Export is not available for the following:

- Validation checks for structural elements (such as table existence or column
  presence)
- Validations that involve system-level constraints (such as size limits, counts,
  and thresholds)
- Forecasting eligibility checks (such as time series limits or active product
  counts)
