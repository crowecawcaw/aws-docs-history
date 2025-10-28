# Deleting a blue/green deployment in Amazon Aurora

You can delete a blue/green deployment before or after you switch it over.

When you delete a blue/green deployment before switching it over, Amazon RDS optionally deletes
the DB
cluster in the green environment:

- If you choose to delete the DB
  cluster in the green environment
  (`--delete-target`), it must have deletion protection turned off.
- If you don't delete the DB
  cluster in the green environment
  (`--no-delete-target`), the cluster is retained, but it's no longer
  part of a blue/green deployment. For Aurora MySQL, replication continues
  between the environments. For Aurora PostgreSQL, the green environment is promoted to a
  standalone environment, so replication stops.
  The option to delete the green databases isn't available in the console after [switchover](blue-green-deployments-switching.md "blue-green-deployments-switching.md"). When you delete blue/green
  deployments using the AWS CLI, you can't specify the `--delete-target` option if the
  deployment [status](../APIReference/API_BlueGreenDeployment.md "../APIReference/API_BlueGreenDeployment.md") is
  `SWITCHOVER_COMPLETED`.

###### Important

After you delete a blue/green deployment, RDS removes read-only
protections from the previous production DB cluster. If the `read_only` parameter is
disabled for the DB cluster, it starts to allow write operations again.

You can delete a blue/green deployment using the AWS Management Console, the AWS CLI, or the RDS API.

###### To delete a blue/green deployment

1. Sign in to the AWS Management Console and open the Amazon RDS console at
   [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/ "https://console.aws.amazon.com/rds/").
2. In the navigation pane, choose **Databases**, and then choose the blue/green deployment
   that you want to delete.
3. For **Actions**, choose **Delete**.

The **Delete blue/green deployment?** window appears.

![Delete blue/green deployment](images/blue-green-deployment-delete-aurora.png)

To delete the green databases, select **Delete the green databases in this
blue/green deployment**. 4. Enter `delete me` in the box. 5. Choose **Delete**.
To delete a blue/green deployment by using the AWS CLI, use the [delete-blue-green-deployment](../../../cli/latest/reference/rds/delete-blue-green-deployment.md "../../../cli/latest/reference/rds/delete-blue-green-deployment.md") command with the following options:

- `--blue-green-deployment-identifier` – The resource ID of the
  blue/green deployment to be deleted.
- `--delete-target` – Specifies that the DB
  cluster in the green environment
  is deleted. You can't specify this option if the
  blue/green deployment has a status of `SWITCHOVER_COMPLETED`.
- `--no-delete-target` – Specifies that the DB
  cluster in the green environment
  is retained.

###### Example Delete a blue/green deployment and the DB cluster in the green environment

For Linux, macOS, or Unix:

```
aws rds delete-blue-green-deployment \
    --blue-green-deployment-identifier `bgd-1234567890abcdef` \
    --delete-target
```

For Windows:

```
aws rds delete-blue-green-deployment ^
    --blue-green-deployment-identifier `bgd-1234567890abcdef` ^
    --delete-target
```

###### Example Delete a blue/green deployment but retain the DB cluster in the green environment

For Linux, macOS, or Unix:

```
aws rds delete-blue-green-deployment \
    --blue-green-deployment-identifier `bgd-1234567890abcdef` \
    --no-delete-target
```

For Windows:

```
aws rds delete-blue-green-deployment ^
    --blue-green-deployment-identifier `bgd-1234567890abcdef` ^
    --no-delete-target
```

To delete a blue/green deployment by using the Amazon RDS API, use the [`DeleteBlueGreenDeployment`](../APIReference/API_DeleteBlueGreenDeployment.md "../APIReference/API_DeleteBlueGreenDeployment.md") operation with the following parameters:

- `BlueGreenDeploymentIdentifier` – The resource ID of the
  blue/green deployment to be deleted.
- `DeleteTarget` – Specify `TRUE` to delete the DB

cluster in the green environment or
`FALSE` to retain it. Cannot be `TRUE` if the blue/green
deployment has a status of `SWITCHOVER_COMPLETED`.
