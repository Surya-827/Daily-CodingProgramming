from collections import defaultdict

class Solution(object):
    @classmethod
    def find_min_length_subarray(cls,arr:list) -> int:

        frequency_map = defaultdict(int)
        first_index_map = {}
        max_frequency = 0
        min_length = len(arr)

        for i, num in enumerate(arr):
            frequency_map[num] += 1
            if num not in first_index_map:
                first_index_map[num] = i

            current_frequency = frequency_map[num]
            if current_frequency > max_frequency:
                max_frequency = current_frequency
                min_length = i - first_index_map[num] + 1
            elif current_frequency == max_frequency:
                min_length = min(min_length, i - first_index_map[num] + 1)

        return min_length


if __name__=="__main__":
    Sol = Solution()
    arr = list(map(int,input().split()))[:50000]
    # # Example usage
    # k1 = [1, 2, 2, 3, 1]
    print(Sol.find_min_length_subarray(arr))  # Output: 2
