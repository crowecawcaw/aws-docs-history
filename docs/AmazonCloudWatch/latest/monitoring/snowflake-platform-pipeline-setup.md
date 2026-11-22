

# CloudWatch pipelines configuration for Snowflake Platform

In the following example, replace {{secret-arn}}, {{secret-region}}, {{account-identifier}}, {{role-name}}, and {{log-group-name}} with your own values. The following YAML pipeline configuration collects audit data from Snowflake `ACCOUNT_USAGE` views, maps it to OCSF, and sends it to a CloudWatch Logs log group:

```yaml
extension:
  aws:
    secrets:
      snowflake-credentials:
        secret_id: "<<secret-arn>>"
        region: "<<secret-region>>"
pipeline:
  source:
    snowflake_platform:
      account_identifier: "<<account-identifier>>"
      authentication:
        jwt_key_pair:
          user: "${{aws_secrets:snowflake-credentials:user}}"
          private_key: "${{aws_secrets:snowflake-credentials:private_key}}"
          private_key_passphrase: "${{aws_secrets:snowflake-credentials:private_key_passphrase}}"
      role: "<<role-name>>"
      warehouse: "COMPUTE_WH"
      # Valid range: positive duration up to P365D.
      backfill: "P7D"
  processor:
    - ocsf:
        version: "1.5"
        mapping_version: "1.5.0"
        schema:
          snowflake_platform: null
  sink:
    - cloudwatch_logs:
        log_group: "<<log-group-name>>"
```Parameters

`account_identifier` (required)  
Snowflake account identifier in the format `orgname-accountname` or `locator.region` (such as `myorg-myaccount` or `xy12345.us-east-1`). Can contain only letters, numbers, hyphens, underscores, and dots.

`authentication.jwt_key_pair.user` (required)  
Snowflake user name for JWT key-pair authentication. Must use `${{aws_secrets:...}}`.

`authentication.jwt_key_pair.private_key` (required)  
RSA private key in PEM format (PKCS\#8, minimum 2048 bits). Assign the matching public key to the Snowflake user with `ALTER USER ... SET RSA_PUBLIC_KEY`. Must use `${{aws_secrets:...}}`.

`authentication.jwt_key_pair.private_key_passphrase` (optional)  
Passphrase for an encrypted private key. Omit this parameter if the private key is unencrypted. Must use `${{aws_secrets:...}}`.

`role` (optional)  
Snowflake role that runs the queries. The role needs read access to the `ACCOUNT_USAGE` views. If you omit this parameter, the connector uses the user's default role.

`warehouse` (optional)  
Snowflake warehouse that runs the queries. The warehouse must be running or set to auto-resume. Default: `COMPUTE_WH`.

`database` (optional)  
Snowflake database that contains the audit views. Default: `SNOWFLAKE`.

`schema` (optional)  
Snowflake schema that contains the audit views. Default: `ACCOUNT_USAGE`.

`backfill` (optional)  
How far back the first run collects logs, in ISO 8601 duration format, such as `P1D` or `P7D`. Must be a positive duration of 365 days or less. You can also use `range` for this parameter. Default: `P365D`.

**Note**  
The pipeline retrieves the `user`, `private_key`, and `private_key_passphrase` values from AWS Secrets Manager.