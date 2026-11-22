

# ADVSUS01-BP03 Reduce CPU time per bid in agent containers to lower fleet energy intensity

 ARTF agent containers process bid requests and return OpenRTB Patch mutations under strict auction deadlines. Inefficiency in container image size, memory allocation, serialization, or inference execution increases the CPU time and compute resources each bid consumes. Because compute resource use is the practical proxy for the energy and carbon cost of this workload, containers that complete work in fewer CPU cycles reduce that footprint while also meeting auction deadlines. 

 **Desired outcome:** 
+  ARTF agent containers complete the full bid processing pipeline within the sub-millisecond to single-digit-millisecond budget using pre-allocated memory pools and compiled model formats. 
+  Container images contain only the compiled binary and model artifacts, reducing image pull time and container startup resource use. 
+  Per-request heap allocation and garbage collection pauses are avoided through pre-allocated memory pools, lowering CPU consumed per bid. 

 **Common anti-patterns:** 
+  Packaging bid agents in large general-purpose base images that carry shells, package managers, and unused libraries, inflating image pull time and startup cost across thousands of bidding nodes. 
+  Allocating protobuf buffers and inference tensors per bid request, triggering frequent garbage collection pauses that consume CPU cycles without producing auction output. 
+  Loading or just-in-time compiling machine learning models on the first request after a container starts, so early bids run slowly and burn extra compute before the runtime warms up. 
+  Continuing to process a bid after the auction deadline has effectively passed, spending CPU on a response the exchange will discard. 
+  Treating container performance purely as a latency problem and ignoring the proportional compute resource cost of inefficient execution. 

 **Benefits of establishing this best practice:** 
+  Lower CPU utilization per bid, which is the practical proxy for reduced energy and carbon across high-volume bidding fleets. 
+  Higher bid responsiveness within the auction deadline, improving win rates and reducing no-bids caused by timeouts. 
+  Smaller container images that pull and start faster, reducing scaling latency and registry storage footprint. 
+  More predictable latency by removing garbage collection pauses and cold-start inference from the request path. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Real-time bidding agents operate under an auction deadline measured in single-digit milliseconds. Unlike most services, they have no opportunity to retry or degrade gracefully. A response that arrives after the deadline is worth nothing. Work that produces no completed bid, such as a garbage collection pause or a cold-start inference, consumes compute resources without contributing auction value. At fleet scale, where thousands of containers each handle high request rates, these small per-request inefficiencies add up. 

 Garbage-collected runtimes simplify development but introduce nondeterministic pauses. High-performance bidders often pre-allocate and reuse fixed object pools to avoid allocations on the request path, trading code simplicity for predictable latency. For the inference runtime, interpreted or framework-based model execution is flexible but slow to start and slower per call. Compiled runtimes such as ONNX Runtime or NVIDIA TensorRT perform optimization work ahead of time so each inference runs faster. Both of these choices reduce the compute consumed per bid but add operational complexity that your team must be prepared to own. 

 Use compute resource signals as your working proxy, such as CPU utilization per node, garbage collection pause frequency and duration, image pull time, and inference latency. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build minimal container images using multi-stage builds:** Use multi-stage Docker builds to separate compilation from production images. Production images should contain only the compiled binary and model artifacts. Smaller images reduce pull time, reduce startup resource use, and reduce the storage footprint of Amazon ECR image archival. 

1.  **Pre-allocate memory pools at container startup:** At container startup, allocate fixed-size pools for protobuf message buffers, inference input/output tensors, and intermediate data structures. Reuse pool objects across bid requests by clearing fields rather than allocating new objects. Monitor garbage collection pause frequency and duration as efficiency signals. Declining GC activity indicates less CPU consumed per bid. 

1.  **Compile bid scoring models to a compiled inference runtime:** Convert bid scoring models to ONNX Runtime or NVIDIA TensorRT format so inference runs as optimized, precompiled operations rather than interpreted framework calls. Compiled models execute with lower and more predictable per-call latency, reducing the CPU time each bid spends in inference. 

1.  **Preload models and run warm-up passes before accepting traffic:** Load model weights at container startup and run warm-up inference passes before the container joins the bidding pool. Every served bid then executes at full inference speed rather than paying just-in-time compilation cost on the first requests after startup. 

1.  **Configure gRPC deadline propagation for early abandonment:** Configure deadline checking in the bid processing pipeline so that when remaining time drops below the minimum threshold, the agent returns a no-bid response immediately rather than consuming resources completing work that will be discarded. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSUS01-BP01 Run advertising fleets on multiple chipsets, including ARM, to lower energy intensity](advsus01-bp01.md) 
+  [ADVSUS01-BP04 Tune adapter concurrency and timeouts to stop spending compute on unusable bids](advsus01-bp04.md) 
+  [ADVSUS04-BP02 Match model capability to task complexity to reduce agent fleet energy use](advsus04-bp02.md) 

 **Related documents:** 
+  [IAB Tech Lab Agentic RTB Framework (ARTF) specification](https://iabtechlab.com/standards/artf/) 
+  [ONNX Runtime documentation](https://onnxruntime.ai/docs/) 

 **Related services:** 
+  [AWS Inferentia](https://aws.amazon.com/machine-learning/inferentia/) 