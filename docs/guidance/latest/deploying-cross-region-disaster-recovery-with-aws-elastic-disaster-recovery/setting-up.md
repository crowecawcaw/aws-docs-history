# Setting up

AWS Elastic Disaster Recovery is only one part of a larger disaster recovery strategy, and being prepared for these unforeseen events requires proper coordination across people, processes, and technology. The recovery plan should be documented and clearly define the stakeholders with roles and responsibilities, along with the steps that should be taken in the event of a real disaster. Below is a checklist of key concepts to consider as part of the planning process.

## Sign up for AWS

If you do not have an AWS account, complete the following steps to create one.

1. Open [https://portal.aws.amazon.com/billing/signup](https://portal.aws.amazon.com/billing/signup "https://portal.aws.amazon.com/billing/signup").
2. Follow the online instructions.

Part of the sign-up procedure involves receiving a phone call and entering a verification code on the phone keypad.

### Who are the stakeholders?

Identify all individuals and stakeholders who should be involved and informed when a disaster occurs. Consider using tools such as a responsibility matrix that provide a method to define who is responsible, accountable, consulted, and informed during a disaster. In many situations, we tend to focus on technical stakeholders who are involved with responding to the actual disaster, but we should also consider other stakeholders, such as vendors, third-party suppliers, public relations, marketing teams, and even key customers. We recommend
keeping a registry of all stakeholders with their defined
responsibilities and contact information. One of the most critical roles when preparing for a disaster is defining the individual(s) who will make the final decision on declaring a disaster and initiating the Business Continuity/Disaster Recovery Plan.

### Establish Communication Channels

Once you have identified and documented all relevant stakeholders, it will be necessary to define the proper communication channels to keep everyone informed. Part of this process should be establishing a chain of command and defining well-understood escalation paths. We generally
recommend the use of dedicated communication channels and hubs, such as an on-site situation room where everyone will gather to respond to the disaster. Video conferencing and instant messaging can also be used to facilitate virtual meeting rooms. It is highly advised that executive
leadership is kept informed throughout the process.

### Maintain Up to Date Documentation

Disaster might be hard to predict, but how we respond to these types of events should be predictable. Once it has been determined that you will be activating your disaster recovery response, it is critical to follow the procedures that have been tried and tested. In all cases, this
should start with up to date documentation detailing all steps to be followed. Although your operations and engineering teams are skilled and knowledgeable, the pressure that comes with a disaster is high.

The documentation should include: information on configuration state (mapped network connections), with functioning devices and their configurations.

Furthermore, documentation should include the entire setup of systems and their usage: operating system (OS) and configuration, applications versions, storage and databases (how and where the data is saved, how backups are restored, how the data is verified for accuracy),architecture diagrams, vendor support contacts, and the responsibility matrix. It should contain everything IT related that your business relies upon. Keep hard copies
of the documentation, as outages may knock your internal systems offline.

### When to Activate the Disaster Recovery Plan

It is critical to quickly detect when your workloads are not meeting business objectives. In this way, you can quickly declare a disaster and recover from an incident. For aggressive recovery objectives, this response time, coupled with appropriate information, is critical in
meeting recovery objectives. If your recovery point objective is one hour, then you need to detect the incident, notify appropriate personnel, engage your escalation processes, evaluate information (if
you have any) on expected time to recovery (without executing the DRplan), declare a disaster, and recover within an hour.

Key Performance indicators (KPIs) are quantifiable measurements that help you understand how well you’re performing. It is critical to define and track KPIs in order to determine when your business processes are
impaired and determine the cause. In this way, you can quickly declare a disaster and recover from an unexpected event. For aggressive recovery objectives, the time to detect an event, declare a disaster, and respond
with your recovery plan will determine if your recovery objectives can be met.

### Define action response procedure and verification process

After declaring a disaster, the recovery environment should be activated as soon as possible. An action response procedure outlines all of the necessary steps for recovering at the disaster recovery site. Ensure
that your action response procedure is documented and provides details on how the necessary services will be started, verified, and controlled. It is recommended that automation be used whenever possible to minimize the impact of human error. Having all services up in the recovery site is not enough to declare success. It is critical to have a verification process that tests that all of the required data is in place, network
traffic has been redirected, and all of the required business applications are functioning properly.

### Perform Regular Disaster Recovery Drills

Many organizations do not perform disaster recovery drills on a regular basis because their failover procedures are too complex and they have concerns that failover tests will lead to a disruption of their production environment (and possibly data loss). Despite these concerns,
it is important to schedule frequent disaster recovery drills to build confidence in the plan, build comfort within the team, and identify gaps. People will play a large part in any disaster recovery plan, and only by rehearsing the steps and procedures can we ensure that they can respond quickly and accurately to a real event. Furthermore, as the state and configuration of our systems change over time, only by conducting such exercises can we identify unexpected impact. In many cases, planned drills can be scoped down to focus on specific parts of
the response plan. When using Elastic Disaster Recovery, these drills can be conducted in an isolated manner, in such a way that production is not impacted.

### Stay up to date

Many companies maintain a risk register that tracks and quantifies potential risks to the business. They often include an analysis of current threats, previous disasters, and lessons learned. The risk register should have stakeholders that extend outside of the technology
and operations teams and include the business, risk, and executive leadership roles. It is important to be aware of how you handled previous disasters, as well as how you performed during more recent drills. All documentation should be up to date reflecting the current environment,
processes, and procedures.

### Recovery Operations

In a cross-Region use case, most customers will want to return to the primary Region once they have confidence that the Region is no longer impaired and is considered stable. The process to return to the primary Region should be scheduled in advance and should be done during a planned maintenance window.
