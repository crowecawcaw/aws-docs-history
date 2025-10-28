# Anti-patterns for secure access and delegation

- **Broad permissions**:
  Granting extensive permissions without regular checks can
  lead to inadvertent access rights. This poses a
  significant security risk as potential vulnerabilities or
  unauthorized activities could occur. Review and adjust
  permissions periodically, adhering strictly to the
  principle of least privilege.
- **Manual identity and access
  management**: Depending on manual methods for
  both access control and identity management may lead to
  inconsistencies, delays, and errors. This manual approach
  is especially problematic as organizations grow, making it
  harder to scale and maintain security. Transition to using
  automated processes to manage identity and access
  management to help ensure timely updates, reduce errors,
  and enhanced scalability.
- **Static permission
  management**: Without a method to periodically
  review permissions as roles or business needs evolve can
  create both security vulnerabilities and operational
  inefficiencies. Schedule regular or continuous IAM reviews
  to perform automated audits to keep IAM configurations
  updated and aligned with present-day requirements.
- **Neglecting break-glass protocols**: Lacking established
  break-glass procedures could impair timely responses during emergencies that require
  elevated access. Incorporate just-in-time (JIT) access controls and regular drills to
  handle these incidents securely and efficiently.
- **Not evolving security with
  DevOps**: Adhering strictly to existing or
  outdated security models as the organization adopts DevOps
  best practices can introduce vulnerabilities and slow down
  progress. As organizations integrate new DevOps
  capabilities, their security models must adapt as well.
  Ensure that as DevOps practices evolve, the security model
  does too, prioritizing identity-centric strategies and
  continuous assessment of potential risks. By evolving
  security practices alongside DevOps capabilities,
  organizations  can protect against both internal and
  external threats.
