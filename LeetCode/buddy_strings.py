class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False

        ht = {}

        for i in range(len(A)):
            if A[i] != B[i]:
                ht[i] = A[i]

        # ht is a dictionary which contain the index and different characters between A and B

        if len(ht) == 2:
            i,j=ht.keys()

            # i and j will be the indices of two inputs
            # see this, by running the code with the inputs "aaaaaaabc" and "aaaaaaacb"

            # split the sentence into characters
            A = list(A)

            # swap the different characters
            A[i],A[j]=A[j],A[i]

            # if we have swapped the characters of A, we check if it is similar to B
            # if yes, we return True, otherwise return False
            return "".join(A) == B

        # if there is no difference between A and B
        # AND sentence A and B are exactly the same
        # AND length of sentence A bigger than length of unique words of A
        # return True
        # see this, by running the code with the inputs "abab" and "abab"
        elif len(ht) == 0 and A == B and len(A) > len(set(A)):
            return True

        else:
            return False
