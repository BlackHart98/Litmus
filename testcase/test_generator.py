from random import *

if __name__ == "__main__":

    keywords = ["academics", "sport", "tech", "fashion", "travels", "politics", "music"]
    file_handle = open("dummy-list-of-tags.txt", "w+")
    content_size = randint(5, 10)
    file_handle.write(str(content_size) + "\n")
    for i in range(content_size):
        number_of_tags = randint(1, len(keywords))

        temp = set()
        for j in range(number_of_tags):
            tag = choice(keywords)
            temp.add(tag)

        file_handle.write(str(i) + " " + str(len(temp)) + " ")
        for tag in temp:
            file_handle.write(tag + " ")
        rand = uniform(0, 1)
        file_handle.write("\n" +  str(rand) + "\n")
    file_handle.close()

    file_handle = open("dummy-list-of-tags-all.txt", "w+")
    all_content_size = randint(10, 50)
    file_handle.write(str(all_content_size)+"\n")
    for i in range(all_content_size):
        number_of_tags = randint(1, len(keywords))
        temp = set()
        for j in range(number_of_tags):
            tag = choice(keywords)
            temp.add(tag)
        file_handle.write(str(i) + " " +str(len(temp)) + " ")

        for tag in temp:
            file_handle.write(tag + " ")
        file_handle.write("\n")
    file_handle.close()
