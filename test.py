# import Litmus as lt
# # test the litmus class
# if __name__ == "__main__":
#     litmus_obj = lt.Litmus()
#     file_handle = open("testcase/dummy-list-of-tags.txt", "r")
#     number_of_content = int(file_handle.readline())
#     # print(number_of_content)
#     fitness_data = []
#     content = []
#     for i in range(number_of_content):
#         data = file_handle.readline()
#         number_of_tags = int(data[0])
#         splited_data = data[1:].split()
#         tagSet = set()
#         for i in range(len(splited_data)):
#             tagSet.add(splited_data[i])
#         content.append(tagSet)
#
#         fitness_data.append(float(file_handle.readline()))
#
#
#     file_handle.close()
#
#     litmus_obj.setData(content)
#     litmus_obj.setFitness(fitness_data)
#
#     file_handle = open("testcase/dummy-list-of-tags-all.txt", "r")
#     number_of_content =int(file_handle.readline())
#     content = []
#     for i in range(number_of_content):
#         data = file_handle.readline()
#         number_of_tags = int(data[0])
#         splited_data = data[1:].split()
#         tagSet = set()
#         for i in range(len(splited_data)):
#             tagSet.add(splited_data[i])
#         content.append(tagSet)
#
#     file_handle.close()
#
#     litmus_obj.setAllData(content)
#     litmus_obj.vectorizeData()
#
#     litmus_obj.generateUserTaste()
#     litmus_obj.generateAllVector()
#     print(litmus_obj.getTagSet())
#     litmus_obj.generateUserContent()
#     print(litmus_obj.getAssociatedVector())
