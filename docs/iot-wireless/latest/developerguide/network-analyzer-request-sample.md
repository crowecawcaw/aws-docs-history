# Sample Python code to generate

presigned URL

The following code shows an example for generating the pre-signed URL using Python
as the programming language.

## Pre-requisites

To use the Python programming language to generate requests, you must
have:

- Python installed on your computer. You can either run the following
  command or download the [Python installer](https://www.python.org/downloads/ "https://www.python.org/downloads/") and then run it.

```
sudo apt install python3
```

- The Python requests library. You can either run the following command
  or download the [Requests library](https://pypi.python.org/pypi/requests "https://pypi.python.org/pypi/requests"), which is used in the example script to
  make web requests.

```
pip install requests
```

- An access key that consists of the access key ID and secret access key
  in environment variables named `AWS_ACCESS_KEY_ID` and
  `AWS_SECRET_ACCESS_KEY`. Alternatively, you can keep
  these values in a credentials file and read them from that file.

###### Note

As a best practice, we recommend that you do not embed credentials
in code. For more information, see [Best
Practices for AWS accounts](../../../accounts/latest/reference/best-practices.md "../../../accounts/latest/reference/best-practices.md") in the AWS account
Management Reference Guide.

```
$ export AWS_ACCESS_KEY_ID=My_Access_Key
$ export AWS_SECRET_ACCESS_KEY=My_Secret_Key

# Session token is required only if you use temporary access key starting with "ASIA"
$ export AWS_SESSION_TOKEN=My_Session_token
```

## Sample Python code

This Python code generates the pre-signed URL that the WebSocket library can
use to send requests to the service. The function creates a canonical request,
then creates the string to sign which is used to calculate the signature, and
then adds the signature to the HTTP request to create the pre-signed URL. You
can then use the WebSocket library to request the pre-signed URL.

To run the script, `generate_presigned_url.py`, run the following
command if you're running it from the same path where the script is
located.

```
python generate_presigned_url.py
```

The following shows the contents of the `generate_presigned_url.py`
script.

```
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

#  Version 4 signing example

"""
    Sample Python code to generate the pre-signed URL. You can
    change the parameters in this code to your own values, such
    as the variables that are required for the request URL, the
    network analyzer configuration name, and Region.
"""

# ------------------------------------------------------------------
# Step 1. Import the required libraries and define the functions
# sign and getSignatureKey that will be used to derive a signing key.
# ------------------------------------------------------------------
import sys, os, base64, datetime, hashlib, hmac, urllib.pars
import requests     # pip install requests

def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

def getSignatureKey(key, dateStamp, regionName, serviceName):
    kDate = sign(("AWS4" + key).encode("utf-8"), dateStamp)
    kRegion = sign(kDate, regionName)
    kService = sign(kRegion, serviceName)
    kSigning = sign(kService, "aws4_request")
    return kSigning

# ------------------------------------------------------------------
# Step 2. Define the variables required for the request URL. Replace
# values for the variables, such as region, with your own values.
# ------------------------------------------------------------------
method = "GET"
service = "iotwireless"
region = "us-east-1"

# Host and endpoint information.
host = "api.iotwireless." + region + ".amazonaws.com"
endpoint = "wss://" + host

# Create a date for headers and the credential string.
t = datetime.datetime.utcnow()
amz_date = t.strftime("%Y%m%dT%H%M%SZ")

# For date stamp, the date without time is used in credential scope.
datestamp = t.strftime("%Y%m%d")

# -----------------------------------------------------------------------
# Step 3. Create the canonical URI and canonical headers for the request.
# -----------------------------------------------------------------------
canonical_uri = "/start-network-analyzer-stream"
configuration_name = "My_Network_Analyzer_Config"

canonical_headers = "host:" + host + "\n"
signed_headers = "host"
algorithm = "AWS4-HMAC-SHA256"
credential_scope = datestamp + "/" + region + "/" + service + "/" + "aws4_request"

# -----------------------------------------------------------------------
# Step 4. Read the  credentials that are required for the request
# from environment variables or configuration file.
# -----------------------------------------------------------------------

# IMPORTANT: Best practice is NOT to embed credentials in code.

access_key = os.environ.get("AWS_ACCESS_KEY_ID")
secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
token = os.environ.get("AWS_SESSION_TOKEN")

if access_key is None or secret_key is None:
    print("No access key is available.")
    sys.exit()

if access_key.startswith("ASIA") and token is None:
    print("Detected temporary credentials. You must specify a token.")
    sys.exit()

# ----------------------------------------------------------------------
# Step 5. Create the canonical query string. Query string values must be
# URI-encoded and sorted by name. Query headers must in alphabetical order.
# ----------------------------------------------------------------------
    canonical_querystring  = "X-Amz-Algorithm=" + algorithm

    canonical_querystring += "&X-Amz-Credential=" + \
    urllib.parse.quote(access_key + "/" + credential_scope, safe="-_.~")

    canonical_querystring += "&X-Amz-Date=" + amz_date
    canonical_querystring += "&X-Amz-Expires=300"

    if access_key.startswith("ASIA"):
        # percent encode the token and double encode "="
        canonical_querystring += "&X-Amz-Security-Token=" + \
        urllib.parse.quote(token, safe="-_.~").replace("=", "%253D")

    canonical_querystring += "&X-Amz-SignedHeaders=" + signed_headers
    canonical_querystring += "&configuration-name=" + configuration_name

# ----------------------------------------------------------------------
# Step 6. Create a hash of the payload.
# ----------------------------------------------------------------------
payload_hash = hashlib.sha256(("").encode("utf-8")).hexdigest()

# ------------------------------------------------------------------
# Step 7. Combine the elements, which includes the query string, the
# headers, and the payload hash, to form the canonical request.
# ------------------------------------------------------------------
canonical_request = method + "\n" + canonical_uri + "\n" + canonical_querystring \
+ "\n" + canonical_headers + "\n" + signed_headers + "\n" + payload_hash

# ----------------------------------------------------------------------
# Step 8. Create the metadata string to store the information required to
# calculate the signature in the following step.
# ----------------------------------------------------------------------
string_to_sign = algorithm + "\n" + amz_date + "\n" + \
credential_scope + "\n" + hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()

# ----------------------------------------------------------------------
# Step 9. Calculate the signature by using a signing key that"s obtained
# from your secret key.
# ----------------------------------------------------------------------
# Create the signing key from your  secret key.
signing_key = getSignatureKey(secret_key, datestamp, region, service)

# Sign the string_to_sign using the signing key.
signature = hmac.new(signing_key, (string_to_sign).encode("utf-8"), hashlib.sha256).hexdigest()

# ----------------------------------------------------------------------
# Step 10. Create the request URL using the calculated signature and by
# combining it with the canonical URI and the query string.
# ----------------------------------------------------------------------
canonical_querystring += "&X-Amz-Signature=" + signature

request_url = endpoint + canonical_uri + "?" + canonical_querystring

print("\n-----------PRESIGNED URL-----------")
print(request_url)
```

## Next steps

You can now use the request URL with your WebSocket library to make the
request to the service and observe the messages.

To install a WebSocket library to use with Python, run the following command.
For information about how you can use a WebSocket client with Python, see [WebSocket client for Python
with low level API options](https://pypi.org/project/websocket-client/ "https://pypi.org/project/websocket-client/").

```
pip install websocket-client
```

After you install the client and make the request, you'll see messages and
status codes that indicate the status of your request. For more information, see
[WebSocket messages and status
codes](network-analyzer-messages-status.md "network-analyzer-messages-status.md").
