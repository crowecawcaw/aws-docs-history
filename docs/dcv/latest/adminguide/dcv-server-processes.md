# Amazon DCV server processes

This counter set contains information about the individual Amazon DCV processes.

`agent_type can be one of: session_agent, system_agent, user_agent`

Counters are updated once per second.

| Counter name          | Description                                                        | Unit    | Notes                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------ | ------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| % Processor Time      | Percentage of processor time used by the process                   | Percent | Percentage is relative to one CPU core (i.e. 100% means the process is hogging one thread).<br>Same as \Process(NAME)\% Processor Time |
| Physical Memory Bytes | Current amount of physical memory used by the process, in bytes    | Bytes   | Same as \Process(NAME)\Working Set                                                                                                     |
| Virtual Memory Bytes  | Current size of the virtual address space of the process, in bytes | Bytes   |                                                                                                                                        |
| Process Identifier    | Numeric process identifier (PID)                                   | -       |                                                                                                                                        |
