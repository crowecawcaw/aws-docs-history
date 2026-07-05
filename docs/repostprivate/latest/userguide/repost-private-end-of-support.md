End of support notice: On June 30, 2027, AWS
will end support for AWS re:Post Private. After June 30, 2027, you will
no longer be able to access the re:Post Private console or re:Post Private resources.
For more information, see [AWS re:Post Private end of support](repost-private-end-of-support.md "repost-private-end-of-support.md").

# AWS re:Post Private end of support

AWS re:Post Private will reach end of service on June 30, 2027. After this date, the re:Post Private
service will no longer be available, and all private re:Post Private spaces will be decommissioned. We
understand that re:Post Private has been a valuable tool for centralizing AWS technical content and
fostering private collaboration within your organization, and we are committed to helping you
transition smoothly to alternative solutions before the end-of-service date.

This guide provides information on what to expect leading up to June 30, 2027, recommended alternatives, step-by-step instructions for exporting your data, and answers to frequently asked questions.

## Service updates before end of service

Effective immediately, no new feature updates, or enhancements will be made to AWS re:Post Private. The service will remain operational and accessible in its current state through June 30, 2027, allowing you time to complete your transition. Security patches critical to maintaining service integrity may still be applied at AWS's discretion during this period.

We strongly encourage all customers to begin their offboarding and data migration process as soon as possible to avoid any last-minute disruptions.

## Alternative services

We recommend the following alternatives depending on your organization's needs:

**Option 1: Stack Overflow for Teams (now Stack Internal)**

For organizations seeking a feature set most similar to re:Post Private, Stack Overflow for Teams (recently rebranded as Stack Internal) offers a comprehensive private knowledge management and collaboration platform. Key benefits include:

- Private Q&A forums — Create a structured, searchable knowledge base with question-and-answer workflows similar to re:Post Private
- Knowledge centralization — Consolidate institutional knowledge into one accessible, searchable location to reduce silos
- Integrations — Connects with your existing tools and tech stack (Slack, Microsoft Teams, Jira, and more)
- Content curation and validation — Community tools that encourage your team to validate, share ideas, and build your knowledge ecosystem
- Enterprise-grade security — Dedicated support and robust security controls for enterprise environments
- AI-powered search — Helps teams find verified answers faster and reduces repetitive questions to subject matter experts

Learn more at: [https://stackoverflow.co/internal/](https://stackoverflow.co/internal/ "https://stackoverflow.co/internal/")

**Option 2: AWS Builder Center**

For organizations that want to create and participate in a community with other AWS builders, the AWS Builder Center provides a collaborative space to connect with the broader AWS community. Key benefits include:

- Community engagement — Connect with other AWS builders, share best practices, and learn from peers
- AWS ecosystem integration — Stay connected to the latest AWS resources, content, and community discussions
- Public collaboration — Engage in open knowledge sharing across the AWS builder community

Learn more at: [https://builder.aws.com/](https://builder.aws.com/ "https://builder.aws.com/")

## How to offboard your data

To ensure a smooth transition, you will need to export your re:Post Private data before June 30, 2027. Data egress will be facilitated through your AWS Technical Account Manager (TAM) and delivered to an Amazon S3 bucket that you designate. Follow the steps below:

### Prerequisites

- An active AWS account with permissions to create and manage S3 buckets
- Access to your assigned AWS Technical Account Manager (TAM)
- An Amazon S3 bucket configured to receive your exported data

Your exported data will be available in one of two formats, based on your preference: CSV format (compatible with Stack Overflow for Teams / Stack Internal) or a collection of JSON objects (for compatibility with other platforms). Please indicate your preferred format when contacting your TAM in Step 2.

### Step-by-step instructions

**Step 1: Create or identify an S3 bucket for your data**

1. Sign in to the AWS Management Console and navigate to the Amazon S3 service.
2. Create a new S3 bucket (or identify an existing one) to receive your re:Post Private data. Ensure the bucket is in your preferred AWS Region.
3. Configure appropriate bucket policies and access permissions. At minimum, ensure the bucket allows write access for the data egress process (your TAM will provide specific principal ARNs if needed).
4. (Recommended) Enable server-side encryption (SSE-S3 or SSE-KMS) on the bucket to protect your data at rest.
5. (Recommended) Enable versioning on the bucket to safeguard against accidental overwrites.

**Step 2: Contact your Technical Account Manager (TAM)**

1. Reach out to your assigned TAM to initiate the data egress process. If you are unsure who your TAM is, contact your AWS Account team or open a support case (see "Getting Help" below).
2. Provide your TAM with the following information:

   - Your re:Post Private space identifier(s) or AWS account ID associated to your re:Post Private space
   - The destination S3 bucket name and ARN (e.g., arn:aws:s3:::your-bucket-name)
   - The AWS account ID that owns the destination bucket
   - Your preferred timeline for data export (must be completed before June 30, 2027)
   - Your preferred export format: CSV or JSON objects

**Step 3: Configure bucket permissions for data transfer**

1. Your TAM will provide you with the specific IAM role or principal that will be used to write data to your bucket.
2. Update your S3 bucket policy to grant `s3:PutObject` and `s3:PutObjectAcl` permissions to the provided principal. Example bucket policy statement:

```
{
  "Sid": "AllowRePostDataEgress",
  "Effect": "Allow",
  "Principal": {
    "AWS": "<ARN provided by your TAM>"
  },
  "Action": [
    "s3:PutObject",
    "s3:PutObjectAcl"
  ],
  "Resource": "arn:aws:s3:::your-bucket-name/*"
}
```

3. Confirm with your TAM that the permissions are correctly configured.

**Step 4: Initiate and verify data export**

1. Your TAM will coordinate the data egress on your behalf and confirm when the export process has begun.
2. Once your TAM has submitted the data export request, you can expect delivery of your data within 3 business days. Once the export is complete, your TAM will notify you.
3. Verify the exported data in your S3 bucket. Your data will include questions, answers, discussions, articles, and associated metadata from your private re:Post.
4. Review the exported content for completeness and confirm receipt with your TAM.

**Step 5: Migrate data to your chosen alternative**

1. Once your data is in S3, download or access it as needed to import into your chosen alternative platform (Stack Overflow for Teams, AWS Builder Center, or another solution).
2. Refer to your chosen platform's documentation for import/migration procedures.

## Important deadlines

| Milestone                                               | Date                   |
| ------------------------------------------------------- | ---------------------- |
| Begin offboarding process (recommended)                 | As soon as possible    |
| Final deadline to initiate data egress with TAM         | June 15, 2027          |
| Expected data delivery after TAM submits export request | Within 3 business days |
| Service end date — all data permanently deleted         | June 30, 2027          |

###### Important

Any data not exported by June 30, 2027 will be permanently deleted and cannot be recovered.

## Getting help

If you have additional questions about the re:Post Private end-of-service transition, please use one of the following channels:

- **Contact your AWS Account team** — Reach out directly to your Technical Account Manager (TAM) or Account Manager for personalized guidance on your transition plan.
- **Open a Support ticket** — Sign in to the AWS Support Center and create a new case. Select "Account and Billing" or "Technical" as appropriate, and reference "re:Post Private end of service" in your subject line.

## Frequently asked questions

**Why is AWS re:Post Private being discontinued?**
After careful evaluation, AWS has decided to end the re:Post Private service to focus investments on other solutions that better serve our customers' evolving needs. We are committed to ensuring a smooth transition for all affected customers.

**When exactly will re:Post Private stop working?**
The service will be fully decommissioned on June 30, 2027. After this date, you will no longer be able to access your private re:Post or any data within it.

**Will I lose my data if I don't take action?**
Yes. Any data not exported before June 30, 2027 will be permanently deleted. We strongly recommend beginning the offboarding process immediately.

**What data will be included in the export?**
Your data export will include all content from your private re:Post, including questions, answers, discussions, articles, knowledge articles, and associated metadata (such as tags, timestamps, and author information).

**What format will my exported data be in?**
Your exported data will be available in one of two formats, based on your preference: CSV format or a collection of JSON objects for compatibility with other platforms. Please indicate your preferred format when contacting your TAM in Step 2.

**Is there a cost associated with the data export?**
There is no charge for the data egress process itself. However, standard Amazon S3 storage charges will apply for data stored in your destination bucket. Refer to Amazon S3 pricing for details.

**I don't know who my TAM is. How do I find out?**
You can contact your AWS Account team or open a support case through the AWS Support Center. If you have an Enterprise Support or Enterprise On-Ramp Support plan, a TAM is assigned to your account.

**Can I continue to use re:Post Private in a read-only mode after June 30, 2027?**
No. The service will be fully decommissioned on June 30, 2027. No access — including read-only access — will be available after that date.

**How does Stack Overflow for Teams compare to re:Post Private?**
Stack Overflow for Teams (Stack Internal) offers a very similar feature set to re:Post Private, including private Q&A forums, knowledge base articles, tagging, search, and team collaboration tools. It also offers additional integrations with third-party tools and AI-powered features for knowledge discovery.

**Is AWS Builder Center a direct replacement for re:Post Private?**
AWS Builder Center is not a direct 1:1 replacement. It is best suited for organizations that want to engage with the broader AWS builder community in a public or semi-public setting, rather than maintaining a fully private internal knowledge base. For a private knowledge management solution, Stack Overflow for Teams is the closer alternative.

**Can AWS help me migrate my content to Stack Overflow for Teams?**
AWS will export your data to an S3 bucket. From there, you will need to work with Stack Overflow for Teams on their import process. Please refer to Stack Overflow for Teams documentation or contact their sales team for migration assistance.

**What if I need more time beyond June 30, 2027?**
The June 30, 2027 end-of-service date is final. We encourage all customers to begin their transition as early as possible. If you anticipate challenges meeting this deadline, please contact your AWS Account team immediately to discuss your situation.

**Will there be any impact to my other AWS services?**
No. The end of re:Post Private will not affect any other AWS services in your account. Only the re:Post Private service will be decommissioned.
