# Adding an existing Amazon EMR on EC2 cluster in Amazon SageMaker Unified Studio

As a data worker, you can make use of Amazon EMR on EC2 by adding existing or new Amazon EMR on EC2
clusters as compute instances to a project in the Amazon SageMaker Unified Studio Studio. Within a project, you can
use both existing and new Amazon EMR on EC2 clusters.

Before you can connect to an Amazon EMR on EC2 cluster, you must complete the following prerequisites:

- Your Amazon SageMaker Unified Studio admin must enable blueprints. On-demand
  creation isn't supported for Amazon EMR on EC2 in quick setup. In addition, if you are connecting to an Amazon EMR on EC2 cluster that is not runtime-role enabled,
  the admin must configure specific blueprints as described in the section below.
- You must have a project created in Amazon SageMaker Unified Studio. If you are connecting to an Amazon EMR on EC2 cluster that is not runtime-role enabled, you must create a project that includes specific blueprint configurations in the project profile.
- The admin that owns the Amazon EMR resource you want to connect to must complete a set of prerequisite steps to grant you access to the resource.
  More details on each of these steps is found in the sections below.

## Prerequisite steps for you and your Amazon SageMaker Unified Studio admin

Amazon EMR on EC2 clusters can be runtime-role enabled or not runtime-role enabled. You can connect
to both kinds of Amazon EMR on EC2 clusters in Amazon SageMaker Unified Studio. However, to use clusters that are not
runtime-role enabled, you and your Amazon SageMaker Unified Studio admin must prepare to use a project with specific configurations.

###### Note

If you are connecting to clusters that are runtime-role enabled, you can proceed
to the section for prerequisite steps for Amazon EMR admins without completing the steps in this section.

- You can use runtime-role enabled clusters to specify different IAM roles for individual jobs or steps within a cluster,
  with fine-grained access control tailored to specific job needs.
- Clusters that are not runtime-role enabled have limited granular access control for jobs.
  Instead, all jobs on the cluster use the same set of permissions.

Amazon EMR clusters with runtime roles enabled are considered more secure because they allow for fine-grained access control at the job level, meaning each individual job
running on the cluster can be assigned a specific IAM role with only the necessary
permissions to access the data and resources it needs.

To prepare to use clusters that are not runtime-role enabled, complete the following additional steps:

###### Note

Amazon EMR clusters that are not runtime-role enabled must have in-transit encryption enabled in order to be connected to
Amazon SageMaker Unified Studio. To ensure that the Amazon EMR cluster meets this requirement, verify with your Amazon EMR admin that the cluster
has a security configuration with in-transit encryption enabled. For more information, see
[Create a security configuration with the Amazon EMR console or with the AWS CLI](../../../emr/latest/ManagementGuide/emr-create-security-configuration.md "../../../emr/latest/ManagementGuide/emr-create-security-configuration.md")
in the Amazon EMR Management Guide.

1. The Amazon SageMaker Unified Studio admin must configure the tooling configurations in the blueprints for a project profile so that
   **allowConnectionToUserGovernedEmrClusters** is set to **True** in the Amazon SageMaker Unified Studio management console.
   For more information, see the Amazon SageMaker Unified Studio Administrator Guide.
2. You create a project using the project profile that your admin modified in step 1.

For more information about runtime roles, see [Runtime roles for Amazon EMR steps](../../../emr/latest/ManagementGuide/emr-steps-runtime-roles.md "../../../emr/latest/ManagementGuide/emr-steps-runtime-roles.md")
in the Amazon EMR Management Guide.

###### Note

For clusters without runtime roles, Amazon SageMaker Unified Studio cannot provide governance on the clusters, and applications running on these clusters will not be isolated between projects or honor fine-grained access control based on project data permissions.

Additionally, all project resources are inaccessible to the cluster unless additional permissions are granted to the IAM instance profile role attached to the Amazon EC2 instance.

## Prerequisite steps for Amazon EMR admins

Before you can add an existing Amazon EMR on EC2 resource to your project in Amazon SageMaker Unified Studio,
the admin that owns that resource must grant access to you by completing the following steps:

###### Create an Amazon EMR access role with a trust policy

1. Get the project role ARN and project ID for the Amazon SageMaker Unified Studio project that you want to grant access to.
   Project members can get the project role ARN and project ID from the **Project overview** page in their project.

###### Note

If the Amazon SageMaker Unified Studio project uses a different VPC than the Amazon EMR on EC2 cluster you want to grant access to, you must also get the project VPC information from the project member and complete additional steps to connect the VPCs.
For more information, see [VPC to VPC connectivity](../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.md "../../../whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/vpc-to-vpc-connectivity.md") and [Connect VPCs using VPC peering](../../../vpc/latest/userguide/vpc-peering.md "../../../vpc/latest/userguide/vpc-peering.md"). 2. Make sure that the EMR cluster you want to grant access to has an instance profile role with the `sts:AssumeRole` permission on the runtime role.
For more information, see [Runtime roles for Amazon EMR steps](../../../emr/latest/ManagementGuide/emr-steps-runtime-roles.md#configure-ec2-profile "../../../emr/latest/ManagementGuide/emr-steps-runtime-roles.md#configure-ec2-profile")
in the Amazon EMR Management Guide. 3. Go to the AWS IAM console. 4. On the Roles page, choose **Create role**. 5. Choose **Custom trust policy**. 6. Enter information for the trust policy as shown in the example below, and edit it according to the project information you received in step 1.

    * Change `project-role-arn` to be the project role ARN you received from the Amazon SageMaker Unified Studio project member.
    * Change `project-id` to be the project ID you received from the Amazon SageMaker Unified Studio project member.

7. Choose **Next**.
8. Under **Role name**, enter a name for the role.
9. (Optional) Enter a description for the role.
10. Choose **Create role**.

###### Attach permissions to the role

1. Select the role you have created in the AWS IAM console.
2. Choose **Add permissions** > **Create inline policy**.
3. Enter information as shown in the example below, and edit it according to the information for your Amazon EMR clusters that you want to grant access to.
   - Change the EMR cluster ARN to be the ARN for the cluster.
     You can find this on the cluster details page in the Amazon EMR console by selecting the cluster ID of the cluster that you want to share.

   ###### Note

   You can use an asterisk instead of the Amazon EMR cluster ID if you want to grant access to all clusters instead of just one.
   - Change the certificate path to the one defined in the Amazon EMR security configuration for that cluster in the Amazon EMR console.
     For more information, see [Specify a security configuration for an Amazon EMR cluster](../../../emr/latest/ManagementGuide/emr-specify-security-configuration.md "../../../emr/latest/ManagementGuide/emr-specify-security-configuration.md")
     in the Amazon EMR Management Guide.

4. Choose **Next**.
5. Under **Policy name**, enter a name for the polciy.
6. Choose **Create policy**. You can then see the permissions policy listed on the page for the role you created in the IAM console.

###### Send information to project members

1. Copy the ARN of the EMR access role you created in the IAM console and send it to the Amazon SageMaker Unified Studio project member you want to grant access to.
2. Copy the Amazon EMR cluster ARN that you added to the permissions policy and send it to the Amazon SageMaker Unified Studio project member you want to grant access to.
3. From the Amazon EMR on EC2 cluster details page in the Amazon EMR console, copy the EC2 instance profile string
   and search for it on the Roles page in the IAM console to find the role that contains the Amazon EC2 instance profile ARN.
4. Select the name of the role that contains the instance profile ARN to open the role details page, then copy the ARN and send it to
   the Amazon SageMaker Unified Studio project member you want to grant access to.

After the Amazon EMR admin has completed these steps, project members are able to add a connection to the Amazon EMR on EC2 cluster as a compute resource in Amazon SageMaker Unified Studio.

## Adding the Amazon EMR on EC2 compute resource

1. From inside the project management view in Amazon SageMaker Unified Studio, select **Compute** from the navigation bar.
2. On the Compute page, select the **Data processing** tab.
3. Choose **Add compute**, then choose **Connect to existing compute resources**.
4. In the **Add compute** modal, you can select the type of compute resource you would like to add
   to your project. Select **EMR on EC2 cluster**.
5. To add a connection to an existing Amazon EMR on EC2 cluster, you must have the correct permissions to access the Amazon EMR
   on EC2 cluster. You can select the **Copy project information** button to copy the data
   that the Amazon EMR admin will need to grant the data worker access. If you haven't already, send the project role ARN and the project ID to your
   admin.

###### Note

The Amazon EMR admin will also need the project ID, which is the penultimate string in the project ARN.
To view and copy the project ID, go to the **Project overview** page of your project. 6. After the account administrator has granted you access according to the prerequisite steps above, you can specify the ARNs
associated with the cluster. You must fill in the **Access role ARN**, **EMR on EC2 cluster
ARN**, **Compute name**, and the **Instance profile role ARN**. 7. Choose **Add compute**. Your Amazon EMR on EC2 instance is then added to your
project.

After you have added a cluster to a project, you are able to see the cluster in the
list on the **Data processing** tab in the Compute panel. You can then view the cluster details by
selecting the cluster you want.
