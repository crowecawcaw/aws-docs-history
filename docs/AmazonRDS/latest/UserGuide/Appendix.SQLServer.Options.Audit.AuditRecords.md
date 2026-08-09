# Viewing audit logs

Your audit logs are stored in `D:\rdsdbdata\SQLAudit`.

After SQL Server finishes writing to an audit log file—when the file reaches its
size limit—Amazon RDS uploads the file to your S3 bucket. If retention is enabled,
Amazon RDS moves the file into the retention folder:
`D:\rdsdbdata\SQLAudit\transmitted`.

For information about configuring retention, see [Adding SQL Server Audit to the DB instance options](Appendix.SQLServer.Options.Audit.Adding.md "Appendix.SQLServer.Options.Audit.Adding.md").

Audit records are kept on the DB instance until the audit log file is uploaded. You can
view the audit records by running the following command.

```
SELECT   *
	FROM     msdb.dbo.rds_fn_get_audit_file
	             ('D:\rdsdbdata\SQLAudit\*.sqlaudit'
	             , default
	             , default )
```

You
can use the same command to view audit records in your retention folder by changing the filter
to
`D:\rdsdbdata\SQLAudit\transmitted\*.sqlaudit`.

```
SELECT   *
	FROM     msdb.dbo.rds_fn_get_audit_file
	             ('D:\rdsdbdata\SQLAudit\transmitted\*.sqlaudit'
	             , default
	             , default )
```

## Viewing audit log records in CloudWatch

If you chose to upload the audit logs to CloudWatch, you can access the log records
(in JSON format) by following these steps.

###### To view audit logs in CloudWatch

1. Open the CloudWatch console at
   [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the left navigation pane, choose **Logs**, **Log Management**.
3. Enter your DB instance name in the **Log Groups** search box.
4. Choose the appropriate log group.
5. Under the **Log Streams** tab, choose the log stream.

Alternatively, you can use the AWS CLI to query the log stream. The following example
extracts audit log events and exports them to a CSV file.

```

# Parameters
# -----------
LOG_GROUP="/aws/rds/instance/<your-db-instance-id>/sqlaudit"
START_DATE="2026-06-18"
END_DATE="2026-06-19"
OUTPUT_FILE="sql_audit_extract.csv"

# Convert dates to epoch milliseconds
# -----------------------------------
START_TIME=$(date -d "${START_DATE}" +%s)000
END_TIME=$(date -d "${END_DATE}" +%s)000

# Fetch log events
# ----------------
# Note: --no-paginate returns all results in a single call.
# For large result sets, consider using --page-size or manual pagination.
RESPONSE=$(aws logs filter-log-events \
  --log-group-name "${LOG_GROUP}" \
  --start-time "${START_TIME}" \
  --end-time "${END_TIME}" \
  --output json \
  --no-paginate)

# Parse and export to CSV
# Extract the 'message' field from each event (JSON formatted messages),
# then convert to CSV using jq.
# Get CSV headers from the first record
# -------------------------------------
HEADERS=$(echo "${RESPONSE}" | jq -r '
  [.events[0].message | fromjson | keys[]] | @csv
')

# Write headers to output file
# ----------------------------
echo "${HEADERS}" > "${OUTPUT_FILE}"

# Write all records to output file
# --------------------------------
echo "${RESPONSE}" | jq -r '
  .events[].message | fromjson | [.[]] | @csv
' >> "${OUTPUT_FILE}"

# Script execution summary
# -------------------------
RECORD_COUNT=$(echo "${RESPONSE}" | jq '.events | length')
echo "Exported ${RECORD_COUNT} records to ${OUTPUT_FILE}"

```
