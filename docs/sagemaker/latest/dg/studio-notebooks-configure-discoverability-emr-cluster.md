

# Configure listing Amazon EMR clusters
<a name="studio-notebooks-configure-discoverability-emr-cluster"></a>

Administrators can configure permissions for the SageMaker Studio execution role to grant users the ability to view the list of Amazon EMR clusters they have access to, allowing them to connect to these clusters. The clusters to which you want access can be deployed in the same AWS account as Studio (choose *Single account*) or in separate accounts (choose *Cross account*). The following page describes how to grant the permissions for viewing Amazon EMR clusters from Studio or Studio Classic.

**Important**  
You can only discover and connect to Amazon EMR clusters for JupyterLab and Studio Classic applications that are launched from private spaces. Ensure that the Amazon EMR clusters are located in the same AWS region as your Studio environment.

To let data scientists discover and then connect to Amazon EMRclusters from Studio or Studio Classic, follow these steps.

## Single account
<a name="studio-set-up-emr-permissions-singleaccount-list-clusters"></a>

If your Amazon EMR clusters and Studio or Studio Classic are deployed in the same AWS account, attach the following permissions to the SageMaker AI execution role accessing your cluster.

1. **Step 1**: Retrieve the ARN of the SageMaker AI execution role used by your private space.

   For information on spaces and execution roles in SageMaker AI, see [Understanding domain space permissions and execution roles](execution-roles-and-spaces.md).

   For more information about how to retrieve the ARN of SageMaker AI's execution role, see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role).

1. **Step 2**: Attach the following permissions to the SageMaker AI execution role accessing your Amazon EMR clusters.

   1. Navigate to the [IAM console](https://console.aws.amazon.com/iam).

   1. Choose **Roles** and then search for your execution role by name in the **Search** field. The role name is the last part of the ARN, after the last forward slash (/). 

   1. Follow the link to your role.

   1. Choose **Add permissions** and then **Create inline policy**.

   1. In the **JSON** tab, add the Amazon EMR permissions allowing Amazon EMR access and operations. For details on the policy document, see *List Amazon EMR policies* in [Reference policies](studio-set-up-emr-permissions-reference.md). Replace the `region`, and `accountID` with their actual values before copying the list of statements to the inline policy of your role.

   1. Choose **Next** and then provide a **Policy name**.

   1. Choose **Create policy**.

**Note**  
Users of role-based access control (RBAC) connectivity to Amazon EMR clusters should also refer to [Configure runtime role authentication when your Amazon EMR cluster and Studio are in the same account](studio-notebooks-emr-cluster-rbac.md#studio-notebooks-emr-cluster-iam-same). 

## Cross account
<a name="studio-set-up-emr-permissions-crossaccount-list-clusters"></a>

Before you get started, retrieve the ARN of the SageMaker AI execution role used by your private space.

For information on spaces and execution roles in SageMaker AI, see [Understanding domain space permissions and execution roles](execution-roles-and-spaces.md).

For more information about how to retrieve the ARN of SageMaker AI's execution role, see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role).

If your Amazon EMR clusters and Studio or Studio Classic are deployed in separate AWS accounts, you configure the permissions on both accounts.

**Note**  
Users of role-based access control (RBAC) connectivity to Amazon EMR clusters should also refer to [Configure runtime role authentication when your cluster and Studio are in different accounts](studio-notebooks-emr-cluster-rbac.md#studio-notebooks-emr-cluster-iam-diff). 

**On the Amazon EMR cluster account**

Follow these steps to create the necessary roles and policies on the account where Amazon EMR is deployed, also referred to as the *trusting account*:

1. **Step 1**: Retrieve the ARN of the [service role of your Amazon EMR cluster](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-role.html). 

   To learn about how to find the ARN of the service role of a cluster, see [Configure IAM service roles for Amazon EMR permissions to AWS services and resources](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles.html#emr-iam-role-landing).

1. **Step 2**: Create a custom IAM role named `AssumableRole` with the following configuration:
   + Permissions: Grant the necessary permissions to `AssumableRole` to allow accessing Amazon EMR resources. This role is also known as an *Access role* in scenarios involving cross-account access.
   + Trust relationship: Configure the trust policy for `AssumableRole` to allow assuming the execution role (The `SageMakerExecutionRole` in the cross-account diagram) from the Studio account that requires access.

   By assuming the role, Studio or Studio Classic can gain temporary access to the permissions it needs in Amazon EMR.

   For detailed instructions on how to create a new `AssumableRole` in your Amazon EMR AWS account, follow these steps:

   1. Navigate to the [IAM console](https://console.aws.amazon.com/iam).

   1. In the left navigation pane, choose **Policy**, and then **Create policy**.

   1. In the **JSON** tab, add the Amazon EMR permissions allowing Amazon EMR access and operations. For details on the policy document, see *List Amazon EMR policies* in [Reference policies](studio-set-up-emr-permissions-reference.md). Replace the `region`, and `accountID` with their actual values before copying the list of statements to the inline policy of your role.

   1. Choose **Next** and then provide a **Policy name**.

   1. Choose **Create policy**.

   1. In the left navigation pane, choose **Roles** and then **Create role**.

   1. On the **Create role** page, choose **Custom trust policy** as the trusted entity.

   1. Paste in the following JSON document in the **Custom trust policy** section and then choose **Next**.

------
#### [ For users of Studio and JupyterLab ]

      Replace `studio-account` with the Studio account ID, and `AmazonSageMaker-ExecutionRole` with the execution role used by your JupyterLab space.

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "AWS": "arn:aws:iam::{{111122223333}}:role/service-role/{{AmazonSageMaker-ExecutionRole}}"
                  },
                  "Action": "sts:AssumeRole"
              }
          ]
      }
      ```

------

------
#### [ For users of Studio Classic ]

      Replace `studio-account` with the Studio Classic account ID.

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Effect": "Allow",
                  "Principal": {
                      "AWS": "arn:aws:iam::{{111122223333}}:root"
                  },
                  "Action": "sts:AssumeRole"
              }
          ]
      }
      ```

------

------

   1. In the **Add permissions** page, add the permission you just created and then choose **Next**.

   1. On the **Review** page, enter a name for the role such as `AssumableRole` and an optional description.

   1. Review the role details and choose **Create role**.

   For more information about creating a role on an AWS account, see [Creating an IAM role (console)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html).

**On the Studio account**

On the account where Studio is deployed, also referred to as the *trusted account*, update the SageMaker AI execution role accessing your clusters with the required permissions to access resources in the trusting account.

1. **Step 1**: Retrieve the ARN of the SageMaker AI execution role used by your private space.

   For information on spaces and execution roles in SageMaker AI, see [Understanding domain space permissions and execution roles](execution-roles-and-spaces.md).

   For more information about how to retrieve the ARN of SageMaker AI's execution role, see [Get your execution role](sagemaker-roles.md#sagemaker-roles-get-execution-role).

1. **Step 2**: Attach the following permissions to the SageMaker AI execution role accessing your Amazon EMR clusters.

   1. Navigate to the [IAM console](https://console.aws.amazon.com/iam).

   1. Choose **Roles** and then search for your execution role by name in the **Search** field. The role name is the last part of the ARN, after the last forward slash (/). 

   1. Follow the link to your role.

   1. Choose **Add permissions** and then **Create inline policy**.

   1. In the **JSON** tab, add the inline policy granting the role permissions to update the domains, user profiles, and spaces. For details on the policy document, see *Domain, user profile, and space update actions policy* in [Reference policies](studio-set-up-emr-permissions-reference.md). Replace the `region` and `accountID` with their actual values before copying the list of statements to the inline policy of your role.

   1. Choose **Next** and then provide a **Policy name**.

   1. Choose **Create policy**.

   1. Repeat the **Create inline policy** step to add another policy granting the execution role the permissions to assume the `AssumableRole` and then perform actions permitted by the role's access policy. Replace `emr-account` with the Amazon EMR account ID, and `AssumableRole` with the name of the assumable role created in the Amazon EMR account.

------
#### [ JSON ]

****  

      ```
      {
          "Version":"2012-10-17",		 	 	 
          "Statement": [
              {
                  "Sid": "AllowRoleAssumptionForCrossAccountDiscovery",
                  "Effect": "Allow",
                  "Action": "sts:AssumeRole",
                  "Resource": [
                      "arn:aws:iam::{{111122223333}}:role/{{AssumableRole}}"
                  ]
              }
          ]
      }
      ```

------

   1. (Optional) To allow listing Amazon EMR clusters deployed in the same account as Studio, add an additional inline policy to your Studio execution role as defined in *List Amazon EMR policies* in [Reference policies](studio-set-up-emr-permissions-reference.md). 

1. **Step 3**: Associate your assumable role(s) (access role) with your domain or user profile. JupyterLab users in Studio can use the SageMaker AI console or the provided script.

    Choose the tab that corresponds to your use case.

------
#### [ Associate your assumable roles in JupyterLab using the SageMaker AI console ]

   To associate your assumable roles with your user profile or domain using the SageMaker AI console:

   1. Navigate to the SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

   1. In the left navigation pane, choose **domain**, and then select the domain using the SageMaker AI execution role whose permissions you updated.

   1. 
      + To add your assumable role(s) (access role) to your domain: In the **App Configurations** tab of the **Domain details** page, navigate to the **JupyterLab** section.
      + To add your assumable role(s) (access role) to your user profile: On the **Domain details** page, chose the **User profiles** tab, select the user profile using the SageMaker AI execution role whose permissions you updated. In the **App Configurations** tab, navigate to the **JupyterLab** section.

   1. Choose **Edit** and add the ARNs of your assumable role (access role).

   1. Choose **Submit**.

------
#### [ Associate your assumable roles in JupyterLab using a Python script ]

    In a JupyterLab application started from a space using the SageMaker AI execution role whose permissions you updated, run the following command in a terminal. Replace the `domainID`, `user-profile-name`, `emr-accountID`, and `AssumableRole` ( `EMRServiceRole` for [RBAC runtime roles]()) with their proper values. This code snippet updates the user profile settings for a specific user profile (use `client.update_userprofile`) or domain settings (use `client.update_domain`) within a SageMaker AI domain. Specifically, it allows the JupyterLab application to assume a particular IAM role (`AssumableRole`) for running Amazon EMR clusters within the Amazon EMR account.

   ```
   import botocore.session
   import json
   sess = botocore.session.get_session()
   client = sess.create_client('sagemaker')
   
   client.update_userprofile(
   DomainId="{{domainID}}", 
   UserProfileName="{{user-profile-name}}",
   DefaultUserSettings={
       'JupyterLabAppSettings': {
           'EmrSettings': {
               'AssumableRoleArns': ["arn:aws:iam::{{emr-accountID}}:role/{{AssumableRole}}"],
               'ExecutionRoleArns': ["arn:aws:iam::{{emr-accountID}}:role/{{EMRServiceRole}}", 
                                "arn:aws:iam::{{emr-accountID}}:role/{{AnotherServiceRole}}"]
           }
           
       }
   })
   resp = client.describe_user_profile(DomainId="{{domainID}}", UserProfileName={{user-profile-name}}")
   
   resp['CreationTime'] = str(resp['CreationTime'])
   resp['LastModifiedTime'] = str(resp['LastModifiedTime'])
   print(json.dumps(resp, indent=2))
   ```

------
#### [ For users of Studio Classic ]

   Provide the ARN of the `AssumableRole` to your Studio Classic execution role. The ARN is loaded by the Jupyter server at launch. The execution role used by Studio assumes that cross-account role to discover and connect to Amazon EMR clusters in the *trusting account*.

   You can specify this information by using Lifecycle Configuration (LCC) scripts. You can attach the LCC to your domain or a specific user profile. The LCC script that you use must be a JupyterServer configuration. For more information on how to create an LCC script, see [Use Lifecycle Configurations with Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-lcc.html). 

   The following is an example LCC script. To modify the script, replace `AssumableRole` and `emr-account` with their respective values. The number of cross-accounts is limited to five.

   ```
   # This script creates the file that informs Studio Classic that the role "arn:aws:iam::emr-account:role/AssumableRole" in remote account "emr-account" must be assumed to list and describe Amazon EMR clusters in the remote account.
   
   #!/bin/bash
   
   set -eux
   
   FILE_DIRECTORY="/home/sagemaker-user/.cross-account-configuration-DO_NOT_DELETE"
   FILE_NAME="emr-discovery-iam-role-arns-DO_NOT_DELETE.json"
   FILE="$FILE_DIRECTORY/$FILE_NAME"
   
   mkdir -p $FILE_DIRECTORY
   
   cat > "$FILE" <<- "EOF"
   {
     {{emr-cross-account1}}: "arn:aws:iam::{{emr-cross-account1}}:role/AssumableRole",
     {{emr-cross-account2}}: "arn:aws:iam::{{emr-cross-account2}}:role/AssumableRole"
   }
   EOF
   ```

    After the LCC runs and the files are written, the server reads the file `/home/sagemaker-user/.cross-account-configuration-DO_NOT_DELETE/emr-discovery-iam-role-arns-DO_NOT_DELETE.json` and stores the cross-account ARN.

------

Refer to [List Amazon EMR clusters from Studio or Studio Classic](discover-emr-clusters.md) to learn about how to discover and connect to Amazon EMR clusters from Studio or Studio Classic notebooks.