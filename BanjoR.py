def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        return str(name) + " plays banjo"
    else:
        return str(name) + " does not play banjo"

print(are_you_playing_banjo("Riki"))

#Solution
# def areYouPlayingBanjo(name):
#     if name[0].lower() == 'r':
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'