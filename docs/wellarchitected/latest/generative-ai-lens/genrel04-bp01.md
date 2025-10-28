# GENREL04-BP01 Implement a prompt catalog

Prompt catalogs store and manage prompts and prompt versions. They
act as a reliable store for prompts for generative AI workloads.

**Desired outcome:** When
implemented, this best practice improves the reliability of your
generative AI workload by creating a central store for prompts that
can be used for generative AI workloads.

**Benefits of establishing this best
practice:**
[Manage
change through automation](../framework/rel-dp.md "../framework/rel-dp.md") - Implementing a prompt catalog
helps to automate the process of deploying and rolling back prompt
versions.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Prompt catalogs function as a centralized system for developing,
testing, and managing prompts. Customers should implement a prompt
catalog to maintain different version of prompts. Prompts should
be released to a live version once passing the appropriate testing
thresholds and benchmarks. In the case where a prompt results in
unexpected or undesirable behavior, a prompt catalog enables the
ability to roll back to the previous version.

Amazon Bedrock Prompt Management helps customers maintain prompts
and prompt versions. Additionally, Prompt Management through
Amazon Bedrock maintains versioned information on hyperparameter
rangers for a prompt. Prompt behavior can change drastically when
tuning hyperparameters such as temperature,
top_p, or top_k. Value
ranges for these hyperparameters should be paired with and
validated against prompt versions as part of the prompt
engineering process.

Prompt catalogs should maintain test results for a prompt against
several model versions. A given foundation model can have several
versions, and prompt test results for each model version can vary
accordingly. Consider using Bedrock Prompt Management or a similar
capability to maintain prompt versions for each of the available
models.

### Implementation steps

1. Create a prompt, and identify variables and hyperparameter
   ranges to test.
2. Test the prompt against several models and model versions.
3. Publish the best performing prompt for the given model for
   use in your application stack.
   - Integrate prompt versions into your application CI/CD
     process to maintain continual performance evaluation and
     tracking.

## Resources

**Related practices:**

- [REL07-BP01](../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md "../reliability-pillar/rel_adapt_to_changes_autoscale_adapt.md")
- [REL08-BP02](../reliability-pillar/rel_tracking_change_management_functional_testing.md "../reliability-pillar/rel_tracking_change_management_functional_testing.md")
- [REL08-BP04](../reliability-pillar/rel_tracking_change_management_immutable_infrastructure.md "../reliability-pillar/rel_tracking_change_management_immutable_infrastructure.md")

**Related guides, videos, and documentation:**

- [AWS re:Invent 2023

* Prompt Engineering Best Practices for LLMs on Amazon Bedrock
  (AIM377)](https://www.youtube.com/watch?v=jlqgGkh1wzY "https://www.youtube.com/watch?v=jlqgGkh1wzY")

**Related examples:**

- [Amazon Bedrock Prompt Management is now Available in GA](https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/ "https://aws.amazon.com/blogs/machine-learning/amazon-bedrock-prompt-management-is-now-available-in-ga/")
