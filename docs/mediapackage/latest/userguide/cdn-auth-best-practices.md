# Optimize MediaPackage CDN authorization

security

Implementing AWS Elemental MediaPackage CDN authorization effectively requires following security best
practices for secret management, monitoring, and operational procedures. These
recommendations help you maintain secure, cost-effective, and reliable content
delivery.

- **Use UUID format for secret values** - We
  recommend using UUID version 4 format for your secret values, which produces a
  36-character string that is both unique and unpredictable.
- **Reuse secrets across endpoints** - When
  appropriate for your security requirements, use the same secret across multiple
  endpoints in the same Region and account to reduce management overhead and
  costs.
- **Implement regular rotation** - Rotate your
  secrets periodically as part of your security best practices.
- **Monitor authorization failures** - Set up
  alarms for unusual patterns of authorization failures, which could indicate
  attempted unauthorized access.
- **Test rotation procedures** - Regularly test
  your secret rotation procedures to ensure smooth transitions during actual
  rotations.
