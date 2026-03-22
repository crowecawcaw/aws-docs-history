# Tutorial: Specify which DB instances to stop by using tags

This tutorial assumes that you have several DB instances in a development or test environment.
You need to keep these DB instances for several days. Some DB instances run tests overnight, whereas
others can be stopped overnight and started again the next day.

The following tutorial shows how to assign a tag to DB instances that are suitable to stop
overnight. The tutorial shows how a script can detect which DB instances have the tag and then stop
the tagged DB instances. In this example, the value portion of the key-value pair doesn't
matter. The presence of the `stoppable` tag signifies that the DB instance has this
user-defined property.

In the following tutorial, the commands and APIs for tagging work with ARNs, which allow
RDS to work seamlessly across AWS Regions, AWS accounts, and different types of resources
that might have identical short names. You can specify the ARN instead of the DB instance ID in CLI
commands that operate on DB instances.

###### To specify which DB instances to stop

1. Determine the ARN of a DB instance that you want to designate as stoppable.

In the following example, substitute the name of your own DB instances for
`dev-test-db-instance`. In subsequent commands that use ARN
parameters, substitute the ARN of your own DB instance. The ARN includes your own AWS account
ID and the name of the AWS Region where your DB instance is located.

```
`$` aws rds describe-db-instances --db-instance-identifier `dev-test-db-instance` \
  --query "*[].{DBInstance:DBInstanceArn}" --output text
`arn:aws:rds:us-east-1:123456789102:db:dev-test-db-instance`
```

2. Add the tag `stoppable` to this DB instance.

You choose the name for this tag. Because this example treats the tag as an
attribute that is either present or absent, it omits the `Value=` part of the
`--tags` parameter. This approach means that you can avoid devising a naming
convention that encodes all relevant information in names. In such a convention, you might
encode information in the DB instance name or names of other resources.

```
`$` aws rds add-tags-to-resource \
  --resource-name `arn:aws:rds:us-east-1:123456789102:db:dev-test-db-instance` \
  --tags Key=stoppable
```

3. Confirm that the tag is present in the DB instance.

The following commands retrieve the tag information for the DB instance in JSON format and
in plain tab-separated text.

```
`$` aws rds list-tags-for-resource \
  --resource-name `arn:aws:rds:us-east-1:123456789102:db:dev-test-db-instance`
`{
 "TagList": [
 {
 "Key": "stoppable",
 "Value": ""

 }
 ]
}`
aws rds list-tags-for-resource \
  --resource-name `arn:aws:rds:us-east-1:123456789102:db:dev-test-db-instance` --output text
`TAGLIST stoppable`
```

4. Stop all the DB instances that are designated as `stoppable`.

The following example create a text file that lists all your DB instances. The shell command
loops through the list and checks if each DB instance is tagged with the relevant attribute and
performs runs the command `aws rds stop-db-instance` for each DB instance.

```
`$` aws rds describe-db-instances --query "*[].[DBInstanceArn]" --output text >/tmp/db_instance_arns.lst
`$` for arn in $(cat /tmp/db_instance_arns.lst)
do
  match="$(aws rds list-tags-for-resource --resource-name $arn --output text | grep stoppable)"
  if [[ ! -z "$match" ]]
  then
      echo "DB instance $arn is tagged as stoppable. Stopping it now."
# Note that you need to get the DB instance identifier from the ARN.
      dbid=$(echo $arn | sed -e 's/.*://')
      aws rds stop-db-instance --db-instance-identifier $dbid
  fi
done

`DB instance arn:arn:aws:rds:us-east-1:123456789102:db:dev-test-db-instance is tagged as stoppable. Stopping it now.
{
 "DBInstance": {
 "DBInstanceIdentifier": "dev-test-db-instance",
 "DBInstanceClass": "db.t3.medium",
 ...`

```

You can run a script like the preceding one at the end of every day to make sure that
nonessential DB instances are stopped. You might also schedule a job using a utility such as
`cron` to perform such a check each night. For example, you might do this in case
some DB instances were left running by mistake. Here, you might fine-tune the command that prepares
the list of DB instances to check.

The following command produces a list of your DB instances, but only the ones in
`available` state. The script can ignore DB instances that are already stopped,
because they will have different status values such as `stopped` or
`stopping`.

```
`$` aws rds describe-db-instances \
  --query '*[].{DBInstanceArn:DBInstanceArn,DBInstanceStatus:DBInstanceStatus}|[?DBInstanceStatus == `available`]|[].{DBInstanceArn:DBInstanceArn}' \
  --output text
`arn:aws:rds:us-east-1:123456789102:db:db-instance-2447
arn:aws:rds:us-east-1:123456789102:db:db-instance-3395
arn:aws:rds:us-east-1:123456789102:db:dev-test-db-instance
arn:aws:rds:us-east-1:123456789102:db:pg2-db-instance`

```

###### Tip

You can use assigning tags and finding DB instances with those tags to reduce costs in
other ways. For example, take this scenario with DB instances used for development and
testing. In this case, you might designate some DB instances to be deleted at the end of
each day. Or you might designate them to have their DB instances changed to small DB
instance classes during times of expected low usage.
