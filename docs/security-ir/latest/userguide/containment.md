# Containment

One definition of containment, as it relates to incident response, is the process or
implementation of a strategy during the handling of a security event that acts to minimize
the scope of the security event and contain the effects of unauthorized usage within the environment.

A containment strategy depends on a myriad of factors and can be different from one organization to
another in terms of application of containment tactics, timing, and purpose. The
[NIST SP 800-61 Computer Security Incident Handling Guide](https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final "https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final")
outlines several criteria for determining the appropriate containment strategy, which includes:

- Potential damage to and theft of resources
- Need for evidence preservation
- Service availability (network connectivity, services provided to external parties)
- Time and resources needed to implement the strategy
- Effectiveness of the strategy (partial or full containment)
- Duration of the solution (emergency workaround to be removed in four hours, temporary workaround to be removed in two weeks, permanent solution)

Regarding services on AWS, however, the fundamental containment steps can be distilled down to three categories:

- **Source containment** – Use filtering and routing to
  prevent access from a certain source.
- **Technique and access containment** – Remove access to
  prevent unauthorized access to the affected resources.
- **Destination containment** – Use filtering and routing to
  prevent access to a target resource.
