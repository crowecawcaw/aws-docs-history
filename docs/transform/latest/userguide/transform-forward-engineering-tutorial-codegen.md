# Code generation with Kiro

After you define your application specifications, the next step is to generate source code and tests. You provide a code generation prompt to Kiro and optionally configure Hooks to improve code and test quality.

## Step 3: Generate source code and tests

### Prompt for code generation

Using the same shared steering files and the Kiro specification workflow described in [Prepare your Kiro workspace](transform-forward-engineering-tutorial.md#transform-forward-engineering-tutorial-kiro-setup "transform-forward-engineering-tutorial.md#transform-forward-engineering-tutorial-kiro-setup"), create a new spec with a prompt tailored for code generation. From the Kiro pane, click the + button under Specs and describe your project idea using prompts.

Below is a sample prompt for Kiro spec generation:

```
Mainframe-to-AWS Modernization

Context
You are assisting in a comprehensive modernization of the Customer Account Management business function from the CardDemo mainframe application.

Project Structure
- source-code/ — COBOL copybook file definitions
- ApplicationLevelAnalysis/CustomerAccountManagement/ — Business function analysis with entrypoint documentation
- carddemo-v2-main/app/ — Extracted business rules per COBOL/JCL file

Target
Produce a compilable, deployable Java Spring Boot microservice that faithfully implements all mainframe business logic, following the steering guidelines exactly.

Initial Instructions
- Read and strictly follow the steering guidelines at .kiro/steering/mainframe-modernization.md before any code generation or analysis.
- Fully understand business requirements, data flows, and program paths from the provided analysis files.
- Preserve every business rule and data structure exactly as specified — no assumptions or inference allowed.
- Generate code that complies with AWS managed services and architecture principles defined in the steering file.
- Produce a clean project structure with all dependencies declared and ready to build and deploy.
- Follow the AWS Well-Architected Tool Framework best practices for security, reliability, and operational excellence.

Deliverables
- Java Spring Boot microservice source code (fully working and deployable)
- Infrastructure as Code using AWS CDK (v2) with multi-stack architecture
- Granular tasks mapped to business rules and program entrypoints
- Documentation for all generated components

Notes
- If any information is missing or ambiguous, stop and explicitly request clarification before proceeding.
- Do not start code generation until the above steps are fully confirmed.
```

### Execute code generation

Once you have reviewed the three specs and are satisfied that they accurately reflect the desired solution, you have two options for execution:

- **Run tasks individually** – Execute each entry in tasks.md one‑by‑one, allowing you to monitor progress and intervene as needed.
- **Run all tasks at once** – Ask the Kiro agent to "Execute all tasks in the spec." Kiro will then generate the complete codebase, unit tests, and functional tests for your new AWS‑hosted application in a single pass.

#### Next steps before deployment

The generated code and test suite provide a solid starting point, but they are not yet production‑ready. Before you ship the application, a developer should:

- Review the generated source code for correctness, security, and style compliance.
- Run the automatically generated unit and functional tests, fixing any failures.
- Perform additional manual testing (e.g., integration, performance, and user‑acceptance testing) to validate the system in real‑world scenarios.

Only after this human‑in‑the‑loop verification should the application be considered ready for deployment.

### Boost code and test quality with Kiro Hooks (optional)

Agent hooks are lightweight automation utilities that let you trigger predefined Kiro actions directly from your IDE whenever a specific event occurs. By wiring these hooks into your workflow you can automatically improve the quality of the code and tests that Kiro generates.

#### Why use a Hook for AWS Transform projects?

- **Complex business logic** – AWS Transform extracts and modernizes mainframe business rules.
- **Risk of omissions** – When Kiro produces new code it may miss subtle but critical rules.
- **Continuous feedback** – A hook can detect missing rules, invoke Kiro to regenerate the relevant sections, and automatically update the test suite.

Below is a sample of predefined hook prompt:

```
{
  "enabled": true,
  "name": "Business Rules Coverage Analyzer",
  "description": "Trigger for comprehensive business rules coverage analysis and implementation",
  "version": "1",
  "when": {
    "type": "userTriggered",
    "patterns": [
      "account-management-service/scripts/analyze-business-rules-coverage.py",
      "account-management-service/scripts/analyze-business-rules-coverage.json"
    ]
  },
  "then": {
    "type": "askAgent",
    "prompt": "COMPREHENSIVE BUSINESS RULES COVERAGE ANALYSIS\n\nYou are automatically analyzing and improving business rule coverage for account-management-service. Execute these steps in sequence:\n\n## STEP 1: Run Coverage Analysis\n• Execute: cd account-management-service & python3 scripts/analyze-business-rules-coverage.py\n• Capture the current coverage percentage from console output\n\n## STEP 2: Extract Specific Uncovered Rules\n• Execute: cd account-management-service &  python3 scripts/extract_uncovered_rules.py\n• Do the Deep Analysis of the output File: account-management-service/scripts/uncovered_rules_details.json\n• This section contains ONLY the rules that need implementation - focus exclusively on these\n• Do not implement rules that are already covered or not in this list\n• Prioritize from uncovered_rules_details by:\n  - Missing tagging (business logic exists but not tagged per steering guide)\n  - Missing implementation (business logic entirely missing)\n  - High-impact rules (validation, process rules)\n\n## STEP 3: \n- Check where to implement this missing rule. \n- Scan ALL files under the Backend directories: \n1. account-management-service/src/main/java/com/enterprise/carddemo/controller\n2. account-management-service/src/main/java/com/enterprise/carddemo/service\n3. account-management-service/src/main/java/com/enterprise/carddemo/repository\n - Scan ALL files under the Frontend directories:\n1. account-management-frontend/src\n\n### STEP 4:\n• After analyzing, Focus on 5-10 rules from uncovered_rules_details per automation cycle\n\n## STEP 5: Implement Improvements\n• DO NOT implement business rules without the ACTUAL Logic like using logger.debug without Actual Implemenation. \n• For missing tags: Add proper COBOL/JCL rule documentation to existing methods\n• For missing logic: Implement new methods following the steering guide patterns\n• Ensure all new code is:\n  - Properly integrated into service flows. Your newly Generated Code should be getting invoked from some methods.\n  - Follows existing patterns in Backend files like ValidationService, CobolAccountUpdateRulesService, etc. OR in frontened files.\n  - Includes proper error handling and logging\n  - Has appropriate COBOL/JCL rule documentation headers\n\n## STEP 6: CRITICAL - Verify No Dead Code (Integration Verification)\n• MANDATORY: Verify that ALL newly implemented business rule methods are actually invoked from somewhere in the application\n• For each new method created, trace the call path to ensure it's reachable:\n  - Backend: Check that new validation/service methods are called from Controllers, other Services, or Components\n  - Frontend: Check that new utility functions are called from React components, hooks, or other utilities\n• Examples of proper integration:\n  - New validation methods should be called in Controllers or Services during request processing\n  - New formatting methods should be called when preparing data for display\n  - New business rule methods should be integrated into existing workflows\n  - New UI utilities should be used in actual form fields or components\n• Fix dead code immediately: If any method is not invoked, either:\n  - Add proper integration points (recommended)\n  - Remove the dead code (if not needed)\n• Document the integration points in your summary\n\n## STEP 7: Validate Improvements\n• Re-run: cd account-management-service & python3 scripts/analyze-business-rules-coverage.py`\n• Confirm coverage percentage increased\n• Report the improvement: \"Coverage improved from X% to Y% (+Z rules)\" with specific rule IDs moved from uncovered to covered\n\n## STEP 8: Verify and FIX compilation issues\n• Compile the Backend Code and Frontend Code to verify if the build is successful. If there are compilation issues, Fix the errors, but DO NOT implement quick fix or workarounds.\n\n## SUCCESS CRITERIA:\n✅ Coverage analysis runs successfully\n✅ At least 5-10 new rules implemented or tagged\n✅ Coverage percentage increases\n✅ No compilation errors\n✅ All new code follows COBOL/JCL business rule patterns\n✅ NO DEAD CODE: All new methods have verified call paths\n✅ Integration points documented and tested\n\n## OUTPUT REQUIRED:\n• Summary of changes made\n• Before/after coverage statistics\n• List of newly covered rules\n• Integration verification: Document call paths for each new method\n• Confirmation that all code compiles and integrates properly\n• Verification that no dead code exists"
  }
}

```

### Summary – What You've Accomplished

- Exported the artifacts from AWS Transform and imported them into a Kiro workspace.
- Defined project‑wide conventions with steering files (product, technology, and structure) and a clear prompt to guide the IDE.
- Driven the three‑phase workflow (Requirements → Design → Implementation) to produce living specifications.
- Generated a Java‑Spring‑Boot microservice, infrastructure‑as‑code, and a full test suite, with an optional Hook‑based feedback loop to catch missing business rules.

### Next Steps

- Code Review & Quality Assurance
- Test Execution & Enhancement
- CI/CD Integration
- Production Deployment & Monitoring
