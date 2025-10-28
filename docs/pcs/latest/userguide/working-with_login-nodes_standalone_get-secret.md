# Step 4 – Retrieve and

store the cluster secret

These instructions require the AWS CLI. For more information, see [Install or update to the latest version
of the AWS CLI](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") in the _AWS Command Line Interface User Guide for Version 2_.

Store the cluster secret with the following commands.

- Create the configuration directory for Slurm.

```
sudo mkdir -p /etc/slurm
```

- Retrieve, decode, and store the cluster secret. Before running this command, replace
  `region-code` with the Region where the target cluster is running,
  and replace `secret-arn` with the value for `secretArn`
  retrieved in [Step 1](working-with_login-nodes_standalone_get-addr.md "working-with_login-nodes_standalone_get-addr.md").

```
aws secretsmanager get-secret-value \
 --region `region-code` \
 --secret-id '`secret-arn`' \
 --version-stage AWSCURRENT \
 --query '`SecretString`' \
 --output text | base64 -d | sudo tee /etc/slurm/slurm.key
```

###### Warning

In a multiuser environment, any user with access to the instance might be able to fetch
the cluster secret if they can access the instance metadata service (IMDS). This, in turn,
could allow them to impersonate other users. Consider restricting access to IMDS to root or
administrative users only. Alternatively, consider using a different mechanism that doesn't
rely on the instance profile to fetch and configure the secret.

- Set ownership and permissions on the Slurm key file.

```
sudo chmod 0600 /etc/slurm/slurm.key
sudo chown slurm:slurm /etc/slurm/slurm.key
```

###### Note

The Slurm key must be owned by the user and group that the `sackd` service
runs as.
