# Import files with distributed

cache with Amazon EMR

DistributedCache is a Hadoop feature that can boost efficiency when
a map or a reduce task needs access to common data. If your cluster depends on
existing applications or binaries that are not installed when the cluster is
created, you can use DistributedCache to import these files. This
feature lets a cluster node read the imported files from its local file system,
instead of retrieving the files from other cluster nodes.

For more information, go to [http://hadoop.apache.org/docs/stable/api/org/apache/hadoop/filecache/DistributedCache.html](http://hadoop.apache.org/docs/stable/api/org/apache/hadoop/filecache/DistributedCache.html "http://hadoop.apache.org/docs/stable/api/org/apache/hadoop/filecache/DistributedCache.html").

You invoke DistributedCache when you create the cluster. The files
are cached just before starting the Hadoop job and the files remain cached for the
duration of the job. You can cache files stored on any Hadoop-compatible file
system, for example HDFS or Amazon S3. The default size of the file cache is 10GB. To
change the size of the cache, reconfigure the Hadoop parameter,
`local.cache.size` using the bootstrap action. For more information,
see [Create bootstrap actions to install additional
software with an Amazon EMR cluster](emr-plan-bootstrap.md "emr-plan-bootstrap.md").

###### Topics

- [Supported file types](#emr-dev-supported-file-types "#emr-dev-supported-file-types")
- [Location of cached files](#locationofcache "#locationofcache")
- [Access cached files from streaming
  applications](#cachemapper "#cachemapper")
- [Access cached files from streaming
  applications](#cacheinconsole "#cacheinconsole")

## Supported file types

DistributedCache allows both single files and archives.
Individual files are cached as read only. Executables and binary files have
execution permissions set.

Archives are one or more files packaged using a utility, such as
`gzip`. DistributedCache passes the compressed
files to each core node and decompresses the archive as part of caching.
DistributedCache supports the following compression
formats:

- zip
- tgz
- tar.gz
- tar
- jar

## Location of cached files

DistributedCache copies files to core nodes only. If there are
no core nodes in the cluster, DistributedCache copies the files
to the primary node.

DistributedCache associates the cache files to the current
working directory of the mapper and reducer using symlinks. A symlink is an
alias to a file location, not the actual file location. The value of the
parameter, `yarn.nodemanager.local-dirs` in
`yarn-site.xml`, specifies the location of
temporary files. Amazon EMR sets this parameter to `/mnt/mapred`,
or some variation based on instance type and EMR version. For example, a setting
may have `/mnt/mapred` and `/mnt1/mapred`
because the instance type has two ephemeral volumes. Cache files are located in
a subdirectory of the temporary file location at
`/mnt/mapred/taskTracker/archive`.

If you cache a single file, DistributedCache puts the file in
the `archive` directory. If you cache an archive,
DistributedCache decompresses the file, creates a
subdirectory in `/archive` with the same name as the archive file
name. The individual files are located in the new subdirectory.

You can use DistributedCache only when using Streaming.

## Access cached files from streaming

applications

To access the cached files from your mapper or reducer applications, make sure
that you have added the current working directory (./) into your application
path and referenced the cached files as though they are present in the current
working directory.

## Access cached files from streaming

applications

You can use the AWS Management Console and the AWS CLI to create clusters that use
Distributed Cache.

Console

###### To specify distributed cache files with the new

console

1. Sign in to the AWS Management Console, and open the Amazon EMR console at
   [https://console.aws.amazon.com/emr](https://console.aws.amazon.com/emr "https://console.aws.amazon.com/emr").
2. Under **EMR on EC2** in the left
   navigation pane, choose **Clusters**, and
   then choose **Create cluster**.
3. Under **Steps**, choose **Add
   step**. This opens the **Add
   step** dialog. In the
   **Arguments** field, include the files
   and archives to save to the cache. The size of the file (or
   total size of the files in an archive file) must be less
   than the allocated cache size.

If you want to add an individual file to the distributed
cache, specify `-cacheFile`, followed by the name
and location of the file, the pound (#) sign, and the name
you want to give the file when it's placed in the local
cache. The following example demonstrates how to add an
individual file to the distributed cache.

```
-cacheFile \
s3://`amzn-s3-demo-bucket`/`file-name`#`cache-file-name`
```

If you want to add an archive file to the distributed
cache, enter `-cacheArchive` followed by the
location of the files in Amazon S3, the pound (#) sign, and then
the name you want to give the collection of files in the
local cache. The following example demonstrates how to add
an archive file to the distributed cache.

```
-cacheArchive \
s3://`amzn-s3-demo-bucket`/`archive-name`#`cache-archive-name`
```

Enter appropriate values in the other dialog fields.
Options differ depending on the step type. To add your step
and exit the dialog, choose **Add
step**. 4. Choose any other options that apply to your cluster. 5. To launch your cluster, choose **Create
cluster**.

CLI

###### To specify distributed cache files with the AWS CLI

- To submit a Streaming step when a cluster is created, type
  the `create-cluster` command with the
  `--steps` parameter. To specify distributed
  cache files using the AWS CLI, specify the appropriate
  arguments when submitting a Streaming step.

If you want to add an individual file to the distributed
cache, specify `-cacheFile`, followed by the name
and location of the file, the pound (#) sign, and the name
you want to give the file when it's placed in the local
cache.

If you want to add an archive file to the distributed
cache, enter `-cacheArchive` followed by the
location of the files in Amazon S3, the pound (#) sign, and then
the name you want to give the collection of files in the
local cache. The following example demonstrates how to add
an archive file to the distributed cache.

For more information on using Amazon EMR commands in the AWS CLI,
see [https://docs.aws.amazon.com/cli/latest/reference/emr](../../../cli/latest/reference/emr.md "../../../cli/latest/reference/emr.md").

###### Example 1

Type the following command to launch a cluster and submit a
Streaming step that uses `-cacheFile` to add one
file, `sample_dataset_cached.dat`, to the
cache.

```
aws emr create-cluster --name "Test cluster" --release-label emr-4.0.0 --applications Name=Hive Name=Pig --use-default-roles --ec2-attributes KeyName=myKey --instance-type m5.xlarge --instance-count 3 --steps Type=STREAMING,Name="Streaming program",ActionOnFailure=CONTINUE,Args=["--files","s3://my_bucket/my_mapper.py s3://my_bucket/my_reducer.py","-mapper","my_mapper.py","-reducer","my_reducer.py,"-input","s3://my_bucket/my_input","-output","s3://my_bucket/my_output", "-cacheFile","s3://my_bucket/sample_dataset.dat#sample_dataset_cached.dat"]
```

When you specify the instance count without using the
`--instance-groups` parameter, a single primary
node is launched, and the remaining instances are launched as
core nodes. All nodes will use the instance type specified in
the command.

If you have not previously created the default EMR service
role and EC2 instance profile, type `aws emr
 create-default-roles` to create them before typing the
`create-cluster` subcommand.

###### Example 2

The following command shows the creation of a streaming
cluster and uses `-cacheArchive` to add an archive of
files to the cache.

```
aws emr create-cluster --name "Test cluster" --release-label emr-4.0.0 --applications Name=Hive Name=Pig --use-default-roles --ec2-attributes KeyName=myKey --instance-type m5.xlarge --instance-count 3 --steps Type=STREAMING,Name="Streaming program",ActionOnFailure=CONTINUE,Args=["--files","s3://my_bucket/my_mapper.py s3://my_bucket/my_reducer.py","-mapper","my_mapper.py","-reducer","my_reducer.py,"-input","s3://my_bucket/my_input","-output","s3://my_bucket/my_output", "-cacheArchive","s3://my_bucket/sample_dataset.tgz#sample_dataset_cached"]
```

When you specify the instance count without using the
`--instance-groups` parameter, a single primary
node is launched, and the remaining instances are launched as
core nodes. All nodes will use the instance type specified in
the command.

If you have not previously created the default EMR service
role and EC2 instance profile, type `aws emr
 create-default-roles` to create them before typing the
`create-cluster` subcommand.
