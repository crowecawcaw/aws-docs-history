

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Use custom plugins with the processing engine
<a name="influxdb3-custom-plugins"></a>

 Amazon Timestream for InfluxDB 3 lets you run your own Python plugins on the managed [processing engine](processing-engine.md). With custom plugins, you host your plugin code in one or more plugin repositories that you control – public or private – and the engine fetches and runs it in response to triggers (data writes, schedules, or HTTP requests). Use custom plugins to implement logic that is specific to your workload: custom data transformations, alerting, aggregation, and integrations with your own services. 

 You enable custom plugins by setting a plugin repository on a DB parameter group and applying that parameter group to your cluster. Custom plugins run on both Core and Enterprise editions. 

## How custom plugins work
<a name="influxdb3-custom-plugins-how-it-works"></a>

 You configure a plugin repository URL – and, for a private repository, a secret that holds an access token – as parameters on a DB parameter group. After your cluster uses that parameter group, you reference a plugin in a trigger with the `gh:` prefix. The engine resolves the path against your repository URL and fetches the raw file over HTTPS: 

```
gh:<path-to-plugin-file>   →   <plugin-repository-url>/<path-to-plugin-file>
```

 For example, with a plugin repository URL of `https://raw.githubusercontent.com/my-org/influxdb-plugins/main/`, a trigger created with `--path "gh:transforms/enrich.py"` fetches: 

```
https://raw.githubusercontent.com/my-org/influxdb-plugins/main/transforms/enrich.py
```

**Note**  
 The `gh:` prefix supports single-file plugins only. Each custom plugin must be a self-contained `.py` file addressable by a stable path under your repository URL. 

## Prerequisites
<a name="influxdb3-custom-plugins-prerequisites"></a>
+ An Amazon Timestream for InfluxDB 3 cluster (Core or Enterprise), with custom plugins enabled for your account.
+ A plugin repository reachable over HTTPS that serves raw plugin files (public or private).
+ Permission to create and apply DB parameter groups (`timestream-influxdb:CreateDbParameterGroup`, `timestream-influxdb:UpdateDbCluster`).
+ An InfluxDB 3 admin token for your cluster, to create and update triggers.
+ (Private repositories only) A read-only repository access token, and permission to create a secret in AWS Secrets Manager.

## Step 1: Create a parameter group with the plugin repository
<a name="influxdb3-custom-plugins-create-parameter-group"></a>

 Create a DB parameter group that sets the custom plugin repository. Set both parameters: the repository URL, and – for a private repository – the ARN of the Secrets Manager secret that holds your repository access token. 

```
aws timestream-influxdb create-db-parameter-group \
  --name my-plugin-parameter-group \
  --description "InfluxDB 3 cluster with a custom plugin repository" \
  --region us-west-2 \
  --parameters '{
    "InfluxDBv3Core": {
      "pluginRepositoryUrl": "https://raw.githubusercontent.com/my-org/influxdb-plugins/main/",
      "pluginRepositorySecretArn": "arn:aws:secretsmanager:us-west-2:111122223333:secret:InfluxDB-RepoToken-my-plugins-AbCdEf"
    }
  }'
```

Set the parameters under `InfluxDBv3Core`, or `InfluxDBv3Enterprise` for an Enterprise cluster:
+ `pluginRepositoryUrl` – The base HTTPS URL that serves your raw plugin files. It must use HTTPS with a valid host, and must not include embedded credentials, query strings, or fragments. The base can be a full repository path (recommended – it confines the cluster to that one repository) or a host-only URL if you need plugins from more than one repository (see [Use multiple plugin repositories](#influxdb3-custom-plugins-multiple-repos)). Include the branch (for example, `.../main/`) so plugin versions are predictable.

  The URL is normalized when you create the parameter group: a bare GitHub repository URL (`https://github.com/<owner>/<repo>`) is automatically rewritten to its raw-content form (`https://raw.githubusercontent.com/<owner>/<repo>`), and a trailing slash is removed (`.../main/` becomes `.../main`). GitHub `/tree/<branch>` and `/blob/...` web URLs are not rewritten – provide a raw-content base URL for those.
+ `pluginRepositorySecretArn` – The ARN of the Secrets Manager secret that holds your repository access token. Required only for private repositories. The secret must be in the same AWS account and AWS Region as the parameter group, and its name must begin with `InfluxDB-RepoToken-` (see [(Optional) Create the repository access secret](#influxdb3-custom-plugins-create-secret)). Omit this parameter for public repositories.

For a public repository, set only the URL:

```
aws timestream-influxdb create-db-parameter-group \
  --name my-plugin-parameter-group \
  --description "InfluxDB 3 cluster with a public custom plugin repository" \
  --region us-west-2 \
  --parameters '{
    "InfluxDBv3Core": {
      "pluginRepositoryUrl": "https://raw.githubusercontent.com/my-org/influxdb-plugins/main/"
    }
  }'
```

**Important**  
 The plugin repository parameters are immutable on an existing parameter group – there is no `UpdateDbParameterGroup` operation. To change the repository URL or secret, create a new parameter group and apply it to the cluster with `update-db-cluster`. 

## (Optional) Create the repository access secret
<a name="influxdb3-custom-plugins-create-secret"></a>

 If your plugin repository is private, create a Secrets Manager secret that holds a repository access token, then pass its ARN as `pluginRepositorySecretArn` in Step 1. Skip this section for public repositories. 

The secret must meet all of the following requirements, which are validated when you create the parameter group:
+ Its name begins with `InfluxDB-RepoToken-`. This is the only name pattern Timestream for InfluxDB is authorized to read; a secret with any other name is rejected.
+ It is in the same AWS account as the caller and the same AWS Region as the parameter group.
+ Its value is the access token itself, as a plain string (not JSON).

1.  In your repository provider, create a fine-grained, read-only access token scoped to only the plugin repositories you reference. Fine-grained tokens (for example, a GitHub fine-grained personal access token) let you limit access to specific repositories with read-only contents permission and an expiration date – prefer them over classic or broad tokens. With a host-only base URL, the same token is used for every fetch from the configured host, so it must have read access to each private repository your triggers reference. 

1. Store the token in Secrets Manager, with a name that begins with `InfluxDB-RepoToken-`:

   ```
   aws secretsmanager create-secret \
     --name InfluxDB-RepoToken-my-plugins \
     --secret-string "YOUR_REPOSITORY_ACCESS_TOKEN" \
     --region us-west-2
   ```

1. Copy the returned ARN and use it as the `pluginRepositorySecretArn` value in your parameter group.

 By default, the secret is encrypted with the AWS managed key for Secrets Manager (`aws/secretsmanager`), which requires no additional configuration. 

### Use a customer managed AWS KMS key (CMK)
<a name="influxdb3-custom-plugins-secret-cmk"></a>

 You can encrypt the repository token secret with a customer managed AWS KMS key. No changes to the key policy are required for the default case: Timestream for InfluxDB reads the secret using its service-linked role in your account, which already has scoped permission to decrypt `InfluxDB-RepoToken-*` secrets. Create the secret with the CMK and reference its ARN as usual: 

```
aws secretsmanager create-secret \
  --name InfluxDB-RepoToken-my-plugins \
  --secret-string "YOUR_REPOSITORY_ACCESS_TOKEN" \
  --kms-key-id arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab \
  --region us-west-2
```

**Note**  
 This works with a key that uses the default AWS KMS key policy (which delegates access to IAM identities in your account). If you replace the default key policy with a custom one that removes IAM delegation, you must ensure the Timestream for InfluxDB service-linked role (`AWSServiceRoleForTimestreamInfluxDB`) can still call `kms:Decrypt` on the key – otherwise plugin fetches fail with a AWS KMS access-denied error. 

## Step 2: Apply the parameter group to your cluster
<a name="influxdb3-custom-plugins-apply-parameter-group"></a>

 Associate the parameter group with a cluster, either when you create the cluster or by updating an existing cluster. Applying a parameter group runs a cluster maintenance action, so plan for a maintenance window. 

New cluster:

```
aws timestream-influxdb create-db-cluster \
  --name my-cluster \
  --db-instance-type db.influx.large \
  --db-parameter-group-identifier my-plugin-parameter-group \
  --vpc-subnet-ids subnet-0123456789abcdef0 subnet-0abcdef1234567890 \
  --vpc-security-group-ids sg-0123456789abcdef0 \
  --region us-west-2
```

Existing cluster:

```
aws timestream-influxdb update-db-cluster \
  --db-cluster-id my-cluster-id \
  --db-parameter-group-identifier my-plugin-parameter-group \
  --region us-west-2
```

When the cluster returns to the `AVAILABLE` state, the custom plugin repository is active.

## Step 3: Create a trigger that runs your custom plugin
<a name="influxdb3-custom-plugins-create-trigger"></a>

 Create triggers against your cluster's InfluxDB endpoint using the `influxdb3` CLI (or the HTTP API), and reference your custom plugin with the `gh:` prefix. The path after `gh:` is resolved against the `pluginRepositoryUrl` you configured in Step 1. 

Trigger on writes to a table:

```
influxdb3 create trigger \
  --trigger-spec "table:sensor_data" \
  --path "gh:transforms/enrich.py" \
  --database DATABASE_NAME \
  --token YOUR_ADMIN_TOKEN \
  enrich_sensor_data
```

Trigger on a schedule:

```
influxdb3 create trigger \
  --trigger-spec "every:5m" \
  --path "gh:metrics/custom_system.py" \
  --database DATABASE_NAME \
  --token YOUR_ADMIN_TOKEN \
  custom_metrics
```

Trigger on an HTTP request:

```
influxdb3 create trigger \
  --trigger-spec "request:ingest" \
  --path "gh:alerting/threshold.py" \
  --database DATABASE_NAME \
  --token YOUR_ADMIN_TOKEN \
  threshold_endpoint
```

 You can pass configuration to a custom plugin with `--trigger-arguments`, and control error handling and concurrency exactly as you do for other processing engine plugins. For the full command reference, see [influxdb3 create trigger](https://docs.influxdata.com/influxdb3/enterprise/reference/cli/influxdb3/create/trigger/) in the InfluxDB 3 documentation; for Amazon Timestream trigger configuration, see [Configure triggers](processing-engine.md#configuring-triggers). 

## Use multiple plugin repositories
<a name="influxdb3-custom-plugins-multiple-repos"></a>

 A parameter group registers one `pluginRepositoryUrl`, but if you set that base to the raw-content host only (no owner or repository), each trigger can select a different repository in its `gh:` path – for example, the public InfluxData repository and your own repository on the same cluster. The engine appends the trigger path to the base URL, so different triggers can load from different repositories. 

Set the repository URL to the host with no owner or repository path:

```
{
  "InfluxDBv3Core": {
    "pluginRepositoryUrl": "https://raw.githubusercontent.com"
  }
}
```

Then give each trigger the full owner/repository/branch/path after `gh:`:

```
# Plugin from the public InfluxData repository
influxdb3 create trigger \
  --trigger-spec "every:5m" \
  --path "gh:influxdata/influxdb3_plugins/main/influxdata/signal_generator/signal_generator.py" \
  --database DATABASE_NAME --token YOUR_ADMIN_TOKEN influxdata_signal

# Plugin from your own repository
influxdb3 create trigger \
  --trigger-spec "table:sensor_data" \
  --path "gh:my-org/my-plugins/main/transforms/enrich.py" \
  --database DATABASE_NAME --token YOUR_ADMIN_TOKEN my_enrich
```

Both resolve to `https://raw.githubusercontent.com/<the gh: path>`.
+ Include the **branch** (for example, `main`) in every `gh:` path – the segment after the repository name is required.
+ This applies to **public** repositories. For a private repository, also set `pluginRepositorySecretArn`. The token in that secret is used for every fetch from the configured host, so it must have read access to each private repository you reference.

**Important**  
 A host-only base lets the cluster load plugin code from *any* repository the host can serve – not only the ones you intend. Use it only when you genuinely need multiple repositories. When you use a single repository, pin the base to `https://raw.githubusercontent.com/<owner>/<repo>/<branch>/` so the cluster is confined to that one repository. Always point production clusters at reviewed, trusted repositories. 

## Update custom plugins
<a name="influxdb3-custom-plugins-update"></a>

 To update a plugin after you push changes to your repository, use the `influxdb3 update trigger` command against your cluster endpoint. This re-fetches the plugin and applies the change to the running trigger without recreating it – no cluster reboot is required: 

```
influxdb3 update trigger \
  --database DATABASE_NAME \
  --token YOUR_ADMIN_TOKEN \
  --trigger-name enrich_sensor_data \
  --path "gh:transforms/enrich.py"
```

 To change the plugin *repository* itself (URL or secret), create a new parameter group with the new values and apply it to the cluster with `update-db-cluster`. The repository parameters are immutable on an existing parameter group. 

## Security considerations
<a name="influxdb3-custom-plugins-security"></a>

 Custom plugins execute code that you supply inside your database engine. Treat plugin code as you would any code with access to your data. 
+ **Only use repositories you trust and control.** Custom plugins run within your cluster with access to your database.
+ **Use least-privilege, fine-grained repository tokens.** Scope the token to read-only access to only the plugin repositories your triggers reference, set an expiration, and rotate it periodically.
+ **Protect the secret.** Restrict access to the Secrets Manager secret with IAM. Optionally encrypt it with a customer managed AWS KMS key.
+ **Validate inputs in HTTP-request plugins.** Treat request bodies, headers, and query parameters as untrusted input.
+ **Pin the repository base URL.** A host-only base URL lets the cluster load plugin code from any repository the host can serve – not only the ones you intend. When you use a single repository, pin the base to `https://raw.githubusercontent.com/<owner>/<repo>/<branch>/` so the cluster is confined to that one repository.
+ **Use a vetted repository for production.** Point production clusters at a repository that contains only reviewed, approved plugin versions, and use change control for updates.

### Restrict the secret and CMK to Timestream for InfluxDB (resource policies)
<a name="influxdb3-custom-plugins-resource-policies"></a>

 By default, access to the repository-token secret and its encryption key is governed by IAM in your account. To tightly scope access so that only Timestream for InfluxDB – and no other principal in your account – can read the token secret and decrypt it, attach the following resource policies. Both grant the Timestream for InfluxDB service-linked role (`AWSServiceRoleForTimestreamInfluxDB`, created automatically in your account) exactly the two permissions it needs, and nothing more. Replace `<account-id>` and `<region>` with your values. 

**Secret resource policy (Secrets Manager)**  
Grants only the service-linked role `secretsmanager:GetSecretValue` on the secret:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowTimestreamInfluxDBReadRepoToken",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<account-id>:role/aws-service-role/timestream-influxdb.amazonaws.com/AWSServiceRoleForTimestreamInfluxDB"
      },
      "Action": "secretsmanager:GetSecretValue",
      "Resource": "*"
    }
  ]
}
```

Apply it (`"Resource": "*"` refers to the secret the policy is attached to):

```
aws secretsmanager put-resource-policy \
  --secret-id InfluxDB-RepoToken-my-plugins \
  --resource-policy file://secret-resource-policy.json \
  --region <region>
```

**CMK key policy (AWS KMS)**  
If the secret is encrypted with a customer managed key, attach a key policy that grants only the service-linked role `kms:Decrypt` / `kms:DescribeKey`, and only when the key is used through Secrets Manager (`kms:ViaService`). Keep the `EnableIAMRoot` statement so you don't lose administrative control of the key:

```
{
  "Version": "2012-10-17",
  "Id": "timestream-repo-token-key-policy",
  "Statement": [
    {
      "Sid": "EnableIAMRoot",
      "Effect": "Allow",
      "Principal": { "AWS": "arn:aws:iam::<account-id>:root" },
      "Action": "kms:*",
      "Resource": "*"
    },
    {
      "Sid": "AllowTimestreamInfluxDBDecryptViaSecretsManager",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::<account-id>:role/aws-service-role/timestream-influxdb.amazonaws.com/AWSServiceRoleForTimestreamInfluxDB"
      },
      "Action": [
        "kms:Decrypt",
        "kms:DescribeKey"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "kms:ViaService": "secretsmanager.<region>.amazonaws.com"
        }
      }
    }
  ]
}
```

Apply it:

```
aws kms put-key-policy \
  --key-id <cmk-key-id> \
  --policy-name default \
  --policy file://cmk-key-policy.json \
  --region <region>
```

**Note**  
Keep the `EnableIAMRoot` statement – removing it can lock you out of the key.
These resource-side grants scope access independently of the service-linked role's own identity policy, so they are the reliable way to restrict the secret and key to only Timestream for InfluxDB.
To scope the key even more tightly to this one secret, add a `"kms:EncryptionContext:SecretARN": "<secret-arn>"` entry to the `StringEquals` condition.

## Python dependencies
<a name="influxdb3-custom-plugins-dependencies"></a>

 Custom plugins run in a managed Python environment that includes the Python standard library and a set of pre-installed, Amazon-vetted libraries (for example, `numpy`, `pandas`, and `httpx`). To keep the environment secure and consistent, the Python package manager is **disabled** – you cannot install additional third-party packages from within a plugin or on the cluster. Write your custom plugins to use only the standard library and the pre-installed libraries. 

 If a plugin imports a package that is not available in the environment, the trigger fails when it runs. Check `system.processing_engine_logs` for the import error. 

## Limitations
<a name="influxdb3-custom-plugins-limitations"></a>
+ Only single-file plugins are supported from a custom repository.
+ The plugin repository must serve raw file bytes over HTTPS, with no embedded credentials, query strings, or fragments in the URL.
+ The repository access secret must be in the same AWS account and AWS Region as the parameter group and named `InfluxDB-RepoToken-*`.
+ The plugin repository parameters on a parameter group are immutable. To change the repository, create a new parameter group and apply it with `update-db-cluster`.

## Monitor custom plugin execution
<a name="influxdb3-custom-plugins-monitoring"></a>

 Custom plugins are monitored the same way as certified plugins. Query the processing engine system tables to confirm a plugin loaded and to troubleshoot failures: 

```
-- View processing engine logs for a trigger
SELECT * FROM system.processing_engine_logs
WHERE trigger_name = 'enrich_sensor_data'
  AND time > now() - INTERVAL '1 hour'
ORDER BY time DESC;

-- Check trigger status
SELECT * FROM system.processing_engine_triggers
WHERE database = 'DATABASE_NAME';
```

## Troubleshoot custom plugins
<a name="influxdb3-custom-plugins-troubleshooting"></a>


| Issue | Possible cause and resolution | 
| --- | --- | 
| CreateDbParameterGroup rejects the secret ARN | The secret must be in the same AWS account and AWS Region as the parameter group and named InfluxDB-RepoToken-\*. Verify all three. | 
| Invalid pluginRepositoryUrl | The URL must be HTTPS with a valid host, and must not contain credentials, query strings, or fragments. A host-only base URL (no repository path) is accepted. | 
| Plugin fetch fails with 404 Not Found | The plugin path doesn't exist at the resolved URL. Verify the gh: path and that pluginRepositoryUrl includes the correct branch. Note that GitHub /tree/<branch> and /blob/... URLs are not supported – use a raw-content base URL. | 
| Plugin fetch fails with 401/403 (private repository) | The access token is missing, expired, or lacks read access. Verify the token in the InfluxDB-RepoToken-\* secret and its scope. | 
| AWS KMS access-denied reading the secret | You replaced the default key policy on your CMK. Ensure the Timestream for InfluxDB service-linked role can kms:Decrypt the key. | 
| Updated a plugin but the trigger runs the old version | Run influxdb3 update trigger to re-fetch the updated plugin for that trigger. | 
| Plugin fails with a Python import error | The plugin imports a package that is not in the managed Python environment. The package manager is disabled; use only the standard library and pre-installed libraries. Check system.processing\_engine\_logs. | 