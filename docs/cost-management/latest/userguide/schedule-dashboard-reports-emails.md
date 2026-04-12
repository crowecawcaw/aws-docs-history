# Understanding scheduled report emails

When a scheduled report is generated, recipients receive an email notification
containing:

- A secure, time-limited download link to access the PDF report. The link expires after
  15 days.
- A unique password required to open the PDF file. Each report generation produces a new
  password.
- The report name, dashboard name, and generation timestamp.
  PDF reports are encrypted and stored in AWS-managed Amazon S3 buckets. The download links use
  pre-signed URLs that grant time-limited access to the specific PDF file.
