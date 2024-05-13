import warnings
warnings.filterwarnings('ignore')

accounts = [[1, 5], [7, 5], [3, 5]]

def maximumWealth(accounts):
    max = 0
    for i in range(0, len(accounts)):
        if sum(accounts[i]) > max:
            max = sum(accounts[i])
    return max


count = maximumWealth(accounts)
print('maximum Wealth: ' + str(count))