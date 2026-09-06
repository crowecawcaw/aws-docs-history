

# Amazon SimpleDB Glossary
<a name="Glossary"></a>

**account**<a name="glossary_Account"></a>  
AWS account associated with a particular developer.

**attribute**<a name="glossary_Attribute"></a>  
Similar to columns on a spreadsheet, attributes represent categories of data that can be assigned to items.

**consistent read**<a name="glossary_ConsistentRead"></a>  
 A consistent read (using Select or GetAttributes with ConsistentRead=true) returns a result that reflects all writes that received a successful response prior to the read. 

**domain**<a name="glossary_Domain"></a>  
All Amazon SimpleDB information is stored in domains. Domains are similar to tables that contain similar data. You can execute queries against a domain, but cannot execute joins between domains.   
The name of the domain must be unique within the customer account. 

**eventually consistent read**<a name="glossary_EventualConsistency"></a>  
 An eventually consistent read (using Select or GetAttributes) might not reflect the results of a recently completed write (using PutAttributes, BatchPutAttributes, DeleteAttributes). Consistency is usually reached within a second; repeating a read after a short time should return the updated data. 

**exponential backoff**<a name="glossary_ExponentialBackoff"></a>  
 A strategy for reducing the load on the system and increasing the likelihood of repeated requests succeeding by incrementally decreasing the rate at which retries are executed. For example, client applications might wait up to 400 milliseconds before attempting the first retry, up to 1600 milliseconds before the second, up to 6400 milliseconds (6.4 seconds) before the third, and so on. 

**items**<a name="glossary_Items"></a>  
Similar to rows on a spreadsheet, items represent individual objects that contain one or more value-attribute pairs

**item name**<a name="glossary_ItemName"></a>  
An identifier for an item. The identifier must be unique within the domain.

**machine utilization**<a name="glossary_MachineUtilization"></a>  
Charges based on the amount of machine capacity used to complete the particular request (SELECT, GET, PUT, etc.), normalized to the hourly capacity of a circa 2007 1.7 GHz Xeon processor. Machine Utilization is measured in Machine Hour increments. 

**multi-valued attribute**<a name="glossary_MultiValuedAttribute"></a>  
An attribute with more than one value. 

**network partition**<a name="glossary_NetworkPartition"></a>  
A rare error condition where some Amazon SimpleDB computers cannot contact each other, but all other components are operating correctly. Normally this is repaired within seconds or minutes. 

**single-valued attribute**<a name="glossary_SingleValuedAttribute"></a>  
An attribute with one value.

**value**<a name="glossary_Value"></a>  
Similar to cells on a spreadsheet, values represent instances of attributes for an item. An attribute might have multiple values.