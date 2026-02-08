# Application security

Application security describes the overall process of how you design, build, and test the
security properties of the workloads you develop. You should have appropriately trained people
in your organization, understand the security properties of your build and release
infrastructure, and use automation to identify security issues.

| HNSEC07: How do you provide encryption in transit? |
| -------------------------------------------------- |
|                                                    |

Ensuring proper encryption in transit is critical for protecting data as it moves between
cloud and on-premises infrastructure. To achieve this, implement TLS 1.2 or later encryption
for application-level traffic, maintain proper certificate management with automated rotation
before expiration.

###### Best practices

- [HNSEC07-BP01 Enforce End-to-End TLS Encryption](hnsec07-bp01.md "hnsec07-bp01.md")
