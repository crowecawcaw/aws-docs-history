

# Installing updates to your Neptune engine manually
<a name="engine-updates-manually"></a>

## Installing a major version engine upgrade
<a name="engine-major-updates-manually"></a>

Major engine releases must always be installed manually. To minimize downtime and provide for plenty of time for testing and validation, the best way to install a new major version is generally to use the [Neptune Blue-Green deployment solution](neptune-BG-deployments.md).

In some cases you can also use the CloudFormation template with which you created your DB cluster to install a major version upgrade (see [Using a CloudFormation template to update the engine version of your Neptune DB Cluster](cfn-engine-update.md)).

If you want to install a major version update immediately, you can use a CLI command like the following:

```
aws neptune modify-db-cluster \
  --db-cluster-identifier {{(identifier for your neptune cluster)}} \
  --engine neptune \
  --engine-version {{(the new engine version)}} \
  --apply-immediately
```

Be sure to specify the engine version to which you want to upgrade. If you don't, your engine may be upgraded to a version that is not the most recent one or the one you expect.

Instead of `--apply-immediately`, you can specify `--no-apply-immediately`.

If your cluster uses a custom cluster parameter group, be sure to specify using this paramater:

```
  --db-cluster-parameter-group-name {{(name of the custom DB cluster parameter group)}}
```

Similarly, if any instances in the cluster use a custom DB parameter group, be sure to specify it using this parameter:

```
  ---db-instance-parameter-group-name {{(name of the custom instance parameter group)}}
```

## Installing a minor version engine upgrade using the AWS Management Console
<a name="engine-minor-updates-using-console"></a>

**To perform a minor version upgrade using the Neptune console**

1. Sign in to the AWS Management Console, and open the Amazon Neptune console at [https://console.aws.amazon.com/neptune/home](https://console.aws.amazon.com/neptune/home).

1. In the navigation pane, choose **Databases**, and then choose the DB cluster that you want to modify.

1. Choose **Modify**.

1. Under **Instance specifications**, choose the new version to which you want to upgrade.

1. Choose **Next**.

1. If you want to apply the changes immediately, choose **Apply immediately**.

1. Choose **Submit** to update your DB cluster.

## Installing a minor version engine upgrade using the AWS CLI
<a name="engine-updates-using-cli"></a>

You can use a command like the following to perform a minor version upgrade without waiting for the next maintenance window:

```
aws neptune modify-db-cluster \
  --db-cluster-identifier {{(your-neptune-cluster)}} \
  --engine-version {{(new-engine-version)}} \
  --apply-immediately
```

If you are manually upgrading using the AWS CLI, be sure to include the engine version to which you want to upgrade. If you do not, your engine may be upgraded to a version that is not the most recent one or the one you expect.