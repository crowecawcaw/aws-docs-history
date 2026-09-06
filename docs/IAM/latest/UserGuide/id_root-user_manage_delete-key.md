

# Delete access keys for the root user
<a name="id_root-user_manage_delete-key"></a>

You can use the AWS Management Console, the AWS CLI or the AWS API to delete the root user access keys.

------
#### [ AWS Management Console ]

**To delete an access key for the root user**
**Minimum permissions**  
To perform the following steps, you must have at least the following IAM permissions:  
You must sign in as the AWS account root user, which requires no additional AWS Identity and Access Management (IAM) permissions. You can't perform these steps as an IAM user or role.

1. Open the [AWS Management Console](https://console.aws.amazon.com/) and sign in using your root user credentials.

   For instructions, see [Sign in to the AWS Management Console as the root user](https://docs.aws.amazon.com/signin/latest/userguide/introduction-to-root-user-sign-in-tutorial.html) in the *AWS Sign-In User Guide*.

1. In the upper right corner of the console, choose your account name or number and then choose **Security Credentials**. 

1. In the **Access keys** section, select the access key that you want to delete, and then, under **Actions**, choose **Delete**.
**Note**  
Alternatively, you can **Deactivate** an access key, instead of permanently deleting it. This way you can resume using it in the future without having to change either the key ID or secret key. While the key is inactive, any attempts to use it in requests to the AWS API fail with the error access denied.

1. On the **Delete <access key ID>** dialog box, choose **Deactivate**, enter the access key ID to confirm you want to delete it, and then choose **Delete**. 

------
#### [ AWS CLI & SDKs ]

**To delete an access key for the root user**
**Minimum permissions**  
To perform the following steps, you must have at least the following IAM permissions:  
You must sign in as the AWS account root user, which requires no additional AWS Identity and Access Management (IAM) permissions. You can't perform these steps as an IAM user or role.
+ AWS CLI: [aws iam delete-access-key](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-access-key.html)  
**Example**  

  ```
  $ aws iam delete-access-key \
      --access-key-id AKIAIOSFODNN7EXAMPLE
  ```

  This command produces no output when successful.
+ AWS API: [DeleteAccessKey](https://docs.aws.amazon.com/IAM/latest/APIReference/API_DeleteAccessKey.html) 

------