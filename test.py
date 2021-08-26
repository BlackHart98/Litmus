import Litmus as lt


# def performanceMeasure(current_data,data_pool,interest_score_list,mutation_rate):
#     average = .0
#     litmus_obj = lt.Litmus()
#     content_list = []
#     for i in range(100):
#         content_list.append(litmus_obj.recommendContent(
#         current_data,data_pool,interest_score_list,mutation_rate
#         ))
#     dict_counter = {}
#     for i in range(100):
#         for j in range(len(content_list[i])):
#             if content_list[i][j] not in dict_counter:
#                 dict_counter[content_list[i][j]] = 1
#             else:
#                 dict_counter[content_list[i][j]] +=1
#     return dict_counter


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



    litmus_obj = lt.Litmus()

    new_content = litmus_obj.recommendContent(
    current_data, data_pool, interest_score_list, .005)

    print("new id list of recommended content : {}\n".format(new_content))
    print("previous content : {}\n".format(current_data))
    print("interest score of each content: {}\n"
    .format(interest_score_list))

    new_current_data = []

    data_pool_dict = {}
    for element in data_pool:
        data_pool_dict[element[0]] = element[1]

    for index in new_content:
        new_current_data.append((index, data_pool_dict[index]))

    print("data pool : {}\n".format(data_pool))
    print("current content : {}\n".format(new_current_data))
    print("the preprocessed data : {}"
    .format(litmus_obj.getPreprocessedData()["tag set"]))


    # litmus_obj.getIndices()
    # frequency = performanceMeasure(current_data,data_pool,
    # interest_score_list,.0)
    #
    # print("frequency : {}".format(frequency))
