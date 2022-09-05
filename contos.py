import math

def challenge_compute():
    words_count, line_count, max_line_words = (int(x) for x in input().split())
    phrase = input()

    lines = [[]]
    for word in phrase.split():
        last_index = len(lines) - 1
        length_last_line = len(' '.join(lines[last_index]  + [word]))

        if length_last_line > max_line_words:
            lines.append([word])
        else:
            lines[last_index].append(word)

    print(math.ceil(len(lines) / line_count))

if __name__ == '__main__':
    while True:
        try:
            challenge_compute()
        except EOFError:
            break
