# Best practices

## Your current instance/stack is your cell zero

When starting to plan your migration to a cell-based
architecture, consider your current stack as cell zero. Adding
the router layer above and little by little distributing your
workload traffic according to your cell and cell partition
strategy.

## Start with multiple cells from day one

Since the cell is a replica of your workload to handle a portion
of your customers, keep in mind from day 1 to have more than one
cell. This will bring you the adverse issues and experience
needed to operate in this type of environment, reducing
surprises.

## Start with a cell migration mechanism from day one

Migrating clients from one cell to another is a tricky topic,
depending on the nature of your workload it may require a lot of
coordination and orchestration. Have that in mind from day one.
So even if a customer quickly becomes too big for a cell, or the
cell size you initially set isn't ideal, you have the mechanism
to move your customers to other cells.

## Perform a failure mode analysis of your cell

Since the cell is a failure isolation boundary, it is a good
exercise to analyze which services make up your cell and what is
the effect of each component failing partially or completely and
make sure that other cells are not impacted.

A worksheet containing the component and cause, probability,
mitigation of the failure will already give you good ideas of
what can happen and how to react accordingly.
