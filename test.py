"""Given an array of strings strs, group the anagrams together.
You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters
of a different word or phrase, typically using all the original
letters exactly once."""


def is_anagram(first: str, second: str) -> bool:
    """returns if two strings are anagram"""
    if len(first) != len(second):
        return False
    tracker_f, tracker_s = {}, {}
    for i in range(len(first)):
        tracker_f[first[i]] = 1 + tracker_f.get(first[i], 0)
        tracker_s[second[i]] = 1 + tracker_s.get(second[i], 0)
    return tracker_f == tracker_s


def group_anagrams(strs: list[str]) -> list[list[str]]:
    """Given an array of strings strs, group the anagrams together."""
    out = []
    i = 0
    while i < len(strs):
        inner = [strs[i]]
        j = i + 1
        while j < len(strs):
            if is_anagram(strs[i], strs[j]):
                inner.append(strs[j])
                strs.pop(j)
                continue
            j += 1
        out.append(inner)
        strs.pop(i)
    return out


test1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
test2 = ["", "b", ""]
test3 = ["", "", ""]
test4 = ["eat", "tea", "ate"]



def main():
    """main function"""
    import large_testcase.
    
    print(group_anagrams(test4))


if __name__ == "__main__":
    main()
