# CIS hardening components

The Center for Internet Security (CIS) is a community-driven nonprofit organization. Their
cybersecurity experts work together to develop IT security guidelines that safeguard public
and private organizations against cyber threats. Their globally recognized set of best
practices, known as CIS Benchmarks, help IT organizations around the world to securely configure
their systems. For trending articles, blog posts, podcasts, webinars, and
whitepapers, see [CIS Insights](https://www.cisecurity.org/insights "https://www.cisecurity.org/insights") on
the _Center for Internet Security_ website.

###### CIS Benchmarks

CIS creates and maintains a set of configuration guidelines, known as the CIS Benchmarks,
which provide configuration best practices for specific technologies, including operating
systems, cloud platforms, applications, databases, and more. CIS Benchmarks are recognized
as an industry standard by organizations and standards such as PCI DSS, HIPAA,
DoD Cloud Computing SRG, FISMA, DFARS, and FEDRAMP. To learn more, see [CIS Benchmarks](https://www.cisecurity.org/benchmark "https://www.cisecurity.org/benchmark") on the _Center
for Internet Security_ website.

###### CIS hardening components

When you subscribe to a CIS Hardened Image in AWS Marketplace, you also get access to the associated
hardening component that runs a script to enforce CIS Benchmarks Level 1 guidelines for
your configuration. The CIS organization owns and maintains CIS hardening components to ensure
that they reflect the latest guidelines.

###### Note

CIS hardening components don't follow the standard component ordering rules in Image Builder
recipes. The CIS hardening components always run last to ensure that the benchmark tests run
against your output image.
