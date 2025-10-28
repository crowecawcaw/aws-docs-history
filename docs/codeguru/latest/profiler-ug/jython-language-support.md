# Jython

You can add support for the CodeGuru Profiler agent into your Jython application by adding the
following lines into your startup or `main` function.

```
import sys
sys.path.append("/path/to/codeguru-profiler-java-agent-1.2.4.jar")
from software.amazon.codeguruprofilerjavaagent import Profiler

Profiler.builder()
    .profilingGroupName("MyProfilingGroup")
    .build()
    .start()
...
```

You need to [add a dependency](enabling-the-agent-with-code.md "enabling-the-agent-with-code.md") to the
agent .jar file.
