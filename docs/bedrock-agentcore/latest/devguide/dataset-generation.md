

# Dataset generation

**Note**  
Dataset generation is in public preview. Features and APIs may change before general availability.

Dataset generation reads your agent’s traces and turns observed sessions into evaluation scenarios, then adds them to an existing dataset’s Draft. Each generated example is a normal dataset example that you review, edit, delete, and publish with the standard dataset operations. You start a generation. The service selects sessions from your traces and writes one scenario for each session, redacts sensitive data if you configured redaction, removes duplicates, and merges the results into the Draft. You then review the examples and publish a version.

A generation writes one scenario type for each run. A fixed scenario is a transcript of what a session recorded. A dynamic scenario is a model-written persona and goal that an actor can replay. The following table compares the two.


| Scenario type | What each run writes | 
| --- | --- | 
|  `FIXED`  | Each selected session (or listed trace) becomes a fixed scenario whose `turns` are the user inputs that the session recorded, in order. Nothing is invented. | 
|  `DYNAMIC` (default) | A model reads each selected session and writes a dynamic scenario with an opening `input` and an `actor_profile` that has a `goal` and `context`, with `max_turns` set to 30. | 

## How dataset generation works
<a name="dataset-generation-how-it-works"></a>

A generation runs the following steps:

1.  **Start** - You call `StartDatasetGeneration` with a trace source, a scenario type, and optional selection, sampling, and redaction settings.

1.  **Select** - The service reads the source and selects the sessions that match your selection within the time window.

1.  **Generate** - The service writes one scenario for each selected session (or one scenario for each listed trace).

1.  **Redact** - If you configured redaction, the service masks matching findings before anything is written.

1.  **Deduplicate** - The service removes duplicates within the run and against existing Draft examples, and counts them in `scenariosDeduplicated`.

1.  **Merge** - On completion, the service merges the generated examples into the dataset’s Draft automatically.

After the generation completes, you review the examples in the Draft, edit or delete any you don’t want, and publish a version.

The following topics describe how to set up and run dataset generation.