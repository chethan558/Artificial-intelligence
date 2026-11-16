from itertools import product

def pl_true(sentence, model):
    return eval(sentence, {"__builtins__": {}}, model)



def tt_entails(KB, query):

    
    symbols = ['P', 'Q', 'R']

    
    for values in product([True, False], repeat=len(symbols)):

        model = dict(zip(symbols, values))

        
        kb_true = all(pl_true(sentence, model) for sentence in KB)

        if kb_true:
            
            if not pl_true(query, model):
                return False

    return True



KB = [
    "(not Q) or P",       
    "(not P) or (not Q)", 
    "Q or R"              
]



print("P\tQ\tR\tKB")

for values in product([True, False], repeat=3):

    model = dict(zip(['P', 'Q', 'R'], values))

    result = all(pl_true(sentence, model) for sentence in KB)

    print(values[0], values[1], values[2], result, sep="\t")



queries = {
    "R": "R",
    "R -> P": "(not R) or P",
    "Q -> R": "(not Q) or R"
}


for name, query in queries.items():

    result = tt_entails(KB, query)

    print("\nDoes KB entail", name, "?")

    if result:
        print("YES")
    else:
        print("NO")


