# Technical FAQ—fields

**Q: Does the integration support CSV
format?**

No. The integration accepts only JSON file
formats.

**Q: When do the files have to be deleted from
outbound folders?**

Delete the files only after you successfully
process them.

**Q: If I accidentally delete the files from
outbound folders, where can I find the original files?**

The files are available in the
`opportunity-outbound-archive` and
`lead-outbound-archive` folders.

**Q: What do I do for support during
development?**

For assistance during
development, reach out to AWS Partner Network (APN) support on
Partner Central.

**Q: What is the difference between
`opportunityOwnerName` and
`opportunityOwnerEmail`?**

- `opportunityOwnerName`: The opportunity owner’s
  name in the partner organization. This needs to be a Partner Central
  user.
- `opportunityOwnerEmail`: The opportunity
  owner’s email in the partner organization. This needs to be a
  Partner Central user. If not provided, the opportunity is created
  with the Partner Central Alliance Lead as the owner.

**Q: What's the time zone for all the date
fields (`targetCloseDate`,
`lastModifiedDate`, `createdDate`,
and `acceptBy`)?**

The time zone for
the date fields is Greenwich Mean Time (GMT).

**Q: Are the inbound JSON files
versioned?**

No. Amazon Web Services (AWS) doesn’t support
versioning of the files. APN Customer Engagement (ACE) processes the
file immediately after receiving and then deletes the file after
successful processing. If we receive the same file name again,
it’s rejected.

**Q: What fields in the Amazon Simple Storage Service (Amazon S3) JSON file indicate the creation and latest
update date of a particular lead and opportunity?**

`createdDate` and
`lastModifiedDate`.

**Q: How do you determine if an opportunity is
new or existing?**

The field
`PartnerCrmUniqueIdentifier` is a unique identifier on each opportunity
that we require from the partner. This
identifier must be defined in the source CRM of the partner's
system. We use this to determine if an opportunity exists in AWS. If it exists, we update the opportunity with the shared information. If not, we create a new opportunity.

When we send data to the partner, we include both
`PartnerCrmUniqueIdentifier` and
`apnCrmUniqueIdentifier`. If the opportunity shared
by AWS is being sent for the first time, you won’t see any value for
`PartnerCrmUniqueIdentifier`. This helps you to
treat the opportunity as new from ACE. Once you ingest it into your
CRM, you send the updates back to us with both
`PartnerCrmUniqueIdentifier` and
`apnCrmUniqueIdentifier`.

**Q: Is it possible to have more than one
outbound and result JSON file in Amazon S3?**

Yes. Sometimes we may generate more files in the outbound folder.
Similarly, if you send files to the inbound folder, we process them
and keep the results files in the result folder. You must
tag or delete the result files after processing.

**Q: Does the outbound file contain more than
one record?**

Yes. The outbound file can contain multiple
records.

**Q: If 20 inbound opportunities are sent in a
single input JSON file under the opportunities section, and one of
the opportunities doesn’t comply with APN standard, what
happens?**

If the format is incorrect, regardless of
the case, the entire file is rejected. If the format is correct but
only one opportunity can’t be processed on our end, the results file
includes all 20 opportunities and their status, along with the error
message for the failed opportunity.

**Q: What are the key attributes to validate
if the JSON file was processed successfully?**

These are
the key attributes to help you understand if the JSON file processed
successfully.

```

{
  "inboundApiResults": [
    {
      "warnings": null,  // no warnings
      "partnerCrmUniqueIdentifier": "XXXX", //uniqueId from Partner side
      "isSuccess": true, // file successfully processed
      "errors": null, //no errors reported
      "apnCrmUniqueIdentifier": "OXXXX" //uniqueId from AWS side
    }
  ]
}

```

**Q: What happens if I send an invalid
JSON?**

You receive this error response:
"`[{input JSON}]` is not of type
`object`".

**Q: How many lead/opportunity records can be
included in a single inbound JSON file?**

A maximum of 50
records can be in one file.
