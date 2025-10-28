# Things to know about Thailand number

porting

Porting in Thailand differs from other countries. Instead of the number being able
to directly moved to Amazon Connect, it’s necessary to route the calls from your current
provider to Amazon Connect. To help plan for the process here are some helpful hints.

- Numbers being ported in to Amazon Connect must be from E1 or SIP services
  only.
- The E1 or SIP service, along with all associated numbers, must be routed
  to Amazon Connect's provider's network first. Amazon Connect will help coordinate this. Based
  on your configuration this may involve additional charges to your current
  provider or Amazon Connect's provider to support the re-routing.
- Once the E1 or SIP service has ported to Amazon Connect's provider selected numbers
  from the service can be activated for use on Amazon Connect. Once activated the
  numbers will use Amazon Connect for both inbound and outbound calling.
