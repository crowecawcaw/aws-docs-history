# Enabling logs

The Amazon CodeGuru Profiler agent uses the `logging` library. It only uses logs at or below
the `INFO` level. To see the logs, include
`logging.basicConfig(level=logging.INFO)` or
`logging.getLogger('codeguru_profiler_agent').setLevel(logging.INFO)` in your
handler code.
