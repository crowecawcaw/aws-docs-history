# Amazon ECR Public troubleshooting

This chapter helps you find diagnostic information for Amazon ECR Public, and provides
troubleshooting steps for common issues and error messages.

###### Topics

- [Authentication issues](#public-troubleshooting-authentication "#public-troubleshooting-authentication")

## Authentication issues

**Issue:** When performing an unauthenticated pull from
an Amazon ECR Public repository, you receive an authentication token expired response. This
is likely due to the fact that you've previously requested an authentication token from
Amazon ECR Public and that token has expired. When the new Amazon ECR Public image pull is
performed, the expired token is used and the error is received. The following is an
example error.

```
Error response from daemon: pull access denied for public.ecr.aws/`registry_alias`/`repository_name`, repository does not exist or may require 'docker login': denied: Your authorization token has expired. Reauthenticate and try again.
```

**Resolution:** To resolve this issue, you can either
re-authenticate to Amazon ECR Public or you can log your Docker CLI out of the Amazon ECR Public
registry and re-attempt your unauthenticated image pull.

```
`docker logout public.ecr.aws`
```
