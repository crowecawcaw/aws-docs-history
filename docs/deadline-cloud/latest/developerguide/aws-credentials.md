# Configuring AWS credentials

The initial phase of the worker life cycle is bootstrapping. In this phase the worker
 agent software creates a worker in your fleet, and obtains AWS credentials from your
 fleet's role for further operation. 


AWS credentials for Amazon EC2
###### To create an IAM role for Amazon EC2 with Deadline Cloud worker host permissions

1. Open the IAM console at
 [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles** in the
 navigation pane, then choose **Create** role.
3. Select **AWS service**.
4. Select **EC2** as the **Service or use
 case**, then select **Next**.
5. To grant the necessary permissions, attach the
 `AWSDeadlineCloud-WorkerHost` AWS managed policy.


On-premises AWS credentials
Your on-premises workers use credentials to access Deadline Cloud. For the most secure
 access, we recommend using IAM Roles Anywhere to authenticate your workers.
 For more information, see [IAM Roles Anywhere](https://https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html "https://https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html").


 For testing, you can use IAM user access keys for AWS credentials. We
 recommend that you set an expiration for the IAM user by including a
 restrictive inline policy.


###### Important

Heed the following warnings:


* **Do NOT** use your account's root
 credentials to access AWS resources. These credentials provide
 unrestricted account access and are difficult to revoke.
* **Do NOT** put literal access keys or
 credential information in your application files. If you do, you
 create a risk of accidentally exposing your credentials if, for
 example, you upload the project to a public repository.
* **Do NOT** include files that contain
 credentials in your project area.
* Secure your access keys. Do not provide your access keys to
 unauthorized parties, even to help [find your account identifiers](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html "https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-identifiers.html"). By doing this, you might
 give someone permanent access to your account.
* Be aware that any credentials stored in the shared AWS
 credentials file are stored in plain text.

For more details, see [Best practices for managing AWS access keys in the *AWS
 General Reference*.](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#securing_access-keys")


###### Create an IAM user

1. Open the IAM console at
 [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, select **Users** and the
 select **Create user**.
3. Name the user. Clear the checkbox for **Provide user access to
 the AWS Management Console**, then choose
 **Next**.
4. Choose **Attach policies directly**.
5. From the list of permission policies, choose the
 **AWSDeadlineCloud-WorkerHost** policy and then
 choose **Next**.
6. Review the user details and then choose **Create
 user**.

###### Restrict user access to a limited time window

Any IAM user access keys that you create are long-term credentials. To
 ensure that these credentials expire in case they are mishandled, you can
 make these credentials time-bound by creating an inline policy that
 specifies a date after which the keys will no longer be valid.

1. Open the IAM user that you just created. In the
 Permissions tab, choose **Add permissions**
 and then choose **Create inline policy**.
2. In the JSON editor, specify the following permissions. To use this
 policy, replace the `aws:CurrentTime` timestamp value in the
 example policy with your own time and date.


JSONJSON




```
`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Effect": "Deny",
 "Action": "*",
 "Resource": "*",
 "Condition": {
 "DateGreaterThan": {
 "aws:CurrentTime": "`2024-01-01T00:00:00Z`"
 }
 }
 }
 ]
}`

```

###### Create an access key

1. On the user details page, select the **Security
 credentials** tab. In the **Access keys**
 section, choose **Create access key**.
2. Indicate that you want to use the key for Other, then choose
 **Next**, then choose **Create access
 key**.
3. On the **Retrieve access keys** page, choose
 **Show** to reveal the value of your user's secret
 access key. You can copy the credentials or download a .csv file.

###### Store the user access keys

* Store the user access keys in the agent user's AWS credentials file
 on the worker host system:




	+ On Linux, the file is located at
	 `~/.aws/credentials`
	+ On Windows, the file is located at
	 `%USERPROFILE\.aws\credentials`
Replace the following keys:



```
[default]
aws_access_key_id=`ACCESS_KEY_ID`
aws_secret_access_key=`SECRET_ACCESS_KEY`
```

###### Important

When you no longer need this IAM user, we recommend that you remove it
 to align with the [AWS security best practice](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials "https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials"). We recommend that you require
 your human users to use temporary credentials through [AWS IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md") when accessing AWS.
