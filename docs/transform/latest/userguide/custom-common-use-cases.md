

# Common Use Cases
<a name="custom-common-use-cases"></a>

This section provides step-by-step guidance for common transformation scenarios using the AWS Transform CLI.

## Lambda Runtime Upgrades
<a name="custom-use-case-lambda-runtime-upgrades"></a>

Lambda periodically deprecates older language runtimes, requiring teams to upgrade their Lambda functions to supported versions. AWS Transform custom can automate these upgrades using the AWS-managed language version upgrade transformations. For example, to upgrade a Lambda function written in Python 3.9 to Python 3.13, you would use the `AWS/python-version-upgrade` transformation. Similar transformations are available for Java (`AWS/java-version-upgrade`) and Node.js (`AWS/nodejs-version-upgrade`), covering the most common Lambda runtime languages.

To upgrade a single Lambda function interactively, navigate to the root of your function's source repository and start the AWS Transform CLI with `atx`. In the interactive session, describe the upgrade you need—for example, "Upgrade this Python 3.9 Lambda function to Python 3.13." The agent will select the appropriate AWS-managed transformation, analyze your code, update language syntax, adjust dependencies, and modernize deprecated API calls. You can provide a build or validation command such as `pytest` or `python -m py_compile *.py` so the agent can verify the transformed code compiles and passes tests. Throughout the interactive session, you can review the agent's proposed changes, provide feedback, and request adjustments before accepting the final result.

When you need to upgrade Lambda runtimes across many repositories, use non-interactive mode to run transformations at scale. For each repository, invoke the CLI with the appropriate flags to run without user input. For example, to upgrade a Node.js 16 Lambda function to Node.js 22:

```
atx custom def exec \
  -n AWS/nodejs-version-upgrade \
  -p ./my-lambda-repo \
  -c "npm test" \
  -g "additionalPlanContext='Upgrade from Node.js 16 to Node.js 22'" \
  -x -t
```

The `-x` flag runs the transformation non-interactively, and `-t` trusts all tool executions so no prompts are required. You can script this command across dozens or hundreds of repositories using a simple shell loop. After each transformation completes, review the Git diff to verify the changes and run your test suite to confirm the upgraded function works correctly. You can also integrate AWS Transform custom into your CI/CD pipeline to identify deprecated Lambda functions on an ongoing basis. This approach not only addresses the immediate problem of deprecated runtimes, but also establishes a continuous process to detect and upgrade functions before they reach end-of-support status.

Central platform teams can create campaigns through the [AWS Transform web application](https://docs.aws.amazon.com/transform/latest/userguide/custom-get-started.html#custom-web-application) to define the transformation, specify target Lambda repositories, and track progress across the organization. For a detailed walkthrough of building a production-grade scaled deployment solution using AWS Batch, see [Building a scalable code modernization solution with AWS Transform custom](https://aws.amazon.com/blogs/devops/building-a-scalable-code-modernization-solution-with-aws-transform-custom/).