# Application security

Application security (AppSec) describes the overall process of how
you design, build, and test the security properties of the workloads
you develop. You should have appropriately trained people in your
organization, understand the security properties of your build and
release infrastructure, and use automation to identify security
issues.

Adopting application security testing as a regular part of your
software development lifecycle (SDLC) and post release processes
help ensure that you have a structured mechanism to identify, fix,
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
Each area provides a set of principles that you can implement. and
provides an end-to-end view of how you design, develop, build,
deploy, and operate workloads.

In AWS, there are a number of approaches you can use when addressing
your application security program. Some of these approaches rely on
technology while others focus on the people and organizational
aspects of your application security program.

###### Best practices

- [SEC11-BP01 Train for application security](sec_appsec_train_for_application_security.md "sec_appsec_train_for_application_security.md")
- [SEC11-BP02 Automate testing throughout the development and
  release lifecycle](sec_appsec_automate_testing_throughout_lifecycle.md "sec_appsec_automate_testing_throughout_lifecycle.md")
- [SEC11-BP03 Perform regular penetration testing](sec_appsec_perform_regular_penetration_testing.md "sec_appsec_perform_regular_penetration_testing.md")
- [SEC11-BP04 Conduct code reviews](sec_appsec_manual_code_reviews.md "sec_appsec_manual_code_reviews.md")
- [SEC11-BP05 Centralize services for packages and dependencies](sec_appsec_centralize_services_for_packages_and_dependencies.md "sec_appsec_centralize_services_for_packages_and_dependencies.md")
- [SEC11-BP06 Deploy software programmatically](sec_appsec_deploy_software_programmatically.md "sec_appsec_deploy_software_programmatically.md")
- [SEC11-BP07 Regularly assess security properties of the
  pipelines](sec_appsec_regularly_assess_security_properties_of_pipelines.md "sec_appsec_regularly_assess_security_properties_of_pipelines.md")
- [SEC11-BP08 Build a program that embeds security ownership in
  workload teams](sec_appsec_build_program_that_embeds_security_ownership_in_teams.md "sec_appsec_build_program_that_embeds_security_ownership_in_teams.md")
