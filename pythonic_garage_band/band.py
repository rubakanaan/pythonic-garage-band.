class Band():

    members_list=[]
    solos=[]
    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.members_list.append(self)

    
    def play_solos(self):
        for i in self.members:
            Band.solos.append(i.play_solo())
        print(Band.solos)
        return Band.solos
        
    def __str__(self):
        return  f'My name is {self.name}.'

    def __repr__(self):
        return  f'My name is {self.name}.'

    @classmethod
    def to_list(cls):
        return cls.members_list
   



class Musician():

    def __init__(self, name):
        self.name = name




class Guitarist(Musician):
    def play_solo(self):
        return "face melting guitar solo"

    def get_instrument(self):
        return "guitar"

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):
    def play_solo(self):
        return "bom bom buh bom"

    def get_instrument(self):
        return "bass"

    def __str__(self):
        return f'My name is {self.name} and I play bass'

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):
    def play_solo(self):
        return "rattle boom crash"

    def get_instrument(self):
        return "drums"

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


if __name__ == "__main__":
    band = Band(  "Nirvana",
        [Guitarist("Kurt Cobain"), Bassist("Krist Novoselic"), Drummer("Dave Grohl"),], )
    
    print(Band.to_list())
