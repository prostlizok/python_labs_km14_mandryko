card_s = ("diamonds", "clubs", "hearts", "spades")
nums = ("A", "2","3","4","5","6", "7", "8", "9","10", "J", "Q","K")

def gen(card_s, nums):
    for i in card_s:
        for j in range(len(nums)):
            yield nums[j], i

deck = gen(card_s, nums)

for i in range(1, 53):
    a = next(deck)
    print(a[0], a[1])
