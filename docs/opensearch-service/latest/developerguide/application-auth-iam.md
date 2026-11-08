

# IAM authentication for OpenSearch UI
<a name="application-auth-iam"></a>

This topic covers the minimum IAM permissions required to access an OpenSearch UI application that uses IAM authentication, without AWS IAM Identity Center. After you complete these steps, an IAM role can sign in to the application and query its data sources.

## Prerequisites
<a name="application-auth-iam-prerequisites"></a>
+ An OpenSearch UI application created with IAM authentication. For instructions on creating an application, see [Getting started with the OpenSearch user interface in Amazon OpenSearch Service](application-getting-started.md).
+ An IAM role that needs access to the application.
+ The AWS CLI configured with credentials.

## Step 1: Grant the IAM permission
<a name="application-auth-iam-grant"></a>

The following IAM policy grants access to the application interface. Attach it to the IAM role that needs access, and replace the placeholder values with your own information:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "opensearch:ApplicationAccessAll",
            "Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:application/{{application-id}}"
        }
    ]
}
```

Scoping the resource to a single application ID grants the least privilege that the role needs. To grant access to every application in the account and Region instead, use a wildcard:

```
"Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:application/*"
```

You can attach the same policy with the AWS CLI:

```
aws iam put-role-policy \
    --role-name {{role-name}} \
    --policy-name OpenSearchAppAccess \
    --policy-document '{
      "Version":"2012-10-17",
      "Statement":[{
        "Effect":"Allow",
        "Action":"opensearch:ApplicationAccessAll",
        "Resource":"arn:aws:opensearch:{{region}}:{{account-id}}:application/{{application-id}}"
      }]
    }'
```

**Note**  
The action that grants access to the application interface is `opensearch:ApplicationAccessAll`. For more information about the permissions that an application requires, see [IAM policy reference for OpenSearch UI](application-iam-policy-reference.md).

If your users also open the application from the AWS Management Console, add the following statement, so they can view the application in the console:

```
{
    "Effect": "Allow",
    "Action": "es:GetApplication",
    "Resource": "arn:aws:opensearch:{{region}}:{{account-id}}:application/{{application-id}}"
}
```

## Step 2: Configure the dashboard administrator
<a name="application-auth-iam-admin"></a>

Set which IAM principals receive administrator privileges inside OpenSearch UI. To grant administrator privileges to all authenticated users, run the following command:

```
aws opensearch update-application \
    --id {{application-id}} \
    --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"*"}]' \
    --region {{region}}
```

To grant administrator privileges to a single role, specify the role ARN:

```
aws opensearch update-application \
    --id {{application-id}} \
    --app-configs '[{"key":"opensearchDashboards.dashboardAdmin.users","value":"arn:aws:iam::{{account-id}}:role/{{role-name}}"}]' \
    --region {{region}}
```

**Note**  
The dashboard administrator setting controls administrator features inside the interface, such as index pattern management and saved objects. You don't need it to sign in—the IAM policy in step 1 is sufficient to access the application.

## Step 3: Verify access
<a name="application-auth-iam-verify"></a>

You can verify access from a browser with a presigned URL, or programmatically with Signature Version 4 request headers.

### Verify access from a browser
<a name="application-auth-iam-verify-browser"></a>

The following Python code example generates a Signature Version 4 presigned URL that you open in a browser:

```
from botocore.session import Session
from botocore.auth import SigV4QueryAuth
from botocore.awsrequest import AWSRequest

session = Session()
cred = session.get_credentials().get_frozen_credentials()

endpoint = "{{application-endpoint}}"
region = "{{region}}"

url = f"https://{endpoint}/_login/"
request = AWSRequest(method="GET", url=url)
SigV4QueryAuth(cred, "opensearch", region, expires=300).add_auth(request)

print(request.url)  # Open this URL in a browser
```

**Note**  
The `/_login/` presigned URL works only in a browser. It does not work with `curl` or other HTTP clients.

### Verify access programmatically
<a name="application-auth-iam-verify-programmatic"></a>

The following Python code example signs a request to the application endpoint with Signature Version 4 headers:

```
from botocore.session import Session
from botocore.auth import SigV4Auth
from botocore.awsrequest import AWSRequest
import subprocess

session = Session()
cred = session.get_credentials().get_frozen_credentials()

endpoint = "{{application-endpoint}}"
region = "{{region}}"

url = f"https://{endpoint}/"
request = AWSRequest(method="GET", url=url)
SigV4Auth(cred, "opensearch", region).add_auth(request)

cmd = ["curl", "-s", "-w", "\nHTTP: %{http_code}\n", "-D", "-"]
for k, v in request.headers.items():
    cmd.extend(["-H", f"{k}: {v}"])
cmd.append(url)

result = subprocess.run(cmd, capture_output=True, text=True)
print(result.stdout)
```

A successful request returns `HTTP/1.1 302 Found` with a `location` header of `/app/workspace_initial`. A request that returns `HTTP/1.1 403 Forbidden` indicates a problem with the IAM policy.

## Signature Version 4 signing details
<a name="application-auth-iam-sigv4"></a>

The following table lists the Signature Version 4 parameters that OpenSearch UI expects.


| Parameter | Value | 
| --- | --- | 
| Service name | opensearch | 
| Algorithm | AWS4-HMAC-SHA256 | 
| Signed headers | host, at a minimum | 
| Presigned URL expiry | No more than 300 seconds is recommended | 

**Important**  
The Signature Version 4 service name is `opensearch`. Signing with `es` or `aoss` causes the request to fail.

## Configuration summary
<a name="application-auth-iam-summary"></a>

The following table lists what each configuration layer controls.


| Layer | Configuration | Required to sign in? | 
| --- | --- | --- | 
| IAM policy | opensearch:ApplicationAccessAll on the application ARN | Yes | 
| IAM policy | es:GetApplication on the application ARN | Only to open the application from the AWS Management Console | 
| Application configuration | opensearchDashboards.dashboardAdmin.users | No—it controls administrator features only | 

## Troubleshooting IAM authentication
<a name="application-auth-iam-troubleshooting"></a>

IAM authentication problems usually come from a missing policy action, a presigned URL used outside a browser, or a request signed with the wrong service name. The following table lists common symptoms, their likely causes, and how to resolve each one.


| Symptom | Likely cause | Resolution | 
| --- | --- | --- | 
| 403 Forbidden when you open the application URL | The opensearch:ApplicationAccessAll permission is missing | Add the IAM policy from step 1 | 
| 403 with a message that you are not authorized to perform es:GetApplication | The console permission is missing | Add es:GetApplication on the application ARN. This is required only for AWS Management Console access | 
| 400 Bad Request on /\_login/ with curl | The /\_login/ endpoint works only in a browser | Use Signature Version 4 header authentication on / for programmatic access | 
| The presigned URL returns SignatureDoesNotMatch | The Signature Version 4 service name is wrong | Sign the request with opensearch, not es or aoss | 
| You can open the application but administrator features are missing | The dashboard administrator is not configured | Run update-application with opensearchDashboards.dashboardAdmin.users, as described in step 2 | 
| The presigned URL has expired | The URL was generated more than 300 seconds earlier | Generate a new presigned URL. Presigned URLs are short-lived | 

For more information about the IAM actions that OpenSearch UI uses, see [IAM policy reference for OpenSearch UI](application-iam-policy-reference.md).