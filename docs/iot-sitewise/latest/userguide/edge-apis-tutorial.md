# Tutorial: List asset models on an AWS IoT SiteWise Edge

gateway

You can use a subset of the available AWS IoT SiteWise APIs along with edge-specific APIs to
interact with asset models and their assets on the edge. This tutorial will walk you
through getting temporary credentials to an AWS IoT SiteWise Edge gateway and getting a list
of the asset models on the SiteWise Edge gateway.

## Prerequisites

In the steps of this tutorial you can use a variety of tools. To use these
tools, make sure you have the corresponding prerequisites installed.

To complete this tutorial, you need the following:

- A deployed and running [AWS IoT SiteWise Edge self-hosted gateway
  requirements](configure-gateway-ggv2.md "configure-gateway-ggv2.md")
- Access to your SiteWise Edge gateway in the same network over port

443.

- [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/") installed
- (AWS OpsHub for AWS IoT SiteWise) The [AWS OpsHub for AWS IoT SiteWise application](manage-gateways-ggv2.md#opshub-app "manage-gateways-ggv2.md#opshub-app")
- (curl) [curl](https://ec.haxx.se/install/ "https://ec.haxx.se/install/")
  installed
- (Python) [urllib3](https://urllib3.readthedocs.io/en/stable/index.html "https://urllib3.readthedocs.io/en/stable/index.html") installed
- (Python) [Python3](https://www.python.org/downloads/ "https://www.python.org/downloads/") installed
- (Python) [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html") installed
- (Python) [BotoCore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html "https://botocore.amazonaws.com/v1/documentation/api/latest/index.html") installed

## Step 1: Get a SiteWise Edge gateway

service signed certificate

To establish a TLS connection to the APIs available at the SiteWise Edge gateway,
you need a trusted certificate. You can generate this certificate using a
OpenSSL or AWS OpsHub for AWS IoT SiteWise.

OpenSSL

###### Note

You need [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/")
installed to run this command.

Open a terminal and run the following command to get a signed
certificate from the SiteWise Edge gateway. Replace
`<sitewise_gateway_ip>` with the IP of the
SiteWise Edge gateway.

```
`openssl s_client -connect `<sitewise_gateway_ip>`:443 </dev/null 2>/dev/null | openssl x509 -outform PEM > GatewayCert.pem`
```

AWS OpsHub for AWS IoT SiteWise
You can use AWS OpsHub for AWS IoT SiteWise. For more information, see [Manage SiteWise Edge gateways](manage-gateways-ggv2.md "manage-gateways-ggv2.md").

The absolute path to the downloaded SiteWise Edge gateway certificate is used in
this tutorial. Run the following command to export the complete path of your
certificate, replacing `<absolute_path_to_certificate>` with
the path to the certificate:

```
`export PATH_TO_CERTIFICATE='`<absolute_path_to_certificate>`'`
```

## Step 2: Get your SiteWise Edge

gateway hostname

###### Note

You need [OpenSSL](https://www.openssl.org/ "https://www.openssl.org/") installed
to run this command.

To complete the tutorial you'll need the hostname of your SiteWise Edge gateway. To
get the hostname of your SiteWise Edge gateway, run the following, replacing
`<sitewise_gateway_ip>` with the IP of the SiteWise Edge
gateway:

```
`openssl s_client -connect `<sitewise_gateway_ip>`:443 </dev/null 2>/dev/null | grep -Po 'CN = \K.*'| head -1`
```

Run the following command to export the hostname for use later, replacing
`<your_edge_gateway_hostname>` with the hostname of your
SiteWise Edge gateway:

```
`export GATEWAY_HOSTNAME='`<your_edge_gateway_hostname>`'`
```

## Step 3: Get temporary

credentials for your SiteWise Edge gateway

Now that you have the signed certificate and the hostname of your SiteWise Edge
gateway, you need to get temporary credentials so you can run APIs on the
gateway. You can get these credentials through AWS OpsHub for AWS IoT SiteWise or directly
from the SiteWise Edge gateway using APIs.

###### Important

Credentials expire every 4 hours, so you should get the credentials just
before using the APIs on your SiteWise Edge gateway. Don't cache credentials for
longer than 4 hours.

### Get temporary

credentials using AWS OpsHub for AWS IoT SiteWise

###### Note

You need the [AWS OpsHub for AWS IoT SiteWise application](manage-gateways-ggv2.md#opshub-app "manage-gateways-ggv2.md#opshub-app") installed.

To use AWS OpsHub for AWS IoT SiteWise application to get your temporary credentials
do the following:

1. Log into the application.
2. Choose **Settings**.
3. For **Authentication**, choose **Copy
   credentials**.
4. Expand the option that fits your environment and choose
   **Copy**.
5. Save the credentials for use later.

### Get temporary

credentials using the SiteWise Edge gateway API

To use the SiteWise Edge gateway API to get the temporary credentials you can
use a Python script or curl, first you'll need to have a user name and
password for your SiteWise Edge gateway. The SiteWise Edge gateways use SigV4
authentication and authorization. For more information about adding users,
see [LDAP](manage-gateways-ggv2.md#opshub-app "manage-gateways-ggv2.md#opshub-app") or [Linux user pool](manage-gateways-ggv2.md#opshub-app "manage-gateways-ggv2.md#opshub-app"). These credentials will be used in the
following steps to get the local credentials on your SiteWise Edge gateway that
are needed to use the AWS IoT SiteWise APIs.

Python

###### Note

You need [urllib3](https://urllib3.readthedocs.io/en/stable/index.html "https://urllib3.readthedocs.io/en/stable/index.html") and [Python3](https://www.python.org/downloads/ "https://www.python.org/downloads/")
installed.

###### To get the credentials using Python

1. Create a file called
   **get_credentials.py** and the copy
   the following code into it.

```
'''
The following demonstrates how to get the credentials from the SiteWise Edge gateway. You will need to add local users or connect your system to LDAP/AD
https://docs.aws.amazon.com/iot-sitewise/latest/userguide/manage-gateways-ggv2.html#create-user-pool

Example usage:
    python3 get_credentials.py -e https://<gateway_hostname> -c <path_to_certificate> -u '<gateway_username>' -p '<gateway_password>' -m '<method>'
'''
import urllib3
import json
import urllib.parse
import sys
import os
import getopt

"""
This function retrieves the AWS IoT SiteWise Edge gateway credentials.
"""
def get_credentials(endpoint,certificatePath, user, password, method):
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs= certificatePath)
    encoded_body = json.dumps({
        "username": user,
        "password": password,
        "authMechanism": method,
    })

    url =  urllib.parse.urljoin(endpoint, "/authenticate")

    response = http.request('POST', url,
        headers={'Content-Type': 'application/json'},
        body=encoded_body)

    if response.status != 200:
        raise Exception(f'Failed to authenticate! Response status {response.status}')

    auth_data = json.loads(response.data.decode('utf-8'))

    accessKeyId = auth_data["accessKeyId"]
    secretAccessKey = auth_data["secretAccessKey"]
    sessionToken = auth_data["sessionToken"]
    region = "edge"

    return accessKeyId, secretAccessKey, sessionToken, region

def print_help():
    print('Usage:')
    print(f'{os.path.basename(__file__)} -e <endpoint> -c <path/to/certificate> -u <user> -p <password> -m <method> -a <alias>')
    print('')
    print('-e, --endpoint   edge gateway endpoint. Usually the Edge gateway hostname.')
    print('-c, --cert_path path to downloaded gateway certificate')
    print('-u, --user       Edge user')
    print('-p, --password   Edge password')
    print('-m, --method     (Optional) Authentication method (linux, winnt, ldap), default is linux')
    sys.exit()


def parse_args(argv):
    endpoint = ""
    certificatePath = None
    user = None
    password = None
    method = "linux"

    try:
        opts, args = getopt.getopt(argv, "he:c:u:p:m:", ["endpoint=","cert_path=", "user=", "password=", "method="])
    except getopt.GetoptError:
        print_help()

    for opt, arg in opts:
        if opt == '-h':
            print_help()
        elif opt in ("-e", "--endpoint"):
            endpoint = arg
        elif opt in ("-u", "--user"):
            user = arg
        elif opt in ("-p", "--password"):
            password = arg
        elif opt in ("-m", "--method"):
            method = arg.lower()
        elif opt in ("-c", "--cert_path"):
            certificatePath = arg

    if method not in ['ldap', 'linux', 'winnt']:
        print("not valid method parameter, required are ldap, linux, winnt")
        print_help()

    if (user == None or password == None):
        print("To authenticate against edge user, password have to be passed together, and the region has to be set to 'edge'")
        print_help()

    if(endpoint == ""):
        print("You must provide a valid and reachable gateway hostname")
        print_help()

    return endpoint,certificatePath, user, password, method


def main(argv):
    # get the command line args
    endpoint, certificatePath, user, password, method = parse_args(argv)

    accessKeyId, secretAccessKey, sessionToken, region=get_credentials(endpoint, certificatePath, user, password, method)

    print("Copy and paste the following credentials into the shell, they are valid for 4 hours:")
    print(f"export AWS_ACCESS_KEY_ID={accessKeyId}")
    print(f"export AWS_SECRET_ACCESS_KEY={secretAccessKey}")
    print(f"export AWS_SESSION_TOKEN={sessionToken}")
    print(f"export AWS_REGION={region}")
    print()




if __name__ == "__main__":
   main(sys.argv[1:])

```

2. Run **get_credentials.py** from the
   terminal replacing `<gateway_username>`
   and `<gateway_password>` with the
   credentials you created.

```
`python3 get_credentials.py -e https://$GATEWAY_HOSTNAME -c $PATH_TO_CERTIFICATE -u '`<gateway_username>`' -p '`<gateway_password>`' -m 'linux'`
```

curl

###### Note

You need [curl](https://ec.haxx.se/install/ "https://ec.haxx.se/install/") installed.

###### To get the credentials using curl

1. Run the following command from the terminal replacing
   <gateway_username> and <gateway_password>
   with the credentials you created.

```
`curl --cacert $PATH_TO_CERTIFICATE --location \
-X POST https://$GATEWAY_HOSTNAME:443/authenticate \
--header 'Content-Type: application/json' \
--data-raw '{
 "username": "<gateway_username>",
 "password": "<gateway_password>",
 "authMechanism": "linux"
}'`
```

The response should look like the following:

```
{
    "username": "sweuser",
    "accessKeyId": "<accessKeyId>",
    "secretAccessKey": "<secretAccessKey>",
    "sessionToken": "<sessionToken>",
    "sessionExpiryTime": "2022-11-17T04:51:40.927095Z",
    "authMechanism": "linux",
    "role": "edge-user"
}
```

2. Run the following command from your terminal.

```
export AWS_ACCESS_KEY_ID=<accessKeyId>
export AWS_SECRET_ACCESS_KEY=<secretAccessKey>
export AWS_SESSION_TOKEN=<sessionToken>
export AWS_REGION=edge
```

## Step 4: Get a list of the

asset models on the SiteWise Edge gateway

Now that you have a signed certificate, your SiteWise Edge gateway hostname, and
temporary credentials for your SiteWise Edge gateway, you can use the
`ListAssetModels` API to get a list of the asset models on your
SiteWise Edge gateway.

Python

###### Note

You need [Python3](https://www.python.org/downloads/ "https://www.python.org/downloads/"), [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html "https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html"), and [BotoCore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html "https://botocore.amazonaws.com/v1/documentation/api/latest/index.html") installed.

###### To get the the list of asset models using Python

1. Create a file called
   **list_asset_model.py** and the copy
   the following code into it.

```
import json
import boto3
import botocore
import os

# create the client using the credentials
client = boto3.client("iotsitewise",
    endpoint_url= "https://"+ os.getenv("GATEWAY_HOSTNAME"),
    region_name=os.getenv("AWS_REGION"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    aws_session_token=os.getenv("AWS_SESSION_TOKEN"),
    verify=os.getenv("PATH_TO_CERTIFICATE"),
    config=botocore.config.Config(inject_host_prefix=False))

# call the api using local credentials
response = client.list_asset_models()
print(response)
```

2. Run **list_asset_model.py** from the
   terminal.

```
`python3 list_asset_model.py`
```

curl

###### Note

You need [curl](https://ec.haxx.se/install/ "https://ec.haxx.se/install/")
installed.

**To get the list of asset models using
curl**

Run the following command from the terminal.

```
`curl \
 --request GET https://$GATEWAY_HOSTNAME:443/asset-models \
 --cacert $PATH_TO_CERTIFICATE \
 --aws-sigv4 "aws:amz:edge:iotsitewise" \
 --user "$AWS_ACCESS_KEY_ID:$AWS_SECRET_ACCESS_KEY" \
 -H "x-amz-security-token:$AWS_SESSION_TOKEN"`
```

The response should look like the following:

```
{
    "assetModelSummaries": [
        {
            "arn": "arn:aws:iotsitewise:{region}:{account-id}:asset-model/{asset-model-id}",
            "creationDate": 1.669245291E9,
            "description": "This is a small example asset model",
            "id": "{asset-model-id}",
            "lastUpdateDate": 1.669249038E9,
            "name": "Some Metrics Model",
            "status": {
                "error": null,
                "state": "ACTIVE"
            }
        },
        .
        .
        .
    ],
    "nextToken": null
}

```
