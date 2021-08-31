import yaml

with open("chess_figure_config.yml", "r") as ymlfile:
    pos = yaml.load(ymlfile, Loader=yaml.FullLoader)


for piece in pos.keys():
    print(f"piece: {piece}")
    for positions in pos[piece]['init_pos']:
        print(f"position: {positions}")
