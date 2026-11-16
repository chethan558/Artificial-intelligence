def is_variable(x):
    return isinstance(x, str) and x.islower() and x not in ["apple", "riya", "john", "ram"]



def apply_substitution(term, subst):
    if isinstance(term, tuple):
        return (term[0],) + tuple(apply_substitution(x, subst) for x in term[1:])
    while term in subst:
        term = subst[term]
    return term
def occurs_check(var, term, subst):
    term = apply_substitution(term, subst)

    if var == term:
        return True

    if isinstance(term, tuple):
        return any(occurs_check(var, x, subst) for x in term[1:])

    return False



def unify(x, y, subst=None):

    if subst is None:
        subst = {}

    x = apply_substitution(x, subst)
    y = apply_substitution(y, subst)


    if x == y:
        return subst


    if is_variable(x):
        if occurs_check(x, y, subst):
            return None
        subst[x] = y
        return subst

    
    if is_variable(y):
        if occurs_check(y, x, subst):
            return None
        subst[y] = x
        return subst

    
    if not isinstance(x, tuple) or not isinstance(y, tuple):
        return None


    if x[0] != y[0]:
        return None

    
    if len(x) != len(y):
        return None


    for a, b in zip(x[1:], y[1:]):
        result = unify(a, b, subst)

        if result is None:
            return None

    return subst



print("FIRST ORDER LOGIC - UNIFICATION")


E1 = ("Eats", "x", "Apple")
E2 = ("Eats", "Riya", "y")

print("\nExpression 1:", E1)
print("Expression 2:", E2)

result = unify(E1, E2)

if result is None:
    print("\nUnification Failed")
else:
    print("\nUnification Successful")
    print("Substitution:", result)