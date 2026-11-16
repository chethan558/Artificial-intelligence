import copy


def is_variable(term):
    return isinstance(term, str) and term.islower() and len(term) == 1

def subst(theta, expr):
    if isinstance(expr, tuple):
        return tuple(subst(theta, item) for item in expr)
    elif is_variable(expr) and expr in theta:
        return subst(theta, theta[expr])
    return expr

def unify(x, y, theta=None):
    if theta is None:
        theta = {}
    if theta is None:
        return None
    elif x == y:
        return theta
    elif is_variable(x):
        return unify_var(x, y, theta)
    elif is_variable(y):
        return unify_var(y, x, theta)
    elif isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            theta = unify(a, b, theta)
            if theta is None:
                return None
        return theta
    return None

def unify_var(var, x, theta):
    if var in theta:
        return unify(theta[var], x, theta)
    elif x in theta:
        return unify(var, theta[x], theta)
    else:
        new_theta = copy.deepcopy(theta)
        new_theta[var] = x
        return new_theta

def match_premises(premises, facts, theta=None):

    if theta is None:
        theta = {}
    if not premises:
        return [theta]

    first, rest = premises[0], premises[1:]
    results = []
    for fact in facts:
        new_theta = unify(first, fact, copy.deepcopy(theta))
        if new_theta is not None:
            results.extend(match_premises(rest, facts, new_theta))
    return results

def fol_fc_ask(facts, rules, query):

    kb_facts = set(facts)

    while True:
        new_inferred = set()

        for premises, conclusion in rules:

            substitutions = match_premises(premises, kb_facts)

            for theta in substitutions:
                inferred_fact = subst(theta, conclusion)

                if inferred_fact not in kb_facts and inferred_fact not in new_inferred:
                    new_inferred.add(inferred_fact)
                    print(f"Inferred: {inferred_fact}")

                    phi = unify(inferred_fact, query)
                    if phi is not None:
                        return phi

        if not new_inferred:
            return False

        kb_facts.update(new_inferred)


facts = {
    ('American', 'Robert'),
    ('Enemy', 'A', 'America'),
    ('Owns', 'A', 'T1'),
    ('Missile', 'T1')
}

rules = [
    ([('American', 'p'), ('Weapon', 'q'), ('Sells', 'p', 'q', 'r'), ('Hostile', 'r')], ('Criminal', 'p')),

    ([('Missile', 'x'), ('Owns', 'A', 'x')], ('Sells', 'Robert', 'x', 'A')),

    ([('Missile', 'x')], ('Weapon', 'x')),

    ([('Enemy', 'x', 'America')], ('Hostile', 'x'))
]


query = ('Criminal', 'Robert')


result = fol_fc_ask(facts, rules, query)

if result is not False:
    print(f"\nSuccess! Proved {query} with substitution: {result}")
else:
    print(f"\nFailed to prove {query}.")
