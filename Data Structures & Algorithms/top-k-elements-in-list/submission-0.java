public class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // Step 1: Count the frequency of each element
        Map<Integer, Integer> frequencyMap = new HashMap<>();
        for (int num : nums) {
            frequencyMap.put(num, frequencyMap.getOrDefault(num, 0) + 1);
        }

        // Step 2: Store elements in a list of arrays [element, frequency]
        List<int[]> frequencyList = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : frequencyMap.entrySet()) {
            frequencyList.add(new int[]{entry.getKey(), entry.getValue()});
        }

        // Step 3: Sort the list by frequency in descending order
        Collections.sort(frequencyList, (a, b) -> b[1] - a[1]);

        // Step 4: Get the top k elements from the sorted list
        int[] result = new int[k];
        for (int i = 0; i < k; i++) {
            result[i] = frequencyList.get(i)[0];
        }

        return result;
    }
}