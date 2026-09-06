

# Testing and using links
<a name="testing-and-using-links"></a>

**Note**  
 Link addresses will only be visible and accessible from within your VPC. 

**To test your newly created link**

1.  The URL components in the following example come from your API responses. If you don't have them at hand, you can find your gateway ID and link ID in the AWS Management Console, or by calling the [ListRequesterGateways](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListRequesterGateways.html), [ListResponderGateways](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListResponderGateways.html), or [ListLinks](https://docs.aws.amazon.com/rtb-fabric/latest/api/API_ListLinks.html) operation. 

1.  From the command line, use `curl` to send a POST request to the link. Supply an OpenRTB payload to validate end-to-end requests to your partner, or an empty body to test connectivity. The following example shows a request in the us-east-1 Region. 

   ```
   curl -X POST -H "Content-Type: application/json" -d {{{Your RTB JSON Payload}}} \
       "https://{{{your-gateway-id}}}.{{{your-aws-account}}}.gateway.rtbfabric.{{{your-region}}}.amazonaws.com/link/{{{your-link-id}}}"
   ```

    You can append additional URL or path parameters that your partner expects to the link URI. 

 Each response includes the `x-amz-rtb-link-id` and `x-amz-response-source` headers. The `x-amz-response-source` header identifies the component that produced the response (for example, RTB Fabric, a module, or the responder), which is the first signal to check when triaging an unexpected response. For the full header contract, see [Common response headers](common-response-headers.md). 

## Error responses
<a name="testing-link-error-responses"></a>

 When a request does not succeed, the gateway returns an HTTP error response with a JSON body in the following shape. 

```
{"error":"true","reason":"{{message}}"}
```

 The status code tells you where to look first. A `4xx` status code usually means that the request or its configuration needs to change on your side. A `5xx` status code means that RTB Fabric or the responder is the source. A timeout (`408`) is an exception: it is a `4xx` code, but it indicates that the responder did not respond in time. The `reason` field is a free-form text string. The following table lists two common error responses that you can encounter while testing a link. 


| Status code | Reason | Meaning | 
| --- | --- | --- | 
| `503` | `Service temporarily unavailable` | The gateway could not deliver the request to the responder. | 
| `408` | `Timeout waiting for response from responder.` | The responder did not return a response within the gateway's timeout window. | 

 The `x-amz-response-source` header on the error response identifies which component produced it. 