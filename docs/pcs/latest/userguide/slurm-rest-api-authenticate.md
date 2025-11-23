# Authenticating with Slurm REST API in AWS PCS

The Slurm REST API in AWS PCS uses JSON Web Token (JWT) authentication to ensure secure access to your cluster resources. AWS PCS provides a managed signing key stored in AWS Secrets Manager, which you use to generate JWT tokens containing specific user identity claims.

## Prerequisites

Before authenticating with the Slurm REST API, ensure you have:

- **Cluster configuration**: AWS PCS cluster with Slurm 25.05+ and REST API enabled.
- **AWS permissions**: Access to AWS Secrets Manager for the JWT signing key.
- **User information**: Username, POSIX user ID, and one or more POSIX group IDs for your cluster account.
- **Network access**: Connectivity within your cluster's VPC with security group allowing port 6820.

## Procedure

**To retrieve the Slurm REST API endpoint address**

AWS Management Console

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/ "https://console.aws.amazon.com/pcs/").
2. Choose your cluster from the list.
3. In the cluster configuration details, locate the **Endpoints** section.
4. Note the private IP address and port for **Slurm REST API (slurmrestd)**.
5. You can make API calls by sending properly formatted HTTP requests to this address.

AWS CLI

1. Query your cluster status with `aws pcs get-cluster`. Look for the `SLURMRESTD` endpoint in the `endpoints` field in the response. Here is an example:

```
"endpoints": [
      {
          "type": "SLURMCTLD",
          "privateIpAddress": "192.0.2.1",
          "port": "6817"
      },
      {
          "type": "SLURMRESTD",
          "privateIpAddress": "192.0.2.1",
          "port": "6820"
      }
  ]
```

2. You can make API calls by sending properly formatted HTTP requests to `http://`<privateIpAddress>`:`<port>`/`

###### To retrieve the JWT signing key

1. Open the AWS PCS console at [https://console.aws.amazon.com/pcs/](https://console.aws.amazon.com/pcs/ "https://console.aws.amazon.com/pcs/").
2. Choose your cluster from the list.
3. In the cluster configuration details, locate the **Scheduler Authentication** section.
4. Note the **JSON Web Token (JWT) key** ARN and version.
5. Use the AWS CLI to retrieve the signing key from Secrets Manager:

```
aws secretsmanager get-secret-value --secret-id `arn:aws:secretsmanager:region:account:secret:name` --version-id `version`
```

###### To generate a JWT token

1. Create a JWT with the following required claims:
   - `exp` – Expiration time in seconds since 1970 for the JWT
   - `iat` – Current time in seconds since 1970
   - `sun` – The username for authentication
   - `uid` – The POSIX user ID
   - `gid` – The POSIX group ID
   - `id` – Additional POSIX identity properties
     - `gecos` – User comment field, often used to store a human-readable name
     - `dir` – User's home directory
     - `shell` – User's default shell
     - `gids` – List of additional POSIX group IDs the user is in

2. Sign the JWT using the signing key retrieved from Secrets Manager.
3. Set an appropriate expiration time for the token.

###### Note

As an alternative to the `sun` claim, you can provide any of the following:

- `username`
- A custom field name that you define via the `userclaimfield` in the `AuthAltParameters Slurm custom settings`
- A `name` field within the `id` claim

###### To authenticate API requests

1. Include the JWT token in your HTTP requests using one of these methods:
   - **Bearer token** – Add `Authorization: Bearer `<jwt>`` header
   - **Slurm header** – Add `X-SLURM-USER-TOKEN: `<jwt>`` header

2. Make HTTP requests to the REST API endpoint:

Here is an example of accessing the `/ping` API using curl and the `Authorized: Bearer` header.

```
curl -X GET -H "Authorization: Bearer `<jwt>`" \
      http://`<privateIpAddress>`:6820/slurm/v0.0.43/ping
```

## Example JWT generation

Fetch the AWS PCS cluster JWT signing key and store it as a local file. Replace values for **aws-region**, **secret-arn**, and **secret version** with values appropriate for your cluster.

```
#!/bin/bash
SECRET_KEY=$(aws secretsmanager get-secret-value \
  --region `aws-region` \
  --secret-id `secret-arn` \
  --version-stage `secret-version` \
  --query 'SecretString' \
  --output text)
echo "$SECRET_KEY" | base64 --decode > jwt.key
```

This Python example illustrates how to use the signing key to generate a JWT token:

```
#!/usr/bin/env python3

import sys
import os
import pprint
import json
import time
from datetime import datetime, timedelta, timezone
from jwt import JWT
from jwt.jwa import HS256
from jwt.jwk import jwk_from_dict
from jwt.utils import b64decode,b64encode
if len(sys.argv) != 3:
    sys.exit("Usage: gen_jwt.py [jwt_key_file] [expiration_time_seconds]")
SIGNING_KEY = sys.argv[1]
EXPIRATION_TIME = int(sys.argv[2])
with open(SIGNING_KEY, "rb") as f:
    priv_key = f.read()
signing_key = jwk_from_dict({
    'kty': 'oct',
    'k': b64encode(priv_key)
})
message = {
    "exp": int(time.time() + EXPIRATION_TIME),
    "iat": int(time.time()),
    "sun": "ec2-user",
    "uid": 1000,
    "gid": 1000,
    "id": {
        "gecos": "EC2 User",
        "dir": "/home/ec2-user",
        "gids": [1000],
        "shell": "/bin/bash"
    }
}
a = JWT()
compact_jws = a.encode(message, signing_key, alg='HS256')
print(compact_jws)
```

The script will print a JWT to the screen.

```
abcdefgtjwttoken...
```
