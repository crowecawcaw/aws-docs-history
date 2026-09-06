

# Security Considerations for AWS Security Agent and AI assisted penetration testing
<a name="security-guidance"></a>

AWS Security Agent is a frontier agent that proactively secures your applications throughout the development lifecycle across all your environments. It conducts automated security reviews customized to your requirements, with security teams centrally defining standards that are automatically validated during reviews. Security Agent performs on-demand penetration testing customized to your application, discovering and reporting verified security risks. This approach scales security expertise across your applications to match development velocity while providing comprehensive security coverage. By integrating security from design to deployment, it helps prevent vulnerabilities early and at scale.

Security teams define organizational security requirements once in the AWS Console: approved authorization libraries, logging standards, and data access policies. AWS Security Agent automatically enforces these security requirements throughout development, evaluating architectural documents and code against your standards and providing specific guidance when it detects violations. This delivers consistent security enforcement across teams and scales reviews to match development velocity.

For deployment validation, AWS Security Agent transforms penetration testing from a periodic bottleneck into an on-demand capability. Security teams provide target URLs, authentication details, source code and documentation. AWS Security Agent develops deep application understanding and executes sophisticated attack chains to discover and validate vulnerabilities, enabling teams to test whenever needed.

## Key capabilities
<a name="_key_capabilities"></a>

AWS Security Agent provides comprehensive security capabilities spanning the entire development lifecycle.

## Continuum for design security review
<a name="_continuum_for_design_security_review"></a>

AWS Security Agent (now part of AWS Continuum) provides on-demand security feedback on design documents and assesses compliance with organizational security requirements before code is written. Security teams upload design documents through the web application, where the agent analyzes them against your security requirements and surfaces findings with remediation guidance. This accelerates hours-long manual reviews into focused analysis, enabling teams to address security concerns when remediation is most efficient.

## Continuum for code security review
<a name="_continuum_for_code_security_review"></a>

AWS Security Agent (now part of AWS Continuum) analyzes pull requests or uploaded code for organizational security requirements and common security issues like missing input validation and SQL injection risks. The agent provides remediation guidance directly within your code repository platform. Security teams configure which repositories to monitor, scaling evaluation across all codebases while maintaining oversight on critical issues.

## Continuum for on-demand penetration testing
<a name="_continuum_for_on_demand_penetration_testing"></a>

AWS Security Agent (now part of AWS Continuum) provides on-demand penetration testing that discovers and reports validated security vulnerabilities through tailored multi-step attack scenarios. AWS Security Agent deploys specialized AI agents that develop application context from provided documentation and credentials, then execute sophisticated attack chains to identify complex vulnerabilities that conventional tools miss. It documents findings with impact analysis, reproducible attack paths, and ready-to-implement code fixes, accelerating penetration testing from weeks to hours and scaling validation across your application portfolio.

## FAQs
<a name="_faqs"></a>

### Security & Control
<a name="_security_control"></a>

#### How does AWS Security Agent authenticate and maintain access to systems?
<a name="_how_does_aws_security_agent_authenticate_and_maintain_access_to_systems"></a>

Penetration testing is the only capability in AWS Security Agent that can authenticate to a user’s system at runtime. The AWS Security Agent accepts credentials in the form of static username and password credentials (stored in Secrets Manager), or a credential vendor (as a Lambda Function) as configuration before starting the penetration test. These credentials are used to exercise the normal functionality of the user’s system/application through the lifecycle of the penetration test. We encourage users to create new credentials with appropriately scoped permissions for the purposes of penetration testing.

#### Can users control the scope and depth of testing to prevent unintended system impacts?
<a name="_can_users_control_the_scope_and_depth_of_testing_to_prevent_unintended_system_impacts"></a>

AWS Security Agent allows customers to select a specific category of vulnerability to explore in an endpoint. Users can specify out-of-scope URLs to prevent AWS Security Agent from performing penetration testing against those targets. https://docs.aws.amazon.com/securityagent/latest/userguide/perform-penetration-test.html

#### Can AWS Security Agent itself pose a security risk?
<a name="_can_aws_security_agent_itself_pose_a_security_risk"></a>

AWS Security Agent is instructed to discover security risks, but to do so using intentionally minimal impacting payloads (like extracting the SQL version instead of dropping a table when a SQL injection attack is discovered). AWS Security Agent is also confined to deterministic guardrails to prevent risky behavior like creating excessive load against the target application. While guardrails are in place, there could still be unintentional or non-obvious business logic interactions, therefore, we always recommend doing penetration testing against a pre-production environment.

#### What data does AWS Security Agent collect and where is it stored?
<a name="_what_data_does_aws_security_agent_collect_and_where_is_it_stored"></a>

AWS Security Agent allows users to upload artifacts to provide context about their application being tested. For more information on data protection, see [Data protection in AWS Security Agent](data-protection.md). AWS Security Agent will automatically select the optimal region within your geography to process your inference requests. This maximizes available compute resources, model availability, and delivers the best customer experience. Your data will remain stored only in the region where the request originated, however, input prompts and output results may be processed outside that region. All data will be transmitted encrypted across Amazon’s secure network. For more information, see [Cross Region Inference](https://docs.aws.amazon.com/securityagent/latest/userguide/security-best-practices.html#_cross_region_inference).

#### What controls are present to block unauthorized testing against an endpoint?
<a name="_what_controls_are_present_to_block_unauthorized_testing_against_an_endpoint"></a>

Endpoints that are specified as target URLs for penetration testing will require DNS validation or HTTP validation as a measure of ownership. AWS Security Agent will ask the customer to add a TXT record to the endpoint’s DNS or expose an HTTP Route returning validation string as proof of ownership. Only after demonstrating proof of ownership will the user be able to proceed with a penetration test. Requests to URLs outside of the target and accessible URLs will be blocked by the network.

Customers are responsible for ensuring they have proper authorization to test all systems that may be affected by their penetration testing activities. All use of AWS Security Agent must comply with the AWS Acceptable Use Policy (https://aws.amazon.com/aup/).

#### How do users block and report any abuse using AWS Security Agent?
<a name="_how_do_users_block_and_report_any_abuse_using_aws_security_agent"></a>

AWS Security Agent continuously monitors requests and attempts to access URLs that are outside of the target URLs. If abuse is detected, such as attempting to use AWS Security Agent to conduct unauthorized testing on a third party endpoint, any ongoing penetration tests in the account will be terminated. Customers can reach out to AWS Support or their AWS account team for help.

#### Can AWS Security Agent replace penetration testing workflow?
<a name="_can_aws_security_agent_replace_penetration_testing_workflow"></a>

AWS Security Agent is not a professional penetration testing service, and we encourage users to integrate AWS Security Agent into their security review workflow. AWS Security Agent can provide accessibility to penetration testing on-demand during the development phase of the software lifecycle when engaging with penetration testing professionals would be too early, impractical, or need to be re-evaluated too frequently. Security professionals can review findings from AWS Security Agent to validate them, explain them, or extend upon them for new novel findings (if they exist).

#### Can users set up role-based access control (RBAC) for different team members?
<a name="_can_users_set_up_role_based_access_control_rbac_for_different_team_members"></a>

Yes. AWS Security Agent integrates with AWS IAM Identity Center, allowing admins to manage team members who can access the AWS Security Agent web application which allows users to create, manage and view design reviews and penetration tests.

### Testing Capabilities
<a name="_testing_capabilities"></a>

#### What types of vulnerabilities can AWS Security Agent detect?
<a name="_what_types_of_vulnerabilities_can_aws_security_agent_detect"></a>

AWS Security Agent detects vulnerabilities in the OWASP Top 10 for web applications. AWS Security Agent provides specific risk types that you can include or exclude in testing outlined below. Findings could arise within these risk categories or from novel findings discovered by following leads from a combination of these risk categories.
+  [Arbitrary File Upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) 
  + Arbitrary File Upload confirms that the application should be able to fend off bogus and malicious files in a way to keep the application and the users safe
+  [Code Injection](https://owasp.org/www-community/attacks/Code_Injection) 
  + Code Injection is the general term for attack types which consist of injecting code that is then interpreted/executed by the application
+  [Command Injection](https://owasp.org/www-community/attacks/Command_Injection) 
  + Command injection is an attack in which the goal is execution of arbitrary commands on the host operating system via a vulnerable application
+  [Cross-Site Scripting](https://owasp.org/www-community/attacks/xss/) (XSS)
  + Cross-Site Scripting (XSS) attacks are a type of injection, in which malicious scripts are injected into otherwise benign and trusted websites
+  [Insecure Direct Object Reference](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References) 
  + Insecure Direct Object References (IDOR) occur when an application provides direct access to objects based on user-supplied input
+  [JSON Web Token Vulnerabilities](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/06-Session_Management_Testing/10-Testing_JSON_Web_Tokens) 
  + JWTs are a common source of vulnerabilities, both in how they are implemented in applications, and in the underlying libraries
+  [Local File Inclusion](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11.1-Testing_for_Local_File_Inclusion) 
  + File Inclusion vulnerability allows an attacker to include a file, usually exploiting a “dynamic file inclusion” mechanisms implemented in the target application
+  [Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal) 
  + Path Traversal attack (also known as directory traversal) aims to access files and directories that are stored outside the web root folder
+  [Privilege Escalation](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/03-Testing_for_Privilege_Escalation) 
  + Privilege escalation occurs when a user gets access to more resources or functionality than they are normally allowed, and such elevation or changes should have been prevented by the application
+  [Server-Side Request Forgery](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery) (SSRF)
  + Server-Side Request Forgery (SSRF) occurs when the attacker can abuse functionality on the server to read or update internal resources
+  [Server-Side Template Injection](https://owasp.org/www-project-web-security-testing-guide/v41/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server_Side_Template_Injection) 
  + Server Side Template Injection vulnerabilities (SSTI) occur when user input is embedded in a template in an unsafe manner and results in remote code execution on the server
+  [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) 
  + SQL injection attack consists of insertion or “injection” of a SQL query via the input data from the client to the application
+  [XML External Entity](https://owasp.org/www-community/vulnerabilities/XML_External_Entity_(XXE)_Processing) 
  + XML External Entity attack is a type of attack against an application that parses XML input. This attack occurs when XML input containing a reference to an external entity is processed by a weakly configured XML parser

#### Does AWS Security Agent report open network ports?
<a name="exposed-network-ports"></a>

Yes. During a penetration test, AWS Security Agent scans each target host for open network ports. When a host has open TCP ports beyond the standard web ports your application uses, it adds a single informational Exposed Network Ports finding. The finding lists each open port with its detected service and version. AWS Security Agent identifies these ports for your awareness. It does not attempt to exploit the services on them.

#### What authentication methods does AWS Security Agent support?
<a name="_what_authentication_methods_does_aws_security_agent_support"></a>

AWS Security Agent supports common authentication methods, including OAuth and JWT. For more information, see the [documentation](https://docs.aws.amazon.com/securityagent/latest/userguide/provide-testing-credentials.html).

#### How does AWS Security Agent handle rate limiting and Denial of Service (DOS) prevention?
<a name="_how_does_aws_security_agent_handle_rate_limiting_and_denial_of_service_dos_prevention"></a>

AWS Security Agent has guardrails to prevent it from disrupting or taking down endpoints under test, including DOS. It has internal velocity controls to detect and handle unexpected traffic patterns.

#### Can AWS Security Agent test both REST and GraphQL APIs?
<a name="_can_aws_security_agent_test_both_rest_and_graphql_apis"></a>

Yes, AWS Security Agent can test API endpoints. We encourage customers to provide API documentation as **Additional Learning Resources** allowing AWS Security Agent to have better context on the shape and functionality of each API being tested.

#### How can users verify that AWS Security Agent has covered all critical application logic and endpoints?
<a name="_how_can_users_verify_that_aws_security_agent_has_covered_all_critical_application_logic_and_endpoints"></a>

AWS Security Agent will do a breadth-first exploration of the target application(s) and attempt to exercise it normally before attempting any exploits. This allows it to build a working understanding of the application at runtime and discover critical application logic and endpoints. Given its stochastic nature, AWS Security Agent is not guaranteed to discover and test all critical applications and endpoints for any target application. The AWS Security Agent web application provides visibility into all discovered endpoints and actions taken in the Penetration test logs.

### Accuracy & Reliability
<a name="_accuracy_reliability"></a>

#### How does AWS Security Agent validate findings before reporting?
<a name="_how_does_aws_security_agent_validate_findings_before_reporting"></a>

AWS Security Agent uses deterministic validators to help validate the reported finding. In the risk types where it is not possible to use deterministic validators, AWS Security Agent will independently replay the finding steps to gain confidence in the validity of the finding. AWS Security Agent only reports the high or medium confidence findings and hides the unverified findings by default.

#### Can AWS Security Agent adapt to custom application logic?
<a name="_can_aws_security_agent_adapt_to_custom_application_logic"></a>

AWS Security Agent optionally accepts source code, threat model, design documents, and API documentation as **Additional Learning Resources** to gain user-directed context on the target application used in the lifecycle of a penetration test.

#### Can users review AWS Security Agent testing methodology before execution?
<a name="_can_users_review_aws_security_agent_testing_methodology_before_execution"></a>

Currently there is no way to preview the course of action for AWS Security Agent. The AWS Security Agent plan is dynamic in nature based on its exploration of the target application. Customers can monitor AWS Security Agent as it goes through its exploration in real time by observing the penetration test logs. If logs show an invalid or undesirable trajectory, customers can stop ongoing penetration test run.

### Integration & Deployment
<a name="_integration_deployment"></a>

#### Does AWS Security Agent integrate with security tools (SIEM, vulnerability management) or CI/CD pipelines?
<a name="_does_aws_security_agent_integrate_with_security_tools_siem_vulnerability_management_or_cicd_pipelines"></a>

AWS Security Agent does not integrate with any existing security tools or CI/CD pipelines.

#### How does AWS Security Agent handle environment-specific configurations?
<a name="_how_does_aws_security_agent_handle_environment_specific_configurations"></a>

AWS Security Agent can be configured to run with specific IAM roles, inside VPCs, with customer-specified application relevant credentials, and with Github source repositories as source code reference to the target application.

#### Can AWS Security Agent run in air-gapped or isolated environments?
<a name="_can_aws_security_agent_run_in_air_gapped_or_isolated_environments"></a>

 [AWS Security Agent can be configured to have connectivity to VPCs](connect-agent-vpc.md), including ones that do not have outbound internet access.

#### Can multiple team members run tests simultaneously?
<a name="_can_multiple_team_members_run_tests_simultaneously"></a>

AWS Security Agent supports 5 concurrent penetration test runs per account, independent of who starts the test. Customers can create a maximum of 100 Agent Spaces and 1,000 penetration test projects.

### Operational Impact
<a name="_operational_impact"></a>

#### What’s the performance impact on tested systems?
<a name="_whats_the_performance_impact_on_tested_systems"></a>

AWS Security Agent has guardrails to prevent it from disrupting or taking down endpoints under test. This includes velocity controls on number of calls that AWS Security Agent can make to an endpoint. System or the endpoint under test should expect some increase in traffic and potential monitoring alerts being triggered due to the penetration test activity. Our recommendation is to only run AWS Security Agent or any penetration testing activity in pre-production environment.

#### Can users schedule or throttle AWS Security Agent?
<a name="_can_users_schedule_or_throttle_aws_security_agent"></a>

AWS Security Agent does not have public APIs or the ability to schedule the penetration test runs. AWS Security Agent also does not offer a concurrency control on requests to the target endpoint when starting the penetration test run. If AWS Security Agent is causing problems for target endpoints, customers can stop the ongoing penetration test(s).

#### What’s the typical duration for a complete security assessment?
<a name="_whats_the_typical_duration_for_a_complete_security_assessment"></a>

The runtime for each penetration test depends on the breadth of the target application, and the risk types configured to be assessed. Most penetration test runs complete within 16 hours.