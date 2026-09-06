# Set up Basic or PAT authentication for Confluence Data Center

A Confluence Data Center data source supports two authentication methods: Basic
authentication and personal access token (PAT) authentication. For either method, you
create an AWS Secrets Manager secret that holds the credentials, then reference the secret ARN when
you connect the data source. Choose the method that matches how your Confluence Data
Center instance is configured.

## Basic authentication

With Basic authentication (`BASIC`), you create a secret containing a
username (the username used to log in to Confluence) and password (the Confluence
Data Center password) to allow Amazon Bedrock to connect to your Confluence Server or Data
Center instance. Use a Confluence account that has access to all the spaces, pages,
and blog posts you want to crawl.

Store the credentials in an AWS Secrets Manager secret with the following key-value
pairs:

```
{
    "username": "`your-confluence-username`",
    "password": "`your-confluence-password`"
}
```

Secret fields (Basic authentication)| Field | Description |
| --- | --- |
| `username` | The username used to log in to Confluence. |
| `password` | The Confluence Data Center password for that user. |

## Personal access token (PAT) authentication

With personal access token authentication (`PERSONAL_TOKEN`), you create
a secret containing a Confluence token to allow Amazon Bedrock to connect to your Confluence
Data Center instance. For information about how to create a PAT, see [Using Personal Access Tokens](https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html "https://confluence.atlassian.com/enterprise/using-personal-access-tokens-1026032365.html") on the Atlassian website.

Store the token in an AWS Secrets Manager secret with the following key-value pair:

```
{
    "patToken": "`your-confluence-data-center-personal-access-token`"
}
```

Secret fields (PAT authentication)| Field | Description |
| --- | --- |
| `patToken` | The Confluence Data Center account personal access token. |

## Create the Secrets Manager secret

Store the key-value pairs for your chosen method in an AWS Secrets Manager secret in the same
AWS Region as your knowledge base. Create the secret with the AWS Command Line Interface:

```
aws secretsmanager create-secret \
  --name `bedrock-confluence-onprem-creds` \
  --secret-string file://secret.json
```

Record the secret ARN from the response. You use it as the data source
`secretArn`.

## Next steps

After you store the secret, create the data source with `authType` set to
`BASIC` or `PERSONAL_TOKEN` to match the credentials you stored.
See [Connect a Confluence Data Center data source](kb-managed-ds-confluence-onprem-connect.md "kb-managed-ds-confluence-onprem-connect.md").
