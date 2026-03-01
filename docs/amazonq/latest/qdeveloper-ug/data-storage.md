# Data storage in Amazon Q Developer

Amazon Q stores your questions, its responses, and additional context, such as console
metadata and code, to generate responses to your questions and requests. For information about
how data is encrypted, see [Data encryption in Amazon Q Developer](data-encryption.md "data-encryption.md"). For information about how AWS may use some questions
that you ask Amazon Q and its responses to improve our services, see [Amazon Q Developer service improvement](service-improvement.md "service-improvement.md").

## AWS Regions where content is processed and stored

If you're an IAM Identity Center workforce user, at the Amazon Q Developer Pro tier, your content is stored in the AWS Region where your Amazon Q Developer
profile was created only for the following features:

- Amazon Q chat in the AWS Management Console
- Diagnosing AWS console errors with Amazon Q
- Amazon Q in Eclipse, JetBrains IDEs, Visual Studio Code, and Visual Studio
- Amazon Q on the command line

When you use any other feature at the Amazon Q Developer Pro tier, your content may be stored and
processed in a US Region. If you are using a Q Developer profile in a non-US Region, you
can create a service control policy (SCP) to block access to features that store content
and perform inference in the US. For an example SCP, see [Manage access to Amazon Q Developer with policies](security_iam_manage-access-with-policies.md "security_iam_manage-access-with-policies.md").

For other Amazon Q features and integrations, and when using the Amazon Q Developer Free tier,
your content is stored in a Region in the US. Data processed during diagnosing console
error sessions is stored in the US West (Oregon) Region. All other data is stored in the
US East (N. Virginia) Region. Note the following features that store data differently.

###### Note

When you use Amazon Q artifacts, your visualizations-related content is stored in a US Region.

When you use [Console to Code with Amazon Q](console-to-code.md "console-to-code.md"), content is stored in your console Region and processed in a US Region.

When you use Amazon Q generative SQL in Amazon Redshift, your content is stored and processed in your console Region. For more information, see [Interacting with Amazon Q generative SQL](../../../redshift/latest/mgmt/query-editor-v2-generative-ai.md "../../../redshift/latest/mgmt/query-editor-v2-generative-ai.md") in the _Amazon Redshift Management Guide_.

When you create an investigation with Amazon CloudWatch investigations, your content may be stored and processed in other Regions. For more information, see the [Security in CloudWatch investigations](../../../AmazonCloudWatch/latest/monitoring/Investigations-Security.md#cross-region-inference "../../../AmazonCloudWatch/latest/monitoring/Investigations-Security.md#cross-region-inference") topic in the _Amazon CloudWatch User Guide_.

With cross-region inferencing, your requests to Amazon Q Developer may be processed in a
different Region within the geography where your content is stored. For more information,
see [Cross-region inference](cross-region-processing.md#cross-region-inference "cross-region-processing.md#cross-region-inference").
