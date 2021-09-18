import Litmus as lt

# test the litmus class
if __name__ == "__main__":
    file_handle = open("testcase/dummy-list-of-tags.txt","r")

    temp_data = (file_handle.read()).split("\n")
    # print(temp_data)
# Make post data into a dictionary
    data_size = int(temp_data[0])
    i = 1
    current_data = []
    interest_score_list = []
    nn = (data_size * 2)+1
    while i < nn:
        temp = temp_data[i].split()
        index = temp[0]
        current_data.append((index, temp[2:]))
        interest_score_list.append((index,float(temp_data[i+1])))
        i+=2


    file_handle = open("testcase/dummy-list-of-tags-all.txt","r")

    temp_data = (file_handle.read()).split("\n")


# Make post data into a dictionary
    data_size = int(temp_data[0]) + 1
    i = 1
    data_pool = []
    while i < data_size:
        temp = temp_data[i].split()
        index = temp[0]
        data_pool.append((index,temp[2:]))
        i+=1


    # print(f" The data pool structure:\n {data_pool}")
    # print(f"The current data structure:\n {current_data}")
    # print(f"The interest score list: {interest_score_list}")
    litmus_obj = lt.Litmus()

    new_content = litmus_obj.recommendContent(
    current_data, data_pool, interest_score_list,5, .00)

    # the summary prints out the list of recommendation in a table format
    litmus_obj.summary()

    # this is the output(result) of the recommendation system
    # print(new_content)
