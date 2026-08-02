# IAM execution roles for resilience testing

To run a resilience test, you provide an IAM _execution role_ that AWS Fault Injection Service (AWS FIS) assumes to inject faults into your resources. You set this role on the test, and Resilience Hub uses it when you start a test run.

When you create a test in the console, Resilience Hub can create this role for you. Use the policies in this topic when you create or customize the role yourself, for example with the AWS CLI.

The permissions a role needs depend on the test template, because each template runs a different set of AWS FIS actions. This topic provides a permissions policy for each of the four test templates. For more information about the templates, see [Available tests](next-gen-resilience-testing-available-tests.md "next-gen-resilience-testing-available-tests.md").

Resilience Hub supports two account models:

- **Single-account** – The test targets resources in the same account that runs the experiment. You create one execution role.
- **Multi-account** – The test targets resources in other accounts. You create an orchestrator role in the account that runs the experiment, and a target role in each account that contains targeted resources.
  We recommend that you follow the standard security practice of granting least privilege. The following policies scope each permission to the resource type that the action targets. Resilience testing can't scope permissions to individual resource IDs, because the next generation of Resilience Hub resolves the targeted resources at run time.

###### Topics

- [Single-account execution role](next-gen-resilience-testing-iam-single-account.md "next-gen-resilience-testing-iam-single-account.md")
- [Multi-account execution roles](next-gen-resilience-testing-iam-multi-account.md "next-gen-resilience-testing-iam-multi-account.md")
