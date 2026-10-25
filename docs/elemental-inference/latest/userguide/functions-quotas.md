

# Quotas and limits for functions
<a name="functions-quotas"></a>

The following quotas and limits apply to functions. To request an increase to a quota that you can change, see [Quotas for AWS Elemental Inference](quotas.md).


| Quota or limit | Default | Adjustable | 
| --- | --- | --- | 
| Enabled function outputs per feed | 2 | Yes | 
| Enabled outputs per feed, of all types | 5 | No | 
| Total outputs per feed, enabled and disabled | 30 | No | 
| Interval of a fixed-interval trigger | 1–60 seconds | No | 
| Frames per run | 1–64 | No | 
| Size of a resized frame | Width up to 1,280 pixels, height up to 720 pixels | No | 
| Fragments in the video clip | 1–16 | No | 
| Length of each expression | 5,120 characters | No | 
| Length of a function description | 1,024 characters | No | 
| Length of a model ID or ARN | 2,048 characters | No | 
| Size of the request after media substitution | 25 MB | No | 
| Model invocation timeout | About 18 seconds | No | 
| Time from the end of a window to its result, on a live feed | At most about 20 seconds | No | 

Every enabled output on a feed counts against the per-feed output quotas, whichever service created it, and a function output counts against both the function-output quota and the all-types quota. A feed that AWS Elemental MediaLive set up for event clipping and smart subtitles is already using two of its five enabled outputs.

**Important**  
The quotas that most often limit a function in practice are not Elemental Inference quotas at all. They are your account's Amazon Bedrock quotas for the model you chose — requests per minute and tokens per minute — because the invocation runs in your account. A function on a short interval is a continuous workload against those quotas. See [Costs and throughput](functions-costs.md).