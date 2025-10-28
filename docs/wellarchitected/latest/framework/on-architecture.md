# On architecture

In on-premises environments, customers often have a central team
for technology architecture that acts as an overlay to other
product or feature teams to verify they are following best
practice. Technology architecture teams typically include a set of
roles such as: Technical Architect (infrastructure), Solutions
Architect (software), Data Architect, Networking Architect, and
Security Architect. Often these teams use
[TOGAF](https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework "https://en.wikipedia.org/wiki/The_Open_Group_Architecture_Framework")
or the
[Zachman
Framework](https://zachman-feac.com/zachman/about-the-zachman-framework "https://zachman-feac.com/zachman/about-the-zachman-framework") as part of an enterprise architecture capability.

At AWS, we prefer to distribute capabilities into teams rather than having a centralized
team with that capability. There are risks when you choose to distribute decision making
authority, for example, verifying that teams are meeting internal standards. We mitigate these
risks in two ways. First, we have _practices_ (ways of doing things,
process, standards, and accepted norms) that focus on allowing each team to have that
capability, and we put in place experts who verify that teams raise the bar on the standards
they need to meet. Second, we implement _mechanisms_ that carry out
automated checks to verify standards are being met.

######

“Good intentions never work, you need good mechanisms to make anything happen” — Jeff
Bezos.

This means replacing a human's best efforts with mechanisms (often automated) that check for
compliance with rules or process. This distributed approach is supported by the [Amazon leadership
principles](https://www.amazon.jobs/en/principles?ref=wellarchitected-wp "https://www.amazon.jobs/en/principles?ref=wellarchitected-wp"), and establishes a culture across all roles that _works
back_ from the customer. Working backward is a fundamental part of our innovation
process. We start with the customer and what they want, and let that define and guide our
efforts. Customer-obsessed teams build products in response to a customer need.

For architecture, this means that we expect every team to have the capability to create
architectures and to follow best practices. To help new teams gain these capabilities or
existing teams to raise their bar, we activate access to a virtual community of principal
engineers who can review their designs and help them understand what AWS best practices are.
The principal engineering community works to make best practices visible and accessible. One
way they do this, for example, is through lunchtime talks that focus on applying best
practices to real examples. These talks are recorded and can be used as part of onboarding
materials for new team members.

AWS best practices emerge from our experience running thousands of systems at internet
scale. We prefer to use data to define best practice, but we also use subject matter experts,
like principal engineers, to set them. As principal engineers see new best practices emerge,
they work as a community to verify that teams follow them. In time, these best practices are
formalized into our internal review processes, and also into mechanisms that enforce
compliance. The Well-Architected Framework is the customer-facing implementation of our internal
review process, where we have codified our principal engineering thinking across field roles,
like Solutions Architecture and internal engineering teams. The Well-Architected Framework is a
scalable mechanism that lets you take advantage of these learnings.

By following the approach of a principal engineering community with distributed ownership
of architecture, we believe that a Well-Architected enterprise architecture can emerge that is
driven by customer need. Technology leaders (such as a CTOs or development managers), carrying
out Well-Architected reviews across all your workloads will permit you to better understand the
risks in your technology portfolio. Using this approach, you can identify themes across teams
that your organization could address by mechanisms, training, or lunchtime talks where your
principal engineers can share their thinking on specific areas with multiple teams.
