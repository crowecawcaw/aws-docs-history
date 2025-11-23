# RAIER02-BP02 Summarize critical information and review with

appropriate internal stakeholders

Organize evidence from your use case, risk assessments, release
criteria testing, datasets, and system design evidence into a single
document/source of truth that contains the information needed to
make a release decision. Include verification that appropriate
mitigations are in place for risks across relevant responsible AI
dimensions. Update the system registry with the go/no-go decision.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Pull together your release documentation into one package that
   includes your use case definition, risk assessment results,
   how you did on your release criteria tests, dataset quality
   reports, and system design details. Organize everything into a
   single source of truth that gives decision-makers the
   information they need to make an informed choice about
   releasing your system.
2. Check that you've addressed risks across responsible AI areas
   including safety, fairness, privacy, security, robustness,
   veracity, explainability, transparency, controllability, and
   governance. Document what mitigations you put in place and
   make sure they tackle the specific risks you identified
   earlier in your process.
3. Calculate a single readiness score that combines your
   confidence in meeting the release criteria. Start with your
   statistical confidence that the quantitative criteria will
   pass (using methods from PG-SC03-BP03). This gives you one
   clear number that shows overall system readiness for release.
4. Write an executive summary that hits the highlights including
   your key findings, whether you passed or failed each release
   criterion, what risks are still left after your mitigations,
   and a clear recommendation about whether you should go ahead
   with the release. Back up your recommendation with reasoning
   that stakeholders can understand.
5. Set up review meetings with internal teams like your legal
   experts, technical leads, risk management teams,
   compliance-aligned teams and business owners. Walk them
   through your findings and get their input on whether you're
   ready to release, since they might catch issues you missed or
   have concerns you have not considered.
6. Write down your final release decision and update your system
   registry with whether it's a go or no-go, why you made that
   decision, who signed off on it, and conditions or monitoring
   requirements you'll need to follow after release.

## Resources

**Related documents**

- [Machine
  Learning Lens for the AWS Well-Architected Framework](../machine-learning-lens/welcome.md "../machine-learning-lens/welcome.md")
