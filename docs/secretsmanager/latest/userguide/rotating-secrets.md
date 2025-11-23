# Rotate AWS Secrets Manager secrets

_Rotation_ is the process of periodically updating a
secret. When you rotate a secret, you update the credentials in both the secret and the
database or service. In Secrets Manager, you can set up automatic rotation for your secrets. There are
two forms of rotation:

- [Managed rotation](rotate-secrets_managed.md "rotate-secrets_managed.md") – For most [managed secrets](service-linked-secrets.md "service-linked-secrets.md"), you use managed
  rotation, where the service configures and manages rotation for you. Managed
  rotation doesn't use a Lambda function.
- [Rotate Secrets Manager managed external secrets](rotate-secrets_external.md "rotate-secrets_external.md")
  – For secrets held by Secrets Manager partners, you use managed external secrets rotation to update the
  secret on the partner's system. This doesn't require a Lambda function.
- [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md") – For other types of secrets, Secrets Manager
  rotation uses a Lambda function to update the secret and the database or
  service.
