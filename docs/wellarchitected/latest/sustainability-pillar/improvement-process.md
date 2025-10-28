# Improvement process

The architectural improvement process includes understanding what
you have and what you can do to improve, selecting targets for
improvement, testing improvements, adopting successful improvements,
quantifying your success and sharing what you have learned so that
it can be replicated elsewhere, and then repeating the cycle.

The goals of your improvements can be:

- To eliminate waste, low utilization, and idle or unused
  resources
- To maximize the value from resources you consume

###### Note

Use all the resources you provision, and complete the same work with the minimum resources
possible.

In early stages of optimization, first eliminate areas with
waste or low utilization, and then move toward more targeted
optimizations that fit your specific workload.

Monitor changes to the consumption of resources over time.
Identify where accumulated changes result in inefficient or
significant increases in resource consumption. Determine the
need for improvements to address the changes in consumption and
implement the improvements you prioritize.

The following steps are designed to be an iterative process that
evaluates, prioritizes, tests, and deploys sustainability-focused
improvements for cloud workloads.

1. **Identify targets for improvement:** Review your workloads
   against best practices for sustainability that are identified in this document, and identify
   targets for improvement.
2. **Evaluate specific improvements:** Evaluate specific changes
   for potential improvement, projected cost, and business risk.
3. **Prioritize and plan improvements:** Prioritize changes that
   offer the largest improvements at the least cost and risk, and establish a plan for testing
   and implementation.
4. **Test and validate improvements:** Implement changes in
   testing environments to validate their potential for improvement.
5. **Deploy changes to production:** Implement changes across
   production environments.
6. **Measure results and replicate successes:** Look for
   opportunities to replicate successes across workloads, and revert changes with unacceptable
   outcomes.

## Example scenario

The following example scenario is referenced later in this document to illustrate each
step of the improvement process.

Your company has a workload that performs complex image manipulations on Amazon EC2 instances
and stores the modified and original files for user access. The processing activities are CPU
intensive, and the output files are extremely large.
