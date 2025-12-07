# Important: Timeout Configuration

###### Important

Amazon Nova inference requests can take up to 60 minutes to complete. Configure your client
timeout settings accordingly:

The following example is Python code. Users can check the documentation for their preferred SDK language version in that SDK's API docs.

```
from botocore.config import Config

bedrock = boto3.client(
    'bedrock-runtime',
    region_name='us-east-1',
    config=Config(
        read_timeout=3600  # 60 minutes
    )
)
```
