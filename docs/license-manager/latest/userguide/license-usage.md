# Seller issued license usage in License Manager

License Manager allows you to centrally track licenses across multiple Regions, by maintaining a
count of all the checked out entitlements. License Manager also tracks the identity of the user and
the underlying resource identifier, if available, associated with each check out, along
with when it was checked out. You can track this time-series data through CloudWatch Events.

Licenses may be in one of the following states:

- **Created** – The license is created.
- **Updated** – The license is updated.
- **Deactivated** – The license is deactivated.
- **Deleted** – The license is deleted.
