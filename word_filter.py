# Will filter certain words to isolate the title

filter_array = [
            # Words that should be filtered out
            ] 

example_title = "proto void max_intuples 1238asda "

def filter(title:str, to_filter:list)->str:
    """ Get a list of words to remove out of a string array,
    returns the isolated word """

    temp_word = title
    cur_replacer = ""

    for word in to_filter:
        try:
            temp_word = temp_word.replace(word, "")
        except:
            # Word doesn't fit
            pass

    x = [s for s in temp_word.split(" ") if (not s.isspace()) and (not s == "")]
    temp_word = x[0]
    #temp_word = temp_word.replace(" ", "") # Remove initial whitespace
    return temp_word


def main():
    print(filter(example_title, filter_array))

main()
