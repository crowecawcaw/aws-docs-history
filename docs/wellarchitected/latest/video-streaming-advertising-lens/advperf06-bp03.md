

# ADVPERF06-BP03 Optimize Agentic RTB Framework (ARTF) agent container performance for sub-millisecond to single-digit-millisecond latency

 ARTF agent containers process bid requests through gRPC and return OpenRTB Patch mutations under strict auction deadlines. Container image size, startup sequence, serialization format, memory layout, and inference engine affect whether your agent responds within the auction window. ARTF targets sub-millisecond to single-digit-millisecond response times. 

 **Desired outcome:** 
+  Your ARTF agent containers complete the full bid processing pipeline (protobuf deserialization, feature extraction, ML inference, business logic, response serialization) within the sub-millisecond to single-digit-millisecond budget required to respond inside the 100 ms real-time bidding auction window. 
+  Container image size, memory layout, gRPC connection configuration, and ML inference execution are all optimized before bid traffic is accepted. 

 **Common anti-patterns:** 
+  Running ARTF agents without pre-allocated memory pools, so per-request heap allocation accumulates under high concurrency and pushes p99 latency past the auction deadline. 
+  Loading ML models on first invocation rather than at container startup, which adds cold model loading latency to first-request latency after scale-out events. 
+  Sharing a single HTTP/2 connection pool across all agent invocations. A single packet loss stalls all streams until TCP retransmission, causing correlated timeouts across concurrent bid requests. 

 **Benefits of establishing this best practice:** 
+  Pre-allocated memory pools remove per-request heap allocation and GC pauses that are the primary source of p99 latency spikes in high-throughput agent containers. 
+  Model preloading at container startup means all agent invocations execute at full speed from the moment the container begins accepting traffic, removing cold model loading latency after scale-out events. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 ARTF agent containers run on a strict latency budget. The full pipeline (gRPC receive, protobuf deserialization, feature extraction, ML inference, business logic evaluation, OpenRTB Patch construction, protobuf serialization, gRPC send) must complete within a fraction of the total auction window. ARTF targets sub-millisecond to single-digit-millisecond response times to leave headroom for the orchestrator and network transport. Three optimizations deliver the most significant latency improvements: 
+  **Memory management:** Heap allocation during bid request processing triggers garbage collection pauses that add unpredictable overhead to p99 latency. Pre-allocating fixed pools at container startup for protobuf message buffers, inference tensors, and intermediate data structures, and reusing them across requests by clearing and repopulating fields rather than allocating new objects, removes the primary GC pressure source. Rust (compile-time ownership, no GC), C\+\+ (RAII patterns), and Go (with object pools) provide deterministic memory behavior. Java and Python with stop-the-world GC introduce unpredictable pause latency at p99. 
+  **ML inference:** Compiling models to ONNX Runtime or NVIDIA TensorRT format removes framework interpreter overhead. Small, optimized bid scoring models on GPU-accelerated instances can achieve sub-100 μs inference latency. CPU-only deployments or larger models typically operate in the low-millisecond range. Load model weights at container startup and run warm-up inference passes before the gRPC server begins accepting traffic, so the first live bid request executes at full speed. 
+  **gRPC connection management:** Each new gRPC connection requires TCP \+ TLS handshake overhead. Configure the Agent Orchestrator to maintain persistent HTTP/2 connections to agent containers and reuse them across bid requests. For high-QPS agent traffic to the same container, use 2–4 HTTP/2 connections per container to limit the impact of TCP-level head-of-line blocking. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build minimal container images from distroless or scratch base images:** Use multi-stage Docker builds to separate compilation from production. The production image should contain only the compiled binary and model artifacts, no build tools, package managers, or development dependencies. Smaller images reduce pull time during scale-out events. 

1.  **Pre-allocate memory pools at container startup:** At startup, allocate fixed-size object pools for protobuf message buffers, inference input and output tensors, and intermediate data structures. Reuse pool objects across bid requests by clearing fields rather than allocating new instances. Monitor GC pause metrics and heap allocation rate in CloudWatch to confirm that per-request allocation has been removed. 

1.  **Compile ML models to ONNX Runtime format and preload at startup:** Compile your bid scoring model to ONNX Runtime using onnxruntime.InferenceSession and load the compiled model weights at container startup. Run 10–50 warm-up inference passes with representative input tensors before the gRPC server begins accepting traffic. This initializes GPU memory allocations and JIT caches so the first live bid request executes at full speed. 

1.  **Configure gRPC connection pooling and deadline propagation:** Configure the Agent Orchestrator to maintain 2–4 persistent HTTP/2 connections per agent container rather than opening new connections per request. Implement gRPC deadline checking so that when the remaining deadline drops below your minimum processing threshold, your agent returns a no-bid signal immediately rather than continuing work that can't complete in time. 

1.  **Benchmark p99 latency under production concurrency before accepting traffic:** Before enabling production traffic, run your agent container under realistic concurrency (use [AWS Fault Injection Service](https://aws.amazon.com/fis/) to simulate production load) and measure p99 protobuf deserialization time (<100 μs target), p99 ONNX inference time (<500 μs target), and end-to-end gRPC response time (<1 ms target for basic models). Set CloudWatch alarms on these percentiles and alert when they exceed the targets. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVPERF02-BP04 Use a specialized instance family and features](advperf02-bp04.md) 

 **Related documents:** 
+  [IAB Tech Lab Agentic RTB Framework (ARTF) specification](https://iabtechlab.com/standards/artf/) 
+  [ONNX Runtime documentation](https://onnxruntime.ai/docs/) 

 **Related services:** 
+  [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/) 