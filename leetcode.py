from collections import Counter

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# def strStr(haystack, needle):
#     # find which word is longer
#     if len(needle) > len(haystack):
#         return -1
#     firstIndex = None
#     matches = ""
#     needleIndex = 0
#     # loop through and push each index if letters match
#     for i in range(len(haystack)):
#         if haystack[i] == needle[needleIndex]:
#             if firstIndex == None:
#                 # finds the first index
#                 firstIndex = i
#             # appends to matches
#             matches += haystack[i]
#             if needleIndex < len(needle):
#                 needleIndex += 1
#             else:
#                 break
#             # checks to see if they match
#             if matches == needle:
#                 return firstIndex
#         else:
#             firstIndex=None
#             matches = ""
#     return -1
# print(strStr("hello", "ll"))

# def strStr(haystack, needle):
#     firstIndex = None
#     matches = ""
#     for i in range(len(haystack)):
#         for j in range(len(needle)):
#             if firstIndex == None:
#                 firstIndex = i
#             if haystack[i] == needle[j]:
#                 matches += haystack[i]
#             if matches == needle:
#                 return firstIndex
#     return -1

# print(strStr("hello", "ll"))

# def removeElement(nums, val):
#     count = 0
    
#     for i in range(len(nums)):
#         if nums[i] == val:
#             count += 1
#             nums[i] = False
#     return f"{count}, nums = {nums}"
# print(removeElement([3,2,2,3], 3))


# def maxArea(height):
#     left = 0
#     right = len(height)-1
#     area = 0
#     while left < right:
#         if height[left] > height[right]:    
#             if area < abs(height[right] * (left - right)):
#                 area = abs(height[right] * (left - right))
#             right -= 1
#         else:
#             if area < abs(height[left] * (right - left)):
#                 area = abs(height[left] * (right - left))
#             left += 1
#     return area

# print(maxArea([1,8,6,2,5,4,8,3,7]))

# def fib(n):
#     count = 1
#     sequence = [0,1]
#     for i in range(n):
#         equation = sequence[i] + sequence[count]
#         sequence.append(equation)
#         count +=1
#     return sequence[n-1] + sequence[n-2]

# print(fib(5))

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
#         dummy = ListNode()
#         current = dummy
#         while list1 and list2:
#             if list1 < list2:
#                 current.next = list1
#                 list1 = list1.next 
#             else:
#                 current.val = list2
#                 list2 = list2.next
#             current = current.next
#         while list1 or list2:
#             if list1:
#                 current.next = list1
#                 list1 = list1.next
#             if list2:
#                 current.next = list2
#                 list2 = list2.next
#             current = current.next
#         return dummy.next

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def deleteDuplicates(self, head):
#         current = head
#         while current and current.next:
#             if current.val == current.next.val:
#                 current = current.next.next
#             else:
#                 current = current.next
#         return head



# list1 = ListNode(1)
# list1.next = ListNode(2)
# list1.next.next = ListNode(3)
# S1 = Solution().deleteDuplicates(list1)

# def isPalindrome(x):
#     newStr = str(x)
#     rev = newStr[::-1]
#     if newStr == rev:
#         return True
#     else:
#         return False


# print(isPalindrome(121))

# def leftRigthDifference(nums):
#     if len(nums) <= 1:
#         return 0
#     previous = 0
#     ans = []
#     leftSum = []
#     rightSum = []
#     for i in range(len(nums)-1):
#         if i == 0:
#             leftSum.append(0)
#             leftSum.append(nums[0])
#         else:
#             newSum = leftSum[i] + nums[i]
#             leftSum.append(newSum)
#     rightSum.append(0)
#     for i in range(len(nums)-1,0,-1):
#         newSum = nums[i] + previous
#         previous = newSum
#         rightSum.append(newSum)
#     rev = rightSum.reverse()
#     print(rev)
#     for i in range(len(nums)):
#         res = abs(rightSum[i]-leftSum[i])
#         ans.append(res)
#     return ans


# print(leftRigthDifference([1]))

# def leftRigthDifference(nums):
#         ans = []
#         leftSum = []
#         rightSum = []
#         for i in range(len(nums)):
#             leftSum.append(sum(nums[:i]))
#             rightSum.append(sum(nums[i+1:]))
#             ans.append(abs(sum(nums[:i]) - sum(nums[i+1:])))
#         return ans
# print(leftRigthDifference([1,2,3,4,5]))

# def plusOne(digits):
#     num = ""
#     arr = []
#     for i in digits:
#         num += str(i)
#     res = int(num) + 1
#     num = str(res)
#     for char in num:
#         arr.append(int(char))
#     return arr

# print(plusOne([1,2,3]))

# ****** sliding windows *******
# def findMaxAverage(nums, k):
#     subArray = sum(nums[0:k])
#     maxAvg = subArray

#     for i in range(1,len(nums)-k):
#         subArray = subArray + nums[i + k] - nums[i]
#         maxAvg = max(subArray, maxAvg)
#     return maxAvg/k
    

# print(findMaxAverage([1,12,-5,-6,50,3],4))

# def groupThePeople(groupSizes):
#     newArray = []
#     sizes = set(groupSizes)
#     sizeCount = {}
#     for i, value in enumerate(sizes):
#         sizeCount[value] = groupSizes.count(value)
#     for key in sizeCount:
#         print(key)

# print(groupThePeople([3,3,3,3,3,1,3]))

# def restoreString(s, indices):
#     newDict = {}
#     newStr = ""
#     for i in range(len(indices)):
#         newDict[indices[i]] = s[i]
#     for i in range(len(s)):
#         newStr += newDict[i]
#     return newStr

# print(restoreString("codeleet",[4,5,6,7,0,2,1,3]))

# def findMatrix(nums):
#     counter = Counter(nums)
#     most_common = counter.most_common(1)
#     frequency = most_common[0][1]
#     doubles = set(nums)
#     ans = []
#     for i in range(frequency):
#         ans.append([])
#     for num in doubles:
#         count = nums.count(num)
#         for i in range(count):
#             ans[i].append(num)
#     return ans

# print(findMatrix([1,3,4,1,2,3,1]))

# def sumOfMultiples(n):
#     ans = 0
#     for i in range(1, n + 1):
#         if i%3 == 0 or i%5 == 0 or i%7 ==0:
#             ans += i
#     return ans

# print(sumOfMultiples(10))

# def decompressRLElist(nums):
#     ans = []
#     state = False
#     pair = 0
#     for i in range(len(nums)):
#         if not state:
#             pair += nums[i]
#             state = True
#         else:
#             for j in range(pair):
#                 ans.append(nums[i])
#             state = False
#             pair = 0
#     return ans

# print(decompressRLElist([1,2,3,4]))

##### XOR Algos #####
# 
#  def findArray(pref):
#     ans = [pref[0]]
#     for i in range(1,len(pref)):
#         newNum = pref[i-1] ^ pref[i]
#         ans.append(newNum)
#     return ans

# print(findArray([5,2,0,3,1]))

# def decode(encoded, first):
#     ans = [first]
#     for i in range(len(encoded)):
#         num = encoded[i]^ans[i]
#         ans.append(num)
#     return ans

# print(decode([1,2,3],1))

# def groupThePeople(groupSizes):
#     ans = []
#     # dictionary = {}
#     groupSet = set(groupSizes)
#     previous = 0
#     # for num in groupSet:
#     #     dictionary[num] = groupSizes.count(num)
#     #     arrCount += groupSizes.count(num)
#     # print(dictionary)
#     for num in groupSet:
#         subGroup =[]
#         for j in range(len(groupSizes)):
#             if groupSizes[j] == num and len(subGroup) < num:
#                 subGroup.append(j)
#             if groupSizes[j] == num and len(subGroup) == num:
#                 ans.append(subGroup)
#                 subGroup = []
#     return ans

# print(groupThePeople([3,3,3,3,3,1,3]))

# def maxWidthOfVerticalArea(points):
#     newArr = []
#     ans = 0
#     for point in points:
#         newArr.append(point[0])
#     newArr.sort()
#     for i in range(len(newArr)-1,0,-1):
#         if newArr[i] - newArr[i-1] > ans:
#             ans = newArr[i] - newArr[i-1]
#     return ans

# print(maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))

# def pivotArray(nums, pivot):
#     ans= []
#     front = []
#     middle = []
#     back = []
#     for i in range(len(nums)):
#         if nums[i] < pivot:
#             front.append(i)
#         if nums[i] > pivot:
#             back.append(i)
#         if nums[i] == pivot:
#             middle.append(i)
#     front.extend(middle)
#     front.extend(back)
#     print(front)
#     for index in front:
#         ans.append(nums[index])
#     return ans

# print(pivotArray([-3,4,3,2], 2))

# def countDigits(num):
#     count = 0
#     temp = num
#     while temp > 0:
#         remainder = temp % 10
#         if num % remainder == 0:
#             count +=1
#         temp = temp // 10
#     return count

# print(countDigits(121))

# def sortSentence(s):
#     s = s.replace(" ", "")
#     ans = ""
#     word = ""
#     num = 0
#     orderDict = {}
#     for char in s:
#         if char.isdigit() == True:
#             orderDict[int(char)] = word
#             word = ""
#         else:
#             word += char
#     sorted(orderDict)
#     for i in range(1,len(orderDict)+1):
#         if i == len(orderDict):
#             ans += orderDict[i]
#         else:
#             ans += orderDict[i] + " "
#     return ans

# print(sortSentence("is2 sentence4 This1 a3"))

# def findCenter(edges):
#     edgesList = []
#     for i in range(len(edges)):
#         edgesList.append(edges[i][0])
#         edgesList.append(edges[i][1])
#     for i in range(len(edgesList)):
#         if edgesList.count(edgesList[i]) == len(edges):
#             return edgesList[i]
#     return None
# print(findCenter([[1,2],[2,3],[4,2]]))

# def arrayStringsAreEqual(word1, word2):
#     word1 = ''.join(word1)
#     word2 = ''.join(word2)
#     if word1 == word2:
#         return True
#     else:
#         return False

# print(arrayStringsAreEqual(["abc", "d", "defg"],["abcddefg"]))

# def checkIfPangram(sentence):
#         if len(sentence) < 26:
#             return False
#         alpha = []
#         for i in range(len(sentence)):
#             if sentence[i] not in alpha:
#                 alpha.append(sentence[i])
#         if len(alpha) == 26:
#             return True
#         else:
#             return False

# print(checkIfPangram("abacasfkjaskjfsaldfj"))

# def sumOddLengthSubarrays(arr):
#     count = 0
#     length = 1
#     while len(arr) >= length:
#         for i in range(len(arr)):
#             if len(arr[i:i+length]) == length:
#                 print(arr[i:i+length])
#                 count += sum(arr[i:i+length])
#         length += 2
#     return count

# print(sumOddLengthSubarrays([1,4,2,5,3]))

# def truncateSentence(s,k):
#     newS = ""
#     wordCount = 0
#     for i in range(len(s)):
#         if s[i] != ' ':
#             newS += s[i]
#         else:
#             newS += s[i]
#             wordCount +=1
#             if wordCount == k:
#                 break
#     return newS.strip()

# print(truncateSentence("Hello how are you Contestant",4))

# def numberOfMatches(n):
#     matches = 0
#     while n != 1:
#         if n%2 == 0:
#             n = n/2
#             matches += n
#         else:
#             n = ((n-1)/2) + 1
#             matches += n -1
#     return int(matches)

# print(numberOfMatches(7))

def executeInstructions(n, startPos, s):
    vertical = startPos[0]
    horizontal = startPos[1]
    count = 0
    res = []
    while len(s) > 0:
        for i in range(len(s)):
            if s[i] == "R":
                horizontal += 1
            if s[i] == "L":
                horizontal -= 1
            if s[i] == "U":
                vertical -= 1
            if s[i] == "D":
                vertical += 1
            if  horizontal > n-1 or 0 > horizontal:
                res.append(count)
                count=0
                break
            if  vertical > n-1 or 0 > vertical:
                res.append(count)
                count=0
                break
            else:
                count += 1
        s = s[1:]
        vertical = startPos[0]
        horizontal = startPos[1]
        if count > 0:
            res.append(count)
        count = 0
    return res

print(executeInstructions(3, [0,1], "RRDDLU"))

def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans = 0
        for i in range(len(words)):
            status = True
            for j in range(len(words[i])):
                if words[i][j] not in allowed:
                    status = False
                    break
            if status:
                ans += 1
        return ans

def mergeAlternately(self, word1: str, word2: str) -> str:
        newWord = ""
        toggle = True
        if len(word1) <= len(word2):
            shorter = len(word1)
            longer = word2
            amount = len(word2) - len(word1)
        else:
            shorter = len(word2)
            longer = word1
            amount = len(word1) - len(word2)
        for i in range(shorter):
            if toggle:
                newWord += word1[i]
                newWord += word2[i]
                toggle = False
            else:
                newWord += word2[i]
                newWord += word1[i]
                toggle = True
        newWord += longer[:shorter]
        return newWord

def reverseVowels(self, s: str) -> str:
        vowels = ""
        ans = ""
        count = 0
        for i in range(len(s)):
            if s[i].lower() in {'a', 'e', 'i', 'o', 'u'}:
                vowels += s[i]
        revVowelsList = list(vowels[::-1])
        sList = list(s)
        print(sList)
        for i in range(len(sList)):
            if s[i].lower() in {'a', 'e', 'i', 'o', 'u'}:
                sList[i] = revVowelsList[count]
                count += 1
        for i in range(len(sList)):
            ans += sList[i]
        return ans

def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = []
        for i in range(len(nums)):
            if nums[i] == 0:
                nums.remove(nums[i])
                nums.append(0)
        print(zeroes)

def isSubsequence(self, s: str, t: str) -> bool:
        target = 0
        if s == "":
            return True
        for i in range(len(t)):
            if s[target] == t[i]:
                target += 1
                if target == len(s):
                    return True
        return False

def largestAltitude(self, gain: List[int]) -> int:
        altitudes = [0]
        curr = 0
        for i in range(len(gain)):
            curr += gain[i]
            altitudes.append(curr)
        return max(altitudes)

def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        for i in range(len(nums) - 1, -1, -1):
            if sum(nums[0:left]) == sum(nums[left+1:len(nums)]):
                return left
            if left+1 > len(nums):
                return -1
            left +=1
        return -1

def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        setNums1 = list(set(nums1))
        setNums2 = list(set(nums2))
        setNums1.sort()
        setNums2.sort()
        ans = []
        left = 0
        right = 0
        while left < len(setNums1) and right < len(setNums2):
            if setNums1[left] < setNums2[right]:
                left+=1
            elif setNums2[right] < setNums1[left]:
                right +=1
            else:
                setNums1.remove(setNums1[left])
                setNums2.remove(setNums2[right])
        ans.append(setNums1)
        ans.append(setNums2)
        return ans

def uniqueOccurrences(self, arr: List[int]) -> bool:
        setArr = list(set(arr))
        previous = []
        for i in range(len(setArr)):
            if arr.count(setArr[i]) in previous:
                return False
            previous.append(arr.count(setArr[i]))
        return True

def reverseWords(self, s: str) -> str:
        s = s.strip()
        ans = ""
        word = ""
        previous = ""
        for i in range(len(s)-1,-1,-1):
            if previous == " " and s[i] == " ":
                continue
            if s[i] != " ":
                word += s[i]
            else:
                ans += word[::-1] + " "
                word = ""
            previous = s[i]
        if len(word) > 0:
            ans += word[::-1]
            word = ""
        return ans

def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ans = 0
        for i in range(len(hours)):
            if hours[i] >= target:
                ans +=1
        return ans

def differenceOfSums(self, n: int, m: int) -> int:
        num1 = 0
        num2 = 0
        for i in range(n+1):
            if i % m != 0:
                num1 += i
                print(num1)
            if i % m == 0:
                num2 += i
                print(num2)
        print(num1)
        print(num2)
        return num1 - num2
        
def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        for i in range(len(words)):
            for j in range(len(words[i])):
                if words[i][j] == x:
                    ans.append(i)
                    break
        return ans








