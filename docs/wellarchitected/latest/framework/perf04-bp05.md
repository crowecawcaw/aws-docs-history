

# PERF04-BP05 Choose network protocols to improve performance

 The protocol a workload uses to move data between components shapes the workload's latency, throughput, and reliability. When you match the protocol to each communication requirement, you improve performance and user experience. 

 **Desired outcome:** 
+  You select network protocols based on each communication's latency, throughput, reliability, and security requirements. 
+  You use connection-oriented protocols where guaranteed delivery matters and connectionless protocols where speed matters more. 
+  You measure the effect of protocol and encryption choices rather than defaulting to one protocol everywhere. 

 **Common anti-patterns:** 
+  Teams use TCP for all workloads regardless of performance requirements. 
+  Teams add TLS everywhere without measuring the handshake and encryption overhead on latency-sensitive paths. 
+  Teams change protocols before optimizing the application through simpler means. 

 **Benefits of establishing this best practice:** 
+  You improve user experience by using a protocol suited to each communication pattern. 
+  You increase throughput on high-latency paths by avoiding protocols that stall waiting for acknowledgements. 
+  You balance reliability and speed by choosing the protocol that fits the data being moved. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Changing a workload's network protocol is difficult, calls for expertise, and can introduce subtle bugs. Change protocols only after you have optimized the application in simpler ways. When a workload is bounded by how its protocol behaves on the network, though, the right protocol improves latency and throughput more than any amount of instance tuning. 

 Latency and bandwidth together determine throughput. TCP waits for acknowledgements, so higher latency reduces its effective throughput even when bandwidth is plentiful. Address this with TCP tuning and optimized transfer protocols, or choose a protocol that does not pay the acknowledgement cost. 

 TCP delivers data reliably and in order, which is why web, email, and file transfer depend on it. That reliability costs round-trips to set up the connection and overhead to track delivery. UDP is connectionless, so it is fast and efficient but offers no retransmission or ordering guarantee. UDP suits logs, monitoring, voice, and workloads that answer small queries from many clients, where a lost packet matters less than speed. Encryption layers onto both protocols. TLS adds a multi-round-trip handshake to TCP. DTLS, its UDP equivalent, simplifies the handshake, so its overhead comes mainly from encryption and decryption. 

 Some workloads need more than either general-purpose protocol offers. Scalable reliable datagram (SRD) is built for high-throughput, low-latency communication between compute nodes. SRD load balances traffic across multiple paths and recovers quickly from packet drops or link failures. These properties suit high performance computing (HPC), where nodes exchange large volumes of data during simulation, modeling, or analysis. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Speed up file transfers that use TCP:** Use [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/) to lower latency between clients and your workload, and [AWS Transfer Family](https://aws.amazon.com/aws-transfer-family/) to scale and manage transfers over TCP-based protocols such as SFTP and FTPS. 

1.  **Judge whether TCP latency is acceptable:** Measure network latency with metrics such as time to first byte (TTFB) and round-trip time (RTT). When latency is high, the TCP three-way handshake slows responsiveness. For dynamic content, use [Amazon CloudFront](https://aws.amazon.com/cloudfront/), which keeps a persistent connection to each origin and removes the connection setup time from each client request. 

1.  **Scale UDP services with a Network Load Balancer:** Deploy UDP-based services such as authentication, logging, DNS, IoT, and streaming media behind a [Network Load Balancer](https://aws.amazon.com/elasticloadbalancing/network-load-balancer/) to distribute traffic across targets, scale horizontally, and reduce the load on any single target. 

1.  **Use SRD for HPC workloads:** Enable [Elastic Network Adapter (ENA) Express](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ena-express.html), which uses the SRD protocol to raise single-flow bandwidth and lower tail latency for traffic between Amazon EC2 instances. 

1.  **Route gRPC over HTTP/2 with an Application Load Balancer:** Use an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) to route and load balance gRPC traffic. gRPC runs on HTTP/2, which brings a lighter network footprint, compression, efficient binary serialization, and bi-directional streaming. 

1.  **Use QUIC for latency-sensitive or mobile-first clients:** QUIC runs over UDP and folds the transport and TLS 1.3 handshakes into a single round trip, avoiding the separate TCP and TLS handshakes that add latency, and it keeps a connection alive across a client's network changes instead of breaking it like a TCP-based session would. [Amazon CloudFront](https://aws.amazon.com/cloudfront/) terminates HTTP/3 over QUIC at the edge, and [Network Load Balancer passes QUIC traffic through to your targets](https://aws.amazon.com/blogs/networking-and-content-delivery/introducing-quic-protocol-support-for-network-load-balancer-accelerating-mobile-first-applications/) when you need to terminate it yourself. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF04-BP04 Use load balancing to distribute traffic across multiple resources](perf04-bp04.md) 
+  [PERF04-BP02 Evaluate available networking features](perf04-bp02.md) 
+  [PERF04-BP01 Understand how networking impacts performance](perf04-bp01.md) 

 **Related videos:** 
+  [AWS re:Invent 2025 - AWS Networking Fundamentals: Connect, secure and scale (NET208)](https://www.youtube.com/watch?v=nXBqxnp5ybY&feature=youtu.be) 
+  [AWS re:Invent 2025 - Advanced VPC design and new capabilities (NET340)](https://www.youtube.com/watch?v=40QfxdvDGsw&feature=youtu.be) 
+  [AWS re:Invent 2024 - Dive into the depths of routing on AWS (NET318)](https://www.youtube.com/watch?v=2tHMnbTj4pw&feature=youtu.be) 
+  [AWS re:Invent 2024 - AWS application networking: Build simple, secure, and reliable apps](https://www.youtube.com/watch?v=-obQxSPclrw) 

 **Related examples:** 
+  [Guidance for Network Connectivity on AWS](https://docs.aws.amazon.com/solutions/network-connectivity-on-aws/) 