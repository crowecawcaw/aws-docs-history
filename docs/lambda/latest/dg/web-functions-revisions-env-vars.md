

# Environment variables
<a name="web-functions-revisions-env-vars"></a>

Environment variables are key-value pairs that are available to your application code at runtime. Use environment variables for non-sensitive configuration that you want to change without modifying code, such as feature flags, log levels, and resource identifiers like a database host name. For sensitive values such as API keys and database credentials, don't store them in environment variables. Instead, use Secrets Manager or AWS Systems Manager Parameter Store and retrieve the values at runtime.

Environment variables are set when you create the revision and are immutable after creation. To change an environment variable, create a new revision. In the new revision, specify every environment variable and every `serviceConfig` setting that you want to keep, not only the values that change. Settings that you omit take their default values, and environment variables that you omit aren't set.

Lambda sets the following environment variable specifically for Web Functions:
+ **`AWS_LAMBDA_HTTP_ENDPOINT`** – The host and port that your HTTP server must listen on, in `host:port` format. Lambda sets this variable and routes requests to that address. Read it in your application code and bind exactly that host and port. You can't set this variable in a revision's environment variables. Always bind to the address in this variable, not `localhost` or a hardcoded port. The runtime waits for your server to accept a connection at this address, and initialization fails if it never does. Use a fallback address only for local runs. In a Web Function, Lambda always sets this variable.

Web Functions also receive other Lambda runtime environment variables, such as `AWS_LAMBDA_FUNCTION_MEMORY_SIZE`, `AWS_LAMBDA_METADATA_API`, and `AWS_LAMBDA_METADATA_TOKEN`. For the general list, see [Defined runtime environment variables](configuration-envvars.md#configuration-envvars-runtime). If your code or a library reads a variable from that list, confirm that Lambda sets it in a Web Function before you rely on it. Web Functions don't receive every variable in that list.

The following environment variable names are reserved for Lambda Web Functions and can't be set. If you specify one, Lambda rejects the request to create a Web Function or revision:
+ `AWS_ACCESS_KEY`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SECRET_KEY`, `AWS_SECURITY_TOKEN`, and `AWS_SESSION_TOKEN`
+ `AWS_DEFAULT_REGION` and `AWS_REGION`
+ `AWS_LAMBDA_HTTP_ENDPOINT`, `AWS_LAMBDA_RUNTIME_API`, `AWS_LAMBDA_INITIALIZATION_TYPE`, and `AWS_LAMBDA_FUNCTION_MEMORY_SIZE`
+ `AWS_LAMBDA_METADATA_API` and `AWS_LAMBDA_METADATA_TOKEN`

Some frameworks read their own environment variables for the listen address instead. For example, Next.js standalone mode reads `HOSTNAME` and `PORT`. For such frameworks, use an `index.js` entry file that sets those variables from `AWS_LAMBDA_HTTP_ENDPOINT` before starting the server.

By default, the runtime loads `index.js` at the root of your deployment package as your application's entry file. The runtime does not read the entry point from `package.json`. If your entry file has a different name or path (for example, `dist/index.js`), set the `AWS_LAMBDA_NODEJS_ENTRYPOINT` environment variable to its path, relative to the root of your package.

The following example shows how to read the `AWS_LAMBDA_HTTP_ENDPOINT` environment variable in a Node.js application:

```
// Lambda provides the address to bind in AWS_LAMBDA_HTTP_ENDPOINT ("host:port").
// The fallback applies only when running locally.
const [host, port] = (process.env.AWS_LAMBDA_HTTP_ENDPOINT || 'localhost:3000').split(':');
app.listen(port, host, () => {
  console.log(`Server listening on ${host}:${port}`);
});
```

To set your own environment variables, add an `environmentVariables` map to the `serviceConfig` object when you create a revision, as in the following example. For the full command, see [Creating a revision](web-functions-revisions.md#web-functions-revisions-create).

```
{
  "executionRoleArn": "arn:aws:iam::{{111122223333}}:role/{{my-web-function-role}}",
  "environmentVariables": {
    "DATABASE_URL": "{{my-database-endpoint}}",
    "LOG_LEVEL": "info",
    "FEATURE_FLAG_NEW_UI": "true"
  }
}
```

If you specify a customer managed key, Lambda encrypts environment variables at rest with that key. For more information, see [Encryption at rest for Web Functions](web-functions-encryption.md).