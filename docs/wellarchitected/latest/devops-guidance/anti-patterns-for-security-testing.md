# Anti-patterns for security testing

- **Overconfidence in test
  results**: Being overly confident about a low
  false-positive rate and not considering the potential of
  false negatives can lead to genuine threats being ignored,
  which may be exploited by attackers. Regularly re-evaluate
  and adjust security testing tools and
  methodologies. Consider periodic third-party security
  audits and human-driven exploratory testing to get an
  external perspective on the system's security posture.
- **Not considering internal threats**: Focusing security
  testing solely on external threats while neglecting potential insider threats, whether
  malicious or unintentional, can lead to unmitigated attack vectors that can be as
  damaging as external attacks. Testing should encompass all potential threat
  actors. Include scenarios in your testing strategy that emulate insider threats, such as
  permissions escalation, data exfiltration from internal roles, and social engineering.
  Continuously raise awareness, train employees on best practices, and regularly review
  access permissions.
- **Neglecting software supply chain
  attacks**: Not regularly monitoring or
  safeguarding against potential threats in the software
  supply chain, from third-party libraries to development
  tools. Supply chain attacks have become increasingly
  prevalent, and they can compromise systems even if the
  organization's proprietary code is secure. Adopt a
  comprehensive software supply chain security strategy,
  including regularly updating and auditing third-party
  components, monitoring development environments, and
  ensuring secure software development practices are
  followed by all components used to build, test, deploy,
  and operate your systems.
