# Determining the severity level of an

exposure finding

###### Note

AWS Security Hub is in preview release and is subject to change.

AWS Security Hub assigns each exposure finding a default severity of `CRITICAL`,
`HIGH`, `MEDIUM`, or `LOW`. Exposure findings with
a severity of `INFORMATIONAL` aren't published. Security Hub uses several factors
to determine the default severity level of an exposure finding:

- **Awareness** – The extent at which the
  exposure is not theoretical, but has publicly available or automated exploits.
  This applies to exposure findings for EC2 instances and Lambda functions.
- **Ease of discovery** – Whether automated
  tools, such as a port scan or internet search, are available to discover the
  resource at risk.
- **Ease of exploit** – The ease at which a
  threat actor can exploit the exposure. For example, if open network paths or
  misconfigured metadata exists, a threat actor can more easily exploit the
  exposure.
- **Likelihood of exploit** – The likelihood
  the exposure will be exploited in the next 30 days. This factor corresponds to
  the Exploit Protection Scoring System (EPSS) and applies to exposure findings
  for Amazon EC2 instances and Lambda functions.
- **Impact** – The harm if the exploit is
  carried out. For example, an exposure could lead to loss of accountability, loss
  of availability, loss of confidentiality from data exposure, or loss of
  integrity from data corruption.
