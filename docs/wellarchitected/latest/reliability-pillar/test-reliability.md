# Test reliability

After you have designed your workload to be resilient to the
stresses of production, testing is the only way to ensure that it
will operate as designed, and deliver the resiliency you expect.

Test to validate that your workload meets functional and non-functional requirements,
because bugs or performance bottlenecks can impact the reliability of your workload. Test the
resiliency of your workload to help you find latent bugs that only surface in production.
Exercise these tests regularly.

###### Best practices

- [REL12-BP01 Use playbooks to investigate failures](rel_testing_resiliency_playbook_resiliency.md "rel_testing_resiliency_playbook_resiliency.md")
- [REL12-BP02 Perform post-incident analysis](rel_testing_resiliency_rca_resiliency.md "rel_testing_resiliency_rca_resiliency.md")
- [REL12-BP03 Test scalability and performance requirements](rel_testing_resiliency_test_non_functional.md "rel_testing_resiliency_test_non_functional.md")
- [REL12-BP04 Test resiliency using chaos engineering](rel_testing_resiliency_failure_injection_resiliency.md "rel_testing_resiliency_failure_injection_resiliency.md")
- [REL12-BP05 Conduct game days regularly](rel_testing_resiliency_game_days_resiliency.md "rel_testing_resiliency_game_days_resiliency.md")
