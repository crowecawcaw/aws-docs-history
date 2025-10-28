# AWS AppSync directives

###### Note

We now primarily support the APPSYNC_JS runtime and its documentation. Please
consider using the APPSYNC_JS runtime and its guides [here](resolver-reference-js-version.md "resolver-reference-js-version.md").

AWS AppSync exposes directives to facilitate developer productivity when writing in
VTL.

## Directive utils

\***\*`#return(Object)`\*\***

The `#return(Object)` allows you to prematurely return from any
mapping template. `#return(Object)` is analogous to the _return_ keyword in programming languages,
as it will return from the closest scoped block of logic. Using
`#return(Object)` inside of a resolver mapping template will
return from the resolver. Additionally, using `#return(Object)` from
a function mapping template will return from the function and will continue the
run to either the next function in the pipeline or the resolver response
mapping template.

\***\*`#return`\*\***

The `#return` directive exhibits the same behaviors as
`#return(Object)`, but `null` will be returned
instead.
