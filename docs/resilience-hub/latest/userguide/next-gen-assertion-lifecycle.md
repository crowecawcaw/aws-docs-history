

# Assertion lifecycle
<a name="next-gen-assertion-lifecycle"></a>

The recommended workflow is to run an assessment, review the assertions it generated, refine them, and run another assessment. Assertions flow through this loop as follows:

1. **Before the first assessment (optional)** – Add any assertions you already know are important, such as your expected traffic or whether the environment is production. The first assessment uses them immediately.

1. **First assessment** – The assessment engine generates AI-generated assertions that capture what it inferred about your service. It avoids topics you have already covered with your own assertions.

1. **Review** – After the assessment completes, review the assertions. Edit any that are wrong, delete any that do not apply, and add any context that is missing.

1. **Subsequent assessments** – Each later assessment uses the current set of assertions. As long as the service has at least one assertion whose source is still `AI_GENERATED`, the assessment engine does not generate new assertions. User-created assertions are never modified or removed by the next generation of Resilience Hub.

**Note**  
Editing an AI-generated assertion converts it to a user-created assertion. If you edit or delete every AI-generated assertion so that none remain, the next failure mode assessment generates a new set of AI-generated assertions. The new set avoids topics already covered by your user-created assertions. Because the new set counts toward the 20-assertion limit, delete assertions you no longer need before running that assessment. You can also use this behavior deliberately: delete all AI-generated assertions to have the engine re-evaluate your service from scratch.

Assertions are deleted when you delete the service. Assertion changes are recorded in the service event log. For more information, see [Viewing the service event log](next-gen-service-event-log.md).