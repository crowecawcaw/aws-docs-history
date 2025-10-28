# Operating your workloads securely

Operating workloads securely covers the whole lifecycle of a workload from design, to
build, to run, and to ongoing improvement. One of the ways to improve your ability to operate
securely in the cloud is by taking an organizational approach to governance. Governance is the
way that decisions are guided consistently without depending solely on the good judgment of
the people involved. Your governance model and process are the way you answer the question
“How do I know that the control objectives for a given workload are met and are appropriate
for that workload?” Having a consistent approach to making decisions speeds up the deployment
of workloads and helps raise the bar for the security capability in your organization.

To operate your workload securely, you must apply overarching best practices to every area
of security. Take requirements and processes that you have defined in operational excellence
at an organizational and workload level, and apply them to all areas. Staying up to date with
AWS and industry recommendations and threat intelligence helps you evolve your threat model
and control objectives. Automating security processes, testing, and validation help you scale
your security operations.

Automation allows consistency and repeatability of processes. People are good at many
things, but consistently doing the same thing repeatedly without mistakes is not one of them.
Even with well-written runbooks, you run the risk that people won’t consistently carry out
repetitive tasks. This is especially true when people have diverse responsibilities and then
have to respond to unfamiliar alerts. Automation, however, responds the same way
each time. The best way to deploy applications is through automation. The code that runs the
deployment can be tested and then used to perform the deployment. This increases confidence in
the change process and reduces the risk of a failed change.

To verify that the configuration meets your control objectives, test the automation and
the deployed application in a non-production environment first. This way, you can test the
automation to prove that it performed all the steps correctly. You also get early feedback in
the development and deployment cycle, reducing rework. To reduce the chance of deployment
errors, make configuration changes by code not by people. If you need to re-deploy an
application, automation makes this much easier. As you define additional control objectives,
you can easily add them to the automation for all workloads.

Instead of having individual workload owners invest in security specific to their
workloads, save time by using common capabilities and shared components. Some examples of
services that multiple teams can consume include the AWS account creation process, centralized
identity for people, common logging configuration, and AMI and container base image creation.
This approach can help builders improve workload cycle times and consistently meet security
control objectives. When teams are more consistent, you can validate control objectives and
better report your control posture and risk position to stakeholders.

###### Best practices

- [SEC01-BP03 Identify and validate control objectives](sec_securely_operate_control_objectives.md "sec_securely_operate_control_objectives.md")
- [SEC01-BP04 Stay up to date with security threats and recommendations](sec_securely_operate_updated_threats.md "sec_securely_operate_updated_threats.md")
- [SEC01-BP05 Reduce security management scope](sec_securely_operate_reduce_management_scope.md "sec_securely_operate_reduce_management_scope.md")
- [SEC01-BP06 Automate deployment of standard security controls](sec_securely_operate_automate_security_controls.md "sec_securely_operate_automate_security_controls.md")
- [SEC01-BP07 Identify threats and prioritize mitigations using a threat
  model](sec_securely_operate_threat_model.md "sec_securely_operate_threat_model.md")
- [SEC01-BP08 Evaluate and implement new security services and
  features regularly](sec_securely_operate_implement_services_features.md "sec_securely_operate_implement_services_features.md")
