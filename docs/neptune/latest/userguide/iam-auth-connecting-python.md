

# Connecting to Amazon Neptune databases using IAM authentication with Python
<a name="iam-auth-connecting-python"></a>

The `boto3` `neptunedata` client provides the simplest way to connect to an IAM-enabled Neptune database from Python. The client handles Signature Version 4 signing automatically, so you don't need to sign requests yourself.

## Prerequisites
<a name="iam-auth-connecting-python-prereqs"></a>
+ Python 3.x
+ The `boto3` library: `pip install boto3`
+ AWS credentials configured through any standard method (environment variables, AWS config file, instance profile, or Lambda execution role)
+ An IAM policy that allows `neptune-db:*` actions on your Neptune cluster

## Connecting with default credentials
<a name="iam-auth-connecting-python-default"></a>

This approach works when `boto3` can resolve credentials automatically, such as on Amazon Elastic Compute Cloud instances with instance profiles, in AWS Lambda functions, or with configured AWS profiles.

Replace the endpoint URL with your Neptune cluster endpoint.

**Gremlin and openCypher**

```
import boto3
from botocore.config import Config

cfg = Config(retries={"total_max_attempts": 1, "mode": "standard"}, read_timeout=None)

neptune = boto3.client('neptunedata', config=cfg,
    region_name='{{us-east-1}}',
    endpoint_url='https://{{your-neptune-endpoint}}:8182')

# Gremlin
resp = neptune.execute_gremlin_query(gremlinQuery='g.V().limit(1)')
print(resp['result'])

# openCypher
resp = neptune.execute_open_cypher_query(openCypherQuery='MATCH (n) RETURN n LIMIT 1')
print(resp['results'])
```

**SPARQL**

The `boto3` `neptunedata` client does not currently support SPARQL. To send SPARQL queries to an IAM-enabled Neptune database, sign requests manually by using Signature Version 4 with the `botocore` request-signing utilities and the `requests` library (`pip install boto3 requests`).

```
import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.session import Session

endpoint = 'https://{{your-neptune-endpoint}}:8182'
region = '{{us-east-1}}'

query = 'SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 1'

request = AWSRequest(method='POST', url=f'{endpoint}/sparql/',
    data={'query': query})
SigV4Auth(Session().get_credentials(), 'neptune-db', region).add_auth(request)

resp = requests.post(f'{endpoint}/sparql/', headers=request.headers,
    data={'query': query})
print(resp.json())
```

**Note**  
This example uses `botocore.session.Session` to resolve AWS credentials automatically from environment variables, AWS config files, instance profiles, or Lambda execution roles. You don't need to set credentials explicitly.

## Using temporary credentials
<a name="iam-auth-connecting-python-temp-creds"></a>

For cross-account access, time-limited sessions, or as a security best practice to avoid long-lived credentials, use AWS STS to obtain temporary credentials and create a `boto3.Session`.

**Gremlin and openCypher**

```
import boto3
from botocore.config import Config

sts = boto3.client('sts')
creds = sts.assume_role(
    RoleArn='arn:aws:iam::{{123456789012}}:role/{{NeptuneRole}}',
    RoleSessionName='neptune-session'
)['Credentials']

session = boto3.Session(
    aws_access_key_id=creds['AccessKeyId'],
    aws_secret_access_key=creds['SecretAccessKey'],
    aws_session_token=creds['SessionToken'],
    region_name='{{us-east-1}}'
)

cfg = Config(retries={"total_max_attempts": 1, "mode": "standard"}, read_timeout=None)

neptune = session.client('neptunedata', config=cfg,
    endpoint_url='https://{{your-neptune-endpoint}}:8182')

# Gremlin
resp = neptune.execute_gremlin_query(gremlinQuery='g.V().limit(1)')
print(resp['result'])

# openCypher
resp = neptune.execute_open_cypher_query(openCypherQuery='MATCH (n) RETURN n LIMIT 1')
print(resp['results'])
```

**Note**  
Temporary credentials expire after a specified interval (the default is 1 hour) and are not automatically refreshed by the client. For long-running applications, use profile-based credentials or instance profiles instead.

**SPARQL**

Because the `boto3` `neptunedata` client does not currently support SPARQL, you must sign requests manually with the temporary credentials.

```
import boto3
import requests
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
from botocore.credentials import ReadOnlyCredentials

sts = boto3.client('sts')
creds = sts.assume_role(
    RoleArn='arn:aws:iam::{{123456789012}}:role/{{NeptuneRole}}',
    RoleSessionName='neptune-session'
)['Credentials']

endpoint = 'https://{{your-neptune-endpoint}}:8182'
region = '{{us-east-1}}'

query = 'SELECT ?s ?p ?o WHERE { ?s ?p ?o } LIMIT 1'

request = AWSRequest(method='POST', url=f'{endpoint}/sparql/',
    data={'query': query})
SigV4Auth(ReadOnlyCredentials(
    creds['AccessKeyId'], creds['SecretAccessKey'], creds['SessionToken']
), 'neptune-db', region).add_auth(request)

resp = requests.post(f'{endpoint}/sparql/', headers=request.headers,
    data={'query': query})
print(resp.json())
```

## Using with AWS Lambda
<a name="iam-auth-connecting-python-lambda"></a>

In Lambda, the execution role provides credentials automatically through `boto3`. The default credentials example works without modification.

For a complete Lambda example with connection management and retry logic, see [AWS Lambda function examples for Amazon Neptune](lambda-functions-examples.md).