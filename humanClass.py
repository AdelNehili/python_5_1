class Human():
    def __init__(self,the_name,the_age,the_activities) -> None:
        self.name = the_name
        self.age = the_age
        self.activities = the_activities
        self.friend_list = []

    def introduce(self):
        sentence = f"""Salut, je me présente:
            -Mon nom : {self.name}
            -Mon age : {self.age}
            -Mes activités : {self.activities}
        """

        print(sentence)
    
    def add_friend(self, new_friend):
        try:
            if isinstance(new_friend, Human):
                self.friend_list.append(new_friend)
            else:
                raise Exception("Sorry, only Human can be added")
        except Exception as e:
            print(e)

    def introduce_all_friends(self):
        for i in range(len(self.friend_list)):
            self.friend_list[i].introduce()

Goku = Human("Goku",100,["Manger", "Se battre","Crier"])
Goku.introduce()

Vegeta = Human("Vegeta",100,["Perdre", "S'entrainer","Etre meilleur parent que Goku"])
Vegeta.introduce()


Goku.add_friend(Vegeta)
Goku.add_friend("Vegeta")


Goku.introduce_all_friends()