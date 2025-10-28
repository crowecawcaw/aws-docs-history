# Troubleshooting privacy

protection issues

Privacy protection option is not available in the console

This indicates that your domain's TLD does not support privacy
protection. Your contact information will be publicly visible in WHOIS
queries. This is normal behavior for certain TLDs due to registry
policies or local regulations.

To verify whether your TLD supports privacy protection, check the
individual TLD page in [Domains that you can register with Amazon Route 53](registrar-tld-list.md "registrar-tld-list.md") or see [TLDs that don't support privacy
protection](privacy-protection-tld-support.md "privacy-protection-tld-support.md").

Contact information is still visible after enabling privacy
protection

Some registries maintain their own WHOIS databases and may continue
to show contact information even when privacy protection is enabled with
Route 53. This is controlled by the TLD registry, not by Route 53.

Additionally, some TLD registries intentionally maintain limited
privacy protection or redaction services for their domains.
