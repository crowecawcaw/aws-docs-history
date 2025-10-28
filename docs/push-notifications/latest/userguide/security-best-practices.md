# Security best practices

Use AWS Identity and Access Management (IAM) accounts to control access to API operations, especially operations that create, modify, or delete resources.
For the API, such resources include projects, campaigns and journeys.

- Create an individual user for each person who manages resources, including
  yourself. Don't use AWS root credentials to manage resources.
- Grant each user the minimum set of permissions required to perform his or her duties.
- Use IAM groups to effectively manage permissions for multiple users.
- Rotate your IAM credentials regularly.
  For more information about security, see [Security in AWS End User Messaging Push](security.md "security.md"). For
  more information about IAM, see [AWS Identity and Access Management](../../../IAM/latest/UserGuide/getting-set-up.md "../../../IAM/latest/UserGuide/getting-set-up.md"). For information on IAM best
  practices, see [IAM best practices](../../../IAM/latest/UserGuide/best-practices.md "../../../IAM/latest/UserGuide/best-practices.md").
