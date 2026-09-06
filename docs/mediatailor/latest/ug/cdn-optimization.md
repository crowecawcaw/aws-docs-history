

# Performance optimization guide for CDN and MediaTailor integrations
<a name="cdn-optimization"></a>

AWS Elemental MediaTailor performance can be maximized through systematic content delivery network (CDN) optimization. Whether you're implementing server-side ad insertion (SSAI), channel assembly, or combined workflows, the optimization principles and performance targets remain consistent. This guide provides comprehensive optimization techniques and benchmarks that apply across all MediaTailor implementations.

For advanced routing optimization using dynamic variables and configuration aliases, see [MediaTailor dynamic ad variables for ADS requests](variables.md). For query parameter optimization strategies, see [MediaTailor manifest query parameters](manifest-query-parameters.md).

**Optimization workflow overview:**

1. **Configure caching** - Set appropriate TTL values and cache behaviors

1. **Optimize routing** - Configure request routing and origin policies

1. **Measure performance** - Track against established benchmarks

1. **Apply advanced techniques** - Implement additional optimization features

**Topics**
+ [Caching optimization](cdn-optimize-caching.md)
+ [Request routing optimization](cdn-optimize-routing.md)
+ [Performance benchmarks](cdn-performance-benchmarks.md)
+ [Advanced optimization](cdn-advanced-optimization.md)