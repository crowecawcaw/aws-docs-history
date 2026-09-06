

# Get the Slurm cluster secret
<a name="working-with_clusters_secrets_get"></a>

You can use Secrets Manager to get the current base64-encoded version of a Slurm cluster secret The following example uses the AWS CLI. Make the following substitutions before running the command. 
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