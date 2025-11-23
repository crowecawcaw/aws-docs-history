# RAIBR03-BP04 Use a risk registry to track and calibrate

potential harms and risks

Establish a risk registry to track and calibrate categories of risks
across your ML lifecycle and other use cases your team or
organization may be tackling. The registry includes information
about each identified risk, including the associated use case,
examples of harmful input and output pairs, affected stakeholders,
likelihood, severity, risk level, and high-level mitigation
approaches. Risk registry maintenance includes processes for keeping
risk information current and accurate as use cases and systems
evolve, new threats emerge, and responsible AI understanding
deepens.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation considerations

1. Use a secure mechanism to capture each risk, with fields for
   the associated use case, examples of harmful input and output
   pairs, affected stakeholders, likelihood, severity, risk
   level, and high-level mitigation approaches.
2. Create workflows that link each risk in the registry to
   development artifacts such as release criteria and technical
   mitigation specifications, and track whether those fixes
   worked. Record baseline measurements before mitigation,
   implementation details, and follow-up measurements to see
   which approaches work best for different risks.
3. Periodically review registered risks to check if mitigations
   are working and risk assessments were accurate. Compare actual
   outcomes against predictions and update risk ratings when you
   have new evidence about likelihood or severity.
4. When starting a new use case, consult the risk registry to
   speed and calibrate your risk assessments.

## Resources

**Related documents:**

- [ISO/IEC
  42001:2023](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001") A.5.3 Documentation of AI system impact
  assessments
