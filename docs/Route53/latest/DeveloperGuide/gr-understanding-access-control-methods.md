# Understanding access control methods in

Route 53 Global Resolver

Route 53 Global Resolver offers two distinct authentication methods to control client access to your DNS
infrastructure. Each method serves different use cases and environments.

IP-based access sources

You configure access source rules that allow or deny DNS queries based on client IP
addresses. This method works well for environments with predictable IP ranges, such as branch
offices or VPN connections. Access sources support all DNS protocols (Do53, DoT, and DoH) and
provide straightforward configuration for network administrators.

Token-based authentication

Access tokens provide secure authentication for DoH and DoT protocols using encrypted,
time-limited credentials. This method suits mobile clients and environments where IP addresses
change frequently. You can renew tokens before expiration and they offer enhanced security through
encryption.

Consider these factors when selecting your authentication approach:

## Choosing the right authentication method

| Factor                | Access sources                              | Access tokens                               |
| --------------------- | ------------------------------------------- | ------------------------------------------- |
| Best for              | Fixed IP ranges, office networks, VPN users | Mobile devices, dynamic IPs, remote workers |
| Security level        | Network-based, relies on IP trust           | Encrypted credentials, time-limited         |
| Management complexity | Simple IP range management                  | Token lifecycle and distribution            |
| Protocol support      | Do53, DoT, DoH                              | DoT, DoH only                               |

You can use both methods simultaneously to create layered security. For example, use access
sources for office networks and tokens for remote workers.
