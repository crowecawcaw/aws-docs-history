

# Best practices
<a name="routes-best-practices"></a>

This section covers best practices for using compression and choosing between Simple (GeoJSON) and FlexiblePolyline formats when interacting with the API, providing guidance on optimizing performance, bandwidth, and data handling.

## Compression
<a name="compression"></a>

To enhance the performance and efficiency of your applications when interacting with our API, it is recommended to enable compression for responses, especially when dealing with large text-based payloads. You can activate compression by including the `Accept-Encoding` header in your API requests, specifying your preferred compression method. We support `gzip` and `deflate` for their compression capabilities, with `gzip` typically offering better compression ratios.

### When to Enable Compression
<a name="when-to-enable-compression"></a>

**Large responses**  
Enable compression for large text-based responses to reduce bandwidth usage and improve load times.

**Network constraints**  
If your application operates over limited bandwidth or high-latency networks, compression can enhance data transfer efficiency.

### How to Use Compression Effectively
<a name="how-to-use-compression-effectively"></a>

**Set the Accept-Encoding header**  
Include `Accept-Encoding: gzip, deflate` in your HTTP requests to inform our API that you support these compression methods. The method to enable and handle compression varies by [AWS SDK](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html) and programming language. For example, the [AWS SDK for Java v1](https://docs.aws.amazon.com/AWSJavaSDK/latest/javadoc/com/amazonaws/ClientConfiguration.html#withGzip-boolean-) uses the `withGzip` method in the `ClientConfiguration` class to enable gzip, while the AWS SDK for Go requires adding specific middleware for compression handling. For other SDKs, please refer to the [AWS SDK Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/overview.html) for detailed instructions.

**Handle decompression properly**  
Ensure your client application can correctly decompress the responses based on the `Content-Encoding` header returned by our API.

**Test and monitor**  
Regularly evaluate the impact of compression on your application's performance, balancing the benefits of reduced payload sizes against any additional CPU overhead from decompression processes.

## Polyline
<a name="polyline"></a>

Best practices for choosing between Simple (GeoJSON) and FlexiblePolyline formats when interacting with our API, to optimize both performance and usability of your geospatial data.

### Use Simple (GeoJSON) Format
<a name="use-simple-format"></a>

**Readability and Standardization**  
Use when you require a widely recognized and human-readable format for ease of debugging and interoperability with various geospatial tools.

**Precision**  
Choose Simple format when your application needs high precision for coordinates, as GeoJSON maintains full decimal precision without loss.

**Smaller datasets**  
Simple format is ideal when working with smaller sets of coordinate data where the size reduction benefits of compression are minimal.

### Use FlexiblePolyline Format
<a name="use-flexiblepolyline-format"></a>

**Data size reduction**  
FlexiblePolyline is ideal when you need to minimize the amount of data transmitted, especially for large lists of coordinates, by leveraging lossy compression techniques.

**URL safety**  
FlexiblePolyline provides a compact, URL-safe string that can be used directly in query parameters without additional encoding.

**Performance optimization**  
FlexiblePolyline helps reduce the payload size, leading to faster data transfer and lower bandwidth usage, making it crucial for high-performance applications or those operating over constrained networks.