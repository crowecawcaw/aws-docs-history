

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Size cluster functions independently with deployment configurations
<a name="influxdb3-deployment-configuration"></a>

 An InfluxDB 3 Enterprise cluster does four things: it ingests writes, serves queries, runs processing engine plugins, and compacts data. Each of those has a different appetite for CPU and memory. Compaction is bursty and memory-hungry; query serving scales with concurrency; ingest scales with write throughput. 

 A *deployment configuration* lets you size each function separately. You declare groups of nodes, and each group gets its own instance type, its own node count, and its own set of functions. Because the groups can differ in size, the resulting cluster is *heterogeneous*, such as a large dedicated compactor alongside small query nodes instead of paying for the largest instance type across every node. 

 You set the shape with the `--deployment-configuration` parameter on `create-db-cluster`, and you change it later with the same parameter on `update-db-cluster`. 

**Note**  
 Deployment configurations apply to Timestream for InfluxDB 3 Enterprise clusters. They replace the cluster topology that previously lived in a DB parameter group. See [Deployment configurations and parameter groups](#influxdb3-depcfg-parameter-groups). Clusters you already created with parameter-group topology keep running unchanged. 

## Node groups
<a name="influxdb3-depcfg-node-groups"></a>

 A deployment configuration is a list of *node groups*. Every group declares three things: 

`instanceModes`  
 The functions that the nodes in this group perform, in any combination of `INGEST`, `QUERY`, `PROCESS`, and `COMPACT`. A node can perform several functions at once (`["INGEST","QUERY"]`) or exactly one (`["COMPACT"]`). 

`instanceType`  
 The `db.influx.*` instance type for this group. Groups can specify different instance types. This is what makes a cluster heterogeneous. For the available sizes, see [Supported Instance Types and Specifications](supported-instance-types.md). 

`count`  
 The number of nodes in the group. 

 The four functions map onto cluster behavior as follows: 


**InfluxDB 3 Enterprise instance modes**  

|  **Mode**  |  **What the node does**  | 
| --- | --- | 
|  INGEST  |  Accepts writes. Nodes with this mode back the cluster's writer endpoint.  | 
|  QUERY  |  Serves read queries. Nodes that have QUERY but not INGEST back the cluster's reader endpoint.  | 
|  PROCESS  |  Runs [processing engine](processing-engine.md) plugins. Must be combined with QUERY in the same group.  | 
|  COMPACT  |  Compacts Parquet files in Amazon S3. Exactly one node in the cluster has this mode.  | 

 Modes combine freely within the limits described in [Shape rules and limits](#influxdb3-depcfg-limits), so you can dedicate nodes narrowly. A group declared as `["INGEST"]` with no `QUERY` is a write-only node: it accepts writes and does not serve queries, which keeps query load off your ingest path entirely. The one pairing the service requires is `PROCESS` with `QUERY`, because InfluxDB enables query serving implicitly whenever the processing engine is enabled. 

**Important**  
 Instance sizes live inside the node groups, so a deployment configuration does not need `--db-instance-type`. On `update-db-cluster`, passing `--db-instance-type` together with `--deployment-configuration` is rejected. 

## Shape rules and limits
<a name="influxdb3-depcfg-limits"></a>

 Timestream validates the shape before it provisions anything. A request that breaks any of the following rules fails with a validation error and no nodes are created. 


**Deployment configuration limits**  

|  **Rule**  |  **Limit**  | 
| --- | --- | 
|  INGEST nodes  |  1 to 4, counted across every group that includes INGEST  | 
|  QUERY nodes  |  0 to 13, counted across every group that includes QUERY, and subject to the 15-node cluster total below  | 
|  COMPACT nodes  |  Exactly 1  | 
|  Cluster size  |  Up to 15 nodes in total, counting the compactor. This is a cap in its own right: a shape can satisfy every per-function limit above and still be rejected for exceeding it.  | 
|  PROCESS pairing  |  A group that includes PROCESS must also include QUERY. A PROCESS-only group is not supported.  | 
|  Dedicated compactor  |  Above 3 non-compact nodes, COMPACT must be its own group. At 3 or fewer non-compact nodes, you can add COMPACT to a group that also does other work.  | 
|  Engine  |  InfluxDB 3 Enterprise only. A deployment configuration on any other engine is rejected.  | 

**Note**  
 Splitting a function across several groups does not raise its limit. The cap applies to the total number of nodes carrying that mode, no matter how many groups they are spread across. Two groups of three `INGEST` nodes each is six ingest nodes, and is rejected. 

 Separately from the node limits above, a request itself has a fixed shape: a deployment configuration carries **1 to 10 node groups**, each group declares **1 to 4 distinct modes** and a `count` of at least 1, and no two groups may be identical in all three of mode set, instance type, and count. 

**Note**  
 The group limit does not add capacity of its own. However many groups you use, the node limits in the table above still apply to the totals, and the cluster maximum of 15 nodes applies before either. Groups determine how a cluster is *described*, meaning how its nodes are divided by function and instance type, not how large it can be. 

## Working out a valid shape
<a name="influxdb3-depcfg-combinations"></a>

 The limits interact, so it is easier to build a shape in the order the service checks it. Start from the compactor, then place ingest, then spend what is left on query: 

1.  **One compactor, always.** That leaves at most 14 nodes for everything else. Above 3 non-compact nodes it has to be its own `["COMPACT"]` group; at 3 or fewer you may fold `COMPACT` into another group and spend nothing on it. 

1.  **1 to 4 ingest nodes.** Decide whether they also serve queries. `["INGEST","QUERY"]` nodes count against both the ingest limit and the query limit; `["INGEST"]` nodes count only against the ingest limit and keep query load off your write path. 

1.  **Query nodes up to the limit,** counting any ingest nodes that also carry `QUERY`, and staying inside the 15-node cluster total. 

1.  **Group by instance type.** Nodes that share a mode set and an instance type belong in one group. Add another group whenever you want part of a function on a different instance type, such as larger query nodes for heavy dashboards alongside smaller ones for light reads. 

 These shapes are all valid, and show the range the limits allow: 


**Example cluster shapes**  

|  **Shape**  |  **Nodes**  |  **Groups**  |  **Notes**  | 
| --- | --- | --- | --- | 
|  1 × ["INGEST","QUERY","COMPACT"]  |  1  |  1  |  Smallest valid cluster. One node does everything.  | 
|  2 × ["INGEST","QUERY"] \+ 1 × ["COMPACT"]  |  3  |  2  |  The classic 3-node cluster, now with the compactor sizeable on its own.  | 
|  1 × ["INGEST"] \+ 13 × ["QUERY"] \+ 1 × ["COMPACT"]  |  15  |  3  |  Read-heavy maximum: one writer, the full complement of readers, one compactor.  | 
|  4 × ["INGEST"] \+ 10 × ["QUERY"] \+ 1 × ["COMPACT"]  |  15  |  3  |  Write-heavy maximum, with ingest fully isolated from query.  | 
|  2 × ["INGEST","QUERY","PROCESS"] \+ 1 × ["COMPACT"]  |  3  |  2  |  Processing engine on the ingest nodes. PROCESS is legal here because the group also has QUERY.  | 
|  2 × ["INGEST","QUERY"] on large \+ 2 × ["QUERY"] on medium \+ 1 × ["COMPACT"] on 2xlarge  |  5  |  3  |  Three instance types in one cluster. This is what a parameter group cannot express.  | 

 And these are rejected: 
+  4 × `["INGEST"]` \+ 13 × `["QUERY"]` \+ 1 × `["COMPACT"]` is 18 nodes. Every per-function limit is satisfied, but the cluster total is not. The `QUERY` maximum of 13 is only reachable when the rest of the cluster leaves room for it, which in practice means a single ingest node. 
+  3 × `["INGEST"]` plus 2 × `["INGEST","QUERY"]` is 5 ingest nodes, over the limit of 4, even though they sit in different groups. 
+  Any shape with no `COMPACT` node, or with two of them. 
+  A `["PROCESS"]` group with no `QUERY` alongside it. 
+  4 non-compact nodes with `COMPACT` folded into one of their groups. Above 3 non-compact nodes the compactor must be dedicated. 
+  Two byte-identical groups, meaning the same mode set, the same instance type, and the same `count`. Use one group with the combined `count` instead. 

## Create a cluster with a deployment configuration
<a name="influxdb3-depcfg-create"></a>

 The following AWS CLI command creates a five-node cluster: two nodes that both ingest and query, two query-only read nodes on a smaller instance type, and a dedicated compactor on a larger one. Compaction gets the compute it needs without enlarging the rest of the cluster. 

```
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-heterogeneous-cluster" \
  --deployment-configuration '{
    "InfluxDBv3Enterprise": {
      "nodeGroups": [
        {"instanceModes": ["INGEST","QUERY"], "instanceType": "db.influx.large",   "count": 2},
        {"instanceModes": ["QUERY"],          "instanceType": "db.influx.medium",  "count": 2},
        {"instanceModes": ["COMPACT"],        "instanceType": "db.influx.2xlarge", "count": 1}
      ]
    }
  }' \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --no-publicly-accessible
```

### Smaller cluster with a shared compactor
<a name="influxdb3-depcfg-create-small"></a>

 At 3 or fewer non-compact nodes you can skip the dedicated compactor group and add `COMPACT` to a group that already ingests and queries: 

```
aws timestream-influxdb create-db-cluster \
  --region us-east-1 \
  --name "my-small-cluster" \
  --deployment-configuration '{
    "InfluxDBv3Enterprise": {
      "nodeGroups": [
        {"instanceModes": ["INGEST","QUERY","COMPACT"], "instanceType": "db.influx.large", "count": 1},
        {"instanceModes": ["QUERY"],                    "instanceType": "db.influx.large", "count": 2}
      ]
    }
  }' \
  --vpc-subnet-ids subnet-12345abc subnet-67890def \
  --vpc-security-group-ids sg-12345abc \
  --no-publicly-accessible
```

 Sharing a node between compaction and live traffic saves an instance, but compaction then competes with your reads and writes for CPU and memory. For production workloads that compact continuously, give the compactor its own group. 

## Reshape an existing cluster
<a name="influxdb3-depcfg-update"></a>

 To change a cluster's shape, submit the complete target shape to `update-db-cluster`. Timestream compares the shape you submit against the running cluster and then adds, removes, or resizes only what differs. A single call can add a group, remove a group, change a group's `count`, and change a group's `instanceType`. 

**Important**  
 The shape you submit is the shape you get. Any group you leave out of the request is removed from the cluster, so resubmit the groups you want to keep unchanged along with the ones you are changing. 

 This example resizes only the compactor, from `db.influx.2xlarge` to `db.influx.4xlarge`, by resubmitting the other two groups untouched: 

```
aws timestream-influxdb update-db-cluster \
  --region us-east-1 \
  --db-cluster-id "abcdefgh12" \
  --deployment-configuration '{
    "InfluxDBv3Enterprise": {
      "nodeGroups": [
        {"instanceModes": ["INGEST","QUERY"], "instanceType": "db.influx.large",   "count": 2},
        {"instanceModes": ["QUERY"],          "instanceType": "db.influx.medium",  "count": 2},
        {"instanceModes": ["COMPACT"],        "instanceType": "db.influx.4xlarge", "count": 1}
      ]
    }
  }'
```

 The same pattern covers the other reshaping operations: 
+  **Add read capacity.** Raise the `count` of a query-only group, or add another query-only group with a different instance type. 
+  **Scale down.** Lower a group's `count`, or leave the group out of the request entirely to remove it. 
+  **Resize one function.** Change that group's `instanceType` and resubmit the rest unchanged. 
+  **Change what a node does.** Edit the group's `instanceModes`, for example promoting a query-only group to `["INGEST","QUERY"]`. 

**Note**  
 Reshaping is subject to the same limits as creation, so a request that would exceed 4 `INGEST` nodes or leave the cluster without exactly one `COMPACT` node is rejected. 

## Deployment configurations and parameter groups
<a name="influxdb3-depcfg-parameter-groups"></a>

 Before deployment configurations, you expressed cluster topology as parameters on a DB parameter group: `ingestQueryInstances`, `queryOnlyInstances`, and `dedicatedCompactor`. A deployment configuration replaces those fields. The two mechanisms can coexist while you migrate, and Timestream resolves the overlap deterministically: 
+  **The deployment configuration wins.** If the parameter group attached to your request still carries `ingestQueryInstances`, `queryOnlyInstances`, or `dedicatedCompactor`, and you also pass `--deployment-configuration`, those three parameter-group fields are ignored rather than rejected. The deployment configuration is the single source of truth for cluster shape. 
+  **Every other parameter still applies.** Engine tuning parameters such as `bufferMemLimitMb`, `dataFusionNumThreads`, and the compaction parameters continue to take effect from the parameter group as usual. Only the three topology fields are superseded. 
+  **You must supply one or the other.** A `create-db-cluster` request that provides neither a parameter group topology nor a deployment configuration is rejected. 
+  **Existing clusters are unaffected.** A cluster created with parameter-group topology keeps working, and read APIs continue to return its legacy `clusterConfiguration` values. 

**Tip**  
 Because a deployment configuration sets instance size per group, it is also the only way to run nodes of different instance types in one cluster. A cluster configured through parameter-group topology uses a single instance type for every node. 

## Read a cluster's shape and endpoints
<a name="influxdb3-depcfg-read-shape"></a>

 `get-db-cluster` reports cluster shape in two fields: 

`deploymentConfiguration`  
 Returned for a cluster that is governed by a deployment configuration, meaning one that was created or reshaped with it. Timestream reconstructs this field from the cluster's live provisioned instances, so it reflects the shape the cluster actually has right now rather than a stored copy of your last request. A cluster still using parameter-group topology returns this field empty. 

`clusterConfiguration`  
 Always returned for InfluxDB 3 Enterprise clusters. This field is deprecated in favor of `deploymentConfiguration`. It is derived from the deployment configuration when the cluster uses one, and from the parameter group's instance counts otherwise. 

 For a node-by-node view, call `list-db-instances-for-cluster`. Each node reports its own `instanceModes` and `dbInstanceType`. Each node also reports a singular `instanceMode`; for InfluxDB 3 Enterprise nodes, read the plural `instanceModes`, because a node in a deployment configuration can perform several functions at once. 

**Note**  
 Node grouping and ordering are not preserved on read. A compactor that you sideloaded onto an existing group comes back as a `COMPACT` mode on that node rather than as a separate group. To confirm that a cluster matches the shape you requested, group the returned nodes by their mode set and instance type and compare the counts. 

 Both cluster endpoints keep working as you reshape the cluster, and Timestream updates their membership automatically: 
+  `endpoint` is the writer endpoint, backed by the nodes that have `INGEST`. 
+  `readerEndpoint` is the reader endpoint, backed by the nodes that have `QUERY` but not `INGEST`. 

 For guidance on distributing client traffic evenly across the nodes behind an endpoint, see [Managing DNS resolution for cluster endpoints](timestream-for-influx-managing-dns.md). 

## Best practices
<a name="influxdb3-depcfg-best-practices"></a>
+  **Give the compactor its own group for production workloads.** Compaction is bursty and memory-intensive. Isolating it keeps background optimization from competing with live reads and writes, and it lets you size compaction independently of everything else. 
+  **Run at least two `INGEST` nodes.** A single ingest node means writes stop if that node is restarted, patched, or fails. 
+  **Scale query-only nodes for read concurrency.** Add query-only nodes, or move them to a larger instance type, when query latency rises under concurrent load rather than enlarging the whole cluster. 
+  **Match tuning parameters to the largest group.** Parameter groups apply cluster-wide, so a value such as `dataFusionNumThreads` that is sized for your largest instance type also lands on your smallest nodes. Verify the tuning parameters are appropriate for every instance type in the cluster. See [Supported Instance Types and Specifications](supported-instance-types.md). 
+  **Keep your intended shape under version control.** Because `update-db-cluster` converges the cluster to exactly the shape you submit, storing that JSON alongside your infrastructure code makes reshaping repeatable and makes an accidental group deletion easy to spot in review. 
+  **Reshape during periods of lower activity.** Adding, removing, or resizing nodes restarts the affected nodes. Client traffic is redistributed across the remaining nodes behind the cluster endpoints while the change is applied. 