# GAMESEC01-BP02 Use AWS Control Tower to quickly set up a

multi-account environment on AWS

If you start using AWS with just a single account, you might find
your game studio growing out of it as your game development
process advances. For example, with a single AWS account, you
might begin to reach service limits, or your costs for different
projects and workloads may become more complex. Creating different
accounts for different game titles and environments allows teams
to experiment with new features, bypass service limits, and
maintain security posture and compliance. By implementing a
multi-account strategy in AWS, you can benefit from distributing
service limits across multiple accounts and gain insights into
your AWS costs.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

It is a common misconception that using multiple AWS accounts will
automatically be more confusing and time consuming. Rather, using
AWS services that are designed to facilitate the governance of
multiple accounts can assist your game studio to spend less time
managing your accounts.

You can use AWS Control Tower is a service to securely provision a
multi-account AWS environment. Control Tower is recommended if you
are building a new AWS environment, starting your journey on AWS,
or are completely new to AWS. During the short setup process , you
can integrate with other AWS services that are involved with
managing accounts and user access, such as AWS Organizations, Service Catalog, and AWS IAM Identity Center.

**Customer example**

AnyCompany Games initially operated from a single AWS account, and
they hit multiple roadblocks when one of their games' development
team reached EC2 service limits during a crucial beta test. At the
same time, their development team for a different game struggled
with resource allocation for their automated testing pipeline. The
situation reached a breaking point when AnyCompany Games couldn't
accurately separate costs between projects, making it difficult to
budget for each game's development.

AnyCompany Games then implemented a multi-account strategy using
AWS Control Tower. They created separate accounts for each game
project, with distinct development, QA, and production
environments. This account level separation isolates each projects
data and assets, so teams working on one game can't access or
modify resources from another. Through AWS Organizations, they
established a centralized billing structure that clearly showed
each game's infrastructure costs and also created
organization-wide access polices.

### Implementation steps

- Use AWS Control tower to set up an automated multi-account
  environment.
- Organize accounts based on environments (like development,
  QA, and production).
- Use AWS IAM Identity Center and Service Catalog to
  centralize user permissions and streamline resource
  provisioning across accounts.
