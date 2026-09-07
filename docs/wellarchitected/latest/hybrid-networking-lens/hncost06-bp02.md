

# HNCOST06-BP02 Separate traffic classes for dedicated connections
<a name="hncost06-bp02"></a>

 Create multiple dedicated connections for distinct traffic classes such as production versus backups. Assign guaranteed bandwidth to critical dedicated connections and use best-effort routing for dedicated connections. 

 **Desired outcome:** Cost-effective traffic segregation with guaranteed SLAs for priority workloads. 

 **Level of risk exposed if this best practice is not established:** Low 

 **Benefits of establishing this best practice:** 
+  Simplifies cost allocation by traffic type 
+  Enables independent scaling of traffic classes 
+  Complies with network isolation requirements 

## Implementation guidance
<a name="implementation-guidance-57"></a>
+  Configure separate BGP communities for dedicated connection. For example, you can achieve this using AWS Direct Connection VIFs on dedicated connections. 

### Resources
<a name="resources-47"></a>
+  [Direct Connect virtual interfaces](https://docs.aws.amazon.com/directconnect/latest/UserGuide/create-vif.html) 