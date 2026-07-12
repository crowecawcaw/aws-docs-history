# Amazon Bedrock integration for RDS for Oracle

RDS for Oracle supports integration with Amazon Bedrock, enabling you to invoke foundation models
directly from your Oracle database using SQL. With this integration, you can use generative AI
capabilities such as text generation, summarization, and embedding generation without moving
data out of your database.

###### Note

Amazon Bedrock integration is supported only for Oracle Database 26ai.

###### Topics

- [Requirements for Bedrock integration](#Oracle.BedrockIntegration.requirements "#Oracle.BedrockIntegration.requirements")
- [Configuring Bedrock integration](#Oracle.BedrockIntegration.Configuring "#Oracle.BedrockIntegration.Configuring")
- [Using Bedrock integration](#Oracle.BedrockIntegration.Using "#Oracle.BedrockIntegration.Using")

## Requirements for Bedrock integration

To use Amazon Bedrock integration with RDS for Oracle, ensure that the following
requirements are met.

### Database requirements

- Your DB instance must run Oracle Database 26ai (26.0.0.0) or higher.
- The database user that invokes Bedrock models must have the
  `EXECUTE` privilege on the `DBMS_CLOUD` and
  `DBMS_CLOUD_AI` packages.
- The database must be configured with access control entries (ACEs) that
  allow outbound HTTPS access to the Bedrock runtime endpoint. For more
  information, see [Configuring Bedrock integration](#Oracle.BedrockIntegration.Configuring "#Oracle.BedrockIntegration.Configuring").

### AWS credentials requirements

- You must have an IAM user or role with permissions to invoke the desired
  Amazon Bedrock foundation models (the `bedrock:InvokeModel` and
  optionally `bedrock:InvokeModelWithResponseStream`
  actions).
- You must have requested and been granted access to the desired foundation
  models by using the Amazon Bedrock console. For more information, see [Access Amazon Bedrock foundation models](../../../bedrock/latest/userguide/model-access.md "../../../bedrock/latest/userguide/model-access.md") in the
  _Amazon Bedrock User Guide_.
- You must have AWS access keys (an access key ID and secret access key)
  for your IAM identity to store in the database by using
  `DBMS_CLOUD.CREATE_CREDENTIAL`.

### Amazon VPC network requirements

The RDS for Oracle DB instance must be able to reach the Amazon Bedrock runtime endpoint
(`bedrock-runtime.`region`.amazonaws.com`) on
port 443 (HTTPS). You can achieve this in one of the following ways.

###### Option 1: Amazon VPC interface endpoint (AWS PrivateLink) – recommended

Create a Amazon VPC interface endpoint for the Amazon Bedrock runtime service. This
keeps all traffic private within the AWS network and doesn't require
internet access.

1. Create a Amazon VPC interface endpoint using the service name:
   `com.amazonaws.`region`.bedrock-runtime`.
2. Place the endpoint in the same Amazon VPC and subnets as your Amazon RDS DB instance (or
   in subnets with connectivity to the DB instance subnets).
3. Attach a security group to the endpoint that allows inbound HTTPS (port

443)  from the DB instance's security group.

4. Enable Private DNS for the endpoint so that the standard hostname
   `bedrock-runtime.`region`.amazonaws.com`
   resolves to the private endpoint IP address.
5. Ensure that the DB instance's security group allows outbound HTTPS (port

443)  to the endpoint's security group (or to the endpoint's private
      IP addresses).

###### Option 2: NAT gateway (internet route)

If you don't use a Amazon VPC endpoint, the DB instance's subnet must have a
route to the internet through a NAT gateway.

1. Ensure that the DB instance is in a private subnet with a route to a NAT
   gateway.
2. The NAT gateway must be in a public subnet with a route to an internet
   gateway.
3. The DB instance's security group must allow outbound HTTPS (port 443) to
   `bedrock-runtime.`region`.amazonaws.com`.
4. Any Amazon VPC network ACLs on the DB instance's subnet must allow outbound TCP
   443 and the corresponding ephemeral inbound return traffic (TCP ports
   1024–65535).

The following table summarizes the network paths.

Network paths for Bedrock integration| Approach | Internet access needed | Traffic path |
| --- | --- | --- |
| Amazon VPC endpoint (AWS PrivateLink) | No | DB instance → Amazon VPC endpoint → Bedrock service |
| NAT gateway | Yes (outbound only) | DB instance → NAT gateway → internet gateway → Bedrock<br>service |

## Configuring Bedrock integration

To configure Amazon Bedrock integration for your RDS for Oracle DB instance, complete the
following steps.

### Step 1: Configure Amazon VPC network connectivity

Ensure that your DB instance can reach the Bedrock runtime endpoint by using one of the
network options described in [Amazon VPC network requirements](#Oracle.BedrockIntegration.requirements.Network "#Oracle.BedrockIntegration.requirements.Network"). To verify
connectivity after configuration, you can test from the database in a later
step.

### Step 2: Obtain AWS credentials with Bedrock permissions

Create an IAM user or role with the following policy (or attach it to an
existing identity).

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "BedrockInvoke",
      "Effect": "Allow",
      "Action": [
        "bedrock:InvokeModel",
        "bedrock:InvokeModelWithResponseStream"
      ],
      "Resource": [
        "arn:aws:bedrock:`region`::foundation-model/*"
      ]
    }
  ]
}
```

To restrict access to specific models, replace the wildcard with specific model
ARNs, for example:

```
"arn:aws:bedrock:us-east-1::foundation-model/anthropic.claude-sonnet-4-5-20250929-v1:0"
```

Generate access keys for this IAM user from the IAM console. You need the
access key ID and secret access key for the next step.

### Step 3: Grant database privileges

Connect as a DBA and grant the necessary privileges to the application
user.

```
-- Grant EXECUTE on DBMS_CLOUD and DBMS_CLOUD_AI
GRANT EXECUTE ON DBMS_CLOUD TO `db_user`;
GRANT EXECUTE ON DBMS_CLOUD_AI TO `db_user`;
```

### Step 4: Grant network ACL access for the Bedrock endpoint

Grant the database user network ACL access to the Bedrock runtime
endpoint.

```
BEGIN
  DBMS_NETWORK_ACL_ADMIN.APPEND_HOST_ACE(
    host => 'bedrock-runtime.`region`.amazonaws.com',
    ace  => xs$ace_type(
              privilege_list => xs$name_list('http'),
              principal_name => '`db_user`',
              principal_type => xs_acl.ptype_db)
  );
END;
/
```

Replace `region` with your AWS Region (for example,
`us-east-1`) and `db_user` with the Oracle
database user that will invoke Bedrock models.

### Step 5: Create a credential in the database

Connect as the application user and create a credential object by using
`DBMS_CLOUD`.

```
BEGIN
  DBMS_CLOUD.CREATE_CREDENTIAL(
    credential_name => 'AWS_BEDROCK_CRED',
    username        => '`your_AWS_access_key_id`',
    password        => '`your_AWS_secret_access_key`'
  );
END;
/
```

### Step 6: Create an AI profile for Bedrock

Create an AI profile by using `DBMS_CLOUD_AI` that references your
credential and specifies AWS as the provider.

```
BEGIN
  DBMS_CLOUD_AI.CREATE_PROFILE(
    profile_name => 'BEDROCK_PROFILE',
    attributes   => '{"provider": "aws",
      "credential_name": "AWS_BEDROCK_CRED",
      "model": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
      "object_list": [{"owner": "`schema`", "name": "`table1`"},
                      {"owner": "`schema`", "name": "`table2`"}]
    }'
  );
END;
/
```

To use an Amazon Bedrock runtime endpoint in a Region other than
`us-east-1`, include the `region` and
`target_language` attributes in the profile attributes JSON. Set
`region` to the Region where your Amazon Bedrock runtime endpoint is
located (for example, `us-west-2`).

If you set `region`, you must also include
`target_language` or `source_language`. You must set both
attributes together, even for actions that do not use translation, such as
`chat` or `runsql`.

The `target_language` value affects only the `translate`
action. If you include only `target_language` without
`region`, the profile continues to use
`bedrock-runtime.us-east-1.amazonaws.com`.

###### Note

You must set `target_language` alongside `region`
because of a known limitation of the Oracle `DBMS_CLOUD_AI`
package.

The following example creates a profile that uses the `us-west-2`
Region.

```
BEGIN
  DBMS_CLOUD_AI.CREATE_PROFILE(
    profile_name => 'BEDROCK_PROFILE_USW2',
    attributes   => '{"provider": "aws",
      "credential_name": "AWS_BEDROCK_CRED",
      "region": "us-west-2",
      "target_language": "en",
      "model": "us.anthropic.claude-sonnet-4-5-20250929-v1:0",
      "object_list": [{"owner": "`schema`", "name": "`table1`"},
                      {"owner": "`schema`", "name": "`table2`"}]
    }'
  );
END;
/
```

You must specify the `model` attribute explicitly. No default model is
provided for the AWS provider. For model IDs, see the following references:

- Base models: [Amazon Bedrock base model IDs](../../../bedrock/latest/userguide/model-ids.md "../../../bedrock/latest/userguide/model-ids.md").
- Cross-Region inference profiles: [Supported Regions and models for cross-region inference](../../../bedrock/latest/userguide/cross-region-inference-support.md "../../../bedrock/latest/userguide/cross-region-inference-support.md").
- Provisioned Throughput: specify the ARN of the Provisioned
  Throughput.
- Custom models: purchase Provisioned Throughput, and then specify the ARN
  of the resulting provisioned model.

### Verifying your Bedrock integration

Test connectivity with a simple prompt.

```
EXEC DBMS_CLOUD_AI.SET_PROFILE('BEDROCK_PROFILE');
SELECT AI chat what is Amazon RDS;
```

If the response returns successfully, your Bedrock integration is configured
correctly.

## Using Bedrock integration

After you configure the integration, you can invoke Amazon Bedrock foundation models
from your Oracle database using SQL with Select AI.

For complete usage examples with Amazon Bedrock – including `SELECT
 AI` actions (`runsql`, `showsql`, `narrate`,
`chat`, and `explainsql`), the
`DBMS_CLOUD_AI.GENERATE` function, multi-turn conversations, and
retrieval augmented generation (RAG) – see the following Oracle
documentation:

- [Example: Select AI with AWS](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-examples.html#GUID-A2B7D8BB-5CBF-49D4-B12C-8AB54BA7D0A2 "https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-examples.html#GUID-A2B7D8BB-5CBF-49D4-B12C-8AB54BA7D0A2")
- [Manage AI Profiles – Use AWS](https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-manage-profiles.html#GUID-B71D2617-F079-4982-A979-6C1C8C58B577 "https://docs.oracle.com/en/cloud/paas/autonomous-database/serverless/adbsb/select-ai-manage-profiles.html#GUID-B71D2617-F079-4982-A979-6C1C8C58B577")
- [DBMS\_CLOUD\_AI Package Reference](https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/dbms_cloud_ai1.html "https://docs.oracle.com/en/database/oracle/oracle-database/26/arpls/dbms_cloud_ai1.html")
