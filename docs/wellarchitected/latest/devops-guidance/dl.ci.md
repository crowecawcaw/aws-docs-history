# [DL.CI.2] Trigger builds automatically upon source code modifications

**Category:** FOUNDATIONAL

Continuous integration (CI) tools should be configured to
regularly monitor the source code repository for any changes.
Alternatively, set up the source code repository to send an
event upon each commit. This implementation creates an
environment where developers can focus on coding and commit
their changes, leaving the system to handle building, testing,
and deploying the application.

Having this process in place aligns with the continuous integration principle of
_failing fast_. It offers immediate feedback on the impact of changes,
whether they cause a minor regression or a major bug, allowing for prompt correction. If a
build fails, it becomes immediately visible to the team. Fixing a broken build is then
prioritized, fostering a culture of discipline and continuous improvement. This approach
minimizes the risk of integration conflicts and bugs while reducing the likelihood of
unexpected outcomes that can arise from manual processes or irregular updates. It also
streamlines the development process, promotes productivity, and contributes to delivering a
higher-quality outcome.

**Related information:**

- [Amazon CodeCatalyst](https://codecatalyst.aws/explore "https://codecatalyst.aws/explore")
- [Building
  the pipeline](../../../whitepapers/latest/practicing-continuous-integration-continuous-delivery/building-the-pipeline.md "../../../whitepapers/latest/practicing-continuous-integration-continuous-delivery/building-the-pipeline.md")
- [Deploy
  container applications in a multicloud environment using
  Amazon CodeCatalyst](https://aws.amazon.com/blogs/devops/deploy-container-applications-in-a-multicloud-environment-using-amazon-codecatalyst/ "https://aws.amazon.com/blogs/devops/deploy-container-applications-in-a-multicloud-environment-using-amazon-codecatalyst/")
