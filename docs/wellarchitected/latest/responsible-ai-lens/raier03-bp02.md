# RAIER03-BP02 Identify release criteria that cannot be met and

narrow your use case

Assess which of your release criteria you cannot meet with your
current system design and implementation strategies, no matter how
you refine them. When you find gaps that can't be closed through
technical solutions alone, consider whether you are trying to solve
too broad of a problem with your current approach. Rather than
compromising on safety or performance standards, narrow your use
case to focus on scenarios where you can meet your release criteria.
Go back to your original risk and benefit assessment with this more
focused scope, identifying new opportunities and constraints that
come with the narrower application. Update your release criteria to
reflect this refined use case, verifying they capture the specific
harms you need to block and benefits you want to deliver within your
new boundaries. This iterative process assists you to build a system
that performs appropriately in its intended domain rather than
struggling to meet unrealistic expectations or risk releasing with
unmet criteria.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. List out which release criteria your system consistently fails
   to meet despite multiple implementation attempts and assess
   whether these failures are fundamental limitations of your
   current approach rather than problems that more
   implementations can solve. Look for patterns like specific
   types of content your system can't handle safely or
   performance gaps that persist across different model
   architectures.
2. Map these persistent failures to specific parts of your use
   case to understand which scenarios are causing the problems.

For example, if your chatbot struggles with medical advice but
works well for general conversation, or if your content
moderation system fails on certain languages but works fine for
English, you can see where to draw new boundaries.

1. Define a narrower use case that avoids the scenarios where you
   cannot meet your release criteria, focusing on areas where
   your system can genuinely excel and deliver value. This might
   mean limiting the types of queries you handle, the domains you
   operate in, or the user populations you serve, but it lets you
   build something that performs appropriately.
2. Redo your risk and benefit analysis using this more focused
   scope, since narrowing your use case may change both the
   potential harms and the benefits you can deliver. You might
   discover new risks in your focused area that you had not
   considered or find that some broad risks no longer apply.
3. Rewrite your release criteria to match your refined use case,
   making sure they capture the specific standards that matter
   for your new boundaries. Your updated criteria may be
   achievable with your current system design while still
   maintaining the quality standards that protect users and
   deliver real value.
