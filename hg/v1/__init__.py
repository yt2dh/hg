from otree.api import *
from otree.app_template.models import Constants
import random
import json

doc = """
Horse game
"""

Q1_Choice = [(0, "40"),
                 (1, "80"),
                 (2, "150"),
                 (3, "180")]

Q2_Choice = [(0, "10"),
                 (1, "20"),
                 (2, "30"),
                 (3, "120")]

Q3_Choice = [(0, "10"),
                 (1, "70"),
                 (2, "110"),
                 (3, "140")]

class Constants(BaseConstants):
    name_in_url = 'game1'
#Game setup and assigning groups and roles
    players_per_group = 3
    Player_1_role = 'Square'
    Player_2_role = 'Circle'
    Player_3_role = 'Triangle'
    num_rounds = 60
    PAYOFF_A_1 = 120
    PAYOFF_A_2 = 120
    PAYOFF_A_3 = 30
    PAYOFF_B_1 = 60
    PAYOFF_B_2 = 60
    PAYOFF_B_3 = 150
    PAYOFF_C_1 = 60
    PAYOFF_C_2 = 30
    PAYOFF_C_3 = 180
    PAYOFF_D_1 = 30
    PAYOFF_D_2 = 150
    PAYOFF_D_3 = 90
    PAYOFF_E_1 = 90
    PAYOFF_E_2 = 90
    PAYOFF_E_3 = 90


#random role assignment
#array of possibilities for each permutation
mat_r1 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]*5
mat_r2 = [[4, 5, 6], [4, 6, 5], [5, 4, 6], [5, 6, 4], [6, 5, 4], [6, 4, 5]]*5
mat_r3 = [[7, 8, 9], [7, 9, 8], [8, 7, 9], [8, 9, 7], [9, 8, 7], [9, 7, 8]]*5
mat_r4 = [[10, 11, 12], [10, 12, 11], [11, 12, 10], [11, 10, 12], [12, 11, 10], [12, 10, 11]]*5
mat_r1_2 = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]*5
mat_r2_2 = [[4, 5, 6], [4, 6, 5], [5, 4, 6], [5, 6, 4], [6, 5, 4], [6, 4, 5]]*5
mat_r3_2 = [[7, 8, 9], [7, 9, 8], [8, 7, 9], [8, 9, 7], [9, 8, 7], [9, 7, 8]]*5
mat_r4_2 = [[10, 11, 12], [10, 12, 11], [11, 12, 10], [11, 10, 12], [12, 11, 10], [12, 10, 11]]*5

def creating_session(self):
    for p in self.get_players():
        if 'round_payoffs' not in p.participant.vars:
            p.participant.vars['round_payoffs'] = []

    if self.round_number <= 30:
        player_mat = self.get_group_matrix()
        player_mat[0] = random.choice(mat_r1)
        mat_r1.remove(player_mat[0])
        player_mat[1] = random.choice(mat_r2)
        mat_r2.remove(player_mat[1])
        player_mat[2] = random.choice(mat_r3)
        mat_r3.remove(player_mat[2])
        player_mat[3] = random.choice(mat_r4)
        mat_r4.remove(player_mat[3])
        self.set_group_matrix(player_mat)
        self.group_randomly(fixed_id_in_group=True)
    elif 30 < self.round_number <= 60:
        player_mat = self.get_group_matrix()
        player_mat[0] = random.choice(mat_r1_2)
        mat_r1_2.remove(player_mat[0])
        player_mat[1] = random.choice(mat_r2_2)
        mat_r2_2.remove(player_mat[1])
        player_mat[2] = random.choice(mat_r3_2)
        mat_r3_2.remove(player_mat[2])
        player_mat[3] = random.choice(mat_r4_2)
        mat_r4_2.remove(player_mat[3])
        self.set_group_matrix(player_mat)
        self.group_randomly(fixed_id_in_group=True)
'''    for group in self.get_groups():
        players = group.get_players()
        if len(players) == 12:
            players[0].player_role = Constants.Player_1_role
            players[1].player_role = Constants.Player_2_role
            players[2].player_role = Constants.Player_3_role
            players[3].player_role = Constants.Player_1_role
            players[4].player_role = Constants.Player_2_role
            players[5].player_role = Constants.Player_3_role
            players[6].player_role = Constants.Player_1_role
            players[7].player_role = Constants.Player_2_role
            players[8].player_role = Constants.Player_3_role
            players[9].player_role = Constants.Player_1_role
            players[10].player_role = Constants.Player_2_role
            players[11].player_role = Constants.Player_3_role'''


class Subsession(BaseSubsession):
    pass



#FUNCTIONS
class Group(BaseGroup):
    pass





class Player(BasePlayer):
    #player_role = models.StringField() #added
    terminal = models.StringField(label="Please enter the number assigned to your computer terminal.",
                                     max_length=2)
    Q1 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=Q1_Choice)
    Q2 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=Q2_Choice)
    Q3 = models.IntegerField(widget=widgets.RadioSelectHorizontal, choices=Q3_Choice)
    Q1_answer=models.StringField()
    Q2_answer = models.StringField()
    Q3_answer = models.StringField()
    selected_round = models.StringField(initial="[]")
    final_payoff = models.CurrencyField(initial=0)
    final_final_payoff = models.CurrencyField(initial=0)
    total_payoff = models.CurrencyField(initial=0)

    player_choice = models.BooleanField(
        widget=widgets.RadioSelectHorizontal
    )


    def player_choice_choices(self):
        role = self.id_in_group
        if role == 1:
            return [(False, 'Pass to Triangle'), (True, 'Pass to Circle')]
        elif role == 2:
            return [(False, 'Pass to Triangle'), (True, 'End by Circle')]
        elif role == 3:
            return [(False, 'End Left'), (True, 'End Right')]
        else:
            return [(False, 'Left'), (True, 'Right')]  # fallback in case role not assigned

    click_data = models.LongStringField(blank=True, initial='{}')
    highlighted_links = models.LongStringField(blank=True, initial='[]')
    belief_1 = models.IntegerField(min=0, max=100)
    belief_2 = models.IntegerField(min=0, max=100)

    # def reset_for_new_round(self):
    #     self.player_choice = None
    #     self.highlighted_links = '[]'




def set_payoffs(group: Group):
    player_1, player_2, player_3 = group.get_players()
    if not player_1.player_choice:
        if not player_3.player_choice:
            payoffs = [Constants.PAYOFF_A_1, Constants.PAYOFF_A_2, Constants.PAYOFF_A_3]
        else:
            payoffs = [Constants.PAYOFF_B_1, Constants.PAYOFF_B_2, Constants.PAYOFF_B_3]
    else:
        if not player_2.player_choice:
            if not player_3.player_choice:
                payoffs = [Constants.PAYOFF_C_1, Constants.PAYOFF_C_2, Constants.PAYOFF_C_3]
            else:
                payoffs = [Constants.PAYOFF_D_1, Constants.PAYOFF_D_2, Constants.PAYOFF_D_3]
        else:
            payoffs = [Constants.PAYOFF_E_1, Constants.PAYOFF_E_2, Constants.PAYOFF_E_3]


    players = group.get_players()
    for i, p in enumerate(players):
        p.payoff = payoffs[i]  # Assign as integer
        if 'round_payoffs' not in p.participant.vars:
            p.participant.vars['round_payoffs'] = []
        # Store as plain integer, not Currency
        p.participant.vars['round_payoffs'].append(int(p.payoff))
        print(
            f"Player {p.id_in_group}, Round {p.round_number}: Payoff = {p.payoff}, Round Payoffs = {p.participant.vars['round_payoffs']}")




def set_final_payoffs(group: Group):
    print(f"Setting final payoffs for group {group.id_in_subsession}")
    for p in group.get_players():
        round_payoffs = p.participant.vars.get('round_payoffs', [])
        print(f"Player {p.id_in_group}: Round Payoffs = {round_payoffs}")
        if round_payoffs and len(round_payoffs) >= Constants.num_rounds:
            # Select 10 random rounds
            selected_rounds = random.sample(range(1, Constants.num_rounds + 1), 10)
            selected_rounds.sort()
            # Sum the payoffs from the selected rounds
            p.final_payoff = sum(round_payoffs[round_idx - 1] for round_idx in selected_rounds)
            p.participant.payoff = p.final_payoff  # Store as int
            p.final_final_payoff = p.final_payoff * 0.02
            p.total_payoff = p.final_final_payoff + 10
            p.selected_round = str(selected_rounds)
        else:
            p.selected_round = []
            p.final_payoff = 0
            p.participant.payoff = p.final_payoff
            p.final_final_payoff = p.final_payoff * 0.02
            p.total_payoff = p.final_final_payoff + 10
        print(f"Player {p.id_in_group}: Selected Round = {p.selected_round}, Final Payoff = {p.final_payoff}")

# PAGES
class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1

'''class Survey(Page):
    form_model = 'player'
    form_fields = ['belief_1', 'belief_2']


    def is_displayed(self):
        return False


    def vars_for_template(self):
        return {
            'round_number': self.round_number,
            'player_id': self.player.id_in_group,
            'player_role': self.player.player_role
        }'''


class Intro_Questions(Page):
    form_model = 'player'
    form_fields = ["Q1", "Q2", "Q3"]

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.Q1 == 2:
            player.Q1_answer = "correct"
        else:
            player.Q1_answer = "wrong"

        if player.Q2 == 1:
            player.Q2_answer = "correct"
        else:
            player.Q2_answer = "wrong"

        if player.Q3 == 2:
            player.Q3_answer = "correct"
        else:
            player.Q3_answer = "wrong"

    def is_displayed(self):
        return self.round_number == 1
    pass

class Intro_Answers(Page):
    def is_displayed(self):
        return self.round_number == 1
    pass

class IntroWaitPage(WaitPage):
    wait_for_all_groups = True
    pass

class Decision(Page):
    form_model = 'player'
    form_fields = ['player_choice', 'click_data']
    timeout_seconds = 1000

    def vars_for_template(self):
        return {
            #'player_role': self.role,
            'round_number': self.round_number,
        }

    def get_form(self, **kwargs):
        form = super().get_form(**kwargs)
        form._fields['player_choice'].choices = self.player.player_choice_choices()
        return form

    def before_next_page(self, timeout_happened):
        if self.click_data:
            self.click_data = json.dumps(self.click_data)

class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            set_payoffs(group)
            p1, p2, p3 = group.get_players()


            p1_choice = p1.player_choice
            p2_choice = p2.player_choice
            p3_choice = p3.player_choice


            highlighted = []


            if p1_choice:  # Right
                highlighted.append("L1")
                if p2_choice:
                    highlighted.append("L3")
                else:
                    highlighted.append("L4")
                    if p3_choice:
                        highlighted.append("L8")
                    else:
                        highlighted.append("L7")
            else:  # Left
                highlighted.append("L2")
                if p3_choice:
                    highlighted.append("L6")
                else:
                    highlighted.append("L5")


            for player in group.get_players():
                player.highlighted_links = json.dumps(highlighted)




class Results(Page):

    def vars_for_template(self):
        return {
            'highlighted_links': self.highlighted_links,
            #'player_role': self.player.player_role,
            #'round_payoff': self.payoff,
            'payoff': self.payoff,
            'round_number': self.round_number
        }


    # def is_displayed(self):
    #     return self.round_number <= Constants.num_rounds
    #
    #
    # def before_next_page(self,timeout_happened):
    #     if self.round_number < Constants.num_rounds:
    #         self.participant.vars['current_round'] = self.round_number + 1
    #         self.round_number += 1
    #         for player in self.group.get_players():
    #             player.reset_for_new_round()
    #     else:
    #         self.participant.vars['game_completed'] = True




class FinalWaitPage(WaitPage):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


    after_all_players_arrive = set_final_payoffs




class Finalize(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds


    def vars_for_template(self):
        return {
            'selected_rounds': eval(self.selected_round) if isinstance(self.selected_round, str) else self.selected_round,
            'final_payoff': self.final_payoff,
            'final_final_payoff': self.final_final_payoff,
            'total_payoff': self.total_payoff
        }




page_sequence = [Intro, Intro_Questions, Intro_Answers, Decision, ResultsWaitPage, Results, FinalWaitPage, Finalize]

