class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        d = defaultdict(list)
        for triplet in triplets:
            if triplet[0] == target[0]:
                d[(triplet[0], 0)].append([(1, triplet[1]), (2, triplet[2])])
            if triplet[1] == target[1]:
                d[(triplet[1], 1)].append([(0, triplet[0]), (2, triplet[2])])
            if triplet[2] == target[2]:
                d[(triplet[2], 2)].append([(0, triplet[0]), (1, triplet[1])])
        # print(d)
        if len(d) < 3:
            return False
        
        for key, val in d.items():
            allInvalid = True
            for pairs in val:
                if pairs[0][1] <= target[pairs[0][0]] and pairs[1][1] <= target[pairs[1][0]]:
                    allInvalid = False
                    break
            if allInvalid:
                return False
        return True