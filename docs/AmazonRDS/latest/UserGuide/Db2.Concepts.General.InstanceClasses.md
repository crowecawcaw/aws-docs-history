

# Amazon RDS for Db2 instance classes
<a name="Db2.Concepts.General.InstanceClasses"></a>

The computation and memory capacity of a DB instance is determined by its instance class. The DB instance class you need depends on your processing power and memory requirements.



## Supported RDS for Db2 instance classes
<a name="Db2.Concepts.InstanceClasses.Supported"></a>

The supported Amazon RDS for Db2 instance classes are a subset of the Amazon RDS DB instance classes. For the complete list of Amazon RDS instance classes, see [DB instance classes](Concepts.DBInstanceClass.md).

**Topics**
+ [Supported RDS for Db2 instance classes for Db2 Advanced Edition](#Db2.Concepts.InstanceClasses.Supported.AE)
+ [Supported RDS for Db2 instance classes for Db2 Community Edition](#Db2.Concepts.InstanceClasses.Supported.CE)
+ [Supported RDS for Db2 instance classes for Db2 Standard Edition](#Db2.Concepts.InstanceClasses.Supported.SE)

### Supported RDS for Db2 instance classes for Db2 Advanced Edition
<a name="Db2.Concepts.InstanceClasses.Supported.AE"></a>

The following table lists all instance classes supported for the Db2 Advanced Edition. These instance classes are available for both bring your own license (BYOL) and Db2 license through AWS Marketplace.


| Instance class type | Instance class | 
| --- | --- | 
| General purpose instance classes with 3rd generation Intel Xeon Scalable processors, SSD storage, and network optimization | db.m6idn.large–db.m6idn.32xlarge | 
| General purpose instance classes powered by 3rd generation Intel Xeon Scalable processors | db.m6in.large–db.m6in.32xlarge | 
| General purpose instance classes | db.m6i.large–db.m7i.48xlarge<br />db.m7i.large–db.m7i.48xlarge | 
| Memory optimized instance classes with local NVMe-based SSDs, powered by 3rd generation Intel Xeon Scalable processors | db.x2iedn.xlarge–db.x2iedn.32xlarge | 
| Memory optimized instance classes powered by 3rd generation Intel Xeon Scalable processors | db.r6idn.large–db.r6idn.32xlarge<br />db.r6in.8xlarge–db.r6in.32xlarge | 
| Memory optimized instance classes | db.r6i.large–db.r7i.48xlarge<br />db.r7i.large–db.r7i.48xlarge | 
| Burstable performance instance classes | db.t3.small–db.t3.2xlarge | 

### Supported RDS for Db2 instance classes for Db2 Community Edition
<a name="Db2.Concepts.InstanceClasses.Supported.CE"></a>

The following table lists all instance classes supported for the Db2 Community Edition. These instance classes are available for bring your own license (BYOL) only.


| Instance class type | Instance class | 
| --- | --- | 
| General purpose instance classes | db.m6i.large, db.m7i.large | 
| Burstable performance instance classes | db.t3.small–db.t3.large | 

General purpose instance classes might not be available in all AWS Regions. To determine instance class support in a specific Region, see [Determining DB instance class support in AWS Regions](Concepts.DBInstanceClass.RegionSupport.md).

### Supported RDS for Db2 instance classes for Db2 Standard Edition
<a name="Db2.Concepts.InstanceClasses.Supported.SE"></a>

The following table lists all instance classes supported for the Db2 Standard Edition. These instance classes are available for both bring your own license (BYOL) and Db2 license through AWS Marketplace.


| Instance class type | Instance class | 
| --- | --- | 
| General purpose instance classes with 3rd generation Intel Xeon Scalable processors, SSD storage, and network optimization | db.m6idn.large–db.m6idn.8xlarge | 
| General purpose instance classes powered by 3rd generation Intel Xeon Scalable processors | db.m6in.large–db.m6in.8xlarge | 
| General purpose instance classes | db.m7i.large–db.m7i.8xlarge<br />db.m6i.large–db.m6i.8xlarge | 
| Memory optimized instance classes with local NVMe-based SSDs, powered by 3rd generation Intel Xeon Scalable processors | db.x2iedn.xlarge | 
| Memory optimized instance classes powered by 3rd generation Intel Xeon Scalable processors | db.r6idn.large–db.r6idn.4xlarge<br />db.r6in.large–db.r6in.4xlarge | 
| Memory optimized instance classes | db.r7i.large–db.r7i.8xlarge<br />db.r6i.large–db.r6i.4xlarge | 
| Burstable performance instance classes | db.t3.small–db.t3.2xlarge | 