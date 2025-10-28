This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Event logging

Event logging changes the default verbosity level for several backend services. It only
effects the information in the Admin, Admin-API, Switchboard, and Messaging
containers.

- **Activity:** Shows the least amount of information and is the
  default.
- **IP Address:** Shows the IP address of the sending client in
  addition to the default level.
- **Messaging:** Shows the most information, which can
  include:
  - IP address
  - Client ID
  - Device type
  - Recipients

- **Username ID:** Shows the userID associated with information in
  all other verbosity settings.
  Message contents are never shown regardless of the chosen verbosity.
