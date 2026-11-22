

# Granting registry permissions for cross account replication in Amazon ECR

The cross account policy type is used to grant permissions to an AWS principal, allowing the replication of the repositories from a source registry to your registry. By default, you have permission to configure cross-Region replication within your own registry. You only need to configure the registry policy if you're granting another account permission to replicate contents to your registry.

Your registry policy must grant permission for the `ecr:ReplicateImage` API action. When you enable replication of deletes for a replication rule, your registry policy must also grant permission for the `ecr:ReplicateImageDelete` API action. These are internal Amazon ECR APIs that can replicate images, image deletions, and image tag removals between Regions or accounts. You can also grant permission for the ` ecr:CreateRepository` permission, which allows Amazon ECR to create repositories in your registry if they don't exist already. If the `ecr:CreateRepository` permission isn't provided, a repository with the same name as the source repository must be created manually in your registry. If neither is done, replication fails. Any failed `CreateRepository`, `ReplicateImage`, or `ReplicateImageDelete` API actions show up in CloudTrail.

## To configure a permissions policy for replication (AWS Management Console)
<a name="registry-permissions-create-console"></a>

1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/](https://console.aws.amazon.com/ecr/).

1. From the navigation bar, choose the Region to configure your registry policy in.

1. In the navigation pane, choose **Private registry**, choose **Features & Settings**, and then choose **Permissions** .

1. On the **Registry permissions** page, choose **Generate statement**.

1. Complete the following steps to define your policy statement using the policy generator.

   1. For **Policy type**, choose **Replication - cross account**.

   1. For **Statement id**, enter a unique statement ID. This field is used as the `Sid` on the registry policy.

   1. For **Accounts**, enter the account IDs for each account you want to grant permissions to. When specifying multiple account IDs, separate them with a comma.

1. Choose **Save**.

## To configure a permissions policy for replication (AWS CLI)
<a name="registry-permissions-create-cli"></a>

1. Create a file named `registry_policy.json` and populate it with a registry policy.

------
#### [ JSON ]

****  

   ```json
   {
       "Version":"2012-10-17",		 	 	 
       "Statement":[
           {
               "Sid":"ReplicationAccessCrossAccount",
               "Effect":"Allow",
               "Principal":{
                   "AWS":"arn:aws:iam::{{111122223333}}:{{root}}"
               },
               "Action":[
                   "ecr:CreateRepository",
                   "ecr:ReplicateImage"
               ],
               "Resource": [
                   "arn:aws:ecr:us-west-2:{{444455556666}}:repository/{{*}}"
               ]
           }
       ]
   }
   ```

------

1. Create the registry policy using the policy file.

   ```
   aws ecr put-registry-policy \
         --policy-text file://{{registry_policy.json}} \
         --region {{us-west-2}}
   ```

1. Retrieve the policy for your registry to confirm.

   ```
   aws ecr get-registry-policy \
         --region {{us-west-2}}
   ```