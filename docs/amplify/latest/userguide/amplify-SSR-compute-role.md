

# Adding an SSR Compute role to allow access to AWS resources
<a name="amplify-SSR-compute-role"></a>

This integration, enables you to assign an IAM role to the Amplify SSR Compute service to allow your server-side rendered (SSR) application to securely access specific AWS resources based on the role's permissions. For example, you can allow your app's SSR compute functions to securely access other AWS services or resources, such as Amazon Bedrock or an Amazon S3 bucket, based on the permissions defined in the assigned IAM role.

The IAM SSR Compute role provides temporary credentials, eliminating the need to hardcode long-lived security credentials in environment variables. Using the IAM SSR Compute role aligns with the AWS security best practices of granting least-privilege permissions and using short-term credentials when possible.

The instructions later in this section describe how to create a policy with custom permissions and attach the policy to a role. When you create the role, you must attach a custom trust policy that gives Amplify permission to assume the role. If the trust relationship isn't defined correctly, you will get an error when you try to add the role. The following custom trust policy grants Amplify permission to assume the role.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "Service": [
                    "amplify.amazonaws.com"
                ]
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
```

------

You can associate an IAM role in your AWS account with an existing SSR application using the Amplify console, AWS SDKs, or the AWS CLI. The role that you attach is automatically associated with the Amplify SSR compute service, granting it the permissions that you specify to access other AWS resources. As your application's needs change over time, you can modify the attached IAM role without redeploying your application. This provides flexibility and reduces application downtime.

**Important**  
You are responsible for configuring your application to meet your security and compliance objectives. This includes managing your SSR Compute role, which should be configured to have the minimum set of permissions needed to support your use case. For more information, see [Managing IAM SSR Compute role security](#managing-compute-role-security).

## Creating an SSR Compute role in the IAM console
<a name="create-SSR-compute-role-IAM-console"></a>

Before you can attach an IAM SSR Compute role to an Amplify application, the role must already exist in your AWS account. In this section, you will learn how to create an IAM policy and attach it to a role that Amplify can assume to access specific AWS resources.

We recommend that you follow the AWS best practice of granting *least-privilege* permissions when creating an IAM role. The IAM SSR Compute role is called only from SSR compute functions and therefore should only grant the permissions required to run the code.

You can use the AWS Management Console, AWS CLI, or SDKs to create policies in IAM. For more interformation, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the *IAM User Guide*.

The following instructions demonstrate how to use the IAM console to create an IAM policy that defines the permissions to grant to the Amplify Compute service.

**To use the IAM console JSON policy editor to create a policy**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane on the left, choose **Policies**. 

1. Choose **Create policy**.

1. In the **Policy editor** section, choose the **JSON** option.

1. Type or paste a JSON policy document.

1. When you are finished adding permissions to the policy, choose **Next**.

1. On the **Review and create** page, type a **Policy Name** and a **Description** (optional) for the policy that you are creating. Review **Permissions defined in this policy** to see the permissions that are granted by your policy.

1. Choose **Create policy** to save your new policy.

After you create a policy, use the following instructions to attach the policy to an IAM role.

**To create a role that grants Amplify permissions to specific AWS resources**

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. In the navigation pane of the console, choose **Roles** and then choose **Create role**.

1. Choose the **Custom trust policy** role type.

1. In the **Custom trust policy** section, enter the custom trust policy for the role. A role trust policy is required and defines the principals that you trust to assume the role. 

   Copy and paste the following trust policy to grant the Amplify service permission to assume this role.

------
#### [ JSON ]

****  

   ```
   {
       "Version":"2012-10-17",		 	 	 
       "Statement": [
           {
               "Sid": "Statement1",
               "Effect": "Allow",
               "Principal": {
                   "Service": [
                       "amplify.amazonaws.com"
                   ]
               },
               "Action": "sts:AssumeRole"
           }
       ]
   }
   ```

------

1. Resolve any security warnings, errors, or general warnings generated during policy validation, and then choose **Next**.

1. On the **Add permissions** page, search for the name of the policy that you created in the previous procedure and select it. Then choose **Next**.

1. For **Role name**, enter a role name. Role names must be unique within your AWS account. They are not distinguished by case. For example, you cannot create roles named both **PRODROLE** and **prodrole**. Because other AWS resources might reference the role, you cannot edit the name of the role after it has been created.

1. (Optional) For **Description**, enter a description for the new role.

1. (Optional) Choose **Edit** in the **Step 1: Select trusted entities** or **Step 2: Add permissions** sections to edit the custom policy and permissions for the role. 

1. Review the role and then choose **Create role**.

## Adding an IAM SSR Compute role to an Amplify app
<a name="add-ssr-compute-role-to-app"></a>

After you have created an IAM role in your AWS account, you can associate it with an app in the Amplify console.

**To add an SSR Compute role to an app in the Amplify console**

1. Sign in to the AWS Management Console and open the Amplify console at [https://console.aws.amazon.com/amplify/](https://console.aws.amazon.com/amplify/).

1. On the **All apps** page, choose the name of the app to add a Compute role to.

1. In the navigation pane, choose **App settings**, and then choose **IAM roles**.

1. In the **Compute role** section, choose **Edit**.

1. In the **Default role** list, search for the name of the role you want to attach and select it. For this example, you can choose the name of the role you created in the previous procedure. By default, the role that you select will be associated with all branches of your app.

   If the role's trust relationship isn't defined correctly, you will get an error and you won't be able to add the role.

1. (optional) If your application is in a public repository and uses auto-branch creation or has web previews for pull requests enabled, we don't recommend using an app-level role. Instead, attach the Compute role only to branches that require access to specific resources. To override the default app-level behavior and attach a role to a specific branch, do the following:

   1. For **Branch**, select the name of the branch to use.

   1. For **Compute role**, select the name of the role to associate with the branch.

1. Choose, **Save**.

## Managing IAM SSR Compute role security
<a name="managing-compute-role-security"></a>

Security is a shared responsibility between AWS and you. You are responsible for configuring your application to meet your security and compliance objectives. This includes managing your SSR Compute role, which should be configured to have the minimum set of permissions needed to support your use case. Credentials for the SSR Compute role that you specify are immediately available in the runtime of your SSR function. If your SSR code exposes these credentials, either intentionally, due to a bug, or by permitting remote code execution (RCE), an unauthorized user can gain access to the SSR role and its permissions.

When an application in a public repository uses an SSR Compute role and auto-branch creation or web previews for pull requests, you need to carefully manage which branches can access the role. We recommend that you don't use an app-level role. Instead, you should attach a Compute role at the branch-level. This allows you to grant permissions only to the branches that require access to specific resources. 

If your role's credentials are exposed, take the following actions to remove all access to the role's credentials.

1. **Revoke all sessions**

   For instructions on immediately revoking all permissions to the role's credentials, see [ Revoke IAM role temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_revoke-sessions.html).

1. **Delete the role from the Amplify console**

   This action takes immediate effect. You don't need to redeploy your application. 

**To delete a Compute role in the Amplify console**

1. Sign in to the AWS Management Console and open the Amplify console at [https://console.aws.amazon.com/amplify/](https://console.aws.amazon.com/amplify/).

1. On the **All apps** page, choose the name of the app to remove the Compute role from.

1. In the navigation pane, choose **App settings**, and then choose **IAM roles**.

1. In the **Compute role** section, choose **Edit**.

1. To delete the **Default role**, choose the **X** to the right of the role's name.

1. Choose **Save**.