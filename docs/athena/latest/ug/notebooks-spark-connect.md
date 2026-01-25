# Spark Connect support

Spark Connect is a client-server architecture for Apache Spark that decouples the application client from the Spark cluster's driver process, allowing remote connectivity to Spark from supported clients. Spark Connect also enables interactive debugging during development directly from your favorite IDEs/clients.

From Apache Spark version 3.5 release version onward, Athena supports Spark Connect as an AWS endpoint accessible using the `GetSessionEndpoint` API.

## API/CLI examples (GetSessionEndpoint)

You can use the `GetSessionEndpoint` API to get the Spark Connect endpoint for an interactive session.

```
aws athena get-session-endpoint \
  --region "REGION" \
  --session-id "SESSION_ID"
```

This API returns the Spark Connect endpoint URL for that session.

```
{
  "EndpointUrl": "ENDPOINT_URL",
  "AuthToken": "AUTH_TOKEN",
  "AuthTokenExpirationTime": "AUTH_TOKEN_EXPIRY_TIME"
}
```

## Connecting from self-managed clients

You can connect to an Athena Spark Interactive Session from self-managed clients.

### Pre-requisites

Install the pyspark-connect client for Spark 3.5.6 and the AWS SDK for Python.

```
pip install --user pyspark[connect]==3.5.6
pip install --user boto3
```

The following is a sample Python script to send requests directly to the session endpoint:

```
import boto3
import time
from pyspark.sql import SparkSession

client = boto3.client('athena', region_name='<REGION>')

# start the session
response = client.start_session(
    WorkGroup='<WORKGROUP_NAME>',
    EngineConfiguration={}
)

# wait for the session endpoint to be ready
time.sleep(5)
response = client.get_session_endpoint(SessionId=session_id)

# construct the authenticated remote url
authtoken=response['AuthToken']
endpoint_url=response['EndpointUrl']
endpoint_url=endpoint_url.replace("https", "sc")+":443/;use_ssl=true;"
url_with_headers = (
    f"{endpoint_url}"
    f"x-aws-proxy-auth={authtoken}"
)

# start the Spark session
start_time = time.time()
spark = SparkSession.builder\
    .remote(url_with_headers)\
    .getOrCreate()

spark.version

#
# Enter your spark code here
#

# stop the Spark session
spark.stop()
```

The following is a sample Python script to access the live Spark UI or Spark History Server for a session:

```
Region='<REGION>'
WorkGroupName='<WORKGROUP_NAME>'
SessionId='<SESSION_ID>'
Partition='aws'
Account='<ACCOUNT_NUMBER>'

SessionARN=f"arn:{Partition}:athena:{Region}:{Account}:workgroup/{WorkGroupName}/session/{SessionId}"

# invoke the API to get the live UI/persistence UI for a session
response = client.get_resource_dashboard(
    ResourceARN=SessionARN
)
response['Url']
```
