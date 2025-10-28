# Amazon Linux deprecation

The Amazon Linux AMI (also called Amazon Linux 1) reached its end of life on December 31, 2023. AWS Batch has
ended support for Amazon Linux AMI as it will not receive any security updates or bug fixes starting
January 1, 2024. For more information about the Amazon Linux end-of-life, see [AL FAQ](https://aws.amazon.com/amazon-linux-ami/faqs/ "https://aws.amazon.com/amazon-linux-ami/faqs/").

We recommend that you update existing Amazon Linux based compute environments to Amazon Linux 2023 to
prevent unforeseen workload interruptions, and continue to receive security and other
updates.

Your compute environments using the Amazon Linux AMI may continue functioning beyond the December
31, 2023 end-of-life date. However, these compute environments will no longer receive any new
software updates, security patches, or bug fixes from AWS. It is your responsibility to maintain
these compute environments on the Amazon Linux AMI after end-of-life. We recommend migrating AWS Batch
compute environments to Amazon Linux 2023 or Amazon Linux 2 to maintain optimal performance and security.

For help migrating AWS Batch from the Amazon Linux AMI to Amazon Linux 2023 or Amazon Linux 2, see [Updating compute environments - AWS Batch](updating-compute-environments.md "updating-compute-environments.md").
