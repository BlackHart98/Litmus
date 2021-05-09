# litmus vectorizer takes in list of words and generate vectors

class LitmusVectorizer:
    tagSet = set()
    data = []
    all_data = []
    all_data_vector = []

    associated_data_vector = []
    fitness = []


    def createTagSet(self):
        # collapse data into a linear array
        collapsed_data = []
        for item in self.data[0]:
            collapsed_data.append(item)

        for i in range(1,len(self.data)):
            for item in self.data[i]:
                collapsed_data.append(item)

        for i in range(len(collapsed_data)):
            self.tagSet.add(collapsed_data[i])

    def vectorizeAssociatedData(self):
        # vectorize tags for associated tag set
        for i in range(len(self.data)):
            temp = []
            for tag in self.tagSet:
                if tag in self.data[i]:
                    temp.append(1)
                else:
                    temp.append(0)
            self.associated_data_vector.append(temp)


    def vectorizeAllData(self):
        # vectorize tags  for all tag set
        for i in range(len(self.all_data)):
            temp = []
            for tag in self.tagSet:
                if tag in self.all_data[i]:
                    temp.append(1)
                else:
                    temp.append(0)
            self.all_data_vector.append((i,temp))


    def setFitness(self, fitness):
        self.fitness = fitness

    def setData(self, data):
        self.data = data

    def setAllData(self, data):
        self.all_data = data


    def getData(self):
        return self.data

    def getAllData(self):
        return self.all_data

    def getFitness(self):
        return self.fitness

    def getTagSet(self):
        return self.tagSet

    def getVectorizedData(self):
        return self.associated_data_vector

    def getAllDataVector(self):
        return self.all_data_vector

    def getVectorSize(self):
        return len(self.tagSet)

    def devectorize(self, vector):
        tag_dict = {}
        i = 0
        for  item in self.tagSet:
            tag_dict[item] = vector[i]
            i += 1
        return tag_dict

    def getNumberOfContent(self):
        return len(self.data)
