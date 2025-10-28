# Preparing to migrate from Neo4j to Neptune

Migrating from the Neo4j graph database to the Neptune graph database service can be approached in one of two main ways:
re-platforming or refactoring/re-architecting. The re-platforming approach involves modifying the existing data model and
application architecture to best leverage Neptune's capabilities, while the refactoring approach focuses on finding
equivalent components in Neptune to build a comparable implementation. In practice, a combination of these strategies
is often used, as the migration process involves balancing the target Neptune architecture with constraints and
requirements from the existing Neo4j implementation. Regardless of the approach, the key is to work backwards from the
application's use cases to design the data model, queries, and overall architecture that best address your needs.

## Approaches to migrating

When migrating a Neo4j application to Neptune, we recommend one of two strategies:
either re-platforming, or refactoring/re-architecting. For more information about migration
strategies, see [6 Strategies for Migrating Applications to the Cloud](https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/ "https://aws.amazon.com/blogs/enterprise-strategy/6-strategies-for-migrating-applications-to-the-cloud/"), a blog post by Stephen Orban.

The _re-platforming approach_, sometimes called
_lift-tinker-and-shift_, involves the following steps:

- Identify the use cases your application is intended to satisfy.
- Modify the existing graph data model and application architecture to best
  address these workload needs using Neptune's capabilities.
- Determine how to migrate data, queries and other parts of the source
  application into the target model and architecture.

This working-backwards approach lets you migrate your application to the kind of
Neptune solution you might design if this were a brand-new project.

The _refactoring approach_, by contrast, involves:

- Identifying the components of the existing implementation, including
  infrastructure, data, queries, and application capabilities.
- Finding equivalents in Neptune that can be used to build a
  comparable implementation.

This working-forwards approach seeks to swap one implementation for another.

In practice, you're likely to adopt a mix of these two approaches. You might start with
a use case, design the target Neptune architecture, but then turn to the existing Neo4j
implementation to identify constraints and invariants you'll have to maintain. For
example, you might have to continue integrating with other external systems, or continue
offering specific APIs to consumers of your graph application. With this information, you
can determine what data already exists to move to your target model, and what must be
sourced elsewhere.

At other points, you might start by analyzing a specific piece of your Neo4j
implementation as the best source of information about the job your application is
intended to do. That kind of archaeology in the existing application can help define
a use case that you can then design towards using Neptune's capabilities.

Whether you're building a new application using Neptune or migrating an existing
application from Neo4j, we recommend working backwards from use cases to design a
data model, a set of queries, and an application architecture that address your business
needs.
