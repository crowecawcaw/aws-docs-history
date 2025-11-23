# RAIER01-BP02 Independently corroborate more critical and

subjective evaluations

Consider getting second opinions on release criteria that are highly
critical or more subjective. Such opinions can come from internal or
external parties. To maximize independence, consider asking the
independent party to build or acquire their own evaluation datasets,
using the same information about the intended use case(s) of the AI
solution that you intend to communicate to downstream users.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation considerations

1. Identify which evaluations are most critical or subjective and
   would benefit from independent review, such as safety
   assessments, unwanted bias evaluations, or user experience
   judgments. Include evaluations where your team is more likely
   to have blind spots that could affect its assessment.
2. Identify independent evaluation teams with the capability of
   building or acquiring independent datasets, such as quality
   assurance teams, product groups, or other research teams
   within your organization.
3. Run parallel evaluations where both the development team and
   the independent team assess the same aspects of your system
   using the same criteria and datasets. This gives you two
   perspectives on the same issues and assists you to spot areas
   where evaluations might be influenced by external factors.
4. For high-risk systems or particularly subjective evaluations,
   consider bringing in independent evaluators who have no stake
   in your project's success, but who can build their own
   evaluations datasets using only the information that you plan
   to disclose to downstream deployers and users.
5. Compare the results from different evaluation teams and
   investigate significant disagreements before making release
   decisions. When independent evaluations contradict internal
   assessments, dig deeper to understand why before reconsidering
   your evaluation approach.

## Resources

**Related documents**

- [ISO/IEC
  42001:2023 A.6.2.4 AI system verification and
  validation](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
- [Thorn
  and All Tech Is Human Forge Generative AI Principles with AI Leaders to Enact Strong Child Safety Commitments July 16,
  2024](https://www.thorn.org/blog/generative-ai-principles/ "https://www.thorn.org/blog/generative-ai-principles/")
