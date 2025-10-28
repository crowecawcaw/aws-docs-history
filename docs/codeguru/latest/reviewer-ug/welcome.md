Starting November 7, 2025, you will not be able to create new repository associations in Amazon CodeGuru Reviewer. If you would like to use the service, create repository associations prior to November 7, 2025. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](codeguru-reviewer-availability-change.md "codeguru-reviewer-availability-change.md").

# What is Amazon CodeGuru Reviewer?

Amazon CodeGuru Reviewer is a service that uses program analysis and machine learning to detect potential
defects that are difficult for developers to find and offers suggestions for improving your Java
and Python code. This service has been released for general availability in several [Regions](../../../general/latest/gr/codeguru-reviewer.md "../../../general/latest/gr/codeguru-reviewer.md").

By proactively detecting code defects, CodeGuru Reviewer can provide guidelines for addressing them and
implementing best practices to improve the overall quality and maintainability of your code base
during the code review stage. For more information, see [How Amazon CodeGuru Reviewer works](how-codeguru-reviewer-works.md "how-codeguru-reviewer-works.md").

## What kind of recommendations does CodeGuru Reviewer

provide?

CodeGuru Reviewer doesn't flag syntactical mistakes, as these are relatively easy to find. Instead,
CodeGuru Reviewer identifies more complex problems and suggests improvements related to recommendation
types such as resource leak prevention or security analysis. Within each type are several
detectors that CodeGuru Reviewer uses to analyze your code. For information about these detectors, see
the [Amazon CodeGuru Reviewer Detector
Library](../../detector-library/index.md "../../detector-library/index.md").

CodeGuru Reviewer also integrates with AWS Secrets Manager to use a secrets detector that finds unprotected
secrets in your code. For more information, see [Secrets detection](recommendations.md#secrets-detection "recommendations.md#secrets-detection").

## What languages and repositories can I use with

CodeGuru Reviewer?

CodeGuru Reviewer is designed to work with Java and Python code repositories in the following source
providers:

- [AWS CodeCommit](../../../codecommit/latest/userguide/welcome.md "../../../codecommit/latest/userguide/welcome.md")
- Bitbucket
- GitHub
- GitHub Enterprise Cloud
- GitHub Enterprise Server
- Amazon S3

###### Note

S3 repositories are only supported through GitHub Actions. For more information, see
[Create code reviews with GitHub Actions](working-with-cicd.md "working-with-cicd.md").

If you use any of these source providers, you can integrate with CodeGuru Reviewer with just a few
steps. After you associate a repository with CodeGuru Reviewer, you can [interact with
recommendations in the CodeGuru Reviewer console](give-feedback-from-code-review-details.md "give-feedback-from-code-review-details.md"). For incremental code reviews, you can also
[see recommendations directly from inside pull requests](provide-feedback.md#provide-feedback-in-pull-requests "provide-feedback.md#provide-feedback-in-pull-requests") in your repository.

## Accessing CodeGuru Reviewer

You can access CodeGuru Reviewer using any of the following methods:

- **Amazon CodeGuru Reviewer console** – [https://console.aws.amazon.com/codeguru/reviewer/](https://console.aws.amazon.com/codeguru/reviewer/ "https://console.aws.amazon.com/codeguru/reviewer/")
- **AWS CLI** – For more information, see [Getting started with the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-started.md "../../../cli/latest/userguide/cli-chap-getting-started.md")
  in the _AWS Command Line Interface User Guide_.
- **CodeGuru Reviewer API** – For more information, see the [Amazon CodeGuru Reviewer API Reference](../reviewer-api/Welcome.md "../reviewer-api/Welcome.md").
- **AWS SDKs** – For more information, see [Tools to Build on AWS](https://aws.amazon.com/developer/tools "https://aws.amazon.com/developer/tools").
