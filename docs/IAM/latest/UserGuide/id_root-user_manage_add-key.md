# Create access keys for the root user

###### Warning

We strongly recommend that you do **not** create access key
pairs for your root user. Because [only a few tasks require the
root user](id_root-user.md#root-user-tasks "id_root-user.md#root-user-tasks") and you typically perform those tasks infrequently, we recommend signing in
to the AWS Management Console to perform the root user tasks. Before creating access keys, review the [alternatives to long-term
access keys](security-creds-programmatic-access.md#security-creds-alternatives-to-long-term-access-keys "security-creds-programmatic-access.md#security-creds-alternatives-to-long-term-access-keys").

Although we don't recommend it, you can create access keys for your root user so that you can
run commands in the AWS Command Line Interface (AWS CLI) or use API operations from one of the AWS SDKs using
root user credentials. When you create access keys, you create the access key ID and secret
access key as a set. During access key creation, AWS gives you one opportunity to view and
download the secret access key part of the access key. If you don't download it or if you lose
it, you can delete the access key and then create a new one. You can create root user access keys
with the console, AWS CLI, or AWS API.

A newly created access key has the status of _active_, which means that
you can use the access key for CLI and API calls. You can assign up to two access keys to the
root user.

Access keys that are not in use should be inactivated. Once an access key is inactive, you
can't use it for API calls. Inactive keys still count toward your limit. You can create or
delete an access key any time. However, when you delete an access key, it's gone forever and
can't be retrieved.

AWS Management Console

###### To create an access key for the AWS account root user

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- You must sign in as the AWS account root user, which requires no additional
  AWS Identity and Access Management (IAM) permissions. You can't perform these steps as an IAM user or
  role.

1. Open the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") and sign in using your root user credentials.

For instructions, see [Sign
in to the AWS Management Console as the root user](../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md "../../../signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.md") in the _AWS Sign-In User
Guide_. 2. In the upper right corner of the console, choose your account name or number and
then choose **Security Credentials**. 3. In the **Access keys** section, choose **Create access
key**. If this option is not available, then you already have the maximum
number of access keys. You must delete one of the existing access keys before you
can create a new key. For more information, see [IAM
Object Quotas](reference_iam-quotas.md#reference_iam-quotas-entities "reference_iam-quotas.md#reference_iam-quotas-entities"). 4. On the **Alternatives to root user access keys** page, review the
security recommendations. To continue, select the checkbox, and then choose
**Create access key**. 5. On the **Retrieve access key** page, your **Access
key** ID is displayed. 6. Under **Secret access key**, choose **Show**
and then copy the access key ID and secret key from your browser window and paste it
somewhere secure. Alternatively, you can choose **Download .csv
file** which will download a file named `rootkey.csv` that
contains the access key ID and the secret key. Save the file somewhere safe. 7. Choose **Done**. When you no longer need the access key [we recommend that you delete it](id_root-user_manage_delete-key.md "id_root-user_manage_delete-key.md"),
or at least consider deactivating it so that no one can misuse it.

AWS CLI & SDKs

###### To create an access key for the root user

###### Note

To run the following command or API operation as the root user, you must already
have one active access key pair. If you don't have any access keys, create the first
access key using the AWS Management Console. Then, you can use the credentials from that first
access key with the AWS CLI to create the second access key, or to delete an access
key.

- AWS CLI: [aws iam
  create-access-key](../../../cli/latest/reference/iam/create-access-key.md "../../../cli/latest/reference/iam/create-access-key.md")

```
`$` `aws iam create-access-key``{
 "AccessKey": {
 "UserName": "MyUserName",
 "AccessKeyId": "AKIAIOSFODNN7EXAMPLE",
 "Status": "Active",
 "SecretAccessKey": "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
 "CreateDate": "2021-04-08T19:30:16+00:00"
 }
}`
```

- AWS API: [CreateAccessKey](../APIReference/API_CreateAccessKey.md "../APIReference/API_CreateAccessKey.md") in
  the _IAM API Reference_.
