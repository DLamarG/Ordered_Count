def ordered_count(inp):
    all_chars = list(inp)
    singles = []
    char_count = []
    for chars in all_chars:
        if chars not in singles:
            singles.append(chars)
    for lett in singles:
        if lett in all_chars:
            char_count.append((lett, all_chars.count(lett)))
    return char_count


print(ordered_count('Code Wars'))
print(ordered_count('abracadabra'))