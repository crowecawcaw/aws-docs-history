

# Versioning
<a name="acxd-versioning"></a>

Versioning helps you review and recover previous configurations for key resources in agentic CX designer.

Each time you save a supported resource, agentic CX designer captures a snapshot of that resource. This gives your team a historical record of changes so you can understand how a resource evolved, troubleshoot regressions, and restore a previous configuration when needed.

Versioning is useful when multiple builders are collaborating, when a recent change caused unexpected behavior, or when you want to experiment while keeping a recovery path available.

Versioning is available for key workspace resources:

## What can be versioned?
<a name="acxd-versioning-what"></a>


| **Resource** | **What the version can include** | 
| --- | --- | 
| Flows | Canvas structure, node configuration, conversation logic, prompts, paths, and flow settings. | 
| Applications | Via application builds. | 
| Custom slots | Slot values, synonyms, and translations. | 
| Data requests | Custom API configuration, endpoints, request and response schemas, headers, and settings. | 

Each version includes details such as the timestamp and author depending on the resource type.

## Viewing versions
<a name="acxd-versioning-viewing"></a>

**To view versions for a resource**

1. Open the resource you want to review.

1. Select its **Versions** tab.

1. Browse the available historical snapshots.

1. Select a version to preview its previous configuration.

For flows, version history is accessed from the flow **Settings** area in the Canvas.

For applications, build history is managed from the deployment or builds area. Application builds act as packaged versions of the application that can be rolled back, deployed, or promoted to an environment.

## Restoring a version
<a name="acxd-versioning-restoring"></a>

When you restore a previous version, agentic CX designer makes that configuration current again.

Restoring does not erase the version history. Instead, it creates a new saved version based on the restored configuration, preserving the full history of changes over time.

Use restore when you need to:
+ Roll back after an unintended change
+ Recover a previous working configuration
+ Compare a current issue against an earlier setup
+ Revert after testing a change that did not work as expected.