# AWS Secrets Manager secrets managed by other AWS services

Many AWS services store and use secrets in AWS Secrets Manager. In some cases, these secrets are _managed secrets_, which means that the service that created them helps manage them. For example, some managed secrets include [managed rotation](rotate-secrets_managed.md "rotate-secrets_managed.md"), so you don't have to configure rotation yourself. The managing service might also restrict you from updating secrets or
deleting them without a recovery period, which helps prevent outages because the managing service depends on the secret.

###### Note

Managed secrets can only be created by the AWS service that manages them.

Managed secrets use a naming convention that includes the managing service ID to help identify them.

```
Secret name: ServiceID!MySecret
Secret ARN : arn:aws:us-east-1:ServiceID!MySecret-a1b2c3
```

###### IDs for services that manage secrets

- `appflow` – [How Amazon AppFlow uses
  AWS Secrets Manager](integrating_how-services-use-secrets_appflow.md "integrating_how-services-use-secrets_appflow.md")
- `databrew` – [How AWS Glue DataBrew uses
  AWS Secrets Manager](integrating_how-services-use-secrets_databrew.md "integrating_how-services-use-secrets_databrew.md")
- `datasync` – [How AWS DataSync uses
  AWS Secrets Manager](integrating_how-services-use-secrets_datasync.md "integrating_how-services-use-secrets_datasync.md")
- `directconnect` – [How AWS Direct Connect uses
  AWS Secrets Manager](integrating_how-services-use-secrets_directconnect.md "integrating_how-services-use-secrets_directconnect.md")
- `ecs-sc` – [Amazon Elastic Container Service](integrating_how-services-use-secrets_ecs-sc.md "integrating_how-services-use-secrets_ecs-sc.md")
- `events` – [How Amazon EventBridge uses
  AWS Secrets Manager](integrating_how-services-use-secrets_events.md "integrating_how-services-use-secrets_events.md")
- `marketplace-deployment` – [AWS Marketplace](integrating_how-services-use-secrets_marketplace-deployment.md "integrating_how-services-use-secrets_marketplace-deployment.md")
- `opsworks-cm` – [How AWS OpsWorks for Chef Automate uses
  AWS Secrets Manager](integrating_how-services-use-secrets_opsworks-cm.md "integrating_how-services-use-secrets_opsworks-cm.md")
- `pcs` – [How AWS Parallel Computing
  Service uses AWS Secrets Manager](integrating_how-services-use-secrets_pcs.md "integrating_how-services-use-secrets_pcs.md")
- `rds` – [How Amazon RDS uses AWS Secrets Manager](integrating_how-services-use-secrets_RDS.md "integrating_how-services-use-secrets_RDS.md")
- `redshift` – [How Amazon Redshift uses AWS Secrets Manager](integrating_how-services-use-secrets_RS.md "integrating_how-services-use-secrets_RS.md")
- `sqlworkbench` – [Amazon Redshift query editor
  v2](integrating_how-services-use-secrets_sqlworkbench.md "integrating_how-services-use-secrets_sqlworkbench.md")
  To find secrets that are managed by other AWS services, see [Find managed secrets](manage_search-secret.md "manage_search-secret.md").

For a full list of services that use secrets, see [AWS services that use AWS Secrets Manager secrets](integrating.md "integrating.md").
