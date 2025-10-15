# Setting up the tools for the
 walkthroughs

The introductory examples (see [Walkthroughs that use policies to
 manage access to your Amazon S3 resources](example-walkthroughs-managing-access.md "example-walkthroughs-managing-access.md")) use the AWS Management Console to create
 resources and grant permissions. To test permissions, the examples use the command line
 tools, AWS Command Line Interface (AWS CLI) and AWS Tools for Windows PowerShell, so you don't need to write any code. To test
 permissions, you must set up one of these tools. 

###### To set up the AWS CLI

1. Download and configure the AWS CLI. For instructions, see the following topics
 in the *AWS Command Line Interface User Guide*: 



[Install or update to the
 latest version of the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html")




[Get started with the
 AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/installing.html "https://docs.aws.amazon.com/cli/latest/userguide/installing.html")
2. Set the default profile. 


You store user credentials in the AWS CLI config file. Create a default profile in the
 config file using your AWS account credentials. For instructions on finding
 and editing your AWS CLI config file, see [Configuration and credential file
 settings](https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html "https://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html").



```
[default]
aws_access_key_id = `access key ID`
aws_secret_access_key = `secret access key`
region = us-west-2
```
3. Verify the setup by entering the following command at the command prompt. Both these
 commands don't provide credentials explicitly, so the credentials of the default
 profile are used.




	* Try the `help` command.
	
	
	
	```
	aws help
	```
	* To get a list of buckets on the configured account, use the `aws s3 ls`
	 command.
	
	
	
	```
	aws s3 ls
	```
As you go through the walkthroughs, you will create users, and you will save user
 credentials in the config files by creating profiles, as the following example shows.
 These profiles have the names of `AccountAadmin` and
 `AccountBadmin`.


```
[profile AccountAadmin]
aws_access_key_id = `User AccountAadmin access key ID`
aws_secret_access_key = `User AccountAadmin secret access key`
region = us-west-2

[profile AccountBadmin]
aws_access_key_id = `Account B access key ID`
aws_secret_access_key = `Account B secret access key`
region = us-east-1
```
To run a command using these user credentials, you add the `--profile` parameter
 specifying the profile name. The following AWS CLI command retrieves a listing of objects
 in ``examplebucket`` and specifies the
 `AccountBadmin` profile. 


```
aws s3 ls s3://`examplebucket` --profile AccountBadmin
```
Alternatively, you can configure one set of user credentials as the default profile by
 changing the `AWS_DEFAULT_PROFILE` environment variable from the command
 prompt. After you've done this, whenever you perform AWS CLI commands without the
 `--profile` parameter, the AWS CLI uses the profile you set in the
 environment variable as the default profile.


```
`$` export AWS_DEFAULT_PROFILE=AccountAadmin
```
###### To set up AWS Tools for Windows PowerShell

1. Download and configure the AWS Tools for Windows PowerShell. For instructions, go to [Installing the AWS Tools for Windows PowerShell](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html#pstools-installing-download "https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html#pstools-installing-download") in the
 *AWS Tools for PowerShell User Guide*. 


###### Note

To load the AWS Tools for Windows PowerShell module, you must enable PowerShell
 script execution. For more information, see [Enable Script Execution](https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html#enable-script-execution "https://docs.aws.amazon.com/powershell/latest/userguide/pstools-getting-set-up.html#enable-script-execution") in the
 *AWS Tools for PowerShell User Guide*.
2. For these walkthroughs, you specify AWS credentials per session using the
 `Set-AWSCredentials` command. The command saves the credentials
 to a persistent store (`-StoreAs` parameter).



```
Set-AWSCredentials -AccessKey `AccessKeyID` -SecretKey `SecretAccessKey` -storeas `string`
```
3. Verify the setup.




	* To retrieve a list of available commands that you can use for Amazon S3 operations, run the
	 `Get-Command` command. 
	
	
	
	```
	Get-Command -module awspowershell -noun s3* -StoredCredentials `string`
	```
	* To retrieve a list of objects in a bucket, run the `Get-S3Object`
	 command.
	
	
	
	```
	Get-S3Object -BucketName `bucketname` -StoredCredentials `string`
	```
For a list of commands, see [AWS Tools for PowerShell
 Cmdlet
 Reference](https://docs.aws.amazon.com/powershell/latest/reference/Index.html "https://docs.aws.amazon.com/powershell/latest/reference/Index.html").
 

Now you're ready to try the walkthroughs.
 Follow
 the links provided at the beginning of each section.
