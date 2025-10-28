# Allow requirements to relax over

time

Expansions allow you to relax rule criteria over time when FlexMatch can't find a match.
This feature ensures that FlexMatch makes a best available when it can't make a perfect
match. By relaxing your rules with an expansion, you gradually expand the pool of
players that are an acceptable match.

Expansions start when the age of the newest ticket in the incomplete match matches an
expansion wait time. When FlexMatch adds a new ticket to the match, the expansion wait time
clock may be reset. You can customize how expansions start in the `algorithm`
section of the rule set.

Here's an example of an expansion that gradually increases the minimum skill level
required for the match. The rule set uses a distance rule statement, named
_SkillDelta_ to require that all players in a match be within 5
skill levels of each other. If no new matches are made for fifteen seconds, this
expansion looks for a skill level difference of 10, and then ten seconds later looks for
a difference of 20.

```
"expansions": [{
        "target": "rules[SkillDelta].maxDistance",
        "steps": [{
            "waitTimeSeconds": 15,
            "value": 10
        }, {
            "waitTimeSeconds": 25,
            "value": 20
        }]
    }]
```

With matchmakers that have automatic backfill enabled, don't relax your player count
requirements too quickly. It takes a few seconds for the new game session to start up
and begin automatic backfill. A better approach is to start your expansion after
automatic backfill tends to kicks in for your games. Expansion timing varies depending
on your team composition, so do testing to find the best expansion strategy for your
game.
