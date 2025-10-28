Amazon CodeCatalyst will no longer be open to new customers starting on November
7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For
more information, see [How to migrate from CodeCatalyst](migration.md "migration.md").

# Working with lifecycle management as a blueprint user

Lifecycle management is the ability to regenerate a codebase from updated options or versions of a blueprint. This
allows a blueprint author to centrally manage the software development lifecycle of every project that contains a particular
blueprint. For example, pushing a security fix to a web application blueprint will allow every project containing or created
from the web application blueprint to pick up that fix automatically. This same management framework also allows you as a
blueprint user to change blueprint options after they have been selected.

###### Topics

- [Using lifecycle management on existing projects](#using-lm-existing-projects "#using-lm-existing-projects")
- [Using lifecycle management on multiple blueprints in a project](#using-lm-multiple-bp "#using-lm-multiple-bp")
- [Working with conflicts in lifecycle pull requests](#lm-conflicts "#lm-conflicts")
- [Opting out of lifecycle management changes](#opt-out-lm "#opt-out-lm")
- [Overriding a blueprint's lifecycle management in a project](#override-updates-lm "#override-updates-lm")

## Using lifecycle management on existing projects

You can use lifecycle management for projects created from blueprints or on existing projects not associated
with any blueprints. For example, you can add a standard security practices blueprint into a five-year-old Java
application that was never created from a blueprint. The blueprint generates a security scanning workflow and other
related code. That portion of the codebase in the Java application will now be kept up to date automatically with
your team’s best practices any time changes are made to the blueprint.

## Using lifecycle management on multiple blueprints in a project

Because blueprints represent architectural components, multiple blueprints can often be used together in the same
project. For example, a project could be made up of a central web API blueprint built by a company platform engineer,
along with a release check blueprint built by the app-security team. Each of those blueprints can be updated independently
and will remember merge resolutions applied to them in the past.

###### Note

As arbitrary architectural components, not all blueprints make sense together or will logically work together,
even though they will still attempt to merge into each other.

## Working with conflicts in lifecycle pull requests

Occasionally, lifecycle pull requests might generate merge conflicts. These can be manually resolved. Resolutions are
remembered on subsequent blueprint updates.

## Opting out of lifecycle management changes

Users can remove a blueprint from a project to disassociate all references to the blueprint and opt out of lifecycle updates.
For safety reasons, this doesn’t remove or impact any of the project’s code or resources, including what was added from the blueprint.
For more information, see [Disassociating a blueprint from a project to stop updates](disassociate-bp.md "disassociate-bp.md").

## Overriding a blueprint's lifecycle management in a project

If you want to to override a blueprint’s updates to specific files in your project, you can include an ownership file in
your repository. [GitLab’s Code Owners](https://docs.gitlab.com/ee/user/project/codeowners/ "https://docs.gitlab.com/ee/user/project/codeowners/") spec is the
recommended guidelines. The blueprint always respects the code owners file over everything else and can generate a sample one
like the following:

```
new BlueprintOwnershipFile(sourceRepo, {
      resynthesis: {
        strategies: [
          {
            identifier: 'dont-override-sample-code',
            description: 'This strategy is applied accross all sample code. The blueprint will create sample code, but skip attempting to update it.',
            strategy: MergeStrategies.neverUpdate,
            globs: [
              '**/src/**',
              '**/css/**',
            ],
          },
        ],
      },
    });
```

This generates a `.ownership-file` with the following contents:

```
[dont-override-sample-code] @amazon-codecatalyst/blueprints.import-from-git
# This strategy is applied accross all sample code. The blueprint will create sample code, but skip attempting to update it.
# Internal merge strategy: neverUpdate
**/src/**
**/css/**
```
