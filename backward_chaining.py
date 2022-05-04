import aima3.utils
import aima3.logic

def backward_chaining():
    clauses = list()

    clauses.append(aima3.utils.expr("(American(x) & Weapon(y) & Sells(x, y, z) & Hostile(z)) ==> Criminal(x)"))
    clauses.append(aima3.utils.expr("Enemy(Nono, America)"))
    clauses.append(aima3.utils.expr("Owns(Nono, M1)"))
    clauses.append(aima3.utils.expr("Missile(M1)"))
    clauses.append(aima3.utils.expr("(Missile(x) & Owns(Nono, x)) ==> Sells(Colonel, x, Nono)"))
    clauses.append(aima3.utils.expr("American(Colonel)"))
    clauses.append(aima3.utils.expr("Missile(x) ==> Weapon(x)"))

    kb = aima3.logic.FolKB(clauses)

    kb.tell(aima3.utils.expr("Enemy(x, America) ==> Hostile(x)"))

    criminal = aima3.logic.fol_bc_ask(kb, aima3.utils.expr("Criminal(x)"))

    print("Criminal is: ", list(criminal))


backward_chaining()
    
