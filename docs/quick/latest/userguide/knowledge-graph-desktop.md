

# Knowledge graph
<a name="knowledge-graph-desktop"></a>

Amazon Quick builds a personal knowledge graph that captures entities and the relationships between them from your connected data sources and files. The graph gives Quick contextual understanding of the people, projects, organizations, and events in your work, so it provides more relevant, personalized responses. It is kept for you, per user, in your Amazon Quick account.

If you ask about a project, Quick uses the graph to identify related people, recent meetings, associated documents, and relevant channels.

## Entity categories
<a name="kg-desktop-entity-categories"></a>

Quick organizes graph entities into categories that span the people, organizations, projects, places, events, communications, documents, actions, decisions, and terminology in your work, along with structured data types such as datasets, dashboards, and topics when relevant. The category set is supplied at runtime. Each entity has a count of edges, the relationships connecting it to other entities.

## Data sources
<a name="kg-desktop-data-sources"></a>

The graph extracts entities from connected integrations and from local folders. When you enable auto-ingestion, Quick extracts entities from your connected apps. When you enable knowledge graph extraction for a folder on the Knowledge tab in Customize (see [Knowledge](knowledge-desktop.md)), Quick extracts entities from files in that folder, independently of keyword and semantic indexing.

## Viewing the knowledge graph
<a name="kg-desktop-viewing"></a>

Open My context and choose the Knowledge graph tab for an interactive, force-directed visualization where nodes are entities and edges are relationships.
+ Node color: each category has a distinct color; a legend maps colors to categories and lets you highlight a category.
+ Node size: scaled automatically by how connected an entity is; more-connected entities appear larger.
+ Search entities: find an entity by name and jump to it.
+ Interact: click a node to select it and view its details, double-click to focus on a node and see its direct connections, scroll to zoom, and drag to pan.
+ View mode: switch between Top N connected (the most-connected entities) and Communities (clustered by community detection).
+ Display limits: choose how many nodes (50 to 1,000) and edges (100 to 2,000) render, shown against the totals, to keep large graphs responsive.
+ Node details: selecting an entity opens an entity details panel (see the next section).

### Working with an entity
<a name="kg-desktop-working-with-entity"></a>

When you select an entity, the entity details panel shows the following.
+ Name and category: the entity's display name and its category (for example, Person or Project). Choose Edit next to either to rename the entity or change its category.
+ AI-generated summary: a short summary of what Quick knows about the entity. Choose Regenerate to rebuild the summary from the latest data.
+ Connected entities: other entities that this entity is related to, grouped by relationship.
+ Source files: the files and messages Quick used to extract this entity.
+ Ask: start a new chat about the entity. Quick opens a conversation preloaded with the entity's context.
+ Delete: remove the entity and its relationships from the knowledge graph. This permanently removes the entity and any relationships that connect to it, and cannot be undone.

## Configuring and resetting the knowledge graph
<a name="kg-desktop-configuring-resetting"></a>

The Knowledge graph settings include Auto-ingest from integrations, a single toggle that lets Quick learn from your connected apps and build the graph. Per-folder knowledge graph extraction is configured separately, on the Knowledge tab in Customize (see [Knowledge](knowledge-desktop.md)).

You can reset the knowledge graph to permanently remove all entities and relationships that Quick has built. Resetting removes all people, projects, organizations, events, and relationships. It does not affect your files, your memories, or your connected services. Quick can rebuild the graph from those sources over time if you leave auto-ingest and per-folder extraction enabled.

**To reset the knowledge graph**

1. From the account menu, choose My context.

1. Choose Configuration in the upper-right corner.

1. In the Knowledge graph section, choose Reset knowledge graph.

1. Type "reset" to confirm, and then choose Reset.

A reset is permanent. There is no undo. Consider narrowing auto-ingest or per-folder extraction first if you only want to remove a specific source of entities.