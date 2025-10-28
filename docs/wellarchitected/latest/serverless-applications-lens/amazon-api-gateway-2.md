# Amazon API Gateway

Amazon API Gateway and
AWS AppSync caching can be enabled to improve performance for applicable operations. DAX can
improve read responses significantly as well as Global and Local Secondary Indexes to prevent
DynamoDB full table scan operations. These details and resources were described in the Mobile
Backend scenario.

API Gateway content encoding allows API clients to request the payload to be compressed
before being sent back in the response to an API request. This reduces the number of bytes
that are sent from API Gateway to API clients and decreases the time it takes to transfer the
data. You can enable content encoding in the API definition, and you can also set the
minimum response size that triggers compression. By default, APIs do not have content
encoding support enabled.
