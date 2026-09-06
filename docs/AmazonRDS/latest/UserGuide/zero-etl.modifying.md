

# Modifying Amazon RDS zero-ETL integrations
<a name="zero-etl.modifying"></a>

You can modify only the name, description, and data filtering options for a zero-ETL integration in a supported data warehouse. You can't modify the AWS KMS key used to encrypt the integration, or the source or target databases.

If you add a data filter to an existing integration, Amazon RDS reevaluates the filter as if it always existed. It removes any data that is currently in the target data warehouse that doesn't match the new filtering criteria. If you *remove* a data filter from an integration, it replicates any data that previously didn't match the filtering criteria (but now does) into the target data warehouse. For more information, see [Data filtering for Amazon RDS zero-ETL integrations](zero-etl.filtering.md).

You can modify a zero-ETL integration using the AWS Management Console, the AWS CLI, or the Amazon RDS API.

## RDS console
<a name="modify-integration-console"></a>

**To modify a zero-ETL integration**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Zero-ETL integrations**, and then choose the integration that you want to modify. 

1. Choose **Modify** and make modifications to any available settings.

1. When all the changes are as you want them, choose **Modify**.

## AWS CLI
<a name="modify-integration-cli"></a>

To modify a zero-ETL integration using the AWS CLI, call the [modify-integration](https://docs.aws.amazon.com/cli/latest/reference/rds/modify-integration.html) command. Along with the `--integration-identifier`, specify any of the following options:
+ `--integration-name` – Specify a new name for the integration.
+ `--description` – Specify a new description for the integration.
+ `--data-filter` – Specify data filtering options for the integration. For more information, see [Data filtering for Amazon RDS zero-ETL integrations](zero-etl.filtering.md).

**Example**  
The following request modifies an existing integration.  
For Linux, macOS, or Unix:  

```
aws rds modify-integration \
    --integration-identifier {{ee605691-6c47-48e8-8622-83f99b1af374}} \
    --integration-name {{my-renamed-integration}}
```
For Windows:  

```
aws rds modify-integration ^
    --integration-identifier {{ee605691-6c47-48e8-8622-83f99b1af374}} ^
    --integration-name {{my-renamed-integration}}
```

## RDS API
<a name="modify-integration-api"></a>

To modify a zero-ETL integration using the RDS API, call the [ModifyIntegration](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ModifyIntegration.html) operation. Specify the integration identifier, and the parameters that you want to modify.