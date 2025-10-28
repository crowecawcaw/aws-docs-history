# Metrics for cryptographic signing

- **Number of unsigned
  releases**: Measures the number of releases
  without cryptographic signatures. This goal of this metric
  is to reduce this percentage, reflecting increased
  compliance with cryptographic practices across the
  organization. Track it by comparing the number of unsigned
  releases to the total releases over a specific time frame.
- **Number of expired certificates
  used**: Assesses how often expired certificates
  are used. Using expired certificates suggests potential
  operational oversights in certificate renewal and
  management. Improve this metric by routinely auditing and
  updating certificate management processes and automating
  renewal reminders. Track this metric by logging and
  counting releases where expired certificates were used.
- **Time to revoke a compromised
  key**: The duration between the detection of a
  key compromise and its revocation. This measures
  efficiency of the incident response process and how
  quickly the organization can react to potential threats to
  key compromise. Aim to minimize this duration, as a
  shorter time indicates a more agile and responsive
  incident response process. Monitor this metric by
  calculating the average time between the occurrence of key
  compromise and key revocation.
- **Time to sign:** This amount of time it takes to sign a
  code artifact. If it takes too long to sign an artifact, it could be a bottleneck in the
  deployment or release process. Aim for a consistently short duration, which indicates an
  optimized and streamlined signing workflow. Measure by averaging the time taken for
  signing across the entire organization in a given time frame.
- **Time to verify**:
  Measures the duration required to verify the cryptographic
  signature of a code artifact. It ensures the verification
  process is efficient and doesn't become a bottleneck.
  Optimize by streamlining the verification procedure and
  addressing technical inefficiencies. Track by calculating
  the average time taken to verify across all signatures in
  a given period.
