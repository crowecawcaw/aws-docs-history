# Amazon Elastic Container Service

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you easily
deploy, manage, and scale containerized applications. You can inject sensitive data into your
containers by referencing Secrets Manager secrets. For more information, see the following pages in the
_Amazon Elastic Container Service Developer Guide_:

- [Tutorial:
  Specifying sensitive data using Secrets Manager secrets](../../../AmazonECS/latest/developerguide/specifying-sensitive-data-tutorial.md "../../../AmazonECS/latest/developerguide/specifying-sensitive-data-tutorial.md")
- [Retrieve secrets
  programmatically through your application](../../../AmazonECS/latest/developerguide/secrets-app-secrets-manager.md "../../../AmazonECS/latest/developerguide/secrets-app-secrets-manager.md")
- [Retrieve
  secrets through environment variables](../../../AmazonECS/latest/developerguide/secrets-envvar-secrets-manager.md "../../../AmazonECS/latest/developerguide/secrets-envvar-secrets-manager.md")
- [Retrieve secrets for
  logging configuration](../../../AmazonECS/latest/developerguide/secrets-logconfig.md "../../../AmazonECS/latest/developerguide/secrets-logconfig.md")
  Amazon ECS supports FSx for Windows File Server volumes for containers. Amazon ECS uses the
  credentials stored in a Secrets Manager secret to domain join the Active Directory and attach the FSx
  for Windows File Server file system. For more information, see [Tutorial: Using FSx for
  Windows File Server file systems with Amazon ECS](../../../AmazonECS/latest/developerguide/tutorial-wfsx-volumes.md "../../../AmazonECS/latest/developerguide/tutorial-wfsx-volumes.md") and [FSx for Windows File Server
  volumes](../../../AmazonECS/latest/developerguide/wfsx-volumes.md "../../../AmazonECS/latest/developerguide/wfsx-volumes.md") in the _Amazon Elastic Container Service Developer Guide_.

You can reference container images in private registries outside of AWS that require
authentication by using a Secrets Manager secret with the registry credentials. For more information,
see [Private registry authentication for tasks](../../../AmazonECS/latest/developerguide/private-auth.md "../../../AmazonECS/latest/developerguide/private-auth.md") in the _Amazon Elastic Container Service Developer
Guide_.

When you use Amazon ECS Service Connect, Amazon ECS uses Secrets Manager [managed secrets](service-linked-secrets.md "service-linked-secrets.md") to store AWS Private Certificate Authority TLS certificates.
The cost of storing the secret is included with the charges for Amazon ECS. To update the secret,
you must use Amazon ECS rather than Secrets Manager. For more information, see [TLS with Service
Connect](../../../AmazonECS/latest/developerguide/service-connect-tls.md "../../../AmazonECS/latest/developerguide/service-connect-tls.md") in the _Amazon Elastic Container Service Developer Guide_.
