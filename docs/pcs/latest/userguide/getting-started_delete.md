# Delete your AWS resources for AWS PCS

After you are done with the cluster and node groups that you created for this tutorial, you
should delete the resources that you created.

###### Important

You get billing charges for all resources running in your AWS account

###### To delete AWS PCS resources that you created for this tutorial

- Open the [AWS PCS console](https://console.aws.amazon.com/pcs/home#/clusters "https://console.aws.amazon.com/pcs/home#/clusters").
- Navigate to the cluster named **get-started**.
- Navigate to the **Queues** section.
- Select the queue named **demo**.
- Choose **Delete**.

###### Important

Wait until the queue has been deleted before proceeding.

- Navigate to the **Compute node groups** section.
- Select the compute node group named **compute-1**.
- Choose **Delete**.
- Select the compute node group named **login**.
- Choose **Delete**.

###### Important

Wait until both compute node groups have been deleted before proceeding.

- In the cluster detail page for **get-started**, choose
  **Delete**.

###### Important

Wait until the cluster has been deleted before proceeding with subsequent steps.

###### To delete other AWS resources you created for this tutorial

- Open the [IAM console](https://console.aws.amazon.com/iam "https://console.aws.amazon.com/iam").
  - Choose **Roles**.
  - Select the role named **AWSPCS-getstarted-role** then choose
    **Delete**.
  - After the role has been deleted, choose **Policies**.
  - Select the policy named **AWSPCS-getstarted-policy** then choose
    **Delete**.

- Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
  - Select the stack named **getstarted-lt**.
  - Choose **Delete**.

  ###### Important

  Wait for the stack to delete before proceeding.

- Open the [Amazon EFS console](https://console.aws.amazon.com/efs "https://console.aws.amazon.com/efs").
  - Choose **File systems**.
  - Select the file system named **getstarted-efs**.
  - Choose **Delete**.

  ###### Important

  Wait for the file system to delete before proceeding.

- Open the [Amazon FSx console](https://console.aws.amazon.com/fsx "https://console.aws.amazon.com/fsx").
  - Choose **File systems**.
  - Select the file system named **getstarted-fsx**.
  - Choose **Delete**.

  ###### Important

  Wait for the file system to delete before proceeding.

- Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
  - Select the stack named **getstarted-sg**.
  - Choose **Delete**.

- Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation").
  - Select the stack named **hpc-networking**.
  - Choose **Delete**.
