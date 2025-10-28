# Technical FAQ—leads and opportunities

## Send and receive leads and opportunities

**Q: Is there a file naming
convention?**

Each file name needs to be unique. We
recommend the file name
`PartnerProvided FileName+{timestamp}.json`.

**Q: What's the structure of the
results?**

Sample files for the results (success and error)
can be downloaded from the following locations:

- [Lead Results Success Sample.json](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Results-Success-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Results-Success-Sample.json")
- [Opportunity Results Success Sample.json](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Results-Success-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Results-Success-Sample.json")
- [Lead Results With Errors Sample.json](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Results_With-Errors-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Results_With-Errors-Sample.json")
- [Opportunity Results With Errors Sample.json](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Results_With-Errors-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Results_With-Errors-Sample.json")

**Q: What's the naming convention of the
results?**

`PartnerProvidedFileName_result.json`

**Q: What if I submit a second JSON
file with the same name?**

We won’t process the file, and
the file is moved to the archive folder.

**Q: What is the inbound file size
limit?**

The inbound file size limit is 1MB.

**Q: Is there a maximum number of
opportunities and leads that can be batched into one JSON
file?**

Given the 1MB limit, we recommend you have one
opportunity or lead per file.

**Q: I’m getting an access denied error
message, so I’m not able to upload the files. What should I
do?**

Partners receive an
_Access denied_
message for two reasons.

1. You uploaded the file into the `outbound` folder
   instead of the `inbound` folder. Upload the file into the `inbound` folder.
2. You need to provide a access control list (ACL). Use the
   following Amazon Web Services (AWS) CLI command for uploading
   the data file:

```

aws s3 cp example.json s3://awsexamplebucket --acl bucket-owner-full-control

```

**Q: What happens if files with extensions
such as `.pdf`, `.docx`, or
anything other than `.json` are
uploaded?**

We reject the files and generate a
`*.error.json` file with the reason details.

**Q: What do I do after I receive a data issue
error message in production?**

1. If the data needs to be
   corrected in the partner’s customer relationship management (CRM)
   system, after you correct the data, send the revised file to Amazon Simple Storage Service
   (Amazon S3).
2. If any clarifications are
   required for the data, reach out to your Partner Development Manager
   (PDM).
3. For any other technical support, raise an AWS Partner Network (APN) support case in the APN Portal.

**Q: Where can I find the results files and
how long are they available?**

The results
files are in the `lead-inbound-results`
and `opportunity-inbound-results` folders. They're available until you delete them. You can
delete the files after successful pull.

**Q: If I need to find a results file after
I delete it, where can we find it?**

You can find the results
files in the
`lead-inbound-results-archive/YYYY/MM/DD` and
`opportunity-inbound-results-archive/YYYY/MM/DD`
folders.

**Q: If there is any failure in APN processing the
file, how am I notified?**

APN has alarms that
automatically create Sev2 tickets to track the processing errors. We
review, resolve, and communicate these to partners.

**Q: What fields can be updated after the
opportunity is launched?**

The following fields can be
updated only by Independent Software Vendor (ISV) Accelerate
Partners:

- `isThisForMarketplace`
- `isNetNewBusinessForCompany`
- `deliveryModel`
- `awsFieldEngagement`
- `additionalComments`

**Q: I received a _Record not
editable_ error. What does it mean?**

When a
you send a new partner referred opportunity, it goes through
the validation process and the APN Customer Engagement (ACE) team
must approve or reject it. While the opportunity is in review and
has not yet been validated, you can’t
update the record, and you receive this error.

**Q: What happens if there is no activity on the
my side (example: I'm not processing the file or not
sending any inbound opportunity)?**

If you don't
send any information or aren't processing the files we provide, we
currently don’t have a mechanism in place to alert you. We
encourage you to monitor your system to ensure the information
is flowing to APN.

**Q: How soon are the JSON results available in
the results folder following the submission of a new/updated inbound
opportunity/lead?**

The processing is almost real time. You
should receive the files in less than five minutes.

**Q: If I send an inbound opportunity CRM that
doesn’t comply with the format/length restriction of the APN
standard, how does the system handle it? Does it generate the error
report?**

If the file isn't in the field definition format, the result file from APN calls out
the file.

**Q: I don’t have an AWS account ID at the
time of launching. What do I do?**

Per the ACE process,
`Launched` means workload completed and billing
started. This requires an AWS account ID. For more
information, refer to the [ACE Program FAQs](https://partnercentral.awspartner.com/partnercentral2/s/resources?Id=0690h000003xjjXAAQ "https://partnercentral.awspartner.com/partnercentral2/s/resources?Id=0690h000003xjjXAAQ").

**Q: Following User Acceptance Testing (UAT), how should the historical data be handled
during the move to production?**

By default,
when any updates happen in ACE, we send those opportunities to the
Amazon S3 bucket. For historical data that you don’t want to
process, you need to provide the
`partnerCrmUniqueIdentifier` with dummy values such
as `X0001, X0002….X000N` in the extract for what
you don’t want to process in your system. You need to write code to
recognize these identifiers and process them accordingly. The rest
of the opportunities provide the correct
`partnerCrmUniqueIdentifier` value. This ensures
that you have full control on what to process and what not to
process in your system.

**Q: Does the outbound file contain more than
one record?**

Yes. The outbound file can contain more than
one record.

**Q: Why does the data send _Accept
to view_ for some fields?**

For an AWS referred
opportunity or lead, all PII fields are masked with the label
_Accept to view_ until the opportunity or lead is
accepted by you. Once accepted, you receive all
data fields in the next sync cycle.

**Q: What do I do when a new AWS referred
opportunity or lead is synced for the first time?**

When a
new opportunity or lead is synced for the first time, you need to
accept or reject it to get additional data (example: customer
contacts).

## Creating and updating opportunities/leads

**Q: How do I ingest new _Partner
Referred (Originated)_ opportunities into ACE through the
integration?**

To create new opportunities in ACE
through the integration, you need to ingest the required opportunity
information in the defined JSON format into the
`opportunity-inbound` folder. AWS processes this
information, creates a new opportunity in ACE, and shares results of
a successful/failed create operation in the
`opportunity-inbound-processed-results` folder.

**Q: How does the integration differentiate
between new opportunity submissions and updates?**

The field `PartnerCrmUniqueIdentifier` on each
opportunity is a required unique identifier required. This
identifier must be defined in the your system source CRM. AWS
uses this to determine if an opportunity already exists in ACE. If
it's available in ACE, we use the
information shared to update the opportunity, but if
it's not available in ACE, we use the
information shared to create a new opportunity.

**Q: If I’ve already implemented the update
functionality through the integration, what do I need to do to use
the integration to submit (create) new opportunities?**

You
need to make the following changes to the existing integration:

1. Start ingesting new opportunities for creation in the
   `opportunity-inbound` folder. Provide updates in the same folder.
2. Ensure that the mandatory fields required to create are
   available in the Opportunity JSON shared.
3. Verify each new opportunity has a unique
   `PartnerCrmUniqueIdentifier` that doesn’t exist in ACE/Partner
   Central. An important go-live best practice is to map and update
   the existing data in ACE to each `PartnerCrmUniqueIdentifier` in
   your CRM so we don’t create duplicates when we receive updates.
   For assistance, contact ACE.

**Q: As part of the
go-live process, how do I update existing
opportunities in ACE with my
`PartnerCrmUniqueIdentifier`?**

The ACE team supplies you with a list of all open
opportunities to aid in preparation for the production launch. You must map these existing opportunities in ACE to their
respective `PartnerCrmUniqueIdentifier`, and return
the updated file to ACE for integration into AWS’s CRM.

If you choose to sync only a subset of the opportunities AWS
provides, you must develop logic to bypass AWS updates for any
opportunities you don’t want to process. This approach should also
be applied to future opportunities, post-onboarding. You must
supply the associated `partnerCrmUniqueIdentifier`
for opportunities that need alignment across both CRMs.
Additionally, you should indicate which opportunities you won’t be
updating (example: Marking closed-lost or closed-won opportunities)
to exclude them from updates. It’s important that all open/active
opportunities that AWS shares, and you accept, are assigned a
`partnerCrmUniqueIdentifier`.

**Q: Can I update only specific fields in the
opportunity or lead?**

Yes. You can provide only the fields
that require updates, along with the necessary identifiers.

**Q: Is it possible to change the
_ApnCrmUniqueIdentifier_**?

No. This identifier remains
constant for AWS and uniquely identifies each opportunity.

**Q: What if I provide an incorrect
_partnerCrmUniqueIdentifier_**?

If you provide an
incorrect identifier, a new opportunity is created. Ensure accuracy
to avoid data duplication.

**Q: Can I update opportunities that
AWS submitted?**

Yes. You can update opportunities AWS
submitted using the correct `partnerCrmUniqueIdentifier`.

**Q: How soon can I expect results for
submitted opportunities?**

The processing is almost
real time, and results are usually available within a few minutes in
the `opportunity-inbound-processed-results` folder.

**Q: What should I do if there are processing
errors for opportunities submitted?**

Review error details
in the results files, address issues, and seek further assistance
from the ACE support team.

**Q: Can I delete an opportunity through the
integration?**

No. Direct deletion is not supported.
You can update an opportunity to reflect a
_Closed_ status.

**Q: What does the _Record not
editable_ error mean?**

This error occurs if you try
to update an opportunity in ACE review. These opportunities can’t be
edited until validated.

**Q: What if don't send updates or
new opportunities?**

No new data is received and processed
if you don't send updates or new opportunities through the integration.

**Q: How long are the results files
available?**

Results files are available for a reasonable
duration. You should retrieve and manage them promptly.
