class Solution(object):
    def checkIfPangram(self, sentence):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            if char not in sentence:
                return False
        return True
        