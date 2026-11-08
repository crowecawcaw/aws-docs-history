

# Managing a DB instance in a self-managed Active Directory domain
<a name="oracle-smad-managing"></a>

You can use the AWS Management Console, the AWS CLI, or the Amazon RDS API to manage your Amazon RDS for Oracle DB instance and its relationship with your self-managed Active Directory (AD) domain. For example, you can move the DB instance into, out of, or between domains.

For example, with the AWS CLI you can do the following:
+ To retry a domain join that failed, run [modify-db-instance](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-db-instance.html) with the same four parameters: `--domain-fqdn`, `--domain-ou`, `--domain-auth-secret-arn`, and `--domain-dns-ips`.
+ To remove a DB instance from the domain, run `modify-db-instance` with the `--disable-domain` option.
+ To move a DB instance to another self-managed domain, run `modify-db-instance` with the four domain parameters, `--domain-fqdn`, `--domain-ou`, `--domain-auth-secret-arn`, and `--domain-dns-ips`, for the new domain.
+ To view the domain membership of a DB instance, run [describe-db-instances](https://docs.aws.amazon.com/cli/latest/reference/rds/describe-db-instances.html) and check the `DomainMemberships` field.

## Rotating the domain service account credentials
<a name="oracle-smad-managing.rotate-credentials"></a>

Amazon RDS uses the domain service account to maintain the user object for each DB instance and to rotate its Kerberos keys, not to authenticate your database users. When you change the password of the domain service account in AD, update the secret in Secrets Manager with the new password. Amazon RDS reads the updated secret automatically, so you don't need to modify or reboot the DB instance.

To update the secret, create a file named `smad-secret.json` with the following content. Replace *service-account* with the name of the domain service account that you created in Step 2 of [Setting up self-managed Active Directory](oracle-smad-setting-up.md), such as `rds-join-svc`, and `your-new-service-account-password` with your new password.

```
{
    "SELF_MANAGED_ACTIVE_DIRECTORY_USERNAME": "service-account",
    "SELF_MANAGED_ACTIVE_DIRECTORY_PASSWORD": "your-new-service-account-password"
}
```

Replace `arn:aws:secretsmanager:us-west-2:123456789012:secret:my-ad-secret-AbCdEf` with your secret Amazon Resource Name (ARN) and run the following commands.

For Linux, macOS, or Unix:

```
aws secretsmanager put-secret-value \
    --secret-id "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-ad-secret-AbCdEf" \
    --secret-string file://smad-secret.json
```

For Windows:

```
aws secretsmanager put-secret-value ^
    --secret-id "arn:aws:secretsmanager:us-west-2:123456789012:secret:my-ad-secret-AbCdEf" ^
    --secret-string file://smad-secret.json
```

## Force-rotating Kerberos keys
<a name="oracle-smad-managing.force-rotate-keys"></a>

Amazon RDS for Oracle rotates the Kerberos keys of the DB instance service account every 45 days. You don't need to take any action.

You can use the following Amazon RDS procedure to force the rotation of this key.

```
SELECT rdsadmin.rdsadmin_kerberos_auth_tasks.rotate_kerberos_keytab AS TASK_ID FROM DUAL;
```

The `SELECT` statement returns the ID of the task in a `VARCHAR2` data type. You can view the status of an ongoing task in a bdump file. The bdump files are located in the `/rdsdbdata/log/trace` directory. Each bdump file name is in the following format.

```
dbtask-{{task-id}}.log
```

You can view the result by displaying the task's output file.

```
SELECT text FROM table(rdsadmin.rds_file_util.read_text_file('BDUMP','dbtask-{{task-id}}.log'));
```

Replace {{task-id}} with the task ID returned by the procedure.

**Note**  
Tasks are executed asynchronously.