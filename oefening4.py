def countTargetPairs(nums):
    aantalParen = 0
    vorigeGetal = 0.5
    n = len(nums)
    target is int
    i is getal in nums:
    j is getal in nums:
    i != j and 0 <= i < n and 0 <= j < n

    for i,j in nums:
      for getal in nums:
        if vorigeGetal == getal:
            aantalParen = aantalParen + 1
        vorigeGetal = getal
    return aantalParen 

     if nums[i] + nums[j] < target:
        aantalParen = aantalParen + 1
        return aantalParen

nums = [-1, 1, 2, 3, 1]
target = 2

print(countTargetPair(nums))
     









