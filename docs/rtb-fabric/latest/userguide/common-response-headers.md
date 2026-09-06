

# Common response headers
<a name="common-response-headers"></a>

The following table describes response headers that are common to most RTB Fabric responses.


| Header | Description | 
| --- | --- | 
| x-amz-rtb-link-id | The unique identifier of the RTB Fabric link that this request or response is associated with. This header is used for attribution purposes to correlate a request or response back to the specific link through which it was processed.<br />Type: String | 
| x-amz-response-source |  The system that was the source of the response or error. This header is used to attribute a response back to the component that generated it within the RTB Fabric processing pipeline. When the response originates from the RTB Fabric service infrastructure, this value is set to `RTBFabric`. <br />Type: String<br />Valid Values: `RTBFabric` \| `Module:<module-name>` \| `Responder` \| `Unknown` | 

The following are descriptions of the valid values for `x-amz-response-source`:

`RTBFabric`  
The response originated from RTB Fabric service.

`Module:<module-name>`  
A specific RTB module (for example, `Module:OpenRtbFilter`) was the source of the response or error.

`Responder`  
The responder RTB application was the source of the response.

`Unknown`  
The source of the response could not be determined.