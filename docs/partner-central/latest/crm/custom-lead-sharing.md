# Lead sharing

## How AWS shares leads

1. **Incremental exports**: Amazon Web Services (AWS) exports new leads (and updates) referred by AWS, on an hourly basis.
2. **File creation**: AWS
   generates lead files adhering to a specific format. For
   detailed file specifications, refer to
   [Field definitions](resources.md#custom-field-definitions "resources.md#custom-field-definitions").
3. **File upload**: The lead files
   are uploaded to the `lead-outbound` folder.

## Consuming leads from AWS

To effectively consume leads from AWS, build
custom integration with the following functionalities.

1. **File retrieval**:
   - Regularly scan the `lead-outbound` folder
     using a scheduled job at an interval you choose.
   - Retrieve the lead files for processing.

2. **Data transformation and
   mapping**:
   - After you read the content of each file, transform and map the data to the lead records in your
     customer relationship management (CRM) system.
   - For guidance on field mapping, refer to
     [Field mapping](custom-field-mapping.md "custom-field-mapping.md").

3. **Lead identification**:
   - Uniquely identify each lead using either
     `partnerCrmLeadId` or
     `apnCrmUniqueIdentifier`.
   - If `partnerCrmLeadId` is blank and
     `apnCrmUniqueIdentifier` is present, the
     lead is a new referral from AWS Partner Network (APN) Customer Engagement (ACE).
   - If both identifiers are present, the record is treated as
     an update from ACE.

4. **Lead ingestion**:
   - Ingest new leads or update existing leads in the CRM
     system.

5. **File management**:
   - After you successfully process each lead and the complete
     file data, delete the files from the outbound folder.
   - Each file is automatically archived in the
     `lead-outbound-archive` folder.

**Integration and code reference**:

- For reading files uploaded to the Amazon Simple Storage Service (Amazon S3) bucket, you can use AWS Lambda or read directly from your CRM system.
- Use the sample codes below for Lambda and Salesforce REST API to
  validate and update CRM records.
  - **Lambda for validating files**: [ace_read_s3.py](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/ace_read_s3.py "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/ace_read_s3.py").
  - **Salesforce REST API**: [Apex_Sample_REST_API_Code.cls](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Apex_Sample_REST_API_Code.cls "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/code-snippets/Apex_Sample_REST_API_Code.cls").

- If you use a CRM system other than Salesforce, you must
  provide code specific to your system to update your data.

## Sharing updates on leads with AWS

1. **Identify leads**: Locate the
   leads with updates to be shared with AWS.
2. **Data transformation**:
   Convert the data into the AWS format, as outlined
   in [Field definitions](resources.md#custom-field-definitions "resources.md#custom-field-definitions").
3. **File creation**:
   - Generate lead files in JSON format.
   - Append a timestamp to each file, ensuring all file names
     are unique and follow the format:
     `{name}_MMDDYYYY24HHMMSS.json`.

4. **Authenticate and upload**:
   - Authenticate to the ACE Amazon S3 bucket.
   - Upload the file to the `lead-inbound`
     folder. All files shared with AWS are automatically
     archived in the `lead-inbound-archive`
     folder.
   - When you upload files to S3, ensure you provide
     full access to the bucket owner.

   ```
   aws s3 cp example.jpg s3://awsexamplebucket --acl bucket-owner-full-control
   ```

   See a sample result of running this command in
   ["Results Sample file.json"](https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Results-Success-Sample.json "https://github.com/aws-samples/partner-crm-integration-samples/blob/main/lead-samples/Lead-Results-Success-Sample.json").

5. **File processing**:
   - Upon receipt, AWS automatically processes the files.
   - The results of the processing is uploaded to the
     `lead-inbound-processed-results` folder
     in the Amazon S3 bucket. This includes the status of
     successes and errors, as well as any error messages for
     each lead.
   - These processed results are also archived in the
     `lead-inbound-processed-results-archive`
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
