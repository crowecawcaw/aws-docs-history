

# Optimize data and processing

 Efficient data management and processing affect sustainability by reducing unnecessary storage and computational requirements. Implement data lifecycle policies to eliminate redundant or obsolete data. Select file formats and compression techniques that minimize storage while maintaining functionality. Design distributed systems thoughtfully, placing processing close to data and optimizing resource use across your architecture. 


|  SUS04: How do you manage data and processing to minimize resource use?  | 
| --- | 
|  [SUS04-BP01 Eliminate unnecessary data](sus04-bp01.md)  | 
|  [SUS04-BP02 Select appropriate file formats, compression, and software implementation](sus04-bp02.md)  | 
|  [SUS04-BP03 Implement distributed systems appropriately](sus04-bp03.md)  | 

## Capability intent
<a name="sus04-intent"></a>
+  Only data that serves a current business purpose is retained, with every data set assigned an owner and a retention period, and lifecycle rules that archive or delete data as it ages. 
+  File formats and compression match the access pattern, so storage, transport, and processing use the minimum resources needed for transactional, analytical, or archival data. 
+  Processing code favors efficient algorithms and libraries, and processes only the data a question requires rather than scanning everything by default. 
+  Distributed systems place components close to the data they use, communicate no more chattily than needed, and are only as distributed as the workload genuinely requires. 
+  Network topology reflects the data flows, minimizing cross-Availability Zone and cross-Region traffic. 

## Common issues to watch for
<a name="sus04-issues"></a>
+  Data is stored indefinitely with no owner or purpose, so redundant, obsolete, trivial, and dark data accumulates unnoticed and spreads across replication and backups. 
+  Retention periods are set by habit rather than business value or regulatory need, and a one-time purge without automation lets the waste return within months. 
+  General-purpose formats such as CSV or JSON are used for all data, so analytical queries scan whole rows and structured data moves across the network more verbosely than it needs to. 
+  One compression algorithm is applied everywhere, either wasting storage on cold data or wasting processor cycles decompressing hot data on every read. 
+  Simple or low-volume workloads run on elaborate distributed designs whose network calls, serialization, and coordination cost more resources than the distribution saves. 
+  Systems move large data volumes to a central processor instead of moving computation to the data, and communicate synchronously where an asynchronous pattern would remove idle waiting. 