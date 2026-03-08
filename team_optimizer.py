from pulp import LpProblem, LpMaximize, LpVariable, lpSum, value

def get_optimal_team(players):
    prob = LpProblem("FantasyTeam", LpMaximize)
    player_vars = {p['id']: LpVariable(f"p_{p['id']}", cat='Binary') for p in players}
    
    # Objective: Maximize points
    prob += lpSum([p['points'] * player_vars[p['id']] for p in players])
    
    # Constraints
    prob += lpSum([player_vars[p['id']] for p in players]) == 11
    prob += lpSum([p['credits'] * player_vars[p['id']] for p in players]) <= 100
    
    # Basic Role Constraints
    prob += lpSum([player_vars[p['id']] for p in players if p['role'] == 'WK']) >= 1
    prob += lpSum([player_vars[p['id']] for p in players if p['role'] == 'BAT']) >= 3
    prob.solve()
    
    return [p_id for p_id, var in player_vars.items() if value(var) == 1]
