

# ABAP development
<a name="abap-development"></a>

Developing ABAP objects differs from classic Git-based development workflows. ABAP objects are not files, and a change becomes an inactive version in the live system.

## Creating
<a name="abap-development-creating"></a>

Manipulating objects through ABAP Development Tools (ADT) does not follow filesystem semantics. In particular, creating an object always requires additional metadata such as specifying a package and a transport. ADT does not support partial source writes, so updating an object replaces the entire object.

## Editing
<a name="abap-development-editing"></a>

To change an object, Coding Plugin retrieves the entire object, because ADT has no partial read. For large objects, Coding Plugin writes that source to a temporary local file so that Kiro can search, edit, and append with its built-in file commands, instead of loading the whole object into the model’s context. This ensures high fidelity when editing objects and conserves the session’s context window. The edited object becomes an inactive version in the SAP system until it is activated as a separate operation.

## The self-correcting loop
<a name="abap-development-self-correcting-loop"></a>

 AWS Coding Plugin for SAP ABAP gives Kiro knowledge of the *self-correcting loop* used in ABAP development: activation, unit tests, and ABAP Test Cockpit (ATC) checks that verify syntax, preserved functionality, and ABAP code quality. This loop lets Coding Plugin find and correct its own errors, and is foundational to agentically generating high-quality code.