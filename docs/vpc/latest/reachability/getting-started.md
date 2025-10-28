# Getting started with Reachability Analyzer

You can use Reachability Analyzer to determine whether a destination resource in your virtual private cloud
(VPC) is reachable from a source resource. To get started, you specify a source and a destination.
For example, you can run a reachability analysis between two network interfaces or between a
network interface and a gateway. If there is a reachable path between the source and destination,
Reachability Analyzer displays the details. Otherwise, Reachability Analyzer identifies the blocking component.

###### Tasks

- [Step 1: Create and analyze a path](#create-path "#create-path")
- [Step 2: Include or exclude intermediate resources](#path-filters "#path-filters")
- [Step 3: View the results of the path analysis](#view-results "#view-results")
- [Step 4: Change the network configuration and analyze the path](#analyze-path "#analyze-path")
- [Step 5: Delete the path](#delete-path "#delete-path")

## Step 1: Create and analyze a path

Specify the path for the traffic from a source to a destination. After you create the path,
Reachability Analyzer analyzes the path once. You can analyze a path at any time to determine whether your
intended connectivity is supported, even as your network configuration changes.

###### To create a path

1. Open the Network Manager console at
   [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. In the navigation pane, choose **Reachability Analyzer**.
3. Choose **Create and analyze path**.
4. (Optional) For **Name tag**, enter a descriptive name for the
   analysis.
5. To specify the source resource, choose the resource type from **Source
   type**, and then choose the specific resource from
   **Source**.

(Optional) You can filter the scope of the result based on the packet header leaving the
source resource. For example, use the source and destination IP addresses and ports of
interest. By default, the analysis considers all combinations of IP addresses and ports. 6. To specify the destination resource, choose the resource type from **Destination
type**, and then choose the specific resource from
**Destination**.

(Optional) You can filter the scope of the result based on the packet header arriving at
the destination resource. For example, use the source and destination IP addresses and ports of
interest. By default, the analysis considers all combinations of IP addresses and ports. 7. For **Protocol**, choose **TCP** or
**UDP**. 8. (Optional) To add a tag, choose **Add new tag** and then enter the tag
key and tag value. 9. Choose **Create and analyze path**.

## Step 2: Include or exclude intermediate resources

Reachability Analyzer supports the ability to include or exclude intermediate resources from
analysis.

- Including a specified intermediate component makes it particularly valuable for security
  audits, policy enforcement, and compliance verification in cloud environments and enterprise
  networks. While this provides granular control over path analysis, note that it will only show
  paths that _include_ the specified intermediate component,
  requiring good knowledge of the network topology for effective use.
- Excluding an intermediate component removes that component from analysis. This makes it
  particularly valuable when you don't want your analysis to include a particular component. For
  example, you might have a path that runs through AWS Network Firewall, but you only want to analyze paths
  that bypass it. In this case, you would add the Network Firewall ARN to the exclude field.
  Reachability Analyzer will then ignore this resource and analyze only those paths that don't go
  through it.

###### To include or exclude intermediate resources

1. Choose the checkbox for the path that you want to include or exclude Amazon Resource
   Numbers (ARNs) for.
2. On the **Analysis path** panel, enter an optional ARN for either of the
   following:
   - **Include an intermediate component feature**

   The analyzer only considers paths that include the specified intermediate
   component.
   - **Exclude an intermediate component feature**

   The analyzer ignores a specific intermediate component during analysis and only analyzes
   alternate paths.

###### Note

You can only include a single ARN to include or exclude from analysis. Each ARN must be
unique in order to prevent a conflict. 3. Choose **Confirm**.

## Step 3: View the results of the path analysis

After the path analysis completes, you can view the result of the analysis.

###### To view the results of the path analysis

1. Choose the ID of the path in the **Path ID** column to view the path details page.
2. In the **Analysis explorer** panel, find **Reachability status**
   and check whether it is **Reachable** or **Not reachable**. If the
   path is reachable, the console displays the shortest route found between the source and destination.
   Otherwise, expand **Explanations**, **Details** for information
   about the blocking component.
3. If the reachability status matches your intent, there is no further action required. Consider
   running the analysis again if you change your network configuration so that you can ensure that
   the reachability status still matches your intent. Otherwise, proceed to [Step 3](#analyze-path "#analyze-path").

## Step 4: Change the network configuration and analyze the path

If the reachability status does not match your intent, you can change your network
configuration. Then you can analyze the path again to confirm that the reachability status
matches your intent.

###### To restore connectivity for a path that is not reachable

1. The **Analysis explorer** panel includes an [explanation code](explanation-codes.md "explanation-codes.md") and detailed information about the
   component or combination of components that is blocking the path (under
   **Explanations**, **Details**). For example, in the
   following explanation, a security group is missing a required inbound rule.

![Example explanation details](images/unreachable-path.png) 2. Update the configuration of the component so that the desired traffic can traverse the component. 3. Choose **Analyze path** to confirm that the path is now reachable. You
can optionally specify the Amazon Resource Name (ARN) of a resource that the path must
traverse.

###### To remove connectivity for a reachable path

1. The **Analysis explorer** panel includes a visual representation of the
   shortest route found between the source and destination. It includes all components between the
   source and destination. For example, the following diagram shows the components that traffic
   traverses from the source internet gateway to the destination EC2 instance.

![Example visual representation of a reachable path](images/reachable-path.png) 2. Identify the component that is overly permissive and update its configuration. 3. Choose **Analyze path** to confirm that the path is no longer
reachable.

## Step 5: Delete the path

If you no longer need the path, you can delete it. When you delete a path, you also delete
all its analyses. If you keep the path, note that Reachability Analyzer will automatically delete the analysis 120
days after its creation date.

###### To delete the path

1. Open the Network Manager console at
   [https://console.aws.amazon.com/networkmanager/home](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home").
2. In the navigation pane, choose **Reachability Analyzer**.
3. Select the path.
4. Choose **Actions**, **Delete path**.
5. When prompted for confirmation, choose **Delete path**.
