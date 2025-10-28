# The review process

The review of architectures must be done in a consistent manner, with a blame-free
approach that encourages diving deep. It should be a lightweight process (hours not days) that
is a conversation and not an audit. The purpose of reviewing an architecture is to identify any
critical issues that might need addressing or areas that could be improved. The outcome of the
review is a set of actions that should improve the experience of a customer using the workload.

As discussed in the “On Architecture” section, you will want each
team member to take responsibility for the quality of its
architecture. We recommend that the team members who build an
architecture use the Well-Architected Framework to continually
review their architecture, rather than holding a formal review
meeting. A nearly continuous approach permits your team members to
update answers as the architecture evolves, and improve the
architecture as you deliver features.

The AWS Well-Architected Framework is aligned to the way that AWS
reviews systems and services internally. It is premised on a set
of design principles that influences architectural approach, and
questions that verify that people don’t neglect areas that often
featured in Root Cause Analysis (RCA). Whenever there is a
significant issue with an internal system, AWS service, or
customer, we look at the RCA to see if we could improve the review
processes we use.

Reviews should be applied at key milestones in the product
lifecycle, early on in the design phase to avoid _one-way
doors_ that are difficult
to change, and then before the go-live date.
(Many decisions are reversible, two-way doors. Those decisions can
use a lightweight process. One-way doors are hard or impossible
to reverse and require more inspection before making them.)
After you go into
production, your workload will continue to evolve as you add new
features and change technology implementations. The architecture
of a workload changes over time. You must follow good
hygiene practices to stop its architectural characteristics from
degrading as you evolve it. As you make significant architecture changes, you should follow a set of hygiene processes including a
Well-Architected review.

If you want to use the review as a one-time snapshot or
independent measurement, you will want to verify that you have all
the right people in the conversation. Often, we find that reviews
are the first time that a team truly understands what they have
implemented. An approach that works well when reviewing another
team's workload is to have a series of informal conversations
about their architecture where you can glean the answers to most
questions. You can then follow up with one or two meetings where
you can gain clarity or dive deep on areas of ambiguity or
perceived risk.

Here are some suggested items to facilitate your meetings:

- A meeting room with whiteboards
- Print outs of any diagrams or design notes
- Action list of questions that require out-of-band research to
  answer (for example, “did we activate encryption or not?”)

After you have done a review, you should have a list of issues
that you can prioritize based on your business context. You will
also want to take into account the impact of those issues on the
day-to-day work of your team. If you address these issues early,
you could free up time to work on creating business value rather
than solving recurring problems. As you address issues, you can
update your review to see how the architecture is improving.

While the value of a review is clear after you have done one, you
may find that a new team might be resistant at first. Here are some
objections that can be handled through educating the team on the
benefits of a review:

- “We are too busy!” (Often said when the team is getting ready
  for a significant launch.)
  - If you are getting ready for a big launch, you will want it
    to go smoothly. The review will permit you to understand
    any problems you might have missed.
  - We recommend that you carry out reviews early in the product
    lifecycle to uncover risks and develop a mitigation plan
    aligned with the feature delivery roadmap.

- “We don’t have time to do anything with the results!” (Often
  said when there is an immovable event, such as the Super Bowl,
  that they are targeting.)
  - These events can’t be moved. Do you really want to go into
    it without knowing the risks in your architecture? Even if
    you don’t address all of these issues you can still have
    playbooks for handling them if they materialize.

- “We don’t want others to know the secrets of our solution
  implementation!”
  - If you point the team at the questions in the
    Well-Architected Framework, they will see that none of the
    questions reveal any commercial or technical proprietary
    information.

As you carry out multiple reviews with teams in your organization,
you might identify thematic issues. For example, you might see
that a group of teams has clusters of issues in a particular
pillar or topic. You will want to look at all your reviews in a
holistic manner, and identify any mechanisms, training, or
principal engineering talks that could help address those thematic
issues.
