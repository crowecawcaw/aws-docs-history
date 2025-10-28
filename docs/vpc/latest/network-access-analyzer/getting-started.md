# Getting started with Network Access Analyzer

You can use Network Access Analyzer to understand network access to resources in your virtual private clouds
(VPCs). You can get started with Network Access Analyzer using one of the Amazon created Network Access
Scopes.

###### Tasks

- [Step 1: Analyze your network](#run-analysis "#run-analysis")
- [Step 2: Review your findings](#view-results "#view-results")
- [Step 3: Delete a Network Access Scope (Optional)](#delete-scope "#delete-scope")

###### Note

Network Access Analyzer evaluates network paths only within the account and Region from which you run the
analysis.

## Step 1: Analyze your network

To get started quickly, use one of the Network Access Scopes provided by Amazon
or create a Network Access Scope using a built-in template. Note that it can take a
few minutes to complete the analysis.

###### To analyze a Network Access Scope

1. Open the Network Manager console at
   [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. In the navigation pane, choose **Network Access Analyzer**.
3. If you are using Network Access Analyzer for the first time, choose **Get Started**.
4. Select one of the Amazon created Network Access Scopes:
   - **All-IGW-Ingress (Amazon created)** – Identifies inbound paths
     from internet gateways to network interfaces.
   - **AWS-IGW-Egress (Amazon created)** – Identifies outbound paths
     from network interfaces to internet gateways.
   - **AWS-VPC-Ingress (Amazon created)** – Identifies inbound paths
     from internet gateways, peering connections, VPC endpoints, VPNs, and transit gateways to
     VPCs.
   - **AWS-VPC-Egress (Amazon created)** – Identifies outbound paths
     from VPCs to internet gateways, peering connections, VPC endpoints, VPNs, and transit
     gateways.

5. Choose **Analyze**.
6. Wait for the analysis to complete and then go to [Step 2: Review your findings](#view-results "#view-results").

Alternatively, you can get started by creating a Network Access Scope using a built-in
template or an empty template.

###### To create a Network Access Scope

1. Open the Network Manager console at
   [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. In the navigation pane, choose **Network Access Analyzer**.
3. Choose **Create Network Access Scope**.
4. Select a built-in template and then choose **Next**.
5. (Optional) Add a [match condition](match-paths.md "match-paths.md").
6. (Optional) Add an [exclusion condition](exclude-paths.md "exclude-paths.md").
7. (Optional) To add a tag, choose **Add new tag** and then enter the tag
   key and tag value.
8. Choose **Next** and then choose **Create Network Access Scope**.
9. Select your Network Access Scope and choose **Analyze**. Wait for
   the analysis to complete and then go to [Step 2: Review your findings](#view-results "#view-results").

## Step 2: Review your findings

After your analysis is complete, you can review the results.

###### To review your findings

1. Choose the **Latest analysis** tab. If the analysis produces any findings,
   **Last analysis result** is **Findings detected**, as shown
   in the following figure. Otherwise, **Last analysis result** is **No
   findings detected**.

![Network Access Scope analysis result](images/analysis-result.png) 2. If there are findings detected, the **Findings** pane has the potential
network paths identified by the Network Access Scope. You can add filters based on the resources
present in the findings. For example, you can filter by resource type. 3. Select a finding to view its details. This information helps you understand the network
configurations that produced the finding. For example, you can see the network ACL that applies
to traffic that is destined for the internet.

![Network Access Scope analysis findings details](images/findings.png)

## Step 3: Delete a Network Access Scope (Optional)

If you no longer need a Network Access Scope, you can delete it. This action can't be
undone.

###### To delete a Network Access Scope

1. On the Network Access Scopes page, select the check box next to the Network Access Scope.
2. Choose the **Actions** button and then choose **Delete Network
   Access Scope**.
3. When prompted for confirmation, enter `Delete`.
4. Choose **Delete**.
