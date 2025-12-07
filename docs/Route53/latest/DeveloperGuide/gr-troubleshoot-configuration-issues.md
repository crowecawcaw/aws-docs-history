# Troubleshoot configuration issues in

Route 53 Global Resolver

Route 53 Global Resolver offers extensive configuration options for DNS views, authentication, and firewall
rules, which can sometimes lead to configuration conflicts or mismatches. Identify and resolve
common Route 53 Global Resolver configuration problems that affect DNS resolution.

## Authentication problems

Common authentication issues and solutions:

Access Source rule mismatches

- Verify client device IP addresses match configured CIDR blocks
- Check for NAT or proxy devices changing source IP addresses
- Ensure Access Source rules cover all expected client device IP ranges

Token authentication failures

- Verify tokens are correctly configured on client devices
- Check token expiration dates and renewal processes
- Ensure client device clocks are synchronized for token validation

Protocol mismatches

- Verify client devices use protocols allowed by Access Source rules
- Check that DoH and DoT configurations match token protocols
- Ensure firewall rules don't block required protocols

## DNS view configuration issues

Common DNS view configuration problems:

Incorrect DNS view associations

- Verify client devices are authenticated to the intended DNS view
- Check that private hosted zones are associated with the correct DNS views
- Review firewall rules applied to each DNS view

DNS settings conflicts

- Review DNSSEC validation settings for compatibility with client devices
- Check EDNS Client Subnet settings for privacy and performance balance
- Verify firewall fail-open behavior aligns with security requirements

## Firewall rule issues

Common firewall rule configuration problems:

Rule priority conflicts

- Review rule evaluation order and ensure correct priority assignment
- Check for block rules with higher priority than intended allow rules
- Test rule changes in a controlled environment before production deployment

Domain list mismatches

- Verify domain specifications in custom domain lists
- Check wildcard patterns for correct syntax and coverage
- Ensure domain lists are updated and synchronized
