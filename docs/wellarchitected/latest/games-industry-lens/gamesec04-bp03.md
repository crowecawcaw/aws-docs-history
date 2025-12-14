# GAMESEC04-BP03 Implement geographic restrictions to limit

unauthorized access

When a player requests your content, Amazon CloudFront serves the
requested content from the nearest edge location, regardless of
where the player is located. However, there may be scenarios in
which you need to restrict how your content is accessible by users
in specific parts of the world. For example, you may have a rolling
game deployment strategy that releases content in phases on a
country-by-country basis, or you may have to abide by
country-specific access controls. 

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

You can use
[geographic
restrictions](../../../AmazonCloudFront/latest/DeveloperGuide/georestrictions.md "../../../AmazonCloudFront/latest/DeveloperGuide/georestrictions.md"), also known as geo blocking, to block players
in specific geographic locations from accessing content that you're
distributing through a CloudFront distribution. This feature lets
you restrict access to files that are associated with a
distribution and restrict access at the country level.
Alternatively, you can use a third-party geo-location service to
restrict access to a subset of the files that are associated with a
distribution or to restrict access at a finer granularity than the
country level.

By using CloudFront geographic restrictions, you can allow your
players to only access your content if they're in one of the
countries that are on an allow list of approved countries. You can
also block your players from accessing your content if they're in
one of the countries that are on a deny list of banned countries.
If a request is received from a blocked geographic location,
CloudFront will return a 403 Forbidden HTTP status code to the
player. It is important to note that this works well for
non-sensitive content and should not be used as stand-alone
protection for PII or sensitive game artifacts.

### Implementation steps

- Use CloudFront geographic restrictions to allow or deny
  content access based on country-level allow or deny lists.
- Return a 403 Forbidden HTTP status code for requests
  originating from blocked geographic locations.
- Avoid relying solely on geo restrictions for protecting
  sensitive content or PII
