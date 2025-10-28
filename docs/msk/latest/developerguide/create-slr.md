# Create a service-linked role for Amazon MSK

You don't need to create a service-linked role manually. When you
create an Amazon MSK cluster in the AWS Management Console, the AWS CLI, or the AWS API, Amazon MSK
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create an Amazon MSK cluster, Amazon MSK creates the service-linked role for you again.
