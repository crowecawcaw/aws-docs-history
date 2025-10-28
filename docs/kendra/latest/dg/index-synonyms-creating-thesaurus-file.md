# Creating a thesaurus file

An Amazon Kendra thesaurus file is a UTF-8-encoded file containing a list of synonyms
in the Solr synonym list format. The thesaurus file must be less than 5 MB.

There are two ways to specify synonym mappings:

- _Bidirectional synonyms_ are specified as a comma-separated list of
  terms. If your user queries any of the terms, then all the terms in the list are used to
  search documents, which includes the original queried term.
- _Unidirectional synonyms_ are specified as terms separated by the
  symbol "=>" between them to map terms to their synonyms. If your user queries a term on
  the left of the symbol "=>", then it is mapped to a term on the right to search for
  documents using the synonym. It is not mapped vice versa, making this
  unidirectional.
  The synonyms themselves are case sensitive, but the terms they map to are case
  insensitive. For example, `ML => Machine Learning` means if your user queries "ML"
  or "ml" or uses some other case, it will map to "Machine Learning". If you were to map this
  vice versa, `Machine Learning => ML`, then "Machine Learning" or "machine learning"
  or some other case would map to "ML".

A synonym doesn't search for an exact match on special characters. For example, if you
search for "dead-letter-queue", Amazon Kendra can return documents that match "dead letter
queue" (no hyphen). If your documents contain hyphens, such as "dead-letter-queue", Amazon Kendra processes the documents during search to remove hyphens. For generic English synonym
terms that are built into Amazon Kendra and should not be included in a thesaurus file,
Amazon Kendra can search both the hyphen version of the term and the non-hyphen version of
the term. For example, if you search "third-party" and "third party", Amazon Kendra returns
documents that match either version of those terms.

For synonyms that contain stopwords or commonly used words, Amazon Kendra returns
documents that match terms including stopwords. For example, you can create a synonym rule
to map "on boarding" and "onboarding". You cannot use stopwords alone for synonyms. For example,
if you search for "on", Amazon Kendra cannot return all documents that contain "on".

Some synonym rules are ignored. For example, `a => b` is a rule, but
`a => a` is ignored and doesn't count as a rule.

The term count is the number of unique terms in the theaurus file. The below example file
includes terms `AWS CodeStar`, `ML`,
`Machine Learning`, `autoscaling group`, `ASG`, and more.

There is a maximum amount of synonym rules per thesaurus and a maximum amount of synonyms
per term. For more information, see [Quotas for Amazon Kendra](quotas.md "quotas.md").

The following example shows a thesaurus file with synonym rules. Each line contains a
single synonym rule. Blank lines and comments are ignored.

```
# Lines starting with pound are comments and blank lines are ignored.

# Synonym relationships can be defined as unidirectional or bidirectional relationships.

# Unidirection relationships are represented by any term sequence
# on the left hand side (LHS) of "=>" followed by synonyms on the right hand side (RHS)
CodeStar => AWS CodeStar
# This will map CodeStar to AWS CodeStar, but not vice-versa

# To map terms vice versa
ML => Machine Learning
Machine Learning => ML

# Multiple synonym relationships may be defined in one line as well by comma seperation.
autoscaling group, ASG => Auto Scaling group, autoscaling
# The above is equivalent to:
# autoscaling group => Auto Scaling group, autoscaling
# ASG => Auto Scaling group, autoscaling

# Bi-directional synonyms are comma separated terms with no "=>"
DNS, Route53, Route 53
# DNS, Route53, and Route 53 map to one another and are interchangeable at match time
# The above is equivalent to:
# DNS => Route53, Route 53
# Route53 => DNS, Route 53
# Route 53 => DNS, Route53

# Overlapping LHS terms will be merged
Beta => Alpha
Beta => Gamma
Beta, Delta
# is equivalent to:
# Beta => Alpha, Gamma, Delta
# Delta => Beta

# Each line contains a single synonym rule.
# Synonym rule count is the total number of lines defining synonym relationships
# Term count is the total number of unique terms for all rules.
# Comments and blanks lines do not count.
```
