# Litmus is a python class that utilizes genetic algorithm to detect user taste #
from Litmus.Vectorizer import LitmusVectorizer
from Litmus.Core import LitmusCore

class Litmus:


    litmus_vectorizer_obj = LitmusVectorizer()
    litmus_core_obj = LitmusCore()
    all_data_vector = []

    def vectorizeData(self):
        self.litmus_vectorizer_obj.createTagSet()
        self.litmus_vectorizer_obj.vectorizeAssociatedData()

    def generateAllVector(self):
        self.litmus_vectorizer_obj.vectorizeAllData()

    def generateUserTaste(self):
        number_of_content = self.litmus_vectorizer_obj.getNumberOfContent()
        vector_size = self.litmus_vectorizer_obj.getVectorSize()
        associated_vector = self.getVectorizedData()
        fitness = self.litmus_vectorizer_obj.getFitness()

        # print(associated_vector)
        self.litmus_core_obj.setNumberOfContent(number_of_content)
        self.litmus_core_obj.setVectorSize(vector_size)
        self.litmus_core_obj.setAssociatedVector(associated_vector)
        self.litmus_core_obj.setFitness(fitness)

        self.litmus_core_obj.initialize()
        self.litmus_core_obj.generateUserTaste()

# generates content with user taste
    def generateUserContent(self):
        all_vector =  self.litmus_vectorizer_obj.getAllDataVector()
        # print(all_vector)
        self.litmus_core_obj.setAllVector(all_vector)
        self.litmus_core_obj.findContentBasedOnTaste()


    def setData(self, data):
        self.litmus_vectorizer_obj.setData(data)

    def setFitness(self, fitness):
        self.litmus_vectorizer_obj.setFitness(fitness)

    def setAllData(self, data):
        self.litmus_vectorizer_obj.setAllData(data)

    def getData(self):
        return self.litmus_vectorizer_obj.getData()

    def getAllData(self):
        return self.litmus_vectorizer_obj.getAllData()

    def getFitness(self):
        return self.litmus_vectorizer_obj.getFitness()

    def getTagSet(self):
        return self.litmus_vectorizer_obj.getTagSet()

    def getVectorizedData(self):
        return self.litmus_vectorizer_obj.getVectorizedData()

    def getAllDataVector(self):
        return self.litmus_vectorizer_obj.getAllDataVector()


    def getUserTaste(self):
        return self.litmus_core_obj.getUserTaste()

    def getAssociatedVector(self):
        return self.litmus_core_obj.getAssociatedVector()

    def devectorizeUserTaste(self):
        return self.litmus_vectorizer_obj.devectorize(self.getUserTaste())
