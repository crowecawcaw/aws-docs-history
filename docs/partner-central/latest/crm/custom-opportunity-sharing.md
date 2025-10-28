# Opportunity sharing

## How AWS shares opportunities

1. **Incremental exports**: Amazon Web Services (AWS) exports new opportunities (and updates) referred by AWS,
   on an hourly basis.
2. **File creation**: AWS
   generates opportunity files that adhere to a specific format. For
   detailed file specifications, refer to
   [Opportunity field definitions](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Fields.csv").
3. **File upload**: Opportunity files are uploaded to the
   `opportunity-outbound` folder.

## Consuming opportunities from AWS

To effectively consume opportunities from AWS, you need to
build custom integration with these functionalities.

1. **File retrieval**:
   - Use a scheduled job to regularly scan the `opportunity-outbound`
     folder, at an interval you choose.
   - Retrieve the opportunity files for processing.

2. **Data transformation and
   mapping**:
   - After you read the content of each file, transform and map the data to the opportunity records in
     your customer relationship management (CRM) system.
   - For guidance on field mapping, refer to
     [Field mapping](custom-field-mapping.md "custom-field-mapping.md").

3. **Opportunity identification**:
   - Uniquely identify each opportunity using either
     `partnerCrmOpportunityId` or
     `apnCrmUniqueIdentifier`.
   - If `partnerCrmOpportunityId` is blank and
     `apnCrmUniqueIdentifier` is present, the
     opportunity is a new referral from AWS Partner Network (APN) Customer Engagement
     (ACE).
   - If both identifiers are present, the record is treated as
     an update from ACE.

4. **Opportunity ingestion**: Ingest new opportunities or update existing opportunities in the CRM system.
5. **File management**:
   - After you successfully process each opportunity and the
     complete file data, delete the files from the outbound
     folder.
   - Each file is automatically archived in the
     `opportunity-outbound-archive` folder.

**Integration and code reference**:

- For reading files uploaded to the Amazon Simple Storage Service (Amazon S3) bucket, you can use AWS Lambda or read directly from your CRM system.
- Use the sample codes below for Lambda and Salesforce REST API to validate and update CRM records.
  - **Lambda for validating files**: [ace_read_s3.py](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/ace_read_s3.py "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/ace_read_s3.py").
  - **Salesforce REST API**: [Apex_Sample_REST_API_Code.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Apex_Sample_REST_API_Code.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Apex_Sample_REST_API_Code.cls").

- If you use a CRM system other than Salesforce, you must
  provide code specific to your system to update your data.

## Sharing updates to opportunities with AWS

1. **Identify opportunities**:
   Locate the opportunities with updates to be shared with
   AWS.
2. **Data transformation**:
   Convert the data into the AWS format, as outlined
   in [Field definitions](resources.md#custom-field-definitions "resources.md#custom-field-definitions").
3. **File creation**:
   - Generate opportunity files in JSON format.
   - Append a timestamp to each file, ensuring all file names
     are unique and follow the format:
     `{name}_MMDDYYYY24HHMMSS.json`.

4. **Authenticate and upload**:
   - Authenticate to the ACE Amazon S3 bucket.
   - Upload the file to the `opportunity-inbound` folder. All files
     shared with AWS are automatically archived in the
     `opportunity-inbound-archive` folder.
   - When you upload files to S3, ensure you provide
     full access to the bucket owner:

   ```
   aws s3 cp example.jpg s3://awsexamplebucket --acl bucket-owner-full-control
   ```

   See a sample result of running this command in
   [Opportunity Results Success Sample.json](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Results-Success-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/opportunity-samples/Opportunity-Results-Success-Sample.json").

5. **File processing**:
   - Upon receipt, AWS automatically processes the files.
   - The results of the processing is uploaded to the
     `lead-inbound-processed-results` folder
     in the Amazon S3 bucket. This includes the status of
     successes and errors, as well as any error messages for
     each opportunity.
   - These processed results are also archived in the
     `opportunity-inbound-processed-results-archive`
     folder.
   - For more information, refer to the
     [Technical FAQ—leads and opportunities](technical-faq-leads-and-opps.md "technical-faq-leads-and-opps.md").

6. **Response handling**:
   - You must develop logic to consume these
     responses, review erroneous records, correct any errors,
     and resend the data to ACE.
   - You can find sample errors in the FAQ and Troubleshooting sections.
   - To upload a file to Amazon S3 from CRM:
     - Reference the version of the AWS signature.
     - Use an HTTPS request to upload the file.

   - For reference, use the following files to upload
     a file to the Amazon S3 bucket:
     - **For authenticating an S3
       bucket**:
       [S3_Authentication.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/S3_Authentication.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/S3_Authentication.cls")
     - **For uploading files to an S3
       bucket**:
       [Sample_AceOutboundBatch.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Sample_AceOutboundBatch.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Sample_AceOutboundBatch.cls")

   - **NOTE:**
     Files must not exceed 1 MB in size, and duplicate files
     won’t be processed.
