

# Get the Slurm cluster secret
<a name="working-with_clusters_secrets_get"></a>

You can use Secrets Manager to get the current version of a Slurm cluster secret. Secrets Manager returns the secret as a base64-encoded string. The following example uses the AWS CLI. Make the following substitutions before running the command. 
+ Replace `{{region}}` with the AWS Region to create your cluster in, such as `us-east-1`.
+ Replace `{{secret-arn}}` with the `secretArn` from an AWS PCS cluster.

```
aws secretsmanager get-secret-value \
    --region {{region}} \
    --secret-id '{{secret-arn}}' \
    --version-stage AWSCURRENT \
    --query 'SecretString' \
    --output text
```

**Important**  
Secrets Manager stores and returns the cluster secret as a base64-encoded string, but Slurm requires the secret as the raw (decoded) bytes. If you write the secret to a Slurm key file (for example, `/etc/slurm/slurm.key`), you must base64-decode the value first. Writing the base64-encoded string directly produces a key file that Slurm cannot use. `slurmd` then fails authentication with an error such as `decode_jwt: jwt_decode (with key) failure: Invalid argument`.  
To decode the secret and write it to a key file, pipe the output through `base64 -d`:  

```
aws secretsmanager get-secret-value \
    --region {{region}} \
    --secret-id '{{secret-arn}}' \
    --version-stage AWSCURRENT \
    --query 'SecretString' \
    --output text | base64 -d | sudo tee /etc/slurm/slurm.key
```

**Note**  
You don't need to retrieve the cluster secret yourself on a AWS PCS-managed compute node group. AWS PCS delivers the secret to instances launched by the compute node group as part of the node bootstrap. Retrieve the secret manually only when you configure a Slurm client outside of a managed compute node group, such as a persistent login node.

For information about how to use the Slurm cluster secret, see [Using standalone instances as AWS PCS login nodes](working-with_login-nodes_standalone.md).

**Permissions**  
You use an IAM principal to get the Slurm cluster secret. The IAM principal must have permission to read the secret. For more information, see [Roles terms and concepts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html) in the *AWS Identity and Access Management User Guide*.

The following sample IAM policy allows access to an example cluster secret.

```
{
    "Version": "2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "AllowSecretValueRetrievalAndVersionListing",
            "Effect": "Allow",
            "Action": [
                "secretsmanager:GetSecretValue",
                "secretsmanager:ListSecretVersionIds"
            ],
            "Resource": "arn:aws:secretsmanager:us-east-1:012345678901:secret:pcs!slurm-secret-s3431v9rx2-FN7tJF"
        }
    ]
}
```