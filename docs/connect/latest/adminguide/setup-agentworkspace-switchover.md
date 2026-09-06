

# Set up Connect Customer Agent Workspace to support agents shifting across AWS Regions
<a name="setup-agentworkspace-switchover"></a>

Perform the following steps to enable Connect Customer Agent Workspace to embed the Contact Control Panel from the replica AWS Region to the source Region, and shift between them as agent's active Region changes.

If you have not yet created a replica of your source Connect Customer instance or set up a traffic distribution group, see [Get started with Connect Customer Global Resiliency](get-started-connect-global-resiliency.md). 

1. Go to the AWS Connect Customer console to retrieve the **Access URL** for your source instance. Make a note of the URL. 

1. In the replica Region, AWS Connect Customer console to retrieve the **Access URL** for your replica instance. Make a note of the URL. 

1. In the same window for your replica Connect Customer instance, in the left pane choose **Approved origins**.

1. Add domain for source instance **Access URL**, which you noted in step 1.
**Note**  
Do not include a trailing **/** in the access URL.

1. Repeat the above steps on your source instance: Go to **Approved origins**, add the access URL for the replica instance. 

**Note**  
Agents must set their status to **Available** after they are shifted across Regions.