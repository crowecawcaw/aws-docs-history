# Application security

Application security (AppSec) describes the overall process of how
you design, build, and test the security properties of the workloads
you develop. You should have appropriately trained people in your
organization, understand the security properties of your build and
release infrastructure, and use automation to identify security
issues.

Adopting application security testing as a regular part of your
software development lifecycle (SDLC) and post release processes
help validate that you have a structured mechanism to identify, fix,
and prevent application security issues entering your production
environment.

Your application development methodology should include security
controls as you design, build, deploy, and operate your workloads.
While doing so, align the process for continuous defect reduction
and minimizing technical debt. For example, using threat modeling in
the design phase helps you uncover design flaws early, which makes
them easier and less costly to fix as opposed to waiting and
mitigating them later.

The cost and complexity to resolve defects is typically lower the
earlier you are in the SDLC. The easiest way to resolve issues is to
not have them in the first place, which is why starting with a
threat model helps you focus on the right outcomes from the design
phase. As your AppSec program matures, you can increase the amount
of testing that is performed using automation, improve the fidelity
of feedback to builders, and reduce the time needed for security
reviews. All of these actions improve the quality of the software
you build, and increase the speed of delivering features into
production.

These implementation guidelines focus on four areas: organization
and culture, security _of_ the pipeline, security
_in_ the pipeline, and dependency management.
Each area provides a set of principles that you can implement and
provides an end-to-end view of how you design, develop, build,
deploy, and operate workloads.

In AWS, there are a number of approaches you can use when addressing
your application security program. Some of these approaches rely on
technology while others focus on the people and organizational
aspects of your application security program.

The following question focuses on these considerations for application security.

| SEC 11:  How do you incorporate and validate the security properties of<br>applications throughout the design, development, and deployment lifecycle?                                                                   |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Training people, testing using automation, understanding dependencies, and validating the<br>security properties of tools and applications help to reduce the likelihood of security issues<br>in production workloads. |
