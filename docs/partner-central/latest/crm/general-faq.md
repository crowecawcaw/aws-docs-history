# General FAQ

## How does the integration work?

**Q: Can I access the Amazon Simple Storage Service (Amazon S3) bucket used for sending and receiving the
files?**

Yes. Partners can programmatically access the
Amazon S3 bucket using the secret/access key of the AWS Identity and Access Management (IAM) that has access to the bucket.
Partners won’t have console access to the Amazon S3 buckets because these
buckets are in Amazon Web Services (AWS)’s own account.

**Q: What skill set does the partner's
developer need?**

The partner’s developer needs to be
familiar with their customer relationship management (CRM) system
and Amazon S3.

**Q: Do the sample code files include
complete code or does the partner have to write the
code?**

The partner needs to write the code based on the
provided sample code files.

**Q: If the partner develops their solution
in Python, Golang, or any other language, does AWS Partner Network (APN) Customer
Engagement (ACE) provide any software development kit (SDK) in those languages for this
integration?**

No.

**Q: What is the sync process from the Amazon S3
bucket to internal ACE?**

Every hour, a batch process
runs to pick up the files and synchronize information. Any update
the AWS sales team makes on the record can take up to one
hour to be sent to the partner’s bucket. Partners may receive an
email notification about updates immediately, but the updates from
AWS may still be delayed by one hour.

**Q: What is the frequency of lead and
opportunity file uploads by ACE?**

ACE sends the leads
and opportunities data every one hour.

**Q: Is there a sandbox environment for
ACE?**

Yes. We do have a sandbox environment for ACE, but
we can’t provide access to partners due to security reasons. Raise
a support case on Partner Central if you want to have new
opportunities or leads pushed into your bucket.

**Q: How do we maintain identifiers across
the partner’s CRM and APN?**

To provide more flexibility for our partners, we use two sets of
identifiers in our system.

1. `apnCrmUniqueIdentifier`: AWS manages this
   identifier. It starts with `OXXXXXX` for
   opportunities and `LXXXXXX` for leads.
2. `PartnerCrmUniqueIdentifier`/`partnerCrmLeadId`:
   The partner manages this identifier on opportunities and
   leads, respectively, within their CRM. Partners should add this
   identifier while ingesting new opportunities to trace updates back
   to their CRM.

When an opportunity is sent without
`apnCrmUniqueIdentifier` or
`partnerCrmUniqueIdentifier`, AWS treats it as a
new opportunity and assigns a new
`apnCrmUniqueIdentifier` for the opportunity.

When an opportunity is sent with a
`apnCrmUniqueIdentifier` or
`partnerCrmUniqueIdentifier`, AWS treats it
as an update action and updates the existing opportunity with the
payload data.

**Q: How do I prevent duplicate records from
getting created in both systems?**

From the partner CRM
side, there must be a unique identifier for each record
that’s sent to ACE, which is called `partnerCrmUniqueIdentifier`.
Similarly, ACE also maintains a unique identifier for each record,
which is called `apnCrmUniqueIdentifier`. When the data is sent,
both ACE and the partner have to include these two fields, which
helps to identify if the record is a new opportunity (if blank) or
an existing opportunity (if populated).
