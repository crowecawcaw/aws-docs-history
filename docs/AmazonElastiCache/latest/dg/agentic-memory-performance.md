

# Performance benefits
<a name="agentic-memory-performance"></a>

The following table summarizes the performance improvements observed in testing with a memory-enabled agent versus a stateless agent:


| Metric | Without memory | With memory | Improvement | 
| --- | --- | --- | --- | 
| Tool calls per request | 3 | 0 (memory retrieval) | Eliminated redundant tool calls | 
| Token usage | \~70,000 | \~6,300 | 12x reduction | 
| Response time | 9.25 seconds | 2 seconds | 3x\+ faster | 
| Memory lookup latency | N/A | Sub-millisecond | Valkey in-memory performance | 