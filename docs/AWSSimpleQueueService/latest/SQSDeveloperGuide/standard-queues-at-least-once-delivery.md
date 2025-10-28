# Amazon SQS at-least-once

delivery

Amazon SQS stores copies of your messages on multiple servers for redundancy and high
availability. On rare occasions, one of the servers that stores a copy of a message
might be unavailable when you receive or delete a message.

If this occurs, the copy of the message isn't deleted on the server that is
unavailable, and you might get that message copy again when you receive messages. Design
your applications to be _idempotent_ (they should not
be affected adversely when processing the same message more than once).
