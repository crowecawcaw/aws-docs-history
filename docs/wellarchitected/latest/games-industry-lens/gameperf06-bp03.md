# GAMEPERF06-BP03 Enable efficient log formatting and

batching

Configure your game server processes to generate logs in a structured and in a format that
can be parsed, such as JSON.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

Implement log batching techniques to minimize the frequency of log data transfers from
your game servers to the centralized log storage. Batching logs reduces network overhead and
improves game server performance. Use verbose or debug level logs as an exception and not a
default, as they can incur a performance and cost penalty that should be avoided when
possible.
