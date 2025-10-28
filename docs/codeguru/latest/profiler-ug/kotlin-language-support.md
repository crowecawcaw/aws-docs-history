# Kotlin

You can add support for the CodeGuru Profiler agent into your Kotlin application by adding the
following lines into your startup or `main` function.

```
import software.amazon.codeguruprofilerjavaagent.Profiler

fun main() {
    Profiler.builder()
        .profilingGroupName("MyProfilingGroup")
        .build()
        .start()
    ...
}
```

You need to [add a dependency](enabling-the-agent-with-code.md "enabling-the-agent-with-code.md") to the
agent .jar file.
