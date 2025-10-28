# Iteration

It’s unlikely that a mechanism will operate as designed from day one. It takes time to
experiment with various tools and find one that works. Adoption can also take significant
effort to push out to a large population. Inspection starts when the tool starts to become
broadly adopted, but at each stage you may find that alterations need to be made to the
mechanism. Here are few examples of how AWS iterates on the ORR mechanism.

First, AWS constantly seeks feedback on the ORR mechanism from its users, the AWS
service teams. This drives the creation of new checklists for different occasions or different
types of workloads (like a serverless application, user console, or server agent) so that each
one is as pertinent as possible for its consumers. It also helps curate the guidance and
questions used in each checklist template. Finally, it also drives enhancements in the user
experience provided by the ORR web service.

Another way AWS iterates on the ORR mechanism is through a specialist engineering
community called “Operational Champions” or “Ops Champion” for short. They provide two
different functions for the ORR program. The first is as part of the ORR process itself. Teams
engage an Ops Champion during their review. The Ops Champion challenges the team on their
answers to the checklist, provides context on the adoption and prioritization of best
practices, and ends up influencing everything from workload architecture to operational
culture in the team. They are part of the complete process, including the review meeting and
in retrospectives after the ORR is complete to review lessons learned.

The second function they provide is as a working group to continue to unify and document
emerging best practices from around our decentralized service teams to avoid pockets of
institutional knowledge. They focus on the ORR questions to ensure they are asking the right
thing, providing the right guidance, verifying results can be measured, determining risk
severity, or developing solutions to make the best practices easier to adopt and implement.
They review the outcomes of COEs and create new lessons learned and new best practices. There
is a tight coupling between the COE process and ORR, we use the lessons learned to continually
generate new content to deal with evolving risks in distributed systems. We also use that
information to ensure we prioritize the right risks for inclusion into the ORR checklists.

## Customer recommendations

Quick iteration has proven to be a valuable approach for building modern distributed
systems and is equally valuable in building mechanisms. Just as with the inspection process,
seek diverse perspectives to create a more holistic understanding of how your mechanism
might need to change. Provide opportunities for honest and, if possible, anonymous feedback
on the tool and process. Find out which questions were the most useful or which problems can
be solved with automation or centralized solutions. Use this feedback to improve the tool
and make it easier to drive greater adoption.

Additionally, developing a community of operationally focused specialists helps improve
the effectiveness of the tool, drives further adoption of the tool, and enhances the ability
to iterate on the mechanism. You will likely build your own Ops Champion community as you
iterate on your ORR program. AWS Solutions Architects (SAs) and Technical Account Managers
(TAMs) can help you develop this community.
