# Use awscurl to query with

Prometheus-compatible APIs

API requests for Amazon Managed Service for Prometheus must be signed with [SigV4](../../../general/latest/gr/signature-version-4.md "../../../general/latest/gr/signature-version-4.md"). You can use [awscurl](https://github.com/okigan/awscurl "https://github.com/okigan/awscurl") to simplify the querying process.

To install `awscurl`, you need to have Python 3 and pip package manager
installed.

On a Linux based instance, the following command installs
`awscurl`.

```
`$` pip3 install awscurl
```

On a macOS machine, the following command installs `awscurl`.

```
`$` brew install awscurl
```

The following example is a sample `awscurl` query. Replace the
`Region`, `Workspace-id` and
`QUERY` inputs with appropriate values for your use
case:

```
# Define the Prometheus query endpoint URL. This can be found in the Amazon Managed Service for Prometheus console page
# under the respective workspace.

`$` export AMP_QUERY_ENDPOINT=https://aps-workspaces.`Region`.amazonaws.com/workspaces/`Workspace-id`/api/v1/query

# credentials are infered from the default profile
`$` awscurl -X POST --region `Region` \
                  --service aps "${AMP_QUERY_ENDPOINT}" -d 'query=`QUERY`'  --header 'Content-Type: application/x-www-form-urlencoded'
```

###### Note

Your query string must be url encoded.

For a query like `query=up`, you could get results such as:

```
{
  "status": "success",
  "data": {
    "resultType": "vector",
    "result": [
      {
        "metric": {
          "__name__": "up",
          "instance": "localhost:9090",
          "job": "prometheus",
          "monitor": "monitor"
        },
        "value": [
          1652452637.636,
          "1"
        ]
      },
    ]
  }
}
```

In order for `awscurl` to sign the provided requests, you will need to
pass the valid credentials in one of the following ways:

- Provide the access key ID and the Secret key for the IAM role. You can
  find the access key and the secret key for the role in the
  [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").

For example:

```
`$` export AMP_QUERY_ENDPOINT=https://aps-workspaces.`Region`.amazonaws.com/workspaces/`Workspace_id`/api/v1/query

`$` awscurl -X POST --region <Region> \
                  --access_key <ACCESS_KEY> \
                  --secret_key <SECRET_KEY> \
                  --service aps "$AMP_QUERY_ENDPOINT?query=<QUERY>"
```

- Reference the configuration files stored in the
  `.aws/credentials` and `/aws/config` file. You can
  also choose to specify the name of the profile to be used. If unspecified,
  the `default` file will be used. For example:

```
`$` export AMP_QUERY_ENDPOINT=https://aps-workspaces.<Region>.amazonaws.com/workspaces/<Workspace_ID>/api/v1/query
`$` awscurl -X POST --region <Region> \
                  --profile <PROFILE_NAME>
                  --service aps "$AMP_QUERY_ENDPOINT?query=<QUERY>"
```

- Use the instance profile associated with the EC2 instance.

## Executing query requests using awscurl

container

When installing a different version of **Python** and the
associated dependencies is not feasible, a container can be used to package the
`awscurl` application and its dependencies. The following example
uses a **Docker** runtime to deploy `awscurl`, but
any OCI compliant runtime and image will work.

```
`$` docker pull okigan/awscurl
`$` export AMP_QUERY_ENDPOINT=https://aps-workspaces.`Region`.amazonaws.com/workspaces/`Workspace_id`/api/v1/query
`$` docker run --rm -it okigan/awscurl --access_key $AWS_ACCESS_KEY_ID  --secret_key $AWS_SECRET_ACCESS_KEY \ --region `Region` --service aps "$AMP_QUERY_ENDPOINT?query=`QUERY`"
```
