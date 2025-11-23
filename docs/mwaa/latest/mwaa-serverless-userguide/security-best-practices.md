# Security best practices on Amazon MWAA Serverless

Amazon MWAA Serverless provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your workflow, treat them as helpful considerations rather than prescriptions.

- Use least-permissive permission policies. Grant permissions to only the resources or actions that users need
  to perform tasks.
- Use AWS CloudTrail to monitor user activity in your account.

## Security best practices in Apache Airflow

To implement security boundaries for your workflows:

- Store secrets in AWS Secrets Manager. While this will not prevent users who can write workflow definitions from reading secrets, it prevents them from modifying the secrets that your workflow uses.
