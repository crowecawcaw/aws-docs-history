# Create an IAM user for workloads that can't use

IAM roles

###### Important

As a [best practice](best-practices.md#lock-away-credentials "best-practices.md#lock-away-credentials"), we recommend you require
your human users to use [temporary credentials](id_credentials_temp.md "id_credentials_temp.md") when
accessing AWS.

Alternatively, you can manage your user identities, including your administrative user,
with [AWS IAM Identity Center](../../../singlesignon/latest/userguide/getting-started.md "../../../singlesignon/latest/userguide/getting-started.md"). We recommend you use IAM Identity Center to manage access to your accounts and
permissions within those accounts. If you are using an external identity provider, you can
also configure the access permissions for user identities in IAM Identity Center.

If your use case requires IAM users with programmatic access and long-term credentials, we
recommend that you establish procedures to update access keys when needed. For more information,
see [Update access keys](id-credentials-access-keys-update.md "id-credentials-access-keys-update.md").

To perform some account and service management tasks, you must sign in using root user
credentials. To view the tasks that require you to sign in as the root user, see [Tasks that require root user credentials](id_root-user.md#root-user-tasks "id_root-user.md#root-user-tasks").

## To create an IAM user for workloads that can't use IAM roles

###### Minimum permissions

To perform the following steps, you must have at least the following IAM permissions:

- `iam:AddUserToGroup`
- `iam:AttachGroupPolicy`
- `iam:CreateAccessKey`
- `iam:CreateGroup`
- `iam:CreateServiceSpecificCredential`
- `iam:CreateUser`
- `iam:GetAccessKeyLastUsed`
- `iam:GetAccountPasswordPolicy`
- `iam:GetAccountSummary`
- `iam:GetGroup`
- `iam:GetLoginProfile`
- `iam:GetPolicy`
- `iam:GetRole`
- `iam:GetUser`
- `iam:ListAccessKeys`
- `iam:ListAttachedGroupPolicies`
- `iam:ListAttachedUserPolicies`
- `iam:ListGroupPolicies`
- `iam:ListGroups`
- `iam:ListGroupsForUser`
- `iam:ListInstanceProfilesForRole`
- `iam:ListMFADevices`
- `iam:ListPolicies`
- `iam:ListRoles`
- `iam:ListRoleTags`
- `iam:ListSSHPublicKeys`
- `iam:ListServiceSpecificCredentials`
- `iam:ListSigningCertificates`
- `iam:ListUserPolicies`
- `iam:ListUserTags`
- `iam:ListUsers`
- `iam:UploadSSHPublicKey`
- `iam:UploadSigningCertificate`

[Show moreShow less](# "#")

Console

1. Follow the sign-in procedure appropriate to your user type as described in the topic [How to sign in to AWS](../../../signin/latest/userguide/how-to-sign-in.md "../../../signin/latest/userguide/how-to-sign-in.md") in the _AWS Sign-In User
   Guide_.
2. On the **IAM Console Home** page, in the left navigation pane, enter your query in the **Search IAM** text box.
3. In the navigation pane, choose **Users** and then choose
   **Create users**.
4. On the **Specify user details** page, do the following:
   1. For **User name**, type _`WorkloadName`_. Replace _`WorkloadName`_ with the name of
      the workload that will be using the account.
   2. Choose **Next**.

5. (Optional) On the **Set Permissions** page, do the
   following:
   1. Choose **Add user to group**.
   2. Choose **Create group**.
   3. In the **Create user group** dialog box, for **User
      group name** type a name that represents the use of the workloads in
      the group. For this example, use the name
      `Automation`.
   4. Under **Permissions policies** select the checkbox for the
      **PowerUserAccess** managed policy.

   ###### Tip

   Enter _Power_ into the **Permissions
   policies** search box to quickly find the managed policy. 5. Choose **Create user group**. 6. Back on the page with the list of IAM groups, select the checkbox for
   your new user group. Choose **Refresh** if you don't see the
   new user group in the list. 7. Choose **Next**.

6. (Optional) In the **Tags** section, add metadata to the user by
   attaching tags as key-value pairs. For more information, see [Tags for AWS Identity and Access Management resources](id_tags.md "id_tags.md").
7. Verify the user group memberships for the new user. When you are ready to
   proceed, choose **Create user**.
8. A status notification appears informing you that the user was created
   successfully. Select **View user** to go to the user details
   page
9. Select the **Security credentials** tab. Then create the
   credentials needed for the workload.
   - **Access keys**–Select **Create access
     key** to generate and download access keys for the user.

   ###### Important

   This is your only opportunity to view or download the secret access keys, and you must
   provide this information to your users before they can use the AWS API. Save the user's
   new access key ID and secret access key in a safe and secure place. **You
   will not have access to the secret keys again after this step.**
   - **SSH public keys for AWS CodeCommit**–Select
     **Upload SSH public key** to upload an SSH public key so that
     the user can communicate with CodeCommit repositories over SSH.
   - **HTTPS Git credentials for AWS CodeCommit**–Select
     **Generate credentials** to generate a unique set of user
     credentials to use with Git repositories. Select **Download
     credentials** to save the user name and password to a .csv file. This
     is the only time that information is available. If you forget or lose the
     password you will need to reset it.
   - **Credentials for Amazon Keyspaces (for Apache Cassandra)**–Select
     **Generate credentials** to generate a service-specific user
     credentials to use with Amazon Keyspaces. Select **Download credentials**
     to save the user name and password to a .csv file. This is the only time that
     information is available. If you forget or lose the password you will need to
     reset it.

   ###### Important

   Service-specific credentials are long-term credentials associated with a
   specific IAM user and can only be used for the service they were created
   for. To give IAM roles or federated identities permissions to access all
   your AWS resources using temporary credentials, use AWS authentication
   with the SigV4 authentication plugin for Amazon Keyspaces. For more
   information see, [Using temporary credentials to connect to Amazon Keyspaces (for Apache Cassandra) using an IAM role and
   the SigV4 plugin](../../../keyspaces/latest/devguide/access.md#temporary.credentials.IAM "../../../keyspaces/latest/devguide/access.md#temporary.credentials.IAM") in the _Amazon Keyspaces (for Apache Cassandra) Developer
   Guide_.
   - **X.509 Signing certificates**–Select
     **Create X.509 Certificate** if you need to make secure
     SOAP-protocol requests and are in a Region that's not supported by AWS Certificate Manager.
     ACM is the preferred tool to provision, manage, and deploy your server
     certificates. For more information about using ACM, see the [_AWS Certificate Manager User Guide_](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md").

You have created a user with programmatic access and configured it with the
**PowerUserAccess** job function. This user's permissions policy
grants full access to every service except for IAM and AWS Organizations.

You can use this same process to give additional workloads programmatic access to
your AWS account resources, if the workloads are unable to assume IAM roles. This
procedure used the **PowerUserAccess** managed policy to assign
permissions. To follow the best practice of least privilege, consider using a more
restrictive policy or creating a custom policy that restricts access to only resources
required by the program. To learn about using policies that restrict user permissions to
specific AWS resources, see [Access management for AWS resources](access.md "access.md") and [Example IAM identity-based policies](access_policies_examples.md "access_policies_examples.md"). To add
additional users to the user group after it's created, see [Edit users in IAM groups](id_groups_manage_add-remove-users.md "id_groups_manage_add-remove-users.md").

AWS CLI

1. Create a user named `Automation`.
   - [aws iam
     create-user](../../../cli/latest/reference/iam/create-user.md "../../../cli/latest/reference/iam/create-user.md")

```

              aws iam create-user \
                  --user-name `Automation`
```

2. Create an IAM user group named `AutomationGroup`, attach
   the AWS managed policy `PowerUserAccess` to the group, and then add the
   `Automation` user to the group.

###### Note

An _AWS managed policy_ is a standalone policy that is
created and administered by AWS. Each policy has its own Amazon Resource Name
(ARN) that includes the policy name. For example,
`arn:aws:iam::aws:policy/IAMReadOnlyAccess` is an AWS managed
policy. For more information about ARNs, see [IAM ARNs](reference_identifiers.md#identifiers-arns "reference_identifiers.md#identifiers-arns"). For a list of AWS managed policies for
AWS services, see [AWS managed
policies](../../../aws-managed-policy/latest/reference/policy-list.md "../../../aws-managed-policy/latest/reference/policy-list.md").

    * [aws iam create-group](../../../cli/latest/reference/iam/create-group.md "../../../cli/latest/reference/iam/create-group.md")




    ```

                      aws iam create-group \
                          --group-name `AutomationGroup`
    ```
    * [aws iam
     attach-group-policy](../../../cli/latest/reference/iam/attach-group-policy.md "../../../cli/latest/reference/iam/attach-group-policy.md")



    ```

                      aws iam attach-group-policy \
                          --policy-arn arn:aws:iam::aws:policy/PowerUserAccess \
                          --group-name `AutomationGroup`
    ```
    * [aws iam
     add-user-to-group](../../../cli/latest/reference/iam/add-user-to-group.md "../../../cli/latest/reference/iam/add-user-to-group.md")




    ```

                     aws iam add-user-to-group \
                         --user-name `Automation` \
                         --group-name `AutomationGroup`

    ```
    * Run the [aws iam
     get-group](../../../cli/latest/reference/iam/get-group.md "../../../cli/latest/reference/iam/get-group.md") command to list the `AutomationGroup`
     and its members.



    ```

                    aws iam get-group \
                         --group-name `AutomationGroup`

    ```

3. Create the security credentials needed for the workload.
   - **Create access keys for testing**–[aws iam
     create-access-key](../../../cli/latest/reference/iam/create-access-key.md "../../../cli/latest/reference/iam/create-access-key.md")

   ```

                          aws iam create-access-key \
                              --user-name Automation
   ```

   The output of this command displays the secret access key and the access key
   ID. Record and store this information in a secure location. If these credentials
   are lost, they can't be recovered, and you must create a new access key.

   ###### Important

   These IAM user access keys are long-term credentials that present a
   security-risk to your account. After you have completed testing, we recommend
   that you delete these access keys. If you have scenarios in which you are
   considering access keys, investigate whether you can enable MFA for your
   workload IAM user and use [aws sts
   get-session-token](../../../cli/latest/reference/sts/get-session-token.md "../../../cli/latest/reference/sts/get-session-token.md") to obtain temporary credentials for the session
   instead of using IAM access keys.
   - **Upload SSH public keys for AWS CodeCommit**–[aws iam
     upload-ssh-public-key](../../../cli/latest/reference/iam/upload-ssh-public-key.md "../../../cli/latest/reference/iam/upload-ssh-public-key.md")

   The following example assumes that you have your SSH public keys stored in
   the file `sshkey.pub`.

   ```

                          aws upload-ssh-public-key \
                              --user-name `Automation` \
                              --ssh-public-key-body file://sshkey.pub
   ```

   - **Upload an X.509 signing certificate**–[aws iam
     upload-signing-certificate](../../../cli/latest/reference/iam/upload-signing-certificate.md "../../../cli/latest/reference/iam/upload-signing-certificate.md")

   Upload an X.509 certificate if you need to make secure SOAP-protocol
   requests and are in a Region that's not supported by AWS Certificate Manager. ACM is the
   preferred tool to provision, manage, and deploy your server certificates. For
   more information about using ACM, see the [_AWS Certificate Manager User Guide_](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md").

   The following example assumes that you have your X.509 signing certificate
   stored in the file `certificate.pem`.

   ```

                         aws iam upload-signing-certificate \
                         --user-name Automation \
                         --certificate-body file://certificate.pem

   ```

You can use this same process to give additional workloads programmatic access to
your AWS account resources, if the workloads are unable to assume IAM roles. This
procedure used the **PowerUserAccess** managed policy to assign
permissions. To follow the best practice of least privilege, consider using a more
restrictive policy or creating a custom policy that restricts access to only resources
required by the program. To learn about using policies that restrict user permissions to
specific AWS resources, see [Access management for AWS resources](access.md "access.md") and [Example IAM identity-based policies](access_policies_examples.md "access_policies_examples.md"). To add
additional users to the user group after it's created, see [Edit users in IAM groups](id_groups_manage_add-remove-users.md "id_groups_manage_add-remove-users.md").
