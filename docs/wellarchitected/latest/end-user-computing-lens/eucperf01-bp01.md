

# EUCPERF01-BP01 Check Regional support for the required EUC services
<a name="eucperf01-bp01"></a>

 Not all AWS regions support EUC services such as WorkSpaces Applications, WorkSpaces and WorkSpaces Secure Browser. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Check to see if the relevant AWS EUC service is available in your most proximal Region. If the required service is not available in this Region, check to be sure that you can deliver the required performance from the Region closest to you or with lowest latency. For information on EUC Regional support, see: 
+  [WorkSpaces Regional Support](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html) 
+  [WorkSpaces Applications Regional Support](https://www.aws-services.info/appstream.html) 
+  [WorkSpaces Secure Browser Regional Support](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html) 

 The [WorkSpaces Connection Health Checker](https://clients.amazonworkspaces.com/Health.html) details the latency between a specific endpoint device and the WorkSpaces service running in each available Region. This data is also a good indicator of latency for WorkSpaces Secure Browser and WorkSpaces Applications if they are running in the same Region. 