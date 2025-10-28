# Prerequisites

If you plan to access Quick Sight through its API, make sure you're familiar
with the following:

- JSON
- Web services
- HTTP requests
- One or more programming languages, such as JavaScript, Java, Python, or C#
  We recommend visiting the AWS [Getting Started
  Resource Center](https://aws.amazon.com/getting-started/tools-sdks/ "https://aws.amazon.com/getting-started/tools-sdks/") for a tour of what AWS SDKs and toolkits have to offer.

Although you can use a terminal and your favorite text editor, you might benefit from the
more visual UI experience you get in an integrated development environment (IDE). We
provide a list of IDEs in the AWS Getting Started Resource
Center in the [IDE and IDE Toolkits](https://aws.amazon.com/getting-started/tools-sdks/#IDE_and_IDE_Toolkits "https://aws.amazon.com/getting-started/tools-sdks/#IDE_and_IDE_Toolkits") section. This site provides AWS toolkits that you
can download for your preferred IDE. Some IDEs also offer tutorials to help you
learn more about programming languages.

Before you can call the Quick Sight API operations, make sure that you have the
`quicksight:`operation-name``permission in
 an IAM policy attached to your IAM identity. For example, to call
`list-users`, you need the permission `quicksight:ListUsers`.
The same pattern applies to all operations.

If you’re not sure what the necessary permission is, you can attempt to make a call. The
client then tells you what the missing permission is. You can use asterisk
(`*`) in the Resource field of your permission policy instead of
specifying explicit resources. However, we recommend that you restrict each permission
as much as possible. You can restrict user access by specifying or excluding resources
in the policy, using their Quick Sight Amazon Resource Name (ARN) identifier.

For more information, see the following:

- [IAM Policy Examples](../user/iam-policy-examples.md "../user/iam-policy-examples.md")
  in the _Amazon Quick Sight User Guide_
- [Actions, Resources, and Condition Keys](../../../IAM/latest/UserGuide/list_amazoninspector.md "../../../IAM/latest/UserGuide/list_amazoninspector.md")
  in the _IAM User Guide_
- [IAM JSON Policy Elements](../../../IAM/latest/UserGuide/reference_policies_elements.md "../../../IAM/latest/UserGuide/reference_policies_elements.md") in the _IAM User Guide_
  To retrieve the ARN of a user or a group, use the `Describe` operation on the
  relevant resource. You can also add conditions in IAM to further restrict access to an
  API in some scenarios. For instance, when adding `User1` to
  `Group1`, the main resource is `Group1`, so you can allow or
  deny access to certain groups. However, you can also add a condition by using the Quick Sight IAM
  key `quicksight:UserName` to allow or prevent certain users from being
  added to that group.

Following is an example policy. It means that the caller with this policy attached can invoke
the `CreateGroupMembership` operation for any group, if the user name they
are adding to the group isn't `user1`.

```
{
	"Effect": "Allow",
	"Action": "quicksight:CreateGroupMembership",
	"Resource": "arn:aws:quicksight:us-east-1:`aws-account-id`:group/default/*",
	"Condition": {
		"StringNotEquals": {
			"quicksight:UserName": "user1"
		}
	}
}
```

AWS CLI
The following procedure explains how to interact with Quick Sight API operations through the
AWS Command Line Interface (AWS CLI). The following instructions have been tested in Bash but should be identical or
similar in other command-line environments.

###### To use Quick Sight API operations through the AWS CLI

1. Install AWS SDK in your environment. For instructions, see [AWS Command line
   Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/").
2. Set up your AWS CLI identity and AWS Region using the following command and follow-up
   instructions. Use the credentials for an IAM identity or role that has the
   proper permissions.

```
aws configure
```

3. Look at Quick Sight SDK help by running the following command.

```
aws quicksight help
```

4. To get detailed instructions on how to use an API, enter its name followed by
   `help`, as follows.

```
aws quicksight list-users help
```

5. Call an Quick Sight API operation. The following example returns a list of Quick Sight users in your
   account.

```
aws quicksight list-users \
--aws-account-id `aws-account-id` \
--namespace default \
--region `us-east-1`
```

Java SDK
Use the following procedure to set up a Java app that interacts with Quick Sight.

###### To set up a Java app that works with Quick Sight

1. Create a Java project in your IDE.
2. Import the Quick Sight SDK into your new project, for example:
   `AWSQuickSightJavaClient-1.11.x.jar`
3. After your IDE indexes the Quick Sight SDK, add an import line as follows.

```
import com.amazonaws.services.quicksight.AmazonQuickSight;
```

If your IDE doesn't recognize line this as valid, verify that you imported the
SDK. 4. Download and import external dependencies for the Quick Sight SDK.

Like other AWS SDKs, Quick Sight SDK requires external dependencies to perform many of its
functions. Make sure to download and import those into the same
project. The following dependencies are required:

    * `aws-java-sdk-1.11.402.jar` (AWS Java SDK and credentials setup) –
     To download, see [Set up the AWS SDK for Java](../../../sdk-for-java/v1/developer-guide/setup-install.md "../../../sdk-for-java/v1/developer-guide/setup-install.md") in the SDK for Java documentation.
    * `commons-logging-1.2.jar` – To download, see [Download Apache Commons Logging](https://commons.apache.org/proper/commons-logging/download_logging.cgi "https://commons.apache.org/proper/commons-logging/download_logging.cgi") on the Apache
     Commons website.
    * `jackson-annotations-2.9.6.jar`, `jackson-core-2.9.6.jar`, and
     `jackson-databind-2.9.6.jar` – To
     download, see [the Maven repository](https://repo1.maven.org/maven2/com/fasterxml/jackson/core/ "https://repo1.maven.org/maven2/com/fasterxml/jackson/core/").
    * `httpclient-4.5.6.jar`, `httpcore-4.4.10.jar` – To
     download, see [the Apache
     site](https://hc.apache.org/downloads.cgi "https://hc.apache.org/downloads.cgi").
    * `joda-time-2.1.jar` – To download, see [the MVNrepository Joda Time site.](https://mvnrepository.com/artifact/joda-time/joda-time/2.1 "https://mvnrepository.com/artifact/joda-time/joda-time/2.1")

5. Create an Quick Sight client.

You can use a default public endpoint that the client can
communicate with, or you can reference the endpoint explicitly.
There are multiple ways to provide your AWS credentials. In the
following example, we provide a direct, simple approach.

The following client method is used to make all the API calls that
follow.

```
private static AmazonQuickSight getClient() {
	final AWSCredentialsProvider credsProvider = new AWSCredentialsProvider() {
	@Override
	public AWSCredentials getCredentials() {
	// provide actual IAM access key and secret key here
	return new BasicAWSCredentials("access-key", "secret-key");
	}

	@Override
	public void refresh() {}
	};

	return AmazonQuickSightClientBuilder
	.standard()
	.withRegion(Regions.US_EAST_1.getName())
	.withCredentials(credsProvider)
	.build();
	}
```

6. Use the client that you just created to list all the users in our Quick Sight account.

Provide the AWS account ID that you used to subscribe to Quick Sight.
This ID must match the AWS account ID of the caller's identity.
Cross-account calls aren't supported at this time. Also, make sure
that the required parameter `namespace` is set to
`default`.

```
getClient().listUsers(new ListUsersRequest()
	.withAwsAccountId("`relevant_AWS_account_ID`")
	.withNamespace("default"))
	.getUserList().forEach(user -> {
		System.out.println(user.getArn());
	});
```

7. See a list of all possible API operations and the request objects they use by choosing
   the CTRL key and clicking
   the client object
   in your IDE view of the Quick Sight interface. Or find this list in
   the `com.amazonaws.services.quicksight` package in the
   Quick Sight JavaClient .jar file.

JavaScript (Node.js) SDK
Use the following procedure to interact with Quick Sight using Node.js.

###### To work with Quick Sight using Node.js

1.  Set up your node environment using the following commands:

        * `npm install aws-sdk`
        * `npm install aws4`
        * `npm install request`
        * `npm install url`

    For information on configuring the Node.js with AWS SDK and
    setting your credentials, see the [AWS SDK for JavaScript Developer Guide for SDK v2](../../../sdk-for-javascript/v2/developer-guide/welcome.md "../../../sdk-for-javascript/v2/developer-guide/welcome.md").

2.  Use the following code example to test your setup. HTTPS is required. The example
    displays a full listing of Quick Sight operations along with their URL
    request parameters, followed by a list of Quick Sight users in your
    account.

```
const AWS = require('aws-sdk');
const https = require('https');

var quicksight = new AWS.Service({
	apiConfig: require('./quicksight-2018-04-01.min.json'),
	region: 'us-east-1',
});

console.log(quicksight.config.apiConfig.operations);

quicksight.listUsers({
	// Enter your actual AWS account ID
	'AwsAccountId': '`relevant_AWS_account_ID`',
	'Namespace': 'default',
}, function(err, data) {
	console.log('---');
	console.log('Errors: ');
	console.log(err);
	console.log('---');
	console.log('Response: ');
	console.log(data);
});
```

Python3 SDK
Use the following procedure to create a custom-built `botocore` package to
interact with Quick Sight.

###### To create a custom botocore package to work with Quick Sight

1. Create a credentials file in the AWS directory for your environment. In a Linux- or
   macOS-based environment, that file is called
   `~/.aws/credentials` and looks like the
   following.

```
[default]
aws_access_key_id = `Your_IAM_access_key`
aws_secret_access_key = `Your_IAM_secret_key`
```

2. Unzip the folder `botocore-1.12.10`. Change directory into
   `botocore-1.12.10` and enter the Python3 interpreter
   environment.

Each response comes back as a dictionary object. They each have a
`ResponseMetadata` entry that contains request IDs
and response status. Other entries are based on what type of
operation you run. 3. As a test, use the following example code, a sample app that first creates, deletes, and
lists groups. Then it lists users in a Quick Sight account.

```
import botocore.session
default_namespace = 'default'
account_id = '`relevant_AWS_Account`'

session = botocore.session.get_session()
client = session.create_client("quicksight", region_name='us-east-1')

print('Creating three groups: ')
client.create_group(AwsAccountId = account_id, Namespace=default_namespace, GroupName='MyGroup1')
client.create_group(AwsAccountId = account_id, Namespace=default_namespace, GroupName='MyGroup2')
client.create_group(AwsAccountId = account_id, Namespace=default_namespace, GroupName='MyGroup3')

print('Retrieving the groups and listing them: ')
response = client.list_groups(AwsAccountId = account_id, Namespace=default_namespace)
for group in response['GroupList']:
	print(group)

print('Deleting our groups: ')
client.delete_group(AwsAccountId = account_id, Namespace=default_namespace, GroupName='MyGroup1')
client.delete_group(AwsAccountId = account_id, Namespace=default_namespace, GroupName='MyGroup2')
client.delete_group(AwsAccountId = account_id, Namespace=default_namespace, GroupName='MyGroup3')

response = client.list_users(AwsAccountId = account_id, Namespace=default_namespace)
for user in response['UserList']:
	print(user)
```

.NET/C# SDK
Use the following procedure to interact with Quick Sight using C#.NET. This example is
constructed on Microsoft Visual for Mac; the instructions can vary slightly
based on your IDE and platform.

###### To work with Quick Sight using C#.NET

1. Unzip the `nuget.zip` file into a folder called
   `nuget`.
2. Create a new **Console app** project in Visual Studio.
3. Under your solution, locate app **Dependencies**, then open the context
   (right-click) menu and choose **Add
   Packages**.
4. In the sources list, choose **Configure Sources**.
5. Choose **Add**, and name the source `QuickSightSDK`. Browse to
   the `nuget` folder and choose **Add Source**.
6. Choose **OK**. Then, with `QuickSightSDK` selected, select all
   three Quick Sight packages:
   - `AWSSDK.QuickSight`
   - `AWSSDK.Extensions.NETCore.Setup`
   - `AWSSDK.Extensions.CognitoAuthentication`

7. Choose **Add Package**.
8. Copy and paste the following sample app into your console app editor.

```
using System;
using Amazon.QuickSight.Model;
using Amazon.QuickSight;

namespace DotNetQuickSightSDKTest
{
	class Program
	{
		private static readonly string AccessKey = "`insert_your_access_key`";
		private static readonly string SecretAccessKey = "`insert_your_secret_key`";
		private static readonly string AccountID = "`AWS_account_ID`";
		private static readonly string Namespace = "default";  // leave this as default

		static void Main(string[] args)
		{
			var client = new AmazonQuickSightClient(
				AccessKey,
				SecretAccessKey,
				Amazon.RegionEndpoint.USEast1);

			var listUsersRequest = new ListUsersRequest
			{
				AwsAccountId = AccountID,
				Namespace = Namespace
			};

			client.ListUsersAsync(listUsersRequest).Result.UserList.ForEach(
				user => Console.WriteLine(user.Arn)
			);

			var listGroupsRequest = new ListGroupsRequest
			{
				AwsAccountId = AccountID,
				Namespace = Namespace
			};

			client.ListGroupsAsync(listGroupsRequest).Result.GroupList.ForEach(
				group => Console.WriteLine(group.Arn)
			);
		}
	}
}
```
