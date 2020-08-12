"""
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.

"""

"""
citation => 인용
"h - index"는 결구 연구자의  논문 N개의 논문이 적어도 h개의 인용이 있는 경우 그리고
나머지 N-h개의 놈눈들이 h보다 적은 인용을 가지고 있을때의 숫자다. 
"""
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        self.citations = citations
        self.citations.sort()
        