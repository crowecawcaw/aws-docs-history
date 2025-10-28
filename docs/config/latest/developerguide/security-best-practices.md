# Security Best Practices for AWS Config

AWS Config provides a number of security features to consider as you develop and implement your
own security policies. The following best practices are general guidelines and don’t
represent a complete security solution. Because these best practices might not be
appropriate or sufficient for your environment, treat them as helpful considerations rather
than prescriptions.

- Leverage tagging for AWS Config, which makes is easier to manage, search for, and filter
  resources.
- Confirm your [delivery
  channels](manage-delivery-channel.md "manage-delivery-channel.md") have been properly set, and once confirmed, verify that AWS Config is
  [recording
  properly](stop-start-recorder.md "stop-start-recorder.md").
  For more information, see [AWS Config best
  practices](https://aws.amazon.com/blogs/mt/aws-config-best-practices/ "https://aws.amazon.com/blogs/mt/aws-config-best-practices/") blog.
