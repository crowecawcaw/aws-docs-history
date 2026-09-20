

# Assertion limits
<a name="next-gen-assertion-limits"></a>

Each service can have up to 20 assertions. This limit is shared between AI-generated and user-created assertions and cannot be increased. If a service already has 20 assertions, `CreateAssertion` returns a `ServiceQuotaExceededException`. Delete assertions that no longer apply to make room for new ones. Assertion text is limited to 1,000 characters. For more information, see [Quotas and limits](next-gen-quotas.md).