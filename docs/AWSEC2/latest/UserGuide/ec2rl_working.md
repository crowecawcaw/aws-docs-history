# Run EC2Rescue commands on an Amazon EC2 Linux instance

EC2Rescue is a command line tool. After you have installed EC2Rescue on your Linux
instance, you can get general help on how to use the tool by running `./ec2rl help`.
You can view the available modules by running `./ec2rl list`,
and you can get help on a specific module by running `./ec2rl help `module_name``.

The following are common tasks you can perform to get started using this tool.

###### Tasks

- [Run EC2Rescue modules](#ec2rl_running_module "#ec2rl_running_module")
- [Upload the EC2Rescue module results](#ec2rl_uploading_results "#ec2rl_uploading_results")
- [Create backups of an Amazon EC2 Linux instance](#ec2rl_creating_backups "#ec2rl_creating_backups")

## Run EC2Rescue modules

###### To run all EC2Rescue modules

Use the **./ec2rl run** command without specifying any additional parameters.
Some modules require root access. If you are not a root user, use **sudo** when you
run the command.

```
./ec2rl run
```

###### To run a specific EC2Rescue module

Use the **./ec2rl run** command and for `--only-modules`, specify the
name of the module to run. Some modules require _arguments_ to use them.

```
./ec2rl run --only-modules=`module_name` --`arguments`
```

For example, to run the **dig** module to query the `amazon.com`
domain, use the following command.

```
./ec2rl run --only-modules=dig --domain=amazon.com
```

###### To view the results of an EC2Rescue module

Run the module then view the log file in `cat /var/tmp/ec2rl/`logfile_location``.
For example, the log file for the **dig** module can be found in the following location:

```
cat /var/tmp/ec2rl/`timestamp`/mod_out/run/dig.log
```

## Upload the EC2Rescue module results

If Support has requested the results for a EC2Rescue module, you can upload the log file using
the EC2Rescue tool. You can upload the results either to a location provided by Support or
to an Amazon S3 bucket that you own.

###### To upload results to a location provided by Support

Use the **./ec2rl upload** command. For `--upload-directory`, specify the location
of the log file. For `--support-url`, specify the URL provided by Support.

```
./ec2rl upload --upload-directory=/var/tmp/ec2rl/`logfile_location` --support-url="`url_provided_by_aws_support`"
```

###### To upload results to an Amazon S3 bucket

Use the **./ec2rl upload** command. For `--upload-directory`, specify the location
of the log file. For `--presigned-url`, specify a presigned URL for the S3 bucket.
For more information about generating pre-signed URLs for Amazon S3, see [Uploading Objects Using Pre-Signed
URLs](../../../AmazonS3/latest/userguide/PresignedUrlUploadObject.md "../../../AmazonS3/latest/userguide/PresignedUrlUploadObject.md").

```
./ec2rl upload --upload-directory=/var/tmp/ec2rl/`logfile_location` --presigned-url="`presigned_s3_url`"
```

## Create backups of an Amazon EC2 Linux instance

You can use EC2Rescue to backup your Linux instance by creating an AMI or by creating
snapshots of it's attached volumes.

###### To create an AMI

Use the `./ec2rl run` command and for --`backup`, specify `ami`.

```
./ec2rl run --backup=ami
```

###### To create multi-volume snapshots of all attached volumes

Use the `./ec2rl run` command and for --`backup`, specify `allvolumes`.

```
./ec2rl run --backup=allvolumes
```

###### To create a snapshot of a specific attached volume

Use the `./ec2rl run` command and for --`backup`, specify the ID
of the volume to back up.

```
./ec2rl run --backup=`vol-01234567890abcdef`
```
