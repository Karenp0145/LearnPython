# Exercice 12 : Anagrammes
# Écris une fonction qui groupe les mots qui sont des anagrammes les uns des autres.
# Ex : ["chien", "niche", "chat", "tach"] → [["chien", "niche"], ["chat", "tach"]]

# words = ["chien", "niche", "chat", "tach"]

# groups = {}

# for word in words:
#     sorted_word = ''.join(sorted(word))

#     if sorted_word in groups :
#         groups[sorted_word].append(word)
#     else :
#         groups[sorted_word] = [word]
        
# print(list(groups.values()))


""" Input : str(word)
Output : str(sorted_word) """
def sorted_word(word): 

    sorted_word = ''.join(sorted(word))
    return sorted_word
    
""" Input : str(words)
Output : str(groups) """

def group_anagrams(words):

    groups = {}

    for word in words:
        key = sorted_word(word)
    
        if key in groups:
             groups[key].append(word)
        else :
            groups[key] = [word]
    return groups

""" Input : str(groups)
Output : str(list(groups.values())) """

def get_groups(groups):
    return list(groups.values())


def main():
    words = ["chien", "niche", "chat", "tach"]

    groups_dict = group_anagrams(words)

    groups = get_groups(groups_dict)

    print(groups)

main()