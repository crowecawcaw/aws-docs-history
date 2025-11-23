# RAIRC03-BP07 Measure user controllability of system

behavior

To verify that users can effectively control your AI system when
they need to override, adjust, or roll back its behavior, develop
quantitative measures that assess how well user controls correlate
with intended system outcomes. Test the range and granularity of
control effectiveness by measuring whether adjustments produce the
expected changes in system behavior. Create metrics that capture
both the responsiveness of controls and their precision. Your
metrics should measure when controls fail to work as intended or
when they produce unexpected side effects.

**Level of risk exposed if this best practice
is not established:** High

## Implementation considerations

1. Plan how you'll test user controls before building your system
   by deciding which control mechanisms matter most for user
   safety based on your RAIBR02 risk assessment findings. Create
   simple test scenarios that check if each control works as
   intended and build basic measurement tools that show whether
   user inputs can change system behavior. This upfront planning
   saves time later and assists you to build controls that work
   when users need them.
2. Design tests that check how well users can fine-tune your
   system's behavior, from small adjustments to major changes.
   Test both precise control scenarios where users make small
   tweaks and broad control scenarios where users need to make
   big behavioral shifts. Include tests that push controls to
   their breaking points to determine where the system stops
   responding to user input, which assists you to fix weak spots.
3. Build ways to measure how fast your system reacts when users
   try to override, adjust, or roll back its behavior. Track how
   long controls take to activate and how quickly the system
   settles into new behavior patterns after users make changes.
   Fast, reliable control response keeps users in charge of the
   system.
4. Create tests that catch when controls fail or cause unexpected
   problems elsewhere in your system. Test what happens when
   users try controls that should fail gracefully and verify that
   your system gives clear feedback when controls can't work.
   Look for cases where adjusting one thing accidentally breaks
   something else, as surprise effects can undermine user trust.

## Resources

**Related documents:**

- [FollowBench](https://aclanthology.org/2024.acl-long.257.pdf "https://aclanthology.org/2024.acl-long.257.pdf")
- [IFEval](https://arxiv.org/pdf/2311.07911 "https://arxiv.org/pdf/2311.07911")
- [Prompt
  Steerability](https://aclanthology.org/2025.naacl-long.400.pdf "https://aclanthology.org/2025.naacl-long.400.pdf")
- [Human
  Agency Scale](https://www.emergentmind.com/topics/human-agency-scale-has "https://www.emergentmind.com/topics/human-agency-scale-has")
- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.6.2.4 AI system verification and
  validation
