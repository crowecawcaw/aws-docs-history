# Access control methods

Route 53 Global Resolver offers two distinct authentication methods to control client access to your DNS
infrastructure. Each method serves different use cases and environments.

Access sources

Access sources use IP-based authentication to control DNS queries. You configure access source rules that allow or deny queries based on client IP
addresses. This method works well for environments with predictable IP ranges, such as branch
offices or VPN connections. Access sources support all DNS protocols (Do53, DoT, and DoH) and
provide straightforward configuration for network administrators.

Access tokens

Access tokens use token-based authentication with encrypted,
time-limited credentials for DoH and DoT protocols. This method suits mobile clients and environments where IP addresses
change frequently. You can renew tokens before expiration and they offer enhanced security through
encryption.

Consider these factors when selecting your authentication approach:

Authentication method comparison| Factor | Access sources | Access tokens |
| --- | --- | --- |
| Use case | Fixed IP ranges, office networks, VPN users | Mobile devices, dynamic IPs, remote workers |
| Security level | Network-based, relies on IP trust | Encrypted credentials, time-limited |
| Management complexity | Simple IP range management | Token lifecycle and distribution |
| Protocol support | Do53, DoT, DoH | DoT, DoH only |

You can use both methods simultaneously to create layered security. For example, use access
sources for office networks and tokens for remote workers.
