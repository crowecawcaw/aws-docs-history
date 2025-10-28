# About resilience of the cell

router

In a cell-based architecture, the only component that has the shared state of all cells
is the cell router. It presents itself as a single point of failure. Therefore, it is
essential that it be built of with maximum reliability and also as a cellular component,
regardless of whether your cell strategy is AZ independent or non-AZ independent, all the
recommendations described so far and later must also be followed for the cell router. Mainly
issues of service limits, size and observability.

In other words, the routing layer still has to scale _infinitely_,
but the set of problems that you have to solve for scaling the thinnest possible layer
should be a subset of the scaling challenges that non-cellularized application would have to
face.
