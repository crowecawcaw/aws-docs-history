# Scala

You can add support for the CodeGuru Profiler agent into your Scala application by adding the
following lines into your startup or `main` function.

```
import software.amazon.codeguruprofilerjavaagent.Profiler

object MyObject {
    def main(args: Array[String]) = {
        Profiler.builder()
            .profilingGroupName("MyProfilingGroup")
            .build()
            .start()
        ...
    }
}
```

you need to [add a dependency](enabling-the-agent-with-code.md "enabling-the-agent-with-code.md") to the
agent .jar file.
