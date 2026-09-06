

# Deploy an AWS Cloud WAN core network policy version
<a name="cloudwan-policy-version-deploy"></a>

fter creating a version of a policy, you can deploy the policy version as your new **LIVE** policy. Deploying a new policy version never occurs automatically. 

**To implement a core policy version**

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home).

1. Under **Connectivity**, choose **Global Networks**.

1. On the **Global networks** page, choose the global network ID.

1. In the navigation pane, choose **Core network**, and then choose **Policy versions**.

1. On the **Policy versions** page, choose the policy that you want to deploy.

1. Choose **View or apply change set**.

1. (Optional) Do either of the following: 
   + To review the proposed changes to the policy, choose **Details** in the **New values** column.
   + To review the values of the original policy, choose **Details** in the **Previous values** column.

1. Choose **Apply change set** to deploy the policy to become the new LIVE policy.

1. On the Policy versions page, the status of the policy deployment is **Executing policy**. 

1. To view the deployment details and progress, choose the policy link. The **Policy version - X ** page appears. 
   + The **Policy details** page displays information about the policy that you're deploying.
   + The **JSON** page displays policy information as a JSON file.
   + The **Execution progress** page displays the status of the policy deployment. You can view all events related to the deployment or you can view specific events. For example, you might want to view the deployment status of core network edges.

1. When finished, the **Alias** changes to **LIVE/LATEST** and the **Change set state** changes to **Execution succeeded**. The **Change set state** of any previous policies that were in a **Ready to execute** change set state change to **Out of date**. This indicates that those policies are now considered older than the current LIVE policy.