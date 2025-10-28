# Security best practices

AWS End User Messaging SMS provides a number of security features to consider as you develop and implement your own
security policies. The following best practices are general guidelines and don’t represent a complete security
solution. Because these best practices might not be appropriate or sufficient for your environment, treat them
as helpful considerations rather than prescriptions.

- Create an individual user for each person who manages AWS End User Messaging SMS resources, including
  yourself. Don't use AWS root credentials to manage AWS End User Messaging SMS resources.
- Grant each user the minimum set of permissions required to perform his or her duties.
- Use IAM groups to effectively manage permissions for multiple users.
- Rotate your IAM credentials regularly.
