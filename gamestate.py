from audioop import add
import pygame, sys
from pygame.locals import *
from Afvalgame import Main_afval
from constanten import (
    BREEDTE,
    HOOGTE,
    LIJST_CORDINATEN_DOOLHOF1,
    LIJST_COORDS_OMG,
    CODE,
)
from boris import Player
from kist import Schatkist
from npc import Npc
from tree import trees
from wereld import World
from doors import Doors
from oversteek import *
from kleurcode import Kleur
from Afvalgame import *
from Grid_puzzle import *

main_game = Main()  # voor oversteek minigame
main_game_afval = Main_afval()  # voor afval minigame
main_game_grid = Main_grid()

brecht = Npc(100, 100, "Brecht")
carlo = Npc(200, 100, "Carlul")
cisse = Npc(300, 200, "Cisse")
georges = Npc(400, 100, "Georges")
lucas = Npc(500, 100, "Lucas")

vlot = Npc(100, 100, "vlot")

boris = Player(BREEDTE // 2, HOOGTE - 100, ["key1", "key2"])
bomen_lijst = []
omg_lijst = []

# aanmaken kleurcode.
kleur1 = Kleur(518, 240)
kleur2 = Kleur(578, 240)
kleur3 = Kleur(638, 240)
kleur4 = Kleur(698, 240)

grkleur1 = pygame.sprite.Group()
grkleur1.add(kleur1)
grkleur2 = pygame.sprite.Group()
grkleur2.add(kleur2)
grkleur3 = pygame.sprite.Group()
grkleur3.add(kleur3)
grkleur4 = pygame.sprite.Group()
grkleur4.add(kleur4)

for cordinaten in LIJST_CORDINATEN_DOOLHOF1:
    bomen_lijst.append(trees("treeden", cordinaten[0], cordinaten[1]))

for coords in LIJST_COORDS_OMG:
    omg_lijst.append(trees("crystal", coords[0], coords[1]))


kist1 = Schatkist(str(CODE), 900, 300, "key5")
kist2 = Schatkist("5", 175, 75, "key3")
kist3 = Schatkist("79000", 200, 100, "key6")
kist4 = Schatkist("01", 1000, 350, "key4")

door1 = Doors(0, HOOGTE // 2, "deur1")
door2 = Doors(BREEDTE, HOOGTE // 2, "deur2")
door3 = Doors(BREEDTE // 2, 0, "deur3")
door4 = Doors(BREEDTE // 2, HOOGTE, "deur4")

doors1 = pygame.sprite.Group()
# dit gebeurt vanaf de speler in een wereld komt waar de deur aanwezig moet zijn
# doors1.add(door1)
doors2 = pygame.sprite.Group()
# dit gebeurt vanaf de speler in een wereld komt waar de deur aanwezig moet zijn
# doors2.add(door2)
doors3 = pygame.sprite.Group()

doors3.add(door3)
doors4 = pygame.sprite.Group()
# dit gebeurt vanaf de speler in een wereld komt waar de deur aanwezig moet zijn
# doors4.add(door4)
cisses = pygame.sprite.Group()
carlos = pygame.sprite.Group()
brechts = pygame.sprite.Group()
lucass = pygame.sprite.Group()
georgess = pygame.sprite.Group()
vlots = pygame.sprite.Group()
bomen = pygame.sprite.Group()
kisten = pygame.sprite.Group()


wereld_min1 = World(
    "backgroundbeach", [door3], [cisse, carlo], None, [], boris, "walktype3", []
)
wereld2 = World(
    "backgroundpath",
    [door1, door2, door3, door4],
    [brecht, cisse, carlo, georges, lucas],
    kist2,
    [],
    boris,
    "walktype1",
    [],
)
wereld1 = World("zij1", [door2], [brecht, cisse], kist1, [], boris, "walktype3", [])
wereld3 = World(
    "bosgrond",
    [door1],
    [carlo, brecht, cisse, georges, lucas],
    None,
    bomen_lijst,
    boris,
    "walktype2",
    [],
)
wereld5 = World(
    "cliff",
    [door1, door2, door3, door4],
    [georges, lucas, vlot],
    kist3,
    [],
    boris,
    "walktype1",
    [],
)
wereld6 = World("spiegelwereld", [door1], [], kist4, omg_lijst, boris, "walk_omg", [])
wereld7 = World("trashworld", [door4], [cisse], None, [], boris, "walktype1", [])
wereld8 = World(
    "wereld8",
    [door1, door2, door3, door4],
    [cisse, brecht, georges, lucas],
    None,
    [],
    boris,
    "walktype1",
    [kleur1, kleur2, kleur3, kleur4],
)
wereld9 = World(
    "oilocean",
    [door1],
    [brecht],
    None,
    [],
    boris,
    "walktype1",
    [],
)
wereld11 = World(
    "endworld",
    [door4],
    [vlot],
    None,
    [],
    boris,
    "laatste_walk",
    [],
)
wereld_einde = World("banner", [], [], None, [], boris, "walktype1", [])


class Gamestate:
    def __init__(self):
        self.level = -1  # moet op -1 komen maar staat op vijg voor testen
        self.oversteek_played = False
        self.afval_played = False
        self.grid_played = False
        self.praat = True

    def bots(self):
        if pygame.sprite.spritecollideany(boris, doors1):
            controle_key = f"key{self.level-1}"  # voor andere werelden zorg dat de key verwijst naar de wereld waar hij naartoe wilt dus key vijf verwijst naar de wereld die waarde vijf heeft
            if controle_key in boris.boekentasje:
                self.verwijderen_carracters()

                pygame.time.delay(500)
                wereld2.teleportplayer(boris, BREEDTE - 50, HOOGTE // 2)
                self.level -= 1
            else:
                wereld2.praat(
                    f"Boris heeft sleutel {self.level-1} nog niet",
                    boris.rect,
                    door1,
                )
        elif pygame.sprite.spritecollideany(boris, doors2):
            controle_key = f"key{self.level+1}"  # voor andere werelden zorg dat de key verwijst naar de wereld waar hij naartoe wilt dus key vijf verwijst naar de wereld die waarde vijf heeft
            if controle_key in boris.boekentasje:
                self.verwijderen_carracters()

                pygame.time.delay(500)
                wereld2.teleportplayer(boris, 50, HOOGTE // 2)
                self.level += 1
            else:
                wereld2.praat(
                    f"Boris heeft sleutel {self.level+1} nog niet",
                    boris.rect,
                    door2,
                )

        elif pygame.sprite.spritecollideany(boris, doors3):
            controle_key = f"key{self.level+3}"  # voor andere werelden zorg dat de key verwijst naar de wereld waar hij naartoe wilt dus key vijf verwijst naar de wereld die waarde vijf heeft
            if controle_key in boris.boekentasje:
                self.verwijderen_carracters()

                pygame.time.delay(500)
                wereld2.teleportplayer(boris, BREEDTE // 2, HOOGTE - 100)
                self.level += 3
            else:
                wereld2.praat(
                    f"Boris heeft sleutel {self.level+3} nog niet",
                    boris.rect,
                    door3,
                )

        elif pygame.sprite.spritecollideany(boris, doors4):
            self.verwijderen_carracters()

            pygame.time.delay(500)
            wereld2.teleportplayer(boris, BREEDTE // 2, 100)
            self.level -= 3

    def state_manager(self, events):
        if self.level == -1:

            self.wereld_min1_run()

        if self.level == 1:

            self.wereld_1_run()

        elif self.level == 2:

            self.wereld_2_run()

        elif self.level == 3:

            self.wereld_3_run()

        elif self.level == 4:

            self.oversteek_minigame(events)

        elif self.level == 5:

            self.wereld_5_run()

        elif self.level == 6:

            self.wereld_6_run()

        elif self.level == 7:

            self.afval_minigame(events)

        elif self.level == 8:
            self.wereld_8_run()

        elif self.level == 9:
            self.grid_game(events)

        elif self.level == 11:
            self.wereld_11_run()

        elif self.level == 12:
            self.wereld_einde_run()

        # zeggen welk level er moet gerund worden
        self.bots()

    def verwijderen_carracters(self):
        carracter_list = [brecht, cisse, carlo]
        kist_lijst = [kist1, kist2]
        deuren_lijst = [door1, door2, door3, door4]
        # omg_lijst nieuw
        for x in bomen_lijst + carracter_list + kist_lijst + deuren_lijst + omg_lijst:
            x.kill()

    # TODO adds in alle if statments opkuisen

    def oversteek_minigame(self, events):
        # TODO dit in een fucntie oversteekgame zetten.
        main_game.run_game(main_game, events, boris)
        if main_game.win():
            # wereld toe voegen
            boris.boekentasje.append("key8")
            # TODO zeggen da je gewoonnen hebt en key hebt
            self.oversteek_played = True
            wereld5.timer2 = 240
            # boris naar wereld 5
            self.level = 5
            # boris teleporteren in wereld 5
            wereld5.teleportplayer(boris, 75, HOOGTE // 2)

        if main_game.game_over():
            # transporteren boris
            main_game.boris.x = cell_number
            main_game.boris.y = 0
            main_game.bridge.x = [cell_number]
            main_game.bridge.y = [0]
            # bridge reseten
            main_game.bridge.co = [[int(cell_number), 0]]
            # opnieuw maken bridge
            main_game.bridge.make_bridge()
            # tijd gelijk aan nul stellen
            main_game.t = 0
            # zeggen dat je verloren hebt
            self.oversteek_played = True
            wereld5.timer2 = 240
            # terug naar wereld 5
            self.level = 5
            # boris teleporteren in wereld5
            wereld5.teleportplayer(boris, 50, HOOGTE // 2)

    def afval_minigame(self, events):
        main_game_afval.afval_run(main_game_afval, events)
        if main_game_afval.win():
            self.level = 8
            self.afval_played = True
            wereld8.teleportplayer(boris, 50, HOOGTE // 2)
            boris.boekentasje.append("key9")

        if main_game_afval.check_fail():
            main_game_afval.reset()
            self.level = 8
            self.afval_played = True
            wereld8.teleportplayer(boris, 50, HOOGTE // 2)

    def grid_game(self, events):
        main_game_grid.grid_while(events)
        if main_game_grid.check_full_grid():
            self.level = 8
            self.grid_played = True
            boris.boekentasje.append("key11")

    def wereld_min1_run(self):
        cisses.add(cisse)
        carlos.add(carlo)
        doors3.add(door3)

        wereld2.teleport(BREEDTE // 2 - 70, 100, "Carlul")
        wereld2.teleport(400, 200, "Cisse")
        wereld_min1.act("")
        wereld_min1.praat(
            f"Alles oké? Je bent hier aangespoeld. Geen zorgen, we helpen je! Ga verder. Ik laat je kennis maken met de rest",
            boris.rect,
            cisse,
        )
        wereld_min1.praat(
            f"Zoek het vlot en ontsnap, als je vast zit raadpleeg https://users.ugent.be/~brsteven/Project",
            boris.rect,
            carlo,
        )

    def wereld_1_run(self):
        doors2.add(door2)
        cisses.add(cisse)
        brechts.add(brecht)
        kisten.add(kist1)
        wereld1.act("Wat is de code")
        # aanpassen van de waarden voor cisse zijn spawn point/rect.center
        wereld1.teleport(250, 230, "Cisse")
        wereld1.teleport(300, 350, "Brecht")
        wereld1.praat(
            "Hey Boris, mooie tuin hé! Enige propere plek hier, er zijn veel plaatsen op het eiland vervuilt. Wie doet zoiets...",
            boris.rect,
            cisse,
        )
        wereld1.praat(
            "Wist je dat er 79000 ton plastiek in de stille oceaan ligt! Hopelijk kunnen we er iets aan doen...",
            boris.rect,
            brecht,
        )

    def wereld_2_run(self):
        cisses.add(cisse)
        carlos.add(carlo)
        brechts.add(brecht)
        georgess.add(georges)
        lucass.add(lucas)
        doors1.add(door1)
        doors2.add(door2)
        doors3.add(door3)
        doors4.add(door4)
        kisten.add(kist2)

        wereld3.teleport(BREEDTE // 2 + 100, 180, "Brecht")
        wereld3.teleport(BREEDTE // 2 + 100, 340, "Carlul")
        wereld3.teleport(BREEDTE // 2 - 100, 420, "Cisse")
        wereld3.teleport(BREEDTE // 2 - 100, 260, "Lucas")
        wereld3.teleport(BREEDTE // 2 - 100, 100, "Georges")

        wereld2.act("Hoeveel zeesterren waren er op het strand?")
        wereld2.praat("Aangenaam Boris, mijn naam is Brecht", boris.rect, brecht)
        wereld2.praat("Welkom Boris! Ik ben Carlo", boris.rect, carlo)
        wereld2.praat(
            "Oh, ik ben me vergeten voorstellen! Ik ben Cisse. Hier zijn mijn maten, makkers, (Maes)...",
            boris.rect,
            cisse,
        )
        wereld2.praat("Yo Boris, ik ben Lucas", boris.rect, lucas)
        wereld2.praat(
            "Hallo Boris, ik ben Georges. Moest je hulp nodig hebben kan je ons altijd vinden!",
            boris.rect,
            georges,
        )

    def wereld_3_run(self):
        for boom_aanwezig in wereld3.bomen:
            bomen.add(boom_aanwezig)

        carlos.add(carlo)
        cisses.add(cisse)
        brechts.add(brecht)
        georgess.add(georges)
        lucass.add(lucas)
        doors1.add(door1)

        boris.collisiondoolhof(boris, bomen)
        wereld3.teleport(50, 450, "Brecht")
        wereld3.teleport(50, 100, "Carlul")
        wereld3.teleport(1180, 440, "Cisse")
        wereld3.teleport(1180, 130, "Lucas")
        wereld3.teleport(800, 290, "Georges")
        wereld3.act("")

        wereld3.praat(
            f"Dag Boris, de code is {str(CODE)}. Je bent toch niet eerst naar al de rest gegaan hé want zij weten hem niet...",
            boris.rect,
            carlo,
        )
        wereld3.praat(
            "Ik weet de code niet maar wist je dat 10% van de wereldbevolking heeft geen toegang tot drinkbaar water!",
            boris.rect,
            cisse,
        )
        wereld3.praat(
            "Ik weet de code niet, sorry. Je kan wel altijd elke mogelijke combinatie uitproberen! Veel succes...",
            boris.rect,
            brecht,
        )
        wereld3.praat(
            "Ik denk dat de code 1234 is maar ben niet meer zeker...",
            boris.rect,
            georges,
        )
        wereld3.praat(
            "Je hebt de code nodig? Ik weet hem niet maar Georges of Carlo normaal wel.",
            boris.rect,
            lucas,
        )

    def wereld_5_run(self):
        carlos.add(carlo)
        georgess.add(georges)
        vlots.add(vlot)
        lucass.add(lucas)
        doors4.add(door4)
        doors3.add(door3)
        doors2.add(door2)
        doors1.add(door1)
        kisten.add(kist3)

        wereld5.teleport(1100, 300, "Georges")
        wereld5.teleport(150, 200, "Lucas")
        wereld5.teleport(17, 250, "vlot")
        wereld5.act("Hoeveel ton plastiek ligt er in de stille oceaan")
        wereld5.praat(
            "Op het einde van de brug ligt een sleutel. Na een tijd wordt hij ontzichtbaar dus onthoud het patroon!",
            boris.rect,
            lucas,
        )

        wereld5.minigame_win_lose(
            "key8",
            boris,
            self.oversteek_played,
            "Je bent van de brug gevallen, probeer opnieuw",
        )
        wereld5.praat(
            "Wees voorzichtig Boris. Die grot is echt vreemd. Alles is door omgedraait...",
            boris.rect,
            georges,
        )

    def wereld_6_run(self):
        # nieuw
        for boom_aanwezig in wereld6.bomen:
            bomen.add(boom_aanwezig)
        doors1.add(door1)
        kisten.add(kist4)
        # nieuw
        boris.omg_collision(boris, bomen)
        wereld6.act("retaw raabknird neeg tfeeh gnikloved ed nav tnecorp leeveoH")

    def wereld_8_run(self):
        cisses.add(cisse)
        brechts.add(brecht)
        georgess.add(georges)
        lucass.add(lucas)
        wereld8.teleport(50, 180, "Cisse")
        wereld8.teleport(BREEDTE - 50, 320, "Brecht")
        wereld8.teleport(BREEDTE // 2 - 120, 400, "Georges")
        wereld8.teleport(BREEDTE // 2 - 200, 350, "Lucas")
        doors1.add(door1)
        doors2.add(door2)
        doors3.add(door3)
        doors4.add(door4)
        wereld8.act("")
        if "key11" in boris.boekentasje and "key9" in boris.boekentasje:

            if self.praat:
                wereld8.teleportplayer(boris, BREEDTE - 75, HOOGTE // 2)
                wereld8.timer2 = 240
                self.praat = False
            wereld8.minigame_win_lose(
                "key11", boris, self.grid_played, "Het meer is nog niet proper"
            )

        else:
            wereld8.minigame_win_lose(
                "key9",
                boris,
                self.afval_played,
                "Je hebt niet genoeg vuilnis opgeruimd",
            )

        wereld8.praat(
            "Hé Boris, kan je me helpen? 15 vuilniszakken zijn genoeg. Dan kan ik je verder helpen",
            boris.rect,
            cisse,
        )
        wereld8.praat(
            "Je komt als geroepen Boris! Ik heb gezien dat er een olievlek is in dat meer. Kan me helpen met het op te ruimen?",
            boris.rect,
            brecht,
        )
        wereld8.praat(
            "Ik heb gehoord dat je van dat toestel een sleutel kan krijgen! Ergens op het eiland zijn er tips te vinden...",
            boris.rect,
            georges,
        )
        wereld8.praat(
            "Druk op 'N' om de platen van kleur te veranderen",
            boris.rect,
            lucas,
        )
        wereld8.act_kleurcode(boris, grkleur1, kleur1)
        wereld8.act_kleurcode(boris, grkleur2, kleur2)
        wereld8.act_kleurcode(boris, grkleur3, kleur3)
        wereld8.act_kleurcode(boris, grkleur4, kleur4)
        wereld8.code_check(
            [kleur1, kleur2, kleur3, kleur4],
            ["blue", "green", "yellow", "red"],
        )
        wereld8.kleurcode_key(
            [kleur1, kleur2, kleur3, kleur4],
            ["blue", "green", "yellow", "red"],
            boris,
        )

    def wereld_9_run(self):
        doors1.add(door1)
        wereld9.teleport(250, 180, "Brecht")
        wereld9.act("")  # vervangen met cisse's laatste minigame

    def wereld_11_run(self):
        vlots.add(vlot)
        doors4.add(door4)
        wereld11.teleport(230, 70, "vlot")
        wereld11.act("")
        if pygame.sprite.spritecollideany(boris, vlots):
            pygame.time.delay(1000)
            self.level += 1

    def wereld_einde_run(self):
        wereld8.teleportplayer(boris, BREEDTE + 100, HOOGTE + 5)
        wereld_einde.act("")
