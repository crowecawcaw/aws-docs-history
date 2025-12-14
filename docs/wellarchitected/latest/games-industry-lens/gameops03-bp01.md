# GAMEOPS03-BP01 Validate and test your existing core game

systems and infrastructure before reusing it in your game

Organizations tend to reuse existing components and source code
from previous games to save on development time and cost. These
legacy components and code may not be subjected to a thorough
review or have detailed integration testing and instead rely on
their past performance.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

While reuse assists improving
productivity, it can also introduce the risk of reintroducing past
performance and stability issues into a new project. Therefore,
when reusing existing components and source code from previous
games, robust testing should be implemented.

### Implementation steps

- **Identify reused code and
  components:** Catalog the source code, libraries,
  and components being reused from previous games. Clearly
  distinguish between actively maintained and deprecated code
- **Document original behavior and known
  issues:** Record the original performance
  characteristics, functional limitations, and known bugs or
  production incidents associated with the reused components.
- **Perform a thorough code
  review:** Conduct a detailed technical review of
  the reused components, especially those that had issues in
  the past or are poorly documented.
- **Replace or refactor high risk legacy
  components:** Prioritize replacing or updating
  legacy components that have a history of issues or are no
  longer maintainable, rather than relying on workarounds in
  production.
- **Conduct integration and
  compatibility testing:** Validate the reused
  components within the context of the new game's systems.
  Verify that they interact properly with new modules, tools,
  and APIs.
