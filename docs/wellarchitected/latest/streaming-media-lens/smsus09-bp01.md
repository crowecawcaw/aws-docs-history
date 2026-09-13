

# SMSUS09-BP01 Adopt sustainable development and deployment practices
<a name="smsus09-bp01"></a>

Run the development and deployment process so that it consumes resources only when work is actually happening. Build fleets, test environments, and non-production stacks are often left running indefinitely, so the engineering process behind a streaming service can carry a large, invisible resource footprint that has nothing to do with serving viewers.

**Desired outcome:**
+ Non-production environments exist when they are in use and are torn down or stopped when they are not.
+ Build and test resources are right-sized and reused rather than over-provisioned and rebuilt from scratch each time.
+ Deployment strategies minimize the window during which duplicate resources run.

**Common anti-patterns:**
+ Leaving development, test, and staging environments running continuously, including overnight and at weekends when no one is using them.
+ Provisioning oversized build environments and rebuilding dependencies from scratch on every run instead of caching them.
+ Running blue/green or parallel deployments with a long overlap window, so two full environments run far longer than the cutover requires.
+ Maintaining standing physical or virtual device labs for client testing rather than using on-demand managed device testing.

**Benefits of establishing this best practice:**
+ Lower resource consumption from non-production, because environments run only when in use.
+ Reduced build energy, because right-sized, cached build environments do less repeated work.
+ A shorter window of duplicated resources during deployments, because overlap is minimized.
+ Sustainability treated as a first-class pipeline concern, because efficiency is measured and enforced in CI/CD rather than left to chance.

**Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>

The development and deployment process has its own resource cost, and that cost is dominated by idle time rather than active work. Non-production environments are the clearest example. A staging stack that mirrors production but is used during working hours sits idle most of the week, consuming resources for no delivered value. Infrastructure as code is the enabler for fixing this, because environments that are defined in code can be created on demand and destroyed when idle without the manual effort that makes teams leave them running. The goal is ephemeral non-production that exists for the duration of the work and no longer.

Build environments that are oversized or that rebuild dependencies from scratch on every run do more work than necessary, so right-sizing build compute and caching dependencies reduces both build time and the energy each build consumes. Client testing has a similar pattern. Maintaining standing device labs holds hardware that is used intermittently, whereas on-demand managed device testing consumes resources only during test runs.

Blue/green and parallel deployments improve safety by running a second environment during cutover, but that second environment doubles resources for as long as the overlap lasts, so minimize the overlap window rather than abandon the safety it provides. Energy use isn't measurable per build or deployment, so use resource proxies such as non-production running hours, build compute hours, and deployment overlap duration. Read account-level carbon impact per Region from the AWS Customer Carbon Footprint Tool, which publishes monthly. Where possible, surface these proxies inside the pipeline so efficiency is visible at the point changes are made.

### Implementation steps
<a name="implementation-steps"></a>

1. **Define environments as code for on-demand lifecycle:** Use infrastructure as code so non-production environments can be created when needed and destroyed when idle, removing the manual effort that leads teams to leave them running.

1. **Stop non-production outside working hours:** Schedule automatic shutdown of the following environments overnight and at weekends, starting them on demand when work resumes.
+ Development
+ Test
+ Staging

1. **Right-size and cache build environments:** Configure AWS CodeBuild with appropriately sized compute and dependency caching so builds don't rebuild from scratch or run on oversized resources.

1. **Minimize deployment overlap:** Keep blue/green and parallel deployment overlap windows as short as the cutover safely allows, so duplicate environments run only as long as needed.

1. **Use on-demand device testing:** Run client and device testing on AWS Device Farm rather than maintaining standing device labs, so test hardware is consumed only during runs.

1. **Surface sustainability metrics in CI/CD:** Track the following in the pipeline, and review against the monthly account-level figures from the AWS Customer Carbon Footprint Tool.
+ Non-production running hours
+ Build compute hours
+ Deployment overlap duration

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSUS02-BP01 Implement adaptive infrastructure scaling based on viewer patterns](smsus02-bp01.html)
+ [SMSUS10-BP01 Establish sustainability KPIs and continuous optimization processes](smsus10-bp01.html)

**Related documents**
+ [Sustainability Pillar, Process and culture](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/process-and-culture.html)
+ [Optimizing Streaming Media Workflows to Reduce Your Carbon Footprint, Part I](https://aws.amazon.com/blogs/media/optimizing-streaming-media-workflows-to-reduce-your-carbon-footprint-part-i/)

**Related services**
+ [AWS CodeBuild](https://aws.amazon.com/codebuild/)
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+ [AWS Device Farm](https://aws.amazon.com/device-farm/)