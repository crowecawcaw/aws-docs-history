# Debug builds in AWS CodeBuild

AWS CodeBuild provides two methods for debugging builds during development and
troubleshooting. You can use the CodeBuild Sandbox environment to investigate issues and
validate fixes in real-time, or you can use AWS Systems Manager Session Manager to connect
to the build container and view the container state.

## Debug builds with CodeBuild sandbox

The CodeBuild sandbox environment provides an interactive debug session in a secure
and isolated environment. You can interact with the environment directly through the
AWS Management Console or AWS CLI, execute commands, and validate your build process step by step. It
uses a cost-effective per-second billing model and supports the same native integration
with source providers and AWS services as your build environment. You can also connect
to a sandbox environment using SSH clients or from your integrated development
environments (IDEs).

To learn more about the CodeBuild sandbox pricing, visit the [CodeBuild pricing
documentation](https://aws.amazon.com/codebuild/pricing/#Sandbox "https://aws.amazon.com/codebuild/pricing/#Sandbox"). For detailed instructions, visit the [Debug builds with CodeBuild sandbox](sandbox.md "sandbox.md") documentation.

## Debug builds with Session

Manager

AWS Systems Manager Session Manager enables direct access to running builds in their
actual execution environment. This approach allows you to connect to active build
containers and inspect the build process in real-time. You can examine the file system,
monitor running processes, and troubleshoot issues as they occur.

For detailed instructions, visit the [Debug builds with Session Manager](session-manager.md "session-manager.md") documentation.
