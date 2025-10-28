# FSIREL01: Have you planned for events that impact your software development

infrastructure and challenge your recovery and resolution plans?

Financial services institutions are increasingly relying on continuous integration
(CI) and deployment (CD) pipelines to accelerate development and deployment. Often the
only way to change production systems is through the pipeline to ensure that quality
controls, security guard rails, and standards are maintained as part of the change
management process.

## FSIREL01-BP01 Treat your CI/CD tools as critical workload

components for recovery

If key elements of an SDLC environment, such as the CI/CD pipeline, are impacted,
you might not be able to commit new code, change configurations, pull containers, or
upload application artifacts, which can result in an outage of your workload.
Understand the entire dependencies of your SDLC and plan for disruption of the
critical components that the SDLC relies on. Consider replicating your SDLC
environment and supporting services in another Region, which allows you to continually
replicate source code, application, and container repositories.
