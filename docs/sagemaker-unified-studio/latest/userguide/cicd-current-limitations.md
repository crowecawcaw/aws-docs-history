# Current limitations

- Automatic rollback is not supported. Recover by redeploying a previous bundle, deploying a fix, or using the `destroy` command.
- The CLI does not create Amazon SageMaker Unified Studio domains or projects. Use existing IaC tools for infrastructure setup.
- Native notebook deployment is not yet supported.
