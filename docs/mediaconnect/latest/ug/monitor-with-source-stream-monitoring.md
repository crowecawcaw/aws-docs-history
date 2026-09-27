

# Monitoring using source metadata
<a name="monitor-with-source-stream-monitoring"></a>

MediaConnect source metadata monitoring displays general information about the structure of the incoming media stream. Source metadata monitoring can be used with the MediaConnect console, API, AWS CLI, or SDK. For more information about the API, see [DescribeFlowSourceMetadata](https://docs.aws.amazon.com/mediaconnect/latest/api/API_DescribeFlowSourceMetadata.html) and [GetRouterInputSourceMetadata](https://docs.aws.amazon.com/mediaconnect/latest/api/API_GetRouterInputSourceMetadata.html) in the *MediaConnect API Reference.*

**Note**  
If you are using more than one source for your flow or router input, source metadata is only displayed for the source currently used by the flow or router input. 

## Source metadata availability
<a name="source-metadata-availability"></a>

Source metadata support depends on the source protocol and whether the source is attached to a flow or a router input.


**Source metadata support by protocol**  

| Source protocol | Flows | Router inputs | 
| --- | --- | --- | 
| Transport stream | Supported | Supported | 
| NDI® | Supported | Not supported | 