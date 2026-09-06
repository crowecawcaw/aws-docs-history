

# Limitations
<a name="monday-connector-limitations"></a>

The following are limitations for the Monday connector:
+  The dynamic metadata response has certain conflicts with the documentation as mentioned below: 
  +  Group, Column entity supports filter operations, but it is not present in the dynamic metadata endpoint, hence it's kept as non-filterable entity. 
  +  The dynamic endpoint consists of around 15000\+ lines and returns metadata of all the entities in a single response, because of this the fields are taking an average of 10 seconds to load hence, this would require some additional time while running a job. 
  +  Refer the below table for Monday rate limit. The significant size of the dynamic entity's response data causes a noticeable delay, with fields requiring an average of 10 seconds to load.     
<a name="monday-rate-limit-table"></a>[See the AWS documentation website for more details](http://docs.aws.amazon.com/glue/latest/dg/monday-connector-limitations.html)