import matplotlib.pyplot as plt


def print_dict(dict):
    nb = 0
    for value in dict:
        nb = nb + value[1]
        print("Word:", value[0], ", occurrence:", value[1])
    print("Total words: ", nb)


def graph(dict, nb, win_x, win_y, filename):
    print_dict(dict)
    words = []
    number = []
    i = 0
    if nb > len(dict):
        nb = len(dict)
    while i < nb:
        words.append(dict[i][0])
        number.append(dict[i][1])
        i += 1
    plt.figure(figsize=(win_x, win_y))
    plt.plot(words, number)
    graph_name = "Number of word occurrence in " + filename
    plt.title(graph_name)
    plt.ylabel('Occurrences')
    plt.xlabel('Words')
    plt.show()
    plt.close()