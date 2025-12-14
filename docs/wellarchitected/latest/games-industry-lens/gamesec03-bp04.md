# GAMESEC03-BP04 Enforce a strict security policy for player user

accounts by requiring a strong password

If a game provides players with the ability to create a user
account with a password, you should require players' passwords to
adhere to strong policies. For example, Amazon Cognito user pools
provide you with the ability
to [define password
requirements](../../../cognito/latest/developerguide/user-pool-settings-policies.md "../../../cognito/latest/developerguide/user-pool-settings-policies.md") for user accounts. Establishing a strong
password policy can protect your players' accounts from being
overtaken through social engineering and brute force attacks.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

**Customer example**

AnyCompany Games faced a crisis when their popular title
experienced a wave of account hijackings due to weak password
policies. Players who were using simple passwords like
"password123" were becoming victims of automated brute
force attacks, resulting in lost items and compromised in-game
currency. To combat this, AnyCompany Games revamped their login
system and mandated that passwords not be previously used, include
at least one uppercase letter, one number, one special character,
and a minimum length of 15 characters.

### Implementation steps

- Require strong password policies for player accounts to
  enhance security.
- Use Amazon Cognito user pools to define and enforce password
  requirements.
