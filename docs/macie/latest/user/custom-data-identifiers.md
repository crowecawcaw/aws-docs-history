# Building custom data identifiers

In addition to using the managed data identifiers that Amazon Macie provides, you can build and
use custom data identifiers. A _custom data identifier_ is a set of
criteria that you define to detect sensitive data in Amazon Simple Storage Service (Amazon S3) objects. The criteria
consist of a regular expression (_regex_) that defines a
text pattern to match and, optionally, character sequences and a proximity rule that refine
the results. The character sequences can be: _keywords_,
which are words or phrases that must be in proximity of text that matches the regex, or
_ignore words_, which are words or phrases to exclude
from results.

With custom data identifiers, you can define detection criteria that reflect your
organization's particular scenarios, intellectual property, or proprietary data. For
example, you can detect employee IDs, customer account numbers, or internal data
classifications. If you configure [sensitive data discovery
jobs](discovery-jobs.md "discovery-jobs.md") or [automated sensitive data discovery](discovery-asdd.md "discovery-asdd.md") to use these
identifiers, you can supplement the [managed data
identifiers](managed-data-identifiers.md "managed-data-identifiers.md") that Macie provides.

In addition to detection criteria, you can optionally configure custom severity settings for
findings that a custom data identifier produces. By default, Macie assigns the _Medium_ severity to all the findings that a custom data
identifier produces. Severity doesn't change based on the number of occurrences of text that
match an identifier's detection criteria. If you configure custom severity settings,
severity can be based on the number of occurrences of text that match the criteria.

###### Topics

- [Configuration options for custom data
  identifiers](cdis-options.md "cdis-options.md")
- [Creating a custom data
  identifier](cdis-create.md "cdis-create.md")
- [Deleting a custom data
  identifier](cdis-delete.md "cdis-delete.md")
