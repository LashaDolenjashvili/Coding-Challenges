"""
CHALLENGE DESCRIPTION 
(LeetCode: https://leetcode.com/problems/richest-customer-wealth/description/)
- - - - - - - - - - - -
Given a 2D grid (accounts) of size m x n, where each cell 
represents the money a specific customer has in a particular 
bank, find out which customer has the maximum combined wealth.
"""

# Beginner-Friendly Solution
def maximumWealth(self, accounts: List[List[int]]) -> int:
    # Placeholder for maximum wealth
    maxWealth = 0
    
    # For each customer:
    for wealth in accounts:
      	# Calculate total wealth
        totalWealth = sum(wealth)
        # Updated `maxWealth` variable
        maxWealth = max(maxWealth, totalWealth)

    return maxWealth

# One-liner
def maximumWealth(self, accounts: List[List[int]]) -> int:
    return max(sum(customer_wealth) for customer_wealth in accounts)

accounts = [
    [1, 2, 3], # Customer 1 - `totalWealth` = 1 + 2 + 3 = 6
    [3, 3, 2]  # Customer 2 - `totalWealth` = 3 + 3 + 2 = 8
]
maximumWealth(accounts=accounts) # Result would be: 8
