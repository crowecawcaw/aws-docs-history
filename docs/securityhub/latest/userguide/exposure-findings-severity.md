# Determining the severity level of an exposure finding

AWS Security Hub assigns each exposure finding a default severity of `CRITICAL`,
`HIGH`, `MEDIUM`, or `LOW`. Exposure findings with
a severity of `INFORMATIONAL` are not published. Security Hub determines the
severity of an exposure finding by combining two dimensions, **likelihood** and **impact**, on a risk
matrix. Likelihood reflects how easily the exposure can be exploited, and impact
reflects the magnitude of harm if it is exploited.

In cases where impact cannot be determined for a resource, the severity is based
purely on likelihood.

## Risk matrix

The following table shows how likelihood and impact combine to produce the final
severity of an exposure finding. Likelihood establishes a baseline severity, and
impact adjusts it: high impact increases severity by one level (capped at Critical),
medium impact leaves severity unchanged, and low impact decreases severity by one
level (floored at Low).

Severity risk matrix| Likelihood ↓ / Impact → | Low | Medium | High |
| --- | --- | --- | --- |
| **Very High** | HIGH | CRITICAL | CRITICAL |
| **High** | MEDIUM | HIGH | CRITICAL |
| **Moderate** | LOW | MEDIUM | HIGH |
| **Low** | LOW | LOW | MEDIUM |

## Likelihood

**Likelihood** measures how easily an exposure can be
exploited, based on the contributing traits present on the resource, such as
**Assumability**, **Misconfiguration**,
**Reachability**, **Sensitive Data**, and
**Vulnerability**. Security Hub uses several characteristics to
assess likelihood, including the following:

- **Awareness** – The extent at which the
  exposure is not theoretical, but has publicly available or automated exploits.
- **Ease of discovery** – Whether automated
  tools, such as a port scan or internet search, are available to discover the
  resource at risk.
- **Ease of exploit** – The ease at which a
  threat actor can exploit the exposure. For example, if open network paths or
  misconfigured metadata exists, a threat actor can more easily exploit the
  exposure.
- **Likelihood of exploit** – The likelihood
  the exposure will be exploited in the next 30 days. This factor corresponds to
  the [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/ "https://www.first.org/epss/").

## Impact

**Impact** measures the magnitude of harm to your
environment if the exposure is exploited. For example, an exposure could lead to
loss of accountability, loss of availability, loss of confidentiality from data
exposure, or loss of integrity from data corruption.

To assess impact, Security Hub analyzes the effective permissions of the AWS Identity and Access Management
principals associated with the resource to determine the actions and AWS services
an attacker could invoke. It also identifies the existing resources an attacker could
reach and compromise through privilege escalation. For more information, see [Impact and effective permissions](exposure-findings-supported-traits.md#exposure-findings-impact-analysis "exposure-findings-supported-traits.md#exposure-findings-impact-analysis").
