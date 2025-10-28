# Detective controls

Log management is an important part of a well-architected design for reasons ranging
from security and forensics to regulatory or legal requirements.

It is equally important that you track vulnerabilities in application dependencies
because attackers can exploit known vulnerabilities found in dependencies regardless of
which programming language is used.

For application dependency vulnerability scans, there are several commercial and
open-source solutions, such as OWASP Dependency Check, that can integrate within your
CI/CD pipeline. It’s important to include all your dependencies, including AWS SDKs,
as part of your version control software repository.
