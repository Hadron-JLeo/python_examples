""" Currently only calculates from one rank to another """


tiers_dict = {
    # Amount of shards needed to upgrade to the next rank
    'SSS+' : 0, # Highest Rank
    'SSS' : (25 * 20),
    'SS' : (0 * 20),
    'S' : (9 * 20),
    'A' : (3 * 20),
    'B' : (0 * 20),
}


def get_prev_tier(tier):
    """ Get previous tier of input. E.g.: 'A' -> 'B' """
    key_list = list(tiers_dict.keys())
    cur_index = (key_list.index(tier) + 1)
    prev_tier = key_list[cur_index] 
    
    return prev_tier


def calculate_remaining_shards(next_tier, cur_level, shard_inside=0):
    """ Will calculate remaining shards to next rank"""
    # cur_level = 0-19
    # next_tier = a-sss+
    # cur_tier = b-sss
    # shard_inside : int
    per_level = 20
    
    cur_tier = get_prev_tier(next_tier)
    full_shards = tiers_dict.get(cur_tier)
    

    remaining_shards = full_shards - (int(full_shards/20 * cur_level) + shard_inside)
    return remaining_shards

res = calculate_remaining_shards('SS', 5, 3)
print(res)
