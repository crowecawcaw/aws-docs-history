

# TELCOPERF02-BP01 Deploy containerized network functions on EKS with performance-optimized node configurations

 Telco cloud-based network functions (CNFs) need direct hardware access, such as CPU pinning, NUMA-aware scheduling, SR-IOV, and DPDK, that serverless container platforms can't provide. Running them on Amazon EKS worker nodes tuned for packet processing delivers deterministic, wire-speed performance while retaining Kubernetes lifecycle management. This best practice configures EKS nodes for the performance isolation CNFs require. 

 **Desired outcome:** 
+  CNFs run on EKS worker nodes with CPU pinning, NUMA-aware pod placement, and hugepage allocation configured for deterministic packet processing. 
+  Network-intensive CNFs use SR-IOV or DPDK for data-plane interfaces, bypassing the kernel network stack. 
+  Orchestration handles lifecycle management, including rolling updates, scaling, and health checks, without degrading the performance isolation CNFs need. 

 **Common anti-patterns:** 
+  Deploying CNFs on serverless container platforms that don't support CPU pinning, SR-IOV, hugepages, or direct hardware access. 
+  Injecting service-mesh sidecars onto data-plane CNF pods, adding latency and reducing throughput on the packet path. 
+  Running CNFs on general-purpose node configurations without CPU-manager static policy, NUMA topology awareness, or hugepage pre-allocation. 
+  Sizing nodes by vCPU count alone, ignoring the isolation and network characteristics packet processing depends on. 

 **Benefits of establishing this best practice:** 
+  CPU pinning and NUMA-aware scheduling reduce the jitter caused by kernel scheduler decisions and cross-NUMA memory access. 
+  SR-IOV and DPDK bypass the kernel network stack, achieving the packets-per-second throughput carrier-grade CNFs require. 
+  EKS provides Kubernetes-native lifecycle management while the node configuration provides performance isolation. 
+  Deterministic performance is validated against production traffic rather than assumed. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Telco CNFs have compute requirements that ordinary containerized applications don't. A User Plane Function (UPF) processing subscriber traffic needs CPU cores that are never preempted, memory from the local NUMA node, and network interfaces that bypass the kernel entirely. These requirements are incompatible with serverless platforms that abstract the hardware away, which is why EKS with performance-tuned nodes is a requirement rather than a preference for these workloads. The constraint is hardware access, not container density. 

 The performance isolation is assembled from specific Kubernetes and kernel features working together. The kubelet CPU Manager in static policy mode pins guaranteed-QoS pods to specific cores, and the Topology Manager places a pod's CPU and memory on the same NUMA node. Hugepages pre-allocated at boot feed DPDK memory pools. For the data plane, SR-IOV exposes virtual functions directly to pods through a device plugin, or DPDK binds interfaces to user-space drivers, and either bypasses the kernel network stack to reach carrier-grade packet rates. Each of these is a deliberate node configuration, and omitting one (for example, requesting guaranteed QoS but not enabling the static CPU policy) silently defeats the isolation. 

 Service-mesh sidecars on data-plane pods are a common and costly anti-pattern. A sidecar proxy adds latency and consumes throughput on every packet, which is unacceptable on the subscriber-traffic path, so mesh functionality, if used at all, should be confined to control-plane and management interfaces. Validation under realistic traffic closes the design, confirming that pinning removes jitter and that SR-IOV or DPDK delivers the required rate. 

### Implementation steps
<a name="implementation-steps"></a>
+  Configure nodes for performance isolation: set the kubelet CPU Manager to static policy, enable the Topology Manager with single-NUMA-node policy, and pre-allocate hugepages in the node kernel boot parameters. 
+  Deploy the SR-IOV network device plugin to expose Elastic Network Adapter (ENA) virtual functions to pods, and define Multus NetworkAttachmentDefinitions for each data-plane interface type. 
+  Set guaranteed-QoS pod resources: set CPU requests equal to limits as integers for CNF pods to trigger static CPU pinning, and request hugepages explicitly in the pod spec. 
+  Exclude data-plane pods from any service mesh using namespace labels or pod annotations, applying mesh only to management and control-plane pods. 
+  Where the service mesh previously provided mTLS between workloads, substitute an equivalent for subscriber-traffic confidentiality on N3 or N9 — IPsec, SRv6 encryption, or an equivalent per 3GPP TS 33.501 — and apply the Framework's SEC09 encryption-in-transit guidance. 
+  Validate performance under load with realistic packet sizes, protocol mixes, and flow counts, confirming that pinning reduces jitter and SR-IOV or DPDK achieves the required throughput. \#\# Resources **Key AWS services:** 
+  [Amazon EKS (Elastic Kubernetes Service)](https://aws.amazon.com/pm/eks/) 
+  [Amazon EC2](https://aws.amazon.com/ec2/) 
+  [Amazon VPC](https://aws.amazon.com/vpc/) 