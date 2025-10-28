# Create new access keys for an IAM user

If you already have an IAM user, you can create new access keys at any time. For more information about key management,
for example how to update access keys, see
[Managing access keys for IAM users](../../../IAM/latest/UserGuide/id_credentials_access-keys.md "../../../IAM/latest/UserGuide/id_credentials_access-keys.md").

###### To create access keys for an IAM user (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Users**.
3. Choose the name of the user whose access keys you want to create.
4. On the **Summary** page of the user, choose the **Security
   credentials** tab.
5. In the **Access keys** section under
   **Access key best practices & alternatives**,
   choose the use case **Other**. Click **Next**, enter optional
   information as needed, and
   choose **Create access key**.

To view the new access key pair, choose **Show**. Your credentials will look something like this:

    * Access key ID: AKIAIOSFODNN7EXAMPLE
    * Secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

###### Note

You will not have access to the secret access key again after this dialog box closes.

Consider the following best practices for the key pair that you've created.

    * Never store your access key in plain text, in a code repository, or in code.
    * Disable or delete access keys when no longer needed.
    * Enable least-privilege permissions.
    * Rotate access keys regularly.

6. To download the key pair, choose **Download .csv file**. Store the keys in a secure location.
7. After you download the .csv file, choose **Close**.
   When you create an access key, the key pair is active by default, and you can use the pair right away.
