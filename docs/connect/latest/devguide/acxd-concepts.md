# Concepts

This section defines the key resources and terminology used in the ACXD SDK.

## Workspace

A workspace is an isolated environment containing all the resources for a project or team applications, flows, secrets, knowledge bases, and more. Most SDK operations are scoped to a single workspace, specified via the `workspaceId` client configuration.

## Application

An application is the top-level conversational AI unit. It contains flows, settings, and deployment configuration. Applications go through a build and deploy lifecycle before they are live.

## Flow

A flow defines the conversational logic, the dialog paths, node connections, messages, and behavior your application follows during a conversation. Flows are authored as a graph of typed nodes.

## Build

A build compiles an application's flows and configuration into a deployable artifact. Builds are immutable. Once built, the artifact does not change.

## Deployment

A deployment publishes a build to a channel, making it live for end users. You can have multiple deployments per application (e.g., production, staging).

## Secret

A secret stores a sensitive value (API key, credential, connection string) encrypted at rest. Secrets can be referenced in data requests and integrations without exposing the value.

## Context Variable

A context variable is a typed variable available across conversations within a workspace. Use them to pass information between flows or from external systems.

## Slot Type

A slot type defines a custom entity for extracting structured data from user input, for example a list of product names or cities with synonyms.

## Data Request

A data request is a webhook integration that retrieves or sends data during a conversation. It connects your application to external APIs and services.

## Knowledge Base

A knowledge base is a collection of articles or documents that power AI-generated responses. Knowledge bases must be published before they are available in conversations.

## Guardrail

A guardrail is a safety rule that monitors conversation content and enforces behavior, like blocking, masking, or rerouting when violations are detected.

## Evaluation

An evaluation runs automated quality checks against your application using defined criteria. Evaluations produce scored results and detailed logs.

## Simulation

A simulation runs automated conversations against a deployed application to test behavior at scale.

## Scenario

A scenario defines a scripted test conversation, a sequence of user inputs and expected behaviors used for automated testing.

## Modality

A modality defines the input/output schema for a specific interaction channel (text, voice, custom).

## Analytics Tag

An analytics tag labels conversation events as positive, negative, or neutral for reporting and analysis.

## Trail

A trail is the audit log of changes made to workspace resources, who changed what, and when.

## Programmatic User

A programmatic user is a machine identity that authenticates with the ACXD SDK via API key. Programmatic users are managed by account administrators.

## Role

A role defines a set of permissions. Roles can be pre-defined (administrator, developer, content manager, read-only) or custom. Roles are assigned to programmatic users to control what they can access.
