# Managed rotation for AWS Secrets Manager secrets

Some services offer _managed rotation_, where the service configures and manages rotation for you. With managed rotation, you don't use an AWS Lambda function to update the secret and the credentials in the database.

The following services offer managed rotation:

- **Amazon Aurora** offers managed rotation for master user credentials. For more information, see [Password management with Amazon Aurora and AWS Secrets Manager](../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.md") in the _Amazon Aurora User Guide_.
- **Amazon ECS** Service Connect offers managed rotation for AWS Private Certificate Authority TLS certificates. For more information, see [TLS with Service Connect](../../../AmazonECS/latest/developerguide/service-connect-tls.md "../../../AmazonECS/latest/developerguide/service-connect-tls.md") in the _Amazon Elastic Container Service Developer Guide_.
- **Amazon RDS** offers managed rotation for master user credentials. For more information, see [Password management with Amazon RDS and AWS Secrets Manager](../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md "../../../AmazonRDS/latest/UserGuide/rds-secrets-manager.md") in the _Amazon RDS User Guide_.
- **Amazon Redshift** offers managed rotation for admin passwords. For more information, see [Managing Amazon Redshift admin passwords using AWS Secrets Manager](../../../redshift/latest/mgmt/redshift-secrets-manager-integration.md "../../../redshift/latest/mgmt/redshift-secrets-manager-integration.md") in the _Amazon Redshift Management Guide_.

###### Tip

For all other types of secrets, see [Rotation by Lambda function](rotate-secrets_lambda.md "rotate-secrets_lambda.md").

Rotation for managed secrets typically completes within one minute. During rotation, new connections that retrieve the secret may get the previous version of the credentials. In applications, we strongly recommend that you follow the best practice of using a database user created with the minimal privileges required for your application, rather than using the master user. For application users, for highest availability, you can use the [Alternating users rotation strategy](rotation-strategy.md "rotation-strategy.md").

###### To change the schedule for managed rotation

1. Open the managed secret in the Secrets Manager console. You can follow a link from the managing service, or [search for the secret](service-linked-secrets.md "service-linked-secrets.md") in the Secrets Manager console.
2. Under **Rotation schedule**, enter your schedule in UTC
   time zone in either the **Schedule expression builder**
   or as a **Schedule expression**. Secrets Manager stores your schedule as a
   `rate()` or `cron()`
   expression. The rotation window automatically starts at midnight
   unless you specify a **Start time**. You can rotate a secret as often as every four hours. For more
   information, see [Rotation schedules](rotate-secrets_schedule.md "rotate-secrets_schedule.md").
3. (Optional) For **Window duration**, choose the length of
   the window during which you want Secrets Manager to rotate your secret, for example
   `3h` for a three hour window. The window must not
   extend into the next rotation window. If you don't specify **Window
   duration**, for a rotation schedule in hours, the
   window automatically closes after one hour. For a rotation schedule in days, the
   window automatically closes at the end of the day.
4. Choose **Save**.

###### To change the schedule for managed rotation (AWS CLI)

- Call [`rotate-secret`](../../../cli/latest/reference/secretsmanager/rotate-secret.md "../../../cli/latest/reference/secretsmanager/rotate-secret.md"). The following example rotates the secret between 16:00 and 18:00 UTC on the 1st and 15th day of the month. For more information, see [Rotation schedules](rotate-secrets_schedule.md "rotate-secrets_schedule.md").

```
aws secretsmanager rotate-secret \
    --secret-id MySecret \
    --rotation-rules \
        "{\"ScheduleExpression\": \"cron(0 16 1,15 * ? *)\", \"Duration\": \"2h\"}"
```
