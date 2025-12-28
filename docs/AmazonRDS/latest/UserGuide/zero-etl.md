# Modifying Amazon RDS zero-ETL integrations

You can modify only the name, description, and data filtering options for a zero-ETL integration
in a supported data warehouse. You can't modify the AWS KMS key used to encrypt the integration, or the source or
target databases.

If you add a data filter to an existing integration, Amazon RDS reevaluates the filter as if it
always existed. It removes any data that is currently in the target data warehouse that
doesn't match the new filtering criteria. If you _remove_ a data filter
from an integration, it replicates any data that previously didn't match the filtering
criteria (but now does) into the target data warehouse. For more information, see [Data filtering for Amazon RDS zero-ETL integrations](zero-etl.md "zero-etl.md").

You can modify a zero-ETL integration using the AWS Management Console, the AWS CLI, or the Amazon RDS API.

###### To modify a zero-ETL integration

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Zero-ETL integrations**, and
   then choose the integration that you want to modify.
3. Choose **Modify** and make modifications to any available
   settings.
4. When all the changes are as you want them, choose
   **Modify**.
   To modify a zero-ETL integration using the AWS CLI, call the [modify-integration](../../../cli/latest/reference/rds/modify-integration.md "../../../cli/latest/reference/rds/modify-integration.md")
   command. Along with the `--integration-identifier`, specify any of the
   following options:

- `--integration-name` – Specify a new name for the
  integration.
- `--description` – Specify a new description for the
  integration.
- `--data-filter` – Specify data filtering options for the
  integration. For more information, see [Data filtering for Amazon RDS zero-ETL integrations](zero-etl.md "zero-etl.md").
  The following request modifies an existing integration.

For Linux, macOS, or Unix:

```
aws rds modify-integration \
    --integration-identifier `ee605691-6c47-48e8-8622-83f99b1af374` \
    --integration-name `my-renamed-integration`
```

For Windows:

```
aws rds modify-integration ^
    --integration-identifier `ee605691-6c47-48e8-8622-83f99b1af374` ^
    --integration-name `my-renamed-integration`
```

To modify a zero-ETL integration using the RDS API, call the [ModifyIntegration](../APIReference/API_ModifyIntegration.md "../APIReference/API_ModifyIntegration.md")
operation. Specify the integration identifier, and the parameters that you want to
modify.
