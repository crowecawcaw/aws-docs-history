# Contain

AWS Security Incident Response partners with you to contain events. You can configure the service to take proactive containment actions in your account in response to security findings. You can also perform containment yourself or in partnership with your third party relationships by using SSM documents.

###### Important

AWS Security Incident Response does not enable containment capabilities by default.

Two steps are required to enable proactive containment capabilities:

- Grant the necessary permissions to the service using IAM roles. You can create these roles individually per account or across your entire organization by Working with AWS CloudFormation stacksets, which create the required roles.
- Define your containment preferences per account or across your organization to authorize proactive containment actions. Account-level preferences supersede organization-level preferences. This may be done by creating an AWS Support Case (Technical: Security Incident Response Service/Other). The available containment preferences are:

      + **Approval Required (default):** Do not perform proactive containment of any resource without explicit authorization on a case-by-case basis.
      + **Contain Confirmed:** Perform proactive containment of a resource confirmed to be compromised.
      + **Contain Suspected:** Perform proactive containment of a resource with a high likelihood of having been compromised, based on analysis performed by AWS Security Incident Response Engineering.

  An essential part of containment is decision-making; such as whether to shut down a system, isolate a resource from the network, turn off access, or end sessions. These decisions are made easier when there are predetermined strategies and procedures to contain the event. AWS Security Incident Response provides the containment strategy, informs you of potential impact, and guides you on implementing the solution only after you have considered and agreed to the risks involved.

AWS Security Incident Response executes supported containment actions on your behalf to expedite response and reduce the time a
threat actor has to potentially cause damage in your environment. This capability allows for faster mitigation
of identified threats, minimizing potential impact and enhancing your overall security posture. There are different
containment options depending on the resources under analysis. The supported containment actions are:

- _EC2 Containment:_
  The `AWSSupport-ContainEC2Instance` containment automation performs a reversible network containment
  of an EC2 instance, leaving the instance intact and running, but isolating it from any new network activity
  and preventing it from communicating with resources within and outside your VPC.

###### Important

It is important to note that existing tracked connections won’t be shut down as a result of changing
security groups – only future traffic will be effectively blocked by the new security group and this SSM document.
More information is available in the [source containment](source-containment.md "source-containment.md") section of the service technical guide.

- _IAM Containment:_
  The `AWSSupport-ContainIAMPrincipal` containment automation performs a reversible network containment
  of an IAM user or role, leaving the user or role in IAM, but isolating it
  from communicating with resources within your account.
- _S3 Containment:_
  The `AWSSupport-ContainS3Resource` containment automation performs a reversible containment
  of a S3 bucket, leaving the objects in the bucket, and isolating the Amazon S3 bucket or object by modifying its access policies.

AWS Security Incident Response encourages you to consider
containment strategies for each major event type that fit within
your risk appetite. Document clear criteria to help with
decision-making during an event. Criteria to consider include:

- Potential damage to resources
- Preservation of evidence and regulatory requirements
- Service unavailability (for example, network connectivity, services
  provided to external parties)
- Time and resources needed to implement the strategy
- Effectiveness of the strategy (for example, partial vs. full
  containment)
- Permanence of the solution (for example, reversible vs.
  irreversible)
- Duration of the solution (for example, emergency workaround,
  temporary workaround, permanent solution) Apply security
  controls that can lower risk and allow time to define and
  implement a more effective containment strategy.

AWS Security Incident Response advises a staged approach to
achieve efficient and effective containment, involving
short-term and long-term strategies based on the resource type.

- Containment strategy
  - Can AWS Security Incident Response identify the scope of
    the security event?
    - If yes, identify all the resources (users, systems,
      resources).
    - If no, investigate in parallel with executing the
      next step on identified resources.

  - Can the resource be isolated?
    - If yes, then proceed to isolate the affected
      resources.
    - If no, then work with system owners and managers to
      determine further actions necessary to contain the
      problem.

  - Are all affected resources isolated from non-affected
    resources?
    - If yes, then continue to the next step.
    - If no, then continue to isolate affected resources
      to complete short-term containment and prevent the
      event from escalating further.

- System backup
  - Were backup copies of affected systems created for
    further analysis?
  - Are the forensic copies encrypted and stored in a secure
    location?
    - If yes, then continue to the next step.
    - If no, encrypt the forensic images, then store them
      in a secure location to prevent accidental usage,
      damage, and tampering.
