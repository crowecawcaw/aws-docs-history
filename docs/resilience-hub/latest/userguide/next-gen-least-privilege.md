

# Least privilege recommendations
<a name="next-gen-least-privilege"></a>

Follow these recommendations to apply least privilege principles to your Next generation Resilience Hub configuration:

1. **Use ExternalId for cross-account roles** – The `ExternalId` condition in cross-account trust policies prevents confused deputy attacks.

1. **Use Organizations Service-Linked Roles** – Avoid manual cross-account role setup when possible. Service-Linked Roles provide automatically scoped, auditable access.