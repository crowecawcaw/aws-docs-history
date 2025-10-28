# Authenticating with identities

AMS uses IAM roles, which is a type of IAM identity. An IAM role is very similar to a user,
in that it is an identity with permission policies that determine what the identity can and cannot do in
AWS. However, a role doesn't have credentials associated with it and, instead of being uniquely
associated with one person, a role is intended to be assumable by anyone who needs it. An IAM user can assume a role to
temporarily take on different permissions for a specific task.

Access roles are controlled by internal group membership, which is administered and periodically reviewed by Operations Management.
