# Measure results and replicate successes

Measure results and replicate successes in the following ways:

- Measure the initial improvement to provisioned resources per unit of work and the
  quantitative decrease in resources provisioned.
- Compare initial estimates and testing results to your production measurements.
  Identify factors that might have contributed to differences, and update your estimation
  and testing methodologies where appropriate.
- Determine success, and degree of success, and share results with stakeholders.
- If you had to revert changes due to failed tests or unintended negative consequences
  from the change, identify the contributing factors. Iterate where viable, or evaluate new
  approaches to achieve the goals of the change.
- Take what you have learned, establish standards, and apply successful improvements to
  other systems that can similarly benefit. Capture and share your methodology, related
  artifacts, and net benefits, across teams and organizations so that others can adopt your
  standard and replicate your success.
- Monitor provisioned resources per unit of work and track changes and total impact over
  time. Changes to your workload, or how your customers consume your workload, can have an
  impact on the effectiveness of your improvement. Re-evaluate improvement opportunities if
  you notice significant short-term decreases in the effectiveness of your improvement or an
  accumulated reduction in effectiveness over time.
- Quantify the net benefit from your improvement over time (including the benefits
  received by other teams who applied your improvement if available) to show the return on
  investment from your improvement activities.
  Applying this step to the [Example scenario](improvement-process.md#example-scenario "improvement-process.md#example-scenario"), you measure the following results.

Your workload shows an initial improvement of 23% reduction in
storage requirements after deploying and applying the new
compression algorithm to existing image files.

The measured value is largely in agreement with initial estimates
(25%), and the significant difference compared to testing (30%) is
determined to be the result of the image files used in testing not
being representative of image files present in production. You
modify the testing image set to more appropriately reflect the
images in production.

The improvement is considered a complete success. The total
reduction in provisioned storage is 2% less than the estimated
25%, but 23% is still a huge improvement in sustainability impact,
and is accompanied by an equivalent cost savings.

The only unintended consequences of the change are the beneficial
reduction in elapsed time to perform the compression and an
equivalent reduction vCPU consumed. These improvements are
attributed to the highly optimized code.

You establish an internal open-source project where you share your
code, associated artifacts, guidance on how to implement the
change, and the results of your implementation. The internal
open-source project makes it easy for your teams to adopt the code
for all their persistent file storage use cases. Your teams adopt
the improvement as a standard. Secondary benefits of the internal
open-source project are that everyone who adopts the solution
benefits from improvements to the solution, and anyone can
contribute improvements to the project.

You publish your success and share the open-source project across
your organization. Every team that adopts the solution replicates
the benefit with minimum investment and adds to the net benefit
received from your investment. You publish this data as a
continuing success story.

You continue to monitor the impact of the improvement over time
and will make changes to the internal open-source project as
required.
