# Troubleshooting

## Local development issues

### Port 3000 or 3001 already in use

**Symptom:**
`npm run dev` fails with `EADDRINUSE` on port 3000 or 3001.

**Solution:** Change the dev server port, or stop the process that occupies the default port:

```
# Option 1: Find and stop the blocking process
lsof -i :3000 | grep LISTEN
kill <PID>
```

To run on a different port, set `port:` in the `startDevServer()` options in your generated `aws-blocks/scripts/server.ts`. The generated server does not read a `--port` command-line flag, so `npm run dev — --port `<n>`` has no effect:

```
startDevServer({
  // ...
  port: 3002,
});
```

### Local data is stale or corrupted

**Symptom:** Local development behaves unexpectedly, returns old data, or throws deserialization errors.

**Solution:** Delete the `.bb-data/` directory to reset all local state:

```
rm -rf .bb-data
npm run dev
```

### TypeScript errors after changing the backend

**Symptom:** Frontend shows type errors after modifying API methods in `aws-blocks/index.ts`.

**Solution:** This is expected. This means type safety is working. Update your frontend code to match the new API signature. If your IDE doesn’t pick up the changes, restart the TypeScript language server.

## Deployment issues

### CDK bootstrap required

**Symptom:**
`npm run deploy` or `npm run sandbox` fails with "This stack uses assets, so the toolkit stack must be deployed."

**Solution:** Bootstrap CDK in your account and Region:

```
npx cdk bootstrap aws://ACCOUNT_ID/REGION
```

You need to do this only one time per account/Region combination.

### AWS credentials expired or missing

**Symptom:** Deployment fails with `ExpiredTokenException` or "Unable to locate credentials."

**Solution:** Refresh your AWS credentials:

```
# If using IAM Identity Center
aws sso login

# Verify credentials work
aws sts get-caller-identity
```

### Sandbox deployment hangs or times out

**Symptom:**
`npm run sandbox` takes more than a few minutes or appears stuck.

**Solution:** This usually indicates a CloudFormation stack in a failed state. Destroy and recreate:

```
npm run sandbox:destroy
npm run sandbox
```

If `destroy` also fails, check the CloudFormation console for the stack status and manually delete if in `ROLLBACK_COMPLETE` state.

### Permission denied during deployment

**Symptom:** Deployment fails with `AccessDenied` or "User is not authorized to perform" errors.

**Solution:** Your IAM user or role needs permissions to create Lambda functions, DynamoDB tables, API Gateway APIs, IAM roles, and CloudFormation stacks. Use an account with `AdministratorAccess` for initial setup, then scope down for CI/CD.

## Runtime issues

### Behavior differs between local and deployed

**Symptom:** Code works locally but fails in production, or vice versa.

**Common causes:**

| Cause                             | Solution                                                                                  |
| --------------------------------- | ----------------------------------------------------------------------------------------- |
| DynamoDB item size limit (400 KB) | Reduce payload size or use `FileBucket` for large objects                                 |
| DynamoDB query pagination         | Handle paginated responses. Local implementations return all results in a single response |
| Aurora connection limits          | Reduce concurrent connections or configure connection pooling                             |
| Lambda cold starts                | First request after idle period is slower. Not a bug                                      |
| Environment variables missing     | Ensure CDK layer injects all required env vars via `addEnvironment`                       |

### API returns 500 Internal Server Error

**Symptom:** Frontend receives a generic 500 error without a useful message.

**Solution:** Unhandled exceptions in your API methods return as 500s without details (to avoid leaking internals). Check CloudWatch Logs for the Lambda function to see the full error and stack trace:

```
aws logs tail /aws/lambda/<stack-name>-handler --follow
```

## Getting further help

If your issue isn’t covered here:

- Check [AWS Blocks GitHub Issues](https://github.com/aws-devtools-labs/aws-blocks/issues "https://github.com/aws-devtools-labs/aws-blocks/issues") for known bugs and workarounds
- Search [AWS Blocks GitHub Discussions](https://github.com/aws-devtools-labs/aws-blocks/discussions "https://github.com/aws-devtools-labs/aws-blocks/discussions") for community solutions
- File a new issue with your error message, Node.js version, and steps to reproduce
