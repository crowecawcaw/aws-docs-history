# Running a WAFR

After all the required preparation, it is time for you to run a
Well-Architected Framework Review (WAFR). In this section, we'll explore tips and tricks to become more
efficient while conducting your WAFR.

## Before the WAFR

Before you begin discussing the workload as a group, go over the
following section and discuss the rules of engagement for the
session. You should have a consensus in your group for how to
proceed.

### Define roles and responsibilities

- Who is leading the WAFR?
- Who will be sharing their screen, and what they will be
  sharing on it?
- Who will be taking notes in the WA Tool or another format?
- Which pillars will you be reviewing and in which order?
- Do you have the right people in the room to answer the
  questions?
- How will you capture out of scope items, and how will you
  create your backlog for these items?
- How much time do you want to allocate for each section or
  pillar?
- What do you want to achieve in the time you have allocated?

## Review tips

Plan the meetings around capturing data points about the workload
architectural choices. There's a number of things you can do to
make this section of the WAFR as smooth as possible.

1. **Communicate positive
   intent:** Revisit the positive intent of the WAFR
   with the participants. Critical conversations about work can
   be difficult, so reaffirm that the WAFR is being conducted to
   find improvement opportunities. Reinforce a _no blame
   culture_. There is no attack or defense, but rather
   a collaborative discussion about architectural improvement.
2. **Bring a supporter:**
   Navigating a complex workload architecture, asking questions,
   moderating responses, and taking notes can be challenging for
   one person. A successful WAFR is a team activity. Designate
   alternate roles, which allows one person to run the review
   while another takes notes, checks the documentation, and
   monitors the discussion.
3. **Stay on topic:** It's common
   when having group conversations around architectural decisions
   for people to get sidetracked. If you want to be efficient
   with time, make sure that WAFR participants respectfully hold
   each other to stay on topic. Capture side concepts and ideas
   in a centralized place that can be picked up during future
   discussion sessions.
4. **Take good notes:** Simply
   ticking boxes in the WA Tool does not provide context to
   someone revisiting the WAFR in later milestones. Use the notes
   box in the WA Tool, or create an external document linked from
   the WAFR notes box if you exceed the character limit. Context
   helps other parties, especially people who are new to the
   workload, understand ongoing work and determine what to
   prioritize.
5. **Don't focus on solutions:**
   Focus on capturing data points about the workload rather than
   solutions. Too much focus on solutions can waste time during
   your WAFR session and prevent you from capturing important
   data points. It's not the best use of other participants' time
   if you brainstorm something that is out of scope.
6. **Focus on the workload, not the
   tool:** It's common for people to share their screen
   showing the Well-Architected Tool (WA Tool) in the AWS Management Console. Although capturing data in the WA Tool is crucial,
   don't focus exclusively on the tool. Focus your discussion on
   the architecture instead. Keep the review conversational, and
   paraphrase the questions to align with the context.
7. **Divide the discussion into
   parts:** It can be difficult to review all six
   pillars in one meeting. Spread the review out into smaller
   sessions, which allows for a more topic-targeted approach and
   can be easier to schedule with your participants.
8. **Remember to take breaks:**
   Reviewing architecture thoroughly can be tiring for
   participants, and their concentration can lapse over time.
   Schedule frequent breaks during the WAFR. Be frugal with
   participants' time, and allow for people to drop when they are
   no longer required.
9. **Think carefully about
   maybes:** If you find the answer for a question is
   "maybe," "kind of," or "we
   have something in the backlog to address that,"
   carefully consider if this actually means "no." A
   WAFR is about capturing the honest and
   _current_ state of the workload, not the
   intended state.
10. **Consider trade-offs:**
    Well-Architected is about making trade-offs between pillars.
    To make a workload more resilient might come at the detriment
    of your cost optimization, or further optimizing cost might
    have an impact on your workload's environmental impact. The
    pillars are there to provide a structure for your
    conversations and to help you make informed architectural
    choices.
11. **Recognize that no workload can be
    perfect:** Workloads are rarely perfect and often do
    not need to be. Avoid turning your WAFR into an exercise of
    making everything perfect, and focus on making the workload
    function safely and efficiently for its intended business
    purpose.

## Running the WAFR

Run the WAFR in the AWS account alongside the workload. You can
then share the workload review with other AWS accounts.

[Share
the review](workloads-sharing.md "workloads-sharing.md") with a central account using AWS Organizations.
You can then use the
[dashboard](dashboard.md "dashboard.md")
to view your organization's workloads centrally.

This can help you recognize patterns of risks and improvements
across all your workloads. You can then address the challenge
centrally with a pattern-based approach that can be shared and
used across many accounts and workloads.

## IAM access

Accessing the AWS WA Tool in the AWS Management Console requires IAM permissions.
Determine who needs access in advance to save time at the
beginning of the WAFR session.

For more detail, see
[Providing
users, groups, or roles access to AWS Well-Architected Tool](iam-auth-access.md "iam-auth-access.md").

You can set up a
[cross-account
IAM Role](../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md "../../../IAM/latest/UserGuide/tutorial_cross-account-with-roles.md") to allow external stakeholders to access the WA
Tool and edit or view reviews.

## Resources

- [How
  to perform a Well-Architected Framework Review Part 2](https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part2/ "https://aws.amazon.com/blogs/mt/how-to-perform-a-well-architected-framework-review-part2/")
