# Performance implications

- **Loading time**: Rules are loaded when agents are initialized, which may add startup time for large rule sets
- **Memory usage**: All rules are loaded into memory as part of agent context
- **Context limits**: Large rule sets may consume significant context space, potentially affecting conversation length
- **Recommendations**: Keep rules concise and focused; consider splitting very large rule sets into multiple agents
