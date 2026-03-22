# Tutorial: Use tags to specify which Aurora DB clusters to stop

Suppose that you're creating a number of Aurora DB clusters in a development or test environment.
You need to keep all of these clusters for several days. Some of the clusters run tests overnight.
Other clusters can be stopped overnight and started again the next day. The following example shows
how to assign a tag to those clusters that are suitable to stop overnight. Then the example shows how
a script can detect which clusters have that tag and then stop those clusters. In this example, the value
portion of the key-value pair doesn't matter. The presence of the `stoppable` tag signifies
that the cluster has this user-defined property.

###### To specify which Aurora DB clusters to stop

1. Determine the ARN of a cluster that you want to designate as stoppable.

The commands and APIs for tagging work with ARNs. That way, they can work seamlessly across AWS Regions, AWS accounts, and
different types of resources that might have identical short names. You can specify the ARN instead of
the cluster ID in CLI commands that operate on clusters. Substitute the name of your own cluster for
`dev-test-cluster`. In subsequent commands that use ARN parameters, substitute
the ARN of your own cluster. The ARN includes your own AWS account ID and the name of the AWS Region
where your cluster is located.

```
`$` aws rds describe-db-clusters --db-cluster-identifier `dev-test-cluster` \
  --query "*[].{DBClusterArn:DBClusterArn}" --output text
`arn:aws:rds:us-east-1:123456789:cluster:dev-test-cluster`

```

2. Add the tag `stoppable` to this cluster.

You choose the name for this tag. This approach means that you can avoid devising a
naming convention that encodes all relevant information in names. In such a convention,
you might encode information in the DB instance name or names of other resources. Because this example
treats the tag as an attribute that is either present or absent, it omits the `Value=`
part of the `--tags` parameter.

```
`$` aws rds add-tags-to-resource \
  --resource-name `arn:aws:rds:us-east-1:123456789:cluster:dev-test-cluster` \
  --tags Key=stoppable

```

3. Confirm that the tag is present in the cluster.

These commands retrieve the tag information for the cluster in JSON format and in plain tab-separated text.

```
`$` aws rds list-tags-for-resource \
  --resource-name `arn:aws:rds:us-east-1:123456789:cluster:dev-test-cluster`
`{
 "TagList": [
 {
 "Key": "stoppable",
 "Value": ""

 }
 ]
}`
`$` aws rds list-tags-for-resource \
  --resource-name `arn:aws:rds:us-east-1:123456789:cluster:dev-test-cluster` --output text
`TAGLIST stoppable`

```

4. To stop all the clusters that are designated as `stoppable`, prepare a list of all your
   clusters. Loop through the list and check if each cluster is tagged with the relevant attribute.

This Linux example uses shell scripting to save the list of cluster ARNs to a temporary file and then perform
CLI commands for each cluster.

```
`$` aws rds describe-db-clusters --query "*[].[DBClusterArn]" --output text >/tmp/cluster_arns.lst
`$` for arn in $(cat /tmp/cluster_arns.lst)
do
  match="$(aws rds list-tags-for-resource --resource-name $arn --output text | grep 'TAGLIST\tstoppable')"
  if [[ ! -z "$match" ]]
  then
      echo "Cluster $arn is tagged as stoppable. Stopping it now."
# Note that you can specify the full ARN value as the parameter instead of the short ID 'dev-test-cluster'.
      aws rds stop-db-cluster --db-cluster-identifier $arn
  fi
done

`Cluster arn:aws:rds:us-east-1:123456789:cluster:dev-test-cluster is tagged as stoppable. Stopping it now.
{
 "DBCluster": {
 "AllocatedStorage": 1,
 "AvailabilityZones": [
 "us-east-1e",
 "us-east-1c",
 "us-east-1d"
 ],
 "BackupRetentionPeriod": 1,
 "DBClusterIdentifier": "dev-test-cluster",
 ...`

```

You can run a script like this at the end of each day to make sure that nonessential clusters
are stopped. You might also schedule a job using a utility such as `cron` to
perform such a check each night. For example, you might do this in case some clusters were
left running by mistake. Here, you might fine-tune the command that prepares the list of
clusters to check.

The following command produces a list of your clusters, but only the ones in
`available` state. The script can ignore clusters that are already stopped,
because they will have different status values such as `stopped` or
`stopping`.

```
`$` aws rds describe-db-clusters \
  --query '*[].{DBClusterArn:DBClusterArn,Status:Status}|[?Status == `available`]|[].{DBClusterArn:DBClusterArn}' \
  --output text
`arn:aws:rds:us-east-1:123456789:cluster:cluster-2447
arn:aws:rds:us-east-1:123456789:cluster:cluster-3395
arn:aws:rds:us-east-1:123456789:cluster:dev-test-cluster
arn:aws:rds:us-east-1:123456789:cluster:pg2-cluster`

```

###### Tip

You can use assigning tags and finding clusters that have those tags to reduce costs in
other ways. For example, take the scenario with Aurora DB clusters used for development and
testing. Here, you might designate some clusters to be deleted at the end of each day, or to
have only their reader DB instances deleted. Or you might designate some to have their DB
instances changed to small DB instance classes during times of expected low usage.
