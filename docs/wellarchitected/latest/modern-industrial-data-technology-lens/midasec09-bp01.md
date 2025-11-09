# MIDASEC09-BP01 Apply secure coding practices for applications and data

integrations

Implement secure coding guidelines across industrial application development and
integration pipelines to help prevent common vulnerabilities.

**Desired outcome:** Software and data interfaces in industrial
systems are resilient against common attack vectors.

**Benefits of establishing this best practice:** Reduces
injection attacks and vulnerabilities in custom code and enables secure interoperability.

**Level of risk exposed if this best practice is not
established:** High

## Implementation guidance

Adopt secure coding checklists (like OWASP), enforce static code analysis, and secure
APIs during development.

### Implementation steps

- Incorporate security requirements into software specifications.
- Use tools like Amazon CodeGuru Reviewer and SonarQube in pipelines.
- Secure APIs with authorization, throttling, and validation.
- Review and test all data transformations and payloads for tampering risks.

## Resources

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/ "https://owasp.org/www-project-top-ten/")
- [What is Amazon CodeGuru Reviewer?](../../../codeguru/latest/reviewer-ug/what-is-codeguru-reviewer.md "../../../codeguru/latest/reviewer-ug/what-is-codeguru-reviewer.md")
