# Adding custom synonyms to an index

To add custom synonyms to an index, you specify them in a thesaurus file. You can include
business-specific or specialized terms in Amazon Kendra using synonyms. Generic English
synonyms, such as `leader, head`, are built into Amazon Kendra and should not be
included in a thesaurus file, including generic synonyms that use hyphens. Amazon Kendra
supports synonyms for all response types, which include `DOCUMENT` response types and
`QUESTION_ANSWER` or `ANSWER` response types. Amazon Kendra currently
does not support adding
synonyms flagged as stopwords. This is to be included in a future release.

Amazon Kendra makes correlations between synonyms. For example, using the synonym pair
`Dynamo, Amazon DynamoDB`, Amazon Kendra correlates Dynamo with Amazon DynamoDB. The query "What is dynamo?" then returns a document such as "What is Amazon DynamoDB?". With synonyms, Amazon Kendra can more easily pick up the
correlation.

The thesaurus file is a text file stored in an Amazon S3 bucket. See [Adding a thesaurus to an index](index-synonyms-adding-thesaurus-file.md "index-synonyms-adding-thesaurus-file.md").

The thesaurus file uses the [Solr synonym format](https://lucene.apache.org/solr/guide/6_6/filter-descriptions.html#FilterDescriptions-SynonymGraphFilter "https://lucene.apache.org/solr/guide/6_6/filter-descriptions.html#FilterDescriptions-SynonymGraphFilter"). Amazon Kendra has a limit on the number of thesauri per
index. See [Quotas](quotas.md "quotas.md").

Synonyms can be useful in the following scenarios:

- Specialized terms that are not traditional English language synonyms such as `NLP,
Natural Language Processing`.
- Proper nouns with complex semantic associations. These are nouns that the general public
  are unlikely to understand, for example, in machine learning, `cost, loss, model
performance`.
- Different forms of product names, for example, `Elastic Compute Cloud,
EC2`.
- Domain-specific or business-specific terms, such as product names. For example,
  `Route53, DNS`.
  Do not use synonyms in the following scenarios:

- Generic English language synonyms such as `leader, head`. These synonyms are
  not domain-specific,and using synonyms in these scenarios might have unintended
  effects.
- Typographical errors such as `teh => the`.
- Morphological variants like the plurals and possessives of nouns, the comparative and
  superlative form of adjectives, and the past tense, past participle and progressive form of
  verbs. One example of comparative and superlative adjectives is `good, better,
best`.
- Unigram (single word) stop words such as `WHO`. Unigram stop words are not
  allowed in the thesaurus and are excluded from search. For example, `WHO => World
 Health Organization` is rejected. You can use `W.H.O.` however as a
  synonym term, and you can use stop words as part of a multi-word synonym. For example,
  `of` is not allowed but `United States of America` is
  accepted.
  Custom synonyms make it easy to improve Amazon Kendra's understanding of your
  business-specific terminology by expanding your queries to cover your business-specific
  synonyms. Although synonyms can improve search accuracy, it is important to understand how
  synonyms affect latency so you can optimize for this.

A general rule for synonyms is: the more terms in your query that are matched and expanded
with synonyms, the greater potential impact on latency. Other factors that affect latency
include the average size of documents indexed, the size of your index, any filtering on search
results, and the overall load on your Amazon Kendra index. Queries that don’t match any
synonyms are not affected.

A general guideline for how synonyms affect latency:

| **Use case**                                                                                                           | **Increase in latency\*** |
| ---------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Typical natural language or keyword queries of 3 to 5 words each                                                       | Less than 15 percent      |
| 1 query term expands to 3 synonyms                                                                                     |
| Index of about 500,000 documents (averaging 10.48 KB of extracted text per<br>document) or 30,000 FAQ / question pairs |

\*_Performance varies based on your specific use of synonyms and configurations on
your index. It’s best to test search performance to obtain more accurate benchmarks for your
specific use case._

If your thesaurus is large, has a high term expansion ratio, and your latency increase is
not within acceptable boundaries, you can try one or both of the following:

- Trim your thesaurus to reduce the expansion ratio (number of synonyms per term).
- Trim the overall coverage of terms (number of lines in your thesaurus).
  Alternatively, you can increase the provisioning capacity (virtual storage units) to offset
  the latency increase.

###### Topics

- [Creating a thesaurus file](index-synonyms-creating-thesaurus-file.md "index-synonyms-creating-thesaurus-file.md")
- [Adding a thesaurus to an index](index-synonyms-adding-thesaurus-file.md "index-synonyms-adding-thesaurus-file.md")
- [Updating a thesaurus](index-synonyms-update.md "index-synonyms-update.md")
- [Deleting a thesaurus](index-synonyms-delete.md "index-synonyms-delete.md")
- [Highlights in search
  results](index-synonyms-enabling-synonyms-in-results.md "index-synonyms-enabling-synonyms-in-results.md")
