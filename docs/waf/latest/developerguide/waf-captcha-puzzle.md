**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# AWS WAF CAPTCHA puzzles

This section explains the features and functionality of the AWS WAF CAPTCHA puzzle.

AWS WAF provides standard CAPTCHA functionality that challenges users to confirm that they
are human beings. CAPTCHA stands for Completely Automated Public Turing test to tell
Computers and Humans Apart. CAPTCHA puzzles are designed to verify that a human is
sending requests and to prevent activity like web scraping, credential stuffing, and
spam. CAPTCHA puzzles can't weed out all unwanted requests. Many puzzles have been solved
using machine learning and artificial intelligence. In an effort to circumvent
CAPTCHA, some organizations supplement automated techniques with human intervention.
In spite of this, CAPTCHA continues to be a useful tool to prevent less sophisticated
bot traffic and to increase the resources required for large-scale operations.

AWS WAF randomly generates its CAPTCHA puzzles and rotates through them to ensure that
users are presented with unique challenges. AWS WAF regularly adds new types and styles of
puzzles to remain effective against automation techniques. In addition to the puzzles,
the AWS WAF CAPTCHA script gathers data about the client to ensure that the task is
being completed by a human and to prevent replay attacks.

Each CAPTCHA puzzle includes a standard set of controls for the end user to request a
new puzzle, switch between audio and visual puzzles, access additional instructions, and
submit a puzzle solution. All puzzles include support for screen readers, keyboard
controls, and contrasting colors.

The AWS WAF CAPTCHA puzzles meet the requirements of the Web Content Accessibility Guidelines
(WCAG). For information, see [Web Content
Accessibility Guidelines (WCAG) Overview](https://www.w3.org/WAI/standards-guidelines/wcag/ "https://www.w3.org/WAI/standards-guidelines/wcag/") at the World Wide Web Consortium (W3C) website.

###### Topics

- [CAPTCHA puzzle language
  support](waf-captcha-puzzle-language-support.md "waf-captcha-puzzle-language-support.md")
- [CAPTCHA puzzle examples](waf-captcha-puzzle-examples.md "waf-captcha-puzzle-examples.md")
