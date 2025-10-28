# Step 5: (Optional) Cleanup

Follow these steps to remove all the resources created in this tutorial.

###### Remove the resources created in this tutorial

1. Delete your deployment. You can use the following command to do so.

```
kubectl delete deployment `my-keyspaces-app` -n `my-eks-namespace`
```

2. Delete the Amazon EKS cluster and all Pods contained in it. This also deletes related resources
   like the service account and OIDC identity provider. You can use the following
   command to do so.

```
eksctl delete cluster --name `my-eks-cluster` --region `us-east-1`
```

3. Delete the IAM role used for the Amazon EKS service account with access permissions to Amazon Keyspaces. First, you have to remove
   the managed policy that is attached to the role.

```
aws iam detach-role-policy --role-name `my-iam-role` --policy-arn arn:aws:iam::aws:policy/AmazonKeyspacesFullAccess
```

Then you can delete the role using the following command.

```
aws iam delete-role --role-name `my-iam-role`
```

For more information, see
[Deleting an IAM role (AWS CLI)](../../../IAM/latest/UserGuide/id_roles_manage_delete.md#roles-managingrole-deleting-cli "../../../IAM/latest/UserGuide/id_roles_manage_delete.md#roles-managingrole-deleting-cli")
in the _IAM User Guide_. 4. Delete the Amazon ECR repository including all the images stored in it. You can do so using the
following command.

```
aws ecr delete-repository \
      --repository-name `my-ecr-repository` \
      --force \
      --region `us-east-1`
```

Note that the `force` flag is required to delete a repository that
contains images. To delete your image first, you can do so using the following
command.

```
aws ecr batch-delete-image \
      --repository-name `my-ecr-repository` \
      --image-ids imageTag=latest \
      --region `us-east-1`
```

For more information, see [Delete an image](../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-delete-image "../../../AmazonECR/latest/userguide/getting-started-cli.md#cli-delete-image") in the Amazon Elastic Container Registry User Guide. 5. Delete the Amazon Keyspaces keyspace and table. Deleting the keyspace automatically deletes all tables in that keyspace. You can use one the following options to do so.

AWS CLI

```
aws keyspaces delete-keyspace --keyspace-name '`aws`'
```

To confirm that the keyspace was deleted, you can use the following command.

```
aws keyspaces list-keyspaces
```

To delete the table first, you can use the following command.

```
aws keyspaces delete-table --keyspace-name '`aws`' --table-name '`user`'
```

To confirm that your table was deleted, you can use the following command.

```
aws keyspaces list-tables --keyspace-name '`aws`'
```

For more information, see [delete keyspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-keyspace.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-keyspace.html") and [delete table](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-table.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/keyspaces/delete-table.html") in the _AWS CLI Command Reference_.

cqlsh

```
DROP KEYSPACE IF EXISTS "`aws`";
```

To verify that your keyspaces was deleted, you can use the following statement.

```
SELECT * FROM system_schema.keyspaces ;
```

Your keyspace should not be listed in the output of this
statement. Note that there can be a delay until the keyspaces is
deleted. For more information, see [DROP KEYSPACE](cql.ddl.md#cql.ddl.keyspace.drop "cql.ddl.md#cql.ddl.keyspace.drop").

To delete the table first, you can use the following command.

```
DROP TABLE "`aws.user`"
```

To confirm that your table was deleted, you can use the following command.

```
SELECT * FROM system_schema.tables WHERE keyspace_name = "`aws`";
```

Your table should not be listed in the output of this
statement. Note that there can be a delay until the table is
deleted. For more information, see [DROP TABLE](cql.ddl.md#cql.ddl.table.drop "cql.ddl.md#cql.ddl.table.drop").
