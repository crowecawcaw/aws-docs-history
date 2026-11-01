

# Steering
<a name="steering"></a>

Steering gives Kiro durable, project-level instructions that apply to every prompt, kept as Markdown files under `.kiro/steering/`. For how steering works and how to write your own, see [Steering](https://kiro.dev/docs/steering/) in the Kiro documentation.

Coding Plugin ships built-in ABAP steering and adds two commands that generate steering for your environment. All of it is plain Markdown in your project, so you can review and edit any of it.

## Built-in ABAP steering
<a name="steering-abap"></a>

Coding Plugin ships steering that teaches Kiro how ABAP development works, including the self-correcting loop (see [ABAP development](abap-development.md)). This steering is active by default and needs no setup.

## Organization steering
<a name="steering-organization"></a>

Run `/workspace-init` to record your organization’s standards as steering: its development goals, naming conventions, clean core approach, and change-management practices. The command runs automatically the first time you open a workspace, and you can run it again to update what it wrote.

## Per-system steering
<a name="steering-per-system"></a>

Run `/sap-discover` to set up a connected SAP system. The command runs automatically when you connect to a new SAP system. The agent interviews you about the system and writes your answers to `.kiro/steering/sap-system-<SID>.md`. This steering gives Kiro context about the system’s role (Development, QA, and so on), important packages, useful test data, and other details that help Kiro develop effectively.

## Writing your own steering
<a name="steering-custom"></a>

You can add your own steering files under `.kiro/steering/`. For example, if your team has naming conventions, a preferred error-handling pattern, or packages that should never be modified, write those rules as a Markdown file and Kiro follows them in every session. Kiro can write steering for you. For how to write effective steering, see [Steering](https://kiro.dev/docs/steering/) in the Kiro documentation.