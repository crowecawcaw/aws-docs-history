

# EUCPERF01-BP02 Consider the requirements of your Availability Zones when architecting your AWS EUC services
<a name="eucperf01-bp02"></a>

 Within each Region, only select Availability Zones support each AWS EUC service. This is important if you are architecting solutions with extreme performance or security requirements that demand that applications and desktops reside on the same subnet as the user data they need to access. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-1"></a>

 For the WorkSpaces service line, explore the Availability Zone information. 
+  [Amazon WorkSpaces Availability Zone Support](https://docs.aws.amazon.com/workspaces/latest/adminguide/azs-workspaces.html) 
+  [Amazon WorkSpaces Secure Browser](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html) 

 For WorkSpaces Applications, selecting a subnet when creating a new fleet automatically checks if the associated Availability Zone can support the requested requirements, which are based on several criteria such as instance type and availability. 