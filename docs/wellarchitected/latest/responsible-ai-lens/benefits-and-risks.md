# Benefits and risks

The benefits and risks focus area assists you to characterize the potential benefits
and inherent risks of the use case, using only minimal assumptions
about the AI solution given in the Use Case focus area. In general,
the depth of analysis devoted to potential benefits and inherent
risks should align with the breadth and complexity of the use case,
and the potential scale of deployment. Iteration is expected.
Additionally, since use cases are often defined by working backwards
from desired benefits, risks may require more effort to explore than
benefits.

Technically, benefits and risks can be assessed similarly. Both are
based on the likelihood and impact of system interactions, where a
system interaction typically involves a sequence of input and output
pairs, which can be considered as _events_ in the
interaction. A helpful interaction has a positive impact on a
stakeholder, while a harmful interaction has a negative impact on a
stakeholder.

The result of an interaction can be the compounding effect of
multiple events. To estimate benefits, you identify examples of
helpful interactions, categorize the examples into benefits, and
then use your knowledge of your business to estimate the value of
each benefit. Assessing risk is trickier, because there is usually
less information available about harmful interactions. As a result,
you first identify categories of potential harmful interactions,
qualitatively estimate the likelihood and impact severity of each
harmful interaction category, and map the qualitative estimates to a
risk level. In most cases, benefits and risks should be assessed for
each stakeholder group.

Note that the risk posed by the AI system implementation when
applied to the use case is referred to as residual risk. This is
computed in [Monitoring](monitoring.md "monitoring.md"), as part of the process of
deciding whether the AI system is ready for release.

###### Focus areas

- [Characterize benefits](raibr01.md "raibr01.md")
- [Harmful events](raibr02.md "raibr02.md")
- [Assess risks](raibr03.md "raibr03.md")
- [Mitigate risks](raibr04.md "raibr04.md")
