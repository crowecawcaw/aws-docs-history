# Provide agent resources from an S3 bucket

Connect an Amazon S3 bucket to your Agent Space to give AWS Security Agent the source code and documents it works from, such as source code archives, API documents, and threat model or design documents.

S3 buckets are an Agent Space-wide integration. The buckets you connect are shared across capabilities. The same bucket can supply source code for code review and threat modeling, and supporting context — such as API specifications and design documents — for penetration testing. You connect a bucket once. When you create a code review, penetration test, or threat model in the web application, you select the specific resources you need.

Providing relevant resources helps the agent understand your application, which can improve coverage, reduce false positives, and produce more actionable findings.

## Prerequisites

Before you begin, ensure you have:

- An Agent Space created in the AWS Management Console (see [Create an Agent Space](create-agent-space.md "create-agent-space.md")).
- An Amazon S3 bucket in the same AWS account as your Agent Space that contains the resources you want to provide.
- Permissions to configure integrations for your Agent Space.

## Add an S3 bucket

You add S3 buckets while configuring a capability for your Agent Space. The **S3 buckets** section appears in the code review, penetration test, and threat modeling configuration, and the buckets you add there are shared across all three.

1. In the AWS Security Agent console, select your Agent Space.
2. Open the configuration for any capability that uses shared integrations, such as the **Code review** or **Penetration test** tab, and go to the **S3 buckets** section.
3. Choose **Add S3 resource**.
4. Enter the **S3 URI** for the bucket or prefix that contains your resources.
5. Choose **Add**.

###### Note

You can add up to 10 S3 resources. S3 buckets are shared across capabilities, including code review, penetration testing, and threat modeling.

## Requirements for code review sources

For code review, S3 sources must be ZIP files stored in a connected bucket. Any ZIP file in a connected bucket can be selected as a source when a user creates a code review. Resources that you provide as context for penetration testing or threat modeling, such as API documents or design documents, do not need to be ZIP files.

## Next steps

- Enable code review and select S3 sources (see [Enable code review](enable-code-review-scan.md "enable-code-review-scan.md")).
- Configure penetration testing for your Agent Space (see [Enable penetration test](enable-penetration-test.md "enable-penetration-test.md")).
- Run a threat model on connected sources (see [Enable threat modeling](enable-threat-model.md "enable-threat-model.md")).
- Run a differential code scan from a diff stored in S3 (see [Run a differential code scan with S3](run-diff-scan-s3.md "run-diff-scan-s3.md")).
