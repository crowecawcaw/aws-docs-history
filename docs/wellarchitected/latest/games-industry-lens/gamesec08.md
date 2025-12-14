# Application security

| GAMESEC08: How do you secure your CI/CD pipeline? |
| ------------------------------------------------- |
|                                                   |

A game development CI/CD pipeline is typically comprised of highly available source
control servers and storage, compute resources to run your builds, and software to perform
automated testing, along with the proper network connectivity from your development machines.
Securing your CI/CD pipeline is important for protecting sensitive information, preserving
code integrity, and maintaining trusted releases. Embedding governance and guardrails allows
for developer agility while maintaining good security practices.

Since games often handle payment processing, store personal information, and maintain
virtual economies that are worth real money, a security breach in the development process
could result in significant financial losses, regulatory penalties, and a loss of player
trust.

By integrating safeguards, organizations maintain visibility and control over the
software delivery process, enabling rapid incident response and promoting a culture of secure
coding practices.

###### Best practices

- [GAMESEC08-BP01 Apply security at every stage of the CI/CD
  pipeline](gamesec08-bp01.md "gamesec08-bp01.md")
