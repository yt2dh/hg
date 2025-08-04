from otree.api import *
from otree.app_template.models import Constants

# PAGES
'''class Intro(Page):
    def is_displayed(self):
        return self.round_number == 1'''

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

'''class GameTree(Page):
    form_model = 'player'
    form_fields = ['player_choice']
    def vars_for_template(self):
        return {
            'player_role': self.player.player_role,
            'round_number': self.round_number,
        }

    def before_next_page(self):
        if self.player.click_data:
            self.player.click_data = json.dumps(self.player.click_data)
'''

'''class ResultsWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs
    wait_for_all_groups = True
    def after_all_players_arrive(self):
        for group in self.subsession.get_groups():
            set_payoff(group)
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
            'round_payoff': self.payoff,
            'round_number': self.round_number
        }
    def vars_for_template(self):
        return {
            'highlighted_links': self.player.highlighted_links,
            'player_role': self.player.player_role,
            'payoff': self.player.payoff,
            'round_number': self.round_number
        }


    def is_displayed(self):
        return self.round_number <= Constants.num_rounds


    def before_next_page(self):
        if self.round_number < Constants.num_rounds:
            self.participant.vars['current_round'] = self.round_number + 1
            self.round_number += 1
            for player in self.group.get_players():
                player.reset_for_new_round()
        else:
            self.participant.vars['game_completed'] = True




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
            'final_payoff': self.final_payoff
        }




page_sequence = [Intro, GameTree, ResultsWaitPage, Results, FinalWaitPage, Finalize]


'''