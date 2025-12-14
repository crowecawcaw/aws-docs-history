# ADVCOST04-BP01 Consider lower cost storage for older User

Profile data

As the 30 most recent days are most relevant, using DynamoDB can prioritize high
performance for the most relevant data (typically within the last 30 days), and archiving to
Amazon S3 can reduce costs for less relevant data.

**For S3 profile data:**

- Enable S3 Intelligent-Tiering on your bucket
- Configure lifecycle policies to transition older data
- Set up monitoring to track access patterns

1. **For DynamoDB:**
   - Implement TTL for old profile records
   - Create export jobs to move historical data to S3
   - Use S3 Lifecycle policies for long-term archival

**Cost optimization best practices**

- Regularly analyze data access patterns
- Use AWS Cost Explorer to track storage expenses
- Consider object size and retrieval frequency
- Implement tagging for better cost tracking

## Key AWS services

- DynamoDB
- S3
- Intelligent Tiering
