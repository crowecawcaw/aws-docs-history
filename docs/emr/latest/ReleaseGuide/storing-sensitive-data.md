# Store sensitive configuration data in

AWS Secrets Manager

The Amazon EMR describe and list API operations that emit custom configuration data (such
as `DescribeCluster` and `ListInstanceGroups`) do so in plaintext.
Amazon EMR integrates with AWS Secrets Manager so that you can store your data in Secrets Manager and use
the secret ARN in your configurations. This way, you don't pass sensitive configuration
data to Amazon EMR in plaintext and expose it to external APIs. If you indicate that a
key-value pair contains an ARN for a secret stored in Secrets Manager, Amazon EMR retrieves this
secret when it sends configuration data to the cluster. Amazon EMR doesn't send the
annotation when it uses external APIs to display the configuration.

## Create a secret

To create a secret, follow the steps in [Create an AWS Secrets Manager
secret](../../../secretsmanager/latest/userguide/create_secret.md "../../../secretsmanager/latest/userguide/create_secret.md") in the _AWS Secrets Manager User Guide_. In **Step
3**, you must choose the **Plaintext** field to enter
your sensitive value.

Note that while Secrets Manager allows a secret to contain up to 65536 bytes, Amazon EMR
limits the combined length of the property key (excluding the annotation) and the
retrieved secret value to 1024 characters.

## Grant Amazon EMR access to retrieve the secret

Amazon EMR uses an IAM service role to provision and manage clusters for you. The
service role for Amazon EMR defines the allowable actions for Amazon EMR when it provisions
resources and performs service-level tasks that aren’t performed in the context of
an Amazon EC2 instance running within a cluster. For more information about service
roles, see [Service role for Amazon EMR (EMR
role)](../ManagementGuide/emr-iam-role.md "../ManagementGuide/emr-iam-role.md") and [Customize IAM
roles](../ManagementGuide/emr-iam-roles-custom.md "../ManagementGuide/emr-iam-roles-custom.md").

To allow Amazon EMR to retrieve the secret value from Secrets Manager, add the following
policy statement to your Amazon EMR role when you launch your cluster.

```
{
   "Sid":"AllowSecretsRetrieval",
   "Effect":"Allow",
   "Action":"secretsmanager:GetSecretValue",
   "Resource":[
      "arn:aws:secretsmanager:`<region>`:`<aws-account-id>`:secret:`<secret-name>`"
   ]
}
```

If you create the secret with a customer-managed AWS KMS key, you must also add
`kms:Decrypt` permission to the Amazon EMR role for the key that you use.
For more information, see [Authentication and
access control for AWS Secrets Manager](../../../secretsmanager/latest/userguide/auth-and-access.md "../../../secretsmanager/latest/userguide/auth-and-access.md") in the
_AWS Secrets Manager User Guide_.

## Use the secret in a configuration

classification

You can add the `EMR.secret@` annotation to any configuration property
to indicate that its key-value pair contains an ARN for a secret stored in
Secrets Manager.

The following example shows how to provide a secret ARN in a configuration
classification:

```
{
   "Classification":"core-site",
   "Properties":{
      "presto.s3.access-key":"`<sensitive-access-key>`",
      "EMR.secret@presto.s3.secret-key":"arn:aws:secretsmanager:`<region>`:`<aws-account-id>`:secret:`<secret-name>`"
   }
}
```

When you create your cluster and submit your annotated configuration, Amazon EMR
validates the configuration properties. If your configuration is valid, Amazon EMR strips
the annotation from the configuration and retrieves the secret from Secrets Manager to
create the actual configuration before applying it to the cluster:

```
{
   "Classification":"core-site",
   "Properties":{
      "presto.s3.access-key":"`<sensitive-access-key>`",
      "presto.s3.secret-key":"`<my-secret-key-retrieved-from-Secrets-Manager>`"
   }
}
```

When you call an action like `DescribeCluster`, Amazon EMR returns the
current application configuration on the cluster. If an application configuration
property is marked as containing a secret ARN, then the application configuration
returned by the `DescribeCluster` call contains the ARN and not the
secret value. This ensures that the secret value is only visible on the
cluster:

```
{
   "Classification":"core-site",
   "Properties":{
      "presto.s3.access-key":"`<sensitive-access-key>`",
      "presto.s3.secret-key":"arn:aws:secretsmanager:`<region>`:`<aws-account-id>`:secret:`<secret-name>`"
   }
}
```

## Update the secret value

Amazon EMR retrieves the secret value from an annotated configuration whenever the
attached instance group is starting, reconfiguring, or resizing. You can use
Secrets Manager to modify the value of a secret used in the configuration of a running
cluster. When you do, you can submit a reconfiguration request to each instance
group that you want to receive the updated value. For more information on how to
reconfigure an instance group, and things to consider when you do it, see [Reconfigure an instance group in a
running cluster](emr-configure-apps-running-cluster.md "emr-configure-apps-running-cluster.md").
