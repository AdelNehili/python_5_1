
def learn_f_strings():
    name = "Goku"
    age = 100
    activities = ["Manger", "Se battre","Crier"]

    sentence = f"""Salut, je me présente:
        -Mon nom : {name}
        -Mon age : {age}
        -Mes activités : {activities}
    """

    print(sentence)

#learn_f_strings()


def learn_math(a : int,b : int):
    somme = a+b
    diff = a-b
    produit = a*b
    div = a/b

    div_entiere = a//b
    reste_div = a%b

    puissance = a**b

    sentence = f"""Pour a = {a} et b = {b}:
        -somme : {somme}
        -diff : {diff}
        -produit : {produit}
        -div : {div}
        -div_entiere : {div_entiere}
        -reste_div : {reste_div}
        -puissance : {puissance}
        
    """
    print(sentence)

my_a = 5
my_b = 7
learn_math(a=my_a,b=my_b)

#En gérénéral, les boulces for permettent de parcourir les LISTES!
for i in range(0,10,1):
    print(i)

#En général, boucle while continue à tourner tant que la condition est respectée!
life = 100
while life >1:
    life-=1
    print(f"Ouch il me reste {life} pdv")

if life<=0:
    print("Bark bark, je suis mort....")